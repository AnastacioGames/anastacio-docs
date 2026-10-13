---
title: "KX_2DFilter"
description: "Range.types.KX_2DFilter class reference"
---

Base class: [`BL_Shader`](../bl_shader/)

:::tip[See also]
[`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`KX_2DFilterOffScreen`](../../types/kx_2dfilteroffscreen/), [`BL_Shader`](../../types/bl_shader/)
:::



2D filter shader object. Can be alterated with `BL_Shader`'s functions.

:::caution
The vertex shader must not apply modelview and projection transformation. It should be similar to:

```glsl

void main()
{
    gl_Position = gl_Vertex;
}
```
:::

### mipmap

Request mipmap generation of the render `bgl_RenderedTexture` texture. Accessing mipmapping level is similar to:

```glsl

uniform sampler2D bgl_RenderedTexture;

void main()
{
    float level = 2.0; // mipmap level
    gl_FragColor = textureLod(bgl_RenderedTexture, gl_TexCoord[0].st, level);
}
```

**Type:** boolean

### offScreen

The custom off screen the filter render to (read-only).

**Type:** `Range.types.KX_2DFilterOffScreen` or None

### setTexture(index, bindCode, samplerName="")

Set specified texture bind code `bindCode` in specified slot `index`. Any call to `setTexture`
should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

- **`index`**: The texture slot.
  - type: integer
- **`bindCode`**: The texture bind code/Id.
  - type: integer
- **`samplerName`**: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
  - type: string

### setCubeMap(index, bindCode, samplerName="")

Set specified cube map texture bind code `bindCode` in specified slot `index`. Any call to `setCubeMap`
should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

- **`index`**: The texture slot.
  - type: integer
- **`bindCode`**: The cube map texture bind code/Id.
  - type: integer
- **`samplerName`**: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
  - type: string

### addOffScreen(slots, depth=False, width=-1, height=-1, hdr=bge.render.HDR_NONE, mipmap=False)

Register a custom off screen to render the filter to.

- **`slots`**: The number of color texture attached to the off screen, between 0 and 8 excluded.
  - type: integer
- **`depth`**: True of the off screen use a depth texture (optional).
  - type: boolean
- **`width`**: The off screen width, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
  - type: integer
- **`height`**: The off screen height, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
  - type: integer
- **`hdr`**: The image quality HDR of the color textures (optional).
  - type: one of `these constants`
- **`mipmap`**: True if the color texture generate mipmap at the end of the filter rendering (optional).
  - type: boolean

:::note
If the off screen is created using a dynamic size (`width` and `height` to -1) its bind codes will be unavailable before
the next render of the filter and the it can change when the viewport is resized.
:::

### removeOffScreen()

Unregister the custom off screen the filter render to.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### recompile(fragmentProgram=None)

 <small>method</small>

Compiles new GLSL code. Without an argument, rereads the external text file (if the filter came from one) or recompiles the current code. Returns `True` on success; otherwise see `compileLog`.

**Returns:** `bool`

### setUniform(name, value)

 <small>method</small>

Sets a shader uniform by name. The type comes from the shader (float, vec2-4, int, ivec2-4, bool, mat3, mat4 or arrays of them). The value stays after a `recompile()`.

### activeUniforms

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

List of the uniforms used by the shader, as `(name, type, size)` tuples.

### compileLog

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Messages from the last shader compile (errors and warnings). Empty when it compiled without problems.

### sourceName

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Name of the text or file the filter code came from.

### sourcePath

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Path of the filter external `.glsl` file; empty when the code is inside the `.range`.

