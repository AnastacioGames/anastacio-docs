---
title: "Range.network"
description: "Referência do módulo Range.network"
---

:::tip[Veja também]
[`Range.network.steam`](../../modulos/networksteam/), [`KX_GameObject`](../../types/kx_gameobject/), [`KX_Scene`](../../types/kx_scene/)
:::

Módulo `Range.network` da Anastacio Engine. Também acessível como `bge.network`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### call(name, *args, obj=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Chama uma RPC do jogo registrada com `@rpc`. Com `obj`, vira chamada do objeto (alvo `'owner'` e `owner_only` usam o dono dele). `False` quando recusada aqui (sem sessão, alvo errado...).

**Retorna:** `bool`

### change_scene(name)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: troca a cena da sessão durante a partida. Os clientes carregam a mesma cena e recebem tudo de novo quando ela termina de carregar.

### despawn(obj)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: remove um objeto replicado em todos os jogadores.

**Retorna:** `bool`

### disconnect()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Sai da sessão. No host, fecha a sala para todos.

### discover_lan()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Procura salas na rede local sem travar o jogo. Chame cerca de uma vez por segundo; cada item é um dict com os dados da sala.

**Retorna:** `list`

### host(port=0, max_players=0, room_name='', password='', dedicated=False, websocket_port=-1, transport='enet')

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Abre um servidor (sala). Valores zero ou vazios usam o painel Network da cena. `dedicated=True` não cria jogador local; `websocket_port` aceita clientes Web; `transport` é `'enet'` (LAN/IP) ou `'steam'`.

**Retorna:** `bool`

### input(client)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: input do cliente aplicado neste tick (0 = host), ou `None`.

**Retorna:** `bytes`

### input_stats(client)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: como os inputs do cliente chegaram (atrasados, repetidos, faltando...), ou `None`.

**Retorna:** `dict`

### is_owner(obj)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

`True` se este jogador é o dono do objeto.

**Retorna:** `bool`

### join(address, password='', transport='enet')

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Entra numa sala. `address` aceita `'host'`, `'host:porta'` ou `'[ipv6]:porta'`. O resultado chega por `on_connect` ou `on_reject`.

**Retorna:** `bool`

### net_id(obj)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Id de rede do objeto; 0 quando ele não é replicado.

**Retorna:** `int`

### on_chat(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn(client_id, text)`, chamada a cada mensagem do chat do lobby.

### on_connect(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn(client_id)`, chamada ao conectar (cliente) ou quando a sala abre (host, com 0).

### on_disconnect(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn(reason, detail)`, chamada ao sair da sessão. `reason` é uma constante `DISCONNECT_*` (1 a 5).

### on_lobby(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn()`, chamada quando o host volta a sessão para o lobby.

### on_player_join(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: registra `fn(client_id, name)`, chamada quando um jogador entra.

### on_player_leave(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: registra `fn(client_id)`, chamada quando um jogador sai.

### on_reject(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn(reason, detail)`, chamada quando o servidor recusa a entrada. `reason` é uma constante `REJECT_*` (1 a 6).

### on_scene(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn(scene_name)`, chamada quando a sessão trocou de cena e ela terminou de carregar (servidor e clientes).

### on_start(fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Registra `fn()`, chamada quando o host começa a partida.

### owner(obj)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Id do cliente dono do objeto, ou `None` se ele não é replicado.

**Retorna:** `int`

### predict(obj, fn)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

`fn(obj, input)` move o objeto por um tick com o input do dono (bytes): no servidor a cada tick e no cliente dono à frente do servidor (predição, corrigida pelos snapshots). Registre em todos os jogadores; `None` desliga.

**Retorna:** `bool`

### prediction_stats(obj)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só no cliente: estatísticas da predição do objeto (correções etc.), ou `None`.

**Retorna:** `dict`

### raycast_past(origin, direction, distance=100.0, client=-1, ignore=None, max_rewind_ms=400)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: raio contra as hitboxes como o cliente as via (compensação de lag, até 1 s atrás); `client=-1` usa o momento atual. Retorna `(obj, ponto, distância)` ou `None`.

**Retorna:** `tuple`

### replicate(obj, props, transform=True, velocity=False, angular_velocity=False, always_relevant=False, priority=1.0, quantize=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Faz o mesmo que a caixa **Replicate**: sincroniza o objeto pela rede. Chame antes de `host()`/`join()`, na mesma ordem em todos os jogadores. `props` lista as propriedades de jogo enviadas (pode ser vazia); `quantize={nome: (min, max, bits)}` manda propriedades Float com menos bits. Retorna o id de rede.

**Retorna:** `int`

### return_to_lobby()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o host: encerra a partida, zera o "pronto" dos jogadores e avisa os clientes (`on_lobby`). Trocar de cena fica por conta do jogo.

**Retorna:** `bool`

### send_chat(text)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Envia uma mensagem no chat do lobby, até 200 bytes em UTF-8. Recebida por `on_chat`.

**Retorna:** `bool`

### set_client_view(client, center=None, radius=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: centro (objeto ou posição) e raio de relevância de um cliente; objetos fora do raio não são enviados. Raio 0 envia tudo. Sem centro, usa o primeiro objeto do cliente. Tudo `None` volta ao **Relevance Radius** da cena.

### set_hitbox(obj, radius, half_height=0.0)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: esfera (ou cápsula no Z local) guardada por 1 s de histórico para `raycast_past()`. Raio 0 remove.

**Retorna:** `bool`

### set_input(data)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Input do jogador local (bytes, até 57), enviado a cada tick até mudar, junto com o instante em que os objetos remotos estavam sendo desenhados (compensação de lag). Chame todo frame.

### set_owner(obj, client)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: passa o objeto para outro dono (id do cliente; 0 = host).

**Retorna:** `bool`

### set_ready(ready)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

No lobby, marca este jogador como pronto (`True`) ou não (`False`).

### set_simulation(latency_ms, jitter_ms, loss_percent)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Simula uma rede ruim (atraso, variação e perda de pacotes) no próximo `host()`/`join()`. Útil para testar.

### spawn(prototype, owner=0, position=None, orientation=None)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o servidor: cria uma cópia do objeto inativo `prototype` (nome) e a replica para todos. `owner` é o id do cliente dono (0 = host).

**Retorna:** `KX_GameObject`

### start_game()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Só o host: começa a partida. Retorna `False` se algum jogador não está pronto. Os clientes recebem `on_start`.

**Retorna:** `bool`

### view_time(client=0)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

No cliente: o instante `(tick, alpha)` em que os objetos remotos são desenhados. No servidor: o instante que o cliente mandou com o último input. `None` sem sessão.

**Retorna:** `tuple`

