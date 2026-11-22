# KX_FontObject

Base class: [`KX_GameObject`](KX_GameObject.md)

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

```python

# Show the score stored in a game property.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Score: %d" % font["score"]
```

```python

# Center the text on the X axis, using its current width.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Game Over"
font.localPosition.x = -font.dimensions.x / 2
```

```python

# Reveal the text one letter at a time. Run it every frame (Always sensor with True Pulse).
import Range

font = Range.logic.getCurrentController().owner

if font.visibleCharacters < font.characterCount:
    font.visibleCharacters += 1
```

```python

# Add a dark shadow behind the text.
import Range

font = Range.logic.getCurrentController().owner
font.useShadows = True
font.shadowColor = [0.0, 0.0, 0.0, 0.8]
font.shadowOffset = [0.02, -0.02]
```

## text

The text displayed by this Font object.

**Type:** string

### resolution

The resolution of the font police.

> **Caution:**
High resolution can use a lot of memory and may crash.

**Type:** float (0.1 to 50.0)

### size

The size (scale factor) of the font object, scaled from font object origin (affects text resolution).

> **Caution:**
High size can use a lot of memory and may crash.

**Type:** float (0.0001 to 40.0)

### dimensions

The size (width and height) of the current text in Blender Units.

**Type:** `mathutils.Vector`

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### atlas

*(new in Anastacio)* `attribute`

Name of the text data holding the Bitmap Atlas used for drawing, `""` for the text's own atlas, or `None` for no atlas.

### characterCount

*(new in Anastacio)* `attribute · read-only`

Total number of characters in the text. Read-only.

### font

*(new in Anastacio)* `attribute`

Name of the text's font (as shown in the Text properties), or `None`. Changing it redraws the text immediately; an unknown name raises `ValueError`.

### lines

*(new in Anastacio)* `attribute · read-only`

List of the text lines after wrapping. Read-only.

### page

*(new in Anastacio)* `attribute`

Current page of the text box, from 0. Out-of-range values are clamped to the last valid page.

### pageCount

*(new in Anastacio)* `attribute · read-only`

Number of pages in the text box. Read-only.

### shadowColor

 `attribute`

Text shadow color `[r, g, b, a]`.

### shadowOffset

 `attribute`

Text shadow offset `[x, y]`.

### textBox

*(new in Anastacio)* `attribute`

Size `(width, height)` of the text box. The text wraps and splits into pages to fit it; `(0, 0)` turns it off.

### translationKey

*(new in Anastacio)* `attribute`

Key in the language table (`locale/translations.csv`). With a key, the text shows the translation for the current `Range.locale` language and updates by itself when the language changes. `""` turns it off.

### useLanguageFont

*(new in Anastacio)* `attribute`

When `True`, the text uses the font and atlas set for the current language in `locale/locale.json` (useful for Russian, Japanese, etc.).

### useShadows

 `attribute`

Turns on the text shadow.

### visibleCharacters

*(new in Anastacio)* `attribute`

How many characters are shown, for the typewriter effect. `-1` shows everything.
