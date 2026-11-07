---
title: "SCA_IActuator"
description: "Range.types.SCA_IActuator class reference"
---

Base class: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Base class for all actuator logic bricks.

```python
# All actuators are turned on and off by the controller.
import Range

cont = Range.logic.getCurrentController()

for act in cont.actuators:
    if cont.sensors[0].positive:
        cont.activate(act)
    else:
        cont.deactivate(act)
```



