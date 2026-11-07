---
title: "KX_InputTable"
description: "Range.types.KX_InputTable class reference"
---

:::tip[See also]
[`KX_InputSystem`](../../types/kx_inputsystem/)
:::

Class `Range.types.KX_InputTable`.

```python
# Use an action without knowing which key is connected to it.
import Range

maps = Range.logic.inputSystem.inputMaps
jump = maps["Player"]["Jump"]

if jump.activated:
    print("Jump")
```

```python
# Read an axis.
import Range

move = Range.logic.inputSystem.inputMaps["Player"]["Move"]

if move.active:
    print(move.values)
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### activated

 <small>attribute · read-only</small>

`True` on the frame the action was just triggered.

### active

 <small>attribute · read-only</small>

`True` while the action is triggered.

### released

 <small>attribute · read-only</small>

`True` on the frame the action was just released.

### values

 <small>attribute · read-only</small>

Current action values: tuple with 1, 2 or 3 numbers, depending on the type (button, 2D or 3D axis).

