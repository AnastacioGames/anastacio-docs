---
title: "KX_Mesh"
description: "Range.types.KX_Mesh class reference"
---

Base class: [`EXP_Value`](../exp_value/)

:::tip[See also]
[`KX_MeshBuilder`](../../types/kx_meshbuilder/), [`KX_PolyProxy`](../../types/kx_polyproxy/), [`KX_VertexProxy`](../../types/kx_vertexproxy/), [`KX_BlenderMaterial`](../../types/kx_blendermaterial/)
:::



A mesh object.

You can only change the vertex properties of a mesh object, not the mesh topology.

To use mesh objects effectively, you should know a bit about how the game engine handles them.

#. Mesh Objects are converted from Blender at scene load.
#. The Converter groups polygons by Material.  This means they can be sent to the renderer efficiently.  A material holds:

#. The texture.
#. The Blender material.
#. The Tile properties
#. The face properties - (From the "Texture Face" panel)
#. Transparency & z sorting
#. Light layer
#. Polygon shape (triangle/quad)
#. Game Object

#. Vertices will be split by face if necessary.  Vertices can only be shared between faces if:

#. They are at the same position
#. UV coordinates are the same
#. Their normals are the same (both polygons are "Set Smooth")
#. They are the same color, for example: a cube has 24 vertices: 6 faces with 4 vertices per face.

The correct method of iterating over every `KX_VertexProxy` in a game object

```python

from Range import logic

cont = logic.getCurrentController()
object = cont.owner

for mesh in object.meshes:
   for m_index in range(len(mesh.materials)):
      for v_index in range(mesh.getVertexArrayLength(m_index)):
         vertex = mesh.getVertex(m_index, v_index)
         # Do something with vertex here...
         # ... eg: color the vertex red.
         vertex.color = [1.0, 0.0, 0.0, 1.0]
```

### materials

**Type:** list of `KX_BlenderMaterial` type

### numPolygons

**Type:** integer

### numMaterials

**Type:** integer

### polygons

Returns the list of polygons of this mesh.

**Type:** `KX_PolyProxy` list (read only)

### getMaterialName(matid)

Gets the name of the specified material.

- **`matid`**: the specified material.
  - type: integer

**Returns:** the attached material name.

**Return type:** string

### getTextureName(matid)

Gets the name of the specified material's texture.

- **`matid`**: the specified material
  - type: integer

**Returns:** the attached material's texture name.

**Return type:** string

### getVertexArrayLength(matid)

Gets the length of the vertex array associated with the specified material.

There is one vertex array for each material.

- **`matid`**: the specified material
  - type: integer

**Returns:** the number of verticies in the vertex array.

**Return type:** integer

### getVertex(matid, index)

Gets the specified vertex from the mesh object.

- **`matid`**: the specified material
  - type: integer
- **`index`**: the index into the vertex array.
  - type: integer

**Returns:** a vertex object.

**Return type:** `KX_VertexProxy`

### getPolygon(index)

Gets the specified polygon from the mesh.

- **`index`**: polygon number
  - type: integer

**Returns:** a polygon object.

**Return type:** `KX_PolyProxy`

### transform(matid, matrix)

Transforms the vertices of a mesh.

- **`matid`**: material index, -1 transforms all.
  - type: integer
- **`matrix`**: transformation matrix.
  - type: 4x4 matrix [[float]]

### transformUV(matid, matrix, uv_index=-1, uv_index_from=-1)

Transforms the vertices UV's of a mesh.

- **`matid`**: material index, -1 transforms all.
  - type: integer
- **`matrix`**: transformation matrix.
  - type: 4x4 matrix [[float]]
- **`uv_index`**: optional uv index, -1 for all, otherwise 0 or 1.
  - type: integer
- **`uv_index_from`**: optional uv index to copy from, -1 to transform the current uv.
  - type: integer

### replaceMaterial(matid, material)

Replace the material in slot `matid` by the material `material`.

- **`matid`**: The material index.
  - type: integer
- **`material`**: The material replacement.
  - type: `KX_BlenderMaterial`

:::caution
Changing the material of a mesh used by many objects can be slow. This function should be not called every frames
:::

### copy()

Return a duplicated mesh.

**Returns:** a duplicated mesh of the current used.

**Return type:** `KX_Mesh`.

### constructBvh(transform=mathutils.Matrix.Identity(4), epsilon=0)

Return a BVH tree based on mesh geometry. Indices of tree elements match polygons indices.

- **`transform`**: The transform 4x4 matrix applied to vertices.
  - type: `mathutils.Matrix`
- **`epsilon`**: The tree distance epsilon.
  - type: float

**Returns:** A BVH tree based on mesh geometry.

**Return type:** `mathutils.bvhtree.BVHTree`

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### destruct()

 <small>method</small>

Deletes the mesh from memory. Use only on script-created meshes no object uses anymore.

