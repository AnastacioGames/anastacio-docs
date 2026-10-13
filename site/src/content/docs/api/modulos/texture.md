---
title: "Range.texture"
description: "Referência do módulo Range.texture"
---

:::tip[Veja também]
[`Texture`](../../types/texture/), [`KX_BlenderMaterial`](../../types/kx_blendermaterial/), [`BL_Texture`](../../types/bl_texture/)
:::

## Introdução

O módulo `Range.texture` permite manipular texturas durante o jogo. A textura pode vir de várias fontes: arquivos de vídeo, arquivos de imagem, captura de vídeo, buffer de memória, render de câmera ou uma mistura disso. Os arquivos de vídeo e imagem podem ser carregados da Internet usando uma URL em vez de um nome de arquivo. Também dá para aplicar filtros nas imagens antes de enviá-las à GPU, para efeitos de vídeo: blue screen, faixa de cor, cinza, normal map. `Range.texture` usa o FFmpeg para carregar imagens e vídeos. Todos os formatos e codecs que o FFmpeg suporta são suportados por `Range.texture`, incluindo, entre outros:

* AVI
* Ogg
* Xvid
* Theora
* câmera dv1394
* placa de captura video4linux (inclui muitas webcams)
* placa de captura videoForWindows (inclui muitas webcams)
* JPG

## Como funciona

O princípio é simples: primeiro você identifica uma textura num objeto existente com a função `materialID`, depois cria uma nova textura com conteúdo dinâmico e troca as duas texturas na GPU.

A game engine não percebe a troca e continua mostrando o objeto como sempre, só que agora você controla a textura.

Quando o objeto de textura é apagado, a textura nova é apagada e a antiga é restaurada.

## Preparando o jogo

Antes de usar o módulo `Range.texture`, você precisa de objetos com texturas aplicadas do jeito certo.

Imagine que você quer uma televisão mostrando programas ao vivo no jogo. Você cria um objeto televisão e aplica por UV uma textura diferente no lugar da tela, por exemplo `tv.png`. A aparência dessa textura não importa; provavelmente você vai querer um cinza escuro para simular a TV desligada. Quando a televisão precisar ligar, você cria uma textura dinâmica a partir de uma placa de captura de vídeo e usa no lugar de `tv.png`: a tela da TV ganha vida.

Há dois jeitos de definir texturas que `Range.texture` consegue pegar:

- Textura UV simples.
- Material do Blender com canal de textura de imagem.

Como `Range.texture` trabalha no nível da textura, ele é compatível com todos os recursos de textura da game engine: GLSL, multitextura, shaders personalizados etc.

## Exemplos

## Classes de vídeo

Fonte de vídeo FFmpeg, usada para arquivos de vídeo, capturas de vídeo ou streams de vídeo.

- **`file`**: Caminho do vídeo a carregar; se capture >= 0 no Windows, este parâmetro não é usado.
  - tipo: str
- **`capture`**: Número do dispositivo de captura; se >= 0, a webcam correspondente é usada (opcional).
  - tipo: int
- **`rate`**: Taxa de captura (opcional, só usado se capture >= 0).
  - tipo: float
- **`width`**: Largura da captura (opcional, só usado se capture >= 0).
  - tipo: int
- **`height`**: Altura da captura (opcional, só usado se capture >= 0).
  - tipo: int

### status

Status do vídeo (somente leitura).

**Tipo:** int

**Valor:** `see `FFmpeg Video and Image Status`_.`

### range

O tempo de início e fim da reprodução, em segundos desde o começo. Por padrão, o vídeo inteiro.

**Tipo:** sequence of two floats

### repeat

Número de vezes que o vídeo repete; -1 para repetir sem parar.

**Tipo:** int

### framerate

Frame rate relativo: <1.0 para lento, >1.0 para rápido.

**Tipo:** float

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### scale

Use True para ligar o algoritmo rápido de escala por vizinho mais próximo. A largura e a altura da textura precisam ser potência de 2. Se o tamanho da imagem do vídeo não for potência de 2, é preciso reescalar. Por padrão, `Range.texture` usa a função `gluScaleImage()`, precisa mas lenta. O melhor é reescalar o vídeo antes, para não precisar escalar em tempo de execução!

**Tipo:** bool

### flip

Com True, a imagem é espelhada na vertical. O FFmpeg sempre entrega a imagem de cabeça para baixo, por isso este atributo vem True por padrão.

