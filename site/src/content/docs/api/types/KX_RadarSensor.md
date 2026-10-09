---
title: "KX_RadarSensor"
description: "Referência da classe Range.types.KX_RadarSensor"
---

Classe base: [`KX_NearSensor`](../kx_nearsensor/)



O sensor radar é um sensor near com um objeto sensor em forma de cone.

### coneOrigin

A origem do cone usado no teste. A origem fica no meio do cone (somente leitura).

**Tipo:** `mathutils.Vector`

### coneTarget

O centro da face de baixo do cone usado no teste (somente leitura).

**Tipo:** `mathutils.Vector`

### distance

A altura do cone usado no teste.

**Tipo:** float

### angle

O ângulo do cone (em graus) usado no teste.

**Tipo:** float

### axis

O eixo em que o cone do radar é lançado.

**Tipo:** integer from 0 to 5

KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z, KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z

