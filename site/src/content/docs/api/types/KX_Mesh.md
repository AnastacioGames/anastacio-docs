---
title: "KX_Mesh"
description: "Referência da classe Range.types.KX_Mesh"
---

Classe base: [`EXP_Value`](../exp_value/)



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

**Tipo:** list of `KX_BlenderMaterial` type

### numPolygons

**Tipo:** integer

### numMaterials

**Tipo:** integer

### polygons

Returns the list of polygons of this mesh.

**Tipo:** `KX_PolyProxy` list (read only)

### getMaterialName(matid)

Gets the name of the specified material.

- **`matid`**: the specified material.
  - tipo: integer

**Retorna:** the attached material name.

**Tipo do retorno:** string

### getTextureName(matid)

Gets the name of the specified material's texture.

- **`matid`**: the specified material
  - tipo: integer

**Retorna:** the attached material's texture name.

**Tipo do retorno:** string

### getVertexArrayLength(matid)

Gets the length of the vertex array associated with the specified material.

There is one vertex array for each material.

- **`matid`**: the specified material
  - tipo: integer

**Retorna:** the number of verticies in the vertex array.

**Tipo do retorno:** integer

### getVertex(matid, index)

Gets the specified vertex from the mesh object.

- **`matid`**: the specified material
  - tipo: integer
- **`index`**: the index into the vertex array.
  - tipo: integer

**Retorna:** a vertex object.

**Tipo do retorno:** `KX_VertexProxy`

### getPolygon(index)

Gets the specified polygon from the mesh.

- **`index`**: polygon number
  - tipo: integer

**Retorna:** a polygon object.

**Tipo do retorno:** `KX_PolyProxy`

### transform(matid, matrix)

Transforms the vertices of a mesh.

- **`matid`**: material index, -1 transforms all.
  - tipo: integer
- **`matrix`**: transformation matrix.
  - tipo: 4x4 matrix [[float]]

### transformUV(matid, matrix, uv_index=-1, uv_index_from=-1)

Transforms the vertices UV's of a mesh.

- **`matid`**: material index, -1 transforms all.
  - tipo: integer
- **`matrix`**: transformation matrix.
  - tipo: 4x4 matrix [[float]]
- **`uv_index`**: optional uv index, -1 for all, otherwise 0 or 1.
  - tipo: integer
- **`uv_index_from`**: optional uv index to copy from, -1 to transform the current uv.
  - tipo: integer

### replaceMaterial(matid, material)

Replace the material in slot `matid` by the material `material`.

- **`matid`**: The material index.
  - tipo: integer
- **`material`**: The material replacement.
  - tipo: `KX_BlenderMaterial`

:::caution
Changing the material of a mesh used by many objects can be slow. This function should be not called every frames
:::

### copy()

Return a duplicated mesh.

**Retorna:** a duplicated mesh of the current used.

**Tipo do retorno:** `KX_Mesh`.

### constructBvh(transform=mathutils.Matrix.Identity(4), epsilon=0)

Return a BVH tree based on mesh geometry. Indices of tree elements match polygons indices.

- **`transform`**: The transform 4x4 matrix applied to vertices.
  - tipo: `mathutils.Matrix`
- **`epsilon`**: The tree distance epsilon.
  - tipo: float

**Retorna:** A BVH tree based on mesh geometry.

**Tipo do retorno:** `mathutils.bvhtree.BVHTree`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### destruct()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

