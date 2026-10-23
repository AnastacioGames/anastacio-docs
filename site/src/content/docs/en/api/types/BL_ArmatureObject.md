---
title: "BL_ArmatureObject"
description: "Range.types.BL_ArmatureObject class reference"
---

Base class: [`KX_GameObject`](../kx_gameobject/)

:::tip[See also]
[`BL_ArmatureChannel`](../../types/bl_armaturechannel/), [`BL_ArmatureBone`](../../types/bl_armaturebone/), [`BL_ArmatureConstraint`](../../types/bl_armatureconstraint/), [`BL_ActionActuator`](../../types/bl_actionactuator/)
:::



An armature object.

### constraints

The list of armature constraint defined on this armature.
Elements of the list can be accessed by index or string.
The key format for string access is '<bone_name>:<constraint_name>'.

**Type:** list of `BL_ArmatureConstraint`

### channels

The list of armature channels.
Elements of the list can be accessed by index or name the bone.

**Type:** list of `BL_ArmatureChannel`

### update()

Ensures that the armature will be updated on next graphic frame.

This action is unecessary if a KX_ArmatureActuator with mode run is active
or if an action is playing. Use this function in other cases. It must be called
on each frame to ensure that the armature is updated continously.

### draw()

Draw lines that represent armature to view it in real time.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### clearBoneRotationOffset(bone=None)

 <small>method</small>

Removes the extra rotation of one bone, or of all bones when `bone` is omitted.

### setBoneRotationOffset(bone, rotation)

 <small>method</small>

Extra rotation for a bone on top of the playing actions, in the bone's local space. `rotation`: euler XYZ (3 floats, radians) or quaternion (4 floats, w x y z). Stays until `clearBoneRotationOffset()`.

