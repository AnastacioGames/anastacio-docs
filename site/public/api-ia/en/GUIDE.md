# AI guide: programming for the Anastacio Engine

Read this once before writing code. Then use `INDEX.md` and open only the pages you need.
Anastacio is a new engine: no model was trained on it. **Do not invent functions.** If a name is not on the API pages, it does not exist.

## Names and imports

- The main module is **`Range`**, with a **capital R**: `import Range`, `from Range import logic, events`.
- `bge` also works (`Range.logic` and `bge.logic` are the same object), but the examples and the Web validator use `Range`. On Web export, `import bge` raises warning `WEB-PY-001`.
- Modules: `Range.logic` (scene, objects, time, `globalDict`), `Range.types` (classes), `Range.render`, `Range.events` (keys), `Range.constraints` (physics), `Range.application`, `Range.texture`, `Range.imgui`, `Range.network`, `Range.track`.
- Game scripts do **not** use `bpy`: the exported game runs without it.

## Two ways to write logic

**Script on a Python controller** (wired to sensors with logic bricks):

```python
import Range
from Range import logic, events

cont = logic.getCurrentController()
own = cont.owner                      # KX_GameObject that owns the controller
if logic.keyboard.inputs[events.WKEY].active:
    own.applyMovement((0, 0.1, 0), True)   # True = local axes
```

**Component** (a Python class attached to the object, no logic bricks). Prefer it when the logic is all Python:

```python
import Range
from Range import logic, events
from collections import OrderedDict

class Mover(Range.types.KX_PythonComponent):
    args = OrderedDict([("Speed", 0.1)])   # panel fields, in the written order

    def start(self, args):          # once, when the game starts
        self.speed = args["Speed"]

    def update(self):               # every frame, before logic bricks
        if logic.keyboard.inputs[events.WKEY].active:
            self.object.applyMovement((0, self.speed, 0), True)
```

- In a component the owner is `self.object` (in a script it is `cont.owner`).
- Fields with slider, tooltip, object/scene picker: `from Range.args import Float, Int, Bool, Text, Choice, Object, Scene, Color, Header` (Smart Components).

## Common pitfalls

- **Removed object:** calling ANY method or attribute of an object already removed from the scene raises `SystemError`. If it may have been removed, check the `invalid` attribute first.
- **`endObject()`** takes effect at the end of the frame, not immediately.
- **Time:** for FPS-independent movement use `1.0 / max(logic.getAverageFrameRate(), 1.0)`.
- **Keyboard/mouse:** `logic.keyboard.inputs[events.WKEY]` has `.active` (held) and `.activated` (pressed this frame).
- **Game properties** are accessed as `obj["name"]`; `obj.get("name", default)` avoids an error when missing.
- **Data across scenes:** `logic.globalDict` (and `logic.saveGlobalDict()` to save).
- **Scene:** `obj.scene.addObject("Name", reference, lifetime)`, `scene.replace("Level2")`, `scene.restart()`.
- Names are **camelCase** (`worldPosition`, `applyMovement`), not modern-Blender snake_case.

## How to look things up without blowing the context

1. `INDEX.md`: one line per class/module.
2. The class page, for example `paginas/KX_GameObject.md`. Large pages have an overview plus parts `--props`, `--funcs`, `--consts`.
3. `busca.json` (or the MCP tool `api_buscar`) to find a name without knowing the class.
4. Items marked *(new in Anastacio)* did not exist in the original engine: read the description, the model does not know them.
