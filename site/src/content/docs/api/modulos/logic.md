---
title: "Range.logic"
description: "Referência do módulo Range.logic"
---

## Introdução

Módulo com as funções de lógica do jogo, importado automaticamente no namespace dos controladores Python.

```python

# Para pegar o controlador que está rodando este script Python:
cont = Range.logic.getCurrentController() # Range.logic é importado automaticamente

# Para pegar o objeto do jogo onde está este controlador:
obj = cont.owner
```

Os métodos de `KX_GameObject`, `KX_Camera` ou `KX_LightObject` ficam disponíveis conforme o tipo do objeto

```python

# Para pegar um sensor ligado a este controlador.
# "sensorname" é o nome do sensor como foi definido na interface do Blender.
# +---------------------+  +--------+
# | Sensor "sensorname" +--+ Python +
# +---------------------+  +--------+
sens = cont.sensors["sensorname"]

# Para pegar a lista de todos os sensores:
sensors = co.sensors
```

Veja a referência de cada sensor para os métodos disponíveis:

* `KX_MouseFocusSensor`
* `KX_NearSensor`
* `KX_NetworkMessageSensor`
* `KX_RadarSensor`
* `KX_RaySensor`
* `KX_CollisionSensor`
* `SCA_DelaySensor`
* `SCA_JoystickSensor`
* `SCA_KeyboardSensor`
* `SCA_MouseSensor`
* `SCA_PropertySensor`
* `SCA_RandomSensor`
Você também pode acessar os atuadores ligados ao controlador

```python

# Para pegar um atuador ligado ao controlador:
# +--------+  +-------------------------+
# + Python +--+ Actuator "actuatorname" |
# +--------+  +-------------------------+
actuator = co.actuators["actuatorname"]

# Ativa um atuador
controller.activate(actuator)
```

Veja a referência de cada atuador para os métodos disponíveis

* `BL_ActionActuator`
* `KX_CameraActuator`
* `KX_ConstraintActuator`
* `KX_GameActuator`
* `KX_MouseActuator`
* `KX_NetworkMessageActuator`
* `KX_ObjectActuator`
* `KX_ParentActuator`
* `KX_SCA_AddObjectActuator`
* `KX_SCA_DynamicActuator`
* `KX_SCA_EndObjectActuator`
* `KX_SCA_ReplaceMeshActuator`
* `KX_SceneActuator`
* `KX_SoundActuator`
* `KX_StateActuator`
* `KX_TrackToActuator`
* `KX_VisibilityActuator`
* `SCA_2DFilterActuator`
* `SCA_PropertyActuator`
* `SCA_RandomActuator`
A maioria dos métodos dos logic bricks dá acesso às propriedades que aparecem nos botões de lógica. Consulte a documentação dos logic bricks para saber como cada um funciona.

Também há métodos para acessar a `Range.types.KX_Scene` atual

```python

# Pega a cena atual
scene = Range.logic.getCurrentScene()

# Pega a câmera atual
cam = scene.active_camera
```

As matrizes usadas pela engine são **por linha** (row major): `matrix[row][col] = float`

`Range.types.KX_Camera` tem alguns exemplos usando matrizes.

## Variáveis

### globalDict

Um dicionário que é mantido quando outro arquivo blend é carregado; serve para guardar inventário e outras variáveis entre cenas e arquivos blend. Ele também pode ser gravado num arquivo e carregado depois com os atuadores de carregar/salvar jogo.

:::note
só tipos nativos do Python, como int/string/bool/float/tuplas/listas, podem ser salvos; GameObjects, atuadores etc. não funcionam como esperado.
:::

### keyboard

O teclado atual, dentro de um objeto `SCA_PythonKeyboard`.

### mouse

O mouse atual, dentro de um objeto `SCA_PythonMouse`.

### motion

Os sensores de movimento do aparelho (giroscópio, acelerômetro, inclinação), dentro de um objeto `KX_PythonMotion`.

### joysticks

Lista dos `SCA_PythonJoystick` conectados. O tamanho da lista é o número máximo de joysticks suportados. Se não houver joystick numa posição, ela vale None.

## Funções gerais

### getCurrentController()

Pega o controlador Python ligado a este script.

**Tipo do retorno:** `Range.types.SCA_PythonController`

### getCurrentScene()

Pega a cena atual.

**Tipo do retorno:** `Range.types.KX_Scene`

### getSceneList()

Pega a lista das cenas carregadas na engine agora.

**Tipo do retorno:** list of `Range.types.KX_Scene`

:::note
As cenas do arquivo blend que não foram convertidas não aparecem nesta lista. Ela só traz cenas como as de overlay.
:::

### getInactiveSceneNames()

Pega a lista dos nomes das cenas que não estão carregadas na engine.

**Tipo do retorno:** list of string

### loadGlobalDict()

Carrega Range.logic.globalDict de um arquivo.

### saveGlobalDict()

Salva Range.logic.globalDict num arquivo.

### startGame(blend)

Carrega o arquivo blend.

- **`blend`**: O nome do arquivo blend
  - tipo: string

### endGame()

Encerra o jogo atual.

### restartGame()

Reinicia o jogo atual recarregando o arquivo .blend (a última versão salva, não o que está rodando agora).

### LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

Converte todos os datablocks do tipo indicado do arquivo blend indicado.

- **`blend`**: O caminho do arquivo blend (ou o nome a usar para a biblioteca, se data for passado)
  - tipo: string
- **`type`**: O tipo de datablock (por enquanto só "Action", "Mesh" e "Scene" são suportados)
  - tipo: string
- **`data`**: Dados binários de um arquivo blend (opcional)
  - tipo: bytes
- **`load_actions`**: Procura e carrega todas as ações da cena, não só as ações "ativas" (só para o tipo Scene)
  - tipo: bool
- **`verbose`**: Se mostra ou não informações de depuração (ex.: "SceneName: Scene")
  - tipo: bool
- **`load_scripts`**: Se carrega ou não também os datablocks de texto (pode ser desligado para mais segurança)
  - tipo: bool   
- **`asynchronous`**: Se carrega ou não de forma assíncrona (em outra thread). Por enquanto só o tipo "Scene" suporta isso.
  - tipo: bool
- **`scene`**: Cena onde juntar os dados carregados; se for `None`, usa a cena atual.
  - tipo: `Range.types.KX_Scene` or string

**Tipo do retorno:** `Range.types.KX_LibLoadStatus`

