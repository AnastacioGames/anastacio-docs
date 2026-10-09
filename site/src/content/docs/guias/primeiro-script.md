---
title: Primeiro script
description: Um script Python que move um objeto quando você aperta uma tecla.
---

1. Selecione um objeto na cena e adicione um sensor **Always** (com *True Level Triggering* ligado) ligado a um controlador **Python**.
2. Crie um texto chamado `mover.py` no editor de texto e escolha-o no controlador.
3. Cole o código e aperte **P** para jogar.

```python
import Range
from Range import logic, events

cont = logic.getCurrentController()
own = cont.owner
teclado = logic.keyboard

if teclado.inputs[events.WKEY].active:
    own.applyMovement((0, 0.1, 0), True)   # anda para a frente
if teclado.inputs[events.SKEY].active:
    own.applyMovement((0, -0.1, 0), True)
```

- `logic.getCurrentController()` devolve o controlador que está rodando o script.
- `own` é o objeto dono do controlador, um [`KX_GameObject`](../../api/types/kx_gameobject/).
- `applyMovement(vetor, local)` move o objeto; `True` usa os eixos do próprio objeto.
