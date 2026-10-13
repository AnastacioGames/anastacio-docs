---
title: "Range.network"
description: "Range.network module reference"
---

:::tip[See also]
[`Range.network.steam`](../../modulos/networksteam/), [`KX_GameObject`](../../types/kx_gameobject/), [`KX_Scene`](../../types/kx_scene/)
:::

Anastacio Engine module `Range.network`. Also available as `bge.network`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### call(name, *args, obj=None)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Calls a game RPC registered with `@rpc`. With `obj`, it becomes an object call (target `'owner'` and `owner_only` use its owner). `False` when refused locally (no session, wrong target...).

**Returns:** `bool`

### change_scene(name)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: changes the session scene during the match. Clients load the same scene and receive everything again when it finishes loading.

### despawn(obj)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: removes a replicated object on every player.

**Returns:** `bool`

### disconnect()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Leaves the session. On the host, closes the room for everyone.

### discover_lan()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Looks for rooms on the local network without stalling the game. Call about once a second; each item is a dict with the room data.

**Returns:** `list`

### host(port=0, max_players=0, room_name='', password='', dedicated=False, websocket_port=-1, transport='enet')

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Opens a server (room). Zero or empty values use the scene Network panel. `dedicated=True` creates no local player; `websocket_port` accepts Web clients; `transport` is `'enet'` (LAN/IP) or `'steam'`.

**Returns:** `bool`

### input(client)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: the client input applied this tick (0 = host), or `None`.

**Returns:** `bytes`

### input_stats(client)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: how the client inputs arrived (late, repeated, missing...), or `None`.

**Returns:** `dict`

### is_owner(obj)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

`True` if this player owns the object.

**Returns:** `bool`

### join(address, password='', transport='enet')

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Joins a room. `address` accepts `'host'`, `'host:port'` or `'[ipv6]:port'`. The result arrives through `on_connect` or `on_reject`.

**Returns:** `bool`

### net_id(obj)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Network id of the object; 0 when it is not replicated.

**Returns:** `int`

### on_chat(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn(client_id, text)`, called for each lobby chat message.

### on_connect(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn(client_id)`, called on connecting (client) or when the room opens (host, with 0).

### on_disconnect(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn(reason, detail)`, called when leaving the session. `reason` is a `DISCONNECT_*` constant (1 to 5).

### on_lobby(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn()`, called when the host takes the session back to the lobby.

### on_player_join(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: registers `fn(client_id, name)`, called when a player joins.

### on_player_leave(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: registers `fn(client_id)`, called when a player leaves.

### on_reject(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn(reason, detail)`, called when the server refuses the connection. `reason` is a `REJECT_*` constant (1 to 6).

### on_scene(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn(scene_name)`, called when the session changed scene and it finished loading (server and clients).

### on_start(fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Registers `fn()`, called when the host starts the match.

### owner(obj)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Id of the client that owns the object, or `None` if it is not replicated.

**Returns:** `int`

### predict(obj, fn)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

`fn(obj, input)` moves the object one tick with the owner's input (bytes): on the server every tick and on the owning client ahead of the server (prediction, corrected by snapshots). Register it on every player; `None` turns it off.

**Returns:** `bool`

### prediction_stats(obj)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Client only: prediction statistics for the object (corrections etc.), or `None`.

**Returns:** `dict`

### raycast_past(origin, direction, distance=100.0, client=-1, ignore=None, max_rewind_ms=400)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: ray against the hitboxes as the client saw them (lag compensation, up to 1 s back); `client=-1` uses the current moment. Returns `(obj, point, distance)` or `None`.

**Returns:** `tuple`

### replicate(obj, props, transform=True, velocity=False, angular_velocity=False, always_relevant=False, priority=1.0, quantize=None)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Same as the **Replicate** checkbox: syncs the object over the network. Call it before `host()`/`join()`, in the same order on every player. `props` lists the game properties sent (may be empty); `quantize={name: (min, max, bits)}` sends Float properties with fewer bits. Returns the network id.

**Returns:** `int`

### return_to_lobby()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Host only: ends the match, clears the players' "ready" flag and notifies clients (`on_lobby`). Changing scenes is up to the game.

**Returns:** `bool`

### send_chat(text)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Sends a lobby chat message, up to 200 bytes in UTF-8. Received by `on_chat`.

**Returns:** `bool`

### set_client_view(client, center=None, radius=None)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: relevance center (object or position) and radius of a client; objects outside the radius are not sent. Radius 0 sends everything. Without a center, uses the client's first object. All `None` goes back to the scene **Relevance Radius**.

### set_hitbox(obj, radius, half_height=0.0)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: sphere (or capsule on local Z) kept with 1 s of history for `raycast_past()`. Radius 0 removes it.

**Returns:** `bool`

### set_input(data)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Local player input (bytes, up to 57), sent every tick until it changes, together with the moment remote objects were being drawn (lag compensation). Call it every frame.

### set_owner(obj, client)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: gives the object to another owner (client id; 0 = host).

**Returns:** `bool`

### set_ready(ready)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

In the lobby, marks this player as ready (`True`) or not (`False`).

### set_simulation(latency_ms, jitter_ms, loss_percent)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Simulates a bad network (delay, jitter and packet loss) on the next `host()`/`join()`. Useful for testing.

### spawn(prototype, owner=0, position=None, orientation=None)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Server only: creates a copy of the inactive object `prototype` (name) and replicates it to everyone. `owner` is the owning client id (0 = host).

**Returns:** `KX_GameObject`

### start_game()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Host only: starts the match. Returns `False` if some player is not ready. Clients receive `on_start`.

**Returns:** `bool`

### view_time(client=0)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

On the client: the moment `(tick, alpha)` remote objects are drawn at. On the server: the moment the client sent with its last input. `None` without a session.

**Returns:** `tuple`

