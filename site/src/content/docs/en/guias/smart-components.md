---
title: Smart Components (Range.args and the Editor class)
description: Fields with sliders, tooltips and object pickers, warnings and buttons in the editor, with no change to the game.
---

A regular Python component has `args` and the game code. A **Smart Component** is the same component with two extra features, both optional:

1. **Better fields** with `Range.args`: sliders with limits, tooltips, sections, ordered lists, and picking an object or scene with the mouse.
2. **An `Editor` class** that runs only in the editor: sets up the object when added, shows warnings on fields, adds buttons and draws guides in the viewport.

The game does not change: `args["Speed"]` is still a `float`, and the exported game runs without `bpy`. Old components work the same.

:::tip[Ready-made example]
In the Text Editor, **Templates > Components > 04 Smart Component** opens a full chaser using everything in this guide.
:::

## 1. Fields with Range.args

```python
from collections import OrderedDict
from Range import types
from Range.args import Float, Int, Bool, Text, Choice, Object, Scene, Color, Header

class Chaser(types.KX_PythonComponent):
    args = OrderedDict([
        Header("Target", icon="OBJECT_DATA"),
        ("Target", Object(tip="Object it chases")),
        ("Stop distance", Float(1.5, min=0, max=10, tip="Stops at this distance")),

        Header("Movement", icon="AUTO"),
        ("Speed", Float(3.0, min=0, max=20, tip="Meters per second")),
        ("Mode", Choice("Walk", "Walk", "Run", "Jump")),
        ("Face target", Bool(True, tip="Turns the body towards the target")),
        ("Scene on catch", Scene(tip="Scene added on top when it catches the player")),
        ("Alert color", Color(1.0, 0.1, 0.1, 1.0, tip="Blink color")),
    ])

    def start(self, args):
        self.target = args["Target"]        # KX_GameObject or None
        self.speed = args["Speed"]
```

| Field | In the editor | Arrives in the game as |
|---|---|---|
| `Float(value, min, max, tip)` | number; slider when it has `min` and `max` | `float` |
| `Int(value, min, max, tip)` | integer; slider when it has `min` and `max` | `int` |
| `Bool(value, tip)` | checkbox | `bool` |
| `Text(value, tip)` | text field | `str` |
| `Choice(default, item1, item2, ..., tip)` | list in the written order | `str` |
| `Object(tip)` | pick an object of the scene | `KX_GameObject`, or `None` |
| `Scene(tip)` | pick a scene of the file | `str` with the name (`""` if empty), ready for `logic.addScene` |
| `Color(r, g, b[, a], tip)` | color with picker (3 or 4 values) | `Color` (use 4 values for `obj.color`) |
| `Header(name, icon, open)` | collapsible section title | (not a field) |

Values outside the limits are clamped: typing 50 in a `Float(max=20)` becomes 20. The old format (`("Name", 1.0)`) still works in the same list, just without a tooltip. Renaming the picked object or scene updates the field by itself.

## 2. Asking for things when added: `requires`

```python
class Chaser(types.KX_PythonComponent):
    requires = {"physics": "NO_COLLISION", "components": ["health.Health"]}
```

When the component is added, the editor sets the object's physics type and adds the other listed components.

## 3. The Editor class

It goes inside the component. The game never runs it. It may use `bpy`, but import it only inside the methods. Inside, `self.object` is the object and `self.args["Field"]` reads and writes fields.

```python
class Chaser(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        buttons = [
            ("Drop to ground", "drop_to_ground", "TRIA_DOWN_BAR"),
        ]

        def on_attach(self, obj):
            # once, right after the component is added to the object
            self.args["Name"] = obj.name

        def on_change(self, obj, name, value):
            # runs for each field when something changes and when the file opens;
            # returning a text shows a warning under the field
            if name == "Speed" and value > 15:
                return "Too fast: it may go through walls"
            if name == "Target" and value is None:
                return "No target: it will stand still"

        def drop_to_ground(self, obj, context):
            context.scene.update()
            lowest_z = min((obj.matrix_world * v.co).z for v in obj.data.vertices)
            obj.location.z -= lowest_z

        def draw_gizmo(self, obj, args, g, selected):
            # viewport drawing, not shown in the game
            pos = obj.matrix_world.translation
            g.circle(pos, args["Stop distance"], "GREEN")
            if args["Target"] is not None:
                g.arrow(pos, args["Target"].matrix_world.translation, "YELLOW", width=2)
```

| Item | When it runs |
|---|---|
| `on_attach(self, obj)` | Once, when the component is added. |
| `on_change(self, obj, name, value)` | When a field changes and when the file opens. The returned text becomes a warning. |
| `buttons = [(text, method, icon)]` | Buttons at the end of the component box; the method gets `(obj, context)` and supports undo. |
| `draw_gizmo(self, obj, args, g, selected)` | On every viewport redraw. `g` has `line`, `path`, `circle`, `sphere`, `box`, `arrow` and `text`; colors by name (`"RED"`) or `(r, g, b)`, positions in world space. |

By default gizmos only show for the selected object. The **Overlay > Component Gizmos** option changes that.

Errors in the `Editor` code show in red in the component box and do not affect the game.

## 4. Your own UI: `draw_ui`

To draw the component box your own way, add `draw_ui(self, layout, obj, comp)` to the `Editor` class. `layout` is the regular Blender layout (`row()`, `column()`, `prop()`, `operator()`, `label()`). It is drawn after the fields and before the buttons.

```python
class VideoPlayer(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        fields = False          # hides the default field list

        def draw_ui(self, layout, obj, comp):
            # layout is the Blender layout
            layout.prop(obj, "name")
            layout.label("File: %s" % comp.args["File"])
```

With `fields = False`, only your `draw_ui` is shown. The engine's **Video Player** and **Rigid Body Joint** are built this way. If `draw_ui` raises an error, a red warning appears and the rest of the box keeps working.
