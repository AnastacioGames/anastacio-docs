---
title: "KX_InputSystem"
description: "Referência da classe Range.types.KX_InputSystem"
---

:::tip[Veja também]
[`KX_InputTable`](../../types/kx_inputtable/), [`KX_PythonKeyboard`](../../types/kx_pythonkeyboard/), [`KX_PythonJoystick`](../../types/kx_pythonjoystick/)
:::

Classe `Range.types.KX_InputSystem`.

```python
# Lista os mapas e as ações carregados.
import Range

for mapName, tables in Range.logic.inputSystem.inputMaps.items():
    print(mapName, list(tables))
```

```python
# Salva uma nova sensibilidade escolhida no menu de opções. Argumentos: mapa, ação, binding, valor.
import Range

system = Range.logic.inputSystem

if system.changeSensitivity("Player", "Jump", "keyboard", 0.5):
    system.reloadInputMaps()
```

```python
# Troca a tecla de uma ação. O mapa é o arquivo KeyMapping/Player.json, ao lado do jogo.
import Range

system = Range.logic.inputSystem

if system.changeKeyMap("Player", "Jump", "keyboard", "BUTTON", Range.events.SPACEKEY):
    system.reloadInputMaps()
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### changeJoystickIndex(inputMap, inputTable, name, value)

 <small>método</small>

Troca qual controle (índice do joystick) uma ação usa.

### changeKeyMap(inputMap, inputTable, name, keyType, value)

 <small>método</small>

Troca a tecla ou botão ligado a uma ação. Use para menus de "redefinir controles".

### changeSensitivity(inputMap, inputTable, name, value)

 <small>método</small>

Troca a sensibilidade de uma ação (ex.: do mouse ou do analógico).

### reloadInputMaps()

 <small>método</small>

Recarrega os mapas de entrada do arquivo. É lento; evite chamar várias vezes.

### inputMaps

 <small>atributo · só leitura</small>

Dicionário `{mapa: {tabela: KX_InputTable}}` com todos os mapas de entrada carregados.

