# Range.network.steam

> **See also:**
[`Range.network`](Range.network.md)

Anastacio Engine module `Range.network.steam`. Also available as `bge.network.steam`.

```python
# Load Steam and see who is playing.
import Range
from Range.network import steam

dll = Range.logic.expandPath("//AnastacioSteam.dll")
steam.initialize(dll, 480)

info = steam.status()
if info["ready"]:
    print("Steam id:", info["steam_id"], steam.language())
```

```python
# Unlock an achievement.
from Range.network import steam

if not steam.achievement("FIRST_WIN"):
    steam.achievement("FIRST_WIN", unlock=True)
```

```python
# Handle lobby events and invites.
from Range.network import steam

for event in steam.poll_events():
    print(event["type"], event["name"], event["members"])
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### achievement(name, unlock=False)

*(new in Anastacio)* `function`

Checks a Steam achievement by its API name; with `unlock=True`, unlocks it.

**Returns:** `bool`

### connection_routes()

*(new in Anastacio)* `function`

Route of each connected player: dicts with `peer`, `steam_id` and `route` (`'direct'`, `'relay'` or `'unknown'`). Empty without players.

**Returns:** `list`

### force_relay(force)

*(new in Anastacio)* `function`

With `True`, turns off direct connection and forces Steam relay servers. Call after `initialize()` and before opening the session.

### initialize(absolute_dll_path, app_id)

*(new in Anastacio)* `function`

Loads the optional `AnastacioSteam.dll` add-on (absolute path) with the game AppID (1 to 4294967295). Windows 64-bit only, with the game running; not available on the Web. The multiplayer component does this by itself when **enable_steam** is on.

### language()

*(new in Anastacio)* `function`

Game language chosen in Steam (e.g. `'brazilian'`); empty without Steam.

**Returns:** `str`

### poll_events()

*(new in Anastacio)* `function`

Takes the pending lobby and invite events. Each item is a dict with `type`, `lobby_id`, `host_id`, `port`, `members`, `capacity`, `name` and `detail`.

**Returns:** `list`

### shutdown()

*(new in Anastacio)* `function`

Unloads Steam. Disconnect the session first. Closing the game also unloads it.

### status()

*(new in Anastacio)* `function`

`{'loaded': bool, 'ready': bool, 'steam_id': int}`: whether the DLL loaded, whether Steam is ready, and the player SteamID.

**Returns:** `dict`
