# Range.logic - métodos e funções

Parte de [Range.logic](Range.logic.md).

## getCurrentController()

Pega o controlador Python ligado a este script.

**Tipo do retorno:** `Range.types.SCA_PythonController`

## getCurrentScene()

Pega a cena atual.

**Tipo do retorno:** `Range.types.KX_Scene`

## getSceneList()

Pega a lista das cenas carregadas na engine agora.

**Tipo do retorno:** list of `Range.types.KX_Scene`

> **Note:**
As cenas do arquivo blend que não foram convertidas não aparecem nesta lista. Ela só traz cenas como as de overlay.

## getInactiveSceneNames()

Pega a lista dos nomes das cenas que não estão carregadas na engine.

**Tipo do retorno:** list of string

## loadGlobalDict()

Carrega Range.logic.globalDict de um arquivo.

## saveGlobalDict()

Salva Range.logic.globalDict num arquivo.

## startGame(blend)

Carrega o arquivo blend.

- **`blend`**: O nome do arquivo blend
  - tipo: string

## endGame()

Encerra o jogo atual.

## restartGame()

Reinicia o jogo atual recarregando o arquivo .blend (a última versão salva, não o que está rodando agora).

## LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

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

> **Note:**
Bibliotecas carregadas de forma assíncrona não ficam disponíveis logo que LibLoad() retorna. Use o KX_LibLoadStatus devolvido para saber quando elas estão prontas.

## LibNew(name, type, data)

Usa dados de um datablock que já existe e carrega como uma biblioteca nova.

- **`name`**: Um nome único para a biblioteca, usado depois para removê-la
  - tipo: string
- **`type`**: O tipo de datablock (por enquanto só "Mesh" é suportado)
  - tipo: string
- **`data`**: Lista com os nomes dos datablocks a carregar
  - tipo: list of strings

## LibFree(name)

Libera uma biblioteca, removendo todos os objetos e malhas dela das cenas ativas.

- **`name`**: O nome da biblioteca a liberar (o nome usado em LibNew)
  - tipo: string

## LibList()

Devolve a lista das bibliotecas carregadas agora.

**Tipo do retorno:** list [str]

## setLibLoadFrameBudget([ms])

Tempo por frame, em milissegundos, que o LibLoad assíncrono pode gastar juntando as bibliotecas carregadas à cena (texturas, shaders, objetos). O padrão de 8 mantém o frame rate do jogo; uma tela de carregamento pode aumentar (ex.: 30) para terminar antes com frame rate menor, e depois voltar o valor.

- **`ms`**: Novo limite; se omitido, só devolve o atual.
  - tipo: float

**Retorna:** O limite atual em milissegundos.

**Tipo do retorno:** float

## addScene(name, overlay=1, asynchronous=False)

Carrega uma cena na engine.

> **Note:**
Esta função não tem efeito na hora: a cena entra na fila e é adicionada no próximo ciclo de lógica, quando aparece em `getSceneList`

- **`name`**: O nome da cena
  - tipo: string
- **`overlay`**: Overlay ou underlay (opcional)
  - tipo: integer
- **`asynchronous`**: Compila os shaders da cena aos poucos a cada frame (limite de `setLibLoadFrameBudget`) antes de a cena entrar em `getSceneList`, para a tela de carregamento continuar desenhando; a lógica da cena só começa depois disso.
  - tipo: boolean

## sendMessage(subject, body="", to="", message_from="")

Envia uma mensagem para os sensores de qualquer cena ativa.

- **`subject`**: O assunto da mensagem
  - tipo: string
- **`body`**: O corpo da mensagem (opcional)
  - tipo: string
- **`to`**: O nome do objeto que vai receber a mensagem (opcional)
  - tipo: string
- **`message_from`**: O nome do objeto de onde a mensagem vem (opcional)
  - tipo: string

## setGravity(gravity)

Define a gravidade do mundo.

- **`gravity`**: O vetor de gravidade
  - tipo: Vector((fx, fy, fz))

## getSpectrum() (Deprecated)

