---
title: "BL_ArmatureBone"
description: "Referência da classe Range.types.BL_ArmatureBone"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Proxy para a estrutura de bone do Blender. Todos os campos são somente leitura e seguem os nomes do RNA. Todos os atributos de espaço correspondem à rest pose.

### name

nome do bone.

**Tipo:** string

### connected

true quando a cabeça do bone está presa à cauda do pai.

**Tipo:** boolean

### hinge

true quando o bone não herda rotação nem escala do bone pai.

**Tipo:** boolean

### inherit_scale

true quando o bone herda a escala do bone pai.

**Tipo:** boolean

### bbone_segments

número de segmentos de B-bone.

**Tipo:** integer

### roll

rotação do bone em torno do eixo cabeça-cauda.

**Tipo:** float

### head

posição da cabeça do bone no espaço do bone pai.

**Tipo:** vector [x, y, z]

### tail

posição da cabeça do bone no espaço do bone pai.

**Tipo:** vector [x, y, z]

### length

comprimento do bone.

**Tipo:** float

### arm_head

posição da cabeça do bone no espaço da armature.

**Tipo:** vector [x, y, z]

### arm_tail

posição da cauda do bone no espaço da armature.

**Tipo:** vector [x, y, z]

### arm_mat

matriz da cabeça do bone no espaço da armature.

**Tipo:** matrix [4][4]

:::note
Esta matriz não tem parte de escala.
:::

### bone_mat

matriz de rotação do bone no espaço do bone pai.

**Tipo:** matrix [3][3]

### parent

bone pai, ou None para o bone raiz.

**Tipo:** `BL_ArmatureBone`

### children

lista dos filhos do bone.

**Tipo:** list of `BL_ArmatureBone`

