---
title: "KX_NearSensor"
description: "Referência da classe Range.types.KX_NearSensor"
---

Classe base: [`KX_CollisionSensor`](../kx_collisionsensor/)



O sensor near é uma forma especializada de sensor de toque.

```python
# Abre a porta quando alguém chega perto e só fecha mais longe.
import Range

sensor = Range.logic.getCurrentController().sensors["Near"]

sensor.distance = 3.0
sensor.resetDistance = 5.0

if sensor.positive:
    print(sensor.hitObject.name, "is near")
```

### distance

O sensor near ativa quando um objeto está dentro desta distância.

**Tipo:** float

### resetDistance

O sensor near desativa quando o objeto passa desta distância.

**Tipo:** float

