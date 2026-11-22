# KX_GameObject - atributos

Parte de [KX_GameObject](KX_GameObject.md).

## name

O nome do objeto.

**Tipo:** string

## mass

A massa do objeto.

**Tipo:** float

> **Note:**
O objeto precisa de um controlador de física para a massa valer; sem ele, a massa é lida como 0.0.

## friction

O atrito do objeto.

**Tipo:** float

## isSuspendDynamics

O estado dinâmico do objeto (somente leitura).

**Tipo:** boolean

> **Tip:**
`suspendDynamics` e `restoreDynamics` permitem mudar esse estado.

## linearDamping

O amortecimento linear do objeto, também chamado de amortecimento de translação. Pode ser definido junto com o amortecimento angular pelo método `setDamping`.

**Tipo:** float between 0 and 1 inclusive.

> **Note:**
O objeto precisa de um controlador de física para o amortecimento linear valer; sem ele, o valor é lido como 0.0.

## angularDamping

O amortecimento angular do objeto, também chamado de amortecimento de rotação. Pode ser definido junto com o amortecimento linear pelo método `setDamping`.

**Tipo:** float between 0 and 1 inclusive.

> **Note:**
O objeto precisa de um controlador de física para o amortecimento angular valer; sem ele, o valor é lido como 0.0.

## linVelocityMin

Obriga o objeto a continuar se movendo com uma velocidade mínima.

**Tipo:** float

> **Note:**
Vale só para objetos dinâmicos e rígidos.

> **Note:**
O valor 0.0 desliga esta opção.

> **Note:**
Enquanto o objeto está parado, a velocidade mínima não é aplicada.

## linVelocityMax

Limita a velocidade linear máxima, para o objeto não passar de uma certa velocidade.

**Tipo:** float

> **Note:**
Vale só para objetos dinâmicos e rígidos.

> **Note:**
O valor 0.0 desliga esta opção (não deixa o objeto parado).

## angularVelocityMin

Obriga o objeto a continuar girando com uma velocidade mínima. O valor 0.0 desliga.

**Tipo:** non-negative float

> **Note:**
Vale só para objetos dinâmicos e rígidos. Enquanto o objeto está parado, a velocidade mínima não é aplicada.

## angularVelocityMax

Limita a velocidade angular máxima, para o objeto não girar além de uma certa velocidade. O valor 0.0 desliga o limite; não para a rotação.

**Tipo:** non-negative float

> **Note:**
Vale só para objetos dinâmicos e rígidos.

## localInertia

O vetor de inércia do objeto em coordenadas locais. Somente leitura.

**Tipo:** Vector((ix, iy, iz))

## parent

O objeto pai deste objeto (somente leitura).

**Tipo:** `KX_GameObject` or None

## groupMembers

Devolve a lista de membros do grupo se o objeto for um objeto de grupo (instância de dupli group); caso contrário, devolve None.

**Tipo:** `EXP_ListValue` of `KX_GameObject` or None

## groupObject

Devolve o objeto de grupo (instância de dupli group) a que o objeto pertence, ou None se ele não faz parte de um grupo.

**Tipo:** `KX_GameObject` or None

## collisionGroup

O grupo de colisão do objeto.

**Tipo:** bitfield

## collisionMask

A máscara de colisão do objeto.

**Tipo:** bitfield

## collisionCallbacks

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

> **Note:**
Por compatibilidade, uma função com número variável de argumentos (usando `*args`) recebe só o argumento `object`. A forma com quatro argumentos só é usada quando há mais de um argumento fixo (sem contar o `self` dos métodos).

## scene

A cena do objeto (somente leitura).

**Tipo:** `KX_Scene` or None

## visible

Indica se o objeto está visível.

**Tipo:** boolean

> **Note:**
A lógica do jogo continua rodando para objetos invisíveis.

## layer

A máscara de camadas usada no render de sombras e de cube maps em tempo real.

**Tipo:** bitfield

## cullingBox

A caixa de volume do objeto, usada no culling.

**Tipo:** `KX_BoundingBox`

## culled

Devolve True se o objeto foi descartado pelo culling; caso contrário, False.

> **Caution:**
Esta variável devolve um valor inválido se for lida fora dos callbacks da cena `KX_Scene.pre_draw` e `KX_Scene.post_draw`.

**Tipo:** boolean (read only)

## color

A cor do objeto. [r, g, b, a]

**Tipo:** `mathutils.Vector`

## occlusion

Indica se o objeto participa do occlusion culling.

**Tipo:** boolean

## physicsCulling

True se o objeto suspende a física conforme a distância até a câmera mais próxima.

**Tipo:** boolean

## physicsCullingVelocity

Para a física depois que o objeto para.

**Tipo:** boolean

