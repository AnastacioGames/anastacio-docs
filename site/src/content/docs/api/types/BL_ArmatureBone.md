---
title: "BL_ArmatureBone"
description: "Referência da classe Range.types.BL_ArmatureBone"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Proxy to Blender bone structure. All fields are read-only and comply to RNA names. All space attribute correspond to the rest pose.

### name

bone name.

**Tipo:** string

### connected

true when the bone head is struck to the parent's tail.

**Tipo:** boolean

### hinge

true when bone doesn't inherit rotation or scale from parent bone.

**Tipo:** boolean

### inherit_scale

true when bone inherits scaling from parent bone.

**Tipo:** boolean

### bbone_segments

number of B-bone segments.

**Tipo:** integer

### roll

bone rotation around head-tail axis.

**Tipo:** float

### head

location of head end of the bone in parent bone space.

**Tipo:** vector [x, y, z]

### tail

location of head end of the bone in parent bone space.

**Tipo:** vector [x, y, z]

### length

bone length.

**Tipo:** float

### arm_head

location of head end of the bone in armature space.

**Tipo:** vector [x, y, z]

### arm_tail

location of tail end of the bone in armature space.

**Tipo:** vector [x, y, z]

### arm_mat

matrix of the bone head in armature space.

**Tipo:** matrix [4][4]

:::note
This matrix has no scale part.
:::

### bone_mat

rotation matrix of the bone in parent bone space.

**Tipo:** matrix [3][3]

### parent

parent bone, or None for root bone.

**Tipo:** `BL_ArmatureBone`

### children

list of bone's children.

**Tipo:** list of `BL_ArmatureBone`

