---
title: "Range.network"
description: "Referência do módulo Range.network"
---

Módulo `Range.network` da Anastacio Engine. Também acessível como `bge.network`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### call(name, *args, obj=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Calls a game RPC registered with @rpc; obj makes it an object call (target 'owner' and owner_only use its owner). False when refused here (no session, wrong target...).

**Retorna:** `bool`

### change_scene()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### despawn()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### disconnect()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### discover_lan()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### host(port=0, max_players=0, room_name='', password='', dedicated=False, websocket_port=-1, transport='enet')

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Opens a server. Zero or empty values use the Network panel of the scene.

**Retorna:** `bool`

### input()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### input_stats()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### is_owner()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### join(address, password='', transport='enet')

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Joins 'host', 'host:port' or '[v6]:port'.

**Retorna:** `bool`

### net_id()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_chat()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_connect()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_disconnect()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_lobby()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_player_join()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_player_leave()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_reject()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_scene()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### on_start()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### owner()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### predict()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### prediction_stats()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### raycast_past(origin, direction, distance=100.0, client=-1, ignore=None, max_rewind_ms=400)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-> (obj, point, distance) or None Server: ray against the hitboxes as client saw them (lag compensation, 1 s of history); -1 = now.

### replicate(obj, props=()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

, transform=True, velocity=False, angular_velocity=False, always_relevant=False, priority=1.0, quantize=None) -> int Same as the Replicate checkbox; run it before host()/join(), in the same order on every peer. quantize={name: (min, max, bits)} sends Float properties in fewer bits.

### return_to_lobby()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### send_chat()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### set_client_view(client, center=None, radius=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Server only: relevance center (object or position) and radius of a client; radius 0 sends everything. No center: first object the client owns. All None: back to the scene's Relevance Radius.

### set_hitbox()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### set_input()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### set_owner()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### set_ready()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### set_simulation()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### spawn(prototype, owner=0, position=None, orientation=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Server only: adds a copy of the inactive object 'prototype' and replicates it.

**Retorna:** `object`

### start_game()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### view_time()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

