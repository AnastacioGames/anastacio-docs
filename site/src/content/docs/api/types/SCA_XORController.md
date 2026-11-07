---
title: "SCA_XORController"
description: "Referência da classe Range.types.SCA_XORController"
---

Classe base: [`SCA_IController`](../sca_icontroller/)



Um controlador XOR ativa quando as entradas estão misturadas, mas não quando todas estão ligadas ou desligadas.

Não há métodos Python especiais para este controlador.

```python
# XOR liga os atuadores quando exatamente um sensor está positivo.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) == 1)
```



