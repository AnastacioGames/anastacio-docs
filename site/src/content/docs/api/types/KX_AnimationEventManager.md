---
title: "KX_AnimationEventManager"
description: "Referência da classe Range.types.KX_AnimationEventManager"
---

:::tip[Veja também]
[`KX_AnimationEvent`](../../types/kx_animationevent/), [`SCA_AnimationEventSensor`](../../types/sca_animationeventsensor/)
:::

Classe `Range.types.KX_AnimationEventManager`.

```python
# Toca um som de passo nos quadros marcados na animação.
import Range

cont = Range.logic.getCurrentController()
own = cont.owner

fired = sum(event.getFireCount() for event in own.animationEventManager.events)

if fired != own.get("steps", 0):
    own["steps"] = fired
    cont.activate("StepSound")
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### events

 <small>atributo · só leitura</small>

Lista dos eventos de animação (`KX_AnimationEvent`) do objeto.

