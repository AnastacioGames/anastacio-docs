"""Gera as páginas da API do site (site/src/content/docs/api/).

Junta três fontes:
  1. o texto herdado da Range nos .rst da engine (convertido de reStructuredText);
  2. inventario/api_inventario.json (o que existe no C++ e o selo de cada item);
  3. as docstrings que o C++ já tem nas tabelas PyMethodDef.

Uso: python tools/gerar_paginas.py [--engine D:/AnastacioEngine]
Rode antes tools/api_inventario.py para atualizar o inventário.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parents[1]


def _arg(nome, padrao):
    if nome in sys.argv:
        return sys.argv[sys.argv.index(nome) + 1]
    return padrao


ENGINE = Path(_arg("--engine", "D:/AnastacioEngine")).resolve()
RST = ENGINE / "source" / "doc" / "python_api" / "rst"
CPP = ENGINE / "source" / "source" / "gameengine"
INVENTARIO = AQUI / "inventario" / "api_inventario.json"
DESTINO = AQUI / "site" / "src" / "content" / "docs"

# módulo do inventário -> (arquivo .rst ou None, nome público)
MODULOS = {
    "logic": ("bge.logic", "Range.logic"),
    "render": ("bge.render", "Range.render"),
    "events": ("bge.events", "Range.events"),
    "constraints": ("bge.constraints", "Range.constraints"),
    "app": ("bge.app", "Range.application"),
    "texture": ("bge.texture", "Range.texture"),
    "imgui": (None, "Range.imgui"),
    "network": (None, "Range.network"),
    "network.steam": (None, "Range.network.steam"),
}

SELO = {
    "novo_anastacio": '<span class="ae-badge novo">novo na Anastacio</span>',
    "novo": '<span class="ae-badge pendente">sem documentação</span>',
    "sem_doc": '<span class="ae-badge pendente">sem descrição</span>',
}


# ---------------------------------------------------------------- docstrings do C++

RE_ENTRADA = re.compile(r'\{\s*"(\w+)"\s*,\s*\(PyCFunction\)[^,]+,[^,"}]+,\s*((?:"(?:[^"\\]|\\.)*"\s*)+)\}', re.S)


def docstrings_cpp():
    docs = {}
    for arq in CPP.rglob("*.cpp"):
        txt = arq.read_text(encoding="utf-8", errors="replace")
        for nome, literais in RE_ENTRADA.findall(txt):
            partes = re.findall(r'"((?:[^"\\]|\\.)*)"', literais)
            texto = "".join(partes).encode().decode("unicode_escape", errors="replace")
            texto = texto.encode("latin-1", errors="replace").decode("utf-8", errors="replace")
            if texto.strip():
                docs.setdefault(nome, texto.strip())
    return docs


# ---------------------------------------------------------------- rst -> markdown

def trocar_bge(t):
    t = re.sub(r"\bimport bge\b", "import Range", t)
    t = re.sub(r"\bfrom bge\b", "from Range", t)
    t = re.sub(r"\bbge\.app\b", "Range.application", t)
    return re.sub(r"\bbge\.", "Range.", t)


def inline(t):
    t = re.sub(r":(?:class|data|meth|func|attr|mod|obj|const|ref|exc|doc):`~?([^`<]*?)(?:\s*<[^>]*>)?`",
               lambda m: f"`{m.group(1).split('.')[-1] if m.group(0).count('~') else m.group(1)}`", t)
    t = re.sub(r"``([^`]+)``", r"`\1`", t)
    t = re.sub(r"`([^`<]+?)\s*<(https?://[^>]+)>`_", r"[\1](\2)", t)
    return trocar_bge(t)


RE_DIR = re.compile(r"^(\s*)\.\. ([\w-]+)::\s*(.*)$")
RE_SUBLINHA = re.compile(r"^([=\-*^~#+])\1{2,}\s*$")
ASIDE = {"note": "note", "seealso": "tip", "tip": "tip", "hint": "tip",
         "warning": "caution", "attention": "caution", "important": "caution",
         "deprecated": "danger", "danger": "danger", "versionadded": "note", "versionchanged": "note"}


def indent(l):
    return len(l) - len(l.lstrip())


def bloco(linhas, i, base):
    """Linhas a partir de i com recuo > base (ou vazias). Devolve (linhas, próximo i)."""
    out = []
    while i < len(linhas) and (not linhas[i].strip() or indent(linhas[i]) > base):
        out.append(linhas[i])
        i += 1
    while out and not out[-1].strip():
        out.pop()
    return out, i


def dedent(ls):
    m = min((indent(l) for l in ls if l.strip()), default=0)
    return [l[m:] for l in ls]


def rst_para_md(texto, selos=None):
    """Converte o texto de um .rst. `selos` = {nome: html} para pôr ao lado dos títulos."""
    selos = selos or {}
    linhas = texto.splitlines()
    out, i, titulo_visto = [], 0, False
    while i < len(linhas):
        l = linhas[i]
        s = l.strip()
        # título com sublinhado (e talvez sobrelinhado)
        if i + 1 < len(linhas) and s and RE_SUBLINHA.match(linhas[i + 1].strip()) and not RE_DIR.match(l):
            if not titulo_visto:
                titulo_visto = True
            else:
                out += ["", f"## {inline(s)}", ""]
            i += 2
            continue
        if RE_SUBLINHA.match(s):
            i += 1
            continue
        d = RE_DIR.match(l)
        if d:
            rec, nome, arg = indent(l), d.group(2), d.group(3).strip()
            corpo, i = bloco(linhas, i + 1, rec)
            # opções da diretiva (:linenos: etc.) ficam no começo do corpo
            while corpo and re.match(r"^\s*:\w[\w-]*:", corpo[0]) and nome in ("code-block", "literalinclude", "toctree", "image", "figure"):
                corpo.pop(0)
            if nome in ("code-block", "code", "sourcecode"):
                out += ["", f"```{arg or 'python'}", *map(trocar_bge, dedent(corpo)), "```", ""]
            elif nome in ("method", "function", "attribute", "data", "class"):
                nm = arg.split("(")[0].split(".")[-1]
                if nome == "class":
                    out += ["", rst_para_md("\n".join(dedent(corpo)), selos), ""]
                else:
                    sinal = arg if "(" in arg else nm
                    out += ["", f"### {sinal}", ""]
                    if nm in selos:
                        out += [selos[nm], ""]
                    out += [rst_para_md("\n".join(dedent(corpo)), selos), ""]
            elif nome in ASIDE:
                rot = {"deprecated": "Obsoleto", "versionadded": "Adicionado", "versionchanged": "Alterado"}.get(nome)
                titulo = f"[{rot} {arg}]" if rot else ""
                conteudo = rst_para_md("\n".join(dedent(corpo))) if corpo else (arg if not rot else "")
                out += ["", f":::{ASIDE[nome]}{titulo}", conteudo, ":::", ""]
            elif nome == "rubric":
                out += ["", f"**{inline(arg)}**", ""]
            elif nome in ("module", "currentmodule", "toctree", "include", "literalinclude", "image", "figure", "only", "index"):
                pass
            else:
                out += [rst_para_md("\n".join(dedent(corpo)))]
            continue
        # campos :arg x: / :type: / :return:
        # alvos (.. _nome:) e comentários do rst (.. texto: sem ::)
        if re.match(r"^\s*\.\. (_[\w-]+:|\w+:\s)", l) or re.match(r"^\s*\.\. _[\w-]+:\s*$", l):
            i += 1
            continue
        f = re.match(r"^\s*:(\w+)\s*([^:`]*):(?!`)\s*(.*)$", l)
        if f:
            campo, alvo, valor = f.group(1), f.group(2).strip(), f.group(3)
            extra, i = bloco(linhas, i + 1, indent(l))
            valor = inline(" ".join([valor] + [e.strip() for e in extra if e.strip()]))
            rotulo = {"arg": "", "param": "", "type": "Tipo", "return": "Retorna",
                      "returns": "Retorna", "rtype": "Tipo do retorno", "raises": "Erro"}.get(campo, campo)
            if campo == "columns":
                pass
            elif campo == "value":
                out += ["", f"**Valor:** `{valor}`", ""]
            elif campo in ("arg", "param") and alvo:
                out.append(f"- **`{alvo}`**: {valor}")
            elif campo == "type" and alvo:
                out.append(f"  - tipo: {valor}")
            else:
                out += ["", f"**{rotulo}:** {valor}", ""]
            continue
        # bloco literal depois de "::"
        if s.endswith("::") and not s.startswith(".."):
            txt = s[:-1] if s != "::" else ""
            if txt:
                out.append(inline(txt))
            corpo, i = bloco(linhas, i + 1, indent(l))
            out += ["", "```", *dedent(corpo), "```", ""]
            continue
        # tabela simples/grade do rst: mantém como texto fixo
        if re.match(r"^\s*[+=][-=+ ]{3,}$", l):
            tab = []
            while i < len(linhas) and linhas[i].strip():
                tab.append(linhas[i].strip())
                i += 1
            out += ["", "```text", *tab, "```", ""]
            continue
        out.append(inline(s))
        i += 1
    md = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


# ---------------------------------------------------------------- páginas

def frontmatter(titulo, descricao):
    return f"---\ntitle: {json.dumps(titulo)}\ndescription: {json.dumps(descricao, ensure_ascii=False)}\n---\n\n"


def selo_de(item):
    if item["status"] == "novo":
        return SELO["novo_anastacio"] if item.get("origem") == "anastacio" else SELO["novo"]
    if item["status"] == "sem_doc":
        return SELO["sem_doc"]
    return None


def secao_pendentes(itens, docs):
    """Itens que existem no C++ mas não estão no rst."""
    novos = [(n, i) for n, i in itens.items() if i["status"] == "novo"]
    if not novos:
        return ""
    out = ["", "## Sem documentação da Range", "",
           "Estes itens existem na engine mas não estavam na documentação da Range. "
           "Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.", ""]
    ordem = {"metodo": 0, "funcao": 0, "atributo": 1, "constante": 2}
    for nome, i in sorted(novos, key=lambda x: (ordem.get(x[1]["tipo"], 3), x[0].lower())):
        if nome.startswith("_"):
            continue  # uso interno
        tipo = {"metodo": "método", "funcao": "função", "atributo": "atributo", "constante": "constante"}.get(i["tipo"], i["tipo"])
        doc = docs.get(nome, "")
        m = re.match(rf"{nome}\([^)]*\)", doc)
        cab = m.group(0) if m else nome + ("()" if i["tipo"] in ("metodo", "funcao") else "")
        resto = doc[len(cab):].lstrip(" :") if m else doc
        retorno = re.match(r"->\s*([^\n]+)\n?", resto)
        if retorno:
            resto = resto[retorno.end():]
        out += [f"### {cab}", "", f"{selo_de(i)} <small>{tipo}{' · só leitura' if i.get('so_leitura') else ''}</small>", ""]
        if resto.strip():
            out += [inline(resto.strip()).replace("\n", "  \n"), ""]
        if retorno:
            out += [f"**Retorna:** `{retorno.group(1).strip()}`", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- tradução

# traducao/pt.json: {"texto em inglês": "texto em português"}. A chave é o
# trecho como sai do .rst (parágrafo numa linha só, item de lista ou
# comentário de código). Trecho sem tradução continua em inglês e vai para
# traducao/pendente.json, que serve de lista do que falta traduzir.
TRADUCAO = AQUI / "traducao" / "pt.json"
PENDENTE = AQUI / "traducao" / "pendente.json"
_pt = json.loads(TRADUCAO.read_text(encoding="utf-8")) if TRADUCAO.exists() else {}
_pendente = {}
_pagina_atual = [""]


def _tr(chave):
    chave = chave.strip()
    if (not chave or not re.search(r"[A-Za-z]{3}", chave) or "+--" in chave
            or re.fullmatch(r"[\s,]*(`[^`]+`[\s,]*)+", chave)):
        return chave
    if chave in _pt:
        return _pt[chave]
    if chave in GERADO_PT:
        return chave
    _pendente.setdefault(_pagina_atual[0], {})[chave] = ""
    return chave


# textos que o próprio gerador escreve em português
GERADO_PT = {
    "Sem documentação da Range",
    "Estes itens existem na engine mas não estavam na documentação da Range. "
    "Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.",
}
RE_LISTA_ARG = re.compile(r"^(- \*\*`[^`]+`\*\*: )(.*)$")
RE_CAMPO = re.compile(r"^(\*\*(?:Retorna|Erro):\*\* )(.*)$")
RE_COMENT = re.compile(r"^(\s*(?:[^#'\"]*?)#\s?)(.+)$")


def traduzir_md(md):
    out, paragrafo, em_codigo = [], [], False

    def fechar():
        if paragrafo:
            out.append(_tr(" ".join(paragrafo)))
            paragrafo.clear()

    for l in md.split("\n"):
        if l.startswith("```"):
            fechar()
            em_codigo = not em_codigo
            out.append(l)
            continue
        if em_codigo:
            m = RE_COMENT.match(l)
            out.append(m.group(1) + _tr(m.group(2)) if m else l)
            continue
        s = l.strip()
        if (not s or s.startswith(("#", "|", ":::", "<", "**Tipo", "**Valor", "- tipo", "Classe base"))
                or re.match(r"^[-*] ", s) and not RE_LISTA_ARG.match(s)):
            fechar()
            if s.startswith("## "):
                out.append("## " + _tr(s[3:]))
            elif re.match(r"^[-*] ", s) and not s.startswith("- tipo"):
                out.append(l[:len(l) - len(l.lstrip())] + s[:2] + _tr(s[2:]))
            else:
                out.append(l)
            continue
        m = RE_LISTA_ARG.match(s) or RE_CAMPO.match(s)
        if m:
            fechar()
            out.append(m.group(1) + _tr(m.group(2)))
            continue
        paragrafo.append(s)
    fechar()
    return "\n".join(out)


def escrever(caminho, texto):
    _pagina_atual[0] = caminho.stem
    fm, _, corpo = texto.partition("\n---\n")
    caminho.write_text(fm + "\n---\n" + traduzir_md(corpo), encoding="utf-8")


def pagina_modulo(chave, info, docs):
    rst_nome, publico = MODULOS[chave]
    selos = {n: s for n, i in info["itens"].items() if (s := selo_de(i))}
    corpo = ""
    if rst_nome and (RST / f"{rst_nome}.rst").exists():
        corpo = rst_para_md((RST / f"{rst_nome}.rst").read_text(encoding="utf-8", errors="replace"), selos)
    else:
        corpo = f"Módulo `{publico}` da Anastacio Engine. Também acessível como `{publico.replace('Range.', 'bge.')}`."
    nome_arq = publico.replace("Range.", "")
    texto = frontmatter(publico, f"Referência do módulo {publico}") + corpo + "\n" + secao_pendentes(info["itens"], docs) + "\n"
    escrever(DESTINO / "api" / "modulos" / f"{nome_arq}.md", texto)


def pagina_classe(nome, info, rst_arq, docs):
    selos = {n: s for n, i in (info or {}).get("itens", {}).items() if (s := selo_de(i))}
    if rst_arq:
        corpo = rst_para_md(rst_arq.read_text(encoding="utf-8", errors="replace"), selos)
        base = re.search(r"base class --- :class:`~?([\w.]+)`", rst_arq.read_text(encoding="utf-8", errors="replace"))
    else:
        corpo, base = f"Classe `Range.types.{nome}`.", None
    corpo = re.sub(r"^base class --- .*$", "", corpo, flags=re.M)
    topo = f"Classe base: [`{base.group(1).split('.')[-1]}`](../{base.group(1).split('.')[-1].lower()}/)\n\n" if base else ""
    pend = secao_pendentes(info["itens"], docs) if info else ""
    texto = frontmatter(nome, f"Referência da classe Range.types.{nome}") + topo + corpo + "\n" + pend + "\n"
    escrever(DESTINO / "api" / "types" / f"{nome}.md", texto)


def pagina_situacao(inv):
    linhas = [frontmatter("Situação da documentação", "Quanto da API já está documentado."),
              "Gerado a partir do inventário da engine. **Pendentes** existem no código e ainda não têm texto.", "",
              "| Página | Itens | Documentados | Pendentes | Novos na Anastacio |", "|---|---:|---:|---:|---:|"]
    for grupo, prefixo in (("modulos", "Range."), ("classes", "")):
        for nome, v in sorted(inv[grupo].items()):
            it = v["itens"].values()
            doc = sum(1 for i in it if i["status"] == "documentado")
            pend = sum(1 for i in it if i["status"] in ("novo", "sem_doc"))
            ana = sum(1 for i in it if i.get("origem") == "anastacio")
            titulo = MODULOS[nome][1] if grupo == "modulos" else nome
            linhas.append(f"| `{titulo}` | {len(v['itens'])} | {doc} | {pend} | {ana or ''} |")
    (DESTINO / "situacao-da-doc.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main():
    inv = json.loads(INVENTARIO.read_text(encoding="utf-8"))
    docs = docstrings_cpp()
    for sub in ("api/modulos", "api/types"):
        pasta = DESTINO / sub
        pasta.mkdir(parents=True, exist_ok=True)
        for velho in pasta.glob("*.md"):
            velho.unlink()

    for chave, info in inv["modulos"].items():
        if chave in MODULOS:
            pagina_modulo(chave, info, docs)

    rst_por_nome = {p.stem.replace("bge.types.", ""): p for p in (RST / "bge_types").glob("*.rst")}
    usados = set()
    for nome, info in inv["classes"].items():
        rst_nome = info.get("rst")
        # 'Texture' do VideoTexture casou por engano com BL_Texture no inventário
        if nome == "Texture":
            rst_nome = None
        if rst_nome:
            usados.add(rst_nome)
        pagina_classe(nome, info, rst_por_nome.get(rst_nome), docs)
    for rst_nome, arq in rst_por_nome.items():
        if rst_nome not in usados and not (DESTINO / "api" / "types" / f"{rst_nome}.md").exists():
            pagina_classe(rst_nome, None, arq, docs)

    pagina_situacao(inv)
    PENDENTE.parent.mkdir(exist_ok=True)
    PENDENTE.write_text(json.dumps(_pendente, indent=1, ensure_ascii=False), encoding="utf-8")
    falta = sum(len(v) for v in _pendente.values())
    print(f"tradução: {len(_pt)} trechos traduzidos, {falta} pendentes (traducao/pendente.json)")
    total = len(list((DESTINO / "api").rglob("*.md")))
    print(f"{total} páginas de API geradas em {DESTINO / 'api'}")


if __name__ == "__main__":
    main()
