---
title: "BL_ArmatureChannel"
description: "Referência da classe Range.types.BL_ArmatureChannel"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Proxy para um canal de pose da armature. Permite ler e definir a pose da armature. Os atributos são iguais aos do RNA, mas a maioria é somente leitura.

### name

nome do canal (= nome do bone), somente leitura.

**Tipo:** string

### bone

devolve o objeto bone correspondente a este canal de pose, somente leitura.

**Tipo:** `BL_ArmatureBone`

### parent

devolve o canal pai, None se for o canal raiz, somente leitura.

**Tipo:** `BL_ArmatureChannel`

### has_ik

true se o bone faz parte de uma cadeia IK ativa, somente leitura. Esta flag não é ligada quando uma constraint IK existe mas não está ativa (por exemplo, sem informação de alvo).

**Tipo:** boolean

### ik_dof_x

true se o bone gira livre no eixo X, somente leitura.

**Tipo:** boolean

### ik_dof_y

true se o bone gira livre no eixo Y, somente leitura.

**Tipo:** boolean

### ik_dof_z

true se o bone gira livre no eixo Z, somente leitura.

**Tipo:** boolean

### ik_limit_x

true se há limite na rotação X, somente leitura.

**Tipo:** boolean

### ik_limit_y

true se há limite na rotação Y, somente leitura.

**Tipo:** boolean

### ik_limit_z

true se há limite na rotação Z, somente leitura.

**Tipo:** boolean

### ik_rot_control

true se a rotação do canal deve ser aplicada como constraint IK, somente leitura.

**Tipo:** boolean

### ik_lin_control

true se o tamanho do canal deve ser aplicado como constraint IK, somente leitura.

**Tipo:** boolean

### location

deslocamento da cabeça do bone no espaço local da armature, leitura e escrita.

**Tipo:** vector [X, Y, Z].

:::note
Só dá para mover um bone se ele não estiver conectado ao pai. Uma action tocando na armature pode mudar o valor. Uma cadeia IK não atualiza este valor; veja joint_rotation.
:::

:::note
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`).
:::

### scale

escala do bone relativa ao pai, leitura e escrita.

**Tipo:** vector [sizeX, sizeY, sizeZ].

:::note
Uma action tocando na armature pode mudar o valor. Uma cadeia IK não atualiza este valor; veja joint_rotation.
:::

:::note
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`)
:::

### rotation_quaternion

rotação do bone relativa ao pai, como quaternion, leitura e escrita.

**Tipo:** vector [qr, qi, qj, qk].

:::note
Este campo só é usado se rotation_mode for 0. Uma action tocando na armature pode mudar o valor. Uma cadeia IK não atualiza este valor; veja joint_rotation.
:::

:::note
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`)
:::

### rotation_euler

rotação do bone relativa ao pai, como ângulos de Euler, leitura e escrita.

**Tipo:** vector [X, Y, Z].

:::note
Este campo só é usado se rotation_mode for > 0. Passe os ângulos sempre na ordem [X, Y, Z]; a ordem em que são aplicados ao bone depende de rotation_mode. Uma action tocando na armature pode mudar este campo. Uma cadeia IK não atualiza este valor; veja joint_rotation.
:::

:::note
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`)
:::

### rotation_mode

Método de atualização da rotação do bone, leitura e escrita.

**Tipo:** integer (one of `these constants`)

### channel_matrix

matriz da pose no espaço do bone (deformação do bone por action, constraint etc.), somente leitura. Este campo é atualizado depois do render e representa a pose atual.

**Tipo:** matrix [4][4]

### pose_matrix

matriz da pose no espaço da armature, somente leitura. Este campo é atualizado depois do render e representa a pose atual.

**Tipo:** matrix [4][4]

### pose_head

posição da cabeça do bone no espaço da armature, somente leitura.

**Tipo:** vector [x, y, z]

### pose_tail

posição da cauda do bone no espaço da armature, somente leitura.

**Tipo:** vector [x, y, z]

### ik_min_x