**Tipo:** bool

### filter

Um filtro adicional aplicado no vídeo antes de enviá-lo à GPU.

**Tipo:** one of: * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### preseek

Número de frames de pré-busca.

**Tipo:** int

### deinterlace

Desentrelaça a imagem.

**Tipo:** bool

### play()

Toca (reinicia) o vídeo.

**Retorna:** Se o vídeo estava pronto ou parado.

**Tipo do retorno:** bool

### pause()

Pausa o vídeo.

**Retorna:** Se o vídeo estava tocando.

**Tipo do retorno:** bool

### stop()

Para o vídeo (play toca de novo desde o início).

**Retorna:** Se o vídeo estava tocando.

**Tipo do retorno:** bool

### refresh(buffer=None, format="RGBA", timestamp=-1.0)

Atualiza o vídeo: pega o status e, se quiser, copia o frame para um buffer externo.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str
- **`timestamp`**: Um timestamp opcional (em segundos desde o início do filme) do frame a copiar para o buffer.
  - tipo: float

**Retorna:** veja `FFmpeg Video and Image Status`_.

**Tipo do retorno:** int

## Classes de imagem

Fonte de imagem FFmpeg, usada para arquivos de imagem e imagens da web.

- **`file`**: Caminho da imagem a carregar.
  - tipo: str

### status

Status da imagem (somente leitura).

**Tipo:** int

**Valor:** `see `FFmpeg Video and Image Status`_.`

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

### flip

Espelha a imagem na vertical.

**Tipo:** bool

### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### refresh(buffer=None, format="RGBA")

Atualiza a imagem: pega o status e, se quiser, copia o frame para um buffer externo.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

**Retorna:** veja `FFmpeg Video and Image Status`_.

**Tipo do retorno:** int

### reload(newname=None)

Recarrega a imagem, ou seja, abre de novo.

- **`newname`**: Caminho para uma nova imagem (opcional).
  - tipo: str

Imagem vinda da memória da aplicação. Para imagens geradas pelo computador, aplicativos de desenho.

- **`width`**: Largura da imagem.
  - tipo: int
- **`height`**: Altura da imagem.
  - tipo: int
- **`color`**: Valor para iniciar os canais RGB. O buffer iniciado terá todos os pixels em (color, color, color, 255) (opcional).
  - tipo: int in [0, 255]
- **`scale`**: A imagem usa escala (opcional).
  - tipo: bool

### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Espelha a imagem na vertical.

**Tipo:** bool

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### load(imageBuffer, width, height)

Carrega a imagem de um buffer.

- **`imageBuffer`**: Buffer de onde carregar a imagem.
  - tipo: `Buffer` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Largura da imagem a carregar.
  - tipo: int
- **`height`**: Altura da imagem a carregar.
  - tipo: int

### plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY)

Atualiza o buffer da imagem.

- **`imageBuffer`**: Buffer de onde carregar os dados novos.
  - tipo: `Buffer`, `ImageBuff` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Largura dos dados a carregar.
  - tipo: int
- **`height`**: Altura dos dados a carregar.
  - tipo: int
- **`positionX`**: Borda esquerda da região onde desenhar.
  - tipo: int
- **`positionY`**: Borda de cima da região onde desenhar.
  - tipo: int
- **`mode`**: Modo de desenho; veja `Image Blending Modes`_.
  - tipo: int

### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

Fonte de imagem a partir de um espelho.

- **`scene`**: Cena de onde a imagem deve ser tirada.
  - tipo: `KX_Scene`
- **`observer`**: Objeto de referência do espelho (o objeto de onde o espelho é olhado, por exemplo uma câmera).
  - tipo: `KX_GameObject`
- **`mirror`**: Objeto que tem o espelho.
  - tipo: `KX_GameObject`
- **`material`**: ID do material do espelho usado no reflexo (opcional).
  - tipo: int
- **`width`**: Largura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`height`**: Altura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`samples`**: Amostras do buffer de render fora da tela (opcional).
  - tipo: integer
- **`hdr`**: Formato da imagem fora da tela (opcional).
  - tipo: One of `these constants`

### alpha

Usa alpha na textura.

**Tipo:** bool

### horizon

Cor do horizonte.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

### zenith

Cor do zênite.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

### background

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

Obsoleto; use `Range.texture.ImageMirror.horizon` ou `Range.texture.ImageMirror.zenith`.

