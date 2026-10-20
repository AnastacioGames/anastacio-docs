---
title: "KX_GameObject"
description: "Referência da classe Range.types.KX_GameObject"
---

Classe base: [`SCA_IObject`](../sca_iobject/)

:::tip[Veja também]
[`KX_Scene`](../../types/kx_scene/), [`KX_Mesh`](../../types/kx_mesh/), [`KX_PythonComponent`](../../types/kx_pythoncomponent/), [`KX_VehicleWrapper`](../../types/kx_vehiclewrapper/), [`KX_ParticleSystem`](../../types/kx_particlesystem/)
:::



Todos os objetos do jogo derivam desta classe.

As propriedades de jogo do objeto podem ser acessadas como atributos desta classe.

:::note
Chamar QUALQUER método ou atributo de um objeto que já foi removido da cena gera SystemError. Se o objeto pode ter sido removido desde o último acesso, confira antes com o atributo `invalid`.
:::

KX_GameObject pode ser herdado para estender o que ele faz. Por exemplo:

```python

import Range

class CustomGameObject(Range.types.KX_GameObject):
    RATE = 0.05

    def __init__(self, old_owner):
        # "old_owner" pode ser ignorado. Neste ponto, "self" já é
        # o objeto na cena, e "old_owner" já foi
        # destruído.

        # Dá para criar atributos novos, mas também poderíamos usar uma
        # propriedade de jogo, como "self['rate']".
        self.rate = CustomGameObject.RATE

    def update(self):
        self.worldPosition.z += self.rate

        # inverte a direção
        if self.worldPosition.z > 1.0:
            self.rate = -CustomGameObject.RATE
        elif self.worldPosition.z < 0.0:
            self.rate = CustomGameObject.RATE

# Chamado primeiro
def mutate(cont):
    old_object = cont.owner
    mutated_object = CustomGameObject(cont.owner)

    # Depois de chamar o construtor acima, as referências ao objeto antigo
    # não devem mais ser usadas.
    assert(old_object is not mutated_object)
    assert(old_object.invalid)
    assert(mutated_object is cont.owner)

# Chamado depois. Repare que agora estamos usando o objeto transformado.
def update(cont):
    cont.owner.update()
```

Ao herdar de objetos que não são vazios nem malhas, use o tipo específico. Por exemplo, herde de `BL_ArmatureObject` quando o objeto a transformar for uma armature.

### name

O nome do objeto.

**Tipo:** string

### mass

A massa do objeto.

**Tipo:** float

:::note
O objeto precisa de um controlador de física para a massa valer; sem ele, a massa é lida como 0.0.
:::

### friction

O atrito do objeto.

**Tipo:** float

### isSuspendDynamics

O estado dinâmico do objeto (somente leitura).

**Tipo:** boolean

:::tip
`suspendDynamics` e `restoreDynamics` permitem mudar esse estado.
:::

### linearDamping

O amortecimento linear do objeto, também chamado de amortecimento de translação. Pode ser definido junto com o amortecimento angular pelo método `setDamping`.

**Tipo:** float between 0 and 1 inclusive.

:::note
O objeto precisa de um controlador de física para o amortecimento linear valer; sem ele, o valor é lido como 0.0.
:::

### angularDamping

O amortecimento angular do objeto, também chamado de amortecimento de rotação. Pode ser definido junto com o amortecimento linear pelo método `setDamping`.

**Tipo:** float between 0 and 1 inclusive.

:::note
O objeto precisa de um controlador de física para o amortecimento angular valer; sem ele, o valor é lido como 0.0.
:::

### linVelocityMin

Obriga o objeto a continuar se movendo com uma velocidade mínima.

**Tipo:** float

:::note
Vale só para objetos dinâmicos e rígidos.
:::

:::note
O valor 0.0 desliga esta opção.
:::

:::note
Enquanto o objeto está parado, a velocidade mínima não é aplicada.
:::

### linVelocityMax

Limita a velocidade linear máxima, para o objeto não passar de uma certa velocidade.

**Tipo:** float

:::note
Vale só para objetos dinâmicos e rígidos.
:::

:::note
O valor 0.0 desliga esta opção (não deixa o objeto parado).
:::

### angularVelocityMin

Obriga o objeto a continuar girando com uma velocidade mínima. O valor 0.0 desliga.

**Tipo:** non-negative float

:::note
Vale só para objetos dinâmicos e rígidos. Enquanto o objeto está parado, a velocidade mínima não é aplicada.
:::

### angularVelocityMax

Limita a velocidade angular máxima, para o objeto não girar além de uma certa velocidade. O valor 0.0 desliga o limite; não para a rotação.

**Tipo:** non-negative float

:::note
Vale só para objetos dinâmicos e rígidos.
:::

### localInertia

O vetor de inércia do objeto em coordenadas locais. Somente leitura.

**Tipo:** Vector((ix, iy, iz))

### parent

O objeto pai deste objeto (somente leitura).

**Tipo:** `KX_GameObject` or None

### groupMembers

Devolve a lista de membros do grupo se o objeto for um objeto de grupo (instância de dupli group); caso contrário, devolve None.

**Tipo:** `EXP_ListValue` of `KX_GameObject` or None

### groupObject

Devolve o objeto de grupo (instância de dupli group) a que o objeto pertence, ou None se ele não faz parte de um grupo.

**Tipo:** `KX_GameObject` or None

### collisionGroup

O grupo de colisão do objeto.

**Tipo:** bitfield

### collisionMask

A máscara de colisão do objeto.

**Tipo:** bitfield

### collisionCallbacks

Lista de funções chamadas quando acontece uma colisão.

**Tipo:** list of functions and/or methods

As funções devem aceitar um argumento `(object)` ou quatro argumentos `(object, point, normal, points)`. Para simplificar, o primeiro ponto de colisão de cada objeto colidido vem no segundo e no terceiro argumento.

