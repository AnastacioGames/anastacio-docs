---
title: "EXP_ListValue"
description: "Referência da classe Range.types.EXP_ListValue"
---

Classe base: [`EXP_PropValue`](../exp_propvalue/)



Este é um objeto parecido com lista, usado internamente pela game engine, que na maioria dos casos se comporta como uma lista Python.

Além da busca normal por índice (`val= clist[i]`), EXP_ListValue aceita busca por string (`val= scene.objects["Cube"]`)

Outras operações, como `len(clist)`, `list(clist)` e `clist[0:10]`, também são suportadas.

### append(val)

Adiciona um item à lista (como o append do Python)

:::caution
Adicionar valores à lista pode travar o jogo quando a lista é usada internamente pela game engine.
:::

### count(val)

Conta quantas vezes um valor aparece na lista.

**Retorna:** número de ocorrências

**Tipo do retorno:** integer

### index(val)

Devolve o índice de um valor na lista.

**Retorna:** O índice do valor na lista.

**Tipo do retorno:** integer

### reverse()

Inverte a ordem da lista.

### get(key, default=None)

Devolve o valor da chave, ou o valor padrão se a chave não existir.

**Retorna:** O valor da chave ou o padrão.

### filter(name, prop)

Devolve uma lista dos itens cujo nome casa com a regex `name` e que têm uma propriedade que casa com a regex `prop`. Se `name` estiver vazio, todos os itens são verificados; se `prop` estiver vazio, as propriedades não são verificadas.

**Retorna:** A lista dos itens que casam.

### from_id(id)

Esta é uma função feita para a game engine devolver um valor com um id específico.

Como os nomes de objeto nem sempre são únicos, o id de um objeto pode ser usado para pegá-lo no EXP_ValueList.

Exemplo:

```python

myObID=id(gameObject)
ob= scene.objects.from_id(myObID)
```

Em que `myObID` é um int ou long vindo da função id.

A vantagem é que dá para guardar o id em lugares onde não dá para guardar um gameObject.

:::caution
O id vem de um endereço de memória e muda a cada vez que a game engine inicia.
:::

:::caution
O id não pode ser guardado como inteiro em propriedades de game object, porque elas têm um intervalo limitado em que o id pode não caber. Em vez disso, guarde o id como propriedade de jogo string e converta de volta para inteiro para usar no from_id.
:::

