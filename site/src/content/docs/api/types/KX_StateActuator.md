---
title: "KX_StateActuator"
description: "Referência da classe Range.types.KX_StateActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



O atuador State muda a máscara de estado do objeto pai.

```python
# Liga o estado 2 do objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["State"]

act.operation = Range.logic.KX_STATE_OP_SET
act.mask = Range.logic.KX_STATE2
cont.activate(act)
```

### operation

Tipo de operação de bits aplicada à máscara de estado do objeto.

Você pode usar uma `destas constantes`

**Tipo:** integer

### mask

Valor que define os bits que serão modificados pela operação.

Os bits que valem 1 na máscara são atualizados no estado do objeto.

Os bits que valem 0 ficam sem mudança, exceto na operação Copy, que copia a máscara para o estado do objeto.

**Tipo:** integer

