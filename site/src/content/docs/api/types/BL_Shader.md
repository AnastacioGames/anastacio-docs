---
title: "BL_Shader"
description: "Referência da classe Range.types.BL_Shader"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



BL_Shader é uma classe usada para compilar e usar scripts de shader personalizados. Suporta vertex, fragment e geometry shaders. O shader é compilado com um cabeçalho gerado para os três scripts. Esse cabeçalho define a diretiva `#version`, então o usuário não deve definir a sua própria `#version`.

### enabled

Liga o shader para uso.

**Tipo:** boolean

### objectCallbacks

A lista de callbacks Python executados quando o shader é usado para renderizar um objeto. Todas as funções recebem como argumento o objeto sendo renderizado.

```python

def callback(object):
    print("render object %r" % object.name)
```

**Tipo:** list of functions and/or methods

### bindCallbacks

A lista de callbacks Python executados quando o shader começa a ser usado no render.

**Tipo:** list of functions and/or methods

### setUniformfv(name, fList)

Define um uniform com uma lista de valores float

- **`name`**: o nome do uniform
  - tipo: string
- **`fList`**: uma lista (2, 3 ou 4 elementos) de valores float
  - tipo: list[float]

### delSource()

Limpa o shader. Use este método antes de mudar o código com `setSource`.

### getFragmentProg()

Devolve o fragment program.

**Retorna:** O fragment program.

**Tipo do retorno:** string

### getVertexProg()

Pega o vertex program.

**Retorna:** O vertex program.

**Tipo do retorno:** string

### isValid()

Verifica se o shader é válido.

**Retorna:** True se o shader é válido

**Tipo do retorno:** boolean

### setAttrib(enum)

Define a location do atributo. (O parâmetro é ignorado por enquanto e o valor de "tangent" é sempre usado.)

- **`enum`**: valor da location do atributo
  - tipo: integer

### setSampler(name, index)

Define o índice de sampler de textura do uniform.

- **`name`**: Nome do uniform
  - tipo: string
- **`index`**: Índice do sampler de textura.
  - tipo: integer

### setSource(vertexProgram, fragmentProgram, apply)

Define os programas de vertex e fragment

- **`vertexProgram`**: Vertex program
  - tipo: string
- **`fragmentProgram`**: Fragment program
  - tipo: string
- **`apply`**: Liga o shader.
  - tipo: boolean

### setSourceList(sources, apply)

Define os programas de vertex, fragment e geometry shader.

- **`sources`**: Dicionário com todos os programas. As chaves `vertex`, `fragment` e `geometry` representam os programas de mesmo nome. `geometry` é opcional. Este dicionário pode ficar parecido com: .. code-block:: python sources = { "vertex" : vertexProgram, "fragment" : fragmentProgram, "geometry" : geometryProgram }
  - tipo: dict
- **`apply`**: Liga o shader.
  - tipo: boolean

### setUniform1f(name, fx)

Define um uniform com 1 valor float.

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: Valor do uniform
  - tipo: float

### setUniform1i(name, ix)

Define um uniform com um valor inteiro.

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: o valor do uniform
  - tipo: integer

### setUniform2f(name, fx, fy)

Define um uniform com 2 valores float

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: primeiro valor float
  - tipo: float
- **`fy`**: segundo valor float
  - tipo: float

### setUniform2i(name, ix, iy)

Define um uniform com 2 valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: primeiro valor inteiro
  - tipo: integer
- **`iy`**: segundo valor inteiro
  - tipo: integer

### setUniform3f(name, fx, fy, fz)

Define um uniform com 3 valores float.

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: primeiro valor float
  - tipo: float
- **`fy`**: segundo valor float
  - tipo: float
- **`fz`**: terceiro valor float
  - tipo: float

### setUniform3i(name, ix, iy, iz)

Define um uniform com 3 valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: primeiro valor inteiro
  - tipo: integer
- **`iy`**: segundo valor inteiro
  - tipo: integer
- **`iz`**: terceiro valor inteiro
  - tipo: integer

### setUniform4f(name, fx, fy, fz, fw)

Define um uniform com 4 valores float.

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: primeiro valor float
  - tipo: float
- **`fy`**: segundo valor float
  - tipo: float
- **`fz`**: terceiro valor float
  - tipo: float
- **`fw`**: quarto valor float
  - tipo: float

### setUniform4i(name, ix, iy, iz, iw)

Define um uniform com 4 valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: primeiro valor inteiro
  - tipo: integer
- **`iy`**: segundo valor inteiro
  - tipo: integer
- **`iz`**: terceiro valor inteiro
  - tipo: integer
- **`iw`**: quarto valor inteiro
  - tipo: integer

### setUniformDef(name, type)

Define um novo uniform

- **`name`**: o nome do uniform
  - tipo: string
- **`type`**: tipo do uniform, uma `destas constantes`
  - tipo: integer

### setUniformMatrix3(name, mat, transpose)

Define um uniform com uma matriz 3x3

- **`name`**: o nome do uniform
  - tipo: string
- **`mat`**: Uma matriz 3x3 [[f, f, f], [f, f, f], [f, f, f]]
  - tipo: 3x3 matrix
- **`transpose`**: use True para transpor a matriz
  - tipo: boolean

### setUniformMatrix4(name, mat, transpose)

Define um uniform com uma matriz 4x4

- **`name`**: o nome do uniform
  - tipo: string
- **`mat`**: Uma matriz 4x4 [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
  - tipo: 4x4 matrix
- **`transpose`**: use True para transpor a matriz
  - tipo: boolean

### setUniformiv(name, iList)

Define um uniform com uma lista de valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`iList`**: uma lista (2, 3 ou 4 elementos) de valores inteiros
  - tipo: list[integer]

### setUniformEyef(name)

Define um uniform com um valor float que indica o olho sendo renderizado no modo estéreo: 0.0 para o olho esquerdo, 0.5 para o direito. Fora do modo estéreo, o valor fica fixo em 0.0. O uso típico é no modo estéreo, para ler texturas estéreo com as imagens dos olhos esquerdo e direito em ordem de cima para baixo.

- **`name`**: o nome do uniform
  - tipo: string

### validate()

Valida o objeto de shader.

