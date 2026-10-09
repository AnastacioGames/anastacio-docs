---
title: "KX_PythonMouse"
description: "Referência da classe Range.types.KX_PythonMouse"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



The current mouse.

:::caution
Mouse normalization is using the maximum coordinate in width and height, whether `Range.render.getWindowWidth() - 1` or `Range.render.getWindowHeight() - 1`.

A script setting the mouse at center is similar to the following example:

``python

import Range

w, h = Range.render.getWindowWidth() - 1, Range.render.getWindowHeight() - 1
center_x, center_y = (w // 2) / w, (h // 2) / h

Range.logic.mouse.position = center_x, center_y
``

Note the usage of floor division to round an existing coordinate.
:::

### inputs

A dictionary containing the input of each mouse event. (read-only).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### events

a dictionary containing the status of each mouse event. (read-only).

:::danger[Obsoleto use `inputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### activeInputs

A dictionary containing the input of only the active mouse events. (read-only).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### active_events

a dictionary containing the status of only the active mouse events. (read-only).

:::danger[Obsoleto use `activeInputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### position

The normalized x and y position of the mouse cursor.

**Tipo:** tuple (x, y)

### visible

The visibility of the mouse cursor.

**Tipo:** boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### reCenter()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### deltaPosition

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

