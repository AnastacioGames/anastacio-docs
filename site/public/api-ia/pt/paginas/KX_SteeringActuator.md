# KX_SteeringActuator

Classe base: [`SCA_IActuator`](SCA_IActuator.md)

> **Veja também:**
[`KX_NavMeshObject`](KX_NavMeshObject.md)

Atuador Steering para navegação.

```python
# Segue o jogador usando uma malha de navegação.
import Range

cont = Range.logic.getCurrentController()
scene = Range.logic.getCurrentScene()
act = cont.actuators["Steering"]

act.behavior = Range.logic.KX_STEERING_PATHFOLLOWING
act.target = scene.objects["Player"]
act.navmesh = scene.objects["Navmesh"]
act.velocity = 3.0
act.distance = 1.0
cont.activate(act)
```

## behavior

O comportamento de steering a usar.

**Tipo:** one of `these constants`

### velocity

Módulo da velocidade

**Tipo:** float

### acceleration

Aceleração máxima

**Tipo:** float

### turnspeed

Velocidade máxima de giro

**Tipo:** float

### distance

Distância de relaxamento

**Tipo:** float

### target

Objeto alvo

**Tipo:** `KX_GameObject`

### navmesh

Navigation mesh

**Tipo:** `KX_GameObject`

### selfterminated

Termina quando o alvo é alcançado

**Tipo:** boolean

### enableVisualization

Liga a visualização de depuração

**Tipo:** boolean

### pathUpdatePeriod

Período de atualização do caminho

**Tipo:** int

### path

Lista de pontos do caminho.

**Tipo:** list of `mathutils.Vector`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### facingMode

 `atributo`

Para onde o objeto vira ao andar: 0 não vira, 1 a 3 = eixo +X, +Y, +Z, 4 a 6 = -X, -Y, -Z.

### lockZVelocity

 `atributo`

Não mexe na velocidade vertical (Z) do objeto.

### steeringVec

 `atributo · só leitura`

Vetor de direção calculado pelo atuador neste frame.
