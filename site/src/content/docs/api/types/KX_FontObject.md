---
title: "KX_FontObject"
description: "Referência da classe Range.types.KX_FontObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



A Font object.

``python

# Display a message about the exit key using a Font object.
import Range

co = Range.logic.getCurrentController()
font = co.owner

exit_key = Range.events.EventToString(Range.logic.getExitKey())

if exit_key.endswith("KEY"):
    exit_key = exit_key[:-3]

font.text = "Press key '%s' to quit the game." % exit_key
``

### text

The text displayed by this Font object.

**Tipo:** string

### resolution

The resolution of the font police.

:::caution
High resolution can use a lot of memory and may crash.
:::

**Tipo:** float (0.1 to 50.0)

### size

The size (scale factor) of the font object, scaled from font object origin (affects text resolution).

:::caution
High size can use a lot of memory and may crash.
:::

**Tipo:** float (0.0001 to 40.0)

### dimensions

The size (width and height) of the current text in Blender Units.

**Tipo:** `mathutils.Vector`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### shadowColor

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### shadowOffset

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### useShadows

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

