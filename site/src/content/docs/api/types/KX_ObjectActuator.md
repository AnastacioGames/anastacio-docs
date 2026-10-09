---
title: "KX_ObjectActuator"
description: "Referência da classe Range.types.KX_ObjectActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



O atuador de objeto ("Motion Actuator") aplica força, torque, deslocamento, deslocamento angular, velocidade ou velocidade angular a um objeto. O controle servo permite regular a força para atingir uma velocidade alvo.

### force

A força aplicada pelo atuador.

**Tipo:** Vector((x, y, z))

### useLocalForce

Flag que diz se a força é local.

**Tipo:** boolean

### torque

O torque aplicado pelo atuador.

**Tipo:** Vector((x, y, z))

### useLocalTorque

Flag que diz se o torque é local.

**Tipo:** boolean

### dLoc

O vetor de deslocamento aplicado pelo atuador.

**Tipo:** Vector((x, y, z))

### useLocalDLoc

Flag que diz se o dLoc é local.

**Tipo:** boolean

### dRot

O vetor de deslocamento angular aplicado pelo atuador

**Tipo:** Vector((x, y, z))

:::note
Como o deslocamento é aplicado a cada frame, é preciso ajustá-lo pelo frame rate, ou a experiência de jogo vai depender da velocidade do computador do jogador.
:::

### useLocalDRot

Flag que diz se o dRot é local.

**Tipo:** boolean

### linV

A velocidade linear aplicada pelo atuador.

**Tipo:** Vector((x, y, z))

### useLocalLinV

Flag que diz se a velocidade linear é local.

**Tipo:** boolean

:::note
Esta é a velocidade alvo dos controladores servo.
:::

### angV

A velocidade angular aplicada pelo atuador.

**Tipo:** Vector((x, y, z))

### useLocalAngV

Flag que diz se a velocidade angular é local.

**Tipo:** boolean

### damping

O parâmetro de amortecimento do controlador servo.

**Tipo:** short

### forceLimitX

O limite mín./máx. de força no eixo X, e liga ou desliga os limites no controlador servo.

**Tipo:** list [min(float), max(float), bool]

### forceLimitY

O limite mín./máx. de força no eixo Y, e liga ou desliga os limites no controlador servo.

**Tipo:** list [min(float), max(float), bool]

### forceLimitZ

O limite mín./máx. de força no eixo Z, e liga ou desliga os limites no controlador servo.

**Tipo:** list [min(float), max(float), bool]

### pid

Os coeficientes PID do controlador servo.

**Tipo:** list of floats [proportional, integral, derivate]

### reference

O objeto usado como referência para calcular a velocidade no controlador servo.

**Tipo:** `KX_GameObject` or None