```python

# Como função
def callback_four(object, point, normal, points):
    print('Hit by %r with %i contacts points' % (object.name, len(points)))

def callback_three(object, point, normal):
    print('Hit by %r at %s with normal %s' % (object.name, point, normal))

def callback_one(object):
    print('Hit by %r' % object.name)

def register_callback(controller):
    controller.owner.collisionCallbacks.append(callback_four)
    controller.owner.collisionCallbacks.append(callback_three)
    controller.owner.collisionCallbacks.append(callback_one)

# Como método
class YourGameEntity(Range.types.KX_GameObject):
    def __init__(self, old_owner):
        self.collisionCallbacks.append(self.on_collision_four)
        self.collisionCallbacks.append(self.on_collision_three)
        self.collisionCallbacks.append(self.on_collision_one)

    def on_collision_four(self, object, point, normal, points):
        print('Hit by %r with %i contacts points' % (object.name, len(points)))

    def on_collision_three(self, object, point, normal):
        print('Hit by %r at %s with normal %s' % (object.name, point, normal))

    def on_collision_one(self, object):
        print('Hit by %r' % object.name)
```

:::note
Por compatibilidade, uma função com número variável de argumentos (usando `*args`) recebe só o argumento `object`. A forma com quatro argumentos só é usada quando há mais de um argumento fixo (sem contar o `self` dos métodos).
:::

### scene

A cena do objeto (somente leitura).

**Tipo:** `KX_Scene` or None

### visible

Indica se o objeto está visível.

**Tipo:** boolean

:::note
A lógica do jogo continua rodando para objetos invisíveis.
:::

### layer

A máscara de camadas usada no render de sombras e de cube maps em tempo real.

**Tipo:** bitfield

### cullingBox

A caixa de volume do objeto, usada no culling.

**Tipo:** `KX_BoundingBox`

### culled

Devolve True se o objeto foi descartado pelo culling; caso contrário, False.

:::caution
Esta variável devolve um valor inválido se for lida fora dos callbacks da cena `KX_Scene.pre_draw` e `KX_Scene.post_draw`.
:::

**Tipo:** boolean (read only)

### color

A cor do objeto. [r, g, b, a]

**Tipo:** `mathutils.Vector`

### occlusion

Indica se o objeto participa do occlusion culling.

**Tipo:** boolean

### physicsCulling

True se o objeto suspende a física conforme a distância até a câmera mais próxima.

**Tipo:** boolean

### physicsCullingVelocity

Para a física depois que o objeto para.

**Tipo:** boolean

### logicCulling

True se o objeto suspende a lógica e a animação conforme a distância até a câmera mais próxima.

**Tipo:** boolean

### logicCullingComponents

Não suspende a execução dos componentes do objeto.

**Tipo:** boolean

### physicsCullingRadius

Suspende a física do objeto se este raio for menor que a distância até a câmera mais próxima e `physicsCulling` estiver `True`.

**Tipo:** float

### logicCullingRadius

Suspende a lógica e a animação do objeto se este raio for menor que a distância até a câmera mais próxima e `logicCulling` estiver `True`.

**Tipo:** float

### ~~position~~

A posição do objeto. [x, y, z] Na escrita: posição local; na leitura: posição no mundo.

:::danger[Obsoleto use :data:`localPosition` and :data:`worldPosition`.]

:::

**Tipo:** `mathutils.Vector`

### ~~orientation~~

A orientação do objeto. Matriz 3x3. Também aceita um Quaternion ou um vetor Euler. Na escrita: orientação local; na leitura: orientação no mundo.

:::danger[Obsoleto use :data:`localOrientation` and :data:`worldOrientation`.]

:::

**Tipo:** `mathutils.Matrix`

### ~~scaling~~

O fator de escala do objeto. [sx, sy, sz] Na escrita: escala local; na leitura: escala no mundo.

:::danger[Obsoleto use :data:`localScale` and :data:`worldScale`.]

:::

**Tipo:** `mathutils.Vector`

### localOrientation

A orientação local do objeto. Matriz 3x3. Também aceita um Quaternion ou um vetor Euler.

**Tipo:** `mathutils.Matrix`

### worldOrientation

A orientação do objeto no mundo. Matriz 3x3.

**Tipo:** `mathutils.Matrix`

### localScale

O fator de escala local do objeto. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

### worldScale

O fator de escala do objeto no mundo. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

### localPosition

A posição local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

### worldPosition

A posição do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

### localTransform

A matriz de transformação local do objeto. Matriz 4x4.

**Tipo:** `mathutils.Matrix`

### worldTransform

A matriz de transformação do objeto no mundo. Matriz 4x4.

**Tipo:** `mathutils.Matrix`

### localLinearVelocity

A velocidade linear local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

### worldLinearVelocity

A velocidade linear do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

### localAngularVelocity

A velocidade angular local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

### worldAngularVelocity

A velocidade angular do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

### gravity

A gravidade do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

### timeOffset

Ajusta o atraso do slow parent durante o jogo.

**Tipo:** float

### state

A máscara de estados do objeto, usando os 30 primeiros bits; pelo menos um bit precisa estar ligado.

**Tipo:** int

### meshes

Lista das malhas deste objeto.

**Tipo:** list of `KX_Mesh`

:::note
A maioria dos objetos usa só 1 malha.
:::

:::note
Mudar esta lista não atualiza o KX_GameObject.
:::

### batchGroup

O grupo de batch que contém a malha agrupada do objeto.

**Tipo:** `KX_BatchGroup`

### sensors

Uma sequência de objetos `SCA_ISensor`, com busca por nome/índice e suporte a iteração.

**Tipo:** list

:::note
Este atributo é experimental e pode ser removido (mas provavelmente não será).
:::

:::note
Mudar esta lista não atualiza o KX_GameObject.
:::

### controllers

Uma sequência de objetos `SCA_IController`, com busca por nome/índice e suporte a iteração.

**Tipo:** list of `SCA_ISensor`

:::note
Este atributo é experimental e pode ser removido (mas provavelmente não será).
:::

