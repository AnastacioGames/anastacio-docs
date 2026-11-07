---
title: "KX_VisibilityActuator"
description: "Range.types.KX_VisibilityActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Visibility Actuator.

```python
# Hide the object and its children.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Visibility"]

act.visibility = False
act.useRecursion = True
cont.activate(act)
```

### visibility

whether the actuator makes its parent object visible or invisible.

**Type:** boolean

### useOcclusion

whether the actuator makes its parent object an occluder or not.

**Type:** boolean

### useRecursion

whether the visibility/occlusion should be propagated to all children of the object.

**Type:** boolean

