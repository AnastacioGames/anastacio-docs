---
title: "SCA_JoystickSensor"
description: "Referência da classe Range.types.SCA_JoystickSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Este sensor detecta eventos do joystick do jogador.

### axisValues

O estado dos eixos do joystick, como uma lista de `numAxis` valores (somente leitura).

**Tipo:** list of ints.

Cada um dá o valor de um eixo entre -32767 e 32767, conforme o quanto o eixo está empurrado; 0 quando solto. Os 2 primeiros valores são usados pela maioria dos joysticks e gamepads para o controle de direção. O 3º e o 4º só existem em alguns joysticks e podem ser usados para controles quaisquer.

* esquerda:[-32767, 0, ...]
* direita:[32767, 0, ...]
* up:[0, -32767, ...]
* baixo:[0, 32767, ...]

### axisSingle

como `axisValues`, mas devolve um único valor de eixo, definido pelo sensor (somente leitura).

**Tipo:** integer

:::note
Use só em sensores do tipo "Single Axis"; senão, levanta um erro.
:::

### hatValues (Deprecated. Use :data:button instead)

O estado dos hats do joystick, como uma lista de `numHats` valores (somente leitura).

**Tipo:** list of ints

Cada um dá a direção do hat de 1 a 12; 0 quando inativo.

As direções do hat são estas...

* 0:Nenhuma
* 1:Up
* 2:Direita
* 4:Baixo
* 8:Esquerda
* 3:Cima - Direita
* 6:Baixo - Direita
* 12:Baixo - Esquerda
* 9:Cima - Esquerda

### hatSingle (Deprecated. Use :data:button instead)

Como `hatValues`, mas devolve uma única direção de hat, definida pelo sensor (somente leitura).

**Tipo:** integer

### numAxis

O número de eixos do joystick neste índice (somente leitura).

**Tipo:** integer

### numButtons

O número de botões do joystick neste índice (somente leitura).

**Tipo:** integer

### numHats (Deprecated. Use :data:numButtons instead)

O número de hats do joystick neste índice (somente leitura).

**Tipo:** integer

### connected

True se há um joystick conectado neste índice (somente leitura).

**Tipo:** boolean

### index

O índice do joystick a usar (de 0 a 7). O primeiro joystick é sempre 0.

**Tipo:** integer

### threshold

Limite do eixo. Movimentos do eixo abaixo deste limite não disparam evento. Use valores entre 0 e 32767; valores menores são mais sensíveis.

**Tipo:** integer

### button

O índice do botão a que o sensor reage (primeiro botão = 0). Com a opção "All Events" ligada, esta opção não tem efeito.

**Tipo:** integer

### axis

O eixo a que este sensor reage, como uma lista de dois valores [axisIndex, axisDirection]

* axisIndex: o índice do eixo usado para detectar movimento, 1=controle de direção principal, 2=controle de direção secundário.
* axisDirection: 0=direita, 1=cima, 2=esquerda, 3=baixo.

**Tipo:** [integer, integer]

### hat (Deprecated. Use :data:button instead)

O hat a que o sensor reage, como uma lista de dois valores: [hatIndex, hatDirection]

* hatIndex: o índice do hat usado para detectar movimento, 1=hat principal, 2=hat secundário (4 no máximo).
* hatDirection: 1-12.

**Tipo:** [integer, integer]

### getButtonActiveList()

**Retorna:** Uma lista com os índices dos botões apertados agora.

**Tipo do retorno:** list

### getButtonStatus(buttonIndex)

- **`buttonIndex`**: o índice do botão, 0=primeiro botão
  - tipo: integer

**Retorna:** Se o botão indicado está apertado agora.

**Tipo do retorno:** boolean

