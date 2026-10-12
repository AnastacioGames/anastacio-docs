---
title: "Range.render"
description: "Referência do módulo Range.render"
---

## Introdução

Exemplo usando um `Range.types.SCA_MouseSensor` e dois `Range.types.KX_ObjectActuator` para fazer o mouse look:

:::note
Também dá para fazer isso com o `Range.types.KX_MouseActuator`.
:::

```python

# Para usar um sensor de movimento do mouse "Mouse" e um
# atuador de movimento para olhar com o mouse:
import Range

# scale define a velocidade do movimento
scale = 1.0, 0.5

co = Range.logic.getCurrentController()
obj = co.owner
mouse = co.sensors["Mouse"]
lmotion = co.actuators["LMove"]
wmotion = co.actuators["WMove"]

# Converte as coordenadas do mouse para ver quanto o mouse andou.
def mousePos():
   x = (Range.render.getWindowWidth() / 2 - mouse.position[0]) * scale[0]
   y = (Range.render.getWindowHeight() / 2 - mouse.position[1]) * scale[1]
   return (x, y)

pos = mousePos()

# Define o quanto mover: X é aplicado em coordenadas do mundo...
wmotion.useLocalTorque = False
wmotion.torque = ((0.0, 0.0, pos[0]))

# ...Y é aplicado em coordenadas locais
lmotion.useLocalTorque = True
lmotion.torque = ((-pos[1], 0.0, 0.0))

# Ativa os dois atuadores
co.activate(lmotion)
co.activate(wmotion)

# Centraliza o mouse
Range.render.setMousePosition(int(Range.render.getWindowWidth() / 2), int(Range.render.getWindowHeight() / 2))
```

## Constantes

### KX_TEXFACE_MATERIAL

Obsoleto.

Materiais definidos pelas configurações de texture face.

### KX_BLENDER_MULTITEX_MATERIAL

Obsoleto.

Materiais que imitam os materiais do Blender com multitextura.

### KX_BLENDER_GLSL_MATERIAL

Obsoleto.

Materiais que imitam os materiais do Blender com GLSL.

Desliga o vsync; liga o vsync; liga o vsync adaptativo, se suportado. O vsync adaptativo liga o vsync quando o frame rate está acima da taxa de atualização do monitor e desliga quando o frame rate fica baixo demais.

### LEFT_EYE

Olho esquerdo em uso no render estereoscópico.

### RIGHT_EYE

Olho direito em uso no render estereoscópico.

## HDR

### HDR_NONE

Usa formato de imagem com 8 bits por canal.

### HDR_HALF_FLOAT

Usa formato de imagem com float de 16 bits por canal.

### HDR_FULL_FLOAT

Usa formato de imagem com float de 32 bits por canal.

## Funções

### getWindowWidth()

Pega a largura da janela (em pixels)

**Tipo do retorno:** integer

### getWindowHeight()

Pega a altura da janela (em pixels)

**Tipo do retorno:** integer

### setWindowSize(width, height)

Define a largura e a altura da janela (em pixels). Também funciona em tela cheia.

:::note
Só funciona no player separado, não no player embutido no Blender.
:::

- **`width`**: Largura em pixels
  - tipo: integer
- **`height`**: Altura em pixels
  - tipo: integer

### setFullScreen(enable)

Define se a janela fica em tela cheia ou não.

:::note
Só funciona no player separado, não no player embutido no Blender.
:::

- **`enable`**: `True` para tela cheia, `False` para janela.
  - tipo: bool

### getFullScreen()

Diz se a janela está em tela cheia.

:::note
Só funciona no player separado, não no player embutido no Blender; lá sempre devolve False.
:::

**Tipo do retorno:** bool

### getDisplayDimensions()

Pega as dimensões da tela (por exemplo, do monitor) em pixels. Pode devolver o tamanho da área inteira, somando todos os monitores; por exemplo, `(3840, 1080)` para dois monitores 1080p lado a lado.

**Tipo do retorno:** tuple (width, height)

### makeScreenshot(filename)

Grava um arquivo de imagem com o que está na tela no fim do frame.

A imagem é gravada em *'filename'*. O caminho pode ser absoluto (ex.: `/home/foo/image`) ou relativo, começando com `//` (ex.: `//image`). Caminhos absolutos não funcionam igual em todos os sistemas. Se o nome tiver um `#`, ele é trocado por um número que aumenta a cada vez, para tirar vários prints sem sobrescrever os anteriores (ex.: `image-#`).

