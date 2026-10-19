---
title: Мультиплеер
description: Создайте комнату и подключитесь к ней через готовое меню, реплицируйте объекты и создавайте игрока для каждого участника.
---

:::note
Код тот же, что проверен на португальской странице, поэтому имена вроде `cliente` (клиент) и `jogador` (игрок) на португальском.
:::

Мультиплеер Anastacio построен по схеме сервер–клиенты: тот, кто создаёт комнату (**хост**), ведёт симуляцию, а остальные игроки получают её состояние. Работает в локальной сети, по IP и, с дополнением Steam, через Steam.

Модуль — [`Range.network`](../../api/modulos/network/).

## 1. Готовое меню комнат

Прикрепите компонент `anastacio_network.component.AnastacioNetworkComponent` к объекту, который всё время остаётся в сцене (камера или Empty).

Он показывает окно с кнопками **Create room**, **Find rooms** (локальная сеть), **Join by IP**, списком игроков, отметкой «готов» и чатом. Когда все готовы, хост нажимает **Start**.

Параметры компонента:

- **default_port**: порт комнаты (по умолчанию 7777);
- **max_players**: сколько человек помещается;
- **game_id**: идентифицирует вашу игру, чтобы комнаты другой игры не появлялись в поиске.

<!-- PRINT: component's menu open, with the room list -->

## 2. Репликация объекта

Выберите объект и откройте **Properties > Physics**, панель **Network**:

1. Включите **Replicate**.
2. Выберите, что синхронизировать: позицию (**Sync Transform**), скорость, вращение.
3. Чтобы передавать и игровое свойство (здоровье, очки), включите кнопку **Rep** рядом с ним в списке свойств.

Реплицируемые объекты принадлежат хосту: он их двигает, остальные видят.

<!-- PRINT: Network panel with Replicate on -->

## 3. Один игрок на человека

Оставьте объект `Jogador` с включённым **Replicate** на **неактивном слое**. Хост создаёт копию, когда кто-то подключается:

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

`on_player_join` и `on_player_leave` вызываются только на хосте. `owner=cliente` указывает, какому клиенту принадлежит эта марионетка.

## 4. Отправка ввода каждого игрока

Каждый игрок отправляет свой ввод, а хост применяет его к своей марионетке. Ввод — это `bytes` длиной до 57 байт:

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

Этот компонент стоит на неподвижном объекте сцены (его выполняет каждый игрок). На хосте тот, кто двигает марионеток, читает ввод каждого владельца:

```python
    # внутри класса Partida
    def update(self):
        for cliente, jogador in self.jogadores.items():
            dados = network.input(cliente)
            if dados:
                frente, lado = struct.unpack("bb", dados[:2])
                jogador.applyMovement((lado * 0.1, frente * 0.1, 0.0), True)
```

(не забудьте `import struct` в начале файла Partida)

## Тестирование на одном компьютере

Откройте игру дважды. В одной нажмите **Create room**, в другой — **Join by IP** с адресом `127.0.0.1`.

`network.set_simulation(120, 20, 2)` имитирует задержку 120 мс, джиттер 20 мс и потерю 2% пакетов, чтобы увидеть поведение игры при плохом соединении.
