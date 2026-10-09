---
title: "Range.constraints"
description: "Referência do módulo Range.constraints"
---

A Bullet Physics cuida da detecção de colisão e da dinâmica de corpos rígidos da game engine.

Recursos:

- Simulação de veículos.
- Constraints de corpo rígido: hinge e ponto a ponto (ball socket).
- Acesso às configurações internas da física,
como o tempo de desativação, e recursos de depuração

:::note
Como esta API não é bem documentada, pode não ficar claro que valores usar nos parâmetros. Em geral, os amortecimentos devem ficar entre 0 e 1 e as rigidezes não devem passar muito de 10.
:::

## Exemplos

:::tip
Para mais exemplos da física Bullet e de como usá-la, veja o [fórum do pybullet](https://pybullet.org/Bullet/phpBB3/viewforum.php?f=17)_.
:::

## Funções

### createConstraint( \

physicsid_1, physicsid_2, constraint_type, \ pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, \ axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0)

Cria uma constraint.

- **`physicsid_1`**: O physics id do primeiro objeto da constraint.
  - tipo: int
- **`physicsid_2`**: O physics id do segundo objeto da constraint.
  - tipo: int
- **`constraint_type`**: O tipo da constraint; veja `Create Constraint Constants`_.
  - tipo: int
- **`pivot_x`**: Posição X do pivô (opcional).
  - tipo: float
- **`pivot_y`**: Posição Y do pivô (opcional).
  - tipo: float
- **`pivot_z`**: Posição Z do pivô (opcional).
  - tipo: float
- **`axis_x`**: Ângulo do eixo X em graus (opcional).
  - tipo: float
- **`axis_y`**: Ângulo do eixo Y em graus (opcional).
  - tipo: float
- **`axis_z`**: Ângulo do eixo Z em graus (opcional).
  - tipo: float
- **`flag`**: 128 para desligar a colisão entre os corpos ligados (opcional).
  - tipo: int

**Retorna:** Um wrapper de constraint.

**Tipo do retorno:** `KX_ConstraintWrapper`

### createVehicle(physicsid)

Cria uma constraint de veículo.

- **`physicsid`**: O physics id do objeto chassi da constraint.
  - tipo: int

**Retorna:** Um wrapper de constraint de veículo.

**Tipo do retorno:** `KX_VehicleWrapper`

### exportBulletFile(filename)

Exporta um arquivo que representa o mundo da dinâmica (em geral com extensão `.bullet`).

