"""Prints dos guias Text Editor com editor externo e Converter imagem para DDS (editor invisível, controle.py).
Uso: python editor_externo_dds.py <pasta_saida>"""
import os, sys, time, json
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0, r"D:\AnastacioEngine\tools\testes_engine")
os.environ.setdefault("ANASTACIO_CONTROLE_PASTA", r"D:\AnastacioEngine\artifacts\testes\controle_prints_texto")
import controle  # noqa: E402

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT.mkdir(parents=True, exist_ok=True)
PASTA = Path(r"D:\TestesGuiasTextoDDS")


def py(ed, codigo):
    r = ed.pedir('py', codigo=codigo)
    if not r['ok']:
        raise RuntimeError(r.get('traceback') or r['erro'])
    return r['resultado']


def tela(ed, nome, tipo=None, caixa=None):
    bruto = OUT / ("_" + nome + ".png")
    time.sleep(0.8)
    r = ed.pedir('tela', arquivo=str(bruto))
    assert r['ok'], r
    img = Image.open(bruto)
    if tipo:
        x, y, w, h, wh = json.loads(py(ed, f"""import json
win = bpy.context.window_manager.windows[0]
a = max((a for a in win.screen.areas if a.type == {tipo!r}), key=lambda a: a.width * a.height)
resultado = json.dumps([a.x, a.y, a.width, a.height, win.height])"""))
        img = img.crop((x, wh - y - h, x + w, wh - y))
    if caixa:
        img = img.crop(caixa)
    img.save(OUT / (nome + ".png"))
    bruto.unlink()
    print("ok", nome)


SCRIPT = '''import Range


def main(cont):
    own = cont.owner
    teclado = Range.logic.keyboard
    if teclado.inputs[Range.events.SPACEKEY].activated:
        own.applyForce((0, 0, 400))
    own["pontos"] = own.get("pontos", 0) + 1
'''


def preparar_arquivos():
    import shutil
    shutil.rmtree(PASTA, ignore_errors=True)
    (PASTA / "scripts").mkdir(parents=True)
    (PASTA / "textures").mkdir()
    (PASTA / "scripts" / "pular.py").write_text(SCRIPT, encoding="utf-8")
    # Textura de tijolos 1024x1024 gerada aqui
    img = Image.new("RGB", (1024, 1024), (150, 70, 45))
    d = ImageDraw.Draw(img)
    for linha in range(0, 1024, 64):
        d.line([(0, linha), (1024, linha)], fill=(210, 200, 185), width=6)
        desloc = 0 if (linha // 64) % 2 == 0 else 64
        for col in range(desloc, 1024, 128):
            d.line([(col, linha), (col, linha + 64)], fill=(210, 200, 185), width=6)
    img.save(PASTA / "textures" / "tijolos.png")


TEXTO = r'''
import bpy
win = bpy.context.window_manager.windows[0]
sc = bpy.context.scene
sc.render.engine = 'BLENDER_GAME'
bpy.ops.wm.save_as_mainfile(filepath=r"PASTA\cena.range")
txt = bpy.data.texts.load(r"PASTA\scripts\pular.py")
a = max((a for a in win.screen.areas if a.type == 'VIEW_3D'), key=lambda a: a.width * a.height)
a.type = 'TEXT_EDITOR'
s = a.spaces.active
s.text = txt
s.show_line_numbers = True
s.show_syntax_highlight = True
txt.current_line_index = 9
reg = next(r for r in a.regions if r.type == 'WINDOW')
bpy.ops.text.properties(dict(window=win, screen=win.screen, area=a, region=reg, space_data=s, edit_text=txt))
a.tag_redraw()
'''.replace("PASTA", str(PASTA))

DDS = r'''
import bpy
win = bpy.context.window_manager.windows[0]
sc = bpy.context.scene
for a in win.screen.areas:
    if a.type == 'TEXT_EDITOR':
        a.type = 'VIEW_3D'
ob = sc.objects.get("Cube") or next(o for o in sc.objects if o.type == 'MESH')
for o in sc.objects: o.select = False
ob.select = True; sc.objects.active = ob
img = bpy.data.images.load(r"PASTA\textures\tijolos.png")
img.filepath = bpy.path.relpath(img.filepath)
tex = bpy.data.textures.new("Tijolos", 'IMAGE'); tex.image = img
mat = ob.active_material or bpy.data.materials.new("Parede")
if not ob.data.materials: ob.data.materials.append(mat)
slot = mat.texture_slots.add(); slot.texture = tex
mat.active_texture_index = list(mat.texture_slots).index(slot)
bpy.ops.wm.save_mainfile()
for a in win.screen.areas:
    if a.type == 'PROPERTIES':
        a.spaces.active.context = 'TEXTURE'
        a.tag_redraw()
'''.replace("PASTA", str(PASTA))


def rodar():
    preparar_arquivos()
    controle.abrir(None)
    ed = controle.Editor()
    try:
        py(ed, TEXTO)
        time.sleep(0.5)
        py(ed, "import bpy\nwin = bpy.context.window_manager.windows[0]\nfor a in win.screen.areas:\n"
               "    if a.type == 'TEXT_EDITOR':\n        a.spaces.active.top = 0\n        a.tag_redraw()")
        ed.pedir('evento', tipo='MOUSEMOVE', valor='NOTHING', x=150, y=600)
        time.sleep(0.5)
        tela(ed, "texto_editor_externo", "TEXT_EDITOR")
        py(ed, DDS)
        tela(ed, "dds_painel_antes", "PROPERTIES")
        # Diálogo com tamanho e qualidade
        py(ed, "import bpy\nwin = bpy.context.window_manager.windows[0]\n"
               "a = next(a for a in win.screen.areas if a.type == 'PROPERTIES')\n"
               "bpy.ops.game.prepare_texture_image(dict(window=win, screen=win.screen, area=a), 'INVOKE_DEFAULT', image_name='tijolos.png')")
        time.sleep(0.8)
        tela(ed, "dds_dialogo", caixa=(0, 0, 330, 135))
        ed.pedir('evento', tipo='ESC', valor='PRESS', x=900, y=500)
        ed.pedir('evento', tipo='ESC', valor='RELEASE', x=900, y=500)
        time.sleep(0.5)
        print("convert:", py(ed, "import bpy\nresultado = str(bpy.ops.game.prepare_texture_image('EXEC_DEFAULT', image_name='tijolos.png', max_size='1024', quality='10'))"))
        py(ed, "import bpy\nbpy.ops.wm.save_mainfile()")
        tela(ed, "dds_painel_depois", "PROPERTIES")
    finally:
        try:
            ed.pedir('fechar')
        except Exception:
            pass


rodar()
