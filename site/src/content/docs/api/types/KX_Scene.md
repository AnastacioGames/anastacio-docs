---
title: "KX_Scene"
description: "Referência da classe Range.types.KX_Scene"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[Veja também]
[`KX_GameObject`](../../types/kx_gameobject/), [`KX_Camera`](../../types/kx_camera/), [`KX_WorldInfo`](../../types/kx_worldinfo/), [`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`Range.logic`](../../modulos/logic/)
:::



Uma cena ativa, que dá acesso a objetos, câmeras, luzes e atributos da cena.

O culling de atividade deveria desligar os logic bricks quando o dono deles fica longe demais da câmera ativa. Ele veio de um código antigo escondido no KX_Scene, e ninguém sabe ao certo o que faz.

```python

from Range import logic

# pega a cena
scene = logic.getCurrentScene()

# mostra todos os objetos da cena
for object in scene.objects:
   print(object.name)

# pega o objeto chamado 'Cube'
object = scene.objects["Cube"]

# pega o primeiro objeto da cena.
object = scene.objects[0]
```

```python

# Pega a profundidade de um objeto na visão da câmera.
from Range import logic

object = logic.getCurrentController().owner
cam = logic.getCurrentScene().active_camera

# A profundidade é negativa e diminui conforme se afasta da câmera
depth = object.position[0]*cam.world_to_camera[2][0] + object.position[1]*cam.world_to_camera[2][1] + object.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]
```

@bug: Por enquanto todos os atributos são somente leitura.

### name

O nome da cena (somente leitura).

**Tipo:** string

### objects

Lista dos objetos da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### objectsInactive

Lista dos objetos nas camadas de fundo, usados pelo atuador Add Object (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### lights

Lista das luzes da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_LightObject`

### cameras

Lista das câmeras da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_Camera`

### texts

Lista dos textos da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_FontObject`

### active_camera

A câmera ativa atual.

**Tipo:** `KX_Camera`

:::note
Pode ser definida direto pelo Python, sem precisar do `KX_SceneActuator`.
:::

### overrideCullingCamera

Câmera usada no lugar da padrão para o culling da cena. Se for None, o culling usa a câmera que está renderizando.

**Tipo:** `KX_Camera` or None

### world

O mundo ativo atual (somente leitura).

**Tipo:** `KX_WorldInfo`

### filterManager

O gerenciador de filtros 2D da cena (somente leitura).

**Tipo:** `KX_2DFilterManager`

### suspended

True se a cena estiver suspensa (somente leitura).

**Tipo:** boolean

### activityCulling

True se a cena permite o culling de atividade dos objetos.

**Tipo:** boolean

### dbvt_culling

True quando a árvore de volumes dinâmica (DBVT) está ligada (somente leitura).

**Tipo:** boolean

### pre_draw

Lista de funções chamadas antes da etapa de render. Elas podem receber como argumento a câmera que está renderizando.

**Tipo:** list

### post_draw

Lista de funções chamadas depois da etapa de render.

**Tipo:** list

### pre_draw_setup

Lista de funções chamadas antes da preparação do desenho, ou seja, antes de calcular as matrizes de visão e projeção. Elas podem receber como argumento a câmera que está renderizando; essa câmera pode ser temporária no render estéreo.

**Tipo:** list

### onRemove

Lista de funções chamadas quando a cena é destruída.

```python

@scene.onRemove.append
def callback(scene):
      print('exiting %s...' % scene.name)
```

**Tipo:** list

### gravity

A gravidade da cena nos eixos x, y e z do mundo.

**Tipo:** Vector((gx, gy, gz))

### maxDebris

Quantos fragmentos de objetos quebrados ficam vivos na cena; acima disso, os mais antigos são removidos. Começa com o valor de Scene > Game Physics > Max Debris. 0 significa sem limite. Diminuir o valor remove os pedaços excedentes na hora.

**Tipo:** integer in [0, 100000]

### explode(position, radius=5.0, force=20.0, upBias=0.3, occlusion=True, mask=0xFFFF, ignore=None)

