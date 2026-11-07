---
title: "BL_ArmatureActuator"
description: "Range.types.BL_ArmatureActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Armature Actuators change constraint condition on armatures.

```python
# Change the target of a bone constraint.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Armature"]

act.type = Range.logic.KX_ACT_ARMATURE_SETTARGET
act.target = Range.logic.getCurrentScene().objects["Ball"]
cont.activate(act)
```

```python
# Fade the influence of the constraint.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Armature"]

act.type = Range.logic.KX_ACT_ARMATURE_SETINFLUENCE
act.influence = 0.5
cont.activate(act)
```

### type

The type of action that the actuator executes when it is active.

Can be one of `these constants`

**Type:** integer

### constraint

The constraint object this actuator is controlling.

**Type:** `BL_ArmatureConstraint`

### target

The object that this actuator will set as primary target to the constraint it controls.

**Type:** `KX_GameObject`

### subtarget

The object that this actuator will set as secondary target to the constraint it controls.

**Type:** `KX_GameObject`.

:::note
Currently, the only secondary target is the pole target for IK constraint.
:::

### weight

The weight this actuator will set on the constraint it controls.

**Type:** float.

:::note
Currently only the IK constraint has a weight. It must be a value between 0 and 1.
:::

:::note
A weight of 0 disables a constraint while still updating constraint runtime values (see `BL_ArmatureConstraint`)
:::

### influence

The influence this actuator will set on the constraint it controls.

**Type:** float.

