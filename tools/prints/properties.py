"""Monta um objeto com física e tira prints da janela Properties.
Uso: AnastacioEngine.exe -p 0 0 1600 900 --python properties.py -- <pasta_saida>"""
import bpy, sys, os, json

OUT = os.path.abspath(sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else ".")
os.makedirs(OUT, exist_ok=True)
bpy.context.user_preferences.view.show_splash = False


def montar_cena():
    ob = bpy.context.scene.objects.get("Cube") or bpy.context.active_object
    ob.name = "Player"
    bpy.context.scene.objects.active = ob
    ob.select = True
    ob.game.physics_type = 'DYNAMIC'
    ob.game.mass = 2.0
    ob.game.friction = 0.6
    ob.game.elasticity = 0.2
    bpy.ops.object.game_property_new(type='INT', name="vida")
    bpy.ops.object.game_property_new(type='FLOAT', name="velocidade")


# cada item: (contexto, categoria_object, categoria_physics, arquivo, salvar_json)
PASSOS = [
    ('OBJECT', 'OBJECT', None, "janela.png", True),
    ('OBJECT', 'OBJECT', None, "abas.png", False),
    ('OBJECT', 'GAME', None, "categorias.png", False),
    ('PHYSICS', None, 'PHYSICS', "physics.png", False),
    ('GAME', None, None, "game-components.png", False),
    ('PHYSICS', None, 'DAMAGE', "physics-damage.png", False),
]


class PrintProps(bpy.types.Operator):
    bl_idname = "wm.print_props"
    bl_label = "Print Props"
    passo = 0
    indice = 0
    aguardando = False

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
        self.passo += 1
        win = self.win
        scr = win.screen
        area = max(scr.areas, key=lambda a: a.width * a.height)
        ov = {'window': win, 'screen': scr, 'area': area}
        if self.passo < 3:
            return {'RUNNING_MODAL'}
        if self.aguardando:
            contexto, cat_obj, cat_phys, arquivo, salvar_json = PASSOS[self.indice]
            res = bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, arquivo), full=True)
            print("SHOT", arquivo, res, flush=True)
            if salvar_json:
                info = {"area": [area.x, area.y, area.width, area.height],
                        "regions": {r.type: [r.x, r.y, r.width, r.height] for r in area.regions},
                        "win": [win.width, win.height]}
                json.dump(info, open(os.path.join(OUT, "properties.json"), "w"), indent=1)
            self.aguardando = False
            self.indice += 1
        elif self.indice < len(PASSOS):
            contexto, cat_obj, cat_phys, arquivo, salvar_json = PASSOS[self.indice]
            area.spaces.active.context = contexto
            if cat_obj:
                context.window_manager.ae_object_panel_category = cat_obj
            if cat_phys:
                context.window_manager.ae_physics_panel_category = cat_phys
            self.aguardando = True
        else:
            bpy.ops.wm.quit_blender()
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.win = context.window_manager.windows[0]
        area = max(self.win.screen.areas, key=lambda a: a.width * a.height)
        area.type = 'PROPERTIES'
        wm = context.window_manager
        self._t = wm.event_timer_add(0.7, self.win)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}


bpy.utils.register_class(PrintProps)
montar_cena()
w = bpy.context.window_manager.windows[0]
bpy.ops.wm.print_props({'window': w, 'screen': w.screen})
