---
title: "SCA_MouseSensor"
description: "Referência da classe Range.types.SCA_MouseSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Logic brick do sensor de mouse.

### position

As coordenadas [x, y] atuais do mouse, em coordenadas do frame (pixels).

**Tipo:** [integer, interger]

### mode

O modo do sensor.

**Tipo:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_WHEELUP(4) * KX_MOUSESENSORMODE_WHEELDOWN(5) * KX_MOUSESENSORMODE_MOVEMENT(6)

### getButtonStatus(button)

Lê o estado de um botão do mouse.

- **`button`**: O código do botão cujo estado você quer ler; use uma `destas constantes`
  - tipo: int

**Retorna:** O estado do botão, que pode ser uma `destas constantes`

**Tipo do retorno:** int

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### holdTime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

