---
title: "KX_PolyProxy"
description: "Referência da classe Range.types.KX_PolyProxy"
---

Classe base: [`SCA_IObject`](../sca_iobject/)



Um polígono guarda o índice dos vértices que o formam.

Nota: os atributos do polígono são somente leitura; para mudar as configurações de um vértice, pegue o vertex proxy.

### material_name

O nome do material do polígono; vazio se não houver material.

**Tipo:** string

### material

O material do polígono.

**Tipo:** `KX_BlenderMaterial`

### texture_name

O nome da textura do polígono.

**Tipo:** string

### material_id

O índice do material do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

### v1

índice do primeiro vértice do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

### v2

índice do segundo vértice do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

### v3

índice do terceiro vértice do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

### ~~v4~~

:::danger[Obsoleto polygons are triangles.]

:::

**Tipo:** integer

### visible

estado de visibilidade do polígono: 1=visível, 0=invisível.

**Tipo:** integer

### collide

estado de colisão do polígono: 1=recebe colisão, 0=sem colisão.

**Tipo:** integer

### vertices

Devolve a lista de vértices deste polígono.

**Tipo:** `KX_VertexProxy` list (read only)

### getMaterialName()

Devolve o nome do material do polígono com o prefixo MA

**Retorna:** nome do material

**Tipo do retorno:** string

### getMaterial()

**Retorna:** O material do polígono

**Tipo do retorno:** `KX_BlenderMaterial`

### getTextureName()

**Retorna:** O nome da textura

**Tipo do retorno:** string

### getMaterialIndex()

Devolve o índice do material bucket do polígono. Este índice e os devolvidos por getVertexIndex() são necessários para pegar o vertex proxy a partir de `MeshProxy`.

**Retorna:** o índice do material na malha

**Tipo do retorno:** integer

### getNumVertex()

Devolve o número de vértices do polígono.

**Retorna:** número de vértices.

**Tipo do retorno:** integer

### isVisible()

Diz se o polígono está visível ou não

**Retorna:** 0=invisível, 1=visível

**Tipo do retorno:** boolean

### isCollider()

Diz se o polígono recebe colisão ou não

**Retorna:** 0=sem colisão, 1=recebe colisão

**Tipo do retorno:** integer

### getVertexIndex(vertex)

Devolve o índice, na malha, de um vértice do polígono. Este índice e o devolvido por getMaterialIndex() são necessários para pegar o vertex proxy a partir de `MeshProxy`.

- **`vertex`**: índice do vértice no polígono: 0->2
- **`vertex`**: inteiro

**Retorna:** índice do vértice na malha

**Tipo do retorno:** integer

### getMesh()

Devolve um mesh proxy

**Retorna:** mesh proxy

**Tipo do retorno:** `MeshProxy`

