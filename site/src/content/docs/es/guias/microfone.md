---
title: Micrófono y grabación de voz
description: Graba sonidos en el editor y usa el micrófono del jugador en el juego, con efectos de voz, en escritorio, Web y Android.
---

El motor graba voz en el editor y escucha el micrófono durante el juego. Funciona en escritorio, Web y Android.

## Grabar en el editor

El botón **Record** está en la barra superior. Un clic graba directamente en el Sequencer. Mientras graba se pone rojo y muestra el tiempo y el volumen.

Las opciones junto al botón son:

- **Record New Sound**: graba un sonido nuevo sin colocarlo en el Sequencer.
- **Select Microphone**: elige el micrófono.
- **Adjust Sound**: recorte, fundidos, normalizar y efectos de voz, guardados en un WAV nuevo.
- **Open Video Sequencer Window**: abre el Sequencer en una ventana aparte.

También hay un botón de grabar donde se usa el sonido: en la línea de la cutscene, en el nodo Sound de la Logic Tree y en los strips de sonido del Sequencer.

## Usarlo en el juego sin código

**Sensor Microphone**

| Modo | Cuándo se activa |
|---|---|
| **Talking** | Mientras la voz supera el umbral. Sigue activo durante **Hold** segundos. |
| **Shout / Clap** | Un pulso cuando un sonido fuerte supera el umbral (palmada, grito, soplido). |
| **Silence** | Tras **Hold** segundos por debajo del umbral. |

**Actuador Voice**

| Modo | Qué hace |
|---|---|
| **Record** | Graba mientras el sensor está activo, o hasta **Max Seconds**. |
| **Play Recording** | Reproduce la grabación con el efecto. |
| **Live** | Hace oír el micrófono con el efecto mientras el sensor está activo. |
| **Stop** | Detiene la voz en directo. |
| **Save WAV** | Guarda la grabación como `<nombre>.wav` en la carpeta del juego. |

En la Logic Tree, usa los nodos **When Talking** y **Voice**. La UI Tree tiene **Microphone Meter** y **Enable Microphone**.

## Efectos de voz

`NONE`, `CHIPMUNK` (aguda), `GIANT` (grave), `ROBOT`, `RADIO`, `ECHO`, `CAVE` y `REVERSE` (solo grabaciones).

:::caution
En modo directo, usa auriculares: los altavoces realimentan el micrófono.
:::

## Usarlo desde Python

```python
import Range

# Enciende el micrófono (en la Web, tras un clic o toque).
if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

# Abre la boca del personaje según el volumen de la voz.
own["mouth"] = Range.audio.microphoneLevel()

# Graba, detén y reproduce con efecto.
Range.audio.microphoneRecordStart()
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

En el ejemplo, `own` es el objeto de tu script. La lista completa está en [`Range.audio`](../../api/modulos/audio/), [`KX_MicrophoneSensor`](../../api/types/kx_microphonesensor/) y [`KX_VoiceActuator`](../../api/types/kx_voiceactuator/).

## Web y Android

En el panel de exportación Web, la opción **Microphone** tiene **Auto**, **On** y **Off**. **Auto** la activa cuando el juego usa el micrófono.

- **Web:** el navegador pide permiso al jugador. El micrófono empieza tras el primer toque o clic y necesita `https` (o `localhost`).
- **Android:** el APK solo pide `RECORD_AUDIO` cuando el paquete se exportó con micrófono.
