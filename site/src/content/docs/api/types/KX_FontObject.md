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

### atlas

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nome do texto que guarda o Bitmap Atlas usado para desenhar, `""` para o atlas do próprio texto ou `None` para nenhum atlas.

### characterCount

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### font

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nome da fonte do texto (a fonte que aparece nas propriedades do Text), ou `None`. Trocar redesenha o texto na hora; nome que não existe no arquivo gera `ValueError`.

### lines

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### page

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### pageCount

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### shadowColor

 <small>atributo</small>

Cor `[r, g, b, a]` da sombra do texto.

### shadowOffset

 <small>atributo</small>

Deslocamento `[x, y]` da sombra do texto.

### textBox

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### translationKey

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Chave da tabela de idiomas (`locale/translations.csv`). Com chave, o texto mostra a tradução do idioma atual de [`Range.locale`](../../../guias/idiomas/) e troca sozinho quando o idioma muda. `""` desliga.

### useLanguageFont

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Quando `True`, o texto usa a fonte e o atlas definidos para o idioma atual no `locale/locale.json` (útil para russo, japonês etc.).

### useShadows

 <small>atributo</small>

Liga a sombra do texto.

### visibleCharacters

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