## logicCulling

True se o objeto suspende a lógica e a animação conforme a distância até a câmera mais próxima.

**Tipo:** boolean

## logicCullingComponents

Não suspende a execução dos componentes do objeto.

**Tipo:** boolean

## physicsCullingRadius

Suspende a física do objeto se este raio for menor que a distância até a câmera mais próxima e `physicsCulling` estiver `True`.

**Tipo:** float

## logicCullingRadius

Suspende a lógica e a animação do objeto se este raio for menor que a distância até a câmera mais próxima e `logicCulling` estiver `True`.

**Tipo:** float

## ~~position~~

A posição do objeto. [x, y, z] Na escrita: posição local; na leitura: posição no mundo.

> **Obsoleto use :data:`localPosition` and :data:`worldPosition`.:**

**Tipo:** `mathutils.Vector`

## ~~orientation~~

A orientação do objeto. Matriz 3x3. Também aceita um Quaternion ou um vetor Euler. Na escrita: orientação local; na leitura: orientação no mundo.

> **Obsoleto use :data:`localOrientation` and :data:`worldOrientation`.:**

**Tipo:** `mathutils.Matrix`

## ~~scaling~~

O fator de escala do objeto. [sx, sy, sz] Na escrita: escala local; na leitura: escala no mundo.

> **Obsoleto use :data:`localScale` and :data:`worldScale`.:**

**Tipo:** `mathutils.Vector`

## localOrientation

A orientação local do objeto. Matriz 3x3. Também aceita um Quaternion ou um vetor Euler.

**Tipo:** `mathutils.Matrix`

## worldOrientation

A orientação do objeto no mundo. Matriz 3x3.

**Tipo:** `mathutils.Matrix`

## localScale

O fator de escala local do objeto. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

## worldScale

O fator de escala do objeto no mundo. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

## localPosition

A posição local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

## worldPosition

A posição do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

## localTransform

A matriz de transformação local do objeto. Matriz 4x4.

**Tipo:** `mathutils.Matrix`

## worldTransform

A matriz de transformação do objeto no mundo. Matriz 4x4.

**Tipo:** `mathutils.Matrix`

## localLinearVelocity

A velocidade linear local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

## worldLinearVelocity

A velocidade linear do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

## localAngularVelocity

A velocidade angular local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

## worldAngularVelocity

A velocidade angular do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

## gravity

A gravidade do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

## timeOffset

Ajusta o atraso do slow parent durante o jogo.

**Tipo:** float

## state

A máscara de estados do objeto, usando os 30 primeiros bits; pelo menos um bit precisa estar ligado.

**Tipo:** int

## meshes

Lista das malhas deste objeto.

**Tipo:** list of `KX_Mesh`

> **Note:**
A maioria dos objetos usa só 1 malha.

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

## batchGroup

O grupo de batch que contém a malha agrupada do objeto.

**Tipo:** `KX_BatchGroup`

## sensors

Uma sequência de objetos `SCA_ISensor`, com busca por nome/índice e suporte a iteração.

**Tipo:** list

> **Note:**
Este atributo é experimental e pode ser removido (mas provavelmente não será).

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

## controllers

Uma sequência de objetos `SCA_IController`, com busca por nome/índice e suporte a iteração.

**Tipo:** list of `SCA_ISensor`

> **Note:**
Este atributo é experimental e pode ser removido (mas provavelmente não será).

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

## actuators

Uma lista de `SCA_IActuator`, com busca por nome/índice e suporte a iteração.

**Tipo:** list

> **Note:**
Este atributo é experimental e pode ser removido (mas provavelmente não será).

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

## attrDict

Dá o dicionário interno de atributos Python do objeto, para acesso direto (mais rápido).

**Tipo:** dict

## components

Todos os componentes Python.

**Tipo:** `EXP_ListValue` of `KX_PythonComponent`'s

## children

