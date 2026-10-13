---
title: "Range.imgui"
description: "Referência do módulo Range.imgui"
---

Módulo `Range.imgui` da Anastacio Engine. Também acessível como `bge.imgui`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### begin(name, closable=False)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(is_open, want_close)`

### begin_popup_modal(name, closable=False)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(is_open, want_close) -- only call end_popup() if is_open is True`

### button(label, width=0, height=0)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `bool`

### checkbox(label, value)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_value)`

### close_current_popup()

 <small>função</small>

Fecha o popup aberto.

### color_edit3(label, r, g, b)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, r, g, b)`

### color_edit4(label, r, g, b, a)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, r, g, b, a)`

### combo(label, current_item, items)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_item)`

### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 <small>função</small>

-- desenhado acima de todas as janelas, para fades

### end()

 <small>função</small>

Fecha a janela começada com `begin()`.

### end_popup()

 <small>função</small>

Fecha o bloco de um popup.

### get_cursor_pos()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(x, y) -- position relative to the current window`

### get_cursor_screen_pos()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(x, y)`

### get_display_size()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(width, height)`

### get_io_want_capture_keyboard()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `bool`

### get_io_want_capture_mouse()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `bool`

### image(texture_id, w, h)

 <small>função</small>

-- texture_id é um bind code OpenGL puro

### input_text(label, value, max_length=256)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_value)`

### invisible_button(label, width, height)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `bool`

### listbox(label, current_item, items, height_items=-1)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_item)`

### load_default_font(size)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

**Retorna:** `font_id or None -- engine font with icons; None until built next frame`

### load_font(path, size)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `font_id -- call once; the font is built before the next frame`

### open_popup(name)

 <small>função</small>

Abre o popup com esse nome.

### pop_font()

 <small>função</small>

Volta à fonte anterior a `push_font()`.

### pop_item_width()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Volta à largura anterior a `push_item_width()`.

### pop_style_color(count=1)

 <small>função</small>

Desfaz as últimas `count` cores de `push_style_color()`.

### pop_style_var(count=1)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Desfaz os últimos `count` estilos de `push_style_var()`.

### push_font(font_id)

 <small>função</small>

Usa outra fonte até `pop_font()`.

### push_item_width(width)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-- >0 pixels, <0 alinhado à direita da borda da janela (-1 = largura total)

### push_style_color(idx, r, g, b, a)

 <small>função</small>

-- idx é uma das constantes imgui.COL_*

### push_style_var(idx, value)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

ou push_style_var(idx, x, y) -- idx é uma das imgui.STYLE_*

### radio_button(label, active)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `pressed -- caller owns the group's selected index`

### same_line()

 <small>função</small>

Coloca o próximo item na mesma linha do anterior.

### separator()

 <small>função</small>

Desenha uma linha separadora.

### set_cursor_pos(x, y)

 <small>função</small>

-- posição relativa à janela atual

### set_game_ui_open(open)

 <small>função</small>

-- liga/desliga a entrada + libera o mouse para a UI de jogo desenhada em Python

### set_next_item_width(width)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-- mesma convenção de push_item_width, só para o próximo widget

### set_next_window_pos(x, y, cond=COND_ALWAYS)

 <small>função</small>

Posição da próxima janela, em pixels.

### set_next_window_size(w, h, cond=COND_ALWAYS)

 <small>função</small>

Tamanho da próxima janela, em pixels.

### slider_float(label, value, min, max)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_value)`

### slider_int(label, value, min, max)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_value)`

### text(text)

 <small>função</small>

Mostra um texto.