:::note
Mudar esta lista não atualiza o KX_GameObject.
:::

### actuators

Uma lista de `SCA_IActuator`, com busca por nome/índice e suporte a iteração.

**Tipo:** list

:::note
Este atributo é experimental e pode ser removido (mas provavelmente não será).
:::

:::note
Mudar esta lista não atualiza o KX_GameObject.
:::

### attrDict

Dá o dicionário interno de atributos Python do objeto, para acesso direto (mais rápido).

**Tipo:** dict

### components

Todos os componentes Python.

**Tipo:** `EXP_ListValue` of `KX_PythonComponent`'s

### children

Os filhos diretos deste objeto (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

### childrenRecursive

Todos os filhos deste objeto, incluindo os filhos dos filhos (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

### life

Quantos frames faltam para o objeto acabar, considerando um frame como 1/50 de segundo (somente leitura).

**Tipo:** float

### debug

Se for True, as propriedades de depuração do objeto aparecem na tela.

**Tipo:** boolean

### debugRecursive

Se for True, as propriedades de depuração do objeto e dos filhos aparecem na tela.

**Tipo:** boolean

### currentLodLevel

O índice do nível de detalhe (LOD) que o objeto está usando agora (somente leitura).

**Tipo:** int

### lodManager

Devolve o gerenciador de LOD do objeto, necessário para configurar os níveis de detalhe dele. O gerenciador é compartilhado entre as instâncias e pode ser trocado para usar os níveis de LOD de outro objeto. Se for definido como `None`, a malha do objeto volta a ser a do primeiro nível de LOD anterior.

**Tipo:** `KX_LodManager`

### isDestructible

True se Physics > Destruction estiver ligado neste objeto, inclusive em objetos de camadas inativas (somente leitura).

**Tipo:** boolean

### isExplosive

True se Physics > Explosive estiver ligado neste objeto, inclusive em objetos de camadas inativas (somente leitura).

**Tipo:** boolean

### breakImpulse

O impulso que quebra este objeto destrutível, vindo de uma colisão ou de `KX_Scene.explode`. Começa com o Break Impulse do painel; mudar o valor afeta só esta instância. Em objetos que não são destrutíveis, lê 0.0, e escrever gera AttributeError.

**Tipo:** float

### fuse

Segundos que faltam para este objeto explosivo detonar. O pavio conta a partir do momento em que o objeto entra no jogo (início da cena ou `KX_Scene.addObject`). 0.0 significa sem pavio; definir um valor acende o pavio. Em objetos que não são explosivos, escrever gera AttributeError.

**Tipo:** float

### explosionRadius

Raio da explosão deste objeto explosivo, em metros. Como todos os atributos do painel Explosive abaixo, levanta `AttributeError` se o objeto não for explosivo.

**Tipo:** float

### explosionForce

Impulso da explosão no centro; cai até 0 em `explosionRadius`.

**Tipo:** float

### upBias

Empurrão extra para cima (0 a 5), para os objetos voarem em vez de deslizarem no chão.

**Tipo:** float

### useOcclusion

Se a geometria estática entre a explosão e um objeto protege esse objeto.

**Tipo:** bool

### explosionEffect

Objeto de uma camada inativa adicionado no ponto da explosão (fogo, fumaça, som), ou `None`. Precisa ser um objeto do arquivo da cena.

**Tipo:** `KX_GameObject` or None

### effectLife

Segundos de vida do `explosionEffect` (0 = até a lógica dele o remover).

**Tipo:** float

### useParticleExplosion

Liga a explosão de partículas GPU embutida (núcleo, fumaça e detritos).

**Tipo:** bool

### particleSize

Tamanho da explosão de partículas: `'TINY'`, `'SMALL'`, `'MEDIUM'`, `'LARGE'` ou `'HUGE'`. Também escala a marca no chão.

**Tipo:** str

### particleStyle

Do que a explosão é feita: `'FIRE'`, `'ELECTRIC'`, `'CONCRETE'` ou `'WATER'`. Mudar o estilo volta `fireColor`, `smokeColor` e `sparkColor` para as cores do estilo.

**Tipo:** str

### fireColor

Tinta do núcleo da explosão de partículas (branco = cores naturais do estilo).

**Tipo:** Vector((r, g, b))

### smokeColor

Cor da fumaça (nuvem de poeira, névoa) quando nasce.

**Tipo:** Vector((r, g, b))

### sparkColor

Cor das faíscas (detritos, gotas).

**Tipo:** Vector((r, g, b))

### fireAmount

Quantidade de partículas do núcleo, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

### smokeAmount

Quantidade de fumaça, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

### sparkAmount

Quantidade de faíscas, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

### smokeDuration

Quanto tempo a fumaça dura, relativo ao estilo (0.2 a 4).

**Tipo:** float

### blastSpeed

Força com que as partículas são lançadas, relativa ao tamanho (0.2 a 4).

**Tipo:** float

### useGroundMark

Pinta o material de `groundMark` na superfície estática embaixo da explosão.

**Tipo:** bool

### useMarkNearby

Com `useGroundMark`: pinta também uma marca menor nos objetos em volta da explosão (os 12 mais próximos).

**Tipo:** bool

### groundMark

Objeto de malha de uma camada inativa cujo material é a marca no chão, ou `None`. Precisa ser um objeto do arquivo da cena.

**Tipo:** `KX_GameObject` or None

### markSize

Tamanho da marca no chão, relativo a `particleSize` (0.1 a 4).

**Tipo:** float

### markLife

Segundos que a marca fica no chão (0 = para sempre).

**Tipo:** float

### onBreak

Lista de funções chamadas quando este objeto quebra, com os argumentos `(object, fragments)`. Elas rodam logo depois de os fragmentos entrarem na cena, antes de qualquer explosão empurrá-los. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

```python

def on_break(obj, fragments):
    print('%s broke into %d pieces' % (obj.name, len(fragments)))

controller.owner.onBreak.append(on_break)
```

### onExplode

Lista de funções chamadas quando este objeto explode, com os argumentos `(object, position)`. Num objeto que é destrutível e explosivo ao mesmo tempo, elas rodam depois de `onBreak`. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

### onDent

Lista de funções chamadas quando este objeto deformável amassa (colisão, explosão ou `dent`), com os argumentos `(object, point, impulse)`: o ponto atingido no mundo (o centro da explosão, no caso de explosão) e a força do impacto, por exemplo para tocar um som de metal ou soltar faíscas ali. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

### endObject()

Apaga este objeto. Pode substituir o atuador End Object.

A remoção de fato do objeto da cena acontece um pouco depois.

### shatter(origin=None, burst=None)

Quebra este objeto destrutível agora, trocando-o pelos pedaços do grupo Fragments. Se o objeto também for explosivo, ele detona junto.

- **`origin`**: O ponto de onde os pedaços se afastam; por padrão, a posição do objeto.
  - tipo: 3D Vector
- **`burst`**: A velocidade dada aos pedaços para longe de origin; por padrão, o Burst Speed do painel.
  - tipo: float

**Retorna:** Os pedaços novos, ou uma lista vazia se o objeto não é destrutível ou já quebrou.

**Tipo do retorno:** list of `KX_GameObject`

### detonate()

Faz este objeto explosivo explodir agora: uma explosão como `KX_Scene.explode` com os ajustes do painel, o objeto Effect e a remoção do objeto. Um explosivo destrutível também quebra.

**Retorna:** False se o objeto não é explosivo ou já explodiu.

**Tipo do retorno:** boolean

### dent(point, direction, impulse)

Amassa este objeto deformável (painel Deformation) como um impacto da força dada: os vértices dentro do Radius do painel em volta de point andam na direção direction (para dentro do objeto) (impulse - Dent Impulse) * Depth, limitado por Max Depth. Só esta instância muda; outros objetos que usam a mesma malha mantêm a forma.

- **`point`**: Ponto atingido, no espaço do mundo.
  - tipo: 3D vector
- **`direction`**: Direção do impacto no espaço do mundo, invertida para apontar para dentro do objeto.
  - tipo: 3D vector
- **`impulse`**: Força do impacto (N*s), comparada com o Dent Impulse.
  - tipo: float

**Retorna:** False se o objeto não é deformável, se o impulso é fraco demais ou se nenhum vértice se moveu.

**Tipo do retorno:** boolean

### resetDent()

Restaura a forma de um objeto amassado.

**Retorna:** False se o objeto nunca foi amassado.

**Tipo do retorno:** boolean

### replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False)

Troca a malha deste objeto por outra. Funciona do mesmo jeito que o atuador.

- **`mesh`**: A malha nova, ou o nome dela.
  - tipo: `MeshProxy` or string
- **`useDisplayMesh`**: Se ligado, troca a malha visível (argumento opcional).
  - tipo: boolean
- **`usePhysicsMesh`**: Se ligado, troca a malha da física (argumento opcional).
  - tipo: boolean

### setVisible(visible[, recursive])

Define se o objeto está visível.

- **`visible`**: O estado de visibilidade a definir.
  - tipo: boolean
- **`recursive`**: Argumento opcional para aplicar a visibilidade também a todos os filhos. Se não for passado, vale False.
  - tipo: boolean

### setOcclusion(occlusion[, recursive])

Define se o objeto participa do occlusion culling.

- **`occlusion`**: O estado de oclusão a definir.
  - tipo: boolean
- **`recursive`**: Argumento opcional para aplicar a oclusão também a todos os filhos. Se não for passado, vale False.
  - tipo: boolean

### alignAxisToVect(vect, axis=2, factor=1.0)

Alinha um dos eixos do objeto com o vetor dado.

- **`vect`**: O vetor com o qual alinhar o eixo.
  - tipo: 3D vector
- **`axis`**: O eixo a alinhar * 0: eixo X * 1: eixo Y * 2: eixo Z
  - tipo: integer
- **`factor`**: Gira só uma fração do caminho até o vetor alvo (0.0 a 1.0).
  - tipo: float

### getAxisVect(vect)

Devolve o vetor do eixo girado pela orientação do objeto no mundo. Equivale a multiplicar o vetor pela matriz de orientação.

- **`vect`**: O vetor com o qual alinhar o eixo.
  - tipo: 3D Vector

**Retorna:** O vetor em relação à rotação do objeto.

**Tipo do retorno:** 3d vector.

### applyMovement(movement[, local])

Move o objeto.

- **`movement`**: O vetor de movimento.
  - tipo: 3D Vector
- **`local`**: * False: movimento "global", relativo à orientação do mundo. * True: movimento "local", relativo à orientação do objeto. Se não for passado, vale False.
- **`local`**: boolean

### applyRotation(rotation[, local])

Gira o objeto.

- **`rotation`**: O vetor de rotação.
  - tipo: 3D Vector
- **`local`**: * False: rotação "global", relativa à orientação do mundo. * True: rotação "local", relativa à orientação do objeto. Se não for passado, vale False.
- **`local`**: boolean

### applyForce(force[, local])

Aplica uma força ao objeto.

Exige um objeto dinâmico.

- **`force`**: O vetor de força.
  - tipo: 3D Vector
- **`local`**: * False: força "global", relativa à orientação do mundo. * True: força "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

### applyTorque(torque[, local])

Aplica um torque ao objeto.

Exige um objeto dinâmico.

- **`torque`**: O vetor de torque.
  - tipo: 3D Vector
- **`local`**: * False: torque "global", relativo à orientação do mundo. * True: torque "local", relativo à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

### getLinearVelocity([local])

Lê a velocidade linear do objeto.

Este método devolve a velocidade do objeto no centro de massa, sem a parte angular.

- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

**Retorna:** A velocidade linear do objeto.

**Tipo do retorno:** Vector((vx, vy, vz))

### setLinearVelocity(velocity[, local])

Define a velocidade linear do objeto.

Este método define a velocidade do objeto no centro de massa, sem a parte angular.

Exige um objeto dinâmico.

- **`velocity`**: O vetor de velocidade linear.
  - tipo: 3D Vector
- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

### getAngularVelocity([local])

Lê a velocidade angular do objeto.

- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

**Retorna:** A velocidade angular do objeto.

**Tipo do retorno:** Vector((vx, vy, vz))

### setAngularVelocity(velocity[, local])

Define a velocidade angular do objeto.

Exige um objeto dinâmico.

- **`velocity`**: O vetor de velocidade angular.
  - tipo: boolean
- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.

### getVelocity([point])

Lê a velocidade do objeto no ponto indicado.

Lê a velocidade do objeto no ponto indicado, incluindo a parte angular.

- **`point`**: Ponto opcional onde medir a velocidade, em coordenadas locais. Se não for passado, vale (0, 0, 0).
  - tipo: 3D Vector

**Retorna:** A velocidade no ponto indicado.

**Tipo do retorno:** Vector((vx, vy, vz))

### getReactionForce()

Lê a força de reação do objeto.

A força de reação é a força aplicada a este objeto no último passo da simulação. Inclui também impulsos, como os de colisões.

**Retorna:** A força de reação deste objeto.

**Tipo do retorno:** Vector((fx, fy, fz))

:::note
Isto ainda não está implementado.
:::

### applyImpulse(point, impulse[, local])

Aplica um impulso ao objeto.

Aplica o impulso dado ao objeto no ponto indicado. Se point for diferente da posição, applyImpulse também muda o momento angular do objeto; caso contrário, só o momento linear muda.

- **`point`**: O ponto onde aplicar o impulso (em coordenadas do mundo ou locais).
  - tipo: point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
- **`impulse`**: O vetor de impulso.
  - tipo: 3D Vector
- **`local`**: * False: impulso "global", relativo às coordenadas e à orientação do mundo. * True: impulso "local", relativo às coordenadas e à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

### setDamping(linear_damping, angular_damping)

Define `linearDamping` e `angularDamping` de uma vez. É mais eficiente do que definir cada um separadamente.

- **`linear_damping`**: Fator de amortecimento linear (de translação).
  - tipo: float ∈ [0, 1]
- **`angular_damping`**: Fator de amortecimento angular (de rotação).
  - tipo: float ∈ [0, 1]

### suspendPhysics([freeConstraints])

Suspende a física deste objeto.

- **`freeConstraints`**: Se for `True`, as constraints de física usadas pelo objeto são apagadas. Se for `False` (o padrão), as constraints voltam quando a física é restaurada.
  - tipo: bool

### restorePhysics()

Retoma a física deste objeto e volta a ligar as colisões.

### suspendDynamics([ghost])

Suspende a física dinâmica deste objeto.

- **`ghost`**: Se for `True`, as colisões com o objeto são ignoradas, como a opção "ghost" do Blender. Se for `False` (o padrão), o objeto fica estático mas continua colidindo com os outros.
  - tipo: bool

:::tip
`isSuspendDynamics` mostra se o objeto está suspenso.
:::

### restoreDynamics()

Retoma a física dinâmica deste objeto e volta a ligar as colisões; o objeto deixa de ser ghost.

:::note
O objeto volta com a velocidade linear que tinha quando a dinâmica foi suspensa.
:::

### enableRigidBody()

Liga a física de corpo rígido deste objeto.

Com a física de corpo rígido, o objeto rola ao colidir.

### disableRigidBody()

Desliga a física de corpo rígido deste objeto.

### setParent(parent, compound=True, ghost=True)

Define o pai deste objeto. Os parâmetros opcionais compound e ghost controlam a forma de colisão:

Nesse caso, dá para escolher se ele fica ghost ou não:

- **`parent`**: O novo objeto pai.
  - tipo: `KX_GameObject`
- **`compound`**: Se a forma deve ser somada à forma composta do pai. * True: a forma do objeto entra na forma composta do pai. * False: o objeto mantém a própria forma.
  - tipo: boolean
- **`ghost`**: Se o objeto deve ficar ghost enquanto tiver pai. * True: fica ghost enquanto tiver pai. * False: continua sólido enquanto tiver pai.
  - tipo: boolean

:::note
Se o objeto for do tipo sensor, ele continua ghost, seja qual for o parâmetro ghost.
:::

### removeParent()

Remove o pai deste objeto.

### getPhysicsId()

Devolve o objeto de dados do usuário ligado ao controlador de física deste objeto.

### getPropertyNames()

Lê a lista com os nomes de todas as propriedades.

**Retorna:** Os nomes de todas as propriedades deste objeto.

**Tipo do retorno:** list

### getDistanceTo(other)

- **`other`**: Um ponto ou outro `KX_GameObject` até onde medir a distância.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** A distância até o outro objeto ou ponto.

**Tipo do retorno:** float

### getVectTo(other)

Devolve o vetor e a distância até outro objeto ou ponto. O vetor vem normalizado, a não ser que a distância seja 0; nesse caso, vem um vetor de tamanho zero.

- **`other`**: Um ponto ou outro `KX_GameObject` até onde calcular o vetor e a distância.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** (distância, vetorGlobal(3), vetorLocal(3))

**Tipo do retorno:** 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))

