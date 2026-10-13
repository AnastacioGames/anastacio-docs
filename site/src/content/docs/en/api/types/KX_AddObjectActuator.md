---
title: "KX_AddObjectActuator"
description: "Range.types.KX_AddObjectActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Edit Object Actuator (in Add Object Mode)

:::caution
An Add Object actuator will be ignored if at game start, the linked object doesn't exist (or is empty) or the linked object is in an active layer.

```text

Error: GameObject 'Name' has a AddObjectActuator 'ActuatorName' without object (in 'nonactive' layer)
```
:::

### object

the object this actuator adds.

**Type:** `KX_GameObject` or None

### objectLastCreated

the last added object from this actuator (read-only).

**Type:** `KX_GameObject` or None

### time

the lifetime of added objects, in frames. Set to 0 to disable automatic deletion.

**Type:** float

### linearVelocity

the initial linear velocity of added objects.

**Type:** list [vx, vy, vz]

### angularVelocity

the initial angular velocity of added objects.

**Type:** list [vx, vy, vz]

### instantAddObject()

adds the object without needing to calling SCA_PythonController.activate()

:::note
Use objectLastCreated to get the newly created object.
:::

