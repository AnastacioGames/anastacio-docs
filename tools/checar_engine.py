"""Mostra quais páginas do site ficaram desatualizadas em relação ao código da engine.

Cada página com `fontes:` (arquivos ou pastas da engine) e `conferido:` (commit da engine em que a
página foi conferida) no frontmatter é comparada com o git da engine: lista os commits que mexeram
nessas fontes depois do `conferido`.

    python tools/checar_engine.py                 # relatório de todas as páginas
    python tools/checar_engine.py --diff frame    # mostra o diff das fontes da página "frame"
    python tools/checar_engine.py --marcar frame  # depois de atualizar, carimba com o HEAD da engine
    python tools/checar_engine.py --marcar todas

A engine fica em D:\\AnastacioEngine (troque com --engine).
"""

import argparse
import io
import re
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "site" / "src" / "content" / "docs"


def git(engine, *args):
    return subprocess.run(["git", "-C", str(engine), *args], capture_output=True, text=True,
                          encoding="utf-8").stdout.strip()


def ler_paginas():
    """Páginas em pt (raiz) que têm fontes e conferido; as traduções seguem a página pt."""
    paginas = []
    for arquivo in sorted(DOCS.rglob("*.md*")):
        if arquivo.relative_to(DOCS).parts[0] in ("en", "es", "ru"):
            continue
        texto = io.open(arquivo, encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
        if not m or "fontes:" not in m.group(1):
            continue
        cabecalho = m.group(1)
        fontes = re.findall(r"^\s+-\s+(.+?)\s*$", cabecalho.split("fontes:", 1)[1], re.M)
        conferido = re.search(r"^conferido:\s*(\S+)", cabecalho, re.M)
        nome = arquivo.relative_to(DOCS).with_suffix("").as_posix()
        paginas.append({"arquivo": arquivo, "nome": nome, "fontes": fontes,
                        "conferido": conferido.group(1) if conferido else None})
    return paginas


def escolher(paginas, chave):
    if chave == "todas":
        return paginas
    achadas = [p for p in paginas if p["nome"] == chave or p["nome"].endswith("/" + chave)]
    if not achadas:
        sys.exit("página não encontrada: %s (use o nome do arquivo, ex.: frame)" % chave)
    return achadas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", default=r"D:\AnastacioEngine")
    ap.add_argument("--diff", metavar="PAGINA")
    ap.add_argument("--marcar", metavar="PAGINA")
    a = ap.parse_args()
    paginas = ler_paginas()
    head = git(a.engine, "rev-parse", "--short=8", "HEAD")

    if a.marcar:
        for p in escolher(paginas, a.marcar):
            texto = io.open(p["arquivo"], encoding="utf-8").read()
            texto = re.sub(r"^conferido:.*$", "conferido: " + head, texto, count=1, flags=re.M)
            io.open(p["arquivo"], "w", encoding="utf-8", newline="\n").write(texto)
            print("carimbado %s -> %s" % (p["nome"], head))
        return

    if a.diff:
        for p in escolher(paginas, a.diff):
            print(git(a.engine, "diff", "--stat", p["conferido"] + "..HEAD", "--", *p["fontes"]))
            print(git(a.engine, "diff", p["conferido"] + "..HEAD", "--", *p["fontes"]))
        return

    pendentes = 0
    for p in paginas:
        commits = git(a.engine, "log", "--oneline", "--no-merges", p["conferido"] + "..HEAD", "--", *p["fontes"])
        # Fonte movida ou dividida: o git log do caminho antigo para de enxergar as mudanças.
        sumiram = [f for f in p["fontes"] if not (Path(a.engine) / f).exists()]
        if commits or sumiram:
            pendentes += 1
            print("\n[DESATUALIZADA] %s  (conferida em %s)" % (p["nome"], p["conferido"]))
            if commits:
                print("  " + commits.replace("\n", "\n  "))
            for f in sumiram:
                novo = git(a.engine, "log", "-1", "--name-status", "-M", "--format=", p["conferido"] + "..HEAD", "--", f)
                print("  FONTE SUMIU: %s %s" % (f, ("-> " + novo.replace("\n", " ")) if novo else "(atualize a lista fontes)"))
        else:
            print("[ok] %s" % p["nome"])
    print("\nengine HEAD %s; %d página(s) para revisar" % (head, pendentes))


if __name__ == "__main__":
    main()
