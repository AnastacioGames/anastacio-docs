# KX_FontObject

Classe base: [`KX_GameObject`](KX_GameObject.md)

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

```python

# Mostra a pontuação guardada em uma propriedade de jogo.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Score: %d" % font["score"]
```

```python

# Centraliza o texto no eixo X, usando a largura atual dele.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Game Over"
font.localPosition.x = -font.dimensions.x / 2
```

```python

# Revela o texto letra por letra. Rode a cada frame (sensor Always com True Pulse).
import Range

font = Range.logic.getCurrentController().owner

if font.visibleCharacters < font.characterCount:
    font.visibleCharacters += 1
```

```python

# Coloca uma sombra escura atrás do texto.
import Range

font = Range.logic.getCurrentController().owner
font.useShadows = True
font.shadowColor = [0.0, 0.0, 0.0, 0.8]
font.shadowOffset = [0.02, -0.02]
```

## text

O texto mostrado por este objeto de fonte.

**Tipo:** string

### resolution

A resolução da fonte.

> **Caution:**
Resoluções altas podem usar muita memória e travar.

**Tipo:** float (0.1 to 50.0)

### size

O tamanho (fator de escala) do objeto de fonte, a partir da origem dele (afeta a resolução do texto).

> **Caution:**
Tamanhos grandes podem usar muita memória e travar.

**Tipo:** float (0.0001 to 40.0)

### dimensions

O tamanho (largura e altura) do texto atual, em unidades do Blender.

**Tipo:** `mathutils.Vector`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### atlas

*(novo na Anastacio)* `atributo`

Nome do texto que guarda o Bitmap Atlas usado para desenhar, `""` para o atlas do próprio texto ou `None` para nenhum atlas.

### characterCount

*(novo na Anastacio)* `atributo · só leitura`

Número total de caracteres do texto. Só leitura.

### font

*(novo na Anastacio)* `atributo`

Nome da fonte do texto (a fonte que aparece nas propriedades do Text), ou `None`. Trocar redesenha o texto na hora; nome que não existe no arquivo gera `ValueError`.

### lines

*(novo na Anastacio)* `atributo · só leitura`

Lista com as linhas do texto depois da quebra. Só leitura.

### page

*(novo na Anastacio)* `atributo`

Página atual da caixa de texto, a partir de 0. Valores fora do intervalo são limitados à última página válida.

### pageCount

*(novo na Anastacio)* `atributo · só leitura`

Número de páginas da caixa de texto. Só leitura.

### shadowColor

 `atributo`

Cor `[r, g, b, a]` da sombra do texto.

### shadowOffset

 `atributo`

Deslocamento `[x, y]` da sombra do texto.

### textBox

*(novo na Anastacio)* `atributo`

Tamanho `(largura, altura)` da caixa de texto. O texto quebra as linhas e se divide em páginas para caber nela; `(0, 0)` desliga.

### translationKey

*(novo na Anastacio)* `atributo`

Chave da tabela de idiomas (`locale/translations.csv`). Com chave, o texto mostra a tradução do idioma atual de `Range.locale` e troca sozinho quando o idioma muda. `""` desliga.

### useLanguageFont

*(novo na Anastacio)* `atributo`

Quando `True`, o texto usa a fonte e o atlas definidos para o idioma atual no `locale/locale.json` (útil para russo, japonês etc.).

### useShadows

 `atributo`

Liga a sombra do texto.

### visibleCharacters

*(novo na Anastacio)* `atributo`

Quantos caracteres aparecem, para o efeito de máquina de escrever. `-1` mostra tudo.
