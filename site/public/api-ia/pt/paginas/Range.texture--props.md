# Range.texture - atributos

Parte de [Range.texture](Range.texture.md).

## status

Status do vídeo (somente leitura).

**Tipo:** int

**Valor:** `see `FFmpeg Video and Image Status`_.`

## range

O tempo de início e fim da reprodução, em segundos desde o começo. Por padrão, o vídeo inteiro.

**Tipo:** sequence of two floats

## repeat

Número de vezes que o vídeo repete; -1 para repetir sem parar.

**Tipo:** int

## framerate

Frame rate relativo: <1.0 para lento, >1.0 para rápido.

**Tipo:** float

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## scale

Use True para ligar o algoritmo rápido de escala por vizinho mais próximo. A largura e a altura da textura precisam ser potência de 2. Se o tamanho da imagem do vídeo não for potência de 2, é preciso reescalar. Por padrão, `Range.texture` usa a função `gluScaleImage()`, precisa mas lenta. O melhor é reescalar o vídeo antes, para não precisar escalar em tempo de execução!

**Tipo:** bool

## flip

Com True, a imagem é espelhada na vertical. O FFmpeg sempre entrega a imagem de cabeça para baixo, por isso este atributo vem True por padrão.

**Tipo:** bool

## filter

Um filtro adicional aplicado no vídeo antes de enviá-lo à GPU.

**Tipo:** one of: * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## preseek

Número de frames de pré-busca.

**Tipo:** int

## deinterlace

Desentrelaça a imagem.

**Tipo:** bool

## status

Status da imagem (somente leitura).

**Tipo:** int

**Valor:** `see `FFmpeg Video and Image Status`_.`

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

## flip

Espelha a imagem na vertical.

**Tipo:** bool

## filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Espelha a imagem na vertical.

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## alpha

Usa alpha na textura.

**Tipo:** bool

## horizon

Cor do horizonte.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

## zenith

Cor do zênite.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

## background

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

Obsoleto; use `Range.texture.ImageMirror.horizon` ou `Range.texture.ImageMirror.zenith`.

## updateShadow

Força a atualização do buffer de sombras se houver diferença entre a imagem renderizada e as sombras.

**Tipo:** bool

## colorBindCode

Bind code da textura de cor fora da tela.

**Tipo:** integer

## capsize

Tamanho da área de render.

**Tipo:** sequence of two ints

## clip

Distância de recorte.

**Tipo:** float in [0.01, 5000.0]

## filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Espelha a imagem na vertical.

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## whole

Usa a viewport inteira no render.

**Tipo:** bool

## filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Espelha a imagem na vertical.

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## alpha

Usa alpha na textura.

**Tipo:** bool

## horizon

Cor do horizonte.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

## zenith

Cor do zênite.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

## background

Cor de fundo.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

Obsoleto; use `Range.texture.ImageRender.horizon` ou `Range.texture.ImageRender.zenith`.

## updateShadow

Força a atualização do buffer de sombras se houver diferença entre a imagem renderizada e as sombras.

**Tipo:** bool

## colorBindCode

Bind code da textura de cor fora da tela.

**Tipo:** integer

## capsize

Tamanho da área de render.

**Tipo:** sequence of two ints

## filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Espelha a imagem na vertical.

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## whole

Usa a viewport inteira no render.

**Tipo:** bool

## depth

Usa o componente de profundidade do render como array de float; não serve como fonte de textura, só deve ser usado com Range.texture.imageToArray(mode='F').

**Tipo:** bool

## zbuff

Usa o componente de profundidade do render como cor em tons de cinza; serve como fonte de textura.

**Tipo:** bool

## alpha

Usa alpha na textura.

**Tipo:** bool

## capsize

Tamanho da área da viewport capturada.

**Tipo:** sequence of two ints

## filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Espelha a imagem na vertical.

**Tipo:** bool

## image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

## position

Canto superior esquerdo da área capturada.

**Tipo:** sequence of two ints

## scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

## size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

## valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

## whole

Usa a viewport inteira na captura.

**Tipo:** bool

## depth

Usa o componente de profundidade da viewport como array de float; não serve como fonte de textura, só deve ser usado com `Range.texture.imageToArray(mode='F')`.

**Tipo:** bool

