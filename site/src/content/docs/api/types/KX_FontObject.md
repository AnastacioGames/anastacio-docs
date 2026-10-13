---
title: "KX_FontObject"
description: "Referência da classe Range.types.KX_FontObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



Um objeto de fonte.

```python

# Mostra uma mensagem sobre a tecla de saída usando um objeto de fonte.
import Range

co = Range.logic.getCurrentController()
font = co.owner

exit_key = Range.events.EventToString(Range.logic.getExitKey())

if exit_key.endswith("KEY"):
    exit_key = exit_key[:-3]

font.text = "Press key '%s' to quit the game." % exit_key
```

### text

O texto mostrado por este objeto de fonte.

**Tipo:** string

### resolution

A resolução da fonte.

:::caution
Resoluções altas podem usar muita memória e travar.
:::

**Tipo:** float (0.1 to 50.0)

### size

O tamanho (fator de escala) do objeto de fonte, a partir da origem dele (afeta a resolução do texto).

:::caution
Tamanhos grandes podem usar muita memória e travar.
:::

**Tipo:** float (0.0001 to 40.0)

### dimensions

O tamanho (largura e altura) do texto atual, em unidades do Blender.

**Tipo:** `mathutils.Vector`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### shadowColor

 <small>atributo</small>

Cor `[r, g, b, a]` da sombra do texto.

### shadowOffset

 <small>atributo</small>

Deslocamento `[x, y]` da sombra do texto.

### useShadows

 <small>atributo</small>

Liga a sombra do texto.

