"""Gera a referência da API fatiada para IA (Claude Code, MCP, RAG).

O arquivo único (anastacio-api-*.md) tem ~450 KB: grande demais para colocar no contexto de uma IA.
Aqui a mesma referência sai em pedaços pequenos, mais um índice curto e um índice de busca:

  site/public/api-ia/<lang>/INDEX.md           índice curto: uma linha por página
  site/public/api-ia/<lang>/paginas/<Nome>.md  uma página por classe/módulo
  site/public/api-ia/<lang>/paginas/<Nome>--props|funcs|consts.md
                                               partes de páginas grandes (KX_GameObject, Range.logic...)
  site/public/api-ia/<lang>/busca.json         um registro por item (nome, tipo, resumo, arquivo)
  site/public/api-ia/<lang>/GUIA.md            regras e armadilhas (copiado de conteudo/guia-ia-<lang>.md)

Uso: python tools/gerar_api_ia.py   (rode depois de gerar_paginas.py, junto com gerar_md_unico.py)
"""
import json
import re
import shutil
from pathlib import Path

from gerar_md_unico import AQUI, DOCS, IDIOMAS, PUBLICO, ler_pagina, limpar

SAIDA = PUBLICO / "api-ia"
CONTEUDO = AQUI / "conteudo"
LIMITE_PAGINA = 24 * 1024  # acima disso a página é dividida em partes por tipo de item

TEXTOS = {
    "pt": {
        "titulo": "Anastacio Engine - Referência da API Python (fatiada para IA)",
        "como": [
            "Como usar (para IA):",
            "1. Leia **GUIA.md** uma vez: regras da engine e armadilhas comuns.",
            "2. Ache a classe ou módulo abaixo e abra só essa página (ou use `busca.json` / a ferramenta `api_buscar`).",
            "3. Páginas grandes têm um arquivo de visão geral e partes: `--props` (atributos), `--funcs` (métodos e funções), `--consts` (constantes).",
            "4. Não invente funções: se um nome não está nestas páginas, ele não existe na API.",
        ],
        "modulos": "Módulos", "tipos": "Tipos", "itens": "itens", "partes": "partes",
        "sem_resumo": "sem descrição",
        "visao": "Visão geral. Os itens estão nas partes abaixo:",
        "parte_de": "Parte de",
        "props": "atributos", "funcs": "métodos e funções", "consts": "constantes",
        "boilerplate": "Estes itens existem na engine mas não estavam na documentação da Range",
    },
    "en": {
        "titulo": "Anastacio Engine - Python API reference (sliced for AI)",
        "como": [
            "How to use (for AI):",
            "1. Read **GUIDE.md** once: engine rules and common pitfalls.",
            "2. Find the class or module below and open only that page (or use `busca.json` / the `api_buscar` tool).",
            "3. Large pages have an overview file plus parts: `--props` (attributes), `--funcs` (methods and functions), `--consts` (constants).",
            "4. Do not invent functions: if a name is not on these pages, it does not exist in the API.",
        ],
        "modulos": "Modules", "tipos": "Types", "itens": "items", "partes": "parts",
        "sem_resumo": "no description",
        "visao": "Overview. The items are in the parts below:",
        "parte_de": "Part of",
        "props": "attributes", "funcs": "methods and functions", "consts": "constants",
        "boilerplate": "These items exist in the engine but were not in the Range documentation",
    },
}
NOME_GUIA = {"pt": "GUIA.md", "en": "GUIDE.md"}
PARTES = ("props", "funcs", "consts")


def descer(texto):
    """Sobe a hierarquia de títulos um nível (### -> ##, #### -> ###) fora dos blocos de código."""
    saida, em_codigo = [], False
    for linha in texto.split("\n"):
        if linha.startswith("```"):
            em_codigo = not em_codigo
        elif not em_codigo:
            m = re.match(r"^(#{2,6}) (.*)", linha)
            if m:
                linha = "#" * (len(m.group(1)) - 1) + " " + m.group(2)
        saida.append(linha)
    return "\n".join(saida)


