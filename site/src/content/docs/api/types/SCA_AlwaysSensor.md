---
title: "SCA_AlwaysSensor"
description: "Referência da classe Range.types.SCA_AlwaysSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Este sensor está sempre ativo.

```python
# Roda um script uma vez só, quando o objeto começa.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Always"]

sensor.usePosPulseMode = False

if sensor.positive:
    cont.owner["life"] = 100
```

```python
# Repete a cada 30 quadros de lógica.
import Range

sensor = Range.logic.getCurrentController().sensors["Always"]

sensor.usePosPulseMode = True
sensor.skippedTicks = 30
```



