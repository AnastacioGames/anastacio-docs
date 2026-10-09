---
title: "KX_BlenderMaterial"
description: "Referência da classe Range.types.KX_BlenderMaterial"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



This is the interface to materials in the game engine.

Materials define the render state to be applied to mesh objects.

The example below shows a simple GLSL shader setup allowing to dynamically mix two texture channels in a material. All materials of the object executing this script should have two textures using separate UV maps in the two first texture channels.

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

**Tipo:** `BL_Shader`

### blending

Ints used for pixel blending, (src, dst), matching the setBlending method.

**Tipo:** (integer, integer)

### getShader()

Returns the material's shader.

**Retorna:** the material's shader

**Tipo do retorno:** `BL_Shader`

### getTextureBindcode(textureslot)

Returns the material's texture OpenGL bind code/id/number/name.

:::danger[Obsoleto use :py:meth:`bge.types.BL_Texture.bindCode`]

:::

- **`textureslot`**: Specifies the texture slot number
  - tipo: integer

**Retorna:** the material's texture OpenGL bind code/id/number/name

**Tipo do retorno:** integer

### alpha

The material's alpha transparency.

**Tipo:** float between 0.0 and 1.0 inclusive

### hardness

How hard (sharp) the material's specular reflection is.

**Tipo:** integer between 1 and 511 inclusive

### emit

Amount of light to emit.

**Tipo:** float between 0.0 and 2.0 inclusive

### ambient

Amount of ambient light on the material.

**Tipo:** float between 0.0 and 1.0 inclusive

### specularAlpha

Alpha transparency for specular areas.

**Tipo:** float between 0.0 and 1.0 inclusive (alpha must be < 1.0)

### specularIntensity

How intense (bright) the material's specular reflection is.

**Tipo:** float between 0.0 and 1.0 inclusive

### diffuseIntensity

The material's amount of diffuse reflection.

**Tipo:** float between 0.0 and 1.0 inclusive

### specularColor

The material's specular color.

**Tipo:** `mathutils.Color`

### diffuseColor

The material's diffuse color.

**Tipo:** `mathutils.Color`

### textures

List of all material's textures.

**Tipo:** List of `BL_Texture` (read only)

### setBlending(src, dest)

Set the pixel color arithmetic functions.

- **`src`**: Specifies how the red, green, blue, and alpha source blending factors are computed, one of... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - tipo: int
- **`dest`**: Specifies how the red, green, blue, and alpha destination blending factors are computed, one of... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - tipo: int

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### passIndex

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