:::note
Bibliotecas carregadas de forma assíncrona não ficam disponíveis logo que LibLoad() retorna. Use o KX_LibLoadStatus devolvido para saber quando elas estão prontas.
:::

### LibNew(name, type, data)

Usa dados de um datablock que já existe e carrega como uma biblioteca nova.

- **`name`**: Um nome único para a biblioteca, usado depois para removê-la
  - tipo: string
- **`type`**: O tipo de datablock (por enquanto só "Mesh" é suportado)
  - tipo: string
- **`data`**: Lista com os nomes dos datablocks a carregar
  - tipo: list of strings

### LibFree(name)

Libera uma biblioteca, removendo todos os objetos e malhas dela das cenas ativas.

- **`name`**: O nome da biblioteca a liberar (o nome usado em LibNew)
  - tipo: string

### LibList()

Devolve a lista das bibliotecas carregadas agora.

**Tipo do retorno:** list [str]

### setLibLoadFrameBudget([ms])

Tempo por frame, em milissegundos, que o LibLoad assíncrono pode gastar juntando as bibliotecas carregadas à cena (texturas, shaders, objetos). O padrão de 8 mantém o frame rate do jogo; uma tela de carregamento pode aumentar (ex.: 30) para terminar antes com frame rate menor, e depois voltar o valor.

- **`ms`**: Novo limite; se omitido, só devolve o atual.
  - tipo: float

**Retorna:** O limite atual em milissegundos.

**Tipo do retorno:** float

### addScene(name, overlay=1, asynchronous=False)

Carrega uma cena na engine.

:::note
Esta função não tem efeito na hora: a cena entra na fila e é adicionada no próximo ciclo de lógica, quando aparece em `getSceneList`
:::

- **`name`**: O nome da cena
  - tipo: string
- **`overlay`**: Overlay ou underlay (opcional)
  - tipo: integer
- **`asynchronous`**: Compila os shaders da cena aos poucos a cada frame (limite de `setLibLoadFrameBudget`) antes de a cena entrar em `getSceneList`, para a tela de carregamento continuar desenhando; a lógica da cena só começa depois disso.
  - tipo: boolean

### sendMessage(subject, body="", to="", message_from="")

Envia uma mensagem para os sensores de qualquer cena ativa.

- **`subject`**: O assunto da mensagem
  - tipo: string
- **`body`**: O corpo da mensagem (opcional)
  - tipo: string
- **`to`**: O nome do objeto que vai receber a mensagem (opcional)
  - tipo: string
- **`message_from`**: O nome do objeto de onde a mensagem vem (opcional)
  - tipo: string

### setGravity(gravity)

Define a gravidade do mundo.

- **`gravity`**: O vetor de gravidade
  - tipo: Vector((fx, fy, fz))

### getSpectrum() (Deprecated)

Devolve uma lista de 512 pontos da placa de som. Só funciona com o driver de som fmod.

**Tipo do retorno:** list [float], len(getSpectrum()) == 512

### getMaxLogicFrame()

Pega o número máximo de frames de lógica por frame de render.

**Retorna:** O número máximo de frames de lógica por frame de render

**Tipo do retorno:** integer

### setMaxLogicFrame(maxlogic)

Define o número máximo de frames de lógica executados por frame de render. Não afeta a física, que continua rodando no frame rate completo.

- **`maxlogic`**: O novo número máximo de frames de lógica por frame de render. Valores válidos: 1..5
  - tipo: integer

### getMaxPhysicsFrame()

:::danger[Obsoleto ]
Nenhuma parte da engine usa este limite; o valor definido aqui não tem efeito. Fica só por compatibilidade com scripts antigos. Ele também não controla mais o culling de sombras, que antes usava esta mesma configuração.
:::

Pega o último valor passado para `setMaxPhysicsFrame`.

**Retorna:** O último valor definido (padrão: 5)

**Tipo do retorno:** integer

### setMaxPhysicsFrame(maxphysics)

:::danger[Obsoleto ]
Nenhuma parte da engine usa este limite; chamar isto não tem efeito na física nem nas sombras. Fica só por compatibilidade com scripts antigos.
:::

Guarda o valor para ler depois com `getMaxPhysicsFrame`. Era documentado como o número máximo de passos de física por frame de render, mas nenhum código da engine lê o valor para isso.

- **`maxphysics`**: O novo número máximo de passos de física por frame de render. Valores válidos: 1..5.
  - tipo: integer

### getLogicTicRate()

Pega a frequência de atualização da lógica.

**Retorna:** A frequência da lógica em Hz

**Tipo do retorno:** float

### setLogicTicRate(ticrate)

Define a frequência de atualização da lógica.

A frequência da lógica é quantas vezes por segundo os logic bricks são executados. O padrão é 60 Hz.

- **`ticrate`**: A nova frequência da lógica (em Hz).
  - tipo: float

### getPhysicsTicRate()

Pega a frequência de atualização da física

**Retorna:** A frequência da física em Hz

**Tipo do retorno:** float

### setPhysicsTicRate(ticrate)

Define a frequência de atualização da física

A frequência da física é quantas vezes por segundo a física é executada. O padrão é 60 Hz.

- **`ticrate`**: A nova frequência (em Hz).
  - tipo: float

### getExitKey()

Pega a tecla usada para sair da engine

**Retorna:** A tecla (padrão: `Range.events.ESCKEY`)

**Tipo do retorno:** int

### setExitKey(key)

Define a tecla usada para sair da engine

- **`key`**: Uma constante de tecla de `Range.events`
  - tipo: int

### NextFrame()

Renderiza o próximo frame (se o Python estiver no controle)

### setRender(render)

Define a opção global que controla o render da cena. Se for True, o render acontece depois do frame de lógica. Se for False, o render é pulado e outro frame de lógica começa na hora.

:::note
Com o render desligado, o VSync da GPU não limita mais os frames por segundo, mas a opção *Use Frame Rate* continua regulando o fps. Para rodar o máximo de frames possível, desmarque essa opção (Render Properties, painel System).
:::

- **`render`**: A opção de render
  - tipo: bool

### getRender()

Pega o valor atual da opção global de render

**Retorna:** O valor da opção

**Tipo do retorno:** bool

## Funções de tempo

### getClockTime()

Pega o tempo de render atual da engine, em segundos. É o tempo de simulação correspondente à próxima cena que será renderizada.

