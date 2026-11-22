# KX_VehicleWrapper

Classe base: [`EXP_PyObjectPlus`](EXP_PyObjectPlus.md)

> **Veja também:**
[`KX_GameObject`](KX_GameObject.md), [`Range.constraints`](Range.constraints.md), [`KX_CharacterWrapper`](KX_CharacterWrapper.md)

KX_VehicleWrapper

TODO - descrição

```python
# Cria um veículo com quatro rodas. Os objetos das rodas precisam estar em No Collision.
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

vehicle = constraints.createVehicle(own.getPhysicsId())
own["vehicle_id"] = vehicle.getConstraintId()

wheels = (
    ("WheelFL", (-1.0, 1.5, 0.0), True),
    ("WheelFR", (1.0, 1.5, 0.0), True),
    ("WheelRL", (-1.0, -1.5, 0.0), False),
    ("WheelRR", (1.0, -1.5, 0.0), False),
)

for name, position, steering in wheels:
    vehicle.addWheel(scene.objects[name], position, (0, 0, -1), (-1, 0, 0), 0.4, 0.5, steering)
```

```python
# Dirige a cada quadro.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
vehicle = constraints.getVehicleConstraint(own["vehicle_id"])
keys = Range.logic.keyboard.inputs

force = -800.0 if keys[Range.events.WKEY].active else 0.0
steer = 0.3 if keys[Range.events.AKEY].active else 0.0

for wheel in range(vehicle.getNumWheels()):
    vehicle.applyEngineForce(force, wheel)

vehicle.setSteeringValue(steer, 0)
vehicle.setSteeringValue(steer, 1)
print(vehicle.getCurrentSpeedKmh())
```

```python
# Ajusta a suspensão de cada roda.
for wheel in range(vehicle.getNumWheels()):
    vehicle.setSuspensionStiffness(20.0, wheel)
    vehicle.setSuspensionDamping(2.0, wheel)
    vehicle.setSuspensionCompression(4.0, wheel)
    vehicle.setTyreFriction(2.0, wheel)
```

## addWheel(wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering)

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

 `método`

Eixos `(direita, cima, frente)` do veículo (0=X, 1=Y, 2=Z).

**Retorna:** `tuple`

### getCurrentSpeedKmh()

 `método`

Velocidade atual em km/h.

**Retorna:** `float`

### getCurrentSpeedMps()

 `método`

Velocidade atual em metros por segundo.

**Retorna:** `float`

### getForwardVector()

 `método`

Direção da frente do veículo, no mundo.

**Retorna:** `Vector`

### getWheelConfig(wheelIndex)

 `método`

Configuração da roda: `connectionPoint`, `downDirection`, `axleDirection`, `suspensionRestLength`, `wheelRadius`, `hasSteering` e `isDriveWheel`.

**Retorna:** `dict`

### getWheelState(wheelIndex)

 `método`

Estado da roda neste tick: posição e orientação no mundo, `rotation`, `isInContact`, ponto e normal do contato, `suspensionForce` e mais.

**Retorna:** `dict`

### loadPreset(path)

 `método`

Carrega um preset de veículo (arquivo) e aplica neste veículo.

### rebuildPreset(path, wheelObjects)

 `método`

Recria as rodas a partir do preset, usando os objetos dados (um por roda). Use Empties com física **No Collision** como rodas.

### resetSuspension()

 `método`

Volta a suspensão ao estado de repouso (útil depois de teleportar o carro).

### savePreset(path)

 `método`

Salva a configuração atual do veículo num arquivo de preset.

### setCoordinateSystem(right, up, forward)

 `método`

Define quais eixos (0=X, 1=Y, 2=Z) são direita, cima e frente. Precisa usar os três eixos sem repetir.

### setSuspensionRestLength(valor, wheelIndex)

*(novo na Anastacio)* `método`

Muda o comprimento de repouso da suspensão de uma roda (valor positivo). Aplicado no próximo passo da física.

### setWheelIsDriveWheel(wheelIndex, isDriveWheel)

 `método`

Define se a roda recebe tração do motor.

### setWheelRadius(valor, wheelIndex)

*(novo na Anastacio)* `método`

Muda o raio de uma roda (valor positivo). Aplicado no próximo passo da física.

### constraint_id

 `atributo · só leitura`

Id da restrição (constraint) física do veículo.

### constraint_type

 `atributo · só leitura`

Tipo da restrição física do veículo.
