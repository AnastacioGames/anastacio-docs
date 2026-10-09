---
title: "KX_LodLevel"
description: "Referência da classe Range.types.KX_LodLevel"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Um nível de LOD do lod manager de um game object.

### mesh

A malha usada neste nível de LOD (somente leitura).

**Tipo:** `RAS_MeshObject`

### level

O número do nível de LOD (somente leitura).

**Tipo:** integer

### distance

Distância a partir da qual este nível de detalhe é usado (somente leitura).

**Tipo:** float (0.0 to infinite)

### hysteresis

Mudança mínima do fator de distância, em porcentagem, para voltar ao nível de detalhe anterior (somente leitura).

**Tipo:** float [0.0 to 100.0]

### useMesh

True se o nível de LOD usa uma malha diferente da malha original do objeto (somente leitura).

**Tipo:** boolean

### useMaterial

True se o nível de LOD usa um material diferente do material original da malha do objeto (somente leitura).

**Tipo:** boolean

### useHysteresis

True se o nível de LOD usa substituição de histerese (somente leitura).

**Tipo:** boolean

