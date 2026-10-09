---
title: "KX_TrackToActuator"
description: "Referência da classe Range.types.KX_TrackToActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Edit Object no modo Track To.

:::caution
Atuadores Track To são ignorados se, no início do jogo, o objeto a seguir for inválido.

Isto gera um aviso no console:

```none

GameObject 'Name' no object in EditObjectActuator 'ActuatorName'
```
:::

### object

o objeto que este atuador segue.

**Tipo:** `KX_GameObject` or None

### time

o tempo, em frames, de atraso do movimento de seguir.

**Tipo:** integer

### use3D

o movimento de seguir usa 3D.

**Tipo:** boolean

### upAxis

O eixo que aponta para cima.

**Tipo:** integer from 0 to 2

* KX_TRACK_UPAXIS_POS_X
* KX_TRACK_UPAXIS_POS_Y
* KX_TRACK_UPAXIS_POS_Z

### trackAxis

O eixo que aponta para o objeto alvo.

**Tipo:** integer from 0 to 5

* KX_TRACK_TRAXIS_POS_X
* KX_TRACK_TRAXIS_POS_Y
* KX_TRACK_TRAXIS_POS_Z
* KX_TRACK_TRAXIS_NEG_X
* KX_TRACK_TRAXIS_NEG_Y
* KX_TRACK_TRAXIS_NEG_Z

