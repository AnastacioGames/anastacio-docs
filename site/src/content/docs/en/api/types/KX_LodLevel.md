---
title: "KX_LodLevel"
description: "Range.types.KX_LodLevel class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A single lod level for a game object lod manager.

### mesh

The mesh used for this lod level. (read only)

**Type:** `RAS_MeshObject`

### level

The number of the lod level. (read only)

**Type:** integer

### distance

Distance to begin using this level of detail. (read only)

**Type:** float (0.0 to infinite)

### hysteresis

Minimum distance factor change required to transition to the previous level of detail in percent. (read only)

**Type:** float [0.0 to 100.0]

### useMesh

Return True if the lod level uses a different mesh than the original object mesh. (read only)

**Type:** boolean

### useMaterial

Return True if the lod level uses a different material than the original object mesh material. (read only)

**Type:** boolean

### useHysteresis

Return true if the lod level uses hysteresis override. (read only)

**Type:** boolean

