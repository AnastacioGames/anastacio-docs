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
  editor_py, jogo_py                        (código livre: desligado, ligue com ANASTACIO_CRIADOR_PY=1)

Onde estão os programas (em ordem): --editor/--runtime, variáveis ANASTACIO_EDITOR/ANASTACIO_RUNTIME,
ou AnastacioEngine/AnastacioRuntime no PATH. O instalador não é adivinhado.

Uso com Claude Code:
  claude mcp add anastacio-criador -- python tools/anastacio_criador_mcp.py --editor "C:/.../AnastacioEngine.exe"

Editor já aberto pelo usuário: ele liga "Controle por IA" (complemento da engine) e o MCP conecta sozinho.
--sessao <arquivo de sessão> aponta para outro arquivo.
"""
import base64
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "criador"))
import caminhos  # noqa: E402
import sessao as sessoes  # noqa: E402

VERSAO = "0.1.0"
AQUI = Path(__file__).resolve().parent
SERVIDOR_EDITOR = AQUI / "criador" / "servidor_editor.py"
SERVIDOR_JOGO = AQUI / "criador" / "servidor_jogo.py"
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


class Conexao:
    """Uma linha JSON por pedido, com token; uma linha JSON por resposta."""

    def __init__(self, arquivo_sessao, timeout=120):
        self.sessao = json.loads(Path(arquivo_sessao).read_text())
        self.socket = socket.create_connection(("127.0.0.1", self.sessao["porta"]), timeout=timeout)
        self.canal = self.socket.makefile("rw", encoding="utf-8")

    def pedir(self, cmd, **dados):
        self.canal.write(json.dumps(dict(dados, cmd=cmd, token=self.sessao["token"])) + "\n")
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


def jogo_abrir(arquivo, largura=1280, altura=720):
    if E.jogo is not None:
        jogo_fechar()
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
    return "jogo aberto"


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
    "jogo_abrir": ("Roda um jogo (.range) no Runtime com janela visível.",
                   {"arquivo": ("string", True), "largura": ("integer", False), "altura": ("integer", False)},
                   lambda a: jogo_abrir(a["arquivo"], a.get("largura", 1280), a.get("altura", 720))),
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
        return {"type": t} if t else {}
    return {"type": "object", "properties": {k: um(t) for k, (t, _) in props.items()},
            "required": [k for k, (_, obrig) in props.items() if obrig]}


def responder(msg):
    m, id_ = msg.get("method"), msg.get("id")
    if m == "initialize":
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