### updateShadow

Força a atualização do buffer de sombras se houver diferença entre a imagem renderizada e as sombras.

**Tipo:** bool

### colorBindCode

Bind code da textura de cor fora da tela.

**Tipo:** integer

### capsize

Tamanho da área de render.

**Tipo:** sequence of two ints

### clip

Distância de recorte.

**Tipo:** float in [0.01, 5000.0]

### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Espelha a imagem na vertical.

**Tipo:** bool

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### refresh(buffer=None, format="RGBA")

Atualiza a imagem: renderiza e copia a imagem para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é renderizada e copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### whole

Usa a viewport inteira no render.

**Tipo:** bool

Mixer de imagens, usado para misturar várias fontes de imagem.

### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Espelha a imagem na vertical.

**Tipo:** bool

### getSource(id)

Pega a fonte de imagem.

- **`id`**: Identificador da fonte a pegar.
  - tipo: str

**Retorna:** Fonte de imagem.

**Tipo do retorno:** one of... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

### getWeight(id)

Pega o peso da fonte de imagem.

- **`id`**: Identificador da fonte.
  - tipo: str

**Retorna:** Peso da fonte.

**Tipo do retorno:** int

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### refresh(buffer=None, format="RGBA")

Atualiza a imagem: calcula e copia a imagem para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é calculada e copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### setSource(id, image)

Define a fonte de imagem; todas as fontes precisam ter o mesmo tamanho.

- **`id`**: Identificador da fonte a definir.
  - tipo: str
- **`image`**: Fonte de imagem do tipo... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

### setWeight(id, weight)

Define o peso da fonte de imagem; a soma dos pesos deve ser 256 para ter intensidade de cor completa na saída.

- **`id`**: Identificador da fonte.
  - tipo: str
- **`weight`**: Peso da fonte.
  - tipo: int

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

Fonte de imagem a partir do render de uma câmera não ativa. O render é feito num framebuffer object personalizado se fbo for passado; senão, no framebuffer padrão.

- **`scene`**: Cena de onde a imagem deve ser tirada.
  - tipo: `KX_Scene`
- **`camera`**: Câmera de onde a imagem deve ser tirada.
  - tipo: `KX_Camera`
- **`width`**: Largura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`height`**: Altura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`samples`**: Amostras do buffer de render fora da tela (opcional).
  - tipo: integer
- **`hdr`**: Formato da imagem fora da tela (opcional).
  - tipo: One of `these constants`

### alpha

Usa alpha na textura.

**Tipo:** bool

### horizon

Cor do horizonte.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

### zenith

Cor do zênite.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

### background

Cor de fundo.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

Obsoleto; use `Range.texture.ImageRender.horizon` ou `Range.texture.ImageRender.zenith`.

### updateShadow

Força a atualização do buffer de sombras se houver diferença entre a imagem renderizada e as sombras.

**Tipo:** bool

### colorBindCode

Bind code da textura de cor fora da tela.

**Tipo:** integer

### capsize

Tamanho da área de render.

**Tipo:** sequence of two ints

### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Espelha a imagem na vertical.

**Tipo:** bool

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### whole

Usa a viewport inteira no render.

**Tipo:** bool

### depth

Usa o componente de profundidade do render como array de float; não serve como fonte de textura, só deve ser usado com Range.texture.imageToArray(mode='F').

**Tipo:** bool

### zbuff

Usa o componente de profundidade do render como cor em tons de cinza; serve como fonte de textura.

**Tipo:** bool

### render()

Renderiza a cena, mas ainda não extrai os pixels. A função volta assim que os comandos de render são enviados à GPU. O render continua assíncrono na GPU enquanto o host faz outras tarefas. Para terminar o render, chame `refresh` diretamente ou atualize a textura da qual este objeto é a fonte. Este método serve para fazer render assíncrono com o melhor desempenho: chame render() no frame n e refresh() no frame n+1, para dar o máximo de tempo à GPU para renderizar enquanto a game engine faz outras tarefas.

**Retorna:** True se o render foi iniciado, False se não dá para renderizar (por exemplo, a câmera está ativa)

**Tipo do retorno:** bool

### refresh()

### refresh(buffer, format="RGBA")

Atualiza: renderiza e, se quiser, copia a imagem para um buffer externo, depois invalida o conteúdo atual. O render pode ter sido iniciado antes com o método `render`; nesse caso esta função só espera as operações de render terminarem. Chamada sem argumento, os pixels não são extraídos, mas o render com certeza está completo quando a função volta. Isso só faz sentido com render fora da tela num alvo de textura (veja `offScreenCreate`).

