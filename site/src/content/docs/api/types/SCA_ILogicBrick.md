---
title: "SCA_ILogicBrick"
description: "Referência da classe Range.types.SCA_ILogicBrick"
---

Classe base: [`EXP_Value`](../exp_value/)



Base class for all logic bricks.

### executePriority

This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first).

**Tipo:** executePriority: int

### owner

The game object this logic brick is attached to (read-only).

**Tipo:** `KX_GameObject` or None in exceptional cases.

### name

The name of this logic brick (read-only).

**Tipo:** string

