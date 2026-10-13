---
title: "KX_InputSystem"
description: "Referência da classe Range.types.KX_InputSystem"
---

:::tip[Veja também]
[`KX_InputTable`](../../types/kx_inputtable/), [`KX_PythonKeyboard`](../../types/kx_pythonkeyboard/), [`KX_PythonJoystick`](../../types/kx_pythonjoystick/)
:::

Classe `Range.types.KX_InputSystem`.

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

