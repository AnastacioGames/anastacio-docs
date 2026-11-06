---
title: "KX_LodManager"
description: "Range.types.KX_LodManager class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



This class contains a list of all levels of detail used by a game object.

```python

# Graphics option: values above 1.0 switch to the simpler levels sooner.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.distanceFactor = 2.0
```

```python

# Use the same levels of detail in another object.
import Range

scene = Range.logic.getCurrentScene()
scene.objects["TreeB"].lodManager = scene.objects["TreeA"].lodManager
```

```python

# Also switch the physics mesh when the level changes.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.updatePhysics = True
```

### levels

Return the list of all levels of detail of the lod manager.

**Type:** list of `KX_LodLevel`

### distanceFactor

Method to multiply the distance to the camera.

**Type:** float

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### updatePhysics

 <small>attribute</small>

Also changes the physics mesh when the level of detail (LOD) changes.

