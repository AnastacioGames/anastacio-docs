---
title: "KX_ConstraintWrapper"
description: "Referência da classe Range.types.KX_ConstraintWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



KX_ConstraintWrapper

### getConstraintId(val)

Devolve o ID da constraint

**Retorna:** o ID da constraint

**Tipo do retorno:** integer

### setParam(axis, value0, value1)

Define os limites da constraint

- **`axis`**:
  - tipo: integer

:::note
* Lowerlimit == Upperlimit -> o eixo fica travado
* Lowerlimit > Upperlimit -> o eixo fica livre
* Lowerlimit < Upperlimit -> o eixo fica limitado a esse intervalo
:::

Para PHY_LINEHINGE_CONSTRAINT = 2 ou PHY_ANGULAR_CONSTRAINT = 3:

axis = 3 é um limite da constraint, com valor de limite inferior/superior
* 3: ângulo do eixo X

- **`value0 (min)`**: Define o limite mínimo do eixo
  - tipo: float
- **`value1 (max)`**: Define o limite máximo do eixo
  - tipo: float
Para PHY_CONE_TWIST_CONSTRAINT = 4:

axis = 3..5 são limites da constraint, valores de limite superior
* 3: ângulo do eixo X
* 4: ângulo do eixo Y
* 5: ângulo do eixo Z

- **`value0 (min)`**: Define o limite mínimo do eixo
  - tipo: float
- **`value1 (max)`**: Define o limite máximo do eixo
  - tipo: float
Para PHY_GENERIC_6DOF_CONSTRAINT = 12:

axis = 0..2 são limites da constraint, com valor de limite inferior/superior
* 0: posição no eixo X
* 1: posição no eixo Y
* 2: posição no eixo Z

axis = 3..5 são ângulos (Euler) relativos da constraint, em radianos
* 3: ângulo do eixo X
* 4: ângulo do eixo Y
* 5: ângulo do eixo Z

- **`value0 (min)`**: Define o limite mínimo do eixo
  - tipo: float
- **`value1 (max)`**: Define o limite máximo do eixo
  - tipo: float
axis = 6..8 são motores de translação, com value0 = velocidade alvo, value1 = força máxima do motor
* 6: posição no eixo X
* 7: posição no eixo Y
* 8: posição no eixo Z

axis = 9..11 são motores de rotação, com value0 = velocidade alvo, value1 = força máxima do motor
* 9: ângulo do eixo X
* 10: ângulo do eixo Y
* 11: ângulo do eixo Z

- **`value0 (speed)`**: Define a velocidade linear do eixo
  - tipo: float Range: -10,000.00 to 10,000.00
- **`value1 (force)`**: Define o limite de força máxima do eixo
  - tipo: float Range: -10,000.00 to 10,000.00
axis = 12..14 são molas lineares em cada posição de liberdade
* 12: posição no eixo X
* 13: posição no eixo Y
* 14: posição no eixo Z

axis = 15..17 são molas angulares em cada ângulo de liberdade, em radianos
* 15: ângulo do eixo X
* 16: ângulo do eixo Y
* 17: ângulo do eixo Z

- **`value0 (stiffness)`**: Define a rigidez da mola
  - tipo: float
- **`value1 (damping)`**: Tendência da mola de voltar à posição original
  - tipo: float 1.0 = springs back to original position (no damping) 0.0 = don't springs back

### getParam(axis)

Pega a posição ou o ângulo de Euler de uma constraint 6DOF genérica

- **`axis`**:
  - tipo: integer
axis = 0..2 são valores de constraint linear
* 0: posição no eixo X
* 1: posição no eixo Y
* 2: posição no eixo Z

**Retorna:** posição

**Tipo do retorno:** float

axis = 3..5 são ângulos (Euler) relativos da constraint, em radianos
* 3: ângulo do eixo X
* 4: ângulo do eixo Y
* 5: ângulo do eixo Z

**Retorna:** ângulo

**Tipo do retorno:** float

### constraint_id

Devolve o ID da constraint (somente leitura)

**Tipo:** integer

### constraint_type

Devolve o tipo da constraint (somente leitura)

**Tipo:** integer - `POINTTOPOINT_CONSTRAINT` - `LINEHINGE_CONSTRAINT` - `ANGULAR_CONSTRAINT` - `CONETWIST_CONSTRAINT` - `VEHICLE_CONSTRAINT` - `GENERIC_6DOF_CONSTRAINT`

### breakingThreshold

O limite de impulso que quebra a constraint; se a constraint quebrar, `enabled` vira `False`.

**Tipo:** float greater or equal to 0

### enabled

O status da constraint. Use `True` para restaurar uma constraint depois de quebrada.

**Tipo:** boolean

