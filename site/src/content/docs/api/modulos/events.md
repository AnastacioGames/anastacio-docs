---
title: "Range.events"
description: "Referência do módulo Range.events"
---

## Introdução

Este módulo guarda as constantes de teclas usadas pelo SCA_KeyboardSensor.

```python

# Configura um sensor de teclado conectado para aceitar F1
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' é um sensor de teclado
sensor = co.sensors["Keyboard"]
sensor.key = Range.events.F1KEY
```

```python

# Faz o esquema de todas as teclas
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' é um sensor de teclado
sensor = co.sensors["Keyboard"]

for key, input in sensor.inputs:
	# key[0] == Range.events.keycode = event.type, key[1] = input
	if Range.logic.KX_INPUT_JUST_ACTIVATED in input.queue:
		if key == Range.events.WKEY:
			# Ativa para a frente!
		if key == Range.events.SKEY:
			# Ativa para trás!
		if key == Range.events.AKEY:
			# Ativa para a esquerda!
		if key == Range.events.DKEY:
			# Ativa para a direita!
```

```python

# O esquema de todas as teclas sem sensor de teclado (mas você vai
# precisar de um sensor Always com o modo pulse ligado)
import Range

# Só encurtando os nomes aqui
keyboard = Range.logic.keyboard
JUST_ACTIVATED = Range.logic.KX_INPUT_JUST_ACTIVATED

if JUST_ACTIVATED in keyboard.inputs[Range.events.WKEY].queue:
	print("Activate Forward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.SKEY].queue:
	print("Activate Backward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.AKEY].queue:
	print("Activate Left!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.DKEY].queue:
	print("Activate Right!")
```

## Funções

### EventToString(event)

Devolve o nome em texto de um evento de tecla. Gera ValueError se o evento for inválido.

- **`event`**: Constante de evento de tecla de `Range.events` ou do sensor de teclado.
  - tipo: int

**Tipo do retorno:** string

### EventToCharacter(event, shift)

Devolve o nome em texto de um evento de tecla. Devolve um texto vazio se o evento não puder virar um caractere.

  - tipo: int
- **`event`**: Constante de evento de tecla de `Range.events` ou do sensor de teclado.
  - tipo: bool
- **`shift`**: Defina como true se o shift estiver apertado.

**Tipo do retorno:** string

## Teclas (constantes)

## Teclas do mouse

### LEFTMOUSE

<span class="ae-badge pendente">sem descrição</span>

### MIDDLEMOUSE

<span class="ae-badge pendente">sem descrição</span>

### RIGHTMOUSE

<span class="ae-badge pendente">sem descrição</span>

### WHEELUPMOUSE

<span class="ae-badge pendente">sem descrição</span>

### WHEELDOWNMOUSE

<span class="ae-badge pendente">sem descrição</span>

### LEFTTHUMBMOUSE

<span class="ae-badge pendente">sem descrição</span>

### RIGHTTHUMBMOUSE

<span class="ae-badge pendente">sem descrição</span>

### BUTTON6MOUSE

<span class="ae-badge pendente">sem descrição</span>

### BUTTON7MOUSE

<span class="ae-badge pendente">sem descrição</span>

### MOUSEX

<span class="ae-badge pendente">sem descrição</span>

### MOUSEY

## Teclas do teclado

## Letras

### AKEY

<span class="ae-badge pendente">sem descrição</span>

### BKEY

<span class="ae-badge pendente">sem descrição</span>

### CKEY

<span class="ae-badge pendente">sem descrição</span>

### DKEY

<span class="ae-badge pendente">sem descrição</span>

### EKEY

<span class="ae-badge pendente">sem descrição</span>

### FKEY

<span class="ae-badge pendente">sem descrição</span>

### GKEY

<span class="ae-badge pendente">sem descrição</span>

### HKEY

<span class="ae-badge pendente">sem descrição</span>

### IKEY

<span class="ae-badge pendente">sem descrição</span>

### JKEY

<span class="ae-badge pendente">sem descrição</span>

