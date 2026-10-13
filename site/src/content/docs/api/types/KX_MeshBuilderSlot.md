---
title: "KX_MeshBuilderSlot"
description: "Referência da classe Range.types.KX_MeshBuilderSlot"
---

:::tip[Veja também]
[`KX_MeshBuilder`](../../types/kx_meshbuilder/), [`KX_Mesh`](../../types/kx_mesh/)
:::

Classe `Range.types.KX_MeshBuilderSlot`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### addIndex(indices)

 <small>método</small>

Acrescenta índices de vértices (lista de inteiros) aos primitivos e, se for malha de triângulos, aos triângulos.

### addPrimitiveIndex(indices)

 <small>método</small>

Acrescenta índices só à lista de primitivos (desenho).

### addTriangleIndex(indices)

 <small>método</small>

Acrescenta índices só à lista de triângulos (física e raios).

### addVertex(position, normal=None, tangent=None, uvs=None, colors=None)

 <small>método</small>

Acrescenta um vértice. `uvs` e `colors` são listas, uma entrada por camada.

**Retorna:** `int`

### recalculateNormals()

 <small>método</small>

Recalcula as normais dos vértices a partir dos triângulos.

### removePrimitiveIndex(start, end=-1)

 <small>método</small>

Remove índices de primitivos de `start` até `end`.

### removeTriangleIndex(start, end=-1)

 <small>método</small>

Remove índices de triângulos de `start` até `end`.

### removeVertex(start, end=-1)

 <small>método</small>

Remove vértices de `start` até `end`.

### colorCount

 <small>atributo · só leitura</small>

Quantas camadas de cor de vértice o slot tem.

### indices

 <small>atributo · só leitura</small>

Lista dos índices de primitivos.

### material

 <small>atributo</small>

Material do slot.

### primitive

 <small>atributo · só leitura</small>

Tipo de primitivo do slot (pontos, linhas ou triângulos).

### triangleIndices

 <small>atributo · só leitura</small>

Lista dos índices de triângulos.

### uvCount

 <small>atributo · só leitura</small>

Quantas camadas de UV o slot tem.

### vertices

 <small>atributo · só leitura</small>

Lista dos vértices do slot.

