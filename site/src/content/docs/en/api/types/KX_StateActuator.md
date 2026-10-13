---
title: "KX_StateActuator"
description: "Range.types.KX_StateActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



State actuator changes the state mask of parent object.

### operation

Type of bit operation to be applied on object state mask.

You can use one of `these constants`

**Type:** integer

### mask

Value that defines the bits that will be modified by the operation.

The bits that are 1 in the mask will be updated in the object state.

The bits that are 0 are will be left unmodified expect for the Copy operation which copies the mask to the object state.

**Type:** integer

