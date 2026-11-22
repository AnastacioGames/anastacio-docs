# KX_MeshBuilderSlot

> **See also:**
[`KX_MeshBuilder`](KX_MeshBuilder.md), [`KX_Mesh`](KX_Mesh.md)

Class `Range.types.KX_MeshBuilderSlot`.

```python
# Add a square made of two triangles.
points = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
ids = [slot.addVertex(point) for point in points]

slot.addIndex([ids[0], ids[1], ids[2]])
slot.addIndex([ids[0], ids[2], ids[3]])
slot.recalculateNormals()
```

```python
# See what the slot has.
print(len(slot.vertices), len(slot.indices))
print(slot.uvCount, slot.colorCount)
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### addIndex(indices)

 `method`

Adds vertex indices (list of integers) to the primitives and, for triangle meshes, to the triangles.

### addPrimitiveIndex(indices)

 `method`

Adds indices only to the primitive (drawing) list.

### addTriangleIndex(indices)

 `method`

Adds indices only to the triangle list (physics and rays).

### addVertex(position, normal=None, tangent=None, uvs=None, colors=None)

 `method`

Adds a vertex. `uvs` and `colors` are lists, one entry per layer.

**Returns:** `int`

### recalculateNormals()

 `method`

Recomputes vertex normals from the triangles.

### removePrimitiveIndex(start, end=-1)

 `method`

Removes primitive indices from `start` to `end`.

### removeTriangleIndex(start, end=-1)

 `method`

Removes triangle indices from `start` to `end`.

### removeVertex(start, end=-1)

 `method`

Removes vertices from `start` to `end`.

### colorCount

 `attribute · read-only`

How many vertex color layers the slot has.

### indices

 `attribute · read-only`

List of primitive indices.

### material

 `attribute`

Slot material.

### primitive

 `attribute · read-only`

Slot primitive type (points, lines or triangles).

### triangleIndices

 `attribute · read-only`

List of triangle indices.

### uvCount

 `attribute · read-only`

How many UV layers the slot has.

### vertices

 `attribute · read-only`

List of the slot vertices.
