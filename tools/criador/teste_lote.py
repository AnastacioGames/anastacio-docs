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

# 2. falhas não gravam nada
ok(m.lote_executar(str(BASE), [{'cmd': 'op', 'nome': 'wm.addon_install'}]).startswith('o lote FALHOU'),
   'operador de código bloqueado no lote')
ok(not COPIA.exists() or hash_de(BASE) == h0, 'lote que falha não deixa mudança no original')
ok(m.lote_executar(str(BASE), [{'cmd': 'evento', 'tipo': 'A'}]).startswith('o lote FALHOU'), 'passo desconhecido recusado')
txt = m.lote_executar(str(BASE), [{'cmd': 'py', 'codigo': 'resultado = 1'}])
ok(txt.startswith('o lote FALHOU') and 'ANASTACIO_CRIADOR_PY' in txt, 'py continua desligado no lote')
txt = m.lote_executar(str(BASE), [{'cmd': 'definir', 'caminho': 'bpy.context.user_preferences.filepaths.script_directory',
                                   'valor': 'C:/x'}])
ok(txt.startswith('o lote FALHOU'), 'definir fora do projeto bloqueado no lote')
ok(not COPIA.exists(), 'lote que falha apaga a cópia')
ok(recusa(lambda: m.lote_executar(str(BASE), [{'cmd': 'ler', 'caminho': 'bpy'}], saida=str(BASE)), 'próprio projeto'),
   'saída igual ao original recusada')
ok(recusa(lambda: m.lote_executar(str(BASE), []), 'lista'), 'lote vazio recusado')
ok(recusa(lambda: m.lote_executar(str(TMP / 'nao_existe.range'), [{'cmd': 'ler', 'caminho': 'bpy'}]), 'não achei'),
   'projeto inexistente recusado')
ok(hash_de(BASE) == h0, 'depois de todas as falhas o original segue idêntico')

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
ok(recusa(lambda: m.lote_aplicar(str(BASE)), 'aberto num editor'), 'projeto aberto no editor: a troca é recusada')
ok(hash_de(BASE) == h0, 'recusas não mexeram no original')
parar.set()
arq_sessao.unlink()
ok(not m.arquivo_em_uso(str(BASE)), 'depois de fechar, o projeto não está mais em uso')

# 4. aplicar: backup do original e troca
COPIA.unlink(missing_ok=True)
m.lote_executar(str(BASE), [{'cmd': 'definir', 'caminho': 'bpy.data.objects["Cube"].location', 'valor': [5, 5, 5]}])
h_copia = hash_de(COPIA)
msg = m.lote_aplicar(str(BASE))
backups = list((TMP / 'base.backups').glob('*-antes-do-lote.range'))
ok(len(backups) == 1 and hash_de(backups[0]) == h0, 'lote_aplicar guarda o original em .backups')
ok(hash_de(BASE) == h_copia and not COPIA.exists(), 'lote_aplicar troca o projeto pela cópia')
ok('Backup' in msg, 'lote_aplicar informa o backup')

print('\n%s' % ('FALHAS: ' + ', '.join(falhas) if falhas else 'todas as verificações passaram'))
sys.exit(1 if falhas else 0)
