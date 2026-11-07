---
title: "SCA_ANDController"
description: "Referência da classe Range.types.SCA_ANDController"
---

Classe base: [`SCA_IController`](../sca_icontroller/)



Um controlador AND só ativa quando todos os sensores ligados estão ativos.

Não há métodos Python especiais para este controlador.

```python
# Com um controlador AND, os atuadores rodam quando todos os sensores estão positivos. Este script mostra a mesma regra.
import Range

cont = Range.logic.getCurrentController()

if all(sensor.positive for sensor in cont.sensors):
    print("All sensors are on")
```



