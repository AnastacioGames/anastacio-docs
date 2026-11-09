"""Junta as páginas da API num único Markdown para baixar (uso em IA local/RAG).

Lê as páginas já geradas por gerar_paginas.py e grava:
  site/public/anastacio-api-en.md  (inglês)
  site/public/anastacio-api-pt.md  (português)

Uso: python tools/gerar_md_unico.py   (rode depois de gerar_paginas.py)
"""
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parents[1]
DOCS = AQUI / "site" / "src" / "content" / "docs"
PUBLICO = AQUI / "site" / "public"

IDIOMAS = {
    "en": (DOCS / "en" / "api", "Anastacio Engine - Python API reference",
           "Single-file version of the API reference, for search and local AI (RAG). "
           "Each function and property has its own heading.", "Contents", "Modules", "Types",
           "See also"),
    "pt": (DOCS / "api", "Anastacio Engine - Referência da API Python",
           "Versão em arquivo único da referência da API, para busca e IA local (RAG). "
           "Cada função e propriedade tem um título próprio.", "Índice", "Módulos", "Tipos",
           "Veja também"),
}


def ancora(texto):
    """Âncora no estilo do GitHub."""
    t = texto.strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def ler_pagina(arq):
    texto = arq.read_text(encoding="utf-8")
    titulo = arq.stem
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if m:
        t = re.search(r'^title:\s*"?(.*?)"?\s*$', m.group(1), re.M)
        if t:
            titulo = t.group(1)
        texto = texto[m.end():]
    return titulo, texto


def limpar(texto, titulos, veja):
    saida, em_codigo, membros = [], False, []
    for linha in texto.split("\n"):
        if linha.startswith("```"):
            em_codigo = not em_codigo
            saida.append(linha)
            continue
        if em_codigo:
            saida.append(linha)
            continue
        # avisos do Starlight -> citação
        m = re.match(r"^:::(\w+)(?:\[(.*)\])?\s*$", linha)
        if m:
            rotulo = m.group(2) or m.group(1).capitalize()
            saida.append(f"> **{rotulo}:**")
            continue
        if linha.strip() == ":::":
            saida.append("")
            continue
        # selos HTML -> texto
        linha = re.sub(r'<span class="ae-badge[^"]*">(.*?)</span>', r"*(\1)*", linha)
        linha = re.sub(r"<small>(.*?)</small>", r"`\1`", linha)
        linha = re.sub(r"</?(span|small)[^>]*>", "", linha)
        # links entre páginas -> âncoras deste arquivo
        def troca(mm):
            alvo = mm.group(2).rstrip("/").split("/")[-1].split("#")[0].lower()
            return f"[{mm.group(1)}](#{titulos[alvo]})" if alvo in titulos else mm.group(1)
        linha = re.sub(r"\[([^\]]*)\]\(((?:\.\./)+[^)]*)\)", troca, linha)
        # títulos descem dois níveis: página = ##, seções = ###, membros = ####
        h = re.match(r"^(#{1,4}) (.*)", linha)
        if h:
            nivel = len(h.group(1)) + 1
            linha = "#" * min(nivel, 6) + " " + h.group(2)
            if len(h.group(1)) == 3:
                membros.append(h.group(2).strip())
        saida.append(linha)
    corpo = re.sub(r"\n{3,}", "\n\n", "\n".join(saida)).strip()
    return corpo, membros


def gerar(lang):
    pasta, titulo, intro, rot_ind, rot_mod, rot_tip, veja = IDIOMAS[lang]
    grupos = [(rot_mod, sorted((pasta / "modulos").glob("*.md"))),
              (rot_tip, sorted((pasta / "types").glob("*.md")))]
    paginas = [(g, a) + ler_pagina(a) for g, arqs in grupos for a in arqs]
    titulos = {a.stem.lower(): ancora(t) for _, a, t, _ in paginas}

    corpo, indice, grupo_atual = [], [], None
    for grupo, arq, tit, texto in paginas:
        if grupo != grupo_atual:
            grupo_atual = grupo
            corpo.append(f"# {grupo}")
            indice.append(f"\n**{grupo}**\n")
        conteudo, membros = limpar(texto, titulos, veja)
        corpo.append(f"## {tit}\n\n{conteudo}")
        indice.append(f"- [{tit}](#{ancora(tit)})")
    total = sum(len(re.findall(r"^#### ", c, re.M)) for c in corpo)
    cab = f"# {titulo}\n\n{intro}\n\n{len(paginas)} pages, {total} entries (functions, properties and constants).\n\n## {rot_ind}\n"
    texto = cab + "\n".join(indice) + "\n\n---\n\n" + "\n\n---\n\n".join(corpo) + "\n"
    PUBLICO.mkdir(exist_ok=True)
    dest = PUBLICO / f"anastacio-api-{lang}.md"
    dest.write_text(texto, encoding="utf-8")
    print(f"{dest.name}: {len(paginas)} páginas, {total} itens, {len(texto.encode()) // 1024} KB")


if __name__ == "__main__":
    for l in IDIOMAS:
        gerar(l)