- **`buffer`**: Um objeto que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada. A transferência para o buffer é ideal se a imagem não precisar de processamento, o que acontece com `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` e nenhum filtro.
  - tipo: any buffer type of sufficient size
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

**Retorna:** True se o render terminou, False se não dá para renderizar (por exemplo, a câmera está ativa)

**Tipo do retorno:** bool

Fonte de imagem a partir da viewport renderizada pela câmera ativa. Para renderizar de uma câmera não ativa, veja `ImageRender`.

### alpha

Usa alpha na textura.

**Tipo:** bool

### capsize

Tamanho da área da viewport capturada.

**Tipo:** sequence of two ints

### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Espelha a imagem na vertical.

**Tipo:** bool

### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

### position

Canto superior esquerdo da área capturada.

**Tipo:** sequence of two ints

### refresh(buffer=None, format="RGBA")

Atualiza: copia a viewport para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada. A transferência para o buffer é ideal se a imagem não precisar de processamento, o que acontece com `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` e nenhum filtro.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### whole

Usa a viewport inteira na captura.

**Tipo:** bool

### depth

Usa o componente de profundidade da viewport como array de float; não serve como fonte de textura, só deve ser usado com `Range.texture.imageToArray(mode='F')`.

**Tipo:** bool

### zbuff

Usa o componente de profundidade da viewport como cor em tons de cinza; serve como fonte de textura.

**Tipo:** bool

Fonte de imagem de um stream de vídeo externo capturado com uma placa DeckLink da Black Magic Design. Antes de usar esta fonte, é preciso instalar um dispositivo DeckLink (placa PCIe ou dispositivo USB) e o pacote 'Desktop Video' (versão 10.4 ou mais nova) no host, como descrito na documentação da DeckLink. Se você também tiver uma placa nVidia Quadro recente, pode aproveitar a tecnologia 'GPUDirect' para enviar os frames capturados à GPU de forma bem eficiente. Para isso, instale o 'DeckLink SDK' versão 10.4 ou mais nova e copie a biblioteca 'dvp.dll' para a pasta de instalação do Blender ou para outro lugar de onde o Blender consiga carregar uma DLL.

- **`format`**: string que descreve o formato de vídeo a capturar.
  - tipo: str
- **`capture`**: Número da placa de onde o vídeo de entrada deve ser capturado.
  - tipo: int
O argumento format deve ser escrito como `<displayMode>/<pixelFormat>[/3D][:<cacheSize>]`, em que `<displayMode>` descreve o tamanho e a taxa do frame e <pixelFormat> a codificação dos pixels. O sufixo opcional `/3D` é usado se o stream for estéreo, com imagens de olho esquerdo e direito. O sufixo opcional `:<cacheSize>` define quantos frames ficam em cache, 8 por padrão. Algumas placas DeckLink não funcionam abaixo de um certo tamanho de cache. O padrão 8 deve servir para todas as placas. Dá para tentar diminuir o cache para usar menos memória. Por exemplo, a 4K Extreme funciona com só 3 frames, a Extreme 2 precisa de 4 e a Intensity Shuttle de 6, e assim por diante. Diminuir o cache pode ajudar quando a DeckLink é usada com GPUDirect: nesse caso todos os frames precisam ficar travados na memória, o que pesa muito. Se diminuir demais, não dá erro, mas também não chega vídeo.

Os valores válidos de `<displayMode>` vêm do enum `BMDDisplayMode` da API DeckLink, sem o prefixo 'bmdMode'. Se um modo que não está nesta lista for adicionado numa versão futura do SDK, também dá para passar as 4 letras do código interno desse modo. O código interno está no arquivo `DeckLinkAPIModes.h`, que faz parte do SDK. Para referência, esta é a lista completa dos modos de exibição suportados com o código interno equivalente:

