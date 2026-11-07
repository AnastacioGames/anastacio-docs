---
title: "SCA_AnimationEventSensor"
description: "Referência da classe Range.types.SCA_AnimationEventSensor"
---

Classe `Range.types.SCA_AnimationEventSensor`.

```python
# Dispara nos quadros marcados na animação.
import Range

cont = Range.logic.getCurrentController()

if cont.sensors["AnimationEvent"].positive:
    print("Step")
```



