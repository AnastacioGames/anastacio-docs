---
title: "SCA_IController"
description: "Referência da classe Range.types.SCA_IController"
---

Classe base: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Classe base de todos os logic bricks de controlador.

### state

A máscara de bits de estado do controlador. Pode ser usada com o estado do GameObject para testar se o controlador está ativo.

**Tipo:** int bitmask

### sensors

Uma lista dos sensores ligados a este controlador.

**Tipo:** sequence supporting index/string lookups and iteration.

:::note
Os sensores não pertencem necessariamente ao mesmo objeto.
:::

:::note
Quando objetos são instanciados em dupligroups, as ligações com objetos de fora do dupligroup podem se perder.
:::

### actuators

Uma lista dos atuadores ligados a este controlador.

**Tipo:** sequence supporting index/string lookups and iteration.

:::note
Os sensores não pertencem necessariamente ao mesmo objeto.
:::

:::note
Quando objetos são instanciados em dupligroups, as ligações com objetos de fora do dupligroup podem se perder.
:::

### useHighPriority

Quando ligado, o controlador sempre roda antes de todos os outros controladores que não têm isto ligado.

**Tipo:** boolen

:::note
A ordem de execução entre controladores de alta prioridade não é garantida.
:::

