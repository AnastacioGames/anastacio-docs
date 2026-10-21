"""Tira prints da 3D View com uma cena simples.
Uso: AnastacioEngine.exe -p 0 0 1600 900 --python view_3d.py -- <pasta_saida>"""
import bpy, sys, os, json

OUT = os.path.abspath(sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else ".")
os.makedirs(OUT, exist_ok=True)
bpy.context.user_preferences.view.show_splash = False


def montar_cena():
    ob = bpy.context.scene.objects.get("Cube") or bpy.context.active_object
    ob.name = "Player"
    bpy.context.scene.objects.active = ob
    ob.select = True
    bpy.ops.mesh.primitive_plane_add(radius=4, location=(0, 0, -1))
    bpy.context.scene.objects.active = ob
    ob.select = True


class PrintView3D(bpy.types.Operator):
    bl_idname = "wm.print_view3d"
    bl_label = "Print View3D"
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
        if p == 3:
            bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, "janela.png"), full=True)
            info = {"area": [area.x, area.y, area.width, area.height],
                    "regions": {r.type: [r.x, r.y, r.width, r.height] for r in area.regions},
                    "win": [win.width, win.height]}
            json.dump(info, open(os.path.join(OUT, "view_3d.json"), "w"), indent=1)
        elif p == 5:
            bpy.ops.wm.quit_blender()
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.win = context.window_manager.windows[0]
        wm = context.window_manager
        self._t = wm.event_timer_add(0.7, self.win)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}


bpy.utils.register_class(PrintView3D)
montar_cena()
w = bpy.context.window_manager.windows[0]
bpy.ops.wm.print_view3d({'window': w, 'screen': w.screen})
