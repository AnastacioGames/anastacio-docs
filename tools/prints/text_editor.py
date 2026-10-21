"""Abre um script de exemplo no Text Editor e tira prints da janela e da barra lateral.
Uso: AnastacioEngine.exe -p 0 0 1600 900 --python text_editor.py -- <pasta_saida>"""
import bpy, sys, os, json

OUT = os.path.abspath(sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else ".")
os.makedirs(OUT, exist_ok=True)
bpy.context.user_preferences.view.show_splash = False

SCRIPT = '''import bge

def main(cont):
    own = cont.owner
    sensor = cont.sensors["Andar"]
    actuator = cont.actuators["Mover"]
    if sensor.positive:
        own.worldPosition.y += 0.1
        cont.activate(actuator)
'''


def montar_texto():
    txt = bpy.data.texts.new("player_move.py")
    txt.write(SCRIPT)
    return txt


class PrintText(bpy.types.Operator):
    bl_idname = "wm.print_text"
    bl_label = "Print Text"
    passo = 0

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
        self.passo += 1
        p = self.passo
        win = self.win
        scr = win.screen
        area = max(scr.areas, key=lambda a: a.width * a.height)
        st = area.spaces.active
        ov = {'window': win, 'screen': scr, 'area': area}
        if p == 2:
            st.text = self.txt
            bpy.ops.text.jump(ov, line=1)
        elif 3 <= p <= 9:
            for r in area.regions:
                r.tag_redraw()
        elif p == 10:
            bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, "janela.png"), full=True)
            info = {"area": [area.x, area.y, area.width, area.height],
                    "regions": {r.type: [r.x, r.y, r.width, r.height] for r in area.regions},
                    "win": [win.width, win.height]}
            json.dump(info, open(os.path.join(OUT, "text_editor.json"), "w"), indent=1)
        elif p == 11:
            ui = [r for r in area.regions if r.type == 'UI']
            if not ui or ui[0].width < 2:
                bpy.ops.text.properties(ov)
        elif p == 13:
            bpy.ops.screen.screenshot(ov, filepath=os.path.join(OUT, "editor-view-find.png"), full=True)
        elif p == 15:
            bpy.ops.wm.quit_blender()
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.win = context.window_manager.windows[0]
        area = max(self.win.screen.areas, key=lambda a: a.width * a.height)
        area.type = 'TEXT_EDITOR'
        wm = context.window_manager
        self._t = wm.event_timer_add(0.7, self.win)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}


bpy.utils.register_class(PrintText)
txt = montar_texto()
w = bpy.context.window_manager.windows[0]
op = bpy.ops.wm.print_text
PrintText.txt = txt
op({'window': w, 'screen': w.screen})