Códigos internos
- NTSC 'ntsc'
- NTSC2398 	'nt23'
- PAL		'pal '
- NTSCp		'ntsp'
- PALp		'palp'
Modos HD 1080
- HD1080p2398	'23ps'
- HD1080p24	'24ps'
- HD1080p25	'Hp25'
- HD1080p2997	'Hp29'
- HD1080p30	'Hp30'
- HD1080i50	'Hi50'
- HD1080i5994	'Hi59'
- HD1080i6000	'Hi60'
- HD1080p50	'Hp50'
- HD1080p5994	'Hp59'
- HD1080p6000	'Hp60'
Modos HD 720
- HD720p50	'hp50'
- HD720p5994	'hp59'
- HD720p60	'hp60'
Modos 2k
- 2k2398	'2k23'
- 2k24		'2k24'
- 2k25		'2k25'
Modos 4k
- 4K2160p2398	'4k23'
- 4K2160p24	'4k24'
- 4K2160p25	'4k25'
- 4K2160p2997	'4k29'
- 4K2160p30	'4k30'
- 4K2160p50	'4k50'
- 4K2160p5994	'4k59'
- 4K2160p60	'4k60'

A maioria dos nomes é autoexplicativa. Se precisar, consulte a documentação da API DeckLink para mais informações.

Do mesmo jeito, <pixelFormat> vem do enum BMDPixelFormat.

Para referência, esta é a lista completa dos formatos de pixel suportados com o código interno equivalente:

Formatos de pixel
- 8BitYUV	'2vuy'
- 10BitYUV	'v210'
- 8BitARGB	* sem código equivalente *
- 8BitBGRA	'BGRA'
- 10BitRGB	'r210'
- 12BitRGB	'R12B'
- 12BitRGBLE	'R12L'
- 10BitRGBXLE	'R10l'
- 10BitRGBX	'R10b'

Consulte a documentação do DeckLink SDK para a descrição completa desses formatos de pixel. É importante entendê-los, porque a decodificação dos pixels NÃO é feita no VideoTexture, por desempenho. Em vez disso, é preciso usar um shader específico para decodificar o pixel na GPU. Só os formatos '8BitARGB', '8BitBGRA' e '10BitRGBXLE' são mapeados direto para texturas OpenGL RGB float. Os formatos '8BitYUV' e '10BitYUV' são mapeados para textura OpenGL RGB float, mas precisam de shader para decodificar. Os outros formatos são enviados como textura `GL_RED_INTEGER` (ou seja, uma textura só com o canal vermelho, codificado como inteiro sem sinal de 32 bits) e não são recomendados.

Exemplo: `HD1080p24/10BitYUV/3D:4` equivale a `24ps/v210/3D:4` e representa um vídeo estéreo full HD a 24 frames por segundo, com cache de 4 frames.

Embora alguns dispositivos DeckLink consigam detectar o formato de vídeo sozinhos, essa API NÃO está implementada na BGE. Por isso é importante passar a string de formato que corresponde exatamente ao vídeo. Se o formato estiver errado, nenhum frame é capturado. Repare que o formato de pixel que você precisa passar não é necessariamente o formato real do vídeo. Por exemplo, a placa 4K Extreme entrega pixels RGB de 8 bits no formato '10BitRGBXLE'. Use o aplicativo 'Media Express', que vem com o 'Desktop Video', para descobrir qual formato de pixel funciona com um stream de vídeo.

### status

Status da captura: 1=pronta para uso, 2=capturando, 3=parada

**Tipo:** int

### framerate

Frame rate da captura, calculado a partir do formato de vídeo.

**Tipo:** float

### valid

Diz se o atributo image pode ser usado para pegar a imagem. Sempre False nesta implementação (a imagem não fica disponível no Python)

**Tipo:** bool

### image

Os dados da imagem. Sempre None nesta implementação.

**Tipo:** `Buffer` or None

### size

O tamanho do frame em pixels. Frames estéreo têm o dobro da altura do frame de vídeo, ou seja, o 3D chega à GPU como uma única imagem em ordem de cima para baixo, com o olho esquerdo em cima.

**Tipo:** (int,int)

### scale

Não usado neste objeto.

**Tipo:** bool

### flip

Não usado neste objeto.

**Tipo:** bool

### filter

Não usado neste objeto.

### play()

Inicia a captura depois de criar o objeto.

**Retorna:** True se a captura começou, False se não.

**Tipo do retorno:** bool

### pause()

Para a captura temporariamente. Use play() para reiniciar.

**Retorna:** True se a captura foi pausada, False se não.

**Tipo do retorno:** bool

### stop()

Para a captura.

**Retorna:** True se a captura foi parada, False se não.

**Tipo do retorno:** bool

## Classes de textura

Classe que cria o objeto `Texture`, que carrega a textura dinâmica na GPU.

