---
title: "KX_NetworkMessageActuator"
description: "Referência da classe Range.types.KX_NetworkMessageActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Message

```python
# Envia uma mensagem para objetos da cena.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Message"]

act.subject = "door_open"
act.body = "north"
act.usePropBody = False
cont.activate(act)
```

### propName

As mensagens só são enviadas para objetos com o nome de propriedade indicado.

**Tipo:** string

### subject

O campo assunto da mensagem.

**Tipo:** string

### body

O corpo da mensagem.

**Tipo:** string

### usePropBody

Envia uma propriedade em vez de uma mensagem com corpo normal.

**Tipo:** boolean

