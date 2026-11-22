"""Testa o addon "Controle por IA" e o núcleo do editor com a engine de verdade (abre uma janela).

    python tools/criador/teste_editor.py --editor C:/caminho/AnastacioEngine.exe [--scripts <pasta com addons/>]

Sem --scripts usa o addon instalado na engine (2.79/scripts/addons). Usa uma pasta de sessão própria
(ANASTACIO_CRIADOR_SESSAO_DIR), então não mexe no editor que você tenha aberto.
Cobre: observar bloqueia escrita e troca de layout; liberar; operadores de código e `definir` fora do projeto
bloqueados; cliente que aborta; conexão travada substituída pela nova; `fechar` só desliga; arquivo de sessão
de PID reaproveitado ignorado; segundo editor recusado.
"""
import json, os, socket, subprocess, sys, tempfile, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent))
import sessao  # noqa: E402


def arg(nome):
    return sys.argv[sys.argv.index(nome) + 1] if nome in sys.argv else None


EDITOR = arg('--editor') or os.environ.get('ANASTACIO_EDITOR')
if not EDITOR:
    sys.exit('informe --editor ou ANASTACIO_EDITOR')
TMP = Path(tempfile.mkdtemp(prefix='teste_controle_ia_'))
os.environ['ANASTACIO_CRIADOR_SESSAO_DIR'] = str(TMP / 'sessao')
import anastacio_criador_mcp as m  # noqa: E402  (lê o ambiente acima)

FLAG = TMP / 'liberar.flag'
BOOT = TMP / 'boot.py'
BOOT.write_text(f'''
import bpy, addon_utils, os
n = [0]
def f(_c):
    n[0] += 1
    if n[0] == 3:
        addon_utils.enable('anastacio_controle_ia')
        bpy.ops.wm.anastacio_ia_ligar()
    if n[0] > 3 and os.path.exists({str(FLAG)!r}):
        os.remove({str(FLAG)!r})
        bpy.ops.wm.anastacio_ia_liberar()
bpy.app.handlers.scene_update_post.append(f)
''')

falhas = []


def ok(cond, nome):
    print(('ok   ' if cond else 'FALHOU ') + nome)
    if not cond:
        falhas.append(nome)


def recusa(fn, trecho):
    try:
        fn()
    except Exception as e:
        return trecho in str(e)
    return False


def abrir(extra_env=None):
    env = dict(os.environ, ANASTACIO_EVENT_SIMULATE='1')
    env.pop('ANASTACIO_CRIADOR_PY', None)
    if arg('--scripts'):
        env['BLENDER_USER_SCRIPTS'] = arg('--scripts')
    return subprocess.Popen([EDITOR, '--window-geometry', '0', '0', '1200', '700', '--python', str(BOOT)],
                            env=env, stdout=(TMP / 'editor.log').open('a'), stderr=subprocess.STDOUT)


def esperar(cond, segundos, msg):
    fim = time.time() + segundos
    while time.time() < fim:
        if cond():
            return True
        time.sleep(0.3)
    print('tempo esgotado:', msg)
    return False


