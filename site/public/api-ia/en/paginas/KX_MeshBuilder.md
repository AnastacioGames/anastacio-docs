# KX_MeshBuilder

> **See also:**
[`KX_MeshBuilderSlot`](KX_MeshBuilderSlot.md), [`KX_Mesh`](KX_Mesh.md), [`KX_GameObject`](KX_GameObject.md)

Class `Range.types.KX_MeshBuilder`.

```python
# Create a triangle by script and put it on the object.
import Range

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder("Triangle", scene, ["UVMap"], ["Col"])
slot = builder.addSlot(own.meshes[0].materials[0])

a = slot.addVertex((0.0, 0.0, 0.0))
b = slot.addVertex((1.0, 0.0, 0.0))
c = slot.addVertex((0.0, 1.0, 0.0))
slot.addIndex([a, b, c])
slot.recalculateNormals()

own.replaceMesh(builder.finish())
```

```python
# Copy an existing mesh to change it. Keep the builder in a variable while you use its slots.
import Range

own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder.FromMesh("Copy", own.meshes[0])
print(len(builder.slots))
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### addSlot(material, primitive=0)

 `method`

Creates a mesh part with the given material. `primitive`: 0 triangles (default), 1 points, 2 lines.

**Returns:** `KX_MeshBuilderSlot`

### finish()

 `method`

Builds the mesh from the slots and registers it in the scene. Then use `obj.replaceMesh()` to put it on an object.

**Returns:** `KX_Mesh`

### FromMesh(name, mesh)

 `method`

Creates a builder from an existing mesh, to copy and edit it.

**Returns:** `KX_MeshBuilder`

### slots

 `attribute · read-only`

List of the mesh slots (`KX_MeshBuilderSlot`).
