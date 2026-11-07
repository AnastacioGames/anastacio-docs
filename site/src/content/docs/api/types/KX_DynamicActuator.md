---
title: "KX_DynamicActuator"
description: "Referência da classe Range.types.KX_DynamicActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Dynamic.

```python
# Muda a massa do objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_SET_MASS
act.mass = 5.0
cont.activate(act)
```

```python
# Desliga a física do objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_DISABLE_DYNAMICS
cont.activate(act)
```

### mode

**Tipo:** integer

o tipo de operação do atuador, 0-4

* KX_DYN_RESTORE_DYNAMICS(0)
* KX_DYN_DISABLE_DYNAMICS(1)
* KX_DYN_ENABLE_RIGID_BODY(2)
* KX_DYN_DISABLE_RIGID_BODY(3)
* KX_DYN_SET_MASS(4)

### mass

o valor de massa para a operação KX_DYN_SET_MASS.

**Tipo:** float

