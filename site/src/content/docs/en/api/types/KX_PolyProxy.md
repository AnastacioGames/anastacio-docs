---
title: "KX_PolyProxy"
description: "Range.types.KX_PolyProxy class reference"
---

Base class: [`SCA_IObject`](../sca_iobject/)



A polygon holds the index of the vertex forming the poylgon.

Note:
The polygon attributes are read-only, you need to retrieve the vertex proxy if you want
to change the vertex settings.

### material_name

The name of polygon material, empty if no material.

**Type:** string

### material

The material of the polygon.

**Type:** `KX_BlenderMaterial`

### texture_name

The texture name of the polygon.

**Type:** string

### material_id

The material index of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

### v1

vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

### v2

vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

### v3

vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

### ~~v4~~

:::danger[Deprecated polygons are triangles.]

:::

**Type:** integer

### visible

visible state of the polygon: 1=visible, 0=invisible.

**Type:** integer

### collide

collide state of the polygon: 1=receives collision, 0=collision free.

**Type:** integer

### vertices

Returns the list of vertices of this polygon.

**Type:** `KX_VertexProxy` list (read only)

### getMaterialName()

Returns the polygon material name with MA prefix

**Returns:** material name

**Return type:** string

### getMaterial()

**Returns:** The polygon material

**Return type:** `KX_BlenderMaterial`

### getTextureName()

**Returns:** The texture name

**Return type:** string

### getMaterialIndex()

Returns the material bucket index of the polygon.
This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

**Returns:** the material index in the mesh

**Return type:** integer

### getNumVertex()

Returns the number of vertex of the polygon.

**Returns:** number of vertex.

**Return type:** integer

### isVisible()

Returns whether the polygon is visible or not

**Returns:** 0=invisible, 1=visible

**Return type:** boolean

### isCollider()

Returns whether the polygon is receives collision or not

**Returns:** 0=collision free, 1=receives collision

**Return type:** integer

### getVertexIndex(vertex)

Returns the mesh vertex index of a polygon vertex
This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

- **`vertex`**: index of the vertex in the polygon: 0->2
- **`vertex`**: integer

**Returns:** mesh vertex index

**Return type:** integer

### getMesh()

Returns a mesh proxy

**Returns:** mesh proxy

**Return type:** `MeshProxy`

