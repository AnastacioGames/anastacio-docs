---
title: "KX_LodLevel"
description: "Range.types.KX_LodLevel class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A single lod level for a game object lod manager.

```python

# List the levels of detail of the object.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    for lod in obj.lodManager.levels:
        print(lod.level, lod.distance, lod.useMesh, lod.useMaterial)
```

```python

# See which level the object is using right now.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    lod = obj.lodManager.levels[obj.currentLodLevel]
    print(lod.level, lod.mesh)
```

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

