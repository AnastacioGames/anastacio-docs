---
title: "KX_PythonKeyboard"
description: "Referência da classe Range.types.KX_PythonKeyboard"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[Veja também]
[`Range.events`](../../modulos/events/), [`SCA_InputEvent`](../../types/sca_inputevent/), [`KX_PythonMouse`](../../types/kx_pythonmouse/)
:::



O teclado atual.

### inputs

Dicionário com a entrada de cada tecla do teclado (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~events~~

Dicionário com o estado de cada evento ou tecla do teclado (somente leitura).

:::danger[Obsoleto use :data:`inputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### activeInputs

Dicionário com a entrada só das teclas ativas (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~active_events~~

Dicionário com o estado só dos eventos ou teclas ativas (somente leitura).

:::danger[Obsoleto use :data:`activeInputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### text

O texto unicode digitado no último frame.

**Tipo:** string

### getClipboard()

Lê o texto da área de transferência.

**Tipo do retorno:** string

### setClipboard(text)

Define o texto da área de transferência.

- **`text`**: O novo texto da área de transferência
  - tipo: string

