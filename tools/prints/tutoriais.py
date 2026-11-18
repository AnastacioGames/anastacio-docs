"""Prints do guia de Tutoriais e Help (janela, detalhes, cartão do passo, menu About, "i" e popup do Help).
Uso: python tutoriais.py <pasta_saida>  (editor invisível pelo controle.py)"""
import os, sys, time, json
from pathlib import Path
from PIL import Image

sys.path.insert(0, r"D:\AnastacioEngine\tools\testes_engine")
os.environ.setdefault("ANASTACIO_CONTROLE_PASTA", r"D:\AnastacioEngine\artifacts\testes\controle_prints_tutoriais")
import controle  # noqa: E402

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT.mkdir(parents=True, exist_ok=True)


def py(ed, codigo):
    r = ed.pedir('py', codigo=codigo)
    if not r['ok']:
        raise RuntimeError(r.get('traceback') or r['erro'])
    return r['resultado']


def tela(ed, nome, caixa=None, area=None):
    bruto = OUT / ("_" + nome + ".png")
    time.sleep(0.8)
    r = ed.pedir('tela', arquivo=str(bruto))
    assert r['ok'], r
    img = Image.open(bruto)
    wh = int(py(ed, "resultado = bpy.context.window_manager.windows[0].height"))
    if caixa:
        x0, y0, x1, y1 = caixa
        img = img.crop((int(x0) - 2, wh - int(y1) - 2, int(x1) + 2, wh - int(y0) + 2))
    elif area:
        x, y, w, h = area
        img = img.crop((x, wh - y - h, x + w, wh - y))
    img.save(OUT / (nome + ".png"))
    bruto.unlink()
    print("ok", nome)


JANELA = r'''
import bpy, range_tutorials as rt, range_tutorials_janela as rj
rt._escolher_idioma(IDIOMA)
win = bpy.context.window_manager.windows[0]
rj._fechar(bpy.context)
bpy.ops.wm.range_tutorials_window(dict(window=win, screen=win.screen), 'INVOKE_DEFAULT')
rj.janela["mouse"] = (-1, -1)
'''


def caixa_janela(ed):
    return json.loads(py(ed, "import json, range_tutorials_janela as rj\nresultado = json.dumps(list(rj.janela['caixa']))"))


def area(ed, tipo):
    return json.loads(py(ed, f"""import json
win = bpy.context.window_manager.windows[0]
a = max((a for a in win.screen.areas if a.type == {tipo!r}), key=lambda a: a.width * a.height)
resultado = json.dumps([a.x, a.y, a.width, a.height])"""))


def rodar(idioma):
    controle.abrir(None)
    ed = controle.Editor()
    try:
        py(ed, JANELA.replace("IDIOMA", repr(idioma)))
        tela(ed, f"tutoriais_janela_{idioma}", caixa_janela(ed))
        # Categoria Básico, um tutorial escolhido (detalhes à direita)
        py(ed, "import range_tutorials_janela as rj\nrj.janela['cat'] = 1\nrj.janela['tut'] = 'basico_primeiro_jogo'\n"
               "import range_tutorials as rt\nrt._redesenhar()")
        tela(ed, f"tutoriais_detalhes_{idioma}", caixa_janela(ed))
        py(ed, "import bpy, range_tutorials_janela as rj\nrj._fechar(bpy.context)")
        if idioma != "pt":
            return
        # Cartão do passo dentro do editor
        py(ed, "import bpy\nwin = bpy.context.window_manager.windows[0]\n"
               "bpy.ops.wm.range_tutorial_start(dict(window=win, screen=win.screen), 'INVOKE_DEFAULT', "
               "name='basico_primeiro_jogo', step=0, scene_loaded=True)")
        time.sleep(4)
        tela(ed, "tutoriais_cartao_pt")
        py(ed, "import bpy\nwin = bpy.context.window_manager.windows[0]\n"
               "bpy.ops.wm.range_tutorial_stop(dict(window=win, screen=win.screen))")
        # Menu About
        py(ed, "import bpy\nwin = bpy.context.window_manager.windows[0]\n"
               "bpy.context.window_manager.range_help_on = True\n"
               "bpy.ops.wm.call_menu(dict(window=win, screen=win.screen, area=next(a for a in win.screen.areas if a.type=='INFO')), name='INFO_MT_help')")
        time.sleep(0.6)
        ed.pedir('evento', tipo='MOUSEMOVE', valor='NOTHING', x=110, y=91)
        time.sleep(1.2)
        tela(ed, "tutoriais_menu_about")
        ed.pedir('evento', tipo='ESC', valor='PRESS', x=900, y=500)
        ed.pedir('evento', tipo='ESC', valor='RELEASE', x=900, y=500)
        # "i" nos painéis (aba Render)
        py(ed, "import bpy\nwin = bpy.context.window_manager.windows[0]\n"
               "for a in win.screen.areas:\n    if a.type == 'PROPERTIES':\n        a.spaces.active.context = 'RENDER'\n        a.tag_redraw()")
        tela(ed, "tutoriais_help_i", area=area(ed, "PROPERTIES"))
    finally:
        try:
            ed.pedir('fechar')
        except Exception:
            pass
        time.sleep(2)


for idioma in ("pt", "en"):
    rodar(idioma)
