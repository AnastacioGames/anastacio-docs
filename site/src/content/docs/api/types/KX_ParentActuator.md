---
title: "KX_ParentActuator"
description: "Referência da classe Range.types.KX_ParentActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



The parent actuator can set or remove an objects parent object.

### object

the object this actuator sets the parent too.

**Tipo:** `KX_GameObject` or None

### mode

The mode of this actuator.

**Tipo:** integer from 0 to 1.

### compound

Whether the object shape should be added to the parent compound shape when parenting.

Effective only if the parent is already a compound shape.

**Tipo:** boolean

### ghost

Whether the object should be made ghost when parenting Effective only if the shape is not added to the parent compound shape.

**Tipo:** boolean

