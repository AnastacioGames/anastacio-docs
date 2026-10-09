---
title: "KX_VehicleWrapper"
description: "Referência da classe Range.types.KX_VehicleWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



KX_VehicleWrapper

TODO - descrição

### addWheel(wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering)

Adiciona uma roda ao veículo

- **`wheel`**: O objeto a usar como roda.
  - tipo: `KX_GameObject` or a `KX_GameObject` name
- **`attachPos`**: A posição onde prender a roda, relativa ao centro do objeto chassi.
  - tipo: vector of 3 floats
- **`downDir`**: O vetor de direção apontando para baixo, até onde o veículo deve colidir com o chão.
  - tipo: vector of 3 floats
- **`axleDir`**: O eixo em torno do qual a roda gira, relativo ao chassi.
  - tipo: vector of 3 floats
- **`suspensionRestLength`**: O comprimento da suspensão quando nenhuma força está sendo aplicada.
  - tipo: float
- **`wheelRadius`**: O raio da roda (metade do diâmetro).
  - tipo: float
- **`hasSteering`**: True se a roda deve virar com o volante; em geral usado nas rodas da frente.
  - tipo: boolean

### applyBraking(force, wheelIndex)

Aplica uma força de freio à roda indicada

- **`force`**: a força de freio
  - tipo: float
- **`wheelIndex`**: índice da roda em que a força deve ser aplicada
  - tipo: integer

### applyEngineForce(force, wheelIndex)

Aplica uma força de motor à roda indicada

- **`force`**: a força do motor
  - tipo: float
- **`wheelIndex`**: índice da roda em que a força deve ser aplicada
  - tipo: integer

### getConstraintId()

Pega o ID da constraint

**Retorna:** o id da constraint

**Tipo do retorno:** integer

### getConstraintType()

Devolve o tipo da constraint.

**Retorna:** tipo da constraint

**Tipo do retorno:** integer

### getNumWheels()

Devolve o número de rodas.

**Retorna:** o número de rodas deste veículo

**Tipo do retorno:** integer

### getWheelOrientationQuaternion(wheelIndex)

Devolve a orientação da roda como quaternion.

- **`wheelIndex`**: o índice da roda
  - tipo: integer

**Retorna:** TODO Descrição

**Tipo do retorno:** TODO - type should be quat as per method name but from the code it looks like a matrix

### getWheelPosition(wheelIndex)

Devolve a posição da roda indicada

- **`wheelIndex`**: o índice da roda
  - tipo: integer

**Retorna:** vetor de posição

**Tipo do retorno:** list[x, y, z]

### getWheelRotation(wheelIndex)

Devolve a rotação da roda indicada

- **`wheelIndex`**: o índice da roda
  - tipo: integer

**Retorna:** a rotação da roda

**Tipo do retorno:** float

### setRollInfluence(rollInfluece, wheelIndex)

Define a influência de rolagem da roda indicada. Quanto maior a influência, mais o veículo tende a capotar nas curvas.

- **`rollInfluece`**: a influência de rolagem da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

### setSteeringValue(steering, wheelIndex)

Define o esterço da roda indicada

- **`steering`**: o esterço da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

### setSuspensionCompression(compression, wheelIndex)

Define a compressão da roda indicada

- **`compression`**: a compressão da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

### setSuspensionDamping(damping, wheelIndex)

Define o amortecimento da roda indicada

- **`damping`**: o amortecimento da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

### setSuspensionStiffness(stiffness, wheelIndex)

Define a rigidez da roda indicada

- **`stiffness`**: a rigidez da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

### setTyreFriction(friction, wheelIndex)

Define o atrito do pneu da roda indicada

- **`friction`**: o atrito do pneu
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

### rayMask

Define a máscara do ray cast.

**Tipo:** bitfield

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getCoordinateSystem()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getCurrentSpeedKmh()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getCurrentSpeedMps()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getForwardVector()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getWheelConfig()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getWheelState()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### loadPreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### rebuildPreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### resetSuspension()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### savePreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setCoordinateSystem()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setWheelIsDriveWheel()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### constraint_id

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### constraint_type

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