Devolve uma lista de 512 pontos da placa de som. Só funciona com o driver de som fmod.

**Tipo do retorno:** list [float], len(getSpectrum()) == 512

## getMaxLogicFrame()

Pega o número máximo de frames de lógica por frame de render.

**Retorna:** O número máximo de frames de lógica por frame de render

**Tipo do retorno:** integer

## setMaxLogicFrame(maxlogic)

Define o número máximo de frames de lógica executados por frame de render. Não afeta a física, que continua rodando no frame rate completo.

- **`maxlogic`**: O novo número máximo de frames de lógica por frame de render. Valores válidos: 1..5
  - tipo: integer

## ~~getMaxPhysicsFrame()~~

> **Obsoleto :**
Nenhuma parte da engine usa este limite; o valor definido aqui não tem efeito. Fica só por compatibilidade com scripts antigos. Ele também não controla mais o culling de sombras, que antes usava esta mesma configuração.

Pega o último valor passado para `setMaxPhysicsFrame`.

**Retorna:** O último valor definido (padrão: 5)

**Tipo do retorno:** integer

## ~~setMaxPhysicsFrame(maxphysics)~~

> **Obsoleto :**
Nenhuma parte da engine usa este limite; chamar isto não tem efeito na física nem nas sombras. Fica só por compatibilidade com scripts antigos.

Guarda o valor para ler depois com `getMaxPhysicsFrame`. Era documentado como o número máximo de passos de física por frame de render, mas nenhum código da engine lê o valor para isso.

- **`maxphysics`**: O novo número máximo de passos de física por frame de render. Valores válidos: 1..5.
  - tipo: integer

## getLogicTicRate()

Pega a frequência de atualização da lógica.

**Retorna:** A frequência da lógica em Hz

**Tipo do retorno:** float

## setLogicTicRate(ticrate)

Define a frequência de atualização da lógica.

A frequência da lógica é quantas vezes por segundo os logic bricks são executados. O padrão é 60 Hz.

- **`ticrate`**: A nova frequência da lógica (em Hz).
  - tipo: float

## getPhysicsTicRate()

Pega a frequência de atualização da física

**Retorna:** A frequência da física em Hz

**Tipo do retorno:** float

## setPhysicsTicRate(ticrate)

Define a frequência de atualização da física

A frequência da física é quantas vezes por segundo a física é executada. O padrão é 60 Hz.

- **`ticrate`**: A nova frequência (em Hz).
  - tipo: float

## getExitKey()

Pega a tecla usada para sair da engine

**Retorna:** A tecla (padrão: `Range.events.ESCKEY`)

**Tipo do retorno:** int

## setExitKey(key)

Define a tecla usada para sair da engine

- **`key`**: Uma constante de tecla de `Range.events`
  - tipo: int

## NextFrame()

Renderiza o próximo frame (se o Python estiver no controle)

## setRender(render)

Define a opção global que controla o render da cena. Se for True, o render acontece depois do frame de lógica. Se for False, o render é pulado e outro frame de lógica começa na hora.

> **Note:**
Com o render desligado, o VSync da GPU não limita mais os frames por segundo, mas a opção *Use Frame Rate* continua regulando o fps. Para rodar o máximo de frames possível, desmarque essa opção (Render Properties, painel System).

- **`render`**: A opção de render
  - tipo: bool

## getRender()

Pega o valor atual da opção global de render

**Retorna:** O valor da opção

**Tipo do retorno:** bool

## getClockTime()

Pega o tempo de render atual da engine, em segundos. É o tempo de simulação correspondente à próxima cena que será renderizada.

**Tipo do retorno:** double

## getFrameTime()

Pega o tempo de frame atual da engine, em segundos. É o tempo de simulação correspondente à chamada atual da lógica. Em geral, é este o tempo que interessa.

**Tipo do retorno:** double

## getRealTime()

Pega quantos segundos reais (do relógio do sistema) passaram desde o começo da simulação.

**Tipo do retorno:** double

## getTimeScale()

