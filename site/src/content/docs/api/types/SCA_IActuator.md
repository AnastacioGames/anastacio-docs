---
title: "SCA_IActuator"
description: "Referência da classe Range.types.SCA_IActuator"
---

Classe base: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Classe base de todos os logic bricks de atuador.

```python
# Todos os atuadores são ligados e desligados pelo controlador.
import Range

cont = Range.logic.getCurrentController()

for act in cont.actuators:
    if cont.sensors[0].positive:
        cont.activate(act)
    else:
        cont.deactivate(act)
```