- **`gameObj`**: Game object em que a textura de vídeo será criada.
  - tipo: `KX_GameObject`
- **`materialID`**: ID do material; o padrão 0 é o primeiro material (opcional).
  - tipo: int
- **`textureID`**: Índice da textura em caso de canal de multitextura; 0 = primeiro canal por padrão. Em textura UV, este parâmetro deve ser sempre 0 (opcional).
  - tipo: int
- **`textureObj`**: Referência a outro objeto `Texture` com bindId compartilhado, se você quiser reaproveitar a textura. Se usar este argumento, não crie nenhuma fonte nesta textura nem precisa atualizá-la: o outro objeto `Texture` fornece a textura para os dois materiais/texturas (opcional).
  - tipo: `Texture`

### bindId

Nome de bind OpenGL (somente leitura).

**Tipo:** int

### close()

Fecha a textura dinâmica e restaura a original.

### mipmap

Textura com mipmap.

**Tipo:** bool

### refresh(refresh_source, timestamp=-1.0)

Atualiza a textura a partir da fonte.

- **`refresh_source`**: Se também deve atualizar a fonte de imagem da textura.
  - tipo: bool
- **`timestamp`**: Se a textura controla um objeto VideoFFmpeg: timestamp (em segundos desde o início do filme) do frame a carregar; serve para sincronizar vídeo e som passando `time` a ele (opcional).
  - tipo: float

### source

Fonte da textura.

**Tipo:** one of... * `VideoFFmpeg` * `VideoDeckLink` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

Alguns dispositivos DeckLink podem ser usados para reproduzir vídeo: o host envia frames regularmente para reprodução imediata ou agendada. O vídeo sai pelas interfaces HDMI ou SDI. Esta classe suporta o modo de reprodução imediata: ela tem um atributo source que recebe um dos objetos de fonte do módulo Range.texture. Atualizar o objeto DeckLink faz a fonte de imagem ser calculada e enviada ao dispositivo DeckLink para transmissão imediata nas interfaces de saída. Keying é suportado: permite compor o frame com um vídeo de entrada que passa pela placa DeckLink.

- **`cardIdx`**: Número da placa usada na saída (0 = primeira placa). Repare que os dispositivos DeckLink costumam ser half duplex: servem para captura ou para reprodução, mas não as duas ao mesmo tempo.
  - tipo: int
- **`format`**: String que representa o modo de exibição do vídeo de saída.
  - tipo: str
O valor padrão do argumento format é reservado para detecção automática, mas isso ainda não é suportado (gera erro em tempo de execução), então o formato de vídeo precisa ser passado explicitamente. Se o objetivo for keying (veja os atributos de keying), o formato precisa corresponder exatamente ao vídeo de entrada; senão, pode ser qualquer formato suportado pelo dispositivo (dá erro em tempo de execução se não for). O formato da string é `<displayMode>[/3D]`.

Veja `VideoDeckLink` para a lista de `<displayMode>` aceitos. O sufixo opcional `/3D` cria um vídeo 3D estéreo. Nesse caso, o atributo 'right' também precisa ser definido com a fonte de imagem do olho direito.

Nota: o formato de pixel não é passado aqui porque é sempre BGRA. O canal alpha é usado no keying para misturar a fonte com o vídeo de entrada; fora isso, não é usado. Se for preciso converter para o formato de vídeo nativo, isso é feito dentro do driver ou do dispositivo DeckLink.

### source

Este atributo precisa receber uma das fontes de imagem. Se o tamanho da imagem não bater exatamente com o do frame, o atributo extend decide o que fazer.

Para o melhor desempenho, a imagem de origem deve ter exatamente o tamanho do frame de saída. Fica ainda mais rápido se a fonte de imagem for ImageViewport ou ImageRender com viewport inteira, flip desligado e sem filtro: o frame buffer GL é copiado direto para o buffer da imagem e dali direto para a placa DeckLink (sem cópias de buffer para buffer dentro do VideoTexture).

**Tipo:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

### right

Se o formato de vídeo for 3D estéreo, este atributo deve receber uma fonte de imagem que produz as imagens do olho direito. Para renderizar a cena da BGE em 3D, dá para usar 2 câmeras, uma para cada olho, com 2 ImageRender e um buffer de render fora da tela do tamanho do frame de vídeo.

**Tipo:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

### keying

