# Texture

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

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### close()

 `método`

Fecha o decklink dinâmico e restaura o original

### refresh()

 `método`

Atualiza o decklink a partir da fonte

### bindId

 `atributo · só leitura`

Id OpenGL da textura.

### mipmap

 `atributo`

Usa mipmap na textura (`True`/`False`).

### source

 `atributo`

Fonte da imagem (vídeo, câmera, imagem...) desenhada na textura.
