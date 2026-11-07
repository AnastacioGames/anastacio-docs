---
title: "Texture"
description: "Range.types.Texture class reference"
---

Class `Range.types.Texture`.

```python
# Put an image on a material. Keep the object in a property or it will be released.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.mipmap = True
tex.refresh(False)
own["poster"] = tex
```

```python
# Give the original texture back.
import Range

own = Range.logic.getCurrentController().owner

own["poster"].close()
del own["poster"]
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### close()

 <small>method</small>

Close dynamic decklink and restore original

### refresh()

 <small>method</small>

Refresh decklink from source

### bindId

 <small>attribute · read-only</small>

OpenGL id of the texture.

### mipmap

 <small>attribute</small>

Uses mipmaps on the texture (`True`/`False`).

### source

 <small>attribute</small>

Image source (video, camera, image...) drawn on the texture.