Diz se o keying está ligado. False (padrão): o frame de saída vai sem mudança para a interface de saída (nesse caso não é preciso vídeo de entrada). True: o frame de saída é misturado com o vídeo de entrada, usando o canal alpha para combinar as duas imagens, e o resultado vai para a interface de saída.

**Tipo:** bool

### level

Com keying ligado, define o nível de keying de 0 a 255. Este valor é um alpha global que multiplica o canal alpha da fonte de imagem. Use 255 (o padrão) para manter o canal alpha como está, ou 0 para deixar o frame de saída totalmente transparente.

**Tipo:** int

### extend

Define como a fonte de imagem é mapeada se o tamanho não bater com o do frame de vídeo.
* False (o padrão): mapeia a imagem pixel a pixel.
Se a imagem for menor que o frame, o espaço em volta é preenchido com preto de alpha 0. Se for maior, a imagem é cortada para caber no frame.
* True: a imagem é escalada pelo algoritmo do vizinho mais próximo para caber no frame.
A escala é rápida, mas de baixa qualidade. Para o melhor resultado, ajuste sempre a fonte de imagem ao tamanho do vídeo de saída.

**Tipo:** bool

### close()

Fecha o dispositivo DeckLink e libera todos os recursos. Depois deste método, o objeto não pode ser reativado; é preciso destruí-lo e criar um novo objeto DeckLink para reiniciar a saída.

### refresh(refresh_source,ts)

Este método precisa ser chamado com frequência para atualizar o frame de saída no dispositivo DeckLink.

- **`refresh_source`**: True se o buffer de imagem das fontes deve ser invalidado depois de usado para calcular o frame de saída. Isso faz a imagem de origem ser recalculada no próximo refresh, que normalmente é o desejado. False se o buffer da fonte deve continuar válido e ser reaproveitado no próximo refresh. Repare que o dispositivo DeckLink guarda o frame de saída e repete até o host mandar um novo. Então não é preciso atualizar o objeto DeckLink se você sabe que a fonte de imagem não mudou.
  - tipo: bool
- **`ts`**: O timestamp passado ao objeto de fonte de imagem para calcular a imagem. Se não for passado, é usado o relógio da BGE.
  - tipo: float

## Classes de filtro

Filtro de origem BGR24.

Filtro de blue screen. Os canais RGB da cor ficam iguais, e o alpha de saída é obtido assim:

- se o quadrado da distância euclidiana entre a cor RGB
e a cor de referência do filtro for menor que o limite inferior do filtro, o alpha de saída vira 0;
- se esse quadrado for maior que o limite superior do filtro, o alpha de saída vira 255;
- senão, o alpha de saída é interpolado linearmente entre 0 e 255 no intervalo dos limites.

### color

Cor de referência.

**Tipo:** sequence of three ints

**padrão:** (0, 0, 255)

### limits

Limites da cor de referência.

**Tipo:** sequence of two ints

**padrão:** (64, 64)

### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filtro de cálculo de cor. A cor de saída é obtida multiplicando a matriz 4x4 reduzida pela cor de entrada e somando a coluna restante ao resultado.

### matrix

Matriz [4][5] para o cálculo de cor.

**Tipo:** sequence of four sequences of five ints

**padrão:** ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))

### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filtro de tons de cinza. As proporções de R, G e B no cinza de saída são 28:151:77.

### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filtro de cálculo de níveis. Cada componente de cor de saída é obtido assim:

* se for menor que o valor mínimo correspondente, vira 0;

* se for maior que o valor máximo correspondente, vira 255;

* senão, é interpolado linearmente entre 0 e 255 no intervalo (min, max).

### levels

Matriz de níveis [4] (min, max).

**Tipo:** sequence of four sequences of two ints

**padrão:** ((0, 255), (0, 255), (0, 255), (0, 255))

### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filtro de normal map.

### colorIdx

Índice da cor usada para calcular a normal (0 - vermelho, 1 - verde, 2 - azul, 3 - alpha).

**Tipo:** int in [0, 3]

**padrão:** 0

### depth

Profundidade do relevo.

**Tipo:** float

**padrão:** 4.0

### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Devolve um novo objeto de filtro de entrada para usar com `ImageBuff` quando a imagem passada à função `ImageBuff.load` tem o formato de pixel BGR de 3 bytes.

Filtro de origem RGBA32.

## Funções

### getLastError()

Último erro que aconteceu numa função de Range.texture.