## zbuff

Usa o componente de profundidade da viewport como cor em tons de cinza; serve como fonte de textura.

**Tipo:** bool

## status

Status da captura: 1=pronta para uso, 2=capturando, 3=parada

**Tipo:** int

## framerate

Frame rate da captura, calculado a partir do formato de vídeo.

**Tipo:** float

## valid

Diz se o atributo image pode ser usado para pegar a imagem. Sempre False nesta implementação (a imagem não fica disponível no Python)

**Tipo:** bool

## image

Os dados da imagem. Sempre None nesta implementação.

**Tipo:** `Buffer` or None

## size

O tamanho do frame em pixels. Frames estéreo têm o dobro da altura do frame de vídeo, ou seja, o 3D chega à GPU como uma única imagem em ordem de cima para baixo, com o olho esquerdo em cima.

**Tipo:** (int,int)

## scale

Não usado neste objeto.

**Tipo:** bool

## flip

Não usado neste objeto.

**Tipo:** bool

## filter

Não usado neste objeto.

## bindId

Nome de bind OpenGL (somente leitura).

**Tipo:** int

## mipmap

Textura com mipmap.

**Tipo:** bool

## source

Fonte da textura.

**Tipo:** one of... * `VideoFFmpeg` * `VideoDeckLink` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

## source

Este atributo precisa receber uma das fontes de imagem. Se o tamanho da imagem não bater exatamente com o do frame, o atributo extend decide o que fazer.

Para o melhor desempenho, a imagem de origem deve ter exatamente o tamanho do frame de saída. Fica ainda mais rápido se a fonte de imagem for ImageViewport ou ImageRender com viewport inteira, flip desligado e sem filtro: o frame buffer GL é copiado direto para o buffer da imagem e dali direto para a placa DeckLink (sem cópias de buffer para buffer dentro do VideoTexture).

**Tipo:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

## right

Se o formato de vídeo for 3D estéreo, este atributo deve receber uma fonte de imagem que produz as imagens do olho direito. Para renderizar a cena da BGE em 3D, dá para usar 2 câmeras, uma para cada olho, com 2 ImageRender e um buffer de render fora da tela do tamanho do frame de vídeo.

**Tipo:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

## keying

Diz se o keying está ligado. False (padrão): o frame de saída vai sem mudança para a interface de saída (nesse caso não é preciso vídeo de entrada). True: o frame de saída é misturado com o vídeo de entrada, usando o canal alpha para combinar as duas imagens, e o resultado vai para a interface de saída.

**Tipo:** bool

## level

Com keying ligado, define o nível de keying de 0 a 255. Este valor é um alpha global que multiplica o canal alpha da fonte de imagem. Use 255 (o padrão) para manter o canal alpha como está, ou 0 para deixar o frame de saída totalmente transparente.

**Tipo:** int

## extend

Define como a fonte de imagem é mapeada se o tamanho não bater com o do frame de vídeo.
* False (o padrão): mapeia a imagem pixel a pixel.
Se a imagem for menor que o frame, o espaço em volta é preenchido com preto de alpha 0. Se for maior, a imagem é cortada para caber no frame.
* True: a imagem é escalada pelo algoritmo do vizinho mais próximo para caber no frame.
A escala é rápida, mas de baixa qualidade. Para o melhor resultado, ajuste sempre a fonte de imagem ao tamanho do vídeo de saída.

**Tipo:** bool

## color

Cor de referência.

**Tipo:** sequence of three ints

**padrão:** (0, 0, 255)

## limits

Limites da cor de referência.

**Tipo:** sequence of two ints

**padrão:** (64, 64)

## previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## matrix

Matriz [4][5] para o cálculo de cor.

**Tipo:** sequence of four sequences of five ints

**padrão:** ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))

## previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## levels

Matriz de níveis [4] (min, max).

**Tipo:** sequence of four sequences of two ints

**padrão:** ((0, 255), (0, 255), (0, 255), (0, 255))

## previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## colorIdx

Índice da cor usada para calcular a normal (0 - vermelho, 1 - verde, 2 - azul, 3 - alpha).

**Tipo:** int in [0, 3]

**padrão:** 0

## depth

Profundidade do relevo.

**Tipo:** float

**padrão:** 4.0

## previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`
