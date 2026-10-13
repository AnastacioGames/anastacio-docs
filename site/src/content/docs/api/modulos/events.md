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

Botão esquerdo do mouse.

### MIDDLEMOUSE

Botão do meio do mouse (clique na rodinha).

### RIGHTMOUSE

Botão direito do mouse.

### WHEELUPMOUSE

Rodinha do mouse girando para cima.

### WHEELDOWNMOUSE

Rodinha do mouse girando para baixo.

### LEFTTHUMBMOUSE

Botão lateral de trás do mouse (voltar).

### RIGHTTHUMBMOUSE

Botão lateral da frente do mouse (avançar).

### BUTTON6MOUSE

Botão extra 6 do mouse.

### BUTTON7MOUSE

Botão extra 7 do mouse.

### MOUSEX

Movimento horizontal do mouse.

### MOUSEY

## Teclas do teclado

## Letras

### AKEY

Tecla A.

### BKEY

Tecla B.

### CKEY

Tecla C.

### DKEY

Tecla D.

### EKEY

Tecla E.

### FKEY

Tecla F.

### GKEY

Tecla G.

### HKEY

Tecla H.

### IKEY

Tecla I.

### JKEY

Tecla J.

### KKEY

Tecla K.

### LKEY

Tecla L.

### MKEY

Tecla M.

### NKEY

Tecla N.

### OKEY

Tecla O.

### PKEY

Tecla P.

### QKEY

Tecla Q.

### RKEY

Tecla R.

### SKEY

Tecla S.

### TKEY

Tecla T.

### UKEY

Tecla U.

### VKEY

Tecla V.

### WKEY

Tecla W.

### XKEY

Tecla X.

### YKEY

Tecla Y.

### ZKEY

## Números

### ZEROKEY

Tecla 0 da fileira de números (não a do teclado numérico).

### ONEKEY

Tecla 1 da fileira de números (não a do teclado numérico).

### TWOKEY

Tecla 2 da fileira de números (não a do teclado numérico).

### THREEKEY

Tecla 3 da fileira de números (não a do teclado numérico).

### FOURKEY

Tecla 4 da fileira de números (não a do teclado numérico).

### FIVEKEY

Tecla 5 da fileira de números (não a do teclado numérico).

### SIXKEY

Tecla 6 da fileira de números (não a do teclado numérico).

### SEVENKEY

Tecla 7 da fileira de números (não a do teclado numérico).

### EIGHTKEY

Tecla 8 da fileira de números (não a do teclado numérico).

### NINEKEY

## Teclas modificadoras

### CAPSLOCKKEY

Tecla Caps Lock.

### LEFTCTRLKEY

Tecla Ctrl da esquerda.

### LEFTALTKEY

Tecla Alt da esquerda.

### RIGHTALTKEY

Tecla Alt da direita (AltGr).

### RIGHTCTRLKEY

Tecla Ctrl da direita.

### RIGHTSHIFTKEY

Tecla Shift da direita.

### LEFTSHIFTKEY

## Setas

### LEFTARROWKEY

Seta para a esquerda.

### DOWNARROWKEY

Seta para baixo.

### RIGHTARROWKEY

Seta para a direita.

### UPARROWKEY

## Teclado numérico

### PAD0

Tecla 0 do teclado numérico.

### PAD1

Tecla 1 do teclado numérico.

### PAD2

Tecla 2 do teclado numérico.

### PAD3

Tecla 3 do teclado numérico.

### PAD4

Tecla 4 do teclado numérico.

### PAD5

Tecla 5 do teclado numérico.

### PAD6

Tecla 6 do teclado numérico.

### PAD7

Tecla 7 do teclado numérico.

### PAD8

Tecla 8 do teclado numérico.

### PAD9

Tecla 9 do teclado numérico.

### PADPERIOD

Tecla ponto do teclado numérico.

### PADSLASHKEY

Tecla / do teclado numérico.

### PADASTERKEY

Tecla * do teclado numérico.

### PADMINUS

Tecla - do teclado numérico.

### PADENTER

Tecla Enter do teclado numérico.

### PADPLUSKEY

## Teclas de função

### F1KEY

Tecla F1.

### F2KEY

Tecla F2.

### F3KEY

Tecla F3.

### F4KEY

Tecla F4.

### F5KEY

Tecla F5.

### F6KEY

Tecla F6.

### F7KEY

Tecla F7.

### F8KEY

Tecla F8.

### F9KEY

Tecla F9.

### F10KEY

Tecla F10.

### F11KEY

Tecla F11.

### F12KEY

Tecla F12.

### F13KEY

Tecla F13.

### F14KEY

Tecla F14.

### F15KEY

Tecla F15.

### F16KEY

Tecla F16.

### F17KEY

Tecla F17.

### F18KEY

Tecla F18.

### F19KEY

## Outras teclas

### ACCENTGRAVEKEY

Tecla acento grave (`).

### BACKSLASHKEY

Tecla barra invertida (\).

### BACKSPACEKEY

Tecla Backspace.

### COMMAKEY

Tecla vírgula (,).

### DELKEY

Tecla Delete.

### ENDKEY

Tecla End.

### EQUALKEY

Tecla igual (=).

### ESCKEY

Tecla Esc.

### HOMEKEY

Tecla Home.

### INSERTKEY

Tecla Insert.

### LEFTBRACKETKEY

Tecla colchete esquerdo ([).

### LINEFEEDKEY

Tecla Line Feed (rara em teclados atuais).

### MINUSKEY

Tecla menos (-).

### PAGEDOWNKEY

Tecla Page Down.

### PAGEUPKEY

Tecla Page Up.

### PAUSEKEY

Tecla Pause.

### PERIODKEY

Tecla ponto (.).

### QUOTEKEY

Tecla aspas (').

### RIGHTBRACKETKEY

Tecla colchete direito (]).

### RETKEY (Deprecated: use bge.events.ENTERKEY)

### ENTERKEY

Tecla Enter.

### SEMICOLONKEY

Tecla ponto e vírgula (;).

### SLASHKEY

Tecla barra (/).

### SPACEKEY

Barra de espaço.

### TABKEY

Tecla Tab.

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

