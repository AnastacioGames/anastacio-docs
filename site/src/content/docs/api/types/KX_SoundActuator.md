---
title: "KX_SoundActuator"
description: "Referência da classe Range.types.KX_SoundActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Sound.

`startSound`, `pauseSound` e `stopSound` não exigem que o atuador esteja ativo: agem na hora, desde que o atuador tenha sido ativado pelo menos uma vez.

### volume

O volume (ganho) do som.

**Tipo:** float

### time

A posição atual no stream de áudio (em segundos).

**Tipo:** float

### pitch

O pitch do som.

**Tipo:** float

### mode

O modo de operação do atuador. Pode ser uma `destas constantes`

**Tipo:** integer

### sound

O som que o atuador deve tocar.

**Tipo:** Audaspace factory

### is3D

Se o atuador usa som 3D ou não (somente leitura)

**Tipo:** boolean

### volume_maximum

O ganho máximo do som, não importa quão perto ele esteja.

**Tipo:** float

### volume_minimum

O ganho mínimo do som, não importa quão longe ele esteja.

**Tipo:** float

### distance_reference

A distância em que o som tem ganho 1.0.

**Tipo:** float

### distance_maximum

A distância máxima em que dá para ouvir o som.

**Tipo:** float

### attenuation

O fator de influência no volume conforme a distância.

**Tipo:** float

### cone_angle_inner

O ângulo do cone interno.

**Tipo:** float

### cone_angle_outer

O ângulo do cone externo.

**Tipo:** float

### cone_volume_outer

O ganho fora do cone externo (o ganho dentro do cone externo é interpolado entre este valor e o ganho normal do cone interno).

**Tipo:** float

### startSound()

Começa o som.

**Retorna:** None

### pauseSound()

Pausa o som.

**Retorna:** None

### stopSound()

Para o som.

**Retorna:** None

