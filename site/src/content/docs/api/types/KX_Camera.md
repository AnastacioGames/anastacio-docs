---
title: "KX_Camera"
description: "Referência da classe Range.types.KX_Camera"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)

:::tip[Veja também]
[`KX_Scene`](../../types/kx_scene/), [`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`KX_GameObject`](../../types/kx_gameobject/), [`Range.render`](../../modulos/render/)
:::



Um objeto de câmera.

### INSIDE

Veja `sphereInsideFrustum` e `boxInsideFrustum`

### INTERSECT

Veja `sphereInsideFrustum` e `boxInsideFrustum`

### OUTSIDE

Veja `sphereInsideFrustum` e `boxInsideFrustum`

### lens

O valor da lente da câmera.

**Tipo:** float

### lodDistanceFactor

Fator que multiplica a distância até a câmera para ajustar os níveis de detalhe. Um valor < 1.0 faz a distância usada para calcular os níveis de detalhe diminuir.

**Tipo:** float

### fov

O campo de visão da câmera.

**Tipo:** float

### ortho_scale

A escala da visão da câmera no modo ortográfico.

**Tipo:** float

### near

A distância de corte próxima (near clip) da câmera.

**Tipo:** float

### far

A distância de corte distante (far clip) da câmera.

**Tipo:** float

### shift_x

O deslocamento horizontal da câmera.

**Tipo:** float

### shift_y

O deslocamento vertical da câmera.

**Tipo:** float

### perspective

True se a câmera usa projeção em perspectiva; False para projeção ortográfica.

**Tipo:** boolean

### frustum_culling

True se a câmera faz frustum culling.

**Tipo:** boolean

### activityCulling

True se esta câmera é usada para calcular a distância dos objetos no culling de atividade.

**Tipo:** boolean

### projection_matrix

A matriz de projeção 4x4 da câmera.

:::note
Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).
:::

**Tipo:** 4x4 Matrix [[float]]

### projectionMatrixLeft

A matriz de projeção 4x4 do olho esquerdo.

:::note
Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).
:::

**Tipo:** 4x4 Matrix [[float]]

### projectionMatrixRight

A matriz de projeção 4x4 do olho direito.

:::note
Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).
:::

**Tipo:** 4x4 Matrix [[float]]

### modelview_matrix

A matriz model view 4x4 da câmera (somente leitura).

**Tipo:** 4x4 Matrix [[float]]

:::note
Esta matriz é recalculada a cada frame a partir da posição e da orientação da câmera. Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).
:::

### camera_to_world

A transformação da câmera para o mundo (somente leitura).

**Tipo:** 4x4 Matrix [[float]]

:::note
Esta matriz é recalculada a cada frame a partir da posição e da orientação da câmera.
:::

### world_to_camera

A transformação do mundo para a câmera (somente leitura).

**Tipo:** 4x4 Matrix [[float]]

:::note
Recalculada a cada frame a partir da posição e da orientação da câmera.
:::

:::note
É a inversa de camera_to_world.
:::

### useViewport

True quando a câmera é usada como viewport; defina True para ligar uma viewport para esta câmera.

**Tipo:** boolean

### viewport

Retângulo da viewport usado no último render desta câmera, em pixels (somente leitura). Proporções definidas no editor já vêm convertidas para a janela.

**Tipo:** list [left, bottom, right, top]

### sphereInsideFrustum(centre, radius)

Testa a esfera dada contra o frustum da visão.

- **`centre`**: O centro da esfera (em coordenadas do mundo).
  - tipo: list [x, y, z]
- **`radius`**: O raio da esfera
  - tipo: float

**Retorna:** `INSIDE`, `OUTSIDE` ou `INTERSECT`

**Tipo do retorno:** integer

:::note
Logo que a câmera é iniciada, o resultado é inválido, porque a matriz de projeção ainda não foi definida.
:::

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Uma esfera de raio 4.0 em [x, y, z] = [1.0, 1.0, 1.0]
if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
    # A esfera está dentro do frustum!
    # Faça algo útil!
else:
    # A esfera está fora do frustum
```

### boxInsideFrustum(box)

Testa a caixa dada contra o frustum da visão.

- **`box`**: Os oito (8) cantos da caixa (em coordenadas do mundo).
  - tipo: list of lists

**Retorna:** `INSIDE`, `OUTSIDE` ou `INTERSECT`

:::note
Logo que a câmera é iniciada, o resultado é inválido, porque a matriz de projeção ainda não foi definida.
:::

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Caixa a testar...
box = []
box.append([-1.0, -1.0, -1.0])
box.append([-1.0, -1.0,  1.0])
box.append([-1.0,  1.0, -1.0])
box.append([-1.0,  1.0,  1.0])
box.append([ 1.0, -1.0, -1.0])
box.append([ 1.0, -1.0,  1.0])
box.append([ 1.0,  1.0, -1.0])
box.append([ 1.0,  1.0,  1.0])

if (cam.boxInsideFrustum(box) != cam.OUTSIDE):
  # A caixa está dentro ou cruza o frustum!
  # Faça algo útil!
else:
  # A caixa está fora do frustum!
```

### pointInsideFrustum(point)

Testa o ponto dado contra o frustum da visão.

- **`point`**: O ponto a testar (em coordenadas do mundo).
  - tipo: 3D Vector

**Retorna:** True se o ponto está dentro do frustum de visão desta câmera.

**Tipo do retorno:** boolean

:::note
Logo que a câmera é iniciada, o resultado é inválido, porque a matriz de projeção ainda não foi definida.
:::

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Testa o ponto [0.0, 0.0, 0.0]
if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
  # O ponto está dentro do frustum!
  # Faça algo útil!
else:
  # A caixa está fora do frustum!
```

### getCameraToWorld()

Devolve a transformação da câmera para o mundo.

**Retorna:** A matriz de transformação da câmera para o mundo.

**Tipo do retorno:** matrix (4x4 list)

### getWorldToCamera()

Devolve a transformação do mundo para a câmera.

Devolve a inversa de getCameraToWorld().

**Retorna:** A matriz de transformação do mundo para a câmera.

**Tipo do retorno:** matrix (4x4 list)

### setOnTop()

Coloca a viewport desta câmera por cima de todas as outras.

### setViewport(left, bottom, right, top)

Define a região desta viewport na tela, em pixels.

Use `Range.render.getWindowHeight` e `Range.render.getWindowWidth` para calcular valores relativos à tela inteira.

- **`left`**: Coordenada da esquerda desta viewport, em pixels
  - tipo: integer
- **`bottom`**: Coordenada de baixo desta viewport, em pixels
  - tipo: integer
- **`right`**: Coordenada da direita desta viewport, em pixels
  - tipo: integer
- **`top`**: Coordenada de cima desta viewport, em pixels
  - tipo: integer

### getScreenPosition(object)

Pega a posição de um objeto projetada na tela.

```python

# Para um objeto no meio da tela, coord = [0.5, 0.5]
coord = camera.getScreenPosition(object)
```

- **`object`**: Nome do objeto ou lista [x, y, z]
  - tipo: `KX_GameObject` or 3D Vector

**Retorna:** A posição do objeto em coordenadas de tela.

**Tipo do retorno:** list [x, y]

### getScreenVect(x, y)

Pega o vetor que sai da posição da câmera na direção da coordenada de tela.

- **`x`**: Eixo X
  - tipo: float
- **`y`**: Eixo Y
  - tipo: float

**Tipo do retorno:** 3D Vector

**Retorna:** O vetor a partir da coordenada de tela.

```python

# Pega o vetor da direção da frente da câmera:
m_vect = camera.getScreenVect(0.5, 0.5)
```

### getScreenRay(x, y, dist, property="", xray=False, mask=0xFFFF)

Olha na direção de uma coordenada de tela (x, y) e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop. O raio funciona como KX_GameObject->rayCastTo.

- **`x`**: Eixo X
  - tipo: float
- **`y`**: Eixo Y
  - tipo: float
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`property`**: Nome da propriedade que o objeto precisa ter; se omitido, detecta qualquer objeto
  - tipo: string
- **`xray`**: O raio atravessa os objetos que não têm a propriedade, como a opção X-Ray do sensor Mouse
  - tipo: boolean
- **`mask`**: Máscara de colisão; o raio só atinge objetos destes grupos de colisão
  - tipo: bitfield

**Tipo do retorno:** `KX_GameObject`

**Retorna:** O primeiro objeto atingido, ou None se não atingir nada ou se o objeto não tiver a propriedade

```python

# Pega um objeto com a propriedade "wall" na frente da câmera, a até 100 de distância:
target = camera.getScreenRay(0.5, 0.5, 100, "wall")
```

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### shake(trauma, duration=0.0)

 <small>método</small>

Treme a câmera. `trauma` vai de 0 a 1 e soma com o terremoto do World. Com `duration`, o tremor some nesse tempo; sem, diminui no ritmo de `shakeDecay` por segundo.

### cameraSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Velocidade atual da câmera (unidades por segundo), usada pelos efeitos ligados à velocidade.

### catEyeStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Força do bokeh "olho de gato" do desfoque (DOF), de 0.0 a 1.0: os círculos ficam achatados perto das bordas.

### chromaticStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Força da aberração cromática, de 0.0 a 5.0.

### directionalBlurMax

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Limite do desfoque direcional (rastro ao girar a câmera), de 0.0 a 0.2.

### directionalBlurStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Força do desfoque direcional, de 0.0 a 2.0.

### dofBlur

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tamanho máximo do desfoque de profundidade (DOF), de 0 a 32.

### dofQuality

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Qualidade do DOF: 0 baixa, 1 média, 2 alta.

### droneAmplitude

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Amplitude do balanço do modo de rastreio Drone (0 a 20).

### droneFrequency

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Frequência do balanço do modo Drone (0 a 20).

### fisheyeStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Distorção olho de peixe, de -1.0 (almofada) a 1.0 (barril).

### focusDistance

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Distância de foco usada neste frame, depois de suavizada.

### focusManualDistance

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Distância de foco quando `focusMode` é 0 (manual).

### focusMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Como o foco é escolhido: 0 manual (`focusManualDistance`), 1 objeto (`focusObject`), 2 propriedade (`focusProperty`), 3 automático (raio no ponto da tela).

### focusObject

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Objeto em foco quando `focusMode` é 1. `None` para nenhum.

### focusPosition

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Posição no mundo do ponto em foco, ou `None`.

### focusProperty

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nome da propriedade de jogo usada quando `focusMode` é 2: foca o objeto mais próximo que a tiver verdadeira.

### focusRange

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Faixa de distância, em volta do foco, que continua nítida.

### focusScreenPosition

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Posição na tela (0 a 1) do ponto em foco.

### focusSmooth

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Suavização da troca de foco, de 0 (instantânea) a 10.

### focusTarget

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Objeto que está em foco agora, ou `None`.

### focusValid

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

`True` quando o foco achou um alvo neste frame.

### gazeDirection

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Direção para onde a câmera está olhando, no mundo.

### shakeAmplitude

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Amplitude máxima do tremor (0 a 0.5).

### shakeDecay

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Quanto o tremor diminui por segundo (0 a 20).

### shakeFrequency

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Frequência do tremor (0 a 60).

### shakeTrauma

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Trauma atual do tremor (0 a 1).

### speedBlurMaxSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Velocidade em que o desfoque de velocidade chega ao máximo.

### speedBlurStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Força do desfoque de velocidade, de 0.0 a 2.0.

### speedOverride

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Velocidade usada pelos efeitos no lugar da velocidade real. -1 desliga e volta a usar a real.

### trackBank

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Inclinação lateral da câmera nas curvas do rastreio (0 a 5).

### trackDeadzone

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Zona morta do rastreio: o alvo pode se mover nessa margem da tela sem a câmera virar (0 a 0.5).

### trackLimit

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Ângulo máximo, em radianos, que o rastreio pode girar a câmera.

### trackMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Modo de rastreio: 0 desligado, 1 olhar para o alvo, 2 drone.

### trackOrientation

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Orientação calculada pelo rastreio neste frame.

### trackScreenOffset

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Deslocamento `[x, y]` do alvo na tela, de -0.5 a 0.5.

### trackSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Velocidade com que a câmera vira para o alvo (0 a 10).

### useBlurProtect

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Protege o centro da tela dos desfoques.

### useCatEye

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga o bokeh olho de gato no DOF.

### useChromatic

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga a aberração cromática.

### useChromaticSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Faz a aberração cromática aumentar com a velocidade.

### useDirectionalBlur

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga o desfoque direcional.

### useDof

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga a profundidade de campo (DOF).

### useShakeRoll

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

O tremor também gira a câmera em volta do eixo de visão.

### useSpeedBlur

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga o desfoque de velocidade.

### useTrackUpLock

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Mantém o "para cima" da câmera fixo durante o rastreio.

### useVignette

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga a vinheta (bordas escuras).

### vignetteRadius

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Raio da vinheta (0 a 2).

### vignetteStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Força da vinheta (0 a 1).