def blocos(texto):
    """Divide o texto (títulos ### = seção, #### = item) em [(tipo, título, corpo)]."""
    lista, atual, em_codigo = [], ["pre", "", []], False
    for linha in texto.split("\n"):
        if linha.startswith("```"):
            em_codigo = not em_codigo
        m = None if em_codigo else re.match(r"^(#{3,4}) (.*)", linha)
        if m:
            lista.append(atual)
            atual = ["sec" if len(m.group(1)) == 3 else "item", m.group(2).strip(), []]
        else:
            atual[2].append(linha)
    lista.append(atual)
    return [(t, ti, "\n".join(c).strip("\n")) for t, ti, c in lista]


def tipo_do_item(titulo, em_classe):
    nome = re.split(r"[ (]", titulo)[0]
    if "(" in titulo:
        return "method" if em_classe else "function"
    if nome.isupper() or re.fullmatch(r"[A-Z0-9_]+", nome):
        return "constant"
    return "attribute"


def resumo_do_item(corpo):
    for linha in corpo.split("\n"):
        s = linha.strip()
        if not s or s.startswith(("*(", "`", "**", ">", "```", "|", "-", ".. ")):
            continue
        s = re.sub(r"\s+", " ", s)
        return s[:160] + ("…" if len(s) > 160 else "")
    return ""


def resumo_da_pagina(pre):
    """Primeiro parágrafo de texto corrido (ignora blocos de código e linhas que parecem código)."""
    linhas, em_codigo = [], False
    for linha in pre.split("\n"):
        if linha.startswith("```"):
            em_codigo = not em_codigo
        elif not em_codigo:
            linhas.append(linha)
    for par in re.split(r"\n\s*\n", "\n".join(linhas)):
        s = par.strip()
        if not s or s.startswith(("Classe base", "Base class", ">", "#", ".. ", "Veja", "See")):
            continue
        if re.match(r"^[\w.\[\]\"']+(\(.*\))?\s*(=|\()", s) and " " not in s.split("=")[0].strip():
            continue  # linha de código solta
        return re.sub(r"\s+", " ", s)[:180]
    return ""


