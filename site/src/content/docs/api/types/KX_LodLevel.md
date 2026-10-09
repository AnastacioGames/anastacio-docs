---
title: "KX_LodLevel"
description: "Referência da classe Range.types.KX_LodLevel"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A single lod level for a game object lod manager.

### mesh

The mesh used for this lod level. (read only)

**Tipo:** `RAS_MeshObject`

### level

The number of the lod level. (read only)

**Tipo:** integer

### distance

Distance to begin using this level of detail. (read only)

**Tipo:** float (0.0 to infinite)

### hysteresis

Minimum distance factor change required to transition to the previous level of detail in percent. (read only)

**Tipo:** float [0.0 to 100.0]

### useMesh

Return True if the lod level uses a different mesh than the original object mesh. (read only)

**Tipo:** boolean

### useMaterial

Return True if the lod level uses a different material than the original object mesh material. (read only)

**Tipo:** boolean

### useHysteresis

Return true if the lod level uses hysteresis override. (read only)

**Tipo:** boolean

