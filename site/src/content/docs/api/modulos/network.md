---
title: "Range.network"
description: "Referência do módulo Range.network"
---

Módulo `Range.network` da Anastacio Engine. Também acessível como `bge.network`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### call(name, *args, obj=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Chama um RPC do jogo registrado com @rpc; obj faz dela uma chamada de objeto (o alvo 'owner' e owner_only usam o dono dele). False quando recusada aqui (sem sessão, alvo errado...).

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

Abre um servidor. Valores zero ou vazios usam o painel Network da cena.

**Retorna:** `bool`

### input()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### input_stats()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### is_owner()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### join(address, password='', transport='enet')

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Entra em 'host', 'host:port' ou '[v6]:port'.

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

-> (obj, point, distance) ou None. Servidor: raio contra as hitboxes como o cliente as viu (compensação de lag, 1 s de histórico); -1 = agora.

### replicate(obj, props=()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

, transform=True, velocity=False, angular_velocity=False, always_relevant=False, priority=1.0, quantize=None) -> int. Igual à caixa Replicate; rode antes de host()/join(), na mesma ordem em todos os peers. quantize={name: (min, max, bits)} envia propriedades Float em menos bits.

### return_to_lobby()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### send_chat()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### set_client_view(client, center=None, radius=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só no servidor: centro de relevância (objeto ou posição) e raio de um cliente; raio 0 envia tudo. Sem centro: o primeiro objeto que o cliente possui. Tudo None: volta ao Relevance Radius da cena.

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

Só no servidor: adiciona uma cópia do objeto inativo 'prototype' e a replica.

**Retorna:** `object`

### start_game()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### view_time()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

