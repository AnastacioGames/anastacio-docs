---
title: "Range.network.steam"
description: "Range.network.steam module reference"
---

:::tip[See also]
[`Range.network`](../../modulos/network/)
:::

Anastacio Engine module `Range.network.steam`. Also available as `bge.network.steam`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### achievement(name, unlock=False)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Checks a Steam achievement by its API name; with `unlock=True`, unlocks it.

**Returns:** `bool`

### connection_routes()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Route of each connected player: dicts with `peer`, `steam_id` and `route` (`'direct'`, `'relay'` or `'unknown'`). Empty without players.

**Returns:** `list`

### force_relay(force)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

With `True`, turns off direct connection and forces Steam relay servers. Call after `initialize()` and before opening the session.

### initialize(absolute_dll_path, app_id)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Loads the optional `AnastacioSteam.dll` add-on (absolute path) with the game AppID (1 to 4294967295). Windows 64-bit only, with the game running; not available on the Web. The multiplayer component does this by itself when **enable_steam** is on.

### language()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Game language chosen in Steam (e.g. `'brazilian'`); empty without Steam.

**Returns:** `str`

### poll_events()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Takes the pending lobby and invite events. Each item is a dict with `type`, `lobby_id`, `host_id`, `port`, `members`, `capacity`, `name` and `detail`.

**Returns:** `list`

### shutdown()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Unloads Steam. Disconnect the session first. Closing the game also unloads it.

### status()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

`{'loaded': bool, 'ready': bool, 'steam_id': int}`: whether the DLL loaded, whether Steam is ready, and the player SteamID.

**Returns:** `dict`

