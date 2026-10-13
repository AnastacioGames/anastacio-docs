---
title: "KX_PythonMotion"
description: "Referência da classe Range.types.KX_PythonMotion"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Sensores de movimento do dispositivo (celular ou tablet), disponíveis como `Range.logic.motion`.

Os valores vêm do navegador no runtime Web (`DeviceMotionEvent` e `DeviceOrientationEvent`), inclusive no app Android, que roda o runtime Web dentro de uma WebView. Nas outras plataformas ainda não há fonte de sensores: `available` é `False`, os vetores são zero e `tilt` é `(0.0, 0.0)`, para que o mesmo script rode em todo lugar.

Os vetores usam os eixos da tela como ela está sendo mostrada, em retrato ou paisagem: x para a direita, y para o topo da tela e z para fora da tela, na direção do jogador.

Um objeto controlado pela inclinação:

```python

from Range import logic, events

def main(cont):
    own = cont.owner
    if logic.mouse.inputs[events.LEFTMOUSE].activated:  # um toque na tela
        logic.motion.calibrate()
    x, y = logic.motion.tilt
    own.applyForce((x * 20.0, y * 20.0, 0.0))
```

### available

`True` enquanto os sensores estão mandando dados. Vira `False` quando nenhuma leitura chegou no último segundo (sem sensor, navegador de desktop, página em segundo plano) (somente leitura).

**Tipo:** boolean

### gyroscope

Velocidade de rotação em torno de cada eixo da tela, em radianos por segundo (somente leitura).

**Tipo:** `mathutils.Vector`

### accelerometer

Aceleração incluindo a gravidade, em m/s². Com o dispositivo parado, deitado de face para cima, fica perto de `(0, 0, 9.8)` (somente leitura).

**Tipo:** `mathutils.Vector`

### gravity

Só a gravidade, em m/s², apontando para cima como em `accelerometer`. Quando o dispositivo não informa a aceleração sem gravidade, ela é estimada a partir de `accelerometer` com um filtro passa-baixa (somente leitura).

**Tipo:** `mathutils.Vector`

### orientation

Ângulos de orientação do dispositivo `(alpha, beta, gamma)` em graus, exatamente como o navegador entrega. Seguem os eixos do dispositivo, não os da tela (somente leitura).

**Tipo:** `mathutils.Vector`

### tilt

Quanto o dispositivo está inclinado em relação à posição neutra, de -1.0 a 1.0 em cada eixo: a direção da tela para onde uma bola rolaria. `x` é positivo quando a borda direita da tela desce, `y` quando a borda de cima desce. A posição neutra é o dispositivo deitado, até `calibrate` ser chamado (somente leitura).

**Tipo:** tuple (float, float)

### calibrate()

Usa a posição atual como neutra para `tilt`, para o jogador segurar o dispositivo do jeito que preferir.

**Retorna:** `True` se havia uma leitura do sensor para calibrar, `False` se não.

**Tipo do retorno:** boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### recenter()

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

Usa a direção atual da cabeça (VR) como "frente". `False` se o sensor não está pronto.

**Retorna:** `bool`

### headOrientation

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Orientação da cabeça (matriz 3×3), já recentralizada.

### recenterTime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tempo, em segundos, para recentralizar sozinho quando a cabeça fica parada (0 desliga).

### smoothing

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Suavização do movimento da cabeça (0 a 5).

