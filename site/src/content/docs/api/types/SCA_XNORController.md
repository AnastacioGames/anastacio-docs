---
title: "SCA_XNORController"
description: "Referência da classe Range.types.SCA_XNORController"
---

Classe base: [`SCA_IController`](../sca_icontroller/)



Um controlador XNOR ativa quando todos os sensores ligados estão iguais (ativos ou inativos).

Não há métodos Python especiais para este controlador.

```python
# XNOR liga os atuadores, a não ser que exatamente um sensor esteja positivo.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) != 1)
```