**Tipo do retorno:** double

### getFrameTime()

Pega o tempo de frame atual da engine, em segundos. É o tempo de simulação correspondente à chamada atual da lógica. Em geral, é este o tempo que interessa.

**Tipo do retorno:** double

### getRealTime()

Pega quantos segundos reais (do relógio do sistema) passaram desde o começo da simulação.

**Tipo do retorno:** double

### getTimeScale()

Pega o multiplicador entre o tempo real e o tempo da simulação. O padrão é 1.0. Valores maiores que 1.0 deixam a simulação mais rápida que o tempo real; valores menores, mais lenta.

**Tipo do retorno:** double

### setTimeScale(time_scale)

Define o multiplicador entre o tempo real e o tempo da simulação. Valores maiores que 1.0 deixam a simulação mais rápida que o tempo real; valores menores, mais lenta. Valores muito altos podem deixar a física instável.

- **`time_scale`**: O novo multiplicador de tempo.

### getUseExternalClock()

Diz se a engine usa o relógio interno ou um relógio externo. O padrão é o relógio interno.

**Tipo do retorno:** bool

### setUseExternalClock(use_external_clock)

Define se a engine usa o relógio interno ou um relógio externo. Com o relógio externo, é preciso chamar setClockTime regularmente.

- **`use_external_clock`**: A nova configuração

### setClockTime(new_time)

Define o próximo valor do relógio da simulação. É melhor usar este método numa função main própria em Python: chamá-lo num logic brick pode travar o sistema facilmente (se o tempo não avançar o bastante para rodar pelo menos o próximo passo de lógica).

- **`new_time`**: O próximo valor do relógio da engine (em segundos).

## Funções utilitárias

### expandPath(path)

Converte um caminho interno do Blender num caminho de verdade do sistema de arquivos.

Use / como separador de pastas no caminho. Use '//' no começo para um caminho relativo; o Blender troca isso pela pasta do .blend ou do executável atual para formar o caminho completo. A função também converte o separador para o formato do sistema.

- **`path`**: O caminho a converter/expandir.
  - tipo: string

**Retorna:** O caminho convertido

**Tipo do retorno:** string

### getAverageFrameRate()

Pega o frame rate médio estimado de todas as cenas ativas, não só da atual.

**Retorna:** O frame rate médio estimado, em frames por segundo

**Tipo do retorno:** float

### getBlendFileList(path = "//")

Devolve a lista dos arquivos blend na mesma pasta do arquivo blend aberto, ou na pasta passada como argumento.

- **`path`**: Pasta opcional, que é expandida (como em expandPath) para o caminho completo.
  - tipo: string

**Retorna:** Lista de nomes de arquivo, sem a pasta na frente

**Tipo do retorno:** list

### getRandomFloat()

Devolve um número decimal aleatório no intervalo [0 - 1)

### PrintGLInfo()

Mostra no console as informações das extensões GL

### PrintMemInfo()

Mostra no console as estatísticas da engine

### getProfileInfo()

Devolve um dicionário Python com as mesmas informações do profiler na tela. As chaves são as categorias do profiler, e os valores são tuplas com o tempo gasto (em ms) no primeiro elemento e a porcentagem do tempo total no segundo.

### getRenderStats()

Devolve um dicionário Python com contadores inteiros do último frame completo, os mesmos números que as consultas de render do Debug Mode mostram. Diferente dos tempos de `getProfileInfo`, eles não dependem do hardware nem do relógio, por isso são o que testes A/B devem comparar.

Contadores do rasterizador, cobrindo todas as passadas do frame (câmera principal, sombras, filtros 2D):

* `drawCalls`: draw calls feitas.
* `materialBinds`: binds de material (programa de shader).
* `lightBinds`: envios dos uniforms das luzes da cena e das lâmpadas com sombra. O conjunto de luzes é constante por camada de luz, então isto conta quantas vezes os mesmos valores foram reenviados.

Contadores da cena ativa:

* `cullingTotal`, `cullingTested`, `cullingVisible`: objetos na lista de render, testados contra o frustum/DBVT e achados visíveis, na última passada de culling da câmera principal.
* `lightsTotal`, `lightsShadowUpdated`, `shadowPasses`: luzes da cena, luzes cujo buffer de sombra foi atualizado e passadas de sombra renderizadas (cada divisão de cascata conta como uma).
* `sensors`, `controllersTriggered`, `actuatorsUpdated`: sensores registrados e controladores/atuadores executados no frame de lógica. Atenção: estes dois são contados enquanto o frame roda, e um controlador Python que chama esta função faz parte desse frame; ele só vê o que rodou antes dele, então num controlador o valor costuma ser 0. A sobreposição do Debug Mode lê os valores depois do frame e mostra a contagem completa. Os contadores do rasterizador e do culling não têm esse problema: sempre vêm do último frame completo.

## Constantes

### KX_TRUE

Valor verdadeiro usado por alguns módulos.

### KX_FALSE

Valor falso usado por alguns módulos.

## Sensores

## Estado do sensor

### KX_SENSOR_INACTIVE

Estado do sensor: desligado.

### KX_SENSOR_JUST_ACTIVATED

Estado do sensor: acabou de ligar neste quadro.

### KX_SENSOR_ACTIVE

Estado do sensor: continua ligado.

### KX_SENSOR_JUST_DEACTIVATED

## Sensor de armature

Veja `Range.types.KX_ArmatureSensor.type`

### KX_ARMSENSOR_STATE_CHANGED

Detecta que a constraint mudou de estado (ativa/inativa)

**Valor:** `0`

### KX_ARMSENSOR_LIN_ERROR_BELOW

Detecta que o erro linear da constraint passou de um limite

**Valor:** `1`

### KX_ARMSENSOR_LIN_ERROR_ABOVE

Detecta que o erro linear da constraint ficou abaixo de um limite

**Valor:** `2`

### KX_ARMSENSOR_ROT_ERROR_BELOW

Detecta que o erro de rotação da constraint passou de um limite

**Valor:** `3`

### KX_ARMSENSOR_ROT_ERROR_ABOVE

Detecta que o erro de rotação da constraint ficou abaixo de um limite

**Valor:** `4`

## Sensor de propriedade

### KX_PROPSENSOR_EQUAL

Ativa quando a propriedade é igual ao valor do sensor.

**Valor:** `1`

### KX_PROPSENSOR_NOTEQUAL

