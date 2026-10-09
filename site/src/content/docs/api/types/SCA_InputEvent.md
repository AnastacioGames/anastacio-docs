---
title: "SCA_InputEvent"
description: "Referência da classe Range.types.SCA_InputEvent"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Eventos de uma entrada de teclado ou mouse.

### status

Lista dos estados da entrada desde o último frame. Pode conter `Range.logic.KX_INPUT_NONE` e `Range.logic.KX_INPUT_ACTIVE`. A lista sempre tem um valor. O primeiro valor da lista é o último valor da lista no frame anterior (somente leitura).

**Tipo:** list of integer.

### queue

Lista dos eventos da entrada desde o último frame. Pode conter `Range.logic.KX_INPUT_JUST_ACTIVATED` e `Range.logic.KX_INPUT_JUST_RELEASED`. A lista pode estar vazia (somente leitura).

**Tipo:** list of integer.

### values

Lista dos valores da entrada desde o último frame. No teclado contém 1 ou 0; no mouse, a coordenada do mouse ou o movimento da roda. A lista sempre tem um valor; só nas entradas de teclado o tamanho dela é o de `queue` + 1. O primeiro valor da lista é o último valor da lista no frame anterior (somente leitura).

Exemplo para pegar as coordenadas do mouse sem normalizar:

```python

import Range

x = Range.logic.mouse.inputs[Range.events.MOUSEX].values[-1]
y = Range.logic.mouse.inputs[Range.events.MOUSEY].values[-1]

print("Mouse non-normalized position: x: {0}, y: {1}".format(x, y))
```

**Tipo:** list of integer.

### inactive

True se a entrada estava inativa desde o último frame.

**Tipo:** boolean

### active

True se a entrada estava ativa desde o último frame.

**Tipo:** boolean

### activated

True se a entrada foi ativada desde o último frame.

**Tipo:** boolean

### released

True se a entrada foi solta desde o último frame.

**Tipo:** boolean

### type

O tipo da entrada. Uma `destas constantes`

**Tipo:** integer

