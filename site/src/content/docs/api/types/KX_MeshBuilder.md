---
title: "KX_MeshBuilder"
description: "Referência da classe Range.types.KX_MeshBuilder"
---

:::tip[Veja também]
[`KX_MeshBuilderSlot`](../../types/kx_meshbuilderslot/), [`KX_Mesh`](../../types/kx_mesh/), [`KX_GameObject`](../../types/kx_gameobject/)
:::

Classe `Range.types.KX_MeshBuilder`.

```python
# Cria um triângulo por script e coloca no objeto.
import Range

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder("Triangle", scene, ["UVMap"], ["Col"])
slot = builder.addSlot(own.meshes[0].materials[0])

a = slot.addVertex((0.0, 0.0, 0.0))
b = slot.addVertex((1.0, 0.0, 0.0))
c = slot.addVertex((0.0, 1.0, 0.0))
slot.addIndex([a, b, c])
slot.recalculateNormals()

own.replaceMesh(builder.finish())
```

```python
# Copia uma malha existente para alterar. Guarde o construtor em uma variável enquanto usa os slots.
import Range

own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder.FromMesh("Copy", own.meshes[0])
print(len(builder.slots))
```



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

