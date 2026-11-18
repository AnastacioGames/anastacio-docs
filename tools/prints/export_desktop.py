"""Prints da janela Export to Desktop (pt e en), pelo controle.py do repo da engine (editor invisível).
Uso: python export_desktop.py <pasta_saida>"""
import os, sys, time, json
from pathlib import Path
from PIL import Image

sys.path.insert(0, r"D:\AnastacioEngine\tools\testes_engine")
os.environ.setdefault("ANASTACIO_CONTROLE_PASTA", r"D:\AnastacioEngine\artifacts\testes\controle_prints_export")
import controle  # noqa: E402

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT.mkdir(parents=True, exist_ok=True)
BASE = r"D:\TestesExportDesktop"

PREP = r'''
import bpy, os, sys
import range_tutorials as rt, range_export_desktop as red
rt._escolher_idioma(IDIOMA)
ctx = contexto()
def abrir(pagina):
    red._fechar()
    win = bpy.context.window_manager.windows[0]
    bpy.ops.wm.export_to_desktop(dict(ctx, window=win, screen=win.screen), 'INVOKE_DEFAULT', page=pagina)
'''

def py(ed, codigo):
    r = ed.pedir('py', codigo=codigo)
    if not r['ok']:
        raise RuntimeError(r.get('traceback') or r['erro'])
    return r['resultado']


def foto(ed, nome, menu=False):
    bruto = OUT / ("_" + nome + ".png")
    caixa = json.loads(py(ed, "import json, range_export_desktop as red\nresultado = json.dumps(list(red.estado.get('caixa', [])))") or "[]")
    win_h = int(py(ed, "resultado = bpy.context.window_manager.windows[0].height"))
    time.sleep(0.4)
    r = ed.pedir('tela', arquivo=str(bruto))
    assert r['ok'], r
    img = Image.open(bruto)
    if caixa and not menu:
        x0, y0, x1, y1 = caixa
        m = 2
        img = img.crop((int(x0) - m, win_h - int(y1) - m, int(x1) + m, win_h - int(y0) + m))
    img.save(OUT / (nome + ".png"))
    bruto.unlink()
    print("ok", nome)


def rodar(idioma):
    pasta = os.path.join(BASE, idioma)
    controle.abrir(None)
    ed = controle.Editor()
    try:
        py(ed, PREP.replace("IDIOMA", repr(idioma)) + f'''
import shutil
shutil.rmtree({pasta!r}, ignore_errors=True)
os.makedirs({pasta!r})
bpy.context.scene.render.engine = 'BLENDER_GAME'
bpy.ops.wm.save_as_mainfile(filepath=os.path.join({pasta!r}, 'MyGame.range'))
abrir(1)
''')
        foto(ed, f"export_desktop_projeto_{idioma}")
        proj = os.path.join(pasta, "MyGame")
        py(ed, PREP.replace("IDIOMA", repr(idioma)) + f'''
os.makedirs(os.path.join({proj!r}, 'data'))
bpy.ops.wm.save_as_mainfile(filepath=os.path.join({proj!r}, 'data', 'MyGame.range'))
abrir(1)
red._gravar('nome', 'My Game')
red._gravar('versao', '1.0.0')
red._runtime_ok = lambda alvo: True  # build local sem runtime Linux: no pacote os dois existem
exp = bpy.context.scene.rangearmor_export
exp.export_windows64 = exp.export_linux64 = True
''')
        foto(ed, f"export_desktop_jogo_{idioma}")
        py(ed, "import range_export_desktop as red\nred.estado['pagina'] = 2\nred.estado['mouse']=(-1,-1)")
        foto(ed, f"export_desktop_plataformas_{idioma}")
        py(ed, f'''import range_export_desktop as red, os
red.estado.update(pagina=3, erro=None, log=['Copying runtime for Linux64...'], saidas={{}},
    lista=['preparar', 'runtime', 'cook', 'package'],
    etapas={{'preparar': 'feito', 'runtime': 'feito', 'cook': 'andando'}})''')
        foto(ed, f"export_desktop_exportando_{idioma}")
        py(ed, f'''import range_export_desktop as red, os
proj = r'C:\Games\MyGame'
rel = os.path.join(proj, 'release')
red.estado.update(pagina=4, projeto=proj, saidas={{
    'Windows64': os.path.join(rel, 'My Game-1.0.0-Windows64'),
    'Linux64': os.path.join(rel, 'My Game-1.0.0-Linux64'),
    'Universal': os.path.join(rel, 'My Game-1.0.0-Universal')}})''')
        foto(ed, f"export_desktop_pronto_{idioma}")
        py(ed, "import range_export_desktop as red\nred._fechar()")
        if idioma == "en":
            py(ed, "win = bpy.context.window_manager.windows[0]\nbpy.ops.wm.call_menu(dict(contexto(), window=win, screen=win.screen), name='INFO_MT_file')")
            time.sleep(0.5)
            ed.pedir('evento', tipo='MOUSEMOVE', valor='NOTHING', x=120, y=585)
            time.sleep(0.3)
            foto(ed, "menu_file_desktop", menu=True)
            img = Image.open(OUT / "menu_file_desktop.png"); img.crop((0, 0, 340, 700)).save(OUT / "menu_file_desktop.png")
    finally:
        try:
            ed.pedir('fechar')
        except Exception:
            pass
        time.sleep(2)


for idioma in ("pt", "en"):
    rodar(idioma)
