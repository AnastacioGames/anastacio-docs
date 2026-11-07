---
title: "SCA_PropertyActuator"
description: "Range.types.SCA_PropertyActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Property Actuator

```python
# Change the property that this actuator writes.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Property"]

cont.owner["score"] = 0
act.propName = "score"
act.value = "score + 10"
cont.activate(act)
```

### propName

the property on which to operate.

**Type:** string

### value

the value with which the actuator operates.

**Type:** string

### mode

TODO - add constants to game logic dict!.

**Type:** integer

