#!/usr/bin/env python3
"""Servidor MCP (stdio) para criar jogos na Anastacio Engine com ajuda de uma IA.

A IA descreve a cena, cria e muda objetos, vê a tela, joga o jogo e lê os erros. O MCP abre o editor
com o seu projeto (janela visível) e conversa com ele por TCP local. Só usa a biblioteca padrão.

Ferramentas (as que mudam o projeto fazem um backup antes, na primeira vez da sessão):
  projeto_conectar, projeto_backup, projeto_salvar
  cena_descrever, objeto_descrever
  op_listar, op_descrever, op_executar
  propriedade_ler, propriedade_definir      (só caminhos bpy.a.b[0]["x"], sem chamadas)
  editor_tela, editor_clicar, editor_tecla, editor_fechar
  jogo_abrir, jogo_estado, jogo_tecla, jogo_soltar, jogo_mouse, jogo_esperar, jogo_tela, jogo_fechar
  log_ler
  arquivo_em_uso, lote_executar, lote_aplicar   (edição em segundo plano numa cópia do .range, sem janela)
  jogo_objetos
  editor_py, jogo_py                        (código livre: desligado, ligue com ANASTACIO_CRIADOR_PY=1)

Onde estão os programas (em ordem): --editor/--runtime, variáveis ANASTACIO_EDITOR/ANASTACIO_RUNTIME,
ou AnastacioEngine/AnastacioRuntime no PATH. O instalador não é adivinhado.

Uso com Claude Code:
  claude mcp add anastacio-criador -- python tools/anastacio_criador_mcp.py --editor "C:/.../AnastacioEngine.exe"

Editor já aberto pelo usuário: ele liga "Controle por IA" (complemento da engine) e o MCP conecta sozinho.
--sessao <arquivo de sessão> aponta para outro arquivo.
"""
import base64
import hashlib
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "criador"))
import caminhos  # noqa: E402
import sessao as sessoes  # noqa: E402

VERSAO = "0.1.0"
AQUI = Path(__file__).resolve().parent
SERVIDOR_EDITOR = AQUI / "criador" / "servidor_editor.py"
SERVIDOR_JOGO = AQUI / "criador" / "servidor_jogo.py"
LOTE_EDITOR = AQUI / "criador" / "lote_editor.py"
PY_LIBERADO = os.environ.get("ANASTACIO_CRIADOR_PY") == "1"


def _arg(nome, padrao=None):
    return sys.argv[sys.argv.index(nome) + 1] if nome in sys.argv else padrao


PASTA = Path(_arg("--pasta") or Path(tempfile.gettempdir()) / "anastacio-criador")
SESSAO_EDITOR = Path(_arg("--sessao") or PASTA / "sessao_editor.json")
SESSAO_USUARIO = sessoes.sessao_usuario()
SESSAO_JOGO = PASTA / "sessao_jogo.json"


def achar_programa(arg, env, nome):
    caminho = _arg(arg) or os.environ.get(env) or shutil.which(nome)
    if not caminho:
        raise RuntimeError(f"não achei o {nome}: informe {arg}, a variável {env} ou ponha no PATH")
    return caminho


CLIENTE = {'nome': ''}  # quem está usando este MCP (vem do initialize); o editor mostra


class Conexao:
    """Uma linha JSON por pedido, com token; uma linha JSON por resposta."""

    def __init__(self, arquivo_sessao, timeout=120):
        self.sessao = json.loads(Path(arquivo_sessao).read_text())
        self.socket = socket.create_connection(("127.0.0.1", self.sessao["porta"]), timeout=timeout)
        self.canal = self.socket.makefile("rw", encoding="utf-8")

    def pedir(self, cmd, **dados):
        self.canal.write(json.dumps(dict(dados, cmd=cmd, token=self.sessao["token"], cliente=CLIENTE["nome"])) + "\n")
        self.canal.flush()
        linha = self.canal.readline()
        if not linha:
            raise ConnectionError(f"o programa fechou, caiu ou o usuário desligou o Controle por IA durante: {cmd}. "
                                  "Peça para ligar de novo no editor e chame projeto_conectar.")
        r = json.loads(linha)
        if not r.get("ok"):
            raise RuntimeError(r.get("erro") or "erro sem mensagem")
        return r.get("resultado")

    def fechar(self):
        try:
            self.socket.close()
        except OSError:
            pass


