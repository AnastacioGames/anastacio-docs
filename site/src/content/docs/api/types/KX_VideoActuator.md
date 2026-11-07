---
title: "KX_VideoActuator"
description: "Referência da classe Range.types.KX_VideoActuator"
---

Classe `Range.types.KX_VideoActuator`.

```python
# Pausa o vídeo de outro objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Video"]

act.object = "Screen"
act.mode = 1
cont.activate(act)
```

```python
# Avança dez segundos.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Video"]

act.mode = 5
act.seconds = 10.0
act.useRelative = True
cont.activate(act)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### mode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Ação sobre o Video Player: `0` Play, `1` Pause, `2` Toggle, `3` Stop, `4` Restart, `5` Seek.

### object

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Objeto com o Video Player que o actuator controla (`KX_GameObject`, nome ou `None`).

### seconds

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Posição em segundos usada pelo modo Seek.

### useRelative

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

No modo Seek, se `True`, `seconds` é somado à posição atual em vez de ser absoluto.

