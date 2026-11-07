---
title: "KX_LightningActuator"
description: "Range.types.KX_LightningActuator class reference"
---

Class `Range.types.KX_LightningActuator`.

```python
# Fire a flash with a visible bolt.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Lightning"]

act.bolt = True
cont.activate(act)
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### bolt

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on the visible lightning bolt, besides the flash.

