---
title: "KX_VertexProxy"
description: "Referência da classe Range.types.KX_VertexProxy"
---

Classe base: [`SCA_IObject`](../sca_iobject/)



Um vértice guarda informações de posição, UV, cor e normal.

Nota: a simulação de física NÃO é atualizada por enquanto; a física não reage a mudanças na posição do vértice.

### XYZ

A posição do vértice.

**Tipo:** Vector((x, y, z))

### UV

As coordenadas de textura do vértice.

**Tipo:** Vector((u, v))

### uvs

A lista de coordenadas de textura do vértice.

**Tipo:** list of Vector((u, v))

### normal

A normal do vértice.

**Tipo:** Vector((nx, ny, nz))

### tangent

A tangente do vértice (somente leitura), calculada a partir do UV map usado pelo nó Normal Map ou Tangent do material (o UV map ativo por padrão). O componente w guarda o sinal da bitangente.

**Tipo:** Vector((tx, ty, tz, w))

### color

A cor do vértice.

**Tipo:** Vector((r, g, b, a))

Preto = [0.0, 0.0, 0.0, 1.0], branco = [1.0, 1.0, 1.0, 1.0]

### colors

A lista de cores do vértice.

**Tipo:** list of Vector((r, g, b, a))

### x

A coordenada x do vértice.

**Tipo:** float

### y

A coordenada y do vértice.

**Tipo:** float

### z

A coordenada z do vértice.

**Tipo:** float

### u

A coordenada de textura u do vértice.

**Tipo:** float

### v

A coordenada de textura v do vértice.

**Tipo:** float

### u2

A segunda coordenada de textura u do vértice.

**Tipo:** float

### v2

A segunda coordenada de textura v do vértice.

**Tipo:** float

### r

O componente vermelho da cor do vértice. 0.0 <= r <= 1.0.

**Tipo:** float

### g

O componente verde da cor do vértice. 0.0 <= g <= 1.0.

**Tipo:** float

### b

O componente azul da cor do vértice. 0.0 <= b <= 1.0.

**Tipo:** float

### a

O componente alpha da cor do vértice. 0.0 <= a <= 1.0.

**Tipo:** float

### getXYZ()

Pega a posição deste vértice.

**Retorna:** a posição deste vértice em coordenadas locais.

**Tipo do retorno:** Vector((x, y, z))

### setXYZ(pos)

Define a posição deste vértice.

**Tipo:** Vector((x, y, z))

- **`pos`**: a nova posição deste vértice em coordenadas locais.

### getUV()

Pega as coordenadas UV (de textura) deste vértice.

**Retorna:** as coordenadas UV (de textura) deste vértice.

**Tipo do retorno:** Vector((u, v))

### setUV(uv)

Define as coordenadas UV (de textura) deste vértice.

**Tipo:** Vector((u, v))

### getUV2()

Pega as 2ªs coordenadas UV (de textura) deste vértice.

**Retorna:** as coordenadas UV (de textura) deste vértice.

**Tipo do retorno:** Vector((u, v))

### setUV2(uv, unit)

Define as 2ªs coordenadas UV (de textura) deste vértice.

**Tipo:** Vector((u, v))

- **`unit`**: argumento opcional, FLAT==1, SECOND_UV==2; o padrão é SECOND_UV
- **`unit`**: inteiro

### getRGBA()

Pega a cor deste vértice.

A cor é representada como quatro bytes empacotados num inteiro, no formato RGBA.

Como o Python não tem como pegar cada byte sem deslocamento de bits, use o módulo struct para acessar a cor de um jeito independente da máquina.

Por isso, é recomendado usar os atributos r, g, b e a ou o atributo color.

```python

import struct;
col = struct.unpack('4B', struct.pack('I', v.getRGBA()))
# col = (r, g, b, a)
# black = (  0, 0, 0, 255)
# white = (255, 255, 255, 255)
```

**Retorna:** cor empacotada. Inteiro de 4 bytes com um byte por canal de cor, no formato RGBA.

**Tipo do retorno:** integer

### setRGBA(col)

Define a cor deste vértice.

Veja getRGBA() para o formato de col e os problemas dele. Use os atributos r, g, b e a ou o atributo color.

setRGBA() também aceita uma lista de quatro componentes como argumento col. A lista representa a cor como [r, g, b, a], com preto = [0.0, 0.0, 0.0, 1.0] e branco = [1.0, 1.0, 1.0, 1.0]

```python

v.setRGBA(0xff0000ff) # Vermelho
v.setRGBA(0xff00ff00) # Verde em little endian, roxo transparente em big endian
v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Vermelho
v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Verde em todas as plataformas.
```

- **`col`**: a nova cor deste vértice, no formato RGBA empacotado.
  - tipo: integer or list [r, g, b, a]

### getNormal()

Pega o vetor normal deste vértice.

**Retorna:** vetor normal normalizado.

**Tipo do retorno:** Vector((nx, ny, nz))

### setNormal(normal)

Define o vetor normal deste vértice.

**Tipo:** sequence of floats [r, g, b]

- **`normal`**: a nova normal deste vértice.

