---
title: "KX_LightningActuator"
description: "Referência da classe Range.types.KX_LightningActuator"
---

Classe `Range.types.KX_LightningActuator`.

```python
# Dispara um clarão com o raio visível.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Lightning"]

act.bolt = True
cont.activate(act)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### bolt

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga o raio visível do relâmpago, além do clarão.

