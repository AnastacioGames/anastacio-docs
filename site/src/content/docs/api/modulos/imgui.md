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

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

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

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- drawn above every window, for fades

### end()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### end_popup()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

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

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- texture_id is a raw OpenGL bind code

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

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### pop_font()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### pop_item_width()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### pop_style_color(count=1)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### pop_style_var(count=1)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### push_font(font_id)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### push_item_width(width)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-- >0 pixels, <0 right-aligned to the window edge (-1 = full width)

### push_style_color(idx, r, g, b, a)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- idx is one of the imgui.COL_* constants

### push_style_var(idx, value)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

or push_style_var(idx, x, y) -- idx is one of imgui.STYLE_*

### radio_button(label, active)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `pressed -- caller owns the group's selected index`

### same_line()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### separator()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### set_cursor_pos(x, y)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- position relative to the current window

### set_game_ui_open(open)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- enable/disable input + free mouse for Python-drawn game UI

### set_next_item_width(width)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-- same convention as push_item_width, next widget only

### set_next_window_pos(x, y, cond=COND_ALWAYS)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### set_next_window_size(w, h, cond=COND_ALWAYS)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### slider_float(label, value, min, max)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_value)`

### slider_int(label, value, min, max)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `(changed, new_value)`

### text(text)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

