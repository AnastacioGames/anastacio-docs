# Range.texture

> **Veja também:**
[`Texture`](Texture.md), [`KX_BlenderMaterial`](KX_BlenderMaterial.md), [`BL_Texture`](BL_Texture.md)

```python
# Mostra um vídeo no material do objeto.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

if "video" not in own:
    matID = texture.materialID(own, "MAscreen")
    tex = texture.Texture(own, matID)
    tex.source = texture.VideoFFmpeg(Range.logic.expandPath("//movie.mp4"))
    tex.source.play()
    own["video"] = tex

own["video"].refresh(True)
```

```python
# Troca a imagem de um material com o jogo rodando.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.refresh(False)
own["poster"] = tex
```

```python
# Faz uma imagem de espelho com outra câmera.
import Range
from Range import texture

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageRender(scene, scene.objects["SecurityCamera"])
own["monitor"] = tex
own["monitor"].refresh(True)
```

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

## Classe `VideoFFmpeg(file, capture=-1, rate=25.0, width=0, height=0)`

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

## Classe `ImageFFmpeg(file)`

Fonte de imagem FFmpeg, usada para arquivos de imagem e imagens da web.

- **`file`**: Caminho da imagem a carregar.
  - tipo: str

## Classe `ImageBuff(width, height, color=0, scale=False)`

Imagem vinda da memória da aplicação. Para imagens geradas pelo computador, aplicativos de desenho.

- **`width`**: Largura da imagem.
  - tipo: int
- **`height`**: Altura da imagem.
  - tipo: int
- **`color`**: Valor para iniciar os canais RGB. O buffer iniciado terá todos os pixels em (color, color, color, 255) (opcional).
  - tipo: int in [0, 255]
- **`scale`**: A imagem usa escala (opcional).
  - tipo: bool

## Classe `ImageMirror(scene, observer, mirror, material=0, width, height, samples, hdr)`

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

## Classe `ImageMix`

Mixer de imagens, usado para misturar várias fontes de imagem.

## Classe `ImageRender(scene, camera, width, height, samples, hdr)`

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

## Classe `ImageViewport`

Fonte de imagem a partir da viewport renderizada pela câmera ativa. Para renderizar de uma câmera não ativa, veja `ImageRender`.

## Classe `VideoDeckLink(format, capture=0)`

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

## Classe `Texture(gameObj, materialID=0, textureID=0, textureObj=None)`

Classe que cria o objeto `Texture`, que carrega a textura dinâmica na GPU.

- **`gameObj`**: Game object em que a textura de vídeo será criada.
  - tipo: `KX_GameObject`
- **`materialID`**: ID do material; o padrão 0 é o primeiro material (opcional).
  - tipo: int
- **`textureID`**: Índice da textura em caso de canal de multitextura; 0 = primeiro canal por padrão. Em textura UV, este parâmetro deve ser sempre 0 (opcional).
  - tipo: int
- **`textureObj`**: Referência a outro objeto `Texture` com bindId compartilhado, se você quiser reaproveitar a textura. Se usar este argumento, não crie nenhuma fonte nesta textura nem precisa atualizá-la: o outro objeto `Texture` fornece a textura para os dois materiais/texturas (opcional).
  - tipo: `Texture`

## Classe `DeckLink(cardIdx=0, format="")`

Alguns dispositivos DeckLink podem ser usados para reproduzir vídeo: o host envia frames regularmente para reprodução imediata ou agendada. O vídeo sai pelas interfaces HDMI ou SDI. Esta classe suporta o modo de reprodução imediata: ela tem um atributo source que recebe um dos objetos de fonte do módulo Range.texture. Atualizar o objeto DeckLink faz a fonte de imagem ser calculada e enviada ao dispositivo DeckLink para transmissão imediata nas interfaces de saída. Keying é suportado: permite compor o frame com um vídeo de entrada que passa pela placa DeckLink.

- **`cardIdx`**: Número da placa usada na saída (0 = primeira placa). Repare que os dispositivos DeckLink costumam ser half duplex: servem para captura ou para reprodução, mas não as duas ao mesmo tempo.
  - tipo: int
- **`format`**: String que representa o modo de exibição do vídeo de saída.
  - tipo: str
O valor padrão do argumento format é reservado para detecção automática, mas isso ainda não é suportado (gera erro em tempo de execução), então o formato de vídeo precisa ser passado explicitamente. Se o objetivo for keying (veja os atributos de keying), o formato precisa corresponder exatamente ao vídeo de entrada; senão, pode ser qualquer formato suportado pelo dispositivo (dá erro em tempo de execução se não for). O formato da string é `<displayMode>[/3D]`.

Veja `VideoDeckLink` para a lista de `<displayMode>` aceitos. O sufixo opcional `/3D` cria um vídeo 3D estéreo. Nesse caso, o atributo 'right' também precisa ser definido com a fonte de imagem do olho direito.

Nota: o formato de pixel não é passado aqui porque é sempre BGRA. O canal alpha é usado no keying para misturar a fonte com o vídeo de entrada; fora isso, não é usado. Se for preciso converter para o formato de vídeo nativo, isso é feito dentro do driver ou do dispositivo DeckLink.

## Classe `FilterBGR24`

Filtro de origem BGR24.

## Classe `FilterBlueScreen`

Filtro de blue screen. Os canais RGB da cor ficam iguais, e o alpha de saída é obtido assim:

- se o quadrado da distância euclidiana entre a cor RGB
e a cor de referência do filtro for menor que o limite inferior do filtro, o alpha de saída vira 0;
- se esse quadrado for maior que o limite superior do filtro, o alpha de saída vira 255;
- senão, o alpha de saída é interpolado linearmente entre 0 e 255 no intervalo dos limites.

## Classe `FilterColor`

Filtro de cálculo de cor. A cor de saída é obtida multiplicando a matriz 4x4 reduzida pela cor de entrada e somando a coluna restante ao resultado.

## Classe `FilterGray`

Filtro de tons de cinza. As proporções de R, G e B no cinza de saída são 28:151:77.

## Classe `FilterLevel`

Filtro de cálculo de níveis. Cada componente de cor de saída é obtido assim:

* se for menor que o valor mínimo correspondente, vira 0;

* se for maior que o valor máximo correspondente, vira 255;

* senão, é interpolado linearmente entre 0 e 255 no intervalo (min, max).

## Classe `FilterNormal`

Filtro de normal map.

## Classe `FilterRGB24`

Devolve um novo objeto de filtro de entrada para usar com `ImageBuff` quando a imagem passada à função `ImageBuff.load` tem o formato de pixel BGR de 3 bytes.

## Classe `FilterRGBA32`

Filtro de origem RGBA32.

## Modos de mistura de imagem

Veja [Blend Modes](https://en.wikipedia.org/wiki/Blend_modes) na Wikipédia para referência.

Visão geral. Os itens estão nas partes abaixo:

- [atributos](Range.texture--props.md) (101 itens)
- [métodos e funções](Range.texture--funcs.md) (29 itens)
- [constantes](Range.texture--consts.md) (32 itens)