class Estado:
    editor = None
    jogo = None
    backup_feito = False
    logs = {"editor": None, "jogo": None}
    processos = {"editor": None, "jogo": None}


E = Estado()


def esperar_sessao(arquivo, proc, espera):
    limite = time.time() + espera
    while time.time() < limite:
        if Path(arquivo).exists():
            return
        if proc.poll() is not None:
            raise RuntimeError("o programa fechou ao abrir; veja log_ler")
        time.sleep(0.2)
    raise TimeoutError("o programa não respondeu a tempo; veja log_ler")


def conectar(projeto=None):
    if E.editor is not None:
        try:
            E.editor.pedir("ping")
            return "já conectado"
        except (OSError, ConnectionError, RuntimeError):
            E.editor = None
    PASTA.mkdir(parents=True, exist_ok=True)
    # Um editor que o usuário já abriu com "Controle por IA" ligado (pasta do usuário), ou um nosso anterior.
    for arquivo in (SESSAO_USUARIO, SESSAO_EDITOR):
        if not arquivo.exists():
            continue
        if sessoes.ler(arquivo) is None:  # processo morto: arquivo velho não engana
            arquivo.unlink(missing_ok=True)
            continue
        try:
            c = Conexao(arquivo)
            info = c.pedir("ping")
            E.editor = c
            E.backup_feito = False
            return f"conectado a um editor já aberto (modo {info.get('modo', 'controle')})"
        except (OSError, ConnectionError, RuntimeError, ValueError):
            pass
    editor = achar_programa("--editor", "ANASTACIO_EDITOR", "AnastacioEngine")
    log = PASTA / f"editor_{int(time.time())}.log"
    args = [editor, "--window-geometry", "0", "0", "1500", "900"]
    if projeto:
        args.append(str(Path(projeto).resolve()))
    args += ["--python-exit-code", "1", "--python", str(SERVIDOR_EDITOR), "--", str(SESSAO_EDITOR)]
    env = dict(os.environ, ANASTACIO_EVENT_SIMULATE="1")
    proc = subprocess.Popen(args, env=env, stdout=log.open("w"), stderr=subprocess.STDOUT)
    E.logs["editor"], E.processos["editor"] = log, proc
    esperar_sessao(SESSAO_EDITOR, proc, 90)
    E.editor = Conexao(SESSAO_EDITOR)
    info = E.editor.pedir("ping")
    E.backup_feito = False
    return f"editor aberto: {info.get('arquivo') or '(projeto sem nome)'}"


def editor():
    if E.editor is None:
        conectar()
    return E.editor


def backup(forcar=False):
    if E.backup_feito and not forcar:
        return ""
    r = editor().pedir("backup")
    E.backup_feito = bool(r.get("backup"))
    if r.get("backup"):
        return f"[backup: {r['backup']}] "
    return f"[atenção: {r.get('aviso')}] "


def imagem(caminho):
    dados = base64.b64encode(Path(caminho).read_bytes()).decode()
    return {"type": "image", "data": dados, "mimeType": "image/png"}


def tela_temp(prefixo):
    PASTA.mkdir(parents=True, exist_ok=True)
    return str(PASTA / f"{prefixo}_{int(time.time() * 1000)}.png")


def exigir_py(onde):
    if not PY_LIBERADO:
        raise PermissionError(f"{onde}_py está desligado. Para liberar código livre, inicie o MCP com ANASTACIO_CRIADOR_PY=1")


exigir_caminho = caminhos.exigir


def jogo():
    if E.jogo is None:
        raise RuntimeError("nenhum jogo aberto: use jogo_abrir")
    return E.jogo


