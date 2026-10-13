---
title: "BL_ArmatureChannel"
description: "Range.types.BL_ArmatureChannel class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`BL_ArmatureObject`](../../types/bl_armatureobject/), [`BL_ArmatureBone`](../../types/bl_armaturebone/)
:::



Proxy to armature pose channel. Allows to read and set armature pose.
The attributes are identical to RNA attributes, but mostly in read-only mode.

### name

channel name (=bone name), read-only.

**Type:** string

### bone

return the bone object corresponding to this pose channel, read-only.

**Type:** `BL_ArmatureBone`

### parent

return the parent channel object, None if root channel, read-only.

**Type:** `BL_ArmatureChannel`

### has_ik

true if the bone is part of an active IK chain, read-only.
This flag is not set when an IK constraint is defined but not enabled (miss target information for example).

**Type:** boolean

### ik_dof_x

true if the bone is free to rotation in the X axis, read-only.

**Type:** boolean

### ik_dof_y

true if the bone is free to rotation in the Y axis, read-only.

**Type:** boolean

### ik_dof_z

true if the bone is free to rotation in the Z axis, read-only.

**Type:** boolean

### ik_limit_x

true if a limit is imposed on X rotation, read-only.

**Type:** boolean

### ik_limit_y

true if a limit is imposed on Y rotation, read-only.

**Type:** boolean

### ik_limit_z

true if a limit is imposed on Z rotation, read-only.

**Type:** boolean

### ik_rot_control

true if channel rotation should applied as IK constraint, read-only.

**Type:** boolean

### ik_lin_control

true if channel size should applied as IK constraint, read-only.

**Type:** boolean

### location

displacement of the bone head in armature local space, read-write.

**Type:** vector [X, Y, Z].

:::note
You can only move a bone if it is unconnected to its parent. An action playing on the armature may change the value. An IK chain does not update this value, see joint_rotation.
:::

:::note
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`).
:::

### scale

scale of the bone relative to its parent, read-write.

**Type:** vector [sizeX, sizeY, sizeZ].

:::note
An action playing on the armature may change the value.  An IK chain does not update this value, see joint_rotation.
:::

:::note
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`)
:::

### rotation_quaternion

rotation of the bone relative to its parent expressed as a quaternion, read-write.

**Type:** vector [qr, qi, qj, qk].

:::note
This field is only used if rotation_mode is 0. An action playing on the armature may change the value.  An IK chain does not update this value, see joint_rotation.
:::

:::note
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`)
:::

### rotation_euler

rotation of the bone relative to its parent expressed as a set of euler angles, read-write.

**Type:** vector [X, Y, Z].

:::note
This field is only used if rotation_mode is > 0. You must always pass the angles in [X, Y, Z] order; the order of applying the angles to the bone depends on rotation_mode. An action playing on the armature may change this field.  An IK chain does not update this value, see joint_rotation.
:::

:::note
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`)
:::

### rotation_mode

Method of updating the bone rotation, read-write.

**Type:** integer (one of `these constants`)

### channel_matrix

pose matrix in bone space (deformation of the bone due to action, constraint, etc), Read-only.
This field is updated after the graphic render, it represents the current pose.

**Type:** matrix [4][4]

### pose_matrix

pose matrix in armature space, read-only,
This field is updated after the graphic render, it represents the current pose.

**Type:** matrix [4][4]

### pose_head

position of bone head in armature space, read-only.

**Type:** vector [x, y, z]

### pose_tail

position of bone tail in armature space, read-only.

**Type:** vector [x, y, z]

### ik_min_x

minimum value of X rotation in degree (<= 0) when X rotation is limited (see ik_limit_x), read-only.

**Type:** float

### ik_max_x

maximum value of X rotation in degree (>= 0) when X rotation is limited (see ik_limit_x), read-only.

**Type:** float

### ik_min_y

minimum value of Y rotation in degree (<= 0) when Y rotation is limited (see ik_limit_y), read-only.

**Type:** float

### ik_max_y

maximum value of Y rotation in degree (>= 0) when Y rotation is limited (see ik_limit_y), read-only.

**Type:** float

### ik_min_z

minimum value of Z rotation in degree (<= 0) when Z rotation is limited (see ik_limit_z), read-only.

**Type:** float

### ik_max_z

maximum value of Z rotation in degree (>= 0) when Z rotation is limited (see ik_limit_z), read-only.

**Type:** float

### ik_stiffness_x

bone rotation stiffness in X axis, read-only.

**Type:** float between 0 and 1

### ik_stiffness_y

bone rotation stiffness in Y axis, read-only.

**Type:** float between 0 and 1

### ik_stiffness_z

bone rotation stiffness in Z axis, read-only.

**Type:** float between 0 and 1

### ik_stretch

ratio of scale change that is allowed, 0=bone can't change size, read-only.

**Type:** float

### ik_rot_weight

weight of rotation constraint when ik_rot_control is set, read-write.

**Type:** float between 0 and 1

### ik_lin_weight

weight of size constraint when ik_lin_control is set, read-write.

**Type:** float between 0 and 1

### joint_rotation

Control bone rotation in term of joint angle (for robotic applications), read-write.

When writing to this attribute, you pass a [x, y, z] vector and an appropriate set of euler angles or quaternion is calculated according to the rotation_mode.

When you read this attribute, the current pose matrix is converted into a [x, y, z] vector representing the joint angles.

The value and the meaning of the x, y, z depends on the ik_dof_x/ik_dof_y/ik_dof_z attributes:

* 1DoF joint X, Y or Z: the corresponding x, y, or z value is used an a joint angle in radiant
* 2DoF joint X+Y or Z+Y: treated as 2 successive 1DoF joints: first X or Z, then Y. The x or z value is used as a joint angle in radiant along the X or Z axis, followed by a rotation along the new Y axis of y radiants.
* 2DoF joint X+Z: treated as a 2DoF joint with rotation axis on the X/Z plane. The x and z values are used as the coordinates of the rotation vector in the X/Z plane.
* 3DoF joint X+Y+Z: treated as a revolute joint. The [x, y, z] vector represents the equivalent rotation vector to bring the joint from the rest pose to the new pose.

**Type:** vector [x, y, z]

:::note
The bone must be part of an IK chain if you want to set the ik_dof_x/ik_dof_y/ik_dof_z attributes via the UI, but this will interfere with this attribute since the IK solver will overwrite the pose. You can stay in control of the armature if you create an IK constraint but do not finalize it (e.g. don't set a target) the IK solver will not run but the IK panel will show up on the UI for each bone in the chain.
:::

:::note
[0, 0, 0] always corresponds to the rest pose.
:::

:::note
You must request the armature pose to update and wait for the next graphic frame to see the effect of setting this attribute (see `BL_ArmatureObject.update`).
:::

:::note
You can read the result of the calculation in rotation or euler_rotation attributes after setting this attribute.
:::

