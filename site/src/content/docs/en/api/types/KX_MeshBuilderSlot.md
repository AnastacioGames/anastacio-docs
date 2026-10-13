---
title: "KX_MeshBuilderSlot"
description: "Range.types.KX_MeshBuilderSlot class reference"
---

:::tip[See also]
[`KX_MeshBuilder`](../../types/kx_meshbuilder/), [`KX_Mesh`](../../types/kx_mesh/)
:::

Class `Range.types.KX_MeshBuilderSlot`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### addIndex(indices)

 <small>method</small>

Adds vertex indices (list of integers) to the primitives and, for triangle meshes, to the triangles.

### addPrimitiveIndex(indices)

 <small>method</small>

Adds indices only to the primitive (drawing) list.

### addTriangleIndex(indices)

 <small>method</small>

Adds indices only to the triangle list (physics and rays).

### addVertex(position, normal=None, tangent=None, uvs=None, colors=None)

 <small>method</small>

Adds a vertex. `uvs` and `colors` are lists, one entry per layer.

**Returns:** `int`

### recalculateNormals()

 <small>method</small>

Recomputes vertex normals from the triangles.

### removePrimitiveIndex(start, end=-1)

 <small>method</small>

Removes primitive indices from `start` to `end`.

### removeTriangleIndex(start, end=-1)

 <small>method</small>

Removes triangle indices from `start` to `end`.

### removeVertex(start, end=-1)

 <small>method</small>

Removes vertices from `start` to `end`.

### colorCount

 <small>attribute · read-only</small>

How many vertex color layers the slot has.

### indices

 <small>attribute · read-only</small>

List of primitive indices.

### material

 <small>attribute</small>

Slot material.

### primitive

 <small>attribute · read-only</small>

Slot primitive type (points, lines or triangles).

### triangleIndices

 <small>attribute · read-only</small>

List of triangle indices.

### uvCount

 <small>attribute · read-only</small>

How many UV layers the slot has.

### vertices

 <small>attribute · read-only</small>

List of the slot vertices.

