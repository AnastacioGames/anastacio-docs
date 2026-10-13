---
title: "EXP_BaseListValue"
description: "Referência da classe Range.types.EXP_BaseListValue"
---

Classe `Range.types.EXP_BaseListValue`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### append(item)

 <small>método</small>

Acrescenta um item no fim da lista. Só funciona em listas criadas pelo script; listas internas da engine (ex.: `scene.objects`) não podem ser alteradas.

### count(item)

 <small>método</small>

Quantas vezes o item aparece na lista.

**Retorna:** `int`

### filter(name, prop='')

 <small>método</small>

Nova lista só com os itens cujo nome contém `name` e que têm a propriedade de jogo `prop`. Pelo menos um dos dois precisa ser preenchido.

**Retorna:** `EXP_ListValue`

### from_id(id)

 <small>método</small>

Procura o item pelo `id()` do Python. Útil para guardar a referência de um objeto como número.

**Retorna:** `object`

### get(key, default=None)

 <small>método</small>

Item com esse nome, ou `default` se não existir. Ex.: `scene.objects.get('Player')`.

**Retorna:** `object`

### index(item)

 <small>método</small>

Posição do item na lista. Dá erro se ele não estiver nela.

**Retorna:** `int`

### reverse()

 <small>método</small>

Inverte a ordem da lista. Só em listas criadas pelo script.