Ativa quando a propriedade é diferente do valor do sensor.

**Valor:** `2`

### KX_PROPSENSOR_INTERVAL

Ativa quando a propriedade está entre os limites indicados.

**Valor:** `3`

### KX_PROPSENSOR_CHANGED

Ativa quando a propriedade muda

**Valor:** `4`

### KX_PROPSENSOR_EXPRESSION

Ativa quando a expressão confere

**Valor:** `5`

### KX_PROPSENSOR_LESSTHAN

Ativa quando a propriedade é menor que o valor do sensor

**Valor:** `6`

### KX_PROPSENSOR_GREATERTHAN

Ativa quando a propriedade é maior que o valor do sensor

**Valor:** `7`

## Sensor de radar

Veja `Range.types.KX_RadarSensor`

### KX_RADAR_AXIS_POS_X

Sensor Radar: cone apontando para o eixo +X do objeto.

### KX_RADAR_AXIS_POS_Y

Sensor Radar: cone apontando para o eixo +Y do objeto.

### KX_RADAR_AXIS_POS_Z

Sensor Radar: cone apontando para o eixo +Z do objeto.

### KX_RADAR_AXIS_NEG_X

Sensor Radar: cone apontando para o eixo -X do objeto.

### KX_RADAR_AXIS_NEG_Y

Sensor Radar: cone apontando para o eixo -Y do objeto.

### KX_RADAR_AXIS_NEG_Z

## Sensor de raio

Veja `Range.types.KX_RaySensor`

### KX_RAY_AXIS_POS_X

Sensor Ray: raio lançado no eixo +X do objeto.

### KX_RAY_AXIS_POS_Y

Sensor Ray: raio lançado no eixo +Y do objeto.

### KX_RAY_AXIS_POS_Z

Sensor Ray: raio lançado no eixo +Z do objeto.

### KX_RAY_AXIS_NEG_X

Sensor Ray: raio lançado no eixo -X do objeto.

### KX_RAY_AXIS_NEG_Y

Sensor Ray: raio lançado no eixo -Y do objeto.

### KX_RAY_AXIS_NEG_Z

## Atuadores

## Atuador de ação

Veja `Range.types.BL_ActionActuator`

### KX_ACTIONACT_PLAY

Atuador Action: toca a animação uma vez.

### KX_ACTIONACT_PINGPONG

Atuador Action: toca para frente e, na próxima ativação, para trás.

### KX_ACTIONACT_FLIPPER

Atuador Action: toca enquanto ativo e volta ao início quando desliga.

### KX_ACTIONACT_LOOPSTOP

Atuador Action: repete enquanto o sensor estiver ativo.

### KX_ACTIONACT_LOOPEND

Atuador Action: repete e, ao desligar, termina a volta atual.

### KX_ACTIONACT_PROPERTY

## Atuador de armature

Veja `Range.types.BL_ArmatureActuator.type`

### KX_ACT_ARMATURE_RUN

Só garante que a armature será atualizada no próximo frame gráfico. É o único modo contínuo do atuador: roda sozinho uma vez por frame até um controlador pará-lo

**Valor:** `0`

### KX_ACT_ARMATURE_ENABLE

Liga a constraint.

**Valor:** `1`

### KX_ACT_ARMATURE_DISABLE

Desliga a constraint (os valores da constraint em tempo de jogo não são atualizados).

**Valor:** `2`

### KX_ACT_ARMATURE_SETTARGET

Troca o alvo e o subalvo da constraint.

**Valor:** `3`

### KX_ACT_ARMATURE_SETWEIGHT

Muda o peso da constraint (só IK).

**Valor:** `4`

### KX_ACT_ARMATURE_SETINFLUENCE

Muda a influência da constraint.

**Valor:** `5`

## Atuador de constraint

Veja `Range.types.KX_ConstraintActuator.option`

* Vale para a constraint de distância:

### KX_CONSTRAINTACT_NORMAL

Ativa o alinhamento à superfície

### KX_CONSTRAINTACT_DISTANCE

Ativa o controle de distância

### KX_CONSTRAINTACT_LOCAL

A direção do raio segue o eixo local

* Vale para a constraint de campo de força:

### KX_CONSTRAINTACT_DOROTFH

O campo de força também age na rotação

* Vale para as duas:

### KX_CONSTRAINTACT_MATERIAL

Detecta material em vez de propriedade

### KX_CONSTRAINTACT_PERMANENT

Não desativa se o raio não atingir o alvo

Veja `Range.types.KX_ConstraintActuator.limit`

### KX_CONSTRAINTACT_LOCX

Limita a coordenada X.

### KX_CONSTRAINTACT_LOCY

Limita a coordenada Y

### KX_CONSTRAINTACT_LOCZ

Limita a coordenada Z

### KX_CONSTRAINTACT_ROTX

Limita a rotação X

### KX_CONSTRAINTACT_ROTY

Limita a rotação Y

### KX_CONSTRAINTACT_ROTZ

Limita a rotação Z

### KX_CONSTRAINTACT_DIRNX

Define a distância ao longo do eixo X negativo

### KX_CONSTRAINTACT_DIRNY

Define a distância ao longo do eixo Y negativo

### KX_CONSTRAINTACT_DIRNZ

Define a distância ao longo do eixo Z negativo

### KX_CONSTRAINTACT_DIRPX

Define a distância ao longo do eixo X positivo

### KX_CONSTRAINTACT_DIRPY

Define a distância ao longo do eixo Y positivo

### KX_CONSTRAINTACT_DIRPZ

Define a distância ao longo do eixo Z positivo

### KX_CONSTRAINTACT_ORIX

Define a orientação do eixo X

### KX_CONSTRAINTACT_ORIY

Define a orientação do eixo Y

### KX_CONSTRAINTACT_ORIZ

Define a orientação do eixo Z

### KX_CONSTRAINTACT_FHNX

Define o campo de força ao longo do eixo X negativo

### KX_CONSTRAINTACT_FHNY

Define o campo de força ao longo do eixo Y negativo

### KX_CONSTRAINTACT_FHNZ

Define o campo de força ao longo do eixo Z negativo

### KX_CONSTRAINTACT_FHPX

Define o campo de força ao longo do eixo X positivo

### KX_CONSTRAINTACT_FHPY

Define o campo de força ao longo do eixo Y positivo

### KX_CONSTRAINTACT_FHPZ

Define o campo de força ao longo do eixo Z positivo

