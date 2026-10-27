---
title: "KX_CharacterWrapper"
description: "Referência da classe Range.types.KX_CharacterWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[Veja também]
[`KX_GameObject`](../../types/kx_gameobject/), [`Range.constraints`](../../modulos/constraints/)
:::



Um wrapper que expõe as opções de física de personagem.

:::note
Quando o objeto do personagem é removido, todo método e atributo do wrapper gera `ReferenceError`. Suspender a física mantém o personagem, então o wrapper continua funcionando.
:::

### onGround

Se o personagem está no chão ou não (somente leitura).

**Tipo:** boolean

### gravity

O valor de gravidade usado para o personagem.

**Tipo:** float

### fallSpeed

A velocidade de queda do personagem.

**Tipo:** float

### maxJumps

O número máximo de pulos que o personagem pode dar antes de tocar o chão. O padrão é 1. 2 permite pulo duplo, e assim por diante.

**Tipo:** int in [0, 255], default 1

### jumpCount

A contagem de pulos atual. Serve para ter lógicas diferentes para pulo simples e pulo duplo, por exemplo, uma animação diferente no segundo pulo.

**Tipo:** int

### jumpSpeed

A velocidade de pulo do personagem.

**Tipo:** float

### maxSlope

A inclinação máxima que o personagem consegue subir.

**Tipo:** float

### walkDirection

A velocidade e a direção em que o personagem anda, em coordenadas do mundo. Use isto em vez de applyMovement() para mover o personagem do jeito certo.

**Tipo:** Vector((x, y, z))

### jump()

O personagem pula com base na sua velocidade de pulo.

### jumpDirection

A direção em que o personagem pula.

**Tipo:** Vector((x, y, z))

### setVelocity(velocity, time, local=False)

Define a velocidade linear do personagem por um período.

Este método define a velocidade do personagem pelo centro de massa durante um período.

- **`velocity`**: Vetor de velocidade linear.
  - tipo: 3D Vector
- **`time`**: Período em que a velocidade linear é aplicada.
  - tipo: float
- **`local`**: * False: velocidade "global", ou seja, relativa à orientação do mundo. * True: velocidade "local", ou seja, relativa à orientação do objeto.
  - tipo: boolean

### smoothMovement

Suaviza o movimento causado pela direção de caminhada.

**Tipo:** float (0.0 to 1.0)

### reset()

Zera a velocidade e a direção de caminhada do personagem.

