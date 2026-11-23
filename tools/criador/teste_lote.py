"""Testa a edição em segundo plano (lote_executar / lote_aplicar) com a engine de verdade, sem janela.

    python tools/criador/teste_lote.py --editor C:/caminho/AnastacioEngine.exe

Cobre: o original nunca muda; resumo do que mudou; passo bloqueado ou com erro não grava nada; saída igual ao
original recusada; projeto aberto num editor recusa o lote e a troca; lote_aplicar guarda backup e troca o arquivo.
"""
import hashlib, json, os, socket, subprocess, sys, tempfile, threading
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
TMP = Path(tempfile.mkdtemp(prefix='teste_lote_'))
os.environ['ANASTACIO_CRIADOR_SESSAO_DIR'] = str(TMP / 'sessao')
os.environ.pop('ANASTACIO_CRIADOR_PY', None)
sys.argv += ['--pasta', str(TMP / 'pasta'), '--editor', EDITOR]
import anastacio_criador_mcp as m  # noqa: E402

falhas = []


def ok(cond, nome):
    print(('ok   ' if cond else 'FALHOU ') + nome)
    if not cond:
        falhas.append(nome)


def hash_de(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def recusa(fn, trecho):
    try:
        fn()
    except Exception as e:
        return trecho in str(e)
    return False


def limpar():
    COPIA.unlink(missing_ok=True)
    m._marca(COPIA).unlink(missing_ok=True)


def falhou(passos, trecho='FALHOU', **kw):
    """O lote deve ser recusado/falhar com `trecho`, sem deixar cópia."""
    try:
        m.lote_executar(str(BASE), passos, **kw)
    except Exception as e:
        return trecho in str(e)
    return False


# projeto base: o da fábrica (Cube, Camera, Lamp) gravado em disco
BASE = TMP / 'base.range'
gerar = TMP / 'gerar.py'
gerar.write_text("import bpy\nbpy.ops.wm.save_as_mainfile(filepath=%r)\n" % str(BASE))
subprocess.run([EDITOR, '-b', '--factory-startup', '--python', str(gerar)], stdout=subprocess.DEVNULL,
               stderr=subprocess.STDOUT, timeout=180)
ok(BASE.exists(), 'projeto base gerado')
h0 = hash_de(BASE)
COPIA = m._copia_do_lote(BASE)

# 1. lote que cria e altera
r = json.loads(m.lote_executar(str(BASE), [
    {'cmd': 'op', 'nome': 'mesh.primitive_cube_add', 'args': {'location': [3, 0, 0]}},
    {'cmd': 'definir', 'caminho': 'bpy.data.objects["Cube"].location', 'valor': [1, 2, 3]},
    {'cmd': 'script_gravar', 'nome': 'andar.py', 'conteudo': 'print("oi")\n'},
]))
ok(hash_de(BASE) == h0, 'o original continua idêntico depois do lote')
ok(COPIA.exists() and hash_de(COPIA) != h0, 'a cópia foi gravada e é diferente')
ok(r['passos'] == 3 and len(r['mudou']['criados']) == 1 and 'Cube' in r['mudou']['alterados'],
   'o resumo mostra o objeto criado e o alterado')
r3 = m.lote_executar(str(BASE), [{'cmd': 'script_gravar', 'nome': 'a.py', 'conteudo': 'x = 1'},
                                 {'cmd': 'script_ligar', 'objeto': 'Cube', 'script': 'a.py'}], saida=str(TMP / 'lig.range'))
ok('"controlador": "Python"' in r3, 'script_ligar funciona no lote, sem janela')
r2 = json.loads(m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy.data.texts'}], saida=str(TMP / 'outra.range')))
print(r2['resultados'])
ok('andar.py' not in r2['resultados'][0], 'a cópia nova parte do original, não da cópia anterior')
ok(Path(r['copia']) == COPIA, 'a cópia fica ao lado do original (nome.ia.range)')
limpar()

# 2. falhas não gravam nada
ok(falhou([{'cmd': 'op', 'nome': 'wm.addon_install'}], 'não cabe num lote'), 'operador de código bloqueado no lote')
ok(hash_de(BASE) == h0, 'lote que falha não deixa mudança no original')
ok(falhou([{'cmd': 'evento', 'tipo': 'A'}], 'não permitido'), 'passo desconhecido recusado')
ok(falhou([{'cmd': 'py', 'codigo': 'resultado = 1'}], 'ANASTACIO_CRIADOR_PY'), 'py continua desligado no lote')
ok(falhou([{'cmd': 'definir', 'caminho': 'bpy.context.user_preferences.filepaths.script_directory', 'valor': 'C:/x'}],
         'dados do projeto'), 'definir fora do projeto bloqueado no lote')
ok(not COPIA.exists() and not m._marca(COPIA).exists(), 'lote que falha apaga a cópia')
ok(recusa(lambda: m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy'}], saida=str(BASE)), 'próprio projeto'),
   'saída igual ao original recusada')
ok(recusa(lambda: m.lote_executar(str(BASE), []), 'lista'), 'lote vazio recusado')
ok(recusa(lambda: m.lote_executar(str(TMP / 'nao_existe.range'), [{'cmd': 'ler', 'caminho': 'bpy'}]), 'não achei'),
   'projeto inexistente recusado')
ok(hash_de(BASE) == h0, 'depois de todas as falhas o original segue idêntico')

# o resumo percebe mudança de material
r4 = json.loads(m.lote_executar(str(BASE), [{'cmd': 'definir', 'caminho': 'bpy.data.materials[0].diffuse_color', 'valor': [0.1, 0.2, 0.3]}],
                                saida=str(TMP / 'mat.range')))
ok(len(r4['mudou']['materiais_alterados']) == 1, 'o resumo mostra o material que mudou de cor')

# 2b. gravar arquivo por operador, saída existente, marca, lote concorrente
for op in ('wm.save_as_mainfile', 'wm.save_mainfile', 'export_scene.obj', 'image.save_as', 'render.render', 'file.unpack_all',
           'wm.link', 'wm.append'):
    ok(falhou([{'cmd': 'op', 'nome': op, 'args': {'filepath': str(BASE)}}], 'não cabe num lote'),
       'operador que grava arquivo bloqueado no lote: ' + op)
ok(hash_de(BASE) == h0, 'nenhum operador conseguiu gravar no original')
ok(m.lote_executar(str(BASE), [{'cmd': 'op', 'nome': 'object.select_all', 'args': {'action': 'DESELECT'}}]) is not None
   and COPIA.exists(), 'lote sem mudanças reais ainda gera cópia')
limpar()
EXISTENTE = TMP / 'meu_outro_projeto.range'
EXISTENTE.write_bytes(b'dados do usuario')
ok(recusa(lambda: m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy'}], saida=str(EXISTENTE)), 'já existe'),
   'saída que já existe é recusada')
ok(EXISTENTE.read_bytes() == b'dados do usuario', 'a saída existente não foi sobrescrita nem apagada')
r = json.loads(m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy.data.texts'}]))
ok(recusa(lambda: m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy'}]), 'já existe'),
   'cópia anterior ainda não aplicada não é sobrescrita por um novo lote')
ok(COPIA.exists(), 'e a cópia anterior continua lá')
(TMP / 'solto.range').write_bytes(b'solto')
ok(recusa(lambda: m.lote_aplicar(str(BASE), str(TMP / 'solto.range')), 'marca'), 'lote_aplicar não aceita arquivo solto')
trava = m._trava(BASE)
with trava:
    ok(recusa(lambda: m.lote_aplicar(str(BASE)), 'lote em andamento'), 'dois lotes no mesmo projeto: o segundo é recusado')
ok(not trava.caminho.exists(), 'a trava é liberada')
BASE.write_bytes(BASE.read_bytes() + b'\x00')  # alguém salvou no original depois do lote
ok(recusa(lambda: m.lote_aplicar(str(BASE)), 'mudou depois do lote'), 'original que mudou depois do lote: a troca é recusada')
BASE.write_bytes(BASE.read_bytes()[:-1])
h0 = hash_de(BASE)
ok(hash_de(BASE) == h0 and COPIA.exists(), 'original restaurado para seguir os testes')
COPIA.unlink()
m._marca(COPIA).unlink()

# editor ligado que não responde: estado incerto, nunca "livre"
sessao.escrever(sessao.sessao_usuario(), {'porta': 1, 'token': 'x', 'pid': os.getpid(),
                                          'programa': sessao.nome_processo(os.getpid())})
ok(recusa(lambda: m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy'}]), 'não respondeu'),
   'editor ligado que não responde: o lote é recusado (estado incerto)')
sessao.sessao_usuario().unlink()
ok(not COPIA.exists(), 'recusa por estado incerto não deixa cópia')

# 3. projeto aberto num editor: recusa lote e troca (editor falso que responde ao ping)
servidor = socket.socket()
servidor.bind(('127.0.0.1', 0))
servidor.listen(2)
parar = threading.Event()


def atender_falso():
    servidor.settimeout(0.3)
    while not parar.is_set():
        try:
            c, _ = servidor.accept()
        except OSError:
            continue
        f = c.makefile('rw', encoding='utf-8')
        linha = f.readline()
        if linha:
            f.write(json.dumps({'ok': True, 'resultado': {'arquivo': str(BASE)}}) + '\n')
            f.flush()
        c.close()


threading.Thread(target=atender_falso, daemon=True).start()
arq_sessao = sessao.sessao_usuario()
sessao.escrever(arq_sessao, {'porta': servidor.getsockname()[1], 'token': 'x', 'pid': os.getpid(),
                             'programa': sessao.nome_processo(os.getpid())})
ok(bool(m.arquivo_em_uso(str(BASE))), 'arquivo_em_uso enxerga o projeto aberto no editor')
ok(recusa(lambda: m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy'}]), 'aberto num editor'),
   'projeto aberto no editor: o lote é recusado')
COPIA.write_bytes(b'copia-de-teste')
m._marca(COPIA).write_text(json.dumps({'original': str(BASE), 'hash_original': h0, 'hash_copia': hash_de(COPIA), 'ident': 'abcdef'}))
ok(recusa(lambda: m.lote_aplicar(str(BASE)), 'aberto num editor'), 'projeto aberto no editor: a troca é recusada')
ok(hash_de(BASE) == h0, 'recusas não mexeram no original')
parar.set()
arq_sessao.unlink()
ok(not m.arquivo_em_uso(str(BASE)), 'depois de fechar, o projeto não está mais em uso')

# 4. aplicar: backup do original e troca
COPIA.unlink(missing_ok=True)
m._marca(COPIA).unlink(missing_ok=True)
m.lote_executar(str(BASE), [{'cmd': 'definir', 'caminho': 'bpy.data.objects["Cube"].location', 'valor': [5, 5, 5]}])
h_copia = hash_de(COPIA)
msg = m.lote_aplicar(str(BASE))
backups = list((TMP / 'base.backups').glob('*-antes-do-lote.range'))
ok(len(backups) == 1 and hash_de(backups[0]) == h0, 'lote_aplicar guarda o original em .backups')
ok(hash_de(BASE) == h_copia and not COPIA.exists(), 'lote_aplicar troca o projeto pela cópia')
ok(not m._marca(COPIA).exists(), 'a marca do lote some depois de aplicar')
ok('Backup' in msg, 'lote_aplicar informa o backup')

print('\n%s' % ('FALHAS: ' + ', '.join(falhas) if falhas else 'todas as verificações passaram'))
sys.exit(1 if falhas else 0)
