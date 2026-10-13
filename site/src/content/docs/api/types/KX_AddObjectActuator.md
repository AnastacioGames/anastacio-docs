---
title: "KX_AddObjectActuator"
description: "Referência da classe Range.types.KX_AddObjectActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Edit Object (no modo Add Object)

:::caution
Um atuador Add Object é ignorado se, no início do jogo, o objeto ligado não existir (ou estiver vazio) ou estiver numa layer ativa.

```text

Error: GameObject 'Name' has a AddObjectActuator 'ActuatorName' without object (in 'nonactive' layer)
```
:::

### object

o objeto que este atuador adiciona.

**Tipo:** `KX_GameObject` or None

### objectLastCreated

o último objeto adicionado por este atuador (somente leitura).

**Tipo:** `KX_GameObject` or None

### time

o tempo de vida dos objetos adicionados, em frames. Use 0 para desligar a remoção automática.

**Tipo:** float

### linearVelocity

a velocidade linear inicial dos objetos adicionados.

**Tipo:** list [vx, vy, vz]

### angularVelocity

a velocidade angular inicial dos objetos adicionados.

**Tipo:** list [vx, vy, vz]

### instantAddObject()

adiciona o objeto sem precisar chamar SCA_PythonController.activate()

:::note
Use objectLastCreated para pegar o objeto recém-criado.
:::

