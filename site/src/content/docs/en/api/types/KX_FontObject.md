---
title: "KX_FontObject"
description: "Range.types.KX_FontObject class reference"
---

Base class: [`KX_GameObject`](../kx_gameobject/)



A Font object.

```python

# Display a message about the exit key using a Font object.
import Range

co = Range.logic.getCurrentController()
font = co.owner

exit_key = Range.events.EventToString(Range.logic.getExitKey())

if exit_key.endswith("KEY"):
    exit_key = exit_key[:-3]

font.text = "Press key '%s' to quit the game." % exit_key
```

### text

The text displayed by this Font object.

**Type:** string

### resolution

The resolution of the font police.

:::caution
High resolution can use a lot of memory and may crash.
:::

**Type:** float (0.1 to 50.0)

### size

The size (scale factor) of the font object, scaled from font object origin (affects text resolution).

:::caution
High size can use a lot of memory and may crash.
:::

**Type:** float (0.0001 to 40.0)

### dimensions

The size (width and height) of the current text in Blender Units.

**Type:** `mathutils.Vector`

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### atlas

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Name of the text data holding the Bitmap Atlas used for drawing, `""` for the text's own atlas, or `None` for no atlas.

### characterCount

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

### font

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Name of the text's font (as shown in the Text properties), or `None`. Changing it redraws the text immediately; an unknown name raises `ValueError`.

### lines

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

### page

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

### pageCount

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

### shadowColor

 <small>attribute</small>

Text shadow color `[r, g, b, a]`.

### shadowOffset

 <small>attribute</small>

Text shadow offset `[x, y]`.

### textBox

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

### translationKey

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Key in the language table (`locale/translations.csv`). With a key, the text shows the translation for the current [`Range.locale`](../../../guias/idiomas/) language and updates by itself when the language changes. `""` turns it off.

### useLanguageFont

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

When `True`, the text uses the font and atlas set for the current language in `locale/locale.json` (useful for Russian, Japanese, etc.).

### useShadows

 <small>attribute</small>

Turns on the text shadow.

### visibleCharacters

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

