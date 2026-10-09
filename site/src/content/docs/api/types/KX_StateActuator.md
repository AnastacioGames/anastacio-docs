---
title: "KX_StateActuator"
description: "Referência da classe Range.types.KX_StateActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



O atuador State muda a máscara de estado do objeto pai.

### operation

Tipo de operação de bits aplicada à máscara de estado do objeto.

Você pode usar uma `destas constantes`

**Tipo:** integer

### mask

Valor que define os bits que serão modificados pela operação.

Os bits que valem 1 na máscara são atualizados no estado do objeto.

Os bits que valem 0 ficam sem mudança, exceto na operação Copy, que copia a máscara para o estado do objeto.

**Tipo:** integer