## Atuador dinâmico

Veja `Range.types.KX_SCA_DynamicActuator`

### KX_DYN_RESTORE_DYNAMICS

Atuador Dynamic: volta a ter física.

### KX_DYN_DISABLE_DYNAMICS

Atuador Dynamic: desliga a física do objeto.

### KX_DYN_ENABLE_RIGID_BODY

Atuador Dynamic: liga o modo corpo rígido (rotação pela física).

### KX_DYN_DISABLE_RIGID_BODY

Atuador Dynamic: desliga o modo corpo rígido.

### KX_DYN_SET_MASS

## Atuador de jogo

Veja `Range.types.KX_GameActuator`

### KX_GAME_LOAD

Atuador Game: carrega outro arquivo de jogo.

### KX_GAME_START

Atuador Game: inicia outro arquivo de jogo.

### KX_GAME_RESTART

Atuador Game: reinicia o jogo.

### KX_GAME_QUIT

Atuador Game: fecha o jogo.

### KX_GAME_SAVECFG

Atuador Game: salva as propriedades globais em arquivo.

### KX_GAME_LOADCFG

## Atuador de mouse

### KX_ACT_MOUSE_OBJECT_AXIS_X

Atuador Mouse (look): gira em torno do eixo X do objeto.

### KX_ACT_MOUSE_OBJECT_AXIS_Y

Atuador Mouse (look): gira em torno do eixo Y do objeto.

### KX_ACT_MOUSE_OBJECT_AXIS_Z

## Atuador de parentesco

### KX_PARENT_REMOVE

Atuador Parent: tira o objeto do pai.

### KX_PARENT_SET

## Distribuições aleatórias

Veja `Range.types.SCA_RandomActuator`

### KX_RANDOMACT_BOOL_CONST

Atuador Random: verdadeiro/falso fixo.

### KX_RANDOMACT_BOOL_UNIFORM

Atuador Random: verdadeiro ou falso com 50% de chance cada.

### KX_RANDOMACT_BOOL_BERNOUILLI

Atuador Random: verdadeiro com a chance que você definir.

### KX_RANDOMACT_INT_CONST

Atuador Random: número inteiro fixo.

### KX_RANDOMACT_INT_UNIFORM

Atuador Random: inteiro sorteado entre um mínimo e um máximo.

### KX_RANDOMACT_INT_POISSON

Atuador Random: inteiro com distribuição de Poisson (média definida).

### KX_RANDOMACT_FLOAT_CONST

Atuador Random: número decimal fixo.

### KX_RANDOMACT_FLOAT_UNIFORM

Atuador Random: decimal sorteado entre um mínimo e um máximo.

### KX_RANDOMACT_FLOAT_NORMAL

Atuador Random: decimal com distribuição normal (média e desvio).

### KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

## Atuador de cena

Veja `Range.types.KX_SceneActuator`

### KX_SCENE_RESTART

Atuador Scene: reinicia a cena.

### KX_SCENE_SET_SCENE

Atuador Scene: troca para outra cena.

### KX_SCENE_SET_CAMERA

Atuador Scene: troca a câmera ativa.

### KX_SCENE_ADD_FRONT_SCENE

Atuador Scene: adiciona uma cena por cima (overlay, como HUD).

### KX_SCENE_ADD_BACK_SCENE

Atuador Scene: adiciona uma cena por baixo (fundo).

### KX_SCENE_REMOVE_SCENE

Atuador Scene: remove uma cena.

### KX_SCENE_SUSPEND

Atuador Scene: pausa uma cena.

### KX_SCENE_RESUME

## Atuador de som

Veja `Range.types.KX_SoundActuator`

### KX_SOUNDACT_PLAYSTOP

Atuador Sound: toca enquanto o sensor estiver ativo e para quando desligar.

**Valor:** `1`

### KX_SOUNDACT_PLAYEND

Atuador Sound: toca o som inteiro uma vez.

**Valor:** `2`

### KX_SOUNDACT_LOOPSTOP

Atuador Sound: repete enquanto o sensor estiver ativo.

**Valor:** `3`

### KX_SOUNDACT_LOOPEND

Atuador Sound: repete e, ao desligar, termina a volta atual.

**Valor:** `4`

### KX_SOUNDACT_LOOPBIDIRECTIONAL

Atuador Sound: toca para frente e para trás em repetição.

**Valor:** `5`

### KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

**Valor:** `6`

## Atuador de steering

Veja `Range.types.KX_SteeringActuator.behavior`

### KX_STEERING_SEEK

Atuador Steering: vai até o alvo.

**Valor:** `1`

### KX_STEERING_FLEE

Atuador Steering: foge do alvo.

**Valor:** `2`

### KX_STEERING_PATHFOLLOWING

**Valor:** `3`

## Atuador TrackTo

Veja `Range.types.KX_TrackToActuator`

### KX_TRACK_UPAXIS_POS_X

Atuador Track To: eixo +X do objeto fica para cima.

### KX_TRACK_UPAXIS_POS_Y

Atuador Track To: eixo +Y do objeto fica para cima.

### KX_TRACK_UPAXIS_POS_Z

Atuador Track To: eixo +Z do objeto fica para cima.

### KX_TRACK_TRAXIS_POS_X

Atuador Track To: eixo +X do objeto aponta para o alvo.

### KX_TRACK_TRAXIS_POS_Y

Atuador Track To: eixo +Y do objeto aponta para o alvo.

### KX_TRACK_TRAXIS_POS_Z

Atuador Track To: eixo +Z do objeto aponta para o alvo.

### KX_TRACK_TRAXIS_NEG_X

Atuador Track To: eixo -X do objeto aponta para o alvo.

### KX_TRACK_TRAXIS_NEG_Y

Atuador Track To: eixo -Y do objeto aponta para o alvo.

### KX_TRACK_TRAXIS_NEG_Z

## Diversos

## Filtro 2D

### RAS_2DFILTER_BLUR

Atuador 2D Filter: desfoque.

**Valor:** `2`

### RAS_2DFILTER_CUSTOMFILTER

Filtro personalizado; o código é definido pela propriedade shaderText.

**Valor:** `12`

### RAS_2DFILTER_DILATION

Atuador 2D Filter: dilatação (clareia bordas).

**Valor:** `4`

### RAS_2DFILTER_DISABLED

Desliga o filtro que está ativo agora

**Valor:** `-1`

