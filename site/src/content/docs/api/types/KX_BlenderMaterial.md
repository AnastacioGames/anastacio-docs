---
title: "KX_BlenderMaterial"
description: "Referência da classe Range.types.KX_BlenderMaterial"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Esta é a interface para os materiais na game engine.

Os materiais definem o estado de render aplicado aos objetos de malha.

O exemplo abaixo mostra uma configuração simples de shader GLSL que mistura dinamicamente dois canais de textura num material. Todos os materiais do objeto que roda este script devem ter duas texturas usando UV maps separados nos dois primeiros canais de textura.

O código funciona nos modos de render Multitexture e GLSL.

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

            # pega o primeiro canal de textura do material
            shader.setSampler('texture_0', 0)
            # pega o segundo canal de textura do material
            shader.setSampler('texture_1', 1)
            # passa outro uniform para o shader
            shader.setUniform1f('factor', 0.3)
```

### shader

O shader do material.

**Tipo:** `BL_Shader`

### blending

Inteiros usados na mistura de pixels, (src, dst), iguais aos do método setBlending.

**Tipo:** (integer, integer)

### getShader()

Devolve o shader do material.

**Retorna:** o shader do material

**Tipo do retorno:** `BL_Shader`

### getTextureBindcode(textureslot)

Devolve o bind code/id/número/nome OpenGL da textura do material.

:::danger[Obsoleto use :py:meth:`bge.types.BL_Texture.bindCode`]

:::

- **`textureslot`**: Define o número do slot de textura
  - tipo: integer

**Retorna:** o bind code/id/número/nome OpenGL da textura do material

**Tipo do retorno:** integer

### alpha

A transparência alpha do material.

**Tipo:** float between 0.0 and 1.0 inclusive

### hardness

Quão dura (nítida) é a reflexão especular do material.

**Tipo:** integer between 1 and 511 inclusive

### emit

Quantidade de luz emitida.

**Tipo:** float between 0.0 and 2.0 inclusive

### ambient

Quantidade de luz ambiente no material.

**Tipo:** float between 0.0 and 1.0 inclusive

### specularAlpha

Transparência alpha das áreas especulares.

**Tipo:** float between 0.0 and 1.0 inclusive (alpha must be < 1.0)

### specularIntensity

Quão intensa (brilhante) é a reflexão especular do material.

**Tipo:** float between 0.0 and 1.0 inclusive

### diffuseIntensity

A quantidade de reflexão difusa do material.

**Tipo:** float between 0.0 and 1.0 inclusive

### specularColor

A cor especular do material.

**Tipo:** `mathutils.Color`

### diffuseColor

A cor difusa do material.

**Tipo:** `mathutils.Color`

### textures

Lista de todas as texturas do material.

**Tipo:** List of `BL_Texture` (read only)

### setBlending(src, dest)

Define as funções aritméticas de cor dos pixels.

- **`src`**: Define como os fatores de mistura de origem de vermelho, verde, azul e alpha são calculados; um destes... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - tipo: int
- **`dest`**: Define como os fatores de mistura de destino de vermelho, verde, azul e alpha são calculados; um destes... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - tipo: int

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### passIndex

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