proc = abrir()
try:
    arq = sessao.sessao_usuario()
    ok(esperar(lambda: sessao.ler(arq), 90, 'sessão do editor'), 'liga e escreve a sessão na pasta do usuário')
    c = m.Conexao(arq)
    ok(c.pedir('ping')['modo'] == 'observar', 'começa em só observar')
    ok(c.pedir('cena')['cena'], 'observar permite ler a cena')
    ok(recusa(lambda: c.pedir('op', nome='object.select_all', args={'action': 'DESELECT'}), 'observar'), 'observar recusa op')
    ok(recusa(lambda: c.pedir('evento', tipo='MOUSEMOVE', valor='NOTHING', x=10, y=10), 'observar'), 'observar recusa evento')
    ok(recusa(lambda: c.pedir('fechar'), 'observar'), 'observar recusa fechar')
    ok(recusa(lambda: c.pedir('tela', arquivo=str(TMP / 'x.png'), editor='NODE_EDITOR'), 'layout'),
       'observar não troca o layout para a tela')
    ok(os.path.exists(c.pedir('tela', arquivo=str(TMP / 't.png'))), 'observar permite a tela da área já aberta')

    FLAG.write_text('1')
    ok(esperar(lambda: c.pedir('ping')['modo'] == 'controle', 30, 'liberar'), 'liberar muda para controle')
    ok(c.pedir('op', nome='object.select_all', args={'action': 'DESELECT'})['estado'] == ['FINISHED'], 'controle permite op')
    ok(recusa(lambda: c.pedir('op', nome='script.python_file_run', args={'filepath': 'x.py'}), 'ANASTACIO_CRIADOR_PY'),
       'operador que roda código bloqueado')
    ok(recusa(lambda: c.pedir('op', nome='wm.addon_install'), 'ANASTACIO_CRIADOR_PY'), 'wm.addon_install bloqueado')
    ok(recusa(lambda: c.pedir('definir', caminho='bpy.context.user_preferences.filepaths.script_directory', valor='C:/x'),
              'dados do projeto'), 'definir em preferências bloqueado')
    ok(c.pedir('definir', caminho='bpy.context.scene.frame_current', valor=7) == 7, 'definir em dados da cena passa')
    ok(recusa(lambda: c.pedir('py', codigo='resultado = 1'), 'ANASTACIO_CRIADOR_PY'), 'py continua desligado')

    # scripts: criar, não sobrescrever, ligar, e text.* do editor nunca
    r = c.pedir('script_gravar', nome='andar.py', conteudo='print("oi")\n')
    ok(r['criado'] and r['script'] == 'andar.py', 'script_gravar cria o script')
    ok(c.pedir('script_gravar', nome='andar.py', conteudo='print("v2")\n')['criado'] is False,
       'script_gravar regrava sem pedir um script que a IA criou na sessão')
    c.pedir('op', nome='text.new', editor='TEXT_EDITOR')
    nome_alheio = [n for n in c.pedir('ler', caminho='bpy.data.texts') if n != 'andar.py'][0]
    ok(recusa(lambda: c.pedir('script_gravar', nome=nome_alheio, conteudo='x'), 'não foi criado por você'),
       'script_gravar não sobrescreve script alheio sem autorização')
    ok(c.pedir('script_gravar', nome=nome_alheio, conteudo='x', sobrescrever=True)['criado'] is False,
       'script_gravar sobrescreve alheio quando autorizado')
    ok(recusa(lambda: c.pedir('script_gravar', nome='../x', conteudo='x'), 'inválido'), 'nome de script inválido recusado')
    ok(recusa(lambda: c.pedir('op', nome='text.insert', args={'text': 'x'}), 'script_gravar'), 'text.insert bloqueado')
    obj = c.pedir('cena')['objetos'][0]['nome']
    lig = c.pedir('script_ligar', objeto=obj, script='andar.py')
    ok(lig.get('controlador'), 'script_ligar cria sensor e controlador')
    ok(c.pedir('script_ligar', objeto=obj, script='andar.py').get('aviso'), 'script_ligar não duplica')

    copia = TMP / 'copia.range'
    c.pedir('copia_para_jogo', arquivo=str(copia))
    ok(copia.exists() and copia.stat().st_size > 0, 'copia_para_jogo grava a cena atual sem trocar o arquivo aberto')

    # cliente que pede e some sem ler
    info = json.loads(arq.read_text())
    s = socket.create_connection(('127.0.0.1', info['porta']))
    s.sendall((json.dumps({'cmd': 'cena', 'token': info['token']}) + '\n').encode())
    s.close()
    time.sleep(1)
    c2 = m.Conexao(arq)
    ok(c2.pedir('ping')['modo'] == 'controle', 'servidor segue depois de cliente que aborta (nova conexão assume)')
    # conexão parada (sem fechar) não prende a vaga: a nova assume
    parada = socket.create_connection(('127.0.0.1', info['porta']))
    time.sleep(0.5)
    c3 = m.Conexao(arq)
    ok(c3.pedir('ping')['arquivo'] is not None, 'conexão travada não prende a vaga')
    parada.close()

    # fechar num editor do usuário só desliga o controle
    try:
        c3.pedir('fechar')
    except ConnectionError:  # desligar fecha a conexão antes de responder
        pass
    esperar(lambda: not arq.exists(), 10, 'sessão apagada')
    ok(proc.poll() is None, 'fechar não mata o editor do usuário')
    ok(not arq.exists(), 'desligar apaga a sessão')

    # PID reaproveitado: sessão com pid vivo (este processo) mas nome de programa diferente é velha
    falso = TMP / 'falso.json'
    falso.write_text(json.dumps({'porta': 1, 'token': 'x', 'pid': os.getpid(), 'programa': 'outro-programa.exe'}))
    ok(sessao.ler(falso) is None, 'sessão de PID reaproveitado é ignorada')
    falso.write_text(json.dumps({'porta': 1, 'token': 'x', 'pid': os.getpid(),
                                 'programa': sessao.nome_processo(os.getpid())}))
    ok(sessao.ler(falso) is not None, 'sessão do próprio programa vale')
finally:
    proc.kill()

# segundo editor recusa ligar quando o primeiro está ligado
proc1 = abrir()
try:
    ok(esperar(lambda: sessao.ler(sessao.sessao_usuario()), 90, 'sessão do primeiro'), 'primeiro editor liga de novo')
    antes = json.loads(sessao.sessao_usuario().read_text())
    proc2 = abrir()
    time.sleep(25)
    depois = json.loads(sessao.sessao_usuario().read_text())
    ok(antes == depois, 'segundo editor não sobrescreve a sessão do primeiro')
    proc2.kill()
finally:
    proc1.kill()

print('\n%s' % ('FALHAS: ' + ', '.join(falhas) if falhas else 'todas as verificações passaram'))
sys.exit(1 if falhas else 0)