### RAS_2DFILTER_ENABLED

Liga o filtro que foi desligado antes

**Valor:** `-2`

### RAS_2DFILTER_EROSION

Atuador 2D Filter: erosão (escurece bordas).

**Valor:** `5`

### RAS_2DFILTER_GRAYSCALE

Atuador 2D Filter: tons de cinza.

**Valor:** `9`

### RAS_2DFILTER_INVERT

Atuador 2D Filter: cores invertidas.

**Valor:** `11`

### RAS_2DFILTER_LAPLACIAN

Atuador 2D Filter: detecção de bordas (Laplace).

**Valor:** `6`

### RAS_2DFILTER_MOTIONBLUR

Cria e liga filtros prontos

**Valor:** `1`

### RAS_2DFILTER_NOFILTER

Desliga e destrói o filtro que está ativo agora

**Valor:** `0`

### RAS_2DFILTER_PREWITT

Atuador 2D Filter: detecção de bordas (Prewitt).

**Valor:** `8`

### RAS_2DFILTER_SEPIA

Atuador 2D Filter: sépia.

**Valor:** `10`

### RAS_2DFILTER_SHARPEN

Atuador 2D Filter: nitidez.

**Valor:** `3`

### RAS_2DFILTER_SOBEL

**Valor:** `7`

### RAS_2DFILTER_SOBEL

**Valor:** `14`

## Canal de armature

Veja `Range.types.BL_ArmatureChannel.rotation_mode`

Observação: os modos euler têm os nomes da interface do Blender, mas a ordem real dos eixos é invertida

### ROT_MODE_QUAT

Usa o quaternion do atributo rotation para atualizar a rotação do osso.

**Valor:** `0`

### ROT_MODE_XYZ

Usa euler_rotation e aplica os ângulos nos eixos Z, Y, X do osso, nessa ordem.

**Valor:** `1`

### ROT_MODE_XZY

Usa euler_rotation e aplica os ângulos nos eixos Y, Z, X do osso, nessa ordem.

**Valor:** `2`

### ROT_MODE_YXZ

Usa euler_rotation e aplica os ângulos nos eixos Z, X, Y do osso, nessa ordem.

**Valor:** `3`

### ROT_MODE_YZX

Usa euler_rotation e aplica os ângulos nos eixos X, Z, Y do osso, nessa ordem.

**Valor:** `4`

### ROT_MODE_ZXY

Usa euler_rotation e aplica os ângulos nos eixos Y, X, Z do osso, nessa ordem.

**Valor:** `5`

### ROT_MODE_ZYX

Usa euler_rotation e aplica os ângulos nos eixos X, Y, Z do osso, nessa ordem.

**Valor:** `6`

## Constraint de armature

Veja `Range.types.BL_ArmatureConstraint.type`

### CONSTRAINT_TYPE_TRACKTO

Tipo de restrição de bone: Track To (aponta para um alvo).

### CONSTRAINT_TYPE_KINEMATIC

Tipo de restrição de bone: IK (cinemática inversa).

### CONSTRAINT_TYPE_ROTLIKE

Tipo de restrição de bone: Copy Rotation.

### CONSTRAINT_TYPE_LOCLIKE

Tipo de restrição de bone: Copy Location.

### CONSTRAINT_TYPE_MINMAX

Tipo de restrição de bone: Floor (limite mín./máx.).

### CONSTRAINT_TYPE_SIZELIKE

Tipo de restrição de bone: Copy Scale.

### CONSTRAINT_TYPE_LOCKTRACK

Tipo de restrição de bone: Locked Track.

### CONSTRAINT_TYPE_STRETCHTO

Tipo de restrição de bone: Stretch To.

### CONSTRAINT_TYPE_CLAMPTO

Tipo de restrição de bone: Clamp To (prende a uma curva).

### CONSTRAINT_TYPE_TRANSFORM

Tipo de restrição de bone: Transformation.

### CONSTRAINT_TYPE_DISTLIMIT

Veja `Range.types.BL_ArmatureConstraint.ik_type`

### CONSTRAINT_IK_COPYPOSE

A constraint tenta igualar a posição e, se for o caso, a rotação do alvo.

**Valor:** `0`

### CONSTRAINT_IK_DISTANCE

A constraint mantém uma certa distância do alvo, conforme ik_mode

**Valor:** `1`

Veja `Range.types.BL_ArmatureConstraint.ik_flag`

### CONSTRAINT_IK_FLAG_TIP

Ligado quando a constraint age na cabeça do osso e não na ponta

**Valor:** `1`

### CONSTRAINT_IK_FLAG_ROT

Ligado quando a constraint tenta igualar a orientação do alvo

**Valor:** `2`

### CONSTRAINT_IK_FLAG_STRETCH

Ligado quando a armature pode esticar (só os ossos com fator de estiramento > 0.0)

**Valor:** `16`

### CONSTRAINT_IK_FLAG_POS

Ligado quando a constraint tenta igualar a posição do alvo.

**Valor:** `32`

Veja `Range.types.BL_ArmatureConstraint.ik_mode`

### CONSTRAINT_IK_MODE_INSIDE

A constraint tenta manter o osso a no máximo ik_dist do alvo

**Valor:** `0`

### CONSTRAINT_IK_MODE_OUTSIDE

A constraint tenta manter o osso a mais de ik_dist do alvo

**Valor:** `1`

### CONSTRAINT_IK_MODE_ONSURFACE

A constraint tenta manter o osso exatamente a ik_dist do alvo.

**Valor:** `2`

## Material do Blender

### BL_DST_ALPHA

Fator de mistura (blend) do material: alfa de destino. Usado em setBlending().

### BL_DST_COLOR

Fator de mistura (blend) do material: cor de destino. Usado em setBlending().

### BL_ONE

Fator de mistura (blend) do material: um (cor inteira). Usado em setBlending().

### BL_ONE_MINUS_DST_ALPHA

Fator de mistura (blend) do material: 1 menos o alfa de destino. Usado em setBlending().

### BL_ONE_MINUS_DST_COLOR

Fator de mistura (blend) do material: 1 menos a cor de destino. Usado em setBlending().

### BL_ONE_MINUS_SRC_ALPHA

Fator de mistura (blend) do material: 1 menos o alfa de origem. Usado em setBlending().

### BL_ONE_MINUS_SRC_COLOR

Fator de mistura (blend) do material: 1 menos a cor de origem. Usado em setBlending().

