---
title: "KX_PythonMouse"
description: "Referência da classe Range.types.KX_PythonMouse"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



O mouse atual.

:::caution
A normalização do mouse usa a coordenada máxima da largura e da altura, ou seja, `Range.render.getWindowWidth() - 1` ou `Range.render.getWindowHeight() - 1`.

Um script que põe o mouse no centro fica parecido com este exemplo:

```python

import Range

w, h = Range.render.getWindowWidth() - 1, Range.render.getWindowHeight() - 1
center_x, center_y = (w // 2) / w, (h // 2) / h

Range.logic.mouse.position = center_x, center_y
```

Repare no uso da divisão inteira para arredondar uma coordenada.
:::

### inputs

Dicionário com a entrada de cada evento do mouse (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### events

Dicionário com o estado de cada evento do mouse (somente leitura).

:::danger[Obsoleto use :data:`inputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### activeInputs

Dicionário com a entrada só dos eventos ativos do mouse (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### active_events

Dicionário com o estado só dos eventos ativos do mouse (somente leitura).

:::danger[Obsoleto use :data:`activeInputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### position

A posição x e y normalizada do cursor do mouse.

**Tipo:** tuple (x, y)

### visible

A visibilidade do cursor do mouse.

**Tipo:** boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### reCenter()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### deltaPosition

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