valor mínimo da rotação X em graus (<= 0) quando a rotação X é limitada (veja ik_limit_x), somente leitura.

**Tipo:** float

### ik_max_x

valor máximo da rotação X em graus (>= 0) quando a rotação X é limitada (veja ik_limit_x), somente leitura.

**Tipo:** float

### ik_min_y

valor mínimo da rotação Y em graus (<= 0) quando a rotação Y é limitada (veja ik_limit_y), somente leitura.

**Tipo:** float

### ik_max_y

valor máximo da rotação Y em graus (>= 0) quando a rotação Y é limitada (veja ik_limit_y), somente leitura.

**Tipo:** float

### ik_min_z

valor mínimo da rotação Z em graus (<= 0) quando a rotação Z é limitada (veja ik_limit_z), somente leitura.

**Tipo:** float

### ik_max_z

valor máximo da rotação Z em graus (>= 0) quando a rotação Z é limitada (veja ik_limit_z), somente leitura.

**Tipo:** float

### ik_stiffness_x

rigidez de rotação do bone no eixo X, somente leitura.

**Tipo:** float between 0 and 1

### ik_stiffness_y

rigidez de rotação do bone no eixo Y, somente leitura.

**Tipo:** float between 0 and 1

### ik_stiffness_z

rigidez de rotação do bone no eixo Z, somente leitura.

**Tipo:** float between 0 and 1

### ik_stretch

proporção de mudança de escala permitida; 0 = o bone não muda de tamanho, somente leitura.

**Tipo:** float

### ik_rot_weight

peso da constraint de rotação quando ik_rot_control está ligado, leitura e escrita.

**Tipo:** float between 0 and 1

### ik_lin_weight

peso da constraint de tamanho quando ik_lin_control está ligado, leitura e escrita.

**Tipo:** float between 0 and 1

### joint_rotation

Controla a rotação do bone em termos de ângulo de junta (para aplicações de robótica), leitura e escrita.

Ao escrever neste atributo, você passa um vetor [x, y, z] e um conjunto adequado de ângulos de Euler ou quaternion é calculado conforme rotation_mode.

Ao ler este atributo, a matriz da pose atual é convertida num vetor [x, y, z] que representa os ângulos da junta.

O valor e o significado de x, y e z dependem dos atributos ik_dof_x/ik_dof_y/ik_dof_z:

* Junta de 1 grau de liberdade X, Y ou Z: o valor x, y ou z correspondente é usado como ângulo da junta em radianos
* Junta de 2 graus de liberdade X+Y ou Z+Y: tratada como 2 juntas de 1 grau seguidas, primeiro X ou Z, depois Y. O valor x ou z é usado como ângulo da junta em radianos no eixo X ou Z, seguido de uma rotação de y radianos no novo eixo Y.
* Junta de 2 graus de liberdade X+Z: tratada como uma junta de 2 graus com eixo de rotação no plano X/Z. Os valores x e z são usados como coordenadas do vetor de rotação no plano X/Z.
* Junta de 3 graus de liberdade X+Y+Z: tratada como uma junta de revolução. O vetor [x, y, z] representa o vetor de rotação equivalente que leva a junta da rest pose à nova pose.

**Tipo:** vector [x, y, z]

:::note
O bone precisa fazer parte de uma cadeia IK para você definir os atributos ik_dof_x/ik_dof_y/ik_dof_z pela UI, mas isso atrapalha este atributo, porque o solver de IK sobrescreve a pose. Dá para manter o controle da armature criando uma constraint IK sem terminá-la (por exemplo, sem definir alvo): o solver de IK não roda, mas o painel IK aparece na UI para cada bone da cadeia.
:::

:::note
[0, 0, 0] sempre corresponde à rest pose.
:::

:::note
É preciso pedir a atualização da pose da armature e esperar o próximo frame gráfico para ver o efeito deste atributo (veja `BL_ArmatureObject.update`).
:::

:::note
Depois de definir este atributo, dá para ler o resultado do cálculo nos atributos rotation ou euler_rotation.
:::

