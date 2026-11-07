---
title: "SCA_NANDController"
description: "Referência da classe Range.types.SCA_NANDController"
---

Classe base: [`SCA_IController`](../sca_icontroller/)



Um controlador NAND ativa quando nem todos os sensores ligados estão ativos.

Não há métodos Python especiais para este controlador.

```python
# NAND liga os atuadores, a não ser que todos os sensores estejam positivos.
import Range

cont = Range.logic.getCurrentController()

print(not all(sensor.positive for sensor in cont.sensors))
```



