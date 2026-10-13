---
title: "KX_BoundingBox"
description: "Range.types.KX_BoundingBox class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A bounding volume box of a game object. Used to get and alterate the volume box or AABB.

```python

from Range import logic
from mathutils import Vector

owner = logic.getCurrentController().owner
box = owner.cullingBox

# Disable auto update to allow modify the box.
box.autoUpdate = False

print(box)
# Increase the height of the box of 1.
box.max = box.max + Vector((0, 0, 1))

print(box)
```

### min

The minimal point in x, y and z axis of the bounding box.

**Type:** `mathutils.Vector`

### max

The maximal point in x, y and z axis of the bounding box.

**Type:** `mathutils.Vector`

### center

The center of the bounding box. (read only)

**Type:** `mathutils.Vector`

### radius

The radius of the bounding box. (read only)

**Type:** float

### autoUpdate

Allow to update the bounding box if the mesh is modified.

**Type:** boolean

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### volume

 <small>attribute · read-only</small>

Bounding box volume (width × height × depth).

