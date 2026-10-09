---
title: "BL_ArmatureConstraint"
description: "Referência da classe Range.types.BL_ArmatureConstraint"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Proxy para uma constraint de armature. Permite mudar a constraint em tempo real. Obtido por `BL_ArmatureObject`.constraints.

:::note
Nem todas as constraints de armature são suportadas na GE.
:::

### type

Tipo da constraint (somente leitura).

Use uma `destas constantes`.

**Tipo:** integer, one of CONSTRAINT_TYPE_* constants

### name

Nome da constraint, montado como <bone_name>:<constraint_name>, na lista constraints.

**Tipo:** string

Este nome também é a chave de índice em `BL_ArmatureObject`.

### enforce

fração do efeito da constraint que é aplicada. Entre 0 e 1.

**Tipo:** float

### headtail

Posição do alvo entre a cabeça e a cauda do bone alvo: 0=cabeça, 1=cauda.

**Tipo:** float.

:::note
Só é usado se o alvo for um bone (ou seja, se o objeto alvo for uma armature).
:::

### lin_error

erro linear da constraint em tempo de execução (em unidades do Blender) no frame atual.

É um valor de tempo de execução, atualizado a cada frame pelo solver de IK. Só existe em constraints IK com o solver iTaSC.

**Tipo:** float

### rot_error

Erro de rotação da constraint em tempo de execução (em radianos) no frame atual.

**Tipo:** float.

É um valor de tempo de execução, atualizado a cada frame pelo solver de IK. Só existe em constraints IK com o solver iTaSC.

Só é definido se a constraint tiver parte de rotação, por exemplo, uma constraint IK CopyPose+Rotation.

### target

Objeto alvo principal da constraint. A posição deste objeto na GE é usada como alvo da constraint.

**Tipo:** `KX_GameObject`.

### subtarget

Objeto alvo secundário da constraint. A posição deste objeto na GE é usada como alvo secundário da constraint.

**Tipo:** `KX_GameObject`.

Por enquanto isto só é usado como pole target em constraints IK.

### active

True se a constraint está ativa.

**Tipo:** boolean

:::note
Uma constraint inativa não atualiza lin_error nem rot_error.
:::

### ik_weight

Peso da constraint IK, entre 0 e 1.

Só definido para constraints IK.

**Tipo:** float

### ik_type

Tipo de constraint IK (somente leitura).

Use uma `destas constantes`.

**Tipo:** integer.

### ik_flag

Combinação das flags de opção da constraint IK (somente leitura).

Use uma `destas constantes`.

**Tipo:** integer

### ik_dist

Distância que a constraint tenta manter do alvo; só usada quando ik_type=CONSTRAINT_IK_DISTANCE.

**Tipo:** float

### ik_mode

Use uma `destas constantes`.

Modo adicional da constraint IK. Por enquanto só é usado na constraint Distance:

**Tipo:** integer

