---
title: "KX_2DFilter"
description: "Referência da classe Range.types.KX_2DFilter"
---

Classe base: [`BL_Shader`](../bl_shader/)

:::tip[Veja também]
[`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`KX_2DFilterOffScreen`](../../types/kx_2dfilteroffscreen/), [`BL_Shader`](../../types/bl_shader/)
:::



Objeto de shader de filtro 2D. Pode ser alterado com as funções de `BL_Shader`.

:::caution
O vertex shader não deve aplicar as transformações de modelview e projeção. Ele deve ficar parecido com:

```glsl

void main()
{
    gl_Position = gl_Vertex;
}
```
:::

### mipmap

Pede a geração de mipmaps da textura de render `bgl_RenderedTexture`. Acessar um nível de mipmap fica parecido com:

```glsl

uniform sampler2D bgl_RenderedTexture;

void main()
{
    float level = 2.0; // mipmap level
    gl_FragColor = textureLod(bgl_RenderedTexture, gl_TexCoord[0].st, level);
}
```

**Tipo:** boolean

### offScreen

O off screen personalizado em que o filtro renderiza (somente leitura).

**Tipo:** `Range.types.KX_2DFilterOffScreen` or None

### setTexture(index, bindCode, samplerName="")

Coloca o bind code de textura `bindCode` no slot `index`. Toda chamada a `setTexture` deve vir seguida de uma chamada a `BL_Shader.setSampler` com o mesmo `index` se `sampleName` não for passado.

- **`index`**: O slot da textura.
  - tipo: integer
- **`bindCode`**: O bind code/Id da textura.
  - tipo: integer
- **`samplerName`**: O nome do sampler do shader ligado a `index`, se `samplerName` for passado à função (opcional).
  - tipo: string

### setCubeMap(index, bindCode, samplerName="")

Coloca o bind code de textura cube map `bindCode` no slot `index`. Toda chamada a `setCubeMap` deve vir seguida de uma chamada a `BL_Shader.setSampler` com o mesmo `index` se `sampleName` não for passado.

- **`index`**: O slot da textura.
  - tipo: integer
- **`bindCode`**: O bind code/Id da textura cube map.
  - tipo: integer
- **`samplerName`**: O nome do sampler do shader ligado a `index`, se `samplerName` for passado à função (opcional).
  - tipo: string

### addOffScreen(slots, depth=False, width=-1, height=-1, hdr=bge.render.HDR_NONE, mipmap=False)

Registra um off screen personalizado para o filtro renderizar.

- **`slots`**: O número de texturas de cor ligadas ao off screen, de 0 a 8 (8 excluído).
  - tipo: integer
- **`depth`**: True se o off screen usa uma textura de profundidade (opcional).
  - tipo: boolean
- **`width`**: A largura do off screen; -1 se ele pode ser redimensionado dinamicamente quando as dimensões da viewport mudam (opcional).
  - tipo: integer
- **`height`**: A altura do off screen; -1 se ele pode ser redimensionado dinamicamente quando as dimensões da viewport mudam (opcional).
  - tipo: integer
- **`hdr`**: A qualidade de imagem HDR das texturas de cor (opcional).
  - tipo: one of `these constants`
- **`mipmap`**: True se a textura de cor gera mipmaps no fim do render do filtro (opcional).
  - tipo: boolean

:::note
Se o off screen é criado com tamanho dinâmico (`width` e `height` iguais a -1), os bind codes ficam indisponíveis até o próximo render do filtro e podem mudar quando a viewport é redimensionada.
:::

### removeOffScreen()

Remove o registro do off screen personalizado em que o filtro renderiza.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### recompile(fragmentProgram=None)

 <small>método</small>

Compila um novo código GLSL. Sem argumento, relê o arquivo de texto externo (se o filtro veio de um) ou recompila o código atual. Retorna `True` se deu certo; senão veja `compileLog`.

**Retorna:** `bool`

### setUniform(name, value)

 <small>método</small>

Define um uniform do shader pelo nome. O tipo vem do shader (float, vec2-4, int, ivec2-4, bool, mat3, mat4 ou arrays deles). O valor continua valendo depois de um `recompile()`.

### activeUniforms

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Lista dos uniforms usados pelo shader, como tuplas `(nome, tipo, tamanho)`.

### compileLog

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Mensagens da última compilação do shader (erros e avisos). Vazio quando compilou sem problemas.

### sourceName

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Nome do texto ou arquivo de onde veio o código do filtro.

### sourcePath

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Caminho do arquivo externo `.glsl` do filtro; vazio quando o código está dentro do `.range`.