### rayCastTo(other, dist=0, prop="")

Olha na direção de outro ponto ou objeto e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop.

O raio sempre sai do centro do objeto, ignorando o próprio objeto. Ele vai até o centro de outro objeto ou até um ponto [x, y, z]. Use rayCast() se precisar do ponto atingido.

- **`other`**: [x, y, z] ou objeto na direção do qual o raio é lançado
  - tipo: `KX_GameObject` or 3-tuple
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`prop`**: Nome da propriedade que o objeto precisa ter; se omitido, detecta qualquer objeto
  - tipo: string

**Retorna:** O primeiro objeto atingido, ou None se não atingir nada ou se o objeto não tiver a propriedade

**Tipo do retorno:** `KX_GameObject`

### rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF)

Olha de um ponto ou objeto até outro e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop. Se poly for 0, devolve uma tupla de 3 com o objeto, o ponto e a normal atingidos, ou (None, None, None) se não atingir nada. Se poly for 1, devolve uma tupla de 4 com um `KX_PolyProxy` como 4º elemento. Se poly for 2, devolve uma tupla de 5 com um vetor 2D com a coordenada UV do ponto atingido como 5º elemento.

```python

# atira ao longo do eixo gun-gunAim (gunAim não deve ter colisão)
obj, point, normal = gun.rayCast(gunAim, None, 50)
if obj:
   # faz alguma coisa
   pass
```

