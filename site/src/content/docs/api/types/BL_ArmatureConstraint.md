---
title: "BL_ArmatureConstraint"
description: "Referência da classe Range.types.BL_ArmatureConstraint"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Proxy to Armature Constraint. Allows to change constraint on the fly.
Obtained through `BL_ArmatureObject`.constraints.

:::note
Not all armature constraints are supported in the GE.
:::

### type

Type of constraint, (read-only).

Use one of `these constants`.

**Tipo:** integer, one of CONSTRAINT_TYPE_* constants

### name

Name of constraint constructed as <bone_name>:<constraint_name>. constraints list.

**Tipo:** string

This name is also the key subscript on `BL_ArmatureObject`.

### enforce

fraction of constraint effect that is enforced. Between 0 and 1.

**Tipo:** float

### headtail

Position of target between head and tail of the target bone: 0=head, 1=tail.

**Tipo:** float.

:::note
Only used if the target is a bone (i.e target object is an armature.
:::

### lin_error

runtime linear error (in Blender units) on constraint at the current frame.

This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.

**Tipo:** float

### rot_error

Runtime rotation error (in radiant) on constraint at the current frame.

**Tipo:** float.

This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.

It is only set if the constraint has a rotation part, for example, a CopyPose+Rotation IK constraint.

### target

Primary target object for the constraint. The position of this object in the GE will be used as target for the constraint.

**Tipo:** `KX_GameObject`.

### subtarget

Secondary target object for the constraint. The position of this object in the GE will be used as secondary target for the constraint.

**Tipo:** `KX_GameObject`.

Currently this is only used for pole target on IK constraint.

### active

True if the constraint is active.

**Tipo:** boolean

:::note
An inactive constraint does not update lin_error and rot_error.
:::

### ik_weight

Weight of the IK constraint between 0 and 1.

Only defined for IK constraint.

**Tipo:** float

### ik_type

Type of IK constraint, (read-only).

Use one of `these constants`.

**Tipo:** integer.

### ik_flag

Combination of IK constraint option flags, read-only.

Use one of `these constants`.

**Tipo:** integer

### ik_dist

Distance the constraint is trying to maintain with target, only used when ik_type=CONSTRAINT_IK_DISTANCE.

**Tipo:** float

### ik_mode

Use one of `these constants`.

Additional mode for IK constraint. Currently only used for Distance constraint:

**Tipo:** integer

