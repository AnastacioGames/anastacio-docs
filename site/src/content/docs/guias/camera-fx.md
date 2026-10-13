---
title: Câmera do jogo (foco, efeitos e tremor)
description: Foco automático, câmera que segue o alvo, desfoque de velocidade, DOF e tremor, sem filtros em Python.
---

A câmera da Anastacio tem efeitos nativos: foco que acompanha um objeto, rastreio (a câmera gira para seguir o alvo), DOF, desfoque de velocidade, aberração, vinheta e tremor. Tudo é configurado nas propriedades da câmera e pode ser mudado pelo Python em [`KX_Camera`](../../api/types/kx_camera/).

Tudo vem desligado. Só a câmera ativa da cena é atualizada.

## 1. Foco e rastreio no editor

Selecione a câmera e abra **Properties > Camera** (com o motor Range Game).

No painel **Focus & Tracking**:

1. Em **Focus**, escolha **Object** e coloque o objeto que a câmera deve seguir (o carro, o jogador).
2. Em **Tracking**, escolha **Look At**. A câmera continua no lugar, mas gira suavemente para manter o alvo na tela.
3. **Track Smooth** controla a suavidade (em segundos). **Framing Offset** com Y negativo deixa o alvo um pouco abaixo do centro.

<!-- PRINT: painel Focus & Tracking com Focus Object e Tracking Look At -->

## 2. Efeitos

No painel **Camera Effects**:

- **DOF**: desfoca o que está fora da distância de foco. Funciona junto com o foco do passo anterior.
- **Speed Blur**: borrão radial que cresce com a velocidade da câmera. **Full Speed** é a velocidade (m/s) em que o efeito chega ao máximo.
- **Protect Focus**: deixa o alvo em foco fora do borrão (o carro continua nítido).
- **Vignette / Fisheye**: cantos escuros e distorção de lente.

Cada efeito só custa desempenho enquanto estiver ligado.

## 3. Tremor por script

`shake(trauma, duration)` treme a câmera. `trauma` vai de 0 a 1 e vários tremores somam. Exemplo: tremer quando apertar Espaço, como numa explosão.

```python
import Range
from Range import events, logic


class TremerNoEspaco(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        pass

    def update(self):
        teclado = logic.keyboard.inputs[events.SPACEKEY]
        if teclado.activated:
            camera = self.object.scene.active_camera
            camera.shake(0.8, 0.6)
```

Anexe em qualquer objeto da cena. A força e a frequência do tremor ficam no painel **Camera Shake** da câmera (ou em `shakeAmplitude` e `shakeFrequency`).

## 4. Ligar efeitos pelo menu do jogo

Um menu de opções pode ligar ou desligar efeitos durante o jogo:

```python
camera = Range.logic.getCurrentScene().active_camera
camera.useSpeedBlur = True
camera.speedBlurStrength = 0.5
camera.useDof = False
```

## Grão de filme

O grão fica na cena, não na câmera: **Render > Post Processing**, opção Film Grain. No jogo:

```python
cena = Range.logic.getCurrentScene()
cena.filterManager.changeGrainValues(True, 0.3)
```
