---
title: "KX_MeshBuilder"
description: "Referência da classe Range.types.KX_MeshBuilder"
---

Classe `Range.types.KX_MeshBuilder`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### addSlot(material, primitive=0)

 <small>método</small>

Cria uma parte da malha com o material dado. `primitive`: 0 triângulos (padrão), 1 pontos, 2 linhas.

**Retorna:** `KX_MeshBuilderSlot`

### finish()

 <small>método</small>

Monta a malha com os slots e a registra na cena. Depois use `obj.replaceMesh()` para colocá-la num objeto.

**Retorna:** `KX_Mesh`

### FromMesh(name, mesh)

 <small>método</small>

Cria um construtor a partir de uma malha existente, para copiá-la e editá-la.

**Retorna:** `KX_MeshBuilder`

### slots

 <small>atributo · só leitura</small>

Lista dos slots (`KX_MeshBuilderSlot`) da malha.

