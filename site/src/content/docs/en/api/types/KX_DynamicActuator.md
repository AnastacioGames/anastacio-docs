---
title: "KX_DynamicActuator"
description: "Range.types.KX_DynamicActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Dynamic Actuator.

### mode

**Type:** integer

the type of operation of the actuator, 0-4

* KX_DYN_RESTORE_DYNAMICS(0)
* KX_DYN_DISABLE_DYNAMICS(1)
* KX_DYN_ENABLE_RIGID_BODY(2)
* KX_DYN_DISABLE_RIGID_BODY(3)
* KX_DYN_SET_MASS(4)

### mass

the mass value for the KX_DYN_SET_MASS operation.

**Type:** float

