"""Prints do guia Box Impostor (painel + objeto real ao lado do card), pelo controle.py (editor invisível).
Uso: python box_impostor.py <pasta_saida>"""
import os, sys, time, json
from pathlib import Path
from PIL import Image

sys.path.insert(0, r"D:\AnastacioEngine\tools\testes_engine")
os.environ.setdefault("ANASTACIO_CONTROLE_PASTA", r"D:\AnastacioEngine\artifacts\testes\controle_prints_impostor")
import controle  # noqa: E402

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT.mkdir(parents=True, exist_ok=True)
PASTA = r"D:\TestesBoxImpostor"


def py(ed, codigo):
    r = ed.pedir('py', codigo=codigo)
    if not r['ok']:
        raise RuntimeError(r.get('traceback') or r['erro'])
    return r['resultado']


def tela(ed, nome, area_tipo=None, margem=0):
    bruto = OUT / ("_" + nome + ".png")
    time.sleep(0.6)
    r = ed.pedir('tela', arquivo=str(bruto))
    assert r['ok'], r
    img = Image.open(bruto)
    if area_tipo:
        info = json.loads(py(ed, f"""import json
win = bpy.context.window_manager.windows[0]
a = max((a for a in win.screen.areas if a.type == {area_tipo!r}), key=lambda a: a.width * a.height)
resultado = json.dumps([a.x, a.y, a.width, a.height, win.height])"""))
        x, y, w, h, wh = info
        img = img.crop((x, wh - y - h, x + w, wh - y))
    img.save(OUT / (nome + ".png"))
    bruto.unlink()
    print("ok", nome)


CENA = r'''
import bpy, os, shutil
P = PASTA
shutil.rmtree(P, ignore_errors=True); os.makedirs(P)
sc = bpy.context.scene
sc.render.engine = 'BLENDER_GAME'
for ob in list(sc.objects):
    if ob.type == 'MESH':
        bpy.data.objects.remove(ob, do_unlink=True)
win = bpy.context.window_manager.windows[0]
v3d = next(a for a in win.screen.areas if a.type == 'VIEW_3D')
ctx = dict(window=win, screen=win.screen, area=v3d, region=next(r for r in v3d.regions if r.type == 'WINDOW'),
           scene=sc)
bpy.ops.mesh.primitive_plane_add(ctx, radius=8, location=(0, 0, 0))
chao = bpy.context.scene.objects.active
mc = bpy.data.materials.new("Chao"); mc.diffuse_color = (0.55, 0.55, 0.52); chao.data.materials.append(mc)
bpy.ops.mesh.primitive_monkey_add(ctx, location=(-1.4, 0, 1.1))
mono = bpy.context.scene.objects.active
mono.name = "Monkey"
mono.rotation_euler = (0, 0, 0.5)
m = mono.modifiers.new("Sub", 'SUBSURF'); m.levels = 2
bpy.ops.object.modifier_apply(dict(ctx, object=mono, active_object=mono), modifier="Sub")
bpy.ops.object.shade_smooth(dict(ctx, object=mono, active_object=mono, selected_editable_objects=[mono]))
mat = bpy.data.materials.new("Laranja"); mat.diffuse_color = (0.9, 0.42, 0.12); mat.specular_intensity = 0.3
mono.data.materials.append(mat)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(P, "impostor.range"))
for o in sc.objects: o.select = False
mono.select = True; sc.objects.active = mono
'''.replace("PASTA", repr(PASTA))

PAINEL = r'''
import bpy
from bl_ui import properties_game_object as pgo
for cls in (pgo.OBJECT_PT_box_impostor,):
    bpy.utils.unregister_class(cls); cls.bl_options = set(); bpy.utils.register_class(cls)
bpy.context.window_manager.ae_object_panel_category = 'GAME'
def todas(c):
    for sub in c.__subclasses__():
        yield sub
        yield from todas(sub)
manter = {"Levels of Detail - LOD", "Flat Impostor (Billboard)", "Box Impostor", "Object"}
for cls in set(todas(bpy.types.Panel)):
    if getattr(cls, "bl_space_type", "") == 'PROPERTIES' and getattr(cls, "bl_context", "") == 'object'             and getattr(cls, "bl_label", "") not in manter and getattr(cls, "is_registered", False):
        try:
            bpy.utils.unregister_class(cls)
        except Exception:
            pass
win = bpy.context.window_manager.windows[0]
for a in win.screen.areas:
    if a.type == 'PROPERTIES':
        a.spaces.active.context = 'OBJECT'
        a.tag_redraw()
'''

ROLAR = r'''
import bpy
win = bpy.context.window_manager.windows[0]
a = next(a for a in win.screen.areas if a.type == 'PROPERTIES')
reg = next(r for r in a.regions if r.type == 'WINDOW')
for _ in range(40):
    bpy.ops.view2d.scroll_down(dict(window=win, screen=win.screen, area=a, region=reg), deltay=40)
a.tag_redraw()
'''

BAKE = r'''
import bpy
win = bpy.context.window_manager.windows[0]
sc = bpy.context.scene
mono = sc.objects["Monkey"]
v3d = next(a for a in win.screen.areas if a.type == 'VIEW_3D')
ctx = dict(window=win, screen=win.screen, area=v3d, scene=sc, object=mono, active_object=mono)
resultado = str(bpy.ops.object.bake_box_impostor(ctx, resolution='256', mode='AUTO', use_lod=True, lod_distance=30.0))
'''

VISTA = r'''
import bpy, math
win = bpy.context.window_manager.windows[0]
sc = bpy.context.scene
card = sc.objects["Monkey_box_impostor"]
copia = card.copy()
sc.objects.link(copia)
copia.layers = [i == 0 for i in range(20)]
copia.location = (1.4, 0, 1.1)
copia.parent = None
sc.objects["Monkey"].select = False
for a in win.screen.areas:
    if a.type == 'VIEW_3D':
        s = a.spaces.active
        s.viewport_shade = 'MATERIAL'
        s.show_floor = False
        s.show_manipulator = False
        s.show_only_render = True
        r = s.region_3d
        r.view_perspective = 'PERSP'
        r.view_location = (0, 0, 1.0)
        r.view_distance = 6.5
        from mathutils import Euler
        r.view_rotation = Euler((math.radians(72), 0, math.radians(ANG))).to_quaternion()
        a.tag_redraw()
'''


def rodar():
    controle.abrir(None)
    ed = controle.Editor()
    try:
        py(ed, CENA)
        py(ed, PAINEL)
        tela(ed, "box_impostor_painel", "PROPERTIES")
        print("bake:", py(ed, BAKE))
        py(ed, "import bpy\nbpy.ops.wm.save_mainfile()")
        tela(ed, "box_impostor_painel_depois", "PROPERTIES")
        py(ed, VISTA.replace("ANG", "20"))
        tela(ed, "box_impostor_lado_a_lado", "VIEW_3D")
        py(ed, "import bpy, math\nfrom mathutils import Euler\nwin=bpy.context.window_manager.windows[0]\n"
               "r=next(a for a in win.screen.areas if a.type=='VIEW_3D').spaces.active.region_3d\n"
               "r.view_rotation = Euler((math.radians(25), 0, math.radians(-40))).to_quaternion()")
        tela(ed, "box_impostor_de_cima", "VIEW_3D")
    finally:
        try:
            ed.pedir('fechar')
        except Exception:
            pass


rodar()
