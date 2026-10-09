---
title: "SCA_VibrationActuator"
description: "Referência da classe Range.types.SCA_VibrationActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Vibration.

### joyindex

Índice do joystick.

**Tipo:** integer (0 to 7)

### strengthLeft

Força do motor de baixa frequência do joystick (em geral fica à esquerda).

**Tipo:** float (0.0 to 1.0)

### strengthRight

Força do motor de alta frequência do joystick (em geral fica à direita).

**Tipo:** float (0.0 to 1.0)

### duration

Duração da vibração em milissegundos.

**Tipo:** integer (0 to infinite)

### isVibrating

Verifica o status da vibração do joystick

**Tipo:** bool (true vibrating and false stopped)

### hasVibration

Verifica se o joystick suporta vibração

**Tipo:** bool (true supported and false not supported)

### startVibration()

Começa a vibração.

**Retorna:** None

### stopVibration()

Para a vibração.

**Retorna:** None

