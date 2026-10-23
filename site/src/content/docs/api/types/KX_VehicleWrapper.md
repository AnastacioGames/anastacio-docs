---
title: "KX_VehicleWrapper"
description: "Referência da classe Range.types.KX_VehicleWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[Veja também]
[`KX_GameObject`](../../types/kx_gameobject/), [`Range.constraints`](../../modulos/constraints/), [`KX_CharacterWrapper`](../../types/kx_characterwrapper/)
:::



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

 <small>método</small>

Eixos `(direita, cima, frente)` do veículo (0=X, 1=Y, 2=Z).

**Retorna:** `tuple`

### getCurrentSpeedKmh()

 <small>método</small>

Velocidade atual em km/h.

**Retorna:** `float`

### getCurrentSpeedMps()

 <small>método</small>

Velocidade atual em metros por segundo.

**Retorna:** `float`

### getForwardVector()

 <small>método</small>

Direção da frente do veículo, no mundo.

**Retorna:** `Vector`

### getWheelConfig(wheelIndex)

 <small>método</small>

Configuração da roda: `connectionPoint`, `downDirection`, `axleDirection`, `suspensionRestLength`, `wheelRadius`, `hasSteering` e `isDriveWheel`.

**Retorna:** `dict`

### getWheelState(wheelIndex)

 <small>método</small>

Estado da roda neste tick: posição e orientação no mundo, `rotation`, `isInContact`, ponto e normal do contato, `suspensionForce` e mais.

**Retorna:** `dict`

### loadPreset(path)

 <small>método</small>

Carrega um preset de veículo (arquivo) e aplica neste veículo.

### rebuildPreset(path, wheelObjects)

 <small>método</small>

Recria as rodas a partir do preset, usando os objetos dados (um por roda). Use Empties com física **No Collision** como rodas.

### resetSuspension()

 <small>método</small>

Volta a suspensão ao estado de repouso (útil depois de teleportar o carro).

### savePreset(path)

 <small>método</small>

Salva a configuração atual do veículo num arquivo de preset.

### setCoordinateSystem(right, up, forward)

 <small>método</small>

Define quais eixos (0=X, 1=Y, 2=Z) são direita, cima e frente. Precisa usar os três eixos sem repetir.

### setSuspensionRestLength(valor, wheelIndex)

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

Muda o comprimento de repouso da suspensão de uma roda (valor positivo). Aplicado no próximo passo da física.

### setWheelIsDriveWheel(wheelIndex, isDriveWheel)

 <small>método</small>

Define se a roda recebe tração do motor.

### setWheelRadius(valor, wheelIndex)

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

Muda o raio de uma roda (valor positivo). Aplicado no próximo passo da física.

### constraint_id

 <small>atributo · só leitura</small>

Id da restrição (constraint) física do veículo.

### constraint_type

 <small>atributo · só leitura</small>

Tipo da restrição física do veículo.