O parâmetro face define a orientação da normal.

* 0 => a normal sempre aponta para a origem do raio (como se o raio viesse de fora)
* 1 => a normal é a normal real da face (só para malhas; nos outros casos face não tem efeito)

Se xray for 1, o raio atravessa objetos (raio X); caso contrário, o primeiro objeto atingido (fora o próprio) para o raio. Os parâmetros prop e xray funcionam juntos assim:

* prop desligado, xray desligado: devolve o acerto mais próximo, ou nada se não houver objeto em todo o comprimento do raio.
* prop desligado, xray ligado: o mesmo.
* prop ligado, xray desligado: devolve o acerto mais próximo se ele tiver prop; caso contrário, nada.
* prop ligado, xray ligado: devolve o acerto mais próximo que tenha prop, ou nada se nenhum objeto com prop estiver em todo o comprimento do raio.

O `KX_PolyProxy` que vem como 4º elemento quando poly=1 dá informações sobre o polígono atingido. Se não atingir nada, ou se o objeto atingido não for uma malha estática, o 4º elemento é None.

O raio ignora objetos sem colisão e faces sem a opção de colisão, mas pode atingir objetos ghost.

- **`objto`**: [x, y, z] ou objeto até onde o raio é lançado
  - tipo: `KX_GameObject` or 3-tuple