### KKEY

<span class="ae-badge pendente">sem descrição</span>

### LKEY

<span class="ae-badge pendente">sem descrição</span>

### MKEY

<span class="ae-badge pendente">sem descrição</span>

### NKEY

<span class="ae-badge pendente">sem descrição</span>

### OKEY

<span class="ae-badge pendente">sem descrição</span>

### PKEY

<span class="ae-badge pendente">sem descrição</span>

### QKEY

<span class="ae-badge pendente">sem descrição</span>

### RKEY

<span class="ae-badge pendente">sem descrição</span>

### SKEY

<span class="ae-badge pendente">sem descrição</span>

### TKEY

<span class="ae-badge pendente">sem descrição</span>

### UKEY

<span class="ae-badge pendente">sem descrição</span>

### VKEY

<span class="ae-badge pendente">sem descrição</span>

### WKEY

<span class="ae-badge pendente">sem descrição</span>

### XKEY

<span class="ae-badge pendente">sem descrição</span>

### YKEY

<span class="ae-badge pendente">sem descrição</span>

### ZKEY

## Números

### ZEROKEY

<span class="ae-badge pendente">sem descrição</span>

### ONEKEY

<span class="ae-badge pendente">sem descrição</span>

### TWOKEY

<span class="ae-badge pendente">sem descrição</span>

### THREEKEY

<span class="ae-badge pendente">sem descrição</span>

### FOURKEY

<span class="ae-badge pendente">sem descrição</span>

### FIVEKEY

<span class="ae-badge pendente">sem descrição</span>

### SIXKEY

<span class="ae-badge pendente">sem descrição</span>

### SEVENKEY

<span class="ae-badge pendente">sem descrição</span>

### EIGHTKEY

<span class="ae-badge pendente">sem descrição</span>

### NINEKEY

## Teclas modificadoras

### CAPSLOCKKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTCTRLKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTALTKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTALTKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTCTRLKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTSHIFTKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTSHIFTKEY

## Setas

### LEFTARROWKEY

<span class="ae-badge pendente">sem descrição</span>

### DOWNARROWKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTARROWKEY

<span class="ae-badge pendente">sem descrição</span>

### UPARROWKEY

## Teclado numérico

### PAD0

<span class="ae-badge pendente">sem descrição</span>

### PAD1

<span class="ae-badge pendente">sem descrição</span>

### PAD2

<span class="ae-badge pendente">sem descrição</span>

### PAD3

<span class="ae-badge pendente">sem descrição</span>

### PAD4

<span class="ae-badge pendente">sem descrição</span>

### PAD5

<span class="ae-badge pendente">sem descrição</span>

### PAD6

<span class="ae-badge pendente">sem descrição</span>

### PAD7

<span class="ae-badge pendente">sem descrição</span>

### PAD8

<span class="ae-badge pendente">sem descrição</span>

### PAD9

<span class="ae-badge pendente">sem descrição</span>

### PADPERIOD

<span class="ae-badge pendente">sem descrição</span>

### PADSLASHKEY

<span class="ae-badge pendente">sem descrição</span>

### PADASTERKEY

<span class="ae-badge pendente">sem descrição</span>

### PADMINUS

<span class="ae-badge pendente">sem descrição</span>

### PADENTER

<span class="ae-badge pendente">sem descrição</span>

### PADPLUSKEY

## Teclas de função

### F1KEY

<span class="ae-badge pendente">sem descrição</span>

### F2KEY

<span class="ae-badge pendente">sem descrição</span>

### F3KEY

<span class="ae-badge pendente">sem descrição</span>

### F4KEY

<span class="ae-badge pendente">sem descrição</span>

### F5KEY

<span class="ae-badge pendente">sem descrição</span>

### F6KEY

<span class="ae-badge pendente">sem descrição</span>

### F7KEY

<span class="ae-badge pendente">sem descrição</span>

### F8KEY

<span class="ae-badge pendente">sem descrição</span>

### F9KEY

<span class="ae-badge pendente">sem descrição</span>

