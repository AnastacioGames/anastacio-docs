---
title: "KX_BatchGroup"
description: "Range.types.KX_BatchGroup class reference"
---

Base class: [`EXP_Value`](../exp_value/)



The batch group is class containing a mesh resulting of the merging of meshes used by objects.
The meshes are merged with the transformation of the objects using it.
An instance of this class is not owned by one object but shared between objects.
In consideration an instance of `KX_BatchGroup` have to instanced with as argument a list of at least one object containing the meshes to merge.
This can be done in a way similar to:

```python

import Range

scene = Range.logic.getCurrentScene()

batchGroup = Range.types.KX_BatchGroup([scene.objects["Cube"], scene.objects["Plane"]])
```

:::caution
Rendering settings unique to objects such as `KX_GameObject.layer` and `KX_GameObject.color` are shared when using batch groups.
These settings are taken from object `referenceObject`.
:::

```python

# Merge every object with the rock property to draw them in fewer calls.
import Range

scene = Range.logic.getCurrentScene()
rocks = [obj for obj in scene.objects if "rock" in obj]

group = Range.types.KX_BatchGroup(rocks)
print(len(group.objects))
```

```python

# Take one object out of its group before changing it alone.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.split([obj])
```

```python

# Undo the group and give every object its original mesh back.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.destruct()
```

### objects

The list of the objects merged. (read only)

**Type:** `EXP_ListValue` of `KX_GameObject`

### referenceObject

The object used for object rendering settings (layer, color...).

### merge(objects)

Merge meshes using the transformation of the objects using them.

- **`objects`**: The objects to merge.
  - type: `EXP_ListValue` of `KX_GameObject`

### split(objects)

Split the meshes of the objects using them and restore their original meshes.

- **`objects`**: The objects to unmerge.
  - type: `EXP_ListValue` of `KX_GameObject`

### destruct()

Destruct the batch group and restore all the objects to their original meshes.