- **`objfrom`**: [x, y, z] ou objeto de onde o raio sai; None ou omitido usa o centro do próprio objeto
  - tipo: `KX_GameObject` or 3-tuple or None
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`prop`**: Nome da propriedade que o objeto precisa ter; omitido ou "" detecta qualquer objeto
  - tipo: string
- **`face`**: Opção de normal: 1 devolve a normal da face; 0 ou omitido aponta a normal para a origem
  - tipo: integer
- **`xray`**: Opção de raio X: 1 pula os objetos que não têm prop; 0 ou omitido para no primeiro objeto
  - tipo: integer
- **`poly`**: Opção de polígono: 0, 1 ou 2 para devolver uma tupla de 3, 4 ou 5 com dados da face atingida. * 0 ou omitido: tupla de 3 (object, hitpoint, hitnormal), ou (None, None, None) se não atingir nada. * 1: tupla de 4, com um `KX_PolyProxy` como 4º elemento, ou None se não atingir nada ou se o objeto não usar forma de colisão de malha. * 2: tupla de 5, com uma tupla (u, v) da coordenada UV do ponto atingido como 5º elemento, ou None se não atingir nada, se o objeto não usar forma de colisão de malha ou não tiver mapeamento UV.
  - tipo: integer
- **`mask`**: Máscara de colisão: a máscara (16 camadas num inteiro de 16 bits) é combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só podem ser atingidos os objetos em que `collisionGroup & mask` for verdadeiro.
  - tipo: bitfield

**Retorna:** (object, hitpoint, hitnormal), ou (object, hitpoint, hitnormal, polygon), ou (object, hitpoint, hitnormal, polygon, hituv). * object, hitpoint e hitnormal são None se não atingir nada. * polygon só é válido se o objeto for válido e for estático, dinâmico com forma de colisão de malha ou soft body; senão é None. * hituv só é válido se polygon for válido e o objeto tiver mapeamento UV; senão é None.

**Tipo do retorno:**  * 3-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz)) * or 4-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`) * or 5-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`, 2-tuple (u, v))

:::note
O raio ignora o objeto que chamou o método. Ele sai do centro do objeto, ou vai até ele, ou usa pontos [x, y, z].
:::

### collide(obj)

Testa se este objeto colide com o objeto `obj`.

- **`obj`**: O objeto com o qual testar a colisão
  - tipo: string or `KX_GameObject`

**Retorna:** (collide, points) * collide: True se este objeto colide com `obj` * points: os pontos de contato da colisão, ou None

**Tipo do retorno:** 2-tuple (boolean, list of `KX_CollisionContactPoint` or None)

### setCollisionMargin(margin)

Define a margem de colisão do objeto.

- **`margin`**: A distância da margem de colisão, em unidades do Blender.
  - tipo: float

:::note
Se este objeto não tiver controlador de física (ID de física zero), esta função gera RuntimeError.
:::

### sendMessage(subject, body="", to="")

Envia uma mensagem.

- **`subject`**: O assunto da mensagem
  - tipo: string
- **`body`**: O corpo da mensagem (opcional)
  - tipo: string
- **`to`**: O nome do objeto que vai receber a mensagem (opcional)
  - tipo: string

### reinstancePhysicsMesh(gameObject, meshObject, dupli)

Atualiza a física com a malha alterada.

Sem argumentos, a malha da física é recriada a partir da primeira malha do objeto.

- **`gameObject`**: Argumento opcional: cria a forma de física a partir da malha deste objeto.
  - tipo: string, `KX_GameObject` or None
- **`meshObject`**: Argumento opcional: cria a forma de física a partir desta malha.
  - tipo: string, `MeshProxy` or None
- **`dupli`**: Argumento opcional: duplica a forma de física.
  - tipo: boolean

**Retorna:** True se a recriação deu certo, False se falhou.

**Tipo do retorno:** boolean

:::note
Se este objeto tiver instâncias, elas também são atualizadas.
:::

:::note
O argumento gameObject tem a vantagem de converter a malha com os modificadores aplicados (como o Subdivision Surface).
:::

