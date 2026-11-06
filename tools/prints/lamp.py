"""Print do painel da Lamp, com os tipos de luz.
Uso: AnastacioEngine.exe -p 0 0 1600 900 --python lamp.py -- <pasta_saida>"""
import bpy, sys, os, json

OUT = os.path.abspath(sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else ".")
os.makedirs(OUT, exist_ok=True)
bpy.context.user_preferences.view.show_splash = False


class PrintLamp(bpy.types.Operator):
    bl_idname = "wm.print_lamp"
    bl_label = "Print Lamp"
    passo = 0

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
        self.passo += 1
        win = self.win
        area = next(a for a in win.screen.areas if a.type == 'PROPERTIES')  # coluna normal, sem esticar
        if self.passo == 4:
            area.spaces.active.context = 'DATA'
        elif self.passo == 8:
            ov = {'window': win, 'screen': win.screen, 'area': area}
            print("SHOT", bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, "lamp.png"), full=True), flush=True)
            json.dump({"area": [area.x, area.y, area.width, area.height], "win": [win.width, win.height]},
                      open(os.path.join(OUT, "lamp.json"), "w"))
        elif self.passo == 10:
            bpy.ops.wm.quit_blender()
            return {'FINISHED'}
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.win = context.window_manager.windows[0]
        self.timer = context.window_manager.event_timer_add(0.5, self.win)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


bpy.utils.register_class(PrintLamp)
scene = bpy.context.scene
scene.render.engine = 'BLENDER_GAME'
ob = scene.objects.get("Lamp") or next(o for o in scene.objects if o.type == 'LAMP')
scene.objects.active = ob
ob.select = True
bpy.ops.wm.print_lamp('EXEC_DEFAULT')
