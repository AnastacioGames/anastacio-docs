"""Confere conteudo/exemplos.txt: sintaxe, comentário traduzido e nomes que existem na API.

Uso: python tools/checar_exemplos.py   (rode depois de gerar_paginas.py)
"""
import ast
import builtins
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent.parent
API = AQUI / "site" / "src" / "content" / "docs" / "api"
sys.path.insert(0, str(AQUI / "tools"))

# métodos do Python e de bibliotecas que não aparecem na API da engine
PYTHON = set(dir(dict)) | set(dir(list)) | set(dir(str)) | set(dir(bytes)) | {"radians", "x", "y", "z", "w"}
# submódulos de Range, classes e constantes de imgui, que não têm título próprio
PYTHON |= {"logic", "events", "render", "types", "texture", "constraints", "network", "imgui", "COL_BUTTON", "COND_FIRST_USE_EVER", "KX_PythonComponent", "KX_MeshBuilder", "KX_MeshBuilder", "EXP_Value", "inputSystem", "rpc"}


def ler(caminho=AQUI / "conteudo" / "exemplos.txt"):
    """{pagina: [{"en": [linhas], "pt": [linhas]}]}"""
    paginas = {}
    for sec in re.split(r"^=== ", caminho.read_text(encoding="utf-8"), flags=re.M)[1:]:
        nome, corpo = sec.split("\n", 1)
        lista = []
        for bloco in re.split(r"^---$", corpo, flags=re.M):
            en, pt = [], []
            for l in bloco.strip("\n").split("\n"):
                m = re.match(r"^(\s*)# (.+?) \|\|\| (.+)$", l)
                en.append(m.group(1) + "# " + m.group(2) if m else l)
                pt.append(m.group(1) + "# " + m.group(3) if m else l)
            lista.append({"en": en, "pt": pt})
        paginas[nome.strip()] = lista
    return paginas


def main():
    conhecidos = set()
    arquivos = {}
    for md in API.rglob("*.md"):
        texto = md.read_text(encoding="utf-8")
        arquivos[md.stem] = texto
        conhecidos |= set(re.findall(r"\b[A-Za-z_]\w*\b", "\n".join(re.findall(r"^#{2,5} .+$", texto, re.M))))
    erros = 0
    total = 0
    paginas = ler()
    for nome, lista in paginas.items():
        if nome not in arquivos:
            print(f"{nome}: página não existe")
            erros += 1
        for n, ex in enumerate(lista, 1):
            total += 1
            codigo = "\n".join(ex["en"])
            for l in ex["en"]:
                if "|||" in l or re.match(r"\s*#", l) and ex["pt"][ex["en"].index(l)] == l:
                    print(f"{nome} #{n}: comentário sem tradução: {l}")
                    erros += 1
            try:
                arvore = ast.parse(codigo)
            except SyntaxError as e:
                print(f"{nome} #{n}: sintaxe: {e}")
                erros += 1
                continue
            for no in ast.walk(arvore):
                if isinstance(no, ast.Attribute) and no.attr not in conhecidos and no.attr not in PYTHON:
                    # atributo criado no próprio exemplo (self.volume)
                    if isinstance(no.value, ast.Name) and no.value.id == "self":
                        continue
                    print(f"{nome} #{n}: nome fora da API: {no.attr}")
                    erros += 1
    print(f"{total} exemplos em {len(paginas)} páginas, {erros} problemas")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
