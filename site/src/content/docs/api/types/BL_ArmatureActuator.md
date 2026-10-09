---
title: "BL_ArmatureActuator"
description: "Referência da classe Range.types.BL_ArmatureActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Os atuadores Armature mudam a condição das constraints em armatures.

### type

O tipo de ação que o atuador executa quando está ativo.

Pode ser uma `destas constantes`

**Tipo:** integer

### constraint

O objeto de constraint que este atuador controla.

**Tipo:** `BL_ArmatureConstraint`

### target

O objeto que este atuador define como alvo principal da constraint que controla.

**Tipo:** `KX_GameObject`

### subtarget

O objeto que este atuador define como alvo secundário da constraint que controla.

**Tipo:** `KX_GameObject`.

:::note
Por enquanto, o único alvo secundário é o pole target das constraints IK.
:::

### weight

O peso que este atuador define na constraint que controla.

**Tipo:** float.

:::note
Por enquanto só a constraint IK tem peso. Deve ser um valor entre 0 e 1.
:::

:::note
Peso 0 desliga a constraint, mas continua atualizando os valores dela em tempo de execução (veja `BL_ArmatureConstraint`)
:::

### influence

A influência que este atuador define na constraint que controla.

**Tipo:** float.

