---
title: "BL_ArmatureObject"
description: "Referência da classe Range.types.BL_ArmatureObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)

:::tip[Veja também]
[`BL_ArmatureChannel`](../../types/bl_armaturechannel/), [`BL_ArmatureBone`](../../types/bl_armaturebone/), [`BL_ArmatureConstraint`](../../types/bl_armatureconstraint/), [`BL_ActionActuator`](../../types/bl_actionactuator/)
:::



Um objeto armature.

### constraints

A lista de constraints de armature definidas nesta armature. Os elementos podem ser acessados por índice ou por string. O formato da chave em string é '<bone_name>:<constraint_name>'.

**Tipo:** list of `BL_ArmatureConstraint`

### channels

A lista de canais da armature. Os elementos podem ser acessados por índice ou pelo nome do bone.

**Tipo:** list of `BL_ArmatureChannel`

### update()

Garante que a armature será atualizada no próximo frame gráfico.

Isto não é necessário se um KX_ArmatureActuator no modo run estiver ativo ou se uma action estiver tocando. Use esta função nos outros casos. Ela precisa ser chamada a cada frame para garantir que a armature seja atualizada continuamente.

### draw()

Desenha linhas que representam a armature, para vê-la em tempo real.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### clearBoneRotationOffset(bone=None)

 <small>método</small>

Remove a rotação extra de um osso, ou de todos quando `bone` é omitido.

### setBoneRotationOffset(bone, rotation)

 <small>método</small>

Rotação extra num osso por cima das actions que estão tocando, no espaço local do osso. `rotation`: euler XYZ (3 valores, radianos) ou quaternion (4 valores, w x y z). Fica até `clearBoneRotationOffset()`.