Os filhos diretos deste objeto (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

## childrenRecursive

Todos os filhos deste objeto, incluindo os filhos dos filhos (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

## life

Quantos frames faltam para o objeto acabar, considerando um frame como 1/50 de segundo (somente leitura).

**Tipo:** float

## debug

Se for True, as propriedades de depuração do objeto aparecem na tela.

**Tipo:** boolean

## debugRecursive

Se for True, as propriedades de depuração do objeto e dos filhos aparecem na tela.

**Tipo:** boolean

## currentLodLevel

O índice do nível de detalhe (LOD) que o objeto está usando agora (somente leitura).

**Tipo:** int

## lodLevelMax

Maior índice de nível de detalhe (LOD) para o qual o objeto pode trocar; -1 (padrão) significa sem limite. Enquanto estiver definido, os níveis mais distantes são pulados; por exemplo, um personagem em ragdoll fica num nível com malha em vez do cartão de impostor sentado.

**Tipo:** int (-1 to 255)

## lodManager

Devolve o gerenciador de LOD do objeto, necessário para configurar os níveis de detalhe dele. O gerenciador é compartilhado entre as instâncias e pode ser trocado para usar os níveis de LOD de outro objeto. Se for definido como `None`, a malha do objeto volta a ser a do primeiro nível de LOD anterior.

**Tipo:** `KX_LodManager`

## isDestructible

True se Physics > Destruction estiver ligado neste objeto, inclusive em objetos de camadas inativas (somente leitura).

**Tipo:** boolean

## isExplosive

True se Physics > Explosive estiver ligado neste objeto, inclusive em objetos de camadas inativas (somente leitura).

**Tipo:** boolean

## breakImpulse

O impulso que quebra este objeto destrutível, vindo de uma colisão ou de `KX_Scene.explode`. Começa com o Break Impulse do painel; mudar o valor afeta só esta instância. Em objetos que não são destrutíveis, lê 0.0, e escrever gera AttributeError.

**Tipo:** float

## fuse

Segundos que faltam para este objeto explosivo detonar. O pavio conta a partir do momento em que o objeto entra no jogo (início da cena ou `KX_Scene.addObject`). 0.0 significa sem pavio; definir um valor acende o pavio. Em objetos que não são explosivos, escrever gera AttributeError.

**Tipo:** float

## explosionRadius

Raio da explosão deste objeto explosivo, em metros. Como todos os atributos do painel Explosive abaixo, levanta `AttributeError` se o objeto não for explosivo.

**Tipo:** float

## explosionForce

Impulso da explosão no centro; cai até 0 em `explosionRadius`.

**Tipo:** float

## upBias

Empurrão extra para cima (0 a 5), para os objetos voarem em vez de deslizarem no chão.

**Tipo:** float

## useOcclusion

Se a geometria estática entre a explosão e um objeto protege esse objeto.

**Tipo:** bool

## explosionEffect

Objeto de uma camada inativa adicionado no ponto da explosão (fogo, fumaça, som), ou `None`. Precisa ser um objeto do arquivo da cena.

**Tipo:** `KX_GameObject` or None

## effectLife

Segundos de vida do `explosionEffect` (0 = até a lógica dele o remover).

**Tipo:** float

## useParticleExplosion

Liga a explosão de partículas GPU embutida (núcleo, fumaça e detritos).

**Tipo:** bool

## particleSize

Tamanho da explosão de partículas: `'TINY'`, `'SMALL'`, `'MEDIUM'`, `'LARGE'` ou `'HUGE'`. Também escala a marca no chão.

**Tipo:** str

## particleStyle

Do que a explosão é feita: `'FIRE'`, `'ELECTRIC'`, `'CONCRETE'` ou `'WATER'`. Mudar o estilo volta `fireColor`, `smokeColor` e `sparkColor` para as cores do estilo.

**Tipo:** str

## fireColor

Tinta do núcleo da explosão de partículas (branco = cores naturais do estilo).

**Tipo:** Vector((r, g, b))

## smokeColor

Cor da fumaça (nuvem de poeira, névoa) quando nasce.

**Tipo:** Vector((r, g, b))

## sparkColor

Cor das faíscas (detritos, gotas).

**Tipo:** Vector((r, g, b))

## fireAmount

Quantidade de partículas do núcleo, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

## smokeAmount

Quantidade de fumaça, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

## sparkAmount

Quantidade de faíscas, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

## smokeDuration

Quanto tempo a fumaça dura, relativo ao estilo (0.2 a 4).

**Tipo:** float

## blastSpeed

Força com que as partículas são lançadas, relativa ao tamanho (0.2 a 4).

**Tipo:** float

## useGroundMark

Pinta o material de `groundMark` na superfície estática embaixo da explosão.

**Tipo:** bool

## useMarkNearby

Com `useGroundMark`: pinta também uma marca menor nos objetos em volta da explosão (os 12 mais próximos).

**Tipo:** bool

## groundMark

Objeto de malha de uma camada inativa cujo material é a marca no chão, ou `None`. Precisa ser um objeto do arquivo da cena.

**Tipo:** `KX_GameObject` or None

## markSize

Tamanho da marca no chão, relativo a `particleSize` (0.1 a 4).

**Tipo:** float

## markLife

Segundos que a marca fica no chão (0 = para sempre).

**Tipo:** float

## onBreak

Lista de funções chamadas quando este objeto quebra, com os argumentos `(object, fragments)`. Elas rodam logo depois de os fragmentos entrarem na cena, antes de qualquer explosão empurrá-los. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

```python

def on_break(obj, fragments):
    print('%s broke into %d pieces' % (obj.name, len(fragments)))

controller.owner.onBreak.append(on_break)
```

## onExplode

Lista de funções chamadas quando este objeto explode, com os argumentos `(object, position)`. Num objeto que é destrutível e explosivo ao mesmo tempo, elas rodam depois de `onBreak`. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

## onDent

Lista de funções chamadas quando este objeto deformável amassa (colisão, explosão ou `dent`), com os argumentos `(object, point, impulse)`: o ponto atingido no mundo (o centro da explosão, no caso de explosão) e a força do impacto, por exemplo para tocar um som de metal ou soltar faíscas ali. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

## activitycullingdistance

*(novo na Anastacio)* `atributo · só leitura`

Distância deste objeto até a câmera calculada pelo Activity Culling.

## angularVelocity

*(novo na Anastacio)* `atributo`

Velocidade angular. Lê em coordenadas locais e escreve em coordenadas do mundo.

## animationEventManager

*(novo na Anastacio)* `atributo · só leitura`

Gerenciador dos eventos de animação do objeto (`KX_AnimationEventManager`).

## anisotropicFriction

*(novo na Anastacio)* `atributo`

Liga o atrito diferente por eixo (anisotrópico).

## anisotropicFrictionCoefficients

*(novo na Anastacio)* `atributo`

Atrito `[x, y, z]` em cada eixo quando `anisotropicFriction` está ligado.

## bendAngle

*(novo na Anastacio)* `atributo`

Quanto o objeto entorta a cada impacto.

## bendAxis

*(novo na Anastacio)* `atributo`

Eixo em que o objeto entorta: `'X'`, `'Y'` ou `'Z'`.

## bendMaxAngle

*(novo na Anastacio)* `atributo`

Ângulo máximo que o objeto pode entortar.

## burstSpeed

*(novo na Anastacio)* `atributo`

Velocidade com que os fragmentos saem quando o objeto quebra.

## debrisLifetime

*(novo na Anastacio)* `atributo`

Tempo de vida dos fragmentos depois da quebra.

## decal

*(novo na Anastacio)* `atributo`

Objeto usado como decalque de arranhão nas colisões, ou `None`. Precisa ser um objeto do arquivo da cena.

## decalLife

*(novo na Anastacio)* `atributo`

Tempo de vida de cada decalque.

## decalSize

*(novo na Anastacio)* `atributo`

Tamanho dos decalques.

## dentImpulse

*(novo na Anastacio)* `atributo`

Impulso mínimo de colisão para amassar o objeto.

## fragments

*(novo na Anastacio)* `atributo`

Nome do grupo com os fragmentos usados quando o objeto quebra, ou `None`. Só em objetos destrutíveis; senão levanta `AttributeError`.

## hiddenFromCamera

*(novo na Anastacio)* `atributo`

Câmera que não deve mostrar este objeto (ex.: o próprio carro no split screen), ou `None`.

## impactImpulse

*(novo na Anastacio)* `atributo`

Impulso mínimo de colisão para um objeto explosivo detonar.

## isDeformable

*(novo na Anastacio)* `atributo · só leitura`

`True` se o objeto tem as configurações de deformação ligadas (amassar, entortar, decalques).

## linearVelocity

*(novo na Anastacio)* `atributo`

Velocidade linear. Lê em coordenadas locais e escreve em coordenadas do mundo.

## maxDecals

*(novo na Anastacio)* `atributo`

Número máximo de decalques ao mesmo tempo neste objeto.

## parentRecursive

*(novo na Anastacio)* `atributo · só leitura`

Lista de todos os pais acima do objeto, do mais próximo ao mais distante.

## particles

*(novo na Anastacio)* `atributo · só leitura`

Sistema de partículas do objeto (`KX_ParticleSystem`), ou `None`.

## particlesMix

*(novo na Anastacio)* `atributo · só leitura`

Segundo sistema de partículas (mistura) do objeto, ou `None`.

## passIndex

*(novo na Anastacio)* `atributo`

Pass Index do objeto, usado para separar objetos em filtros e efeitos.

## useBreakOnCollision

*(novo na Anastacio)* `atributo`

Se o objeto quebra ao colidir.

## useChainReaction

*(novo na Anastacio)* `atributo`

Se a explosão deste objeto detona outros explosivos por perto.

## useDentOnCollision

*(novo na Anastacio)* `atributo`

Se o objeto amassa ao colidir.

## useExplodeOnImpact

*(novo na Anastacio)* `atributo`

Se o objeto explosivo detona ao sofrer um impacto acima de `impactImpulse`.

## useInheritVelocity

*(novo na Anastacio)* `atributo`

Se os fragmentos herdam a velocidade do objeto ao quebrar.
