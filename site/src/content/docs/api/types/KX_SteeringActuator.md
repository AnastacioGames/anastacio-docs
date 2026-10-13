---
title: "KX_SteeringActuator"
description: "Referência da classe Range.types.KX_SteeringActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Steering para navegação.

### behavior

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

 <small>atributo</small>

Para onde o objeto vira ao andar: 0 não vira, 1 a 3 = eixo +X, +Y, +Z, 4 a 6 = -X, -Y, -Z.

### lockZVelocity

 <small>atributo</small>

Não mexe na velocidade vertical (Z) do objeto.

### steeringVec

 <small>atributo · só leitura</small>

Vetor de direção calculado pelo atuador neste frame.

