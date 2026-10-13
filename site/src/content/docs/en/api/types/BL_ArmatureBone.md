---
title: "BL_ArmatureBone"
description: "Range.types.BL_ArmatureBone class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Proxy to Blender bone structure. All fields are read-only and comply to RNA names.
All space attribute correspond to the rest pose.

### name

bone name.

**Type:** string

### connected

true when the bone head is struck to the parent's tail.

**Type:** boolean

### hinge

true when bone doesn't inherit rotation or scale from parent bone.

**Type:** boolean

### inherit_scale

true when bone inherits scaling from parent bone.

**Type:** boolean

### bbone_segments

number of B-bone segments.

**Type:** integer

### roll

bone rotation around head-tail axis.

**Type:** float

### head

location of head end of the bone in parent bone space.

**Type:** vector [x, y, z]

### tail

location of head end of the bone in parent bone space.

**Type:** vector [x, y, z]

### length

bone length.

**Type:** float

### arm_head

location of head end of the bone in armature space.

**Type:** vector [x, y, z]

### arm_tail

location of tail end of the bone in armature space.

**Type:** vector [x, y, z]

### arm_mat

matrix of the bone head in armature space.

**Type:** matrix [4][4]

:::note
This matrix has no scale part.
:::

### bone_mat

rotation matrix of the bone in parent bone space.

**Type:** matrix [3][3]

### parent

parent bone, or None for root bone.

**Type:** `BL_ArmatureBone`

### children

list of bone's children.

**Type:** list of `BL_ArmatureBone`

