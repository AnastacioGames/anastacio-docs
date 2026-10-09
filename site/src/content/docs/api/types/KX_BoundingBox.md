---
title: "KX_BoundingBox"
description: "Referência da classe Range.types.KX_BoundingBox"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Uma caixa de volume de um game object. Usada para ler e alterar a caixa de volume ou AABB.

```python

from Range import logic
from mathutils import Vector

owner = logic.getCurrentController().owner
box = owner.cullingBox

# Desliga a atualização automática para permitir modificar a caixa.
box.autoUpdate = False

print(box)
# Aumenta a altura da caixa em 1.
box.max = box.max + Vector((0, 0, 1))

print(box)
```

### min

O ponto mínimo da bounding box nos eixos x, y e z.

**Tipo:** `mathutils.Vector`

### max

O ponto máximo da bounding box nos eixos x, y e z.

**Tipo:** `mathutils.Vector`

### center

O centro da bounding box (somente leitura).

**Tipo:** `mathutils.Vector`

### radius

O raio da bounding box (somente leitura).

**Tipo:** float

### autoUpdate

Permite atualizar a bounding box se a malha for modificada.

**Tipo:** boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### volume

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

