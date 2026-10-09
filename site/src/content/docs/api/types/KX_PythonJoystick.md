---
title: "KX_PythonJoystick"
description: "Referência da classe Range.types.KX_PythonJoystick"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Uma interface Python para um joystick.

### name

O nome dado ao joystick pelo sistema operacional (somente leitura)

**Tipo:** string

### activeButtons

Uma lista dos valores dos botões ativos (somente leitura)

**Tipo:** list

### axisValues

O estado dos eixos do joystick, como uma lista de `numAxis` valores (somente leitura).

**Tipo:** list of ints.

Cada um dá o valor de um eixo entre -1.0 e 1.0, conforme o quanto o eixo está empurrado; 0 quando solto. Os 2 primeiros valores são usados pela maioria dos joysticks e gamepads para o controle de direção. O 3º e o 4º só existem em alguns joysticks e podem ser usados para controles quaisquer.

* esquerda:[-1.0, 0.0, ...]
* direita:[1.0, 0.0, ...]
* up:[0.0, -1.0, ...]
* baixo:[0.0, 1.0, ...]

### hatValues (Deprecated. Use :data:`activeButtons` instead)

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

### numAxis

O número de eixos do joystick neste índice (somente leitura).

**Tipo:** integer

### numButtons

O número de botões do joystick neste índice (somente leitura).

**Tipo:** integer

### numHats (Deprecated. Use :data:`numButtons` instead)

O número de hats do joystick neste índice (somente leitura).

**Tipo:** integer

### startVibration()

Começa a vibração.

**Retorna:** None

### stopVibration()

<span class="ae-badge pendente">sem documentação</span>

Para a vibração.

**Retorna:** None

### strengthLeft

<span class="ae-badge pendente">sem documentação</span>

Força do motor de baixa frequência do joystick (em geral fica à esquerda).

**Tipo:** float (0.0 to 1.0)

### strengthRight

<span class="ae-badge pendente">sem documentação</span>

Força do motor de alta frequência do joystick (em geral fica à direita).

**Tipo:** float (0.0 to 1.0)

### duration

<span class="ae-badge pendente">sem documentação</span>

Duração da vibração em milissegundos.

**Tipo:** integer (0 to infinite)

### isVibrating

<span class="ae-badge pendente">sem documentação</span>

Verifica o status da vibração do joystick

**Tipo:** bool (true vibrating and false stopped)

### hasVibration

<span class="ae-badge pendente">sem documentação</span>

Verifica se o joystick suporta vibração

**Tipo:** bool (true supported and false not supported)

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### stopVibration()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### duration

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### hasVibration

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### inputs

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### isVibrating

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### strengthLeft

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### strengthRight

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

