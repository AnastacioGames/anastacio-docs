---
title: "KX_ArmatureSensor"
description: "Referência da classe Range.types.KX_ArmatureSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Armature sensor detect conditions on armatures.

### type

The type of measurement that the sensor make when it is active.

Can be one of `these constants`

**Tipo:** integer.

### constraint

The constraint object this sensor is watching.

**Tipo:** `BL_ArmatureConstraint`

### value

The threshold used in the comparison with the constraint error
The linear error is only updated on CopyPose/Distance IK constraint with iTaSC solver
The rotation error is only updated on CopyPose+rotation IK constraint with iTaSC solver
The linear error on CopyPose is always >= 0: it is the norm of the distance between the target and the bone
The rotation error on CopyPose is always >= 0: it is the norm of the equivalent rotation vector between the bone and the target orientations
The linear error on Distance can be positive if the distance between the bone and the target is greater than the desired distance, and negative if the distance is smaller.

**Tipo:** float