### BL_SRC_ALPHA

Fator de mistura (blend) do material: alfa de origem. Usado em setBlending().

### BL_SRC_ALPHA_SATURATE

Fator de mistura (blend) do material: alfa de origem saturado. Usado em setBlending().

### BL_SRC_COLOR

Fator de mistura (blend) do material: cor de origem. Usado em setBlending().

### BL_ZERO

## Estado da entrada

Veja `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

### KX_INPUT_NONE

Estado de tecla/botão: solto.

### KX_INPUT_JUST_ACTIVATED

Estado de tecla/botão: acabou de ser apertado.

### KX_INPUT_ACTIVE

Estado de tecla/botão: continua apertado.

### KX_INPUT_JUST_RELEASED

## KX_GameObject

Veja `Range.types.KX_GameObject.playAction`

### KX_ACTION_MODE_PLAY

Toca a ação uma vez.

**Valor:** `0`

### KX_ACTION_MODE_LOOP

Repete a ação em loop.

**Valor:** `1`

### KX_ACTION_MODE_PING_PONG

Toca a ação para a frente e, quando termina, volta para trás.

**Valor:** `2`

### KX_ACTION_BLEND_BLEND

Mistura as camadas por interpolação linear

**Valor:** `0`

### KX_ACTION_BLEND_ADD

Soma as camadas

**Valor:** `1`

## Botões do mouse

Veja `Range.types.SCA_MouseSensor`

### KX_MOUSE_BUT_LEFT

Botão esquerdo do mouse (para o sensor de mouse).

### KX_MOUSE_BUT_MIDDLE

Botão do meio do mouse (para o sensor de mouse).

### KX_MOUSE_BUT_RIGHT

## Modos de desenho da malha de navegação

### RM_WALLS

Desenha só as paredes.

### RM_POLYS

Desenha só os polígonos.

### RM_TRIS

Desenha a malha de triângulos.

## Shader

### VIEWMATRIX

Uniforme de shader com a matriz visão (mundo → câmera). Usado em setUniformDef().

### VIEWMATRIX_INVERSE

Uniforme de shader com a matriz visão (mundo → câmera), inversa. Usado em setUniformDef().

### VIEWMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz visão (mundo → câmera), inversa transposta. Usado em setUniformDef().

### VIEWMATRIX_TRANSPOSE

Uniforme de shader com a matriz visão (mundo → câmera), transposta. Usado em setUniformDef().

### MODELMATRIX

Uniforme de shader com a matriz modelo (objeto → mundo). Usado em setUniformDef().

### MODELMATRIX_INVERSE

Uniforme de shader com a matriz modelo (objeto → mundo), inversa. Usado em setUniformDef().

### MODELMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz modelo (objeto → mundo), inversa transposta. Usado em setUniformDef().

### MODELMATRIX_TRANSPOSE

Uniforme de shader com a matriz modelo (objeto → mundo), transposta. Usado em setUniformDef().

### MODELVIEWMATRIX

Uniforme de shader com a matriz modelo × visão. Usado em setUniformDef().

### MODELVIEWMATRIX_INVERSE

Uniforme de shader com a matriz modelo × visão, inversa. Usado em setUniformDef().

### MODELVIEWMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz modelo × visão, inversa transposta. Usado em setUniformDef().

### MODELVIEWMATRIX_TRANSPOSE

Uniforme de shader com a matriz modelo × visão, transposta. Usado em setUniformDef().

### CAM_POS

Posição da câmera atual

### CONSTANT_TIMER

Uniforme de shader com o tempo do jogo, para animar efeitos.

### EYE

Usa um timer como valor do uniform.

### SHD_TANGENT

## Estados

Veja `Range.types.KX_StateActuator`

### KX_STATE1

Máscara do estado 1 dos logic bricks.

### KX_STATE2

Máscara do estado 2 dos logic bricks.

### KX_STATE3

Máscara do estado 3 dos logic bricks.

### KX_STATE4

Máscara do estado 4 dos logic bricks.

### KX_STATE5

Máscara do estado 5 dos logic bricks.

### KX_STATE6

Máscara do estado 6 dos logic bricks.

### KX_STATE7

Máscara do estado 7 dos logic bricks.

### KX_STATE8

Máscara do estado 8 dos logic bricks.

### KX_STATE9

Máscara do estado 9 dos logic bricks.

### KX_STATE10

Máscara do estado 10 dos logic bricks.

### KX_STATE11

Máscara do estado 11 dos logic bricks.

### KX_STATE12

Máscara do estado 12 dos logic bricks.

### KX_STATE13

Máscara do estado 13 dos logic bricks.

### KX_STATE14

Máscara do estado 14 dos logic bricks.

### KX_STATE15

Máscara do estado 15 dos logic bricks.

### KX_STATE16

Máscara do estado 16 dos logic bricks.

### KX_STATE17

Máscara do estado 17 dos logic bricks.

### KX_STATE18

Máscara do estado 18 dos logic bricks.

### KX_STATE19

Máscara do estado 19 dos logic bricks.

### KX_STATE20

Máscara do estado 20 dos logic bricks.

### KX_STATE21

Máscara do estado 21 dos logic bricks.

### KX_STATE22

Máscara do estado 22 dos logic bricks.

### KX_STATE23

Máscara do estado 23 dos logic bricks.

### KX_STATE24

Máscara do estado 24 dos logic bricks.

### KX_STATE25

Máscara do estado 25 dos logic bricks.

### KX_STATE26

Máscara do estado 26 dos logic bricks.

### KX_STATE27

Máscara do estado 27 dos logic bricks.

### KX_STATE28

Máscara do estado 28 dos logic bricks.

### KX_STATE29

Máscara do estado 29 dos logic bricks.

### KX_STATE30

Veja `Range.types.KX_StateActuator.operation`

### KX_STATE_OP_CLR

Subtrai bits da máscara de estados

**Valor:** `0`

### KX_STATE_OP_CPY

Copia a máscara de estados

**Valor:** `1`

### KX_STATE_OP_NEG

Inverte bits da máscara de estados

**Valor:** `2`

### KX_STATE_OP_SET

Soma bits à máscara de estados

**Valor:** `3`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### deltaTime()

 <small>função</small>

Tempo, em segundos, desde o frame anterior. Multiplique movimentos por ele para não depender do FPS.

**Retorna:** `float`

### freeUnconvertedData(scene)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só no jogo exportado: libera a geometria usada só por objetos da cena deixados de fora pela opção **Convert**. Eles não poderão mais ser convertidos. Retorna os bytes liberados.

**Retorna:** `int`

### getAnimationRate()

 <small>função</small>

Taxa de atualização das animações (vezes por segundo).

**Retorna:** `float`

### getGraphicsCardRenderer()

 <small>função</small>

Nome da placa de vídeo.

**Retorna:** `str`

### getGraphicsCardVendor()

 <small>função</small>

Fabricante da placa de vídeo.

**Retorna:** `str`

### getLoadLog(clear=False)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Relatório dos últimos carregamentos de cena: dicts com `scene`, `stage`, `ms`, `detail` e `total`. Com `clear=True`, limpa depois de ler.

**Retorna:** `list`

### getMessages(to, subject='')

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Mensagens `(assunto, corpo)` que um sensor Message do objeto `to` recebe neste frame.

**Retorna:** `list`

### getObjectConvert(scene, object)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Valor da opção **Convert** do objeto na cena.

**Retorna:** `bool`

### getProcessorName()

 <small>função</small>

Nome do processador.

**Retorna:** `str`

### getRangeFileList(path='')

 <small>função</small>

Arquivos `.range` na pasta do jogo atual (ou em `path`).

**Retorna:** `list`

### getRasecFileList(path='')

 <small>função</small>

Arquivos `.rasec` na pasta do jogo atual (ou em `path`).

**Retorna:** `list`

### getRenderRate()

 <small>função</small>

Taxa de desenho (vezes por segundo).

**Retorna:** `float`

### preloadScene(name)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Converte uma cena com antecedência, no fim deste frame (shaders e texturas incluídos), sem adicioná-la. Depois, um `addScene` ou `replaceScene` dela só insere a cena pronta, sem travar. Chame enquanto uma tela de carregamento estiver aparecendo. Devolve `False` se a cena não existir.

**Retorna:** `bool`

### setAnimationRate(rate)

 <small>função</small>

Muda a taxa de atualização das animações.

### setNeedsParents(count)

 <small>função</small>

Quantas vezes por frame a hierarquia de pais é atualizada (de 3 para 1 economiza CPU).

### setObjectConvert(scene, object, convert, children=True)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Muda a opção **Convert** de um objeto numa cena que ainda não foi carregada. Retorna quantos objetos mudaram.

**Retorna:** `int`

### setRenderRate(rate)

 <small>função</small>

Muda a taxa de desenho.

### KX_GAME_SCREENSHOT

 <small>constante</small>

Modo do atuador Game: tira um print da tela.

### KX_JOYSTICK_BUT_A

 <small>constante</small>

Botão A do controle.

### KX_JOYSTICK_BUT_B

 <small>constante</small>

Botão B do controle.

### KX_JOYSTICK_BUT_BACK

 <small>constante</small>

Botão Back/Select do controle.

### KX_JOYSTICK_BUT_GUIDE

 <small>constante</small>

Botão Guide (botão central) do controle.

### KX_JOYSTICK_BUT_LEFTSHOUDER

 <small>constante</small>

Botão ombro esquerdo (LB) do controle.

### KX_JOYSTICK_BUT_LEFTSTICK

 <small>constante</small>

Botão clique do analógico esquerdo do controle.

### KX_JOYSTICK_BUT_PADDOWN

 <small>constante</small>

Botão direcional para baixo do controle.

### KX_JOYSTICK_BUT_PADLEFT

 <small>constante</small>

Botão direcional para a esquerda do controle.

### KX_JOYSTICK_BUT_PADRIGHT

 <small>constante</small>

Botão direcional para a direita do controle.

### KX_JOYSTICK_BUT_PADUP

 <small>constante</small>

Botão direcional para cima do controle.

### KX_JOYSTICK_BUT_RIGHTSHOUDER

 <small>constante</small>

Botão ombro direito (RB) do controle.

### KX_JOYSTICK_BUT_RIGHTSTICK

 <small>constante</small>

Botão clique do analógico direito do controle.

### KX_JOYSTICK_BUT_X

 <small>constante</small>

Botão X do controle.

### KX_JOYSTICK_BUT_Y

 <small>constante</small>

Botão Y do controle.

### KX_MOUSE_BUT_BUTTON6

 <small>constante</small>

Botão 6 do mouse.

### KX_MOUSE_BUT_BUTTON7

 <small>constante</small>

Botão 7 do mouse.

### KX_MOUSE_BUT_LEFTTHUMBMOUSE

 <small>constante</small>

Botão lateral esquerdo do mouse (polegar).

### KX_MOUSE_BUT_RIGHTTHUMBMOUSE

 <small>constante</small>

Botão lateral direito do mouse (polegar).

### KX_MOVEMENT_ALL_AXIS

 <small>constante</small>

Sensor Movement: vigia todos os eixos.

### KX_MOVEMENT_AXIS_NEG_X

 <small>constante</small>

Sensor Movement: eixo -X.

### KX_MOVEMENT_AXIS_NEG_Y

 <small>constante</small>

Sensor Movement: eixo -Y.

### KX_MOVEMENT_AXIS_NEG_Z

 <small>constante</small>

Sensor Movement: eixo -Z.

### KX_MOVEMENT_AXIS_POS_X

 <small>constante</small>

Sensor Movement: eixo +X.

### KX_MOVEMENT_AXIS_POS_Y

 <small>constante</small>

Sensor Movement: eixo +Y.

### KX_MOVEMENT_AXIS_POS_Z

 <small>constante</small>

Sensor Movement: eixo +Z.

### RAS_2DFILTER_BLOOM

 <small>constante</small>

Filtro 2D: Bloom.

### RAS_2DFILTER_FXAA

 <small>constante</small>

Filtro 2D: FXAA.

### RAS_2DFILTER_LIGHTSCATTER

 <small>constante</small>

Filtro 2D: raios de luz (light scattering).

### RAS_2DFILTER_OUTLINE

 <small>constante</small>

Filtro 2D: contorno (outline).

### RAS_2DFILTER_SSAO

 <small>constante</small>

Filtro 2D: oclusão de ambiente (SSAO).

### RAS_2DFILTER_SSR

 <small>constante</small>

Filtro 2D: reflexos em tela (SSR).

### RAS_2DFILTER_TONEMAP

 <small>constante</small>

Filtro 2D: tonemap.

