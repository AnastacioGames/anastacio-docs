---
title: "KX_DynamicActuator"
description: "Range.types.KX_DynamicActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Dynamic Actuator.

```python
# Change the mass of the object.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_SET_MASS
act.mass = 5.0
cont.activate(act)
```

```python
# Turn the physics of the object off.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_DISABLE_DYNAMICS
cont.activate(act)
```

### mode

**Type:** integer

the type of operation of the actuator, 0-4

* KX_DYN_RESTORE_DYNAMICS(0)
* KX_DYN_DISABLE_DYNAMICS(1)
* KX_DYN_ENABLE_RIGID_BODY(2)
* KX_DYN_DISABLE_RIGID_BODY(3)
* KX_DYN_SET_MASS(4)

### mass

the mass value for the KX_DYN_SET_MASS operation.

**Type:** float

