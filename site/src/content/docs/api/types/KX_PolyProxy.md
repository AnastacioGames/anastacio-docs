---
title: "KX_PolyProxy"
description: "Referência da classe Range.types.KX_PolyProxy"
---

Classe base: [`SCA_IObject`](../sca_iobject/)



A polygon holds the index of the vertex forming the poylgon.

Note: The polygon attributes are read-only, you need to retrieve the vertex proxy if you want to change the vertex settings.

### material_name

The name of polygon material, empty if no material.

**Tipo:** string

### material

The material of the polygon.

**Tipo:** `KX_BlenderMaterial`

### texture_name

The texture name of the polygon.

**Tipo:** string

### material_id

The material index of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Tipo:** integer

### v1

vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Tipo:** integer

### v2

vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Tipo:** integer

### v3

vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Tipo:** integer

### v4

:::danger[Obsoleto polygons are triangles.]

:::

**Tipo:** integer

### visible

visible state of the polygon: 1=visible, 0=invisible.

**Tipo:** integer

### collide

collide state of the polygon: 1=receives collision, 0=collision free.

**Tipo:** integer

### vertices

Returns the list of vertices of this polygon.

**Tipo:** `KX_VertexProxy` list (read only)

### getMaterialName()

Returns the polygon material name with MA prefix

**Retorna:** material name

**Tipo do retorno:** string

### getMaterial()

**Retorna:** The polygon material

**Tipo do retorno:** `KX_BlenderMaterial`

### getTextureName()

**Retorna:** The texture name

**Tipo do retorno:** string

### getMaterialIndex()

Returns the material bucket index of the polygon. This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

**Retorna:** the material index in the mesh

**Tipo do retorno:** integer

### getNumVertex()

Returns the number of vertex of the polygon.

**Retorna:** number of vertex.

**Tipo do retorno:** integer

### isVisible()

Returns whether the polygon is visible or not

**Retorna:** 0=invisible, 1=visible

**Tipo do retorno:** boolean

### isCollider()

Returns whether the polygon is receives collision or not

**Retorna:** 0=collision free, 1=receives collision

**Tipo do retorno:** integer

### getVertexIndex(vertex)

Returns the mesh vertex index of a polygon vertex This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

- **`vertex`**: index of the vertex in the polygon: 0->2
- **`vertex`**: integer

**Retorna:** mesh vertex index

**Tipo do retorno:** integer

### getMesh()

Returns a mesh proxy

**Retorna:** mesh proxy

**Tipo do retorno:** `MeshProxy`

