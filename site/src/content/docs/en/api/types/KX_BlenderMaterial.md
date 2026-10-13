---
title: "KX_BlenderMaterial"
description: "Range.types.KX_BlenderMaterial class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`BL_Shader`](../../types/bl_shader/), [`BL_Texture`](../../types/bl_texture/), [`KX_Mesh`](../../types/kx_mesh/)
:::



This is the interface to materials in the game engine.

Materials define the render state to be applied to mesh objects.

The example below shows a simple GLSL shader setup allowing to dynamically mix two texture channels
in a material. All materials of the object executing this script should have two textures using
separate UV maps in the two first texture channels.

The code works for both Multitexture and GLSL rendering modes.

```python

from Range import logic

vertex_shader = """

void main(void)
{
   // simple projection of the vertex position to view space
   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
   // coordinate of the 1st texture channel
   gl_TexCoord[0] = gl_MultiTexCoord0;
   // coordinate of the 2nd texture channel
   gl_TexCoord[1] = gl_MultiTexCoord1;
}
"""

fragment_shader ="""

uniform sampler2D texture_0;
uniform sampler2D texture_1;
uniform float factor;

void main(void)
{
   vec4 color_0 = texture2D(texture_0, gl_TexCoord[0].st);
   vec4 color_1 = texture2D(texture_1, gl_TexCoord[1].st);
   gl_FragColor = mix(color_0, color_1, factor);
}
"""

object = logic.getCurrentController().owner

for mesh in object.meshes:
    for material in mesh.materials:
        shader = material.getShader()
        if shader is not None:
            if not shader.isValid():
                shader.setSource(vertex_shader, fragment_shader, True)

            # get the first texture channel of the material
            shader.setSampler('texture_0', 0)
            # get the second texture channel of the material
            shader.setSampler('texture_1', 1)
            # pass another uniform to the shader
            shader.setUniform1f('factor', 0.3)
```

### shader

The material's shader.

**Type:** `BL_Shader`

### blending

Ints used for pixel blending, (src, dst), matching the setBlending method.

**Type:** (integer, integer)

### getShader()

Returns the material's shader.

**Returns:** the material's shader

**Return type:** `BL_Shader`

### ~~getTextureBindcode(textureslot)~~

Returns the material's texture OpenGL bind code/id/number/name.

:::danger[Deprecated use :py:meth:`bge.types.BL_Texture.bindCode`]

:::

- **`textureslot`**: Specifies the texture slot number
  - type: integer

**Returns:** the material's texture OpenGL bind code/id/number/name

**Return type:** integer

### alpha

The material's alpha transparency.

**Type:** float between 0.0 and 1.0 inclusive

### hardness

How hard (sharp) the material's specular reflection is.

**Type:** integer between 1 and 511 inclusive

### emit

Amount of light to emit.

**Type:** float between 0.0 and 2.0 inclusive

### ambient

Amount of ambient light on the material.

**Type:** float between 0.0 and 1.0 inclusive

### specularAlpha

Alpha transparency for specular areas.

**Type:** float between 0.0 and 1.0 inclusive (alpha must be < 1.0)

### specularIntensity

How intense (bright) the material's specular reflection is.

**Type:** float between 0.0 and 1.0 inclusive

### diffuseIntensity

The material's amount of diffuse reflection.

**Type:** float between 0.0 and 1.0 inclusive

### specularColor

The material's specular color.

**Type:** `mathutils.Color`

### diffuseColor

The material's diffuse color.

**Type:** `mathutils.Color`

### textures

List of all material's textures.

**Type:** List of `BL_Texture` (read only)

### setScriptUniform(name, value)

Set a `u_` uniform declared in the Text of the GLSL Script nodes of this material
(`uniform float u_speed;`). The value is sent to the GPU on the next draw, the shader is not
compiled again. A uniform whose socket is linked to another node is not affected.

- **`name`**: Name of the uniform, as written in the Text (`"u_speed"`).
  - type: string
- **`value`**: A number, or a sequence of up to 4 numbers for vec2/vec3/vec4.
  - type: float or sequence of floats

**Returns:** True when the material has that uniform.

**Return type:** boolean

### getScriptUniform(name)

Current value of a `u_` uniform of the GLSL Script nodes of this material.

- **`name`**: Name of the uniform.
  - type: string

**Returns:** A float, a tuple (3 values for vec2/vec3, 4 for vec4) or None when there is no such uniform.

### setBlending(src, dest)

Set the pixel color arithmetic functions.

- **`src`**: Specifies how the red, green, blue, and alpha source blending factors are computed, one of... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - type: int
- **`dest`**: Specifies how the red, green, blue, and alpha destination blending factors are computed, one of... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - type: int

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### passIndex

 <small>attribute</small>

Material Pass Index, used to separate materials in filters and effects.

