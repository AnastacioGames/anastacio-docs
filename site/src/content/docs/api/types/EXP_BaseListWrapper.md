---
title: "EXP_BaseListWrapper"
description: "Referência da classe Range.types.EXP_BaseListWrapper"
---

Classe `Range.types.EXP_BaseListWrapper`.

```python
# Essas listas funcionam por nome ou por índice, como sensores ou canais.
import Range

armature = Range.logic.getCurrentController().owner

head = armature.channels.get("Head")
first = armature.channels[0]
print(head, first)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### get(key, default=None)

 <small>método</small>

Item com esse nome, ou `default` se não existir.

**Retorna:** `object`