def jogo_abrir(arquivo=None, largura=1280, altura=720):
    """Sem `arquivo`, roda uma cópia da cena aberta no editor, com o que ainda não foi salvo."""
    if E.jogo is not None:
        jogo_fechar()
    PASTA.mkdir(parents=True, exist_ok=True)
    aviso = ""
    if not arquivo:
        if E.editor is None:
            raise RuntimeError("informe `arquivo` ou conecte no editor (projeto_conectar) para rodar a cena aberta")
        arquivo = str(PASTA / f"jogo_copia_{int(time.time())}.range")
        E.editor.pedir("copia_para_jogo", arquivo=arquivo)
        aviso = "rodando uma cópia da cena aberta no editor (inclui o que não foi salvo). "
    runtime = achar_programa("--runtime", "ANASTACIO_RUNTIME", "AnastacioRuntime")
    PASTA.mkdir(parents=True, exist_ok=True)
    SESSAO_JOGO.unlink(missing_ok=True)
    log = PASTA / f"jogo_{int(time.time())}.log"
    env = dict(os.environ, RANGE_CONTROL_SCRIPT=str(SERVIDOR_JOGO), RANGE_CONTROL_SESSION=str(SESSAO_JOGO),
               RANGE_NO_CRASH_DIALOG="1")
    args = [runtime, "-w", str(largura), str(altura), "0", "0", str(Path(arquivo).resolve())]
    proc = subprocess.Popen(args, env=env, stdout=log.open("w"), stderr=subprocess.STDOUT)
    E.logs["jogo"], E.processos["jogo"] = log, proc
    esperar_sessao(SESSAO_JOGO, proc, 90)
    E.jogo = Conexao(SESSAO_JOGO)
    return aviso + "jogo aberto"


def jogo_fechar():
    if E.jogo is not None:
        try:
            E.jogo.pedir("fechar")
        except (OSError, ConnectionError, RuntimeError):
            pass
        E.jogo.fechar()
        E.jogo = None
    return "jogo fechado"


def editor_fechar():
    if E.editor is not None:
        try:
            E.editor.canal.write(json.dumps({"cmd": "fechar", "token": E.editor.sessao["token"]}) + "\n")
            E.editor.canal.flush()
        except OSError:
            pass
        E.editor.fechar()
        E.editor = None
    SESSAO_EDITOR.unlink(missing_ok=True)
    return "editor fechado (o projeto não foi salvo por isso; use projeto_salvar antes se quiser)"


def log_ler(qual="editor", linhas=60):
    arq = E.logs.get(qual)
    if not arq or not Path(arq).exists():
        return f"sem log de {qual} nesta sessão (o log só existe se o MCP abriu o programa)"
    texto = Path(arq).read_text(errors="replace").splitlines()
    if qual == "jogo":
        # No Windows o Runtime grava os erros de script neste arquivo, não na saída padrão.
        rt = Path(tempfile.gettempdir()) / "range_runtime.log.txt"
        if rt.exists():
            texto += rt.read_text(errors="replace").splitlines()
    return "\n".join(texto[-max(1, min(int(linhas), 500)):]) or "(log vazio)"


def evento(tipo, valor, x, y, texto=""):
    return editor().pedir("evento", tipo=tipo, valor=valor, x=x, y=y, texto=texto)


def editor_clicar(x, y, botao="LEFTMOUSE"):
    evento("MOUSEMOVE", "NOTHING", x, y)
    time.sleep(0.15)
    evento(botao, "PRESS", x, y)
    time.sleep(0.15)  # o editor precisa tratar cada evento num quadro; juntos, o clique se perde
    r = evento(botao, "RELEASE", x, y)
    time.sleep(0.15)
    return f"clicou em ({x}, {y}): {r}"


def editor_tecla(tecla, x=0, y=0):
    evento(tecla, "PRESS", x, y)
    time.sleep(0.15)
    evento(tecla, "RELEASE", x, y)
    time.sleep(0.15)
    return f"tecla {tecla} enviada"


def _mesmo_arquivo(a, b):
    try:
        return os.path.normcase(os.path.realpath(a)) == os.path.normcase(os.path.realpath(b))
    except (OSError, ValueError):
        return False


