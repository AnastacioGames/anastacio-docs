---
title: Multiplayer
description: Criar e entrar numa sala com o menu pronto, sincronizar objetos e criar um jogador para cada pessoa.
draft: true
---

O multiplayer da Anastacio é servidor e clientes: quem cria a sala (o **host**) roda a simulação e os outros jogadores recebem o estado dela. Funciona em rede local, por IP e, com o complemento Steam, pela Steam.

O módulo é [`Range.network`](../../api/modulos/network/).

## 1. Menu de sala pronto

Anexe o componente `anastacio_network.component.AnastacioNetworkComponent` num objeto que fique na cena o tempo todo (uma câmera ou um Empty).

Ele mostra uma janela com **Criar sala**, **Procurar salas** (rede local), **Entrar por IP**, lista de jogadores, "pronto" e chat. O host aperta **Iniciar** quando todos estiverem prontos.

Opções do componente:

- **default_port**: porta da sala (padrão 7777);
- **max_players**: quantas pessoas cabem;
- **game_id**: identifica o seu jogo, para não aparecer sala de outro jogo na busca.

<!-- PRINT: menu do componente aberto, com a lista de salas -->

## 2. Sincronizar um objeto

Selecione o objeto e abra **Properties > Physics**, painel **Network**:

1. Ligue **Replicate**.
2. Marque o que sincronizar: posição (**Sync Transform**), velocidade, rotação.
3. Para enviar uma propriedade de jogo também (vida, pontos), ligue o botão **Rep** ao lado dela na lista de propriedades.

Objetos replicados são do host: ele move, os outros veem.

<!-- PRINT: painel Network com Replicate ligado -->

## 3. Um jogador para cada pessoa

Deixe um objeto `Jogador` com **Replicate** numa **camada inativa**. O host cria uma cópia quando alguém entra:

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

`on_player_join` e `on_player_leave` só são chamados no host. `owner=cliente` diz de quem é aquele boneco.

## 4. Mandar os comandos de cada jogador

Cada jogador envia o próprio input, e o host aplica no boneco dele. O input é um `bytes` de até 57 bytes:

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

Este componente fica num objeto fixo da cena (todos os jogadores rodam). No host, quem move os bonecos lê o input de cada dono:

```python
    # dentro da classe Partida
    def update(self):
        for cliente, jogador in self.jogadores.items():
            dados = network.input(cliente)
            if dados:
                frente, lado = struct.unpack("bb", dados[:2])
                jogador.applyMovement((lado * 0.1, frente * 0.1, 0.0), True)
```

(lembre de `import struct` no começo do arquivo da Partida)

## Testar na mesma máquina

Abra o jogo duas vezes. Em uma, **Criar sala**; na outra, **Entrar por IP** com `127.0.0.1`.

`network.set_simulation(120, 20, 2)` simula 120 ms de atraso, 20 ms de variação e 2% de perda, para ver como o jogo se comporta numa internet ruim.