Impulso radial nos objetos dinâmicos em volta de position, que cai a zero em radius (`force * (1 - distance / radius)`). Objetos destrutíveis atingidos acima do seu `KX_GameObject.breakImpulse` quebram e os pedaços são empurrados, dividindo o impulso pela massa. Objetos explosivos atingidos acima do seu Impact Impulse (com Chain Reaction ligado) detonam no frame seguinte.

- **`position`**: O centro da explosão.
  - tipo: 3D Vector
- **`radius`**: A distância que a explosão alcança.
  - tipo: float
- **`force`**: O impulso no centro.
  - tipo: float
- **`upBias`**: Quanto o empurrão é inclinado para cima; 0.0 empurra reto para longe do centro.
  - tipo: float
- **`occlusion`**: Se True, a geometria estática entre o centro e um objeto o protege.
  - tipo: boolean
- **`mask`**: Os grupos de colisão atingidos.
  - tipo: bitfield
- **`ignore`**: Um objeto ou uma lista de objetos que ficam de fora.
  - tipo: `KX_GameObject` or list

**Retorna:** Os objetos atingidos (sem contar os pedaços novos).

**Tipo do retorno:** list of `KX_GameObject`

### addObject(object, reference, time=0.0)

Adiciona um objeto à cena, como o atuador Add Object faria.

- **`object`**: O objeto a adicionar (ou o nome dele).
  - tipo: `KX_GameObject` or string
- **`reference`**: O objeto (ou o nome dele) de onde copiar posição, orientação e escala (opcional). Se o objeto adicionado for uma luz e não houver referência, a camada da luz será a camada ativa da cena do Blender.
  - tipo: `KX_GameObject` or string
- **`time`**: O tempo de vida do objeto adicionado, em frames (considera um frame como 1/50 de segundo). 0.0 significa que o objeto dura para sempre (opcional).
  - tipo: float

**Retorna:** O objeto recém-adicionado.

**Tipo do retorno:** `KX_GameObject`

### end()

Remove a cena do jogo.

### restart()

Reinicia a cena.

### replace(scene)

Troca esta cena por outra.

- **`scene`**: O nome da cena que vai substituir esta.
  - tipo: string

**Retorna:** True se a cena existe e foi agendada para entrar, False caso contrário.

**Tipo do retorno:** boolean

### suspend()

Suspende esta cena.

### resume()

Retoma esta cena.

### get(key, default=None)

Devolve o valor da chave, ou o valor padrão se a chave não existir.

**Retorna:** O valor da chave ou o padrão.

### drawObstacleSimulation()

Desenha a visualização de depuração da simulação de obstáculos.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### convertObject(name, children=True)

 <small>método</small>

Cria agora um objeto que ficou de fora no carregamento pela opção **Convert** (e os filhos não convertidos). Vai para `objects` se estiver numa camada ativa, senão para `objectsInactive` (pronto para `addObject`). Um objeto já convertido é retornado como está.

**Retorna:** `KX_GameObject`

### getQualityPreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### play_cutscene(sequence=0)

 <small>método</small>

Começa a Cutscene nativa da cena. Retorna `True` se deu certo.

**Retorna:** `bool`

### release_cutscene_trigger(name)

 <small>método</small>

Libera um evento **Wait Trigger** da Cutscene esperando por `name`. `True` se ela estava esperando agora; senão o gatilho fica guardado para o próximo Wait Trigger com esse nome. Uma mensagem com assunto `name` faz o mesmo.

**Retorna:** `bool`

### restart_cutscene()

 <small>método</small>

Reinicia a Cutscene ativa e remove os objetos que ela criou.

### setQualityPreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### stop_cutscene()

 <small>método</small>

Para a Cutscene e remove os objetos que ela criou.

### speakers

 <small>atributo · só leitura</small>

Lista dos objetos de som (`KX_Speaker`) da cena.

### thread_logic_1

 <small>atributo</small>

Lista de funções chamadas na thread de lógica paralela, a cada frame. Mesmo uso de `pre_draw`.

### unconvertedObjects

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Nomes dos objetos que ainda podem ser criados com `convertObject()`.

### worldSun

 <small>atributo · só leitura</small>

Luz Sun ligada ao World (posição do sol do céu), ou `None`.

