---
title: "SCA_KeyboardSensor"
description: "Referência da classe Range.types.SCA_KeyboardSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Um sensor de teclado detecta as teclas apertadas pelo jogador.

Veja o módulo `Range.events` para os códigos de tecla.

### key

O código da tecla que este sensor procura.

**Tipo:** keycode from `Range.events` module

### hold1

O código da primeira tecla modificadora que este sensor procura.

**Tipo:** keycode from `Range.events` module

### hold2

O código da segunda tecla modificadora que este sensor procura.

**Tipo:** keycode from `Range.events` module

### toggleProperty

O nome da propriedade que indica se as teclas digitadas devem ser registradas como texto.

**Tipo:** string

### targetProperty

O nome da propriedade que recebe as teclas digitadas, quando elas são registradas como texto.

**Tipo:** string

### useAllKeys

Define se o sensor aceita todas as teclas.

**Tipo:** boolean

### inputs

Lista das teclas de entrada que foram apertadas, acabaram de ser soltas ou estão ativas neste frame (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~events~~

Lista das teclas que foram apertadas, acabaram de ser soltas ou estão ativas neste frame (somente leitura).

:::danger[Obsoleto use :data:`inputs`]

:::

**Tipo:** list [[`keycode`, `status`], ...]

### getKeyStatus(keycode)

Lê o estado de uma tecla.

- **`keycode`**: O código do botão cujo estado você quer ler; use uma `destas constantes`
  - tipo: integer

**Retorna:** O estado do botão, que pode ser uma `destas constantes`

**Tipo do retorno:** int

