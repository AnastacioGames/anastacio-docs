---
title: "SCA_PropertyActuator"
description: "Referência da classe Range.types.SCA_PropertyActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Property

```python
# Troca a propriedade em que este atuador escreve.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Property"]

act.propName = "score"
act.value = "score + 10"
cont.activate(act)
```

### propName

a propriedade sobre a qual operar.

**Tipo:** string

### value

o valor com que o atuador opera.

**Tipo:** string

### mode

TODO - adicionar as constantes ao dicionário de game logic!.

**Tipo:** integer