def gerar(lang):
    pasta, *_ = IDIOMAS[lang]
    T = TEXTOS[lang]
    grupos = [(T["modulos"], True, sorted((pasta / "modulos").glob("*.md"), key=lambda p: p.name.lower())),
              (T["tipos"], False, sorted((pasta / "types").glob("*.md"), key=lambda p: p.name.lower()))]
    paginas = [(g, mod, a) + ler_pagina(a) for g, mod, arqs in grupos for a in arqs]
    titulos = {a.stem.lower(): t for _, _, a, t, _ in paginas}
    destino = SAIDA / lang
    if destino.exists():
        shutil.rmtree(destino)
    (destino / "paginas").mkdir(parents=True)

    busca, indice, grupo_atual, n_itens = [], [], None, 0
    for grupo, modulo, arq, tit, texto in paginas:
        corpo = limpar(texto, titulos, link=lambda t: f"{t}.md")
        bl = blocos(corpo)
        itens = [(t, c) for tp, t, c in bl if tp == "item"]
        n_itens += len(itens)
        # visão geral = tudo antes do primeiro item + texto das seções com conteúdo próprio
        pre, vistos_item = [], False
        for tp, ti, c in bl:
            if tp == "item":
                vistos_item = True
            elif tp == "sec" and not vistos_item:
                pre.append(f"### {ti}\n\n{c}".strip())
            elif tp == "sec" and c.strip() and T["boilerplate"] not in c:
                pre.append(f"### {ti}\n\n{c}".strip())
            elif tp == "pre":
                pre.append(c)
        visao = "\n\n".join(x for x in pre if x.strip())
        resumo = resumo_da_pagina(visao)
        completo = descer(f"## {tit}\n\n" + corpo)
        partes = {}
        if len(completo.encode()) > LIMITE_PAGINA and itens:
            for ti, c in itens:
                partes.setdefault({"attribute": "props", "constant": "consts"}.get(
                    tipo_do_item(ti, not modulo), "funcs"), []).append(f"## {ti}\n\n{c}".strip())
            nomes = []
            for chave in PARTES:
                if chave in partes:
                    nome_arq = f"{tit}--{chave}.md"
                    nomes.append((chave, nome_arq, len(partes[chave])))
                    (destino / "paginas" / nome_arq).write_text(
                        f"# {tit} - {T[chave]}\n\n{T['parte_de']} [{tit}]({tit}.md).\n\n"
                        + "\n\n".join(partes[chave]) + "\n", encoding="utf-8")
            lista = "\n".join(f"- [{T[k]}]({a}) ({n} {T['itens']})" for k, a, n in nomes)
            principal = f"# {tit}\n\n{descer(visao)}\n\n{T['visao']}\n\n{lista}\n"
        else:
            nomes = []
            principal = completo.replace("## ", "# ", 1) + "\n"
        arquivo_pag = f"{tit}.md"
        (destino / "paginas" / arquivo_pag).write_text(principal, encoding="utf-8")

        for ti, c in itens:
            tipo = tipo_do_item(ti, not modulo)
            chave = {"attribute": "props", "constant": "consts"}.get(tipo, "funcs")
            arq_item = f"{tit}--{chave}.md" if nomes else arquivo_pag
            busca.append({"nome": re.split(r"[ (]", ti)[0], "assinatura": ti, "pagina": tit,
                          "tipo": tipo, "resumo": resumo_do_item(c), "arquivo": f"paginas/{arq_item}"})

        if grupo != grupo_atual:
            grupo_atual = grupo
            indice.append(f"\n## {grupo}\n")
        extra = f"; {T['partes']}: " + ", ".join(k for k, _, _ in nomes) if nomes else ""
        indice.append(f"- [{tit}](paginas/{arquivo_pag}) - {resumo or T['sem_resumo']} "
                      f"({len(itens)} {T['itens']}{extra})")

    guia_src = CONTEUDO / f"guia-ia-{lang}.md"
    guia = NOME_GUIA[lang]
    if guia_src.exists():
        shutil.copyfile(guia_src, destino / guia)
    cab = (f"# {T['titulo']}\n\n" + "\n".join(T["como"]) +
           f"\n\n{len(paginas)} {T['partes'] if False else 'páginas' if lang == 'pt' else 'pages'}, "
           f"{n_itens} {T['itens']}. Guia: [{guia}]({guia}). Busca: `busca.json`.\n")
    (destino / "INDEX.md").write_text(cab + "\n".join(indice) + "\n", encoding="utf-8")
    (destino / "busca.json").write_text(
        json.dumps(busca, ensure_ascii=False, indent=0), encoding="utf-8")
    if lang == "pt":
        vazios = [i for i in busca if not i["resumo"]]
        por_pagina = {}
        for i in vazios:
            por_pagina.setdefault(i["pagina"], []).append(i["assinatura"])
        linhas = [f"# Itens sem descrição em texto corrido\n\n{len(vazios)} de {len(busca)} itens não têm "
                  "uma frase de descrição (só assinatura, tipo ou parâmetros). A IA acerta menos nesses. "
                  "Escreva a descrição em `conteudo/descricoes.json` ou na docstring do C++. "
                  "Gerado por `tools/gerar_api_ia.py`.\n"]
        for pag, nomes in sorted(por_pagina.items(), key=lambda x: -len(x[1])):
            linhas.append(f"\n## {pag} ({len(nomes)})\n\n" + "\n".join(f"- `{n}`" for n in nomes))
        (AQUI / "inventario" / "sem_descricao.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    tam = max(p.stat().st_size for p in (destino / "paginas").glob("*.md")) // 1024
    print(f"api-ia/{lang}: {len(paginas)} páginas, {n_itens} itens, "
          f"{len(list((destino / 'paginas').glob('*.md')))} arquivos, maior {tam} KB")


if __name__ == "__main__":
    for l in IDIOMAS:
        gerar(l)
