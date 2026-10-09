---
title: "KX_VertexProxy"
description: "Referência da classe Range.types.KX_VertexProxy"
---

Classe base: [`SCA_IObject`](../sca_iobject/)



A vertex holds position, UV, color and normal information.

Note:
The physics simulation is NOT currently updated - physics will not respond
to changes in the vertex position.

### XYZ

The position of the vertex.

**Tipo:** Vector((x, y, z))

### UV

The texture coordinates of the vertex.

**Tipo:** Vector((u, v))

### uvs

The texture coordinates list of the vertex.

**Tipo:** list of Vector((u, v))

### normal

The normal of the vertex.

**Tipo:** Vector((nx, ny, nz))

### tangent

The tangent of the vertex (read-only), computed from the UV map used by the material's Normal Map or Tangent node (the active UV map by default). The w component holds the bitangent sign.

**Tipo:** Vector((tx, ty, tz, w))

### color

The color of the vertex.

**Tipo:** Vector((r, g, b, a))

Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]

### colors

The color list of the vertex.

**Tipo:** list of Vector((r, g, b, a))

### x

The x coordinate of the vertex.

**Tipo:** float

### y

The y coordinate of the vertex.

**Tipo:** float

### z

The z coordinate of the vertex.

**Tipo:** float

### u

The u texture coordinate of the vertex.

**Tipo:** float

### v

The v texture coordinate of the vertex.

**Tipo:** float

### u2

The second u texture coordinate of the vertex.

**Tipo:** float

### v2

The second v texture coordinate of the vertex.

**Tipo:** float

### r

The red component of the vertex color. 0.0 <= r <= 1.0.

**Tipo:** float

### g

The green component of the vertex color. 0.0 <= g <= 1.0.

**Tipo:** float

### b

The blue component of the vertex color. 0.0 <= b <= 1.0.

**Tipo:** float

### a

The alpha component of the vertex color. 0.0 <= a <= 1.0.

**Tipo:** float

### getXYZ()

Gets the position of this vertex.

**Retorna:** this vertexes position in local coordinates.

**Tipo do retorno:** Vector((x, y, z))

### setXYZ(pos)

Sets the position of this vertex.

**Tipo:** Vector((x, y, z))

- **`pos`**: the new position for this vertex in local coordinates.

### getUV()

Gets the UV (texture) coordinates of this vertex.

**Retorna:** this vertexes UV (texture) coordinates.

**Tipo do retorno:** Vector((u, v))

### setUV(uv)

Sets the UV (texture) coordinates of this vertex.

**Tipo:** Vector((u, v))

### getUV2()

Gets the 2nd UV (texture) coordinates of this vertex.

**Retorna:** this vertexes UV (texture) coordinates.

**Tipo do retorno:** Vector((u, v))

### setUV2(uv, unit)

Sets the 2nd UV (texture) coordinates of this vertex.

**Tipo:** Vector((u, v))

- **`unit`**: optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UV
- **`unit`**: integer

### getRGBA()

Gets the color of this vertex.

The color is represented as four bytes packed into an integer value.  The color is
packed as RGBA.

Since Python offers no way to get each byte without shifting, you must use the struct module to
access color in an machine independent way.

Because of this, it is suggested you use the r, g, b and a attributes or the color attribute instead.

``python

import struct;
col = struct.unpack('4B', struct.pack('I', v.getRGBA()))
# col = (r, g, b, a)
# black = (  0, 0, 0, 255)
# white = (255, 255, 255, 255)
``

**Retorna:** packed color. 4 byte integer with one byte per color channel in RGBA format.

**Tipo do retorno:** integer

### setRGBA(col)

Sets the color of this vertex.

See getRGBA() for the format of col, and its relevant problems.  Use the r, g, b and a attributes
or the color attribute instead.

setRGBA() also accepts a four component list as argument col.  The list represents the color as [r, g, b, a]
with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]

``python

v.setRGBA(0xff0000ff) # Red
v.setRGBA(0xff00ff00) # Green on little endian, transparent purple on big endian
v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Red
v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Green on all platforms.
``

- **`col`**: the new color of this vertex in packed RGBA format.
  - tipo: integer or list [r, g, b, a]

### getNormal()

Gets the normal vector of this vertex.

**Retorna:** normalized normal vector.

**Tipo do retorno:** Vector((nx, ny, nz))

### setNormal(normal)

Sets the normal vector of this vertex.

**Tipo:** sequence of floats [r, g, b]

- **`normal`**: the new normal of this vertex.

