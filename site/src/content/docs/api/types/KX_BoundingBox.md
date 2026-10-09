---
title: "KX_BoundingBox"
description: "Referência da classe Range.types.KX_BoundingBox"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



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

**Tipo:** `mathutils.Vector`

### max

The maximal point in x, y and z axis of the bounding box.

**Tipo:** `mathutils.Vector`

### center

The center of the bounding box. (read only)

**Tipo:** `mathutils.Vector`

### radius

The radius of the bounding box. (read only)

**Tipo:** float

### autoUpdate

Allow to update the bounding box if the mesh is modified.

**Tipo:** boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### volume

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

