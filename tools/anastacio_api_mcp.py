#!/usr/bin/env python3
"""Servidor MCP (stdio) com a referência da API Python da Anastacio Engine.

Dá à IA consulta por partes em vez de um arquivo de 450 KB. Só usa a biblioteca padrão.

Ferramentas:
  api_guia()                       regras da engine e armadilhas (leia primeiro)
  api_indice()                     uma linha por classe/módulo
  api_buscar(consulta, limite)     acha itens por nome ou descrição
  api_pagina(nome, parte)          página de uma classe/módulo (parte: props|funcs|consts)
  api_item(nome, pagina)           descrição completa de um item

Fonte dos dados (pasta api-ia/<lang>/ gerada por tools/gerar_api_ia.py), em ordem:
  --fonte <pasta ou URL>  |  variável ANASTACIO_API_FONTE  |  pasta site/public/api-ia/<lang> deste repo
  --lang pt|en  (padrão pt)

Uso com Claude Code:
  claude mcp add anastacio-api -- python tools/anastacio_api_mcp.py --lang pt
Com a doc publicada (sem clonar o repositório):
  claude mcp add anastacio-api -- python tools/anastacio_api_mcp.py --fonte https://anastaciogames.github.io/anastacio-docs/api-ia/pt/
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

VERSAO = "0.1.0"


def _arg(nome, padrao=None):
    if nome in sys.argv:
        return sys.argv[sys.argv.index(nome) + 1]
    return padrao


LANG = _arg("--lang", "pt")
PADRAO = Path(__file__).resolve().parents[1] / "site" / "public" / "api-ia" / LANG
FONTE = _arg("--fonte") or os.environ.get("ANASTACIO_API_FONTE") or str(PADRAO)
GUIA = "GUIA.md" if LANG == "pt" else "GUIDE.md"
_cache = {}


def ler(rel):
    """Lê um arquivo da fonte (pasta local ou URL), com cache em memória."""
    if rel in _cache:
        return _cache[rel]
    if re.match(r"^https?://", FONTE):
        url = FONTE.rstrip("/") + "/" + rel.replace(" ", "%20")
        with urllib.request.urlopen(url, timeout=30) as r:
            texto = r.read().decode("utf-8")
    else:
        texto = (Path(FONTE) / rel).read_text(encoding="utf-8")
    _cache[rel] = texto
    return texto


def busca_json():
    return json.loads(ler("busca.json"))


def pontuar(item, termos):
    nome, res = item["nome"].lower(), item["resumo"].lower()
    pont = 0
    for t in termos:
        if nome == t:
            pont += 100
        elif nome.startswith(t):
            pont += 40
        elif t in nome:
            pont += 25
        elif t in item["pagina"].lower():
            pont += 8
        if t in res:
            pont += 5
    return pont


def api_buscar(consulta, limite=10):
    termos = [t for t in re.split(r"[\s.,()]+", consulta.lower()) if t]
    if not termos:
        return "Consulta vazia."
    achados = sorted(((pontuar(i, termos), i) for i in busca_json()), key=lambda x: -x[0])
    achados = [i for p, i in achados if p > 0][: max(1, min(int(limite), 30))]
    if not achados:
        return f"Nada encontrado para '{consulta}'. Esse nome provavelmente não existe na API."
    return "\n".join(f"- {i['pagina']}.{i['assinatura']} [{i['tipo']}] {i['resumo']}  ({i['arquivo']})"
                     for i in achados)


def api_pagina(nome, parte=""):
    paginas = {i["pagina"] for i in busca_json()}
    alvo = next((p for p in paginas if p.lower() == nome.lower()), None)
    if not alvo:
        sug = sorted(p for p in paginas if nome.lower() in p.lower())[:10]
        return f"Página '{nome}' não existe." + (f" Parecidas: {', '.join(sug)}" if sug else "")
    arq = f"paginas/{alvo}--{parte}.md" if parte in ("props", "funcs", "consts") else f"paginas/{alvo}.md"
    try:
        return ler(arq)
    except Exception:
        return f"Parte '{parte}' não existe em {alvo}. Abra a página sem 'parte' para ver as partes."


def api_item(nome, pagina=""):
    itens = [i for i in busca_json() if i["nome"].lower() == nome.lower()
             and (not pagina or i["pagina"].lower() == pagina.lower())]
    if not itens:
        return f"Item '{nome}' não existe na API." + (" Use api_buscar para nomes parecidos.")
    saida = []
    for i in itens[:5]:
        texto = ler(i["arquivo"])
        m = re.search(r"^#{1,3} " + re.escape(i["assinatura"]) + r"\s*\n(.*?)(?=^#{1,3} |\Z)",
                      texto, re.S | re.M)
        corpo = m.group(1).strip() if m else i["resumo"]
        saida.append(f"## {i['pagina']}.{i['assinatura']}\n\n{corpo}")
    return "\n\n".join(saida)


FERRAMENTAS = {
    "api_guia": ("Regras da Anastacio Engine e armadilhas comuns. Leia antes de escrever código.",
                 {}, lambda a: ler(GUIA)),
    "api_indice": ("Índice: uma linha por classe/módulo da API Python.", {}, lambda a: ler("INDEX.md")),
    "api_buscar": ("Busca itens da API por nome ou descrição. Se nada for achado, o nome não existe.",
                   {"consulta": ("string", True), "limite": ("integer", False)},
                   lambda a: api_buscar(a["consulta"], a.get("limite", 10))),
    "api_pagina": ("Página de uma classe ou módulo (ex.: KX_GameObject, Range.logic). "
                   "Páginas grandes têm parte: props, funcs ou consts.",
                   {"nome": ("string", True), "parte": ("string", False)},
                   lambda a: api_pagina(a["nome"], a.get("parte", ""))),
    "api_item": ("Descrição completa de um item (método, atributo ou constante).",
                 {"nome": ("string", True), "pagina": ("string", False)},
                 lambda a: api_item(a["nome"], a.get("pagina", ""))),
}


def esquema(props):
    return {"type": "object",
            "properties": {k: {"type": t} for k, (t, _) in props.items()},
            "required": [k for k, (_, obrig) in props.items() if obrig]}


def responder(msg):
    metodo, id_ = msg.get("method"), msg.get("id")
    if metodo == "initialize":
        return {"protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {}, "resources": {}},
                "serverInfo": {"name": "anastacio-api", "version": VERSAO}}
    if metodo == "tools/list":
        return {"tools": [{"name": n, "description": d, "inputSchema": esquema(p)}
                          for n, (d, p, _) in FERRAMENTAS.items()]}
    if metodo == "tools/call":
        nome = msg["params"]["name"]
        args = msg["params"].get("arguments") or {}
        if nome not in FERRAMENTAS:
            return {"content": [{"type": "text", "text": f"Ferramenta desconhecida: {nome}"}], "isError": True}
        try:
            texto, erro = FERRAMENTAS[nome][2](args), False
        except Exception as e:  # falha de leitura/rede vira resposta, não derruba o servidor
            texto, erro = f"Erro: {e}", True
        return {"content": [{"type": "text", "text": texto}], "isError": erro}
    if metodo == "resources/list":
        return {"resources": [{"uri": "anastacio://guia", "name": "Guia da IA", "mimeType": "text/markdown"},
                              {"uri": "anastacio://indice", "name": "Índice da API", "mimeType": "text/markdown"}]}
    if metodo == "resources/read":
        uri = msg["params"]["uri"]
        arq = {"anastacio://guia": GUIA, "anastacio://indice": "INDEX.md"}.get(uri)
        if not arq:
            raise KeyError(uri)
        return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": ler(arq)}]}
    if metodo == "ping":
        return {}
    raise NotImplementedError(metodo)


def main():
    for linha in sys.stdin:
        linha = linha.strip()
        if not linha:
            continue
        try:
            msg = json.loads(linha)
        except ValueError:
            continue
        if "id" not in msg:  # notificação (ex.: notifications/initialized): sem resposta
            continue
        try:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "result": responder(msg)}
        except NotImplementedError:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32601, "message": "Method not found"}}
        except Exception as e:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32603, "message": str(e)}}
        sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
