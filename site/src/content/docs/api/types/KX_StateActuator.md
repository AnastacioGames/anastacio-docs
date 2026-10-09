---
title: "KX_StateActuator"
description: "Referência da classe Range.types.KX_StateActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



State actuator changes the state mask of parent object.

### operation

Type of bit operation to be applied on object state mask.

You can use one of `these constants`

**Tipo:** integer

### mask

Value that defines the bits that will be modified by the operation.

The bits that are 1 in the mask will be updated in the object state.

The bits that are 0 are will be left unmodified expect for the Copy operation which copies the mask to the object state.

**Tipo:** integer

