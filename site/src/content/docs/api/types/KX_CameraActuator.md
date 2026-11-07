---
title: "KX_CameraActuator"
description: "Referência da classe Range.types.KX_CameraActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Aplica mudanças a uma câmera.

```python
# Faz a câmera seguir outro objeto, a uma distância definida.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Camera"]

act.object = Range.logic.getCurrentScene().objects["Car"]
act.min = 4.0
act.max = 8.0
act.height = 2.5
act.damping = 0.1
cont.activate(act)
```

### damping

força do movimento de seguir da câmera.

**Tipo:** float

### axis

O eixo da câmera: (0, 1, 2) para `XYZ` positivo, (3, 4, 5) para `XYZ` negativo.

**Tipo:** int

### min

distância mínima até o objeto alvo mantida pelo atuador.

**Tipo:** float

### max

distância máxima a manter do objeto alvo.

**Tipo:** float

### height

altura a manter acima do objeto alvo.

**Tipo:** float

### object

o objeto que este atuador segue.

**Tipo:** `KX_GameObject` or None

