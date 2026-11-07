---
title: "Texture"
description: "Referência da classe Range.types.Texture"
---

Classe `Range.types.Texture`.

```python
# Coloca uma imagem em um material. Guarde o objeto em uma propriedade, senão ele é liberado.
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
# Devolve a textura original.
import Range

own = Range.logic.getCurrentController().owner

own["poster"].close()
del own["poster"]
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### close()

 <small>método</small>

Fecha o decklink dinâmico e restaura o original

### refresh()

 <small>método</small>

Atualiza o decklink a partir da fonte

### bindId

 <small>atributo · só leitura</small>

Id OpenGL da textura.

### mipmap

 <small>atributo</small>

Usa mipmap na textura (`True`/`False`).

### source

 <small>atributo</small>

Fonte da imagem (vídeo, câmera, imagem...) desenhada na textura.