Veja [Bullet binary serialization](http://bulletphysics.org/mediawiki-1.5.8/index.php/Bullet_binary_serialization)_.

- **`filename`**: Caminho do arquivo.
  - tipo: str

### getAppliedImpulse(constraintId)

- **`constraintId`**: O id da constraint.
  - tipo: int

**Retorna:** O último impulso aplicado.

**Tipo do retorno:** float

### getVehicleConstraint(constraintId)

- **`constraintId`**: O id da constraint de veículo.
  - tipo: int

**Retorna:** Um objeto de constraint de veículo.

**Tipo do retorno:** `KX_VehicleWrapper`

### getCharacter(gameobj)

- **`gameobj`**: O game object com a física de personagem.
  - tipo: `KX_GameObject`

**Retorna:** Wrapper de personagem.

**Tipo do retorno:** `KX_CharacterWrapper`

### removeConstraint(constraintId)

Remove uma constraint.

- **`constraintId`**: O id da constraint a remover.
  - tipo: int

### setCcdMode(ccdMode)

:::note
Muito experimental, não recomendado
:::

Define o modo de CCD (detecção contínua de colisão) no ambiente de física.

- **`ccdMode`**: O novo modo de CCD.
  - tipo: int

### setContactBreakingTreshold(breakingTreshold)

:::note
Um padrão razoável é 0.02 (se as unidades forem metros)
:::

Define limites ligados ao gerenciamento de pontos de contato.

- **`breakingTreshold`**: O novo limite de quebra de contato.
  - tipo: float

### setDeactivationAngularTreshold(angularTreshold)

Define o limite de velocidade angular.

- **`angularTreshold`**: Novo limite angular de desativação.
  - tipo: float

### setDeactivationLinearTreshold(linearTreshold)

Define o limite de velocidade linear.

- **`linearTreshold`**: Novo limite linear de desativação.
  - tipo: float

### setDeactivationTime(time)

Define o tempo depois do qual um corpo rígido parado é desativado.

- **`time`**: O tempo de desativação.
  - tipo: float

### setDebugMode(mode)

Define o modo de depuração.

- **`mode`**: O novo modo de depuração; veja `Debug Mode Constants`_.
  - tipo: int

### setGravity(x, y, z)

Define a força da gravidade.

- **`x`**: Força da gravidade em X.
  - tipo: float
- **`y`**: Força da gravidade em Y.
  - tipo: float
- **`z`**: Força da gravidade em Z.
  - tipo: float

### setLinearAirDamping(damping)

:::note
Não implementado
:::

Define o amortecimento linear do ar para corpos rígidos.

### setNumIterations(numiter)

Define o número de iterações de um solver de constraints iterativo.

- **`numiter`**: Novo número de iterações.
  - tipo: int

### setLinearSlop(slop)

Define a tolerância de penetração de contato da cena de física ativa. Um valor positivo deixa os objetos se sobreporem até `slop` unidades do Blender antes de o solver do Bullet aplicar a correção de posição. O padrão é `0.0`.

É uma configuração do solver para a cena inteira: afeta todos os contatos físicos da cena ativa. Não muda a margem de colisão de um objeto nem o ponto em que as colisões são detectadas. Use valores pequenos, adequados à escala da cena.

- **`slop`**: Tolerância de penetração em unidades do Blender. Use um valor finito e não negativo.
  - tipo: float

### setNumTimeSubSteps(numsubstep)

Define o número de substeps de cada passo da física. Troca qualidade por desempenho.

- **`numsubstep`**: Novo número de substeps.
  - tipo: int

### setSolverDamping(damping)

:::note
Muito experimental, não recomendado
:::

Define a constante de amortecimento de um solver baseado em penalidade.

- **`damping`**: Novo amortecimento do solver.
  - tipo: float

### setSolverTau(tau)

:::note
Muito experimental, não recomendado
:::

Define a constante de mola de um solver baseado em penalidade.

- **`tau`**: Novo tau do solver.
  - tipo: float

### setSolverType(solverType)

:::note
Muito experimental, não recomendado
:::

Define o tipo do solver.

- **`solverType`**: O novo tipo do solver.
  - tipo: int

### setSorConstant(sor)

:::note
Muito experimental, não recomendado
:::

Define a constante de sobre-relaxação sucessiva.

- **`sor`**: Novo valor de sor.
  - tipo: float

### setUseEpa(epa)

:::note
Não implementado
:::

## Constantes

### error

String constante simbólica que indica erro.

**Tipo:** str

## Constantes de modo de depuração

Modo de depuração a usar com `setDebugMode`.

### DBG_NODEBUG

Sem depuração.

### DBG_DRAWWIREFRAME

Desenha wireframe na depuração.

### DBG_DRAWAABB

Desenha a Axis Aligned Bounding Box na depuração.

### DBG_DRAWFREATURESTEXT

Desenha o texto dos recursos na depuração.

### DBG_DRAWCONTACTPOINTS

Desenha os pontos de contato na depuração.

### DBG_NOHELPTEXT

Depuração sem texto de ajuda.

### DBG_DRAWTEXT

Desenha texto na depuração.

### DBG_PROFILETIMINGS

Desenha os tempos de profile na depuração.

### DBG_ENABLESATCOMPARISION

Liga a comparação sat na depuração.

### DBG_DISABLEBULLETLCP

Desliga o LCP do Bullet.

### DBG_ENABLECCD

Liga a detecção contínua de colisão na depuração.

### DBG_DRAWCONSTRAINTS

Desenha as constraints na depuração.

### DBG_DRAWCONSTRAINTLIMITS

Desenha os limites das constraints na depuração.

### DBG_FASTWIREFRAME

Desenha um wireframe rápido na depuração.

## Constantes de criação de constraint

Tipo de constraint a usar com `createConstraint`.

### POINTTOPOINT_CONSTRAINT

.. to do

### LINEHINGE_CONSTRAINT

.. to do

### ANGULAR_CONSTRAINT

.. to do

### CONETWIST_CONSTRAINT

.. to do

### VEHICLE_CONSTRAINT

.. to do

### GENERIC_6DOF_CONSTRAINT

.. to do

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### setErp()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setErp2()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setGlobalCfm()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setMaxGyroscopicForce()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setSplitImpulse()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setSplitImpulsePenetrationThreshold()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setSplitImpulseTurnErp()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setWarmstartingFactor()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