:::caution
Por enquanto, só objetos com malha de triângulos ou convex hull são suportados.
:::

:::caution
Falha se o objeto fizer parte de um objeto composto (pai ou filho).
:::

:::caution
Recriar a malha da física pode ser lento; rodar isso muitas vezes por segundo pesa no desempenho.
:::

:::caution
Duplicar a malha da física pode gastar bem mais memória; use esta opção só em malhas duplicadas, senão use `replacePhysicsShape`.
:::

### replacePhysicsShape(gameObject)

Troca a forma de física atual.

- **`gameObject`**: Cria a forma de física a partir deste objeto.
  - tipo: string, `KX_GameObject`

**Retorna:** True se a troca deu certo, False se falhou.

**Tipo do retorno:** boolean

:::caution
Formas de malha de triângulos não são suportadas.
:::

### get(key[, default])

Devolve o valor da chave, ou o valor padrão se a chave não existir.
- **`key`**: A chave procurada
  - tipo: string
- **`default`**: Valor padrão opcional se a chave não existir; se não for passado, vale None.

**Retorna:** O valor da chave ou o padrão.

### playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=KX_ACTION_BLEND_BLEND)

Toca uma ação.

- **`name`**: O nome da ação
  - tipo: string
- **`start`**: O frame inicial da ação
  - tipo: float
- **`end`**: O frame final da ação
  - tipo: float
- **`layer`**: A camada onde a ação vai tocar (ações em camadas diferentes são somadas/misturadas)
  - tipo: integer
- **`priority`**: Só toca esta ação se não houver outra tocando nesta camada com prioridade maior (número menor)
  - tipo: integer
- **`blendin`**: Quanto misturar esta animação com a anterior nesta camada
  - tipo: float
- **`play_mode`**: O modo de reprodução
  - tipo: one of `these constants`
- **`layer_weight`**: Quanto da camada anterior usar na mistura
  - tipo: float
- **`ipo_flags`**: Flags dos comportamentos antigos de IPO (force etc.)
  - tipo: int bitfield
- **`speed`**: A velocidade da ação como fator (1.0 = normal, 2.0 = o dobro etc.)
  - tipo: float
- **`blend_mode`**: Como misturar esta camada com as anteriores
  - tipo: one of `these constants`

### stopAction([layer])

Para a ação que está tocando na camada indicada.

- **`layer`**: A camada a parar; se não for passada, vale 0.
  - tipo: integer

### getActionFrame([layer])

Lê o frame atual da ação que está tocando na camada indicada.

- **`layer`**: A camada de onde ler o frame; se não for passada, vale 0.
  - tipo: integer

**Retorna:** O frame atual da ação

**Tipo do retorno:** float

### getActionName([layer])

Lê o nome da ação que está tocando na camada indicada.

- **`layer`**: A camada de onde ler o nome da ação; se não for passada, vale 0.
  - tipo: integer

**Retorna:** O nome da ação atual

**Tipo do retorno:** string

### setActionFrame(frame[, layer])

Define o frame atual da ação que está tocando na camada indicada.

- **`layer`**: A camada onde definir o frame; se não for passada, vale 0.
  - tipo: integer
- **`frame`**: O frame para onde levar a ação
  - tipo: float

### isPlayingAction([layer])

Verifica se há uma ação tocando na camada indicada.

- **`layer`**: A camada a verificar; se não for passada, vale 0.
  - tipo: integer

**Retorna:** Se a ação está tocando ou não

**Tipo do retorno:** boolean

### addDebugProperty (name[, debug])

Adiciona uma propriedade à lista de depuração.

- **`name`**: O nome da propriedade a adicionar à lista de depuração.
  - tipo: string
- **`debug`**: O estado de depuração; se não for passado, vale True.
  - tipo: boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getCurvePoints()

 <small>método</small>

`getCurvePoints(world=True)`: pontos da primeira spline de um objeto Curve, como lista de `Vector`. Coordenadas do mundo por padrão; `world=False` devolve em coordenadas locais. Lista vazia se o objeto não for uma curva.

### getTurnTo(other)

 <small>método</small>

Vetor local deste objeto até outro objeto ou ponto. Útil para saber para que lado virar.

**Retorna:** `Vector`

### getVehicle()

 <small>método</small>

O veículo criado pelo painel Vehicle deste objeto, ou `None`.

**Retorna:** `KX_VehicleWrapper`

### getVehicleGearboxType()

 <small>método</small>

Tipo de câmbio configurado no painel Vehicle.

**Retorna:** `int`

### getVehicleGearRatios()

 <small>método</small>

Relações das marchas configuradas no painel Vehicle.

**Retorna:** `tuple`

### getVehicleMaxRPM()

 <small>método</small>

Rotação máxima do motor configurada no painel Vehicle.

**Retorna:** `float`

### getVehicleMaxTorque()

 <small>método</small>

Torque máximo do motor configurado no painel Vehicle.

**Retorna:** `float`

### getVehicleSteeringWheel()

 <small>método</small>

Objeto do volante configurado no painel Vehicle, ou `None`.

**Retorna:** `KX_GameObject`

### lookAt(vect, axis=2, factor=1.0)

 <small>método</small>

Vira o objeto para que o eixo `axis` (0=X, 1=Y, 2=Z) aponte na direção `vect`. `factor` abaixo de 1 vira só uma parte (suaviza).

### resumeAnimations()

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

Retoma as animações pausadas por `suspendAnimations()`.

### setActionLayerSpeed(layer, speed)

 <small>método</small>

Muda a velocidade da ação que toca na camada `layer`.

### setActionLayerWeight(layer, layerWeight)

 <small>método</small>

Muda o peso (0 a 1) da camada de animação `layer`.

### setCcdMotionThreshold(threshold)

 <small>método</small>

Velocidade a partir da qual a detecção contínua de colisão (CCD) entra, evitando que objetos rápidos atravessem paredes.