Pega o multiplicador entre o tempo real e o tempo da simulação. O padrão é 1.0. Valores maiores que 1.0 deixam a simulação mais rápida que o tempo real; valores menores, mais lenta.

**Tipo do retorno:** double

## setTimeScale(time_scale)

Define o multiplicador entre o tempo real e o tempo da simulação. Valores maiores que 1.0 deixam a simulação mais rápida que o tempo real; valores menores, mais lenta. Valores muito altos podem deixar a física instável.

A escala vale para todos os relógios do jogo: física, timers, `getFrameTime`, actions e cutscenes. O valor 0.0 pausa a lógica, então nenhum logic brick ou script roda até a escala mudar de novo; retome de fora da lógica do jogo, ou pause com `KX_Scene.suspend`.

- **`time_scale`**: O novo multiplicador de tempo.

## setAnimationsUseTimeScale(use)

Escolhe se as ações seguem o `setTimeScale`. Com `False` o relógio das animações avança pelo passo de lógica sem escala, então as ações tocam em velocidade normal enquanto física, timers e lógica continuam escalados. Padrão `True`.

- **`use`**: `True` para escalar as animações, `False` para mantê-las em velocidade normal.
  - tipo: bool

## getAnimationsUseTimeScale()

**Retorna:** `True` se as ações seguem a escala de tempo.

**Tipo do retorno:** bool

## ~~getUseExternalClock()~~

> **Obsoleto 0.5.5:**
A flag não tem efeito; a simulação sempre usa o próprio relógio.

**Tipo do retorno:** bool

## ~~setUseExternalClock(use_external_clock)~~

> **Obsoleto 0.5.5:**
Não tem efeito na simulação e emite um `DeprecationWarning`.

- **`use_external_clock`**: A nova configuração

## setClockTime(new_time)

Define o próximo valor do relógio da simulação. É melhor usar este método numa função main própria em Python: chamá-lo num logic brick pode travar o sistema facilmente (se o tempo não avançar o bastante para rodar pelo menos o próximo passo de lógica).

- **`new_time`**: O próximo valor do relógio da engine (em segundos).

## expandPath(path)

Converte um caminho interno do Blender num caminho de verdade do sistema de arquivos.

Use / como separador de pastas no caminho. Use '//' no começo para um caminho relativo; o Blender troca isso pela pasta do .blend ou do executável atual para formar o caminho completo. A função também converte o separador para o formato do sistema.

- **`path`**: O caminho a converter/expandir.
  - tipo: string

**Retorna:** O caminho convertido

**Tipo do retorno:** string

## getAverageFrameRate()

Pega o frame rate médio estimado de todas as cenas ativas, não só da atual.

**Retorna:** O frame rate médio estimado, em frames por segundo

**Tipo do retorno:** float

## getBlendFileList(path = "//")

Devolve a lista dos arquivos blend na mesma pasta do arquivo blend aberto, ou na pasta passada como argumento.

- **`path`**: Pasta opcional, que é expandida (como em expandPath) para o caminho completo.
  - tipo: string

**Retorna:** Lista de nomes de arquivo, sem a pasta na frente

**Tipo do retorno:** list

## getRandomFloat()

Devolve um número decimal aleatório no intervalo [0 - 1)

## PrintGLInfo()

Mostra no console as informações das extensões GL

## PrintMemInfo()

Mostra no console as estatísticas da engine

## getProfileInfo()

Devolve um dicionário Python com as mesmas informações do profiler na tela. As chaves são as categorias do profiler, e os valores são tuplas com o tempo gasto (em ms) no primeiro elemento e a porcentagem do tempo total no segundo.

## getRenderStats()

Devolve um dicionário Python com contadores inteiros do último frame completo, os mesmos números que as consultas de render do Debug Mode mostram. Diferente dos tempos de `getProfileInfo`, eles não dependem do hardware nem do relógio, por isso são o que testes A/B devem comparar.

Contadores do rasterizador, cobrindo todas as passadas do frame (câmera principal, sombras, filtros 2D):

