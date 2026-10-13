---
title: Multiplayer
description: Create and join a room with the ready-made menu, replicate objects and spawn a player for each person.
---

:::note
The code is the same one tested on the Portuguese page, so names such as `cliente` (client) and `jogador` (player) are in Portuguese.
:::

Anastacio's multiplayer is server and clients: whoever creates the room (the **host**) runs the simulation, and the other players receive its state. It works over the local network, by IP and, with the Steam add-on, over Steam.

The module is [`Range.network`](../../api/modulos/network/).

## 1. Ready-made room menu

Attach the `anastacio_network.component.AnastacioNetworkComponent` component to an object that stays in the scene the whole time (a camera or an Empty).

It shows a window with **Create room**, **Find rooms** (local network), **Join by IP**, a player list, "ready" and chat. The host presses **Start** once everyone is ready.

Component options:

- **default_port**: the room's port (default 7777);
- **max_players**: how many people fit;
- **game_id**: identifies your game, so another game's rooms don't show up in the search.

<!-- PRINT: component's menu open, with the room list -->

## 2. Replicate an object

Select the object and open **Properties > Physics**, the **Network** panel:

1. Turn on **Replicate**.
2. Pick what to sync: position (**Sync Transform**), velocity, rotation.
3. To also send a game property (health, score), turn on the **Rep** button next to it in the properties list.

Replicated objects belong to the host: it moves them, everyone else sees them.

<!-- PRINT: Network panel with Replicate on -->

## 3. One player per person

Leave a `Jogador` object with **Replicate** on an **inactive layer**. The host spawns a copy when someone joins:

```python
import Range
from Range import network


class Partida(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.jogadores = {}
        network.on_player_join(self.entrou)
        network.on_player_leave(self.saiu)

    def entrou(self, cliente, nome):
        jogador = network.spawn("Jogador", owner=cliente, position=(cliente * 2.0, 0.0, 1.0))
        self.jogadores[cliente] = jogador

    def saiu(self, cliente):
        jogador = self.jogadores.pop(cliente, None)
        if jogador is not None:
            network.despawn(jogador)

    def update(self):
        pass
```

`on_player_join` and `on_player_leave` are only called on the host. `owner=cliente` says which client that puppet belongs to.

## 4. Send each player's input

Each player sends its own input, and the host applies it to its puppet. The input is a `bytes` of up to 57 bytes:

```python
import struct
import Range
from Range import events, logic, network


class InputDoJogador(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        pass

    def update(self):
        t = logic.keyboard.inputs
        frente = int(t[events.WKEY].active) - int(t[events.SKEY].active)
        lado = int(t[events.DKEY].active) - int(t[events.AKEY].active)
        network.set_input(struct.pack("bb", frente, lado))
```

This component sits on a fixed scene object (every player runs it). On the host, whoever moves the puppets reads each owner's input:

```python
    # inside the Partida class
    def update(self):
        for cliente, jogador in self.jogadores.items():
            dados = network.input(cliente)
            if dados:
                frente, lado = struct.unpack("bb", dados[:2])
                jogador.applyMovement((lado * 0.1, frente * 0.1, 0.0), True)
```

(remember `import struct` at the top of the Partida file)

## Testing on the same machine

Open the game twice. In one, **Create room**; in the other, **Join by IP** with `127.0.0.1`.

`network.set_simulation(120, 20, 2)` simulates 120 ms of latency, 20 ms of jitter and 2% packet loss, to see how the game behaves on a bad connection.