def _sha(arquivo):
    h = hashlib.sha256()
    with open(arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def arquivo_em_uso(arquivo):
    """Editores com o Controle por IA ligado (o do usuário ou o nosso) que estão com `arquivo` aberto.

    Lista vazia = nenhum DETECTADO. Um editor sem o Controle por IA ligado não aparece aqui. Se há um editor ligado mas ele não
    responde, o estado é incerto e a função levanta erro em vez de dizer que o arquivo está livre."""
    achados = []
    for sessao_arq in (SESSAO_USUARIO, SESSAO_EDITOR):
        if not Path(sessao_arq).exists() or sessoes.ler(sessao_arq) is None:
            continue
        try:
            c = Conexao(sessao_arq, timeout=5)
            aberto = c.pedir("ping").get("arquivo") or ""
            c.fechar()
        except (OSError, ConnectionError, RuntimeError, ValueError) as e:
            raise RuntimeError(f"há um editor ligado que não respondeu ({e}); não dá para saber se o projeto está aberto. "
                               "Tente de novo ou feche o editor") from e
        if aberto and _mesmo_arquivo(aberto, arquivo):
            achados.append(str(sessao_arq))
    return achados


def _copia_do_lote(arquivo):
    p = Path(arquivo)
    return p.with_name(p.stem + ".ia" + p.suffix)


def _marca(copia):
    c = Path(copia)
    return c.with_name(c.name + ".lote.json")


class _trava:
    """Uma operação de lote por projeto de cada vez (lote_executar e lote_aplicar)."""

    def __init__(self, origem):
        o = Path(origem)
        self.caminho = o.with_name(o.name + ".lote.lock")

    def __enter__(self):
        try:
            if self.caminho.exists() and time.time() - self.caminho.stat().st_mtime > 900:
                self.caminho.unlink()  # trava velha de um MCP que caiu
            self.fd = os.open(str(self.caminho), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise RuntimeError("já há um lote em andamento neste projeto; espere terminar") from None
        return self

    def __exit__(self, *_):
        os.close(self.fd)
        self.caminho.unlink(missing_ok=True)


def _rodar_editor_sem_janela(args, log, espera):
    with open(log, "w") as f:
        proc = subprocess.Popen(args, stdout=f, stderr=subprocess.STDOUT)
        try:
            return proc.wait(timeout=espera)
        except subprocess.TimeoutExpired:
            if sys.platform == "win32":  # derruba o editor e tudo que ele tenha aberto
                subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True)
            else:
                proc.kill()
            proc.wait()
            raise


def lote_executar(arquivo, passos, saida=None, espera=300):
    """Aplica `passos` numa CÓPIA do projeto, num editor sem janela. O original nunca é alterado."""
    origem = Path(arquivo)
    if not origem.is_file() or origem.is_symlink():
        raise FileNotFoundError(f"não achei o projeto (ou é um link): {arquivo}")
    if not isinstance(passos, list) or not passos:
        raise ValueError("passos deve ser uma lista não vazia, ex.: "
                         '[{"cmd":"op","nome":"mesh.primitive_cube_add"},{"cmd":"definir","caminho":"bpy.data.objects[\\"Cube\\"].location","valor":[1,0,0]}]')
    destino = Path(saida) if saida else _copia_do_lote(origem)
    if _mesmo_arquivo(destino, origem):
        raise ValueError("a saída não pode ser o próprio projeto: o lote trabalha numa cópia")
    if destino.exists() or destino.is_symlink() or _marca(destino).exists():
        raise FileExistsError(f"já existe {destino.name}: aplique (lote_aplicar) ou apague a cópia anterior antes de um novo lote")
    PASTA.mkdir(parents=True, exist_ok=True)
    with _trava(origem):
        if arquivo_em_uso(str(origem)):
            raise RuntimeError("este projeto está aberto num editor (podem existir mudanças não salvas). Use a edição ao vivo "
                               "(op_executar, propriedade_definir...) ou feche o arquivo no editor antes de usar o lote")
        hash_origem = _sha(origem)
        ident = uuid.uuid4().hex
        pasta_lote = PASTA / f"lote_{ident}"
        pasta_lote.mkdir()
        spec, resultado, log = pasta_lote / "passos.json", pasta_lote / "resultado.json", pasta_lote / "editor.log"
        spec.write_text(json.dumps(passos), encoding="utf-8")
        E.logs["lote"] = log
        criou = False
        try:
            with open(origem, "rb") as de, open(destino, "xb") as para:  # "x": nunca sobrescreve
                criou = True
                shutil.copyfileobj(de, para)
            editor_exe = achar_programa("--editor", "ANASTACIO_EDITOR", "AnastacioEngine")
            args = [editor_exe, "-b", str(destino), "--python-exit-code", "1", "--python", str(LOTE_EDITOR), "--",
                    str(spec), str(resultado), ident]
            try:
                codigo = _rodar_editor_sem_janela(args, log, espera)
            except subprocess.TimeoutExpired:
                raise TimeoutError(f"o lote passou de {espera} s e foi cancelado; a cópia foi apagada e o original está intacto")
            r = json.loads(resultado.read_text(encoding="utf-8")) if resultado.exists() else {}
            if codigo != 0 or r.get("ident") != ident:
                raise RuntimeError("o editor sem janela não terminou direito (veja log_ler(qual='lote')). O original está intacto")
            if not r.get("ok"):
                raise RuntimeError(f"o lote FALHOU e nada foi gravado: {r.get('erro')} ({r.get('executados', 0)} passos antes). "
                                   "O original está intacto.")
            if _sha(origem) != hash_origem:
                raise RuntimeError("o projeto original mudou enquanto o lote rodava; a cópia foi descartada. Refaça o lote")
            marca = {"original": str(origem.resolve()), "hash_original": hash_origem, "hash_copia": _sha(destino), "ident": ident}
            _marca(destino).write_text(json.dumps(marca), encoding="utf-8")
            criou = False  # a cópia agora é o resultado entregue
        except BaseException:
            if criou:
                destino.unlink(missing_ok=True)
            raise
    return js({"copia": str(destino), "original_intacto": str(origem), "passos": r["executados"],
               "mudou": r["mudou"], "resultados": r["resultados"],
               "proximo": "Mostre o resumo ao usuário. Só com a aprovação dele, chame lote_aplicar para trocar o original pela cópia "
                          "(com backup)."})


def lote_aplicar(arquivo, copia=None):
    """Troca o projeto pela cópia que lote_executar gerou, guardando antes um backup. Só com aprovação do usuário."""
    origem = Path(arquivo)
    nova = Path(copia) if copia else _copia_do_lote(origem)
    if not origem.is_file() or origem.is_symlink() or not nova.is_file() or nova.is_symlink():
        raise FileNotFoundError("projeto ou cópia do lote não encontrados")
    if not _marca(nova).is_file():
        raise PermissionError("esta cópia não foi gerada por lote_executar (falta a marca do lote); não aplico arquivos soltos")
    marca = json.loads(_marca(nova).read_text(encoding="utf-8"))
    if not _mesmo_arquivo(marca.get("original", ""), origem):
        raise PermissionError("esta cópia foi gerada a partir de outro projeto")
    with _trava(origem):
        if arquivo_em_uso(str(origem)):
            raise RuntimeError("o projeto está aberto num editor: feche-o (ou salve e feche) antes de trocar o arquivo, "
                               "para não perder o que há lá")
        if _sha(origem) != marca["hash_original"]:
            raise RuntimeError("o projeto mudou depois do lote (alguém salvou nele); refaça o lote para não perder essas mudanças")
        if _sha(nova) != marca["hash_copia"]:
            raise RuntimeError("a cópia do lote foi alterada depois de gerada; refaça o lote")
        pasta = origem.with_name(origem.stem + ".backups")
        pasta.mkdir(exist_ok=True)
        bk = pasta / (time.strftime("%Y%m%d-%H%M%S") + "-" + marca["ident"][:6] + "-antes-do-lote" + origem.suffix)
        with open(origem, "rb") as de, open(bk, "xb") as para:  # "x": nunca sobrescreve um backup
            shutil.copyfileobj(de, para)
        if _sha(bk) != marca["hash_original"]:
            bk.unlink(missing_ok=True)
            raise RuntimeError("o backup não confere com o original; nada foi trocado")
        os.replace(str(nova), str(origem))  # troca atômica (a cópia fica ao lado do projeto, no mesmo volume)
        _marca(nova).unlink(missing_ok=True)
    return f"projeto atualizado com o resultado do lote. Backup do original: {bk}"


def pedir_liberacao(motivo, espera=60):
    """Mostra o aviso no editor e espera o clique do usuário (permitir/negar/expirar)."""
    r = editor().pedir("pedir_liberacao", motivo=motivo)
    fim = time.time() + espera
    while r.get("estado") == "pendente" and time.time() < fim:
        time.sleep(1)
        r = editor().pedir("resposta_pedido")
    estado = r.get("estado") or "expirou"
    if estado == "permitido":
        return "o usuário liberou a edição; pode continuar"
    if estado == "negado":
        return "o usuário NEGOU a edição. Não insista nem tente outro caminho; pergunte o que ele prefere. " + r.get("aviso", "")
    return "sem resposta do usuário (expirou). Peça a ele para clicar em Liberar edição, ou tente de novo mais tarde."


def mutar(texto_ou_fn):
    aviso = backup()
    resultado = texto_ou_fn()
    return aviso + (resultado if isinstance(resultado, str) else json.dumps(resultado, ensure_ascii=False))


def js(valor):
    return json.dumps(valor, ensure_ascii=False, indent=1)


# nome: (descrição, {param: (tipo, obrigatório)}, função(args) -> str | dict de imagem+texto)
F = {
    "projeto_conectar": ("Abre o editor com o projeto (ou conecta a um já aberto). Informe `projeto` com o caminho do arquivo.",
                         {"projeto": ("string", False)}, lambda a: conectar(a.get("projeto"))),
    "projeto_backup": ("Grava uma cópia do projeto em <projeto>.backups/ agora.",
                       {}, lambda a: js(editor().pedir("backup"))),
    "projeto_salvar": ("Salva o projeto aberto no arquivo dele.", {}, lambda a: "salvo: " + str(editor().pedir("salvar"))),
    "cena_descrever": ("Lista os objetos da cena atual (nome, tipo, posição, rotação, escala, pai) e a câmera.",
                       {}, lambda a: js(editor().pedir("cena"))),
    "objeto_descrever": ("Detalhes de um objeto: propriedades de jogo, materiais e filhos.",
                         {"nome": ("string", True)}, lambda a: js(editor().pedir("objeto", nome=a["nome"]))),
    "op_listar": ("Lista operadores do editor (ex.: mesh.primitive_cube_add). `filtro` é um trecho do nome.",
                  {"filtro": ("string", False), "limite": ("integer", False)},
                  lambda a: "\n".join(editor().pedir("listar", filtro=a.get("filtro", ""), limite=a.get("limite", 100)))),
    "op_descrever": ("Descreve um operador e os parâmetros dele.",
                     {"nome": ("string", True)}, lambda a: js(editor().pedir("descrever", nome=a["nome"]))),
    "op_executar": ("Executa um operador do editor. Faz backup do projeto antes, na primeira alteração.",
                    {"nome": ("string", True), "args": ("object", False), "editor": ("string", False), "modo": ("string", False)},
                    lambda a: mutar(lambda: js(editor().pedir("op", nome=a["nome"], args=a.get("args") or {},
                                                              editor=a.get("editor"), modo=a.get("modo"))))),
    "propriedade_ler": ("Lê uma propriedade por caminho, ex.: bpy.data.objects[\"Cubo\"].location (sem chamadas).",
                        {"caminho": ("string", True)}, lambda a: (exigir_caminho(a["caminho"]),
                                                                  js(editor().pedir("ler", caminho=a["caminho"])))[1]),
    "arquivo_em_uso": ("Diz se o arquivo está aberto num editor com o Controle por IA ligado (o do usuário ou o do MCP). Um editor SEM o "
                       "Controle por IA não é detectado: se houver dúvida, pergunte ao usuário. Aberto = edição ao vivo; "
                       "fechado = lote (lote_executar).",
                       {"arquivo": ("string", True)},
                       lambda a: js({"aberto_em_editor": bool(arquivo_em_uso(a["arquivo"]))})),
    "lote_executar": ("Edição em segundo plano: aplica uma lista de `passos` numa CÓPIA do .range (nome.ia.range) num editor "
                      "sem janela. O original nunca é alterado e nada é gravado se um passo falhar. Passos: "
                      '{"cmd":"op","nome":"mesh.primitive_cube_add","args":{}}, {"cmd":"definir","caminho":"bpy.data.objects[\"Cube\"].location","valor":[1,0,0]}, '
                      '{"cmd":"script_gravar","nome":"x.py","conteudo":"..."}, {"cmd":"ler","caminho":"..."}. Mesmas proteções do '
                      "editor ao vivo. Recusa se o projeto estiver aberto num editor. Bom para mudanças repetitivas ou em "
                      "quantidade; para o que precisa ser visto na tela, use a edição ao vivo.",
                      {"arquivo": ("string", True), "passos": ("array", True), "saida": ("string", False)},
                      lambda a: lote_executar(a["arquivo"], a["passos"], a.get("saida"))),
    "lote_aplicar": ("Troca o projeto pela cópia gerada por lote_executar, guardando um backup do original em "
                     "<projeto>.backups/. Chame SÓ depois de mostrar o resumo ao usuário e ele aprovar.",
                     {"arquivo": ("string", True), "copia": ("string", False)},
                     lambda a: lote_aplicar(a["arquivo"], a.get("copia"))),
    "pedir_liberacao": ("Em modo só observar, mostra um aviso no editor pedindo ao usuário para liberar a edição e espera a "
                        "resposta (até 60 s). Só o clique do usuário libera. Dê o motivo em uma frase.",
                        {"motivo": ("string", True)}, lambda a: pedir_liberacao(a["motivo"])),
    "script_gravar": ("Cria um script (texto do projeto) pelo nome e grava o conteúdo (código do jogo com `Range`, não `bpy`). "
                      "Só grava, não executa. Recusa se o nome já existe; `sobrescrever` só com autorização do usuário. "
                      "Use esta ferramenta, nunca os operadores text.* do editor.",
                      {"nome": ("string", True), "conteudo": ("string", True), "sobrescrever": ("boolean", False)},
                      lambda a: mutar(lambda: js(editor().pedir("script_gravar", nome=a["nome"], conteudo=a["conteudo"],
                                                                sobrescrever=bool(a.get("sobrescrever")))))),
    "script_ligar": ("Liga um script já criado a um objeto (sensor Always + controlador Python em modo Script), "
                     "para ele rodar todo quadro no jogo.",
                     {"objeto": ("string", True), "script": ("string", True)},
                     lambda a: mutar(lambda: js(editor().pedir("script_ligar", objeto=a["objeto"], script=a["script"])))),
    "propriedade_definir": ("Define uma propriedade por caminho. Faz backup antes, na primeira alteração.",
                            {"caminho": ("string", True), "valor": (None, True)},
                            lambda a: (exigir_caminho(a["caminho"]),
                                       mutar(lambda: js(editor().pedir("definir", caminho=a["caminho"], valor=a["valor"]))))[1]),
    "editor_tela": ("Imagem da janela do editor. `editor` opcional: VIEW_3D, LOGIC_EDITOR, TEXT_EDITOR...",
                    {"editor": ("string", False)}, "IMAGEM_EDITOR"),
    "editor_clicar": ("Clique no editor em coordenadas do print (x, y do canto superior esquerdo).",
                      {"x": ("integer", True), "y": ("integer", True), "botao": ("string", False)},
                      lambda a: editor_clicar(a["x"], a["y"], a.get("botao", "LEFTMOUSE"))),
    "editor_tecla": ("Aperta uma tecla no editor, com o mouse em (x, y).",
                     {"tecla": ("string", True), "x": ("integer", False), "y": ("integer", False)},
                     lambda a: editor_tecla(a["tecla"], a.get("x", 0), a.get("y", 0))),
    "editor_fechar": ("Fecha o editor sem salvar.", {}, lambda a: editor_fechar()),
    "editor_py": ("Executa Python livre no editor (variável `resultado` é devolvida). Desligado por padrão.",
                  {"codigo": ("string", True)},
                  lambda a: (exigir_py("editor"), mutar(lambda: js(editor().pedir("py", codigo=a["codigo"]))))[1]),
    "jogo_abrir": ("Roda o jogo no Runtime com janela visível. Sem `arquivo`, roda uma cópia da cena aberta no editor "
                   "(com as mudanças ainda não salvas); com `arquivo`, roda o .range do disco.",
                   {"arquivo": ("string", False), "largura": ("integer", False), "altura": ("integer", False)},
                   lambda a: jogo_abrir(a.get("arquivo"), a.get("largura", 1280), a.get("altura", 720))),
    "jogo_objetos": ("Posição, rotação e escala dos objetos do jogo rodando (`filtro` por nome). Use para conferir "
                     "que algo se moveu depois de apertar uma tecla.",
                     {"filtro": ("string", False)}, lambda a: js(jogo().pedir("objetos", filtro=a.get("filtro", "")))),
    "jogo_estado": ("Frame, FPS, cenas, objetos e câmera do jogo rodando.", {}, lambda a: js(jogo().pedir("estado"))),
    "jogo_tecla": ("Aperta uma tecla no jogo (W, SPACE, LEFTMOUSE...) por `frames` quadros; `segurar` mantém.",
                   {"tecla": ("string", True), "frames": ("integer", False), "segurar": ("boolean", False)},
                   lambda a: js(jogo().pedir("tecla", tecla=a["tecla"], frames=a.get("frames", 2), segurar=a.get("segurar", False)))),
    "jogo_soltar": ("Solta uma tecla segurada.", {"tecla": ("string", True)},
                    lambda a: js(jogo().pedir("soltar", tecla=a["tecla"]))),
    "jogo_mouse": ("Move o mouse no jogo (pixels da janela, de cima para baixo).",
                   {"x": ("integer", True), "y": ("integer", True)}, lambda a: js(jogo().pedir("mouse", x=a["x"], y=a["y"]))),
    "jogo_esperar": ("Espera alguns quadros do jogo e devolve o frame.", {"frames": ("integer", False)},
                     lambda a: js(jogo().pedir("esperar", frames=a.get("frames", 1)))),
    "jogo_tela": ("Imagem do jogo rodando.", {}, "IMAGEM_JOGO"),
    "jogo_py": ("Executa Python livre no jogo. Desligado por padrão.", {"codigo": ("string", True)},
                lambda a: (exigir_py("jogo"), js(jogo().pedir("py", codigo=a["codigo"])))[1]),
    "jogo_fechar": ("Fecha o jogo.", {}, lambda a: jogo_fechar()),
    "log_ler": ("Últimas linhas do log do editor ou do jogo (erros de script aparecem aqui).",
                {"qual": ("string", False), "linhas": ("integer", False)},
                lambda a: log_ler(a.get("qual", "editor"), a.get("linhas", 60))),
}


def chamar(nome, args):
    if nome not in F:
        return [{"type": "text", "text": f"Ferramenta desconhecida: {nome}"}], True
    fn = F[nome][2]
    if fn == "IMAGEM_EDITOR":
        arq = tela_temp("editor")
        editor().pedir("tela", arquivo=arq, editor=args.get("editor"))
        return [imagem(arq)], False
    if fn == "IMAGEM_JOGO":
        arq = tela_temp("jogo")
        jogo().pedir("tela", arquivo=arq)
        return [imagem(arq)], False
    return [{"type": "text", "text": fn(args)}], False


def esquema(props):
    def um(t):
        if t == "array":
            return {"type": "array", "items": {"type": "object"}}
        return {"type": t} if t else {}
    return {"type": "object", "properties": {k: um(t) for k, (t, _) in props.items()},
            "required": [k for k, (_, obrig) in props.items() if obrig]}


def responder(msg):
    m, id_ = msg.get("method"), msg.get("id")
    if m == "initialize":
        CLIENTE["nome"] = str((msg.get("params", {}).get("clientInfo") or {}).get("name") or "")
        return {"protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {}}, "serverInfo": {"name": "anastacio-criador", "version": VERSAO}}
    if m == "tools/list":
        return {"tools": [{"name": n, "description": d, "inputSchema": esquema(p)} for n, (d, p, _) in F.items()]}
    if m == "tools/call":
        try:
            conteudo, erro = chamar(msg["params"]["name"], msg["params"].get("arguments") or {})
        except Exception as e:  # erro de programa, de rede ou de permissão vira resposta, não derruba o servidor
            conteudo, erro = [{"type": "text", "text": f"Erro: {e}"}], True
        return {"content": conteudo, "isError": erro}
    if m == "ping":
        return {}
    raise NotImplementedError(m)


def main():
    for linha in sys.stdin:
        linha = linha.strip()
        if not linha:
            continue
        try:
            msg = json.loads(linha)
        except ValueError:
            continue
        if "id" not in msg:
            continue
        try:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "result": responder(msg)}
        except NotImplementedError:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32601, "message": "Method not found"}}
        except Exception as e:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32603, "message": str(e)}}
        sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    jogo_fechar()


if __name__ == "__main__":
    main()
