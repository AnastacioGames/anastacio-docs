---
title: "KX_2DFilter"
description: "Referência da classe Range.types.KX_2DFilter"
---

Classe base: [`BL_Shader`](../bl_shader/)



2D filter shader object. Can be alterated with `BL_Shader`'s functions.

:::caution
The vertex shader must not apply modelview and projection transformation. It should be similar to:

``glsl

void main()
{
    gl_Position = gl_Vertex;
}
``
:::

### mipmap

Request mipmap generation of the render `bgl_RenderedTexture` texture. Accessing mipmapping level is similar to:

``glsl

uniform sampler2D bgl_RenderedTexture;

void main()
{
    float level = 2.0; // mipmap level
    gl_FragColor = textureLod(bgl_RenderedTexture, gl_TexCoord[0].st, level);
}
``

**Tipo:** boolean

### offScreen

The custom off screen the filter render to (read-only).

**Tipo:** `Range.types.KX_2DFilterOffScreen` or None

### setTexture(index, bindCode, samplerName="")

Set specified texture bind code `bindCode` in specified slot `index`. Any call to `setTexture`
should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

- **`index`**: The texture slot.
  - tipo: integer
- **`bindCode`**: The texture bind code/Id.
  - tipo: integer
- **`samplerName`**: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
  - tipo: string

### setCubeMap(index, bindCode, samplerName="")

Set specified cube map texture bind code `bindCode` in specified slot `index`. Any call to `setCubeMap`
should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

- **`index`**: The texture slot.
  - tipo: integer
- **`bindCode`**: The cube map texture bind code/Id.
  - tipo: integer
- **`samplerName`**: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
  - tipo: string

### addOffScreen(slots, depth=False, width=-1, height=-1, hdr=Range.render.HDR_NONE, mipmap=False)

Register a custom off screen to render the filter to.

- **`slots`**: The number of color texture attached to the off screen, between 0 and 8 excluded.
  - tipo: integer
- **`depth`**: True of the off screen use a depth texture (optional).
  - tipo: boolean
- **`width`**: The off screen width, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
  - tipo: integer
- **`height`**: The off screen height, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
  - tipo: integer
- **`hdr`**: The image quality HDR of the color textures (optional).
  - tipo: one of `these constants`
- **`mipmap`**: True if the color texture generate mipmap at the end of the filter rendering (optional).
  - tipo: boolean

:::note
If the off screen is created using a dynamic size (`width` and `height` to -1) its bind codes will be unavailable before
the next render of the filter and the it can change when the viewport is resized.
:::

### removeOffScreen()

Unregister the custom off screen the filter render to.

