"""Monta um objeto com física e tira prints da janela Properties nas abas Object e Physics.
Uso: AnastacioEngine.exe -p 0 0 1600 900 --python properties.py -- <pasta_saida>"""
import bpy, sys, os

OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "."
os.makedirs(OUT, exist_ok=True)


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


# (passo, contexto da aba ou None, rolagem em linhas, arquivo)
PASSOS = {
    4: ('OBJECT', None, "janela.png"),
    7: ('PHYSICS', None, "physics.png"),
    10: ('PHYSICS', 60, "physics-damage.png"),
}


class PrintProps(bpy.types.Operator):
    bl_idname = "wm.print_props"
    bl_label = "Print Props"
    passo = 0

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
        self.passo += 1
        p = self.passo
        win = self.win
        scr = win.screen
        area = max(scr.areas, key=lambda a: a.width * a.height)
        ov = {'window': win, 'screen': scr, 'area': area}
        if p == 1:
            bpy.ops.screen.screen_full_area(ov)
        elif p == 2:
            area.spaces.active.context = 'OBJECT'
        elif p in PASSOS:
            contexto, rolagem, arquivo = PASSOS[p]
            area.spaces.active.context = contexto
            if rolagem:
                reg = [r for r in area.regions if r.type == 'WINDOW'][0]
                for _ in range(rolagem):
                    bpy.ops.view2d.scroll_down(dict(ov, region=reg))
            bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, arquivo), full=True)
        elif p == 12:
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