**Retorna:** A descrição do último erro que aconteceu numa função de Range.texture.

**Tipo do retorno:** str

### imageToArray(image, mode)

Devolve um `Buffer` com a imagem atual guardada num objeto de fonte de textura.

- **`image`**: Objeto de fonte de imagem do tipo: * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`
- **`mode`**: Argumento opcional com o formato de pixel. - Use os caracteres R, G e B para os 3 canais de cor, A para o canal alpha, 0 para forçar um canal fixo em 0 e 1 para forçar um canal fixo em 255. Exemplos: - "BGR" devolve 3 bytes por pixel com os canais azul, verde e vermelho nessa ordem. - "RGB1" devolve 4 bytes por pixel com os canais vermelho, verde e azul nessa ordem e o alpha forçado em 255. - O modo especial "F" devolve a imagem como array de float. Ele só deve ser usado para pegar o buffer de profundidade dos objetos `ImageViewport` e `ImageRender`. O modo padrão é "RGBA".
  - tipo: str

**Retorna:** Um objeto que representa a imagem como array de bytes de uma dimensão, de tamanho (pixel_size*width*height), linha por linha a partir de baixo da imagem. O tamanho e o formato do pixel vêm do parâmetro mode. No modo 'F', o array é de float, de uma dimensão, de tamanho (width*height).

**Tipo do retorno:** `Buffer`

### materialID(object, name)

Devolve um valor numérico que pode ser usado em `Texture` para criar uma textura dinâmica.

O valor corresponde a um número interno de material que usa a textura identificada por name. name é uma string com o nome da textura com prefixo `IM`, se você quiser identificar a textura diretamente. Isto funciona para tex face básica e para material, desde que o material tenha um canal de textura usando essa textura na primeira posição da pilha de texturas. name também pode ter o prefixo `MA`, para identificar a textura pelo material. Nesse caso, o material precisa ter um canal de textura na primeira posição.

Se o objeto não tiver um material que corresponda a name, é gerado um erro em tempo de execução. Use try/except para pegar a exceção.

Ex.: `Range.texture.materialID(obj, 'IMvideo.png')`

- **`object`**: O game object que usa a textura que você quer tornar dinâmica.
  - tipo: `KX_GameObject`
- **`name`**: Nome da textura/material que você quer tornar dinâmico.
  - tipo: str

**Retorna:** O número interno do material.

**Tipo do retorno:** int

### setLogFile(filename)

Define o nome de um arquivo de texto onde as mensagens de erro em tempo de execução serão gravadas, além de aparecerem no console Python. Só os erros específicos do módulo VideoTexture são gravados nesse arquivo; erros comuns não são.

- **`filename`**: Nome do arquivo de log de erros.
  - tipo: str

**Retorna:** -1 se o parâmetro name for inválido (não for string); senão, 0.

**Tipo do retorno:** int

## Constantes

## Status de vídeo e imagem do FFmpeg

### SOURCE_ERROR

### SOURCE_EMPTY

### SOURCE_READY

### SOURCE_PLAYING

### SOURCE_STOPPED

## Modos de mistura de imagem

Veja [Blend Modes](https://en.wikipedia.org/wiki/Blend_modes) na Wikipédia para referência.

### IMB_BLEND_MIX

### IMB_BLEND_ADD

### IMB_BLEND_SUB

### IMB_BLEND_MUL

### IMB_BLEND_LIGHTEN

### IMB_BLEND_DARKEN

### IMB_BLEND_ERASE_ALPHA

### IMB_BLEND_ADD_ALPHA

### IMB_BLEND_OVERLAY

### IMB_BLEND_HARDLIGHT

### IMB_BLEND_COLORBURN

### IMB_BLEND_LINEARBURN

### IMB_BLEND_COLORDODGE

### IMB_BLEND_SCREEN

### IMB_BLEND_SOFTLIGHT

### IMB_BLEND_PINLIGHT

### IMB_BLEND_VIVIDLIGHT

### IMB_BLEND_LINEARLIGHT

### IMB_BLEND_DIFFERENCE

### IMB_BLEND_EXCLUSION

### IMB_BLEND_HUE

### IMB_BLEND_SATURATION

### IMB_BLEND_LUMINOSITY

### IMB_BLEND_COLOR

### IMB_BLEND_COPY

### IMB_BLEND_COPY_RGB

### IMB_BLEND_COPY_ALPHA

