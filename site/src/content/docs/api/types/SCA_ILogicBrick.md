---
title: "SCA_ILogicBrick"
description: "Referência da classe Range.types.SCA_ILogicBrick"
---

Classe base: [`EXP_Value`](../exp_value/)



Classe base de todos os logic bricks.

### executePriority

Define a ordem em que os controladores são avaliados e os atuadores são ativados (prioridade menor roda primeiro).

**Tipo:** executePriority: int

### owner

O game object ao qual este logic brick está ligado (somente leitura).

**Tipo:** `KX_GameObject` or None in exceptional cases.

### name

O nome deste logic brick (somente leitura).

**Tipo:** string

