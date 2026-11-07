---
title: "SCA_RandomSensor"
description: "Referência da classe Range.types.SCA_RandomSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Este sensor ativa aleatoriamente.

```python
# Usa uma semente fixa para repetir a mesma sequência.
import Range

sensor = Range.logic.getCurrentController().sensors["Random"]

sensor.seed = 1234
print(sensor.lastDraw)
```

### lastDraw

A semente do gerador de números aleatórios.

**Tipo:** integer

### seed

A semente do gerador de números aleatórios.

**Tipo:** integer

