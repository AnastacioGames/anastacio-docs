---
title: "KX_PythonComponent"
description: "Referência da classe Range.types.KX_PythonComponent"
---

Classe base: [`EXP_Value`](../exp_value/)



Python component can be compared to python logic bricks with parameters. The python component is a script loaded in the UI, this script defined a component class by inheriting from `KX_PythonComponent`. This class must contain a dictionary of properties: `args` and two default functions: `start` and `update`.

The script must have .py extension.

The component properties are loaded from the `args` attribute from the UI at loading time. When the game start the function `start` is called with as arguments a dictionary of the properties' name and value. The `update` function is called every frames during the logic stage before running logics bricks, the goal of this function is to handle and process everything.

The following component example moves and rotates the object when pressing the keys W, A, S and D.

```python

import Range
from collections import OrderedDict

class ThirdPerson(Range.types.KX_PythonComponent):
    """Basic third person controls

    W: move forward
    A: turn left
    S: move backward
    D: turn right

    """

    #

    args = OrderedDict([
        ("Move Speed", 0.1),
        ("Turn Speed", 0.04)
    ])

    def start(self, args):
        self.move_speed = args['Move Speed']
        self.turn_speed = args['Turn Speed']

    def update(self):
        keyboard = Range.logic.keyboard.events

        move = 0
        rotate = 0

        if keyboard[Range.events.WKEY]:
            move += self.move_speed
        if keyboard[Range.events.SKEY]:
            move -= self.move_speed

        if keyboard[Range.events.AKEY]:
            rotate += self.turn_speed
        if keyboard[Range.events.DKEY]:
            rotate -= self.turn_speed

        self.object.applyMovement((0, move, 0), True)
        self.object.applyRotation((0, 0, rotate), True)
```

Since the components are loaded for the first time outside the bge, then `bge` is a fake module that contains only the class `KX_PythonComponent` to avoid importing all the bge modules. This behavior is safer but creates some issues at loading when the user want to use functions or attributes from the bge modules other than the `KX_PythonComponent` class. The way is to not call these functions at loading outside the Range. To detect it, the bge module contains the attribute `__component__` when it's imported outside the Range.

The following component example add a "Cube" object at initialization and move it along x for each update. It shows that the user can use functions from scene and load the component outside the bge by setting global attributes in a condition at the beginning of the script.

```python

import Range

if not hasattr(bge, "__component__"):
    global scene
    scene = Range.logic.getCurrentScene()

class Component(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        scene.addObject("Cube")

    def update(self):
        scene.objects["Cube"].worldPosition.x += 0.1
```

The property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D. The following example show all of these property types.

```python

from Range import *
from mathutils import *
from collections import OrderedDict

class Component(types.KX_PythonComponent):
     args = OrderedDict([
         ("Float", 58.6),
         ("Integer", 150),
         ("Boolean", True),
         ("String", "Cube"),
         ("Enum", {"Enum 1", "Enum 2", "Enum 3"}),
         ("Vector 2D", Vector((0.8, 0.7))),
         ("Vector 3D", Vector((0.4, 0.3, 0.1))),
         ("Vector 4D", Vector((0.5, 0.2, 0.9, 0.6)))
     ])

     def start(self, args):
         print(args)

     def update(self):
         pass
```

### object

The object owner of the component.

**Tipo:** `KX_GameObject`

### args

Dictionary of the component properties, the keys are string and the value can be: float, integer, Vector(2D/3D/4D), set, string.

**Tipo:** dict

### start(args)

Initialize the component.

- **`args`**: The dictionary of the properties' name and value.
  - tipo: dict

:::caution
This function must be inherited in the python component class.
:::

### update()

Process the logic of the component.

:::caution
This function must be inherited in the python component class.
:::

### dispose()

Function called when the component is destroyed.

:::caution
This function must be inherited in the python component class.
:::

