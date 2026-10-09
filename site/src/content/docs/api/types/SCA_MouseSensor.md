---
title: "SCA_MouseSensor"
description: "Referência da classe Range.types.SCA_MouseSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Mouse Sensor logic brick.

### position

current [x, y] coordinates of the mouse, in frame coordinates (pixels).

**Tipo:** [integer, interger]

### mode

sensor mode.

**Tipo:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_WHEELUP(4) * KX_MOUSESENSORMODE_WHEELDOWN(5) * KX_MOUSESENSORMODE_MOVEMENT(6)

### getButtonStatus(button)

Get the mouse button status.

- **`button`**: The code that represents the key you want to get the state of, use one of `these constants`
  - tipo: int

**Retorna:** The state of the given key, can be one of `these constants`

**Tipo do retorno:** int

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### holdTime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

