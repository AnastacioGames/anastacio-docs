---
title: Microfone e gravação de voz
description: Grave sons no editor e use o microfone do jogador no jogo, com efeitos de voz, em desktop, Web e Android.
---

A engine grava voz no editor e ouve o microfone durante o jogo. Funciona em desktop, Web e Android.

## Gravar no editor

O botão **Record** fica na barra superior. Um clique grava direto para o Sequencer. Enquanto grava, ele fica vermelho e mostra o tempo e o volume.

As opções ao lado do botão são:

- **Record New Sound**: grava um som novo, sem colocá-lo no Sequencer.
- **Select Microphone**: escolhe o microfone.
- **Adjust Sound**: corte, fades, normalizar e efeitos de voz, salvos num WAV novo.
- **Open Video Sequencer Window**: abre o Sequencer numa janela separada.

Também há botão de gravar onde o som é usado: na fala da cutscene, no nó Sound da Logic Tree e nos strips de som do Sequencer.

## Usar no jogo sem código

**Sensor Microphone**

| Modo | Quando dispara |
|---|---|
| **Talking** | Enquanto a voz está acima do limite. Continua ligado por **Hold** segundos. |
| **Shout / Clap** | Um pulso quando um som forte passa do limite (palma, grito, sopro). |
| **Silence** | Depois de **Hold** segundos abaixo do limite. |

**Atuador Voice**

| Modo | O que faz |
|---|---|
| **Record** | Grava enquanto o sensor está ligado, ou até **Max Seconds**. |
| **Play Recording** | Toca a gravação com efeito. |
| **Live** | Faz ouvir o microfone com efeito enquanto o sensor está ligado. |
| **Stop** | Para a voz ao vivo. |
| **Save WAV** | Salva a gravação como `<nome>.wav` na pasta do jogo. |

Na Logic Tree, use os nós **When Talking** e **Voice**. Na UI Tree, há **Microphone Meter** e **Enable Microphone**.

## Efeitos de voz

`NONE`, `CHIPMUNK` (aguda), `GIANT` (grave), `ROBOT`, `RADIO`, `ECHO`, `CAVE` e `REVERSE` (só em gravações).

:::caution
No modo ao vivo, use fones: caixas de som realimentam o microfone.
:::

## Usar por Python

```python
import Range

# Liga o microfone (na Web, depois de um clique ou toque).
if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

# Abre a boca do personagem conforme o volume da voz.
own["mouth"] = Range.audio.microphoneLevel()

# Grava, para e toca com efeito.
Range.audio.microphoneRecordStart()
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

No exemplo, `own` é o objeto do seu script. A lista completa está em [`Range.audio`](../../api/modulos/audio/), [`KX_MicrophoneSensor`](../../api/types/kx_microphonesensor/) e [`KX_VoiceActuator`](../../api/types/kx_voiceactuator/).

## Web e Android

No painel de export Web, a opção **Microphone** tem **Auto**, **On** e **Off**. Em **Auto**, ela liga quando o jogo usa o microfone.

- **Web:** o navegador pede permissão ao jogador. O microfone começa depois do primeiro toque ou clique e precisa de `https` (ou `localhost`).
- **Android:** o APK só pede `RECORD_AUDIO` quando o pacote foi exportado com microfone.