* `drawCalls`: draw calls feitas.
* `materialBinds`: binds de material (programa de shader).
* `lightBinds`: envios dos uniforms das luzes da cena e das lâmpadas com sombra. O conjunto de luzes é constante por camada de luz, então isto conta quantas vezes os mesmos valores foram reenviados.

Contadores da cena ativa:

* `cullingTotal`, `cullingTested`, `cullingVisible`: objetos na lista de render, testados contra o frustum/DBVT e achados visíveis, na última passada de culling da câmera principal.
* `lightsTotal`, `lightsShadowUpdated`, `shadowPasses`: luzes da cena, luzes cujo buffer de sombra foi atualizado e passadas de sombra renderizadas (cada divisão de cascata conta como uma).
* `sensors`, `controllersTriggered`, `actuatorsUpdated`: sensores registrados e controladores/atuadores executados no frame de lógica. Atenção: estes dois são contados enquanto o frame roda, e um controlador Python que chama esta função faz parte desse frame; ele só vê o que rodou antes dele, então num controlador o valor costuma ser 0. A sobreposição do Debug Mode lê os valores depois do frame e mostra a contagem completa. Os contadores do rasterizador e do culling não têm esse problema: sempre vêm do último frame completo.

## deltaTime()

 `função`

Tempo, em segundos, desde o frame anterior. Multiplique movimentos por ele para não depender do FPS.

**Retorna:** `float`

## freeUnconvertedData(scene)

*(novo na Anastacio)* `função`

Só no jogo exportado: libera a geometria usada só por objetos da cena deixados de fora pela opção **Convert**. Eles não poderão mais ser convertidos. Retorna os bytes liberados.

**Retorna:** `int`

## getAnimationRate()

 `função`

Taxa de atualização das animações (vezes por segundo).

**Retorna:** `float`

## getGraphicsCardRenderer()

 `função`

Nome da placa de vídeo.

**Retorna:** `str`

## getGraphicsCardVendor()

 `função`

Fabricante da placa de vídeo.

**Retorna:** `str`

## getLoadLog(clear=False)

*(novo na Anastacio)* `função`

Relatório dos últimos carregamentos de cena: dicts com `scene`, `stage`, `ms`, `detail` e `total`. Com `clear=True`, limpa depois de ler.

**Retorna:** `list`

## getMessages(to, subject='')

*(novo na Anastacio)* `função`

Mensagens `(assunto, corpo)` que um sensor Message do objeto `to` recebe neste frame.

**Retorna:** `list`

## getObjectConvert(scene, object)

*(novo na Anastacio)* `função`

Valor da opção **Convert** do objeto na cena.

**Retorna:** `bool`

## getProcessorName()

 `função`

Nome do processador.

**Retorna:** `str`

## getRangeFileList(path='')

 `função`

Arquivos `.range` na pasta do jogo atual (ou em `path`).

**Retorna:** `list`

## getRasecFileList(path='')

 `função`

Arquivos `.rasec` na pasta do jogo atual (ou em `path`).

**Retorna:** `list`

## getRenderRate()

 `função`

Taxa de desenho (vezes por segundo).

**Retorna:** `float`

## preloadScene(name)

*(novo na Anastacio)* `função`

Converte uma cena com antecedência, no fim deste frame (shaders e texturas incluídos), sem adicioná-la. Depois, um `addScene` ou `replaceScene` dela só insere a cena pronta, sem travar. Chame enquanto uma tela de carregamento estiver aparecendo. Devolve `False` se a cena não existir.

**Retorna:** `bool`

## setAnimationRate(rate)

 `função`

Muda a taxa de atualização das animações.

## setNeedsParents(count)

 `função`

Quantas vezes por frame a hierarquia de pais é atualizada (de 3 para 1 economiza CPU).

## setObjectConvert(scene, object, convert, children=True)

*(novo na Anastacio)* `função`

Muda a opção **Convert** de um objeto numa cena que ainda não foi carregada. Retorna quantos objetos mudaram.

**Retorna:** `int`

## setRenderRate(rate)

 `função`

Muda a taxa de desenho.
