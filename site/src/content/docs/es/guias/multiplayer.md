---
title: Multijugador
description: Crea y únete a una sala con el menú listo, replica objetos y genera un jugador para cada persona.
---

:::note
El código es el mismo probado en la página en portugués, por eso nombres como `cliente` (cliente) y `jogador` (jugador) están en portugués.
:::

El multijugador de Anastacio es servidor y clientes: quien crea la sala (el **host**) ejecuta la simulación, y los demás jugadores reciben su estado. Funciona en red local, por IP y, con el complemento de Steam, por Steam.

El módulo es [`Range.network`](../../api/modulos/network/).

## 1. Menú de salas listo

Asigna el componente `anastacio_network.component.AnastacioNetworkComponent` a un objeto que permanezca en la escena todo el tiempo (una cámara o un Empty).

Muestra una ventana con **Create room**, **Find rooms** (red local), **Join by IP**, lista de jugadores, "listo" y chat. El host presiona **Start** cuando todos están listos.

Opciones del componente:

- **default_port**: el puerto de la sala (predeterminado 7777);
- **max_players**: cuántas personas caben;
- **game_id**: identifica tu juego, para que las salas de otro juego no aparezcan en la búsqueda.

<!-- PRINT: component's menu open, with the room list -->

## 2. Replicar un objeto

Selecciona el objeto y abre **Properties > Physics**, panel **Network**:

1. Activa **Replicate**.
2. Elige qué sincronizar: posición (**Sync Transform**), velocidad, rotación.
3. Para enviar también una propiedad de juego (vida, puntaje), activa el botón **Rep** junto a ella en la lista de propiedades.

Los objetos replicados pertenecen al host: él los mueve, los demás los ven.

<!-- PRINT: Network panel with Replicate on -->

## 3. Un jugador por persona

Deja un objeto `Jogador` con **Replicate** en una **capa inactiva**. El host genera una copia cuando alguien entra:

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

`on_player_join` y `on_player_leave` solo se llaman en el host. `owner=cliente` indica a qué cliente pertenece ese títere.

## 4. Enviar la entrada de cada jugador

Cada jugador envía su propia entrada, y el host la aplica a su títere. La entrada es un `bytes` de hasta 57 bytes:

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

Este componente va en un objeto fijo de la escena (todos los jugadores lo ejecutan). En el host, quien mueve los títeres lee la entrada de cada dueño:

```python
    # dentro de la clase Partida
    def update(self):
        for cliente, jogador in self.jogadores.items():
            dados = network.input(cliente)
            if dados:
                frente, lado = struct.unpack("bb", dados[:2])
                jogador.applyMovement((lado * 0.1, frente * 0.1, 0.0), True)
```

(recuerda `import struct` al inicio del archivo de Partida)

## Probar en la misma máquina

Abre el juego dos veces. En uno, **Create room**; en el otro, **Join by IP** con `127.0.0.1`.

`network.set_simulation(120, 20, 2)` simula 120 ms de latencia, 20 ms de jitter y 2% de pérdida de paquetes, para ver cómo se comporta el juego con una mala conexión.
