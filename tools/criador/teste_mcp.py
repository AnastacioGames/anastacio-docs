"""Testa o MCP do criador contra um editor falso que fala o mesmo protocolo (não precisa da engine).

    python tools/criador/teste_mcp.py

Cobre: lista de ferramentas, backup automático só na primeira alteração, caminhos bpy.* sem chamadas,
py desligado por padrão, imagem da tela, erros sem jogo aberto e programa não encontrado.
Não testa o servidor_editor.py dentro do editor de verdade (precisa de bpy).
"""
import json, os, re, socket, subprocess, sys, tempfile, threading
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MCP = RAIZ / "anastacio_criador_mcp.py"
PNG = bytes.fromhex("89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4890000000d49444154789c63f8cfc0f01f0005000201a5f645400000000049454e44ae426082")
chamadas = []


def servidor_falso(pasta):
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen(2)
    token = "tok"
    sessao = pasta / "sessao_editor.json"
    sessao.write_text(json.dumps({"porta": s.getsockname()[1], "token": token, "pid": os.getpid()}))

    def atender(c):
        f = c.makefile("rw", encoding="utf-8")
        for linha in f:
            p = json.loads(linha)
            chamadas.append(p["cmd"])
            cmd = p["cmd"]
            if p.get("token") != token:
                r = {"ok": False, "erro": "token inválido"}
            elif cmd == "ping":
                r = {"ok": True, "resultado": {"versao": 1, "arquivo": "/x/jogo.range", "py_liberado": False}}
            elif cmd == "cena":
                r = {"ok": True, "resultado": {"cena": "Scene", "total": 1, "objetos": [{"nome": "Cubo", "tipo": "MESH"}]}}
            elif cmd == "backup":
                r = {"ok": True, "resultado": {"backup": "/x/jogo.backups/1.range"}}
            elif cmd == "op":
                r = {"ok": True, "resultado": {"estado": ["FINISHED"]}}
            elif cmd in ("ler", "definir"):
                r = {"ok": True, "resultado": [0.0, 0.0, 0.0]}
            elif cmd == "py":
                r = {"ok": True, "resultado": 42}
            elif cmd == "tela":
                Path(p["arquivo"]).write_bytes(PNG)
                r = {"ok": True, "resultado": p["arquivo"]}
            else:
                r = {"ok": False, "erro": "comando desconhecido: " + cmd}
            f.write(json.dumps(r) + "\n")
            f.flush()

    def aceitar():
        while True:
            c, _ = s.accept()
            threading.Thread(target=atender, args=(c,), daemon=True).start()
    threading.Thread(target=aceitar, daemon=True).start()
    return sessao


def rodar_mcp(pasta, pedidos, env_extra=None, extra=()):
    env = dict(os.environ, **(env_extra or {}))
    env.pop("ANASTACIO_EDITOR", None)
    env.pop("ANASTACIO_RUNTIME", None)
    entrada = "\n".join(json.dumps(p) for p in pedidos) + "\n"
    r = subprocess.run([sys.executable, str(MCP), "--pasta", str(pasta), *extra], input=entrada,
                       capture_output=True, text=True, env=env, timeout=60)
    assert r.returncode == 0, r.stderr
    return {json.loads(l)["id"]: json.loads(l) for l in r.stdout.splitlines()}


def chamar(i, ferramenta, **args):
    return {"jsonrpc": "2.0", "id": i, "method": "tools/call", "params": {"name": ferramenta, "arguments": args}}


def texto(r):
    return r["result"]["content"][0].get("text", "")