As configurações da imagem vêm das configurações de render (formato do arquivo e seus ajustes, gamma, conversão de espaço de cor etc.). A resolução da imagem é a do framebuffer, ou seja, o tamanho e a proporção da janela. No player separado, em vez do embutido, só arquivos PNG são suportados, e as conversões de cor extras também não.

- **`filename`**: Caminho e nome do arquivo a gravar
  - tipo: string

### enableVisibility(visible)

Obsoleto; não faz nada.

### showMouse(visible)

Mostra ou esconde o cursor do mouse do sistema.

- **`visible`**:
  - tipo: boolean

### setMousePosition(x, y)

Define a posição do cursor do mouse.

- **`x`**: Coordenada X, em pixels da tela.
  - tipo: integer
- **`y`**: Coordenada Y, em pixels da tela.
  - tipo: integer

### setBackgroundColor(rgba)

Obsoleto e não funciona mais. Use `Range.types.KX_WorldInfo.horizonColor` ou `Range.types.KX_WorldInfo.zenithColor`.

### setEyeSeparation(eyesep)

Define a separação dos olhos no modo estéreo. Em geral, distância focal/30 dá um valor confortável.

- **`eyesep`**: A distância entre o olho esquerdo e o direito.
  - tipo: float

### getEyeSeparation()

Pega a separação dos olhos atual do modo estéreo.

**Tipo do retorno:** float

### setFocalLength(focallength)

Define a distância focal do modo estéreo. O valor inicial é a distância focal da câmera atual.

- **`focallength`**: A distância focal.
  - tipo: float

### getFocalLength()

Pega a distância focal atual do modo estéreo.

**Tipo do retorno:** float

### getStereoEye()

Pega qual olho estereoscópico está sendo renderizado agora. Serve principalmente num callback `Range.types.KX_Scene.pre_draw`, para ajustar as matrizes de projeção da câmera para cada olho.

**Tipo do retorno:** LEFT_EYE, RIGHT_EYE

### setMaterialMode(mode)

Obsoleto e não funciona mais.

Define o modo de material usado no render OpenGL.

- **`mode`**: Modo de material
  - tipo: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

:::note
As mudanças só valem para cenas criadas depois.
:::

### getMaterialMode(mode)

Obsoleto e não funciona mais.

Pega o modo de material usado no render OpenGL.

**Tipo do retorno:** KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

### setGLSLMaterialSetting(setting, enable)

Liga ou desliga uma configuração de material GLSL.

- **`setting`**:
  - tipo: string (lights, shaders, shadows, ramps, nodes, extra_textures)
- **`enable`**:
  - tipo: boolean

### getGLSLMaterialSetting(setting)

Pega o estado de uma configuração de material GLSL.

- **`setting`**:
  - tipo: string (lights, shaders, shadows, ramps, nodes, extra_textures)

**Tipo do retorno:** boolean

### setAnisotropicFiltering(level)

Define o nível de filtragem anisotrópica das texturas.

- **`level`**: O novo nível de filtragem anisotrópica
  - tipo: integer (must be one of 1, 2, 4, 8, 16)

:::note
Limitado ao máximo suportado pela placa de vídeo. O jogo exportado começa com 8.
:::

### getAnisotropicFiltering()

Pega o nível de filtragem anisotrópica das texturas.

**Tipo do retorno:** integer (one of 1, 2, 4, 8, 16)

### setAntiAliasing(level)

Define o nível de anti-aliasing.

- **`level`**: O novo nível de anti-aliasing
  - tipo: integer (must be one of 0, 2, 4, 8, 16)

:::note
Mudar este valor recria todos os buffers fora da tela, o que pode ser lento.
:::

### getAntiAliasing()

Pega o nível de anti-aliasing configurado.

**Tipo do retorno:** integer (one of 0, 2, 4, 8, 16)

### setMipmapping(value)

Muda como o mipmapping é usado.

  - tipo: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

:::note
Alternar entre NEAREST e LINEAR, ou desligá-los, muda apenas os filtros. Com os mipmaps desligados, as texturas são exibidas sem filtragem (nearest), útil para pixel art.
:::

### getMipmapping()

Pega a configuração atual de mipmapping.

**Tipo do retorno:** RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

### setTextureQuality(level)

