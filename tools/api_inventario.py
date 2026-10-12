"""Inventário e auditoria da API Python da Anastacio Engine.

Lê, no repositório da engine, as tabelas de bindings no C++ (Methods/Attributes das classes e os
métodos/constantes dos módulos) e cruza com a documentação herdada em
source/doc/python_api/rst. Gera inventario/api_inventario.json e
inventario/api_inventario.md neste repositório. Também cruza os controles RNA
de recursos de jogo com os bindings e gera inventario/cobertura_python.*.

Uso: python tools/api_inventario.py [--engine D:/AnastacioEngine] [--sem-origem]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

def _arg(nome, padrao):
    if nome in sys.argv:
        return sys.argv[sys.argv.index(nome) + 1]
    return padrao


RAIZ = Path(_arg("--engine", "D:/AnastacioEngine")).resolve()
CPP = RAIZ / "source" / "source" / "gameengine"
RST = RAIZ / "source" / "doc" / "python_api" / "rst"
SAIDA = Path(__file__).resolve().parents[1] / "inventario"

# PyModuleDef -> módulo público (Range.<x>; bge.<x> é alias)
MODULO_DEF = {
    "GameLogic_module_def": "logic",
    "Rasterizer_module_def": "render",
    "GameKeys_module_def": "events",
    "Application_module_def": "app",
    "PhysicsConstraints_module_def": "constraints",
    "Imgui_module_def": "imgui",
    "g_module_def": "network",
    "steamModule": "network.steam",
    "VideoTexture_module_def": "texture",
}
MODULO_METODOS = {
    "game_methods": "logic",
    "rasterizer_methods": "render",
    "gamekeys_methods": "events",
    "physicsconstraints_methods": "constraints",
    "imgui_methods": "imgui",
    "g_methods": "network",
    "steamMethods": "network.steam",
    "moduleMethods": "texture",
}
# nome do .rst -> módulo
RST_MODULO = {"bge.app": "app", "bge.logic": "logic", "bge.render": "render",
              "bge.events": "events", "bge.constraints": "constraints",
              "bge.texture": "texture"}

RE_TABELA_CLASSE = re.compile(r"(PyMethodDef|PyAttributeDef)\s+(\w+)::(Methods|Attributes)\s*\[\]\s*=\s*\{(.*?)\n\};", re.S)
RE_TABELA_LIVRE = re.compile(r"PyMethodDef\s+(\w+)\s*\[\]\s*=\s*\{(.*?)\n\s*\};", re.S)
RE_METODO = re.compile(r'\{\s*"(\w+)"\s*,|EXP_PYMETHODTABLE\w*\(\s*\w+\s*,\s*(\w+)\s*\)')
RE_ATRIB = re.compile(r'(EXP_PYATTRIBUTE_\w+)\(\s*"(\w+)"')
RE_CONST = re.compile(r'KX_MACRO_addTypesToDict\(\s*\w+\s*,\s*(\w+)\s*,')
RE_CONST_FN = re.compile(r'KX_MACRO_addTypesToDict_fn\(\s*\w+\s*,\s*"(\w+)"')
RE_MODCREATE = re.compile(r'PyModule_Create\(\s*&\s*(\w+)\s*\)')


def sem_comentarios(txt):
    txt = re.sub(r"/\*.*?\*/", "", txt, flags=re.S)
    return re.sub(r"//[^\n]*", "", txt)


def ler_cpp():
    classes, modulos = {}, {}
    for arq in CPP.rglob("*.cpp"):
        txt = sem_comentarios(arq.read_text(encoding="utf-8", errors="replace"))
        rel = arq.relative_to(RAIZ).as_posix()
        for tipo, cls, _, corpo in RE_TABELA_CLASSE.findall(txt):
            c = classes.setdefault(cls, {"arquivo": rel, "metodos": {}, "atributos": {}})
            if tipo == "PyMethodDef":
                for a, b in RE_METODO.findall(corpo):
                    nome = a or b
                    if nome and not nome.startswith("__"):
                        c["metodos"][nome] = {}
            else:
                for macro, nome in RE_ATRIB.findall(corpo):
                    c["atributos"][nome] = {"so_leitura": "_RO" in macro}
        for tabela, corpo in RE_TABELA_LIVRE.findall(txt):
            mod = MODULO_METODOS.get(tabela)
            if not mod:
                continue
            m = modulos.setdefault(mod, {"arquivo": rel, "funcoes": {}, "constantes": {}})
            for a, _b in RE_METODO.findall(corpo):
                if a and not a.startswith("__"):
                    m["funcoes"][a] = {}
        # constantes: pertencem ao último PyModule_Create visto no arquivo
        atual = None
        for linha in txt.splitlines():
            mc = RE_MODCREATE.search(linha)
            if mc:
                atual = MODULO_DEF.get(mc.group(1))
            if atual:
                for nome in RE_CONST.findall(linha) + RE_CONST_FN.findall(linha):
                    m = modulos.setdefault(atual, {"arquivo": rel, "funcoes": {}, "constantes": {}})
                    m["constantes"][nome] = {}
    return classes, modulos


# ---------------------------------------------------------------- cobertura RNA -> API Python

def _bloco_funcao(texto, nome):
    """Corpo de uma função C/C++, sem depender de uma quantidade fixa de linhas."""
    inicio = texto.find(nome)
    if inicio < 0:
        return ""
    abre = texto.find("{", inicio)
    if abre < 0:
        return ""
    nivel = 0
    for i in range(abre, len(texto)):
        if texto[i] == "{":
            nivel += 1
        elif texto[i] == "}":
            nivel -= 1
            if nivel == 0:
                return texto[abre + 1:i]
    return ""


def _rna_props(arquivo, funcao):
    texto = arquivo.read_text(encoding="utf-8", errors="replace")
    bloco = _bloco_funcao(texto, funcao)
    return sorted(set(re.findall(r'RNA_def_property\(srna,\s*"([^"]+)"', bloco)))


def _camel(nome):
    partes = nome.split("_")
    return partes[0] + "".join(p.capitalize() for p in partes[1:])


def auditoria_cobertura(classes):
    """Compara controles de runtime visíveis no editor com bindings Python.

    Isto não decide que todo controle RNA *deve* virar API: mostra a lacuna
    para revisão humana. A lista é deliberadamente restrita a estruturas de
    jogo, evitando a enorme quantidade de RNA genérico do editor Blender.
    """
    rna_obj = RAIZ / "source" / "source" / "blender" / "makesrna" / "intern" / "rna_object.c"
    rna_world = RAIZ / "source" / "source" / "blender" / "makesrna" / "intern" / "rna_world.c"
    world_cpp = CPP / "Ketsji" / "KX_WorldInfo.cpp"

    def itens(classe):
        return set(classes.get(classe, {}).get("metodos", {})) | set(classes.get(classe, {}).get("atributos", {}))

    # Nomes que intencionalmente diferem entre RNA (snake_case) e a API atual.
    aliases_particulas = {
        "particle_count": "particleCount", "emitter_position": "emitterPosition",
        "emitter_radius": "emitterRadius", "velocity_randomness": "velocityRandomness",
        "end_color": "endColor", "end_size": "endSize", "emission_direction": "emissionDirection",
        "emission_angle": "emissionAngle", "collision_mode": "collisionMode",
        "collision_height": "collisionHeight", "collision_bounce": "collisionBounce",
        "collision_friction": "collisionFriction", "fragment_shader_path": "fragmentShaderPath",
        "burst_interval": "burstInterval",
    }
    aliases_explosao = {
        "burst_speed": "burstSpeed", "debris_lifetime": "debrisLifetime",
        "use_break_on_collision": "useBreakOnCollision", "use_inherit_velocity": "useInheritVelocity",
        "impact_impulse": "impactImpulse", "use_explode_on_impact": "useExplodeOnImpact",
        "use_chain_reaction": "useChainReaction", "dent_impulse": "dentImpulse",
        "use_dent_on_collision": "useDentOnCollision", "bend_axis": "bendAxis",
        "bend_angle": "bendAngle", "bend_max_angle": "bendMaxAngle",
        "decal_size": "decalSize", "decal_life": "decalLife", "max_decals": "maxDecals",
        # Prefixados na API: radius/force/effect/mark sozinhos seriam ambíguos em KX_GameObject.
        "radius": "explosionRadius", "force": "explosionForce",
        "effect": "explosionEffect", "mark": "groundMark",
    }

    def grupo(nome, props, disponiveis, aliases=None, editor=()):
        aliases = aliases or {}
        linhas = []
        for prop in props:
            if prop in editor or prop.startswith("show_"):
                estado, api = "editor", ""
            else:
                api = aliases.get(prop, _camel(prop))
                estado = "exposto" if api in disponiveis else "sem_binding"
            linhas.append({"controle_rna": prop, "api": api, "estado": estado})
        return {"nome": nome, "itens": linhas}

    particulas = _rna_props(rna_obj, "rna_def_object_gpu_particles")
    explosao = _rna_props(rna_obj, "rna_def_object_explosive")

    # setWeather/getWeather aceitam um vocabulário próprio; extrai-o do C++ em
    # vez de confundir uma propriedade RNA presente no painel com acesso runtime.
    texto_world = world_cpp.read_text(encoding="utf-8", errors="replace")
    bloco_weather = _bloco_funcao(texto_world, "SetWeatherRuntimeProperty") + _bloco_funcao(texto_world, "GetWeatherRuntimeProperty")
    weather_api = set(re.findall(r'"(?:weather\\.)?([a-z][a-z0-9_]*)"', bloco_weather))
    weather_props = [p for p in _rna_props(rna_world, "rna_def_world_weather")
                     if not p.startswith("show_") and (p.startswith(("vfog_", "vcloud_", "cloud_")) or p.startswith("use_"))]
    weather_aliases = {
        "use_vfog": "vfog", "use_volumetric_fog": "vfog", "use_clouds": "clouds",
        "use_rain": "rain", "use_rain_ripple": "ripples", "use_rain_droplets": "droplets",
        "use_rain_splash": "splash", "use_rain_puddles": "puddles",
        "use_rain_puddle_ssr": "puddle_ssr", "use_rain_ripple_puddle_only": "ripple_puddle_only",
        "use_rain_splash_puddle_only": "splash_puddle_only", "use_rain_aura": "aura",
        "use_rain_lightning": "lightning", "use_rain_lightning_side": "lightning_side",
        "use_lens_flare": "lens_flare", "use_earthquake": "earthquake",
        "vfog_color": ("vfog_color_r", "vfog_color_g", "vfog_color_b"),
        "cloud_color": ("cloud_color_r", "cloud_color_g", "cloud_color_b"),
        "vcloud_color": ("vcloud_color_r", "vcloud_color_g", "vcloud_color_b"),
    }
    weather_linhas = []
    for prop in weather_props:
        chave = weather_aliases.get(prop, prop)
        # O nome público omite o prefixo weather., mas mantém vfog_/vcloud_.
        chaves = (chave,) if isinstance(chave, str) else chave
        exposto = all(nome in weather_api for nome in chaves)
        api = "setWeather/getWeather(" + ", ".join(chaves) + ")" if exposto else ""
        weather_linhas.append({"controle_rna": prop, "api": api,
                               "estado": "exposto" if exposto else "sem_binding"})

    return {
        "grupos": [
            grupo("Partículas GPU", particulas, itens("KX_ParticleSystem"), aliases_particulas,
                  editor=("show_expanded",)),
            grupo("Explosão", explosao, itens("KX_GameObject"), aliases_explosao,
                  editor=("show_expanded",)),
            {"nome": "Clima do World", "itens": weather_linhas},
        ]
    }


def relatorio_cobertura(auditoria):
    totais = {"exposto": 0, "sem_binding": 0, "editor": 0}
    for grupo in auditoria["grupos"]:
        for item in grupo["itens"]:
            totais[item["estado"]] += 1
    out = ["# Cobertura Python dos controles de jogo", "",
           "Gerado por `tools/api_inventario.py`. Compara somente controles RNA de recursos de jogo "
           "com bindings Python; não afirma que todo controle do editor deve virar API.", "",
           f"**Total:** {totais['exposto']} expostos · {totais['sem_binding']} sem binding · "
           f"{totais['editor']} só de editor.", ""]
    for grupo in auditoria["grupos"]:
        out += [f"## {grupo['nome']}", "", "| Controle RNA/editor | API Python encontrada | Estado |",
                "|---|---|---|"]
        for item in grupo["itens"]:
            estado = {"exposto": "exposto", "sem_binding": "**sem binding**", "editor": "editor"}[item["estado"]]
            out.append(f"| `{item['controle_rna']}` | `{item['api']}` | {estado} |")
        out.append("")
    return "\n".join(out)


RE_DIRETIVA = re.compile(r"^(\s*)\.\. (class|method|attribute|function|data)::\s*([\w.]+)")


def ler_rst():
    """Devolve {classe: {nome: documentado}} e {modulo: {nome: documentado}}."""
    classes, modulos = {}, {}
    arquivos = list(RST.glob("bge.*.rst")) + list((RST / "bge_types").glob("*.rst"))
    for arq in arquivos:
        linhas = arq.read_text(encoding="utf-8", errors="replace").splitlines()
        mod = RST_MODULO.get(arq.stem)
        cls_atual = None
        for i, linha in enumerate(linhas):
            d = RE_DIRETIVA.match(linha)
            if not d:
                continue
            recuo, tipo, nome = len(d.group(1)), d.group(2), d.group(3).split(".")[-1]
            # documentado = existe texto no bloco abaixo da diretiva
            texto = False
            for prox in linhas[i + 1:i + 8]:
                if RE_DIRETIVA.match(prox):
                    break
                s = prox.strip()
                if s and not s.startswith(":"):
                    texto = True
                    break
                if s.startswith(":type:") or s.startswith(":arg") or s.startswith(":return"):
                    texto = True
            if tipo == "class":
                cls_atual = nome
                classes.setdefault(nome, {})
            elif recuo > 0 and cls_atual:
                classes[cls_atual][nome] = texto
            elif mod:
                modulos.setdefault(mod, {})[nome] = texto
    return classes, modulos


# Commit que trouxe o código-fonte da engine para o repo. O que já existia nele
# pode ser da Range original ou das primeiras mudanças da Anastacio.
COMMIT_SNAPSHOT = "28775369"


def origem(nome, arquivo):
    """Primeiro commit em que '"nome"' aparece no arquivo (git log -S)."""
    r = subprocess.run(["git", "log", "--reverse", "--format=%h %ad", "--date=short",
                        "-S", f'"{nome}"', "--", arquivo],
                       cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    linha = (r.stdout.splitlines() or [""])[0]
    if not linha:
        return {"origem": "desconhecida"}
    commit, data = linha.split()
    if commit.startswith(COMMIT_SNAPSHOT):
        return {"origem": "snapshot", "commit": commit}
    return {"origem": "anastacio", "commit": commit, "data": data}


def marcar_origem(resultado):
    for grupo in ("classes", "modulos"):
        for v in resultado[grupo].values():
            for nome, item in v["itens"].items():
                if item["status"] == "novo":
                    item.update(origem(nome, v["arquivo"]))


def chave(cls):
    """Range renomeou várias classes (SCA_PythonMouse -> KX_PythonMouse,
    KX_SCA_AddObjectActuator -> KX_AddObjectActuator); compara sem prefixo."""
    return re.sub(r"^(KX_SCA_|KX_|SCA_|BL_|EXP_)", "", cls)


def status(nome, doc):
    if nome not in doc:
        return "novo"
    return "documentado" if doc[nome] else "sem_doc"


def main():
    cpp_cls, cpp_mod = ler_cpp()
    rst_cls, rst_mod = ler_rst()
    resultado = {"classes": {}, "modulos": {}}

    rst_por_chave = {chave(c): (c, d) for c, d in rst_cls.items()}
    for cls, info in sorted(cpp_cls.items()):
        nome_rst, doc = rst_por_chave.get(chave(cls), (None, {}))
        itens = {}
        for nome in info["metodos"]:
            itens[nome] = {"tipo": "metodo", "status": status(nome, doc)}
        for nome, a in info["atributos"].items():
            itens[nome] = {"tipo": "atributo", "so_leitura": a["so_leitura"], "status": status(nome, doc)}
        for nome in doc:
            if nome not in itens:
                itens[nome] = {"tipo": "?", "status": "so_no_rst"}
        resultado["classes"][cls] = {"arquivo": info["arquivo"], "rst": nome_rst, "tem_rst": nome_rst is not None, "itens": itens}

    for mod, info in sorted(cpp_mod.items()):
        doc = rst_mod.get(mod, {})
        itens = {}
        for nome in info["funcoes"]:
            itens[nome] = {"tipo": "funcao", "status": status(nome, doc)}
        for nome in info["constantes"]:
            itens[nome] = {"tipo": "constante", "status": status(nome, doc)}
        for nome in doc:
            if nome not in itens:
                itens[nome] = {"tipo": "?", "status": "so_no_rst"}
        resultado["modulos"][mod] = {"arquivo": info["arquivo"], "tem_rst": mod in rst_mod, "itens": itens}

    if "--sem-origem" not in sys.argv:
        marcar_origem(resultado)

    SAIDA.mkdir(exist_ok=True)
    (SAIDA / "api_inventario.json").write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    (SAIDA / "api_inventario.md").write_text(relatorio(resultado), encoding="utf-8")
    cobertura = auditoria_cobertura(cpp_cls)
    (SAIDA / "cobertura_python.json").write_text(json.dumps(cobertura, indent=1, ensure_ascii=False), encoding="utf-8")
    (SAIDA / "cobertura_python.md").write_text(relatorio_cobertura(cobertura), encoding="utf-8")
    sem_binding = sum(1 for grupo in cobertura["grupos"] for item in grupo["itens"]
                      if item["estado"] == "sem_binding")
    print(f"{resumo_total(resultado)} | cobertura: {sem_binding} controles sem binding")


def contar(itens):
    c = {"documentado": 0, "sem_doc": 0, "novo": 0, "so_no_rst": 0}
    for i in itens.values():
        c[i["status"]] += 1
    return c


def resumo_total(r):
    tot = {"documentado": 0, "sem_doc": 0, "novo": 0, "so_no_rst": 0}
    for grupo in ("classes", "modulos"):
        for v in r[grupo].values():
            for k, n in contar(v["itens"]).items():
                tot[k] += n
    return (f"{len(r['classes'])} classes, {len(r['modulos'])} módulos | "
            f"documentados {tot['documentado']} · sem doc {tot['sem_doc']} · "
            f"novos {tot['novo']} · só no rst {tot['so_no_rst']}")


def relatorio(r):
    out = ["# Inventário da API Python", "",
           "Gerado por `tools/docs/api_inventario.py`. Módulos expostos como `Range.<módulo>` e `bge.<módulo>`.", "",
           f"**Total:** {resumo_total(r)}", "",
           "Legenda: **novo** = existe no C++ e não está no rst (provável função da Anastacio); "
           "**sem doc** = está no rst sem descrição; **só no rst** = documentado mas não achado no C++ "
           "(removido, herdado de classe base ou definido de outro jeito).", ""]
    for titulo, grupo, prefixo in (("Módulos", "modulos", "Range."), ("Classes (Range.types)", "classes", "")):
        out += [f"## {titulo}", "", "| Nome | Itens | Documentados | Sem doc | Novos | Só no rst | rst? |",
                "|---|---:|---:|---:|---:|---:|:---:|"]
        for nome, v in sorted(r[grupo].items(), key=lambda kv: -contar(kv[1]["itens"])["novo"]):
            c = contar(v["itens"])
            out.append(f"| `{prefixo}{nome}` | {len(v['itens'])} | {c['documentado']} | {c['sem_doc']} | "
                       f"{c['novo']} | {c['so_no_rst']} | {'sim' if v['tem_rst'] else '**não**'} |")
        out.append("")
    ana = sum(1 for g in ("classes", "modulos") for v in r[g].values()
              for i in v["itens"].values() if i.get("origem") == "anastacio")
    snap = sum(1 for g in ("classes", "modulos") for v in r[g].values()
               for i in v["itens"].values() if i.get("origem") == "snapshot")
    out += ["## Itens novos por classe/módulo", "",
            f"Origem pelo git: **{ana}** adicionados depois de 15/09/2026 (Anastacio, marcados com ✦data); "
            f"**{snap}** já estavam no snapshot inicial do código (Range sem doc ou Anastacio antiga, precisa confirmar).", ""]
    for grupo, prefixo in (("modulos", "Range."), ("classes", "")):
        for nome, v in sorted(r[grupo].items()):
            novos = [f"`{n}`" + (" (só leitura)" if i.get("so_leitura") else "")
                     + (f" ✦{i['data']}" if i.get("origem") == "anastacio" else "")
                     for n, i in v["itens"].items() if i["status"] == "novo"]
            if novos:
                out.append(f"- **{prefixo}{nome}** ({v['arquivo']}): " + ", ".join(novos))
    out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    main()
