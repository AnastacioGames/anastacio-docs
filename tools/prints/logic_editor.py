"""Monta o Logic Editor com bricks de exemplo e salva prints.
Uso: AnastacioEngine.exe --factory-startup --python logic_editor.py -- <pasta_saida>"""
import bpy, sys, os, json

OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "."
os.makedirs(OUT, exist_ok=True)


def montar_cena():
    ob = bpy.context.scene.objects.get("Cube") or bpy.context.active_object
    ob.name = "Player"
    bpy.context.scene.objects.active = ob
    ob.select = True
    for kind, t, name in [("sensor", "KEYBOARD", "Pular"), ("sensor", "KEYBOARD", "Andar"),
                          ("sensor", "NEAR", "Inimigo perto"), ("controller", "LOGIC_AND", "E"),
                          ("controller", "PYTHON", "Script"), ("actuator", "MOTION", "Mover"),
                          ("actuator", "MESSAGE", "Avisar")]:
        getattr(bpy.ops.logic, kind + "_add")(type=t, name=name, object=ob.name)
    g = ob.game
    g.sensors["Andar"].key = 'W'
    g.sensors["Andar"].link(g.controllers["E"])
    g.actuators["Mover"].link(g.controllers["E"])
    g.actuators["Mover"].offset_location[1] = 0.1
    g.sensors["Inimigo perto"].distance = 0.0
    try:
        g.brick_groups.add().name = "Movimento"
    except Exception as e:
        print("grupos:", e)
    bpy.ops.object.game_property_new(type='INT', name="vida")
    bpy.ops.object.game_property_new(type='FLOAT', name="velocidade")


def preparar_tela():
    win = bpy.context.window_manager.windows[0]
    scr = win.screen
    area = max(scr.areas, key=lambda a: a.width * a.height)
    area.type = 'LOGIC_EDITOR'
    return win, scr, area


class PrintLogic(bpy.types.Operator):
    bl_idname = "wm.print_logic"
    bl_label = "Print Logic"
    passo = 0

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
        self.passo += 1
        win = self.win
        scr = win.screen
        area = max(scr.areas, key=lambda a: a.width * a.height)
        self.scr, self.area = scr, area
        regs = [r for r in area.regions if r.type == 'WINDOW']
        ov = {'window': win, 'screen': scr, 'area': area}
        if regs:
            ov['region'] = regs[0]
        if self.passo == 1:
            bpy.ops.screen.screen_full_area(ov)
        elif self.passo == 2:
            ui = [r for r in area.regions if r.type == 'UI']
            if not ui or ui[0].width < 2:
                bpy.ops.logic.properties(ov)
        elif self.passo == 4:
            a = self.area
            bpy.ops.screen.screenshot(ov,
                                      filepath=os.path.join(OUT, "logic_editor_full.png"), full=True)
            info = {"area": [a.x, a.y, a.width, a.height],
                    "regions": {r.type: [r.x, r.y, r.width, r.height] for r in a.regions},
                    "win": [win.width, win.height]}
            json.dump(info, open(os.path.join(OUT, "logic_editor.json"), "w"), indent=1)
        elif self.passo == 5:
            ui = [r for r in area.regions if r.type == 'UI'][0]
            for _ in range(40):
                bpy.ops.view2d.scroll_down(dict(ov, region=ui))
        elif self.passo == 7:
            bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, "logic_editor_full_inspector.png"), full=True)
        elif self.passo == 8:
            bpy.ops.wm.quit_blender()
        if self.passo > 10:
            bpy.ops.wm.quit_blender()
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.win, self.scr, self.area = preparar_tela()
        wm = context.window_manager
        self._t = wm.event_timer_add(0.7, self.win)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}


bpy.utils.register_class(PrintLogic)
montar_cena()
w = bpy.context.window_manager.windows[0]
bpy.ops.wm.print_logic({'window': w, 'screen': w.screen})