Qualidade de textura para um menu gráfico: mantenha apenas a textura de alta resolução no projeto e descarte seus maiores níveis de mipmap ao enviá-la para a placa de vídeo.

* `0`: tamanho completo
* `1`: metade do tamanho (1/4 da memória de vídeo)
* `2`: um quarto do tamanho (1/16 da memória de vídeo)

As texturas nunca ficam menores que 256 pixels em seu maior lado, e texturas sem mipmaps (ou com mipmapping desligado) mantêm seu tamanho. Arquivos DDS pulam os níveis armazenados no arquivo.

- **`level`**: 0, 1 or 2
  - tipo: integer

:::note
Configure no menu, não a cada frame. No editor, o valor é restaurado quando o jogo termina.
:::

### getTextureQuality()

**Retorna:** a qualidade de textura atual (0 completa, 1 metade, 2 um quarto).

**Tipo do retorno:** integer

### drawLine(fromVec,toVec,color)

Desenha uma linha na cena 3D.

- **`fromVec`**: O começo da linha
  - tipo: list [x, y, z]
- **`toVec`**: O fim da linha
  - tipo: list [x, y, z]
- **`color`**: A cor da linha
  - tipo: list [r, g, b, a]

### enableMotionBlur(factor)

Liga o efeito de motion blur.

- **`factor`**: A intensidade do motion blur.
  - tipo: float [0.0 - 1.0]

### disableMotionBlur()

Desliga o efeito de motion blur.

### showFramerate(enable)

Mostra ou esconde o frame rate.

- **`enable`**:
  - tipo: boolean

### showProfile(enable)

Mostra ou esconde o profiler.

- **`enable`**:
  - tipo: boolean

### showProperties(enable)

Mostra ou esconde as propriedades de depuração.

- **`enable`**:
  - tipo: boolean

### autoDebugList(enable)

Liga ou desliga a inclusão automática das propriedades de depuração na lista.

- **`enable`**:
  - tipo: boolean

### clearDebugList()

Limpa a lista de propriedades de depuração.

### setVsync(value)

Define o vsync

- **`value`**: Um destes: VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
  - tipo: integer

### getVsync()

Pega o valor atual do vsync

**Tipo do retorno:** One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE

### setDynamicResolution(enabled, targetFPS=60, minScale=50, maxScale=100, step=5)

Versão em tempo de jogo das configurações de Dynamic Resolution da cena. A cena 3D é renderizada numa escala do tamanho da janela e esticada para a tela; a janela em si não muda. Com a resolução dinâmica, a escala desce `step` quando o tempo de GPU do frame passa do alvo e sobe de novo quando sobra tempo. `minScale == maxScale` dá uma escala de render fixa. Fica pausada enquanto "Show Render Queries" estiver ligado (os dois usam uma consulta de tempo da GPU).

- **`enabled`**: False renderiza a 100%.
  - tipo: boolean
- **`targetFPS`**: O frame rate com que o tempo de GPU é comparado.
  - tipo: integer
- **`minScale`**: Escala mínima, em porcentagem (25-100).
  - tipo: integer
- **`maxScale`**: Escala máxima, em porcentagem (25-100).
  - tipo: integer
- **`step`**: Quanto a escala muda a cada ajuste, em porcentagem (1-25).
  - tipo: integer

### getRenderScale()

A escala de render atual; 1.0 = resolução completa.

**Tipo do retorno:** float

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getMasterVolume()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `volume`

### getStereoMode()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

pega o modo estéreo

### getVRChromaticAberration()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

pega a correção de aberração cromática da lente VR

### getVRLensStrength()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

pega a intensidade da distorção da lente VR

### setCustomMouse(string path)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setMasterVolume(volume)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- volume em [0, 1], aplicado ao dispositivo de áudio real da engine

### setStereoMode()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

define o modo estéreo (constantes STEREO_*)

### setVRChromaticAberration()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

define a correção de aberração cromática da lente VR (0..0.1, padrão 0.01)

### setVRLensStrength()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

define a intensidade da distorção da lente VR (0..1, padrão 0.3)

### showDebugPhysics(bool debug)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### RAS_MIPMAP_LINEAR

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_MIPMAP_NEAREST

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_MIPMAP_NONE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_ABOVEBELOW

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_ANAGLYPH

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_INTERLACED

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_NOSTEREO

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_SIDEBYSIDE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### VSYNC_ADAPTIVE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### VSYNC_OFF

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### VSYNC_ON

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

