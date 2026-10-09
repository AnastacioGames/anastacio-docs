---
title: "KX_ParentActuator"
description: "Referência da classe Range.types.KX_ParentActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



O atuador parent define ou remove o objeto pai de um objeto.

### object

o objeto que este atuador define como pai.

**Tipo:** `KX_GameObject` or None

### mode

O modo deste atuador.

**Tipo:** integer from 0 to 1.

### compound

Se a forma do objeto deve ser adicionada à forma composta do pai ao fazer o parent.

Só tem efeito se o pai já for uma forma composta.

**Tipo:** boolean

### ghost

Se o objeto deve virar ghost ao fazer o parent. Só tem efeito se a forma não for adicionada à forma composta do pai.

**Tipo:** boolean