### F10KEY

<span class="ae-badge pendente">sem descrição</span>

### F11KEY

<span class="ae-badge pendente">sem descrição</span>

### F12KEY

<span class="ae-badge pendente">sem descrição</span>

### F13KEY

<span class="ae-badge pendente">sem descrição</span>

### F14KEY

<span class="ae-badge pendente">sem descrição</span>

### F15KEY

<span class="ae-badge pendente">sem descrição</span>

### F16KEY

<span class="ae-badge pendente">sem descrição</span>

### F17KEY

<span class="ae-badge pendente">sem descrição</span>

### F18KEY

<span class="ae-badge pendente">sem descrição</span>

### F19KEY

## Outras teclas

### ACCENTGRAVEKEY

<span class="ae-badge pendente">sem descrição</span>

### BACKSLASHKEY

<span class="ae-badge pendente">sem descrição</span>

### BACKSPACEKEY

<span class="ae-badge pendente">sem descrição</span>

### COMMAKEY

<span class="ae-badge pendente">sem descrição</span>

### DELKEY

<span class="ae-badge pendente">sem descrição</span>

### ENDKEY

<span class="ae-badge pendente">sem descrição</span>

### EQUALKEY

<span class="ae-badge pendente">sem descrição</span>

### ESCKEY

<span class="ae-badge pendente">sem descrição</span>

### HOMEKEY

<span class="ae-badge pendente">sem descrição</span>

### INSERTKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTBRACKETKEY

<span class="ae-badge pendente">sem descrição</span>

### LINEFEEDKEY

<span class="ae-badge pendente">sem descrição</span>

### MINUSKEY

<span class="ae-badge pendente">sem descrição</span>

### PAGEDOWNKEY

<span class="ae-badge pendente">sem descrição</span>

### PAGEUPKEY

<span class="ae-badge pendente">sem descrição</span>

### PAUSEKEY

<span class="ae-badge pendente">sem descrição</span>

### PERIODKEY

<span class="ae-badge pendente">sem descrição</span>

### QUOTEKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTBRACKETKEY

<span class="ae-badge pendente">sem descrição</span>

### RETKEY (Deprecated: use bge.events.ENTERKEY)

### ENTERKEY

<span class="ae-badge pendente">sem descrição</span>

### SEMICOLONKEY

<span class="ae-badge pendente">sem descrição</span>

### SLASHKEY

<span class="ae-badge pendente">sem descrição</span>

### SPACEKEY

<span class="ae-badge pendente">sem descrição</span>

### TABKEY

<span class="ae-badge pendente">sem descrição</span>

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### JOYSTICKA

 <small>constante</small>

Botão A do controle.

### JOYSTICKB

 <small>constante</small>

Botão B do controle.

### JOYSTICKBACK

 <small>constante</small>

Botão Back/Select do controle.

### JOYSTICKGUIDE

 <small>constante</small>

Botão Guide (botão central) do controle.

### JOYSTICKLEFTSHOUDER

 <small>constante</small>

Botão ombro esquerdo (LB) do controle.

### JOYSTICKLEFTSTICK

 <small>constante</small>

Botão clique do analógico esquerdo do controle.

### JOYSTICKPADDOWN

 <small>constante</small>

Botão direcional para baixo do controle.

### JOYSTICKPADLEFT

 <small>constante</small>

Botão direcional para a esquerda do controle.

### JOYSTICKPADRIGHT

 <small>constante</small>

Botão direcional para a direita do controle.

### JOYSTICKPADUP

 <small>constante</small>

Botão direcional para cima do controle.

### JOYSTICKRIGHTSHOUDER

 <small>constante</small>

Botão ombro direito (RB) do controle.

### JOYSTICKRIGHTSTICK

 <small>constante</small>

Botão clique do analógico direito do controle.

### JOYSTICKX

 <small>constante</small>

Botão X do controle.

### JOYSTICKY

 <small>constante</small>

Botão Y do controle.

### OSKEY

 <small>constante</small>

Tecla do sistema (Windows/Command).

