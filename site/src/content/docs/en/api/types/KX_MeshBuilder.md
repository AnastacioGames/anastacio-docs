---
title: "KX_MeshBuilder"
description: "Range.types.KX_MeshBuilder class reference"
---

:::tip[See also]
[`KX_MeshBuilderSlot`](../../types/kx_meshbuilderslot/), [`KX_Mesh`](../../types/kx_mesh/), [`KX_GameObject`](../../types/kx_gameobject/)
:::

Class `Range.types.KX_MeshBuilder`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### addSlot(material, primitive=0)

 <small>method</small>

Creates a mesh part with the given material. `primitive`: 0 triangles (default), 1 points, 2 lines.

**Returns:** `KX_MeshBuilderSlot`

### finish()

 <small>method</small>

Builds the mesh from the slots and registers it in the scene. Then use `obj.replaceMesh()` to put it on an object.

**Returns:** `KX_Mesh`

### FromMesh(name, mesh)

 <small>method</small>

Creates a builder from an existing mesh, to copy and edit it.

**Returns:** `KX_MeshBuilder`

### slots

 <small>attribute · read-only</small>

List of the mesh slots (`KX_MeshBuilderSlot`).

