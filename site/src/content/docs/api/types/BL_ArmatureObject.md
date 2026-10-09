---
title: "BL_ArmatureObject"
description: "Referência da classe Range.types.BL_ArmatureObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



An armature object.

### constraints

The list of armature constraint defined on this armature.
Elements of the list can be accessed by index or string.
The key format for string access is '<bone_name>:<constraint_name>'.

**Tipo:** list of `BL_ArmatureConstraint`

### channels

The list of armature channels.
Elements of the list can be accessed by index or name the bone.

**Tipo:** list of `BL_ArmatureChannel`

### update()

Ensures that the armature will be updated on next graphic frame.

This action is unecessary if a KX_ArmatureActuator with mode run is active
or if an action is playing. Use this function in other cases. It must be called
on each frame to ensure that the armature is updated continously.

### draw()

Draw lines that represent armature to view it in real time.