### setCcdSweptSphereRadius(radius)

 <small>método</small>

Raio da esfera usada pela detecção contínua de colisão (CCD).

### setHalfAnimations(enabled)

 <small>método</small>

Com `True`, atualiza as animações do objeto em frames alternados, para economizar CPU.

### setSoftAnchorsHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez das âncoras.

### setSoftAngularStiffness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez angular.

### setSoftClusterSolverIterations(iterations)

 <small>método</small>

Física de corpo mole (soft body): iterações do solver de clusters.

### setSoftContactsHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez dos contatos.

### setSoftDampingCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): amortecimento.

### setSoftDragCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): arrasto do ar.

### setSoftDriftSolverIterations(iterations)

 <small>método</small>

Física de corpo mole (soft body): iterações do solver de deriva.

### setSoftDynamicFrictionCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): atrito dinâmico.

### setSoftKineticContactsHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez do contato com objetos cinemáticos.

### setSoftLiftCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): sustentação (lift).

### setSoftLinearStiffness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez linear.

### setSoftPoseMatching(enabled)

 <small>método</small>

Física de corpo mole (soft body): liga a tentativa de voltar à forma original.

### setSoftPoseMatchingCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): força com que volta à forma original.

### setSoftPositionSolverIterations(iterations)

 <small>método</small>

Física de corpo mole (soft body): iterações do solver de posição.

### setSoftPressureCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): pressão interna (efeito balão).

### setSoftRigidContactsHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez do contato com corpos rígidos.

### setSoftVelocitiesCorrectionFactor(value)

 <small>método</small>

Física de corpo mole (soft body): fator de correção das velocidades.

### setSoftVelocitySolverIterations(iterations)

 <small>método</small>

Física de corpo mole (soft body): iterações do solver de velocidade.

### setSoftVolume(volume)

 <small>método</small>

Física de corpo mole (soft body): volume que o corpo tenta manter.

### setSoftVolumeConversationCoefficient(value)

 <small>método</small>

Física de corpo mole (soft body): conservação de volume.

### setSoftVsKineticHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez contra corpos cinemáticos (clusters).

### setSoftVsKineticImpulseSplitCluster(value)

 <small>método</small>

Física de corpo mole (soft body): divisão de impulso contra corpos cinemáticos (clusters).

### setSoftVsRigidHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez contra corpos rígidos (clusters).

### setSoftVsRigidImpulseSplitCluster(value)

 <small>método</small>

Física de corpo mole (soft body): divisão de impulso contra corpos rígidos (clusters).

### setSoftVsSoftHardness(value)

 <small>método</small>

Física de corpo mole (soft body): rigidez contra outros corpos moles (clusters).

### setSoftVsSoftImpulseSplitCluster(value)

 <small>método</small>

Física de corpo mole (soft body): divisão de impulso contra outros corpos moles (clusters).

### strikeLightning(bolt=True)

 <small>método</small>

um raio cai agora (a chuva precisa estar ligada)

### suspendAnimations()

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

Pausa todas as animações do objeto até `resumeAnimations()`.

### activitycullingdistance

 <small>atributo · só leitura</small>

Distância deste objeto até a câmera calculada pelo Activity Culling.

### angularVelocity

 <small>atributo</small>

Velocidade angular. Lê em coordenadas locais e escreve em coordenadas do mundo.

### animationEventManager

 <small>atributo · só leitura</small>

Gerenciador dos eventos de animação do objeto (`KX_AnimationEventManager`).

### anisotropicFriction

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga o atrito diferente por eixo (anisotrópico).

### anisotropicFrictionCoefficients

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Atrito `[x, y, z]` em cada eixo quando `anisotropicFriction` está ligado.

### bendAngle

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Quanto o objeto entorta a cada impacto.

### bendAxis

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Eixo em que o objeto entorta: `'X'`, `'Y'` ou `'Z'`.

### bendMaxAngle

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Ângulo máximo que o objeto pode entortar.

### burstSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Velocidade com que os fragmentos saem quando o objeto quebra.

### debrisLifetime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tempo de vida dos fragmentos depois da quebra.

### decal

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Objeto usado como decalque de arranhão nas colisões, ou `None`. Precisa ser um objeto do arquivo da cena.

### decalLife

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tempo de vida de cada decalque.

### decalSize

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tamanho dos decalques.

### dentImpulse

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Impulso mínimo de colisão para amassar o objeto.

### fragments

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nome do grupo com os fragmentos usados quando o objeto quebra, ou `None`. Só em objetos destrutíveis; senão levanta `AttributeError`.

### hiddenFromCamera

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Câmera que não deve mostrar este objeto (ex.: o próprio carro no split screen), ou `None`.

### impactImpulse

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Impulso mínimo de colisão para um objeto explosivo detonar.

### isDeformable

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

`True` se o objeto tem as configurações de deformação ligadas (amassar, entortar, decalques).

### linearVelocity

 <small>atributo</small>

Velocidade linear. Lê em coordenadas locais e escreve em coordenadas do mundo.

### maxDecals

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Número máximo de decalques ao mesmo tempo neste objeto.

### parentRecursive

 <small>atributo · só leitura</small>

Lista de todos os pais acima do objeto, do mais próximo ao mais distante.

### particles

 <small>atributo · só leitura</small>

Sistema de partículas do objeto (`KX_ParticleSystem`), ou `None`.

### particlesMix

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Segundo sistema de partículas (mistura) do objeto, ou `None`.

### passIndex

 <small>atributo</small>

Pass Index do objeto, usado para separar objetos em filtros e efeitos.

### useBreakOnCollision

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se o objeto quebra ao colidir.

### useChainReaction

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se a explosão deste objeto detona outros explosivos por perto.

### useDentOnCollision

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se o objeto amassa ao colidir.

### useExplodeOnImpact

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se o objeto explosivo detona ao sofrer um impacto acima de `impactImpulse`.

### useInheritVelocity

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se os fragmentos herdam a velocidade do objeto ao quebrar.

