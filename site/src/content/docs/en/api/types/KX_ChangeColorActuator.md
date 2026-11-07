---
title: "KX_ChangeColorActuator"
description: "Range.types.KX_ChangeColorActuator class reference"
---

Class `Range.types.KX_ChangeColorActuator`.

```python
# Fade the color of the object to red.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["ChangeColor"]

act.color = [1.0, 0.0, 0.0, 1.0]
act.useLerp = True
act.lerp = 0.2
cont.activate(act)
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### color

 <small>attribute</small>

Color `[r, g, b, a]` applied by the actuator.

### lerp

 <small>attribute</small>

Color transition speed when `useLerp` is on (0.1 to 1.0).

### useLerp

 <small>attribute</small>

Makes the color change gradually instead of all at once.

