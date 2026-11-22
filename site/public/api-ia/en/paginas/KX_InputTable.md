# KX_InputTable

> **See also:**
[`KX_InputSystem`](KX_InputSystem.md)

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

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### activated

 `attribute · read-only`

`True` on the frame the action was just triggered.

### active

 `attribute · read-only`

`True` while the action is triggered.

### released

 `attribute · read-only`

`True` on the frame the action was just released.

### values

 `attribute · read-only`

Current action values: `True`/`False` on a simple button (`VECTOR1D`); tuple with 2 or 3 numbers on 2D or 3D axes.
