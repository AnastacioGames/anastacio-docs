---
title: "Range.network.steam"
description: "Referência do módulo Range.network.steam"
---

:::tip[Veja também]
[`Range.network`](../../modulos/network/)
:::

Módulo `Range.network.steam` da Anastacio Engine. Também acessível como `bge.network.steam`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### achievement(name, unlock=False)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Consulta uma conquista (achievement) da Steam pelo nome da API; com `unlock=True`, desbloqueia.

**Retorna:** `bool`

### connection_routes()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Rota de cada jogador conectado: dicts com `peer`, `steam_id` e `route` (`'direct'`, `'relay'` ou `'unknown'`). Vazia sem jogadores.

**Retorna:** `list`

### force_relay(force)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Com `True`, desliga a conexão direta e força os servidores de relay da Steam. Chame depois de `initialize()` e antes de abrir a sessão.

### initialize(absolute_dll_path, app_id)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Carrega o complemento opcional `AnastacioSteam.dll` (caminho absoluto) com o AppID do jogo (1 a 4294967295). Só Windows 64 bits, com o jogo rodando; não existe na Web. O componente de multiplayer faz isso sozinho quando **enable_steam** está ligado.

### language()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Idioma do jogo escolhido na Steam (ex.: `'brazilian'`); vazio sem Steam.

**Retorna:** `str`

### poll_events()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Retira os eventos pendentes de lobby e convites. Cada item é um dict com `type`, `lobby_id`, `host_id`, `port`, `members`, `capacity`, `name` e `detail`.

**Retorna:** `list`

### shutdown()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Descarrega a Steam. Desconecte a sessão antes. Fechar o jogo também descarrega.

### status()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

`{'loaded': bool, 'ready': bool, 'steam_id': int}`: se a DLL carregou, se a Steam está pronta e o SteamID do jogador.

**Retorna:** `dict`

