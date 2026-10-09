---
title: "BL_ArmatureObject"
description: "Referência da classe Range.types.BL_ArmatureObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



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

