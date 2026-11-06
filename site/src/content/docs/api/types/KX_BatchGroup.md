---
title: "KX_BatchGroup"
description: "Referência da classe Range.types.KX_BatchGroup"
---

Classe base: [`EXP_Value`](../exp_value/)



O batch group é uma classe que contém uma malha resultante da junção das malhas usadas por objetos. As malhas são juntadas com a transformação dos objetos que as usam. Uma instância desta classe não pertence a um objeto, mas é compartilhada entre objetos. Por isso, uma instância de `KX_BatchGroup` precisa ser criada passando como argumento uma lista de pelo menos um objeto com as malhas a juntar. Dá para fazer isso de um jeito parecido com:

```python

import Range

scene = Range.logic.getCurrentScene()

batchGroup = Range.types.KX_BatchGroup([scene.objects["Cube"], scene.objects["Plane"]])
```

:::caution
Configurações de render próprias de cada objeto, como `KX_GameObject.layer` e `KX_GameObject.color`, são compartilhadas ao usar batch groups. Elas vêm do objeto `referenceObject`.
:::

```python

# Junta todos os objetos com a propriedade rock para desenhar com menos chamadas.
import Range

scene = Range.logic.getCurrentScene()
rocks = [obj for obj in scene.objects if "rock" in obj]

group = Range.types.KX_BatchGroup(rocks)
print(len(group.objects))
```

```python

# Tira um objeto do grupo antes de mexer só nele.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.split([obj])
```

```python

# Desfaz o grupo e devolve a malha original de cada objeto.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.destruct()
```

### objects

A lista dos objetos juntados (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### referenceObject

O objeto usado para as configurações de render (layer, cor...).

### merge(objects)

Junta as malhas usando a transformação dos objetos que as usam.

- **`objects`**: Os objetos a juntar.
  - tipo: `EXP_ListValue` of `KX_GameObject`

### split(objects)

Separa as malhas dos objetos e restaura as malhas originais.

- **`objects`**: Os objetos a separar.
  - tipo: `EXP_ListValue` of `KX_GameObject`

### destruct()

Destrói o batch group e restaura todos os objetos para as malhas originais.