def main():
    ok = 0

    def checar(cond, msg):
        nonlocal ok
        assert cond, "FALHOU: " + msg
        ok += 1
        print("ok  ", msg)

    with tempfile.TemporaryDirectory() as t:
        pasta = Path(t)
        servidor_falso(pasta)
        r = rodar_mcp(pasta, [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            chamar(3, "cena_descrever"),
            chamar(4, "op_executar", nome="mesh.primitive_cube_add"),
            chamar(5, "op_executar", nome="mesh.primitive_cube_add"),
            chamar(6, "propriedade_ler", caminho='bpy.data.objects["Cubo"].location'),
            chamar(7, "propriedade_ler", caminho='bpy.data.objects.remove(1)'),
            chamar(8, "propriedade_ler", caminho='bpy.__class__'),
            chamar(9, "propriedade_definir", caminho='bpy.data.objects["Cubo"].location[0]', valor=2),
            chamar(10, "editor_py", codigo="resultado = 1"),
            chamar(11, "editor_tela"),
            chamar(12, "jogo_estado"),
            chamar(13, "log_ler"),
            chamar(14, "ferramenta_que_nao_existe"),
        ])
        nomes = [t["name"] for t in r[2]["result"]["tools"]]
        checar({"cena_descrever", "op_executar", "editor_tela", "jogo_abrir", "log_ler"} <= set(nomes), "lista de ferramentas")
        checar("Cubo" in texto(r[3]), "cena_descrever devolve a cena")
        checar("[backup:" in texto(r[4]), "primeira alteração faz backup")
        checar("[backup:" not in texto(r[5]), "segunda alteração não repete o backup")
        checar(chamadas.count("backup") == 1, "backup pedido uma única vez ao editor")
        checar(not r[6]["result"]["isError"], "propriedade_ler aceita caminho bpy válido")
        checar(r[7]["result"]["isError"] and "não permitido" in texto(r[7]), "propriedade_ler recusa chamada")
        checar(r[8]["result"]["isError"], "propriedade_ler recusa __")
        checar(not r[9]["result"]["isError"], "propriedade_definir aceita caminho válido")
        checar(r[10]["result"]["isError"] and "desligado" in texto(r[10]), "editor_py desligado por padrão")
        img = r[11]["result"]["content"][0]
        checar(img["type"] == "image" and img["mimeType"] == "image/png" and len(img["data"]) > 20, "editor_tela devolve imagem")
        checar(r[12]["result"]["isError"] and "nenhum jogo aberto" in texto(r[12]), "jogo_estado sem jogo dá erro claro")
        checar("sem log" in texto(r[13]), "log_ler sem log avisa")
        checar(r[14]["result"]["isError"], "ferramenta desconhecida dá erro")

        r = rodar_mcp(pasta, [chamar(1, "editor_py", codigo="resultado = 1")], {"ANASTACIO_CRIADOR_PY": "1"})
        checar(not r[1]["result"]["isError"] and "42" in texto(r[1]), "editor_py liberado por ANASTACIO_CRIADOR_PY=1")

    with tempfile.TemporaryDirectory() as t2:
        r = rodar_mcp(Path(t2), [chamar(1, "projeto_conectar", projeto="/x/jogo.range")],
                      extra=("--sessao", str(Path(t2) / "nao_existe.json")))
        checar(r[1]["result"]["isError"] and "não achei o AnastacioEngine" in texto(r[1]), "sem programa instalado dá erro claro")

    sys.path.insert(0, str(RAIZ / "criador"))
    import caminhos
    from types import SimpleNamespace as NS
    cubo = NS(location=[0.0, 0.0, 0.0], name="Cubo")
    bpy = NS(data=NS(objects={"Cubo": cubo}, nomes=[1, 2]))
    checar(caminhos.ler('bpy.data.objects["Cubo"].name', bpy) == "Cubo", "caminhos.ler com índice de texto")
    checar(caminhos.definir('bpy.data.objects["Cubo"].location[1]', 5.0, bpy) == 5.0 and cubo.location[1] == 5.0, "caminhos.definir em índice")
    checar(caminhos.definir('bpy.data.objects["Cubo"].name', "Novo", bpy) == "Novo" and cubo.name == "Novo", "caminhos.definir em atributo")
    for ruim in ('bpy.data.nomes.append(3)', 'bpy.data.objects["Cubo"].name + "x"', "bpy.__class__", "os.system", 'bpy["a"; 1]', "bpy"):
        try:
            caminhos.definir(ruim, 1, bpy)
            checar(False, "deveria recusar " + ruim)
        except ValueError:
            checar(True, "recusa " + ruim)
    print(f"\n{ok} verificações passaram")


if __name__ == "__main__":
    main()
