---
title: Veículos
description: Montar um carro com o painel Vehicle e dirigir com o componente pronto ou pelo Python.
---

A Anastacio cria o veículo sozinha a partir do painel **Physics > Vehicle**. Você só configura as rodas e anexa um controle.

## 1. Monte o carro

Você precisa de um chassi (a carroceria) e um objeto para cada roda.

1. Selecione o chassi. Em **Properties > Physics**, use **Rigid Body** e ligue o veículo no painel **Vehicle**.
2. Na lista de rodas, adicione uma entrada para cada roda e escolha o objeto dela.
3. Em cada roda, ajuste **raio**, **suspensão**, se ela **esterça** (as da frente) e se ela **traciona**.

<!-- PRINT: painel Physics > Vehicle com quatro rodas -->

:::tip
O demo **Vehicle** que vem com a engine (pasta `demos/Vehicle`) já traz um carro montado. Abra para ver valores que funcionam.
:::

## 2. Dirija com o componente pronto

Anexe o componente `VehiclePlayerComponent` (arquivo `vehicle_player_component.py` do demo) no chassi.

- **W** acelera, **S** dá ré, **A/D** esterçam;
- **Espaço** freia, **Shift esquerdo** é o freio de mão;
- com marchas cadastradas no painel Vehicle, o câmbio troca sozinho (ou com E/Q no manual).

O componente publica as propriedades `vehicle_speed_kmh`, `vehicle_rpm` e `vehicle_gear` no chassi, úteis para um velocímetro.

:::tip
Pela convenção do projeto, a frente do chassi aponta para **+Y**. Se o carro andar de ré ao apertar W, ligue **Invert Direction** nas propriedades do `VehiclePlayerComponent`.
:::

## 3. Ou controle pelo Python

`getVehicle()` devolve o veículo do chassi ([`KX_VehicleWrapper`](../../api/types/kx_vehiclewrapper/)). Um controle mínimo:

```python
import Range
from Range import events, logic


class DirigirSimples(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.carro = self.object.getVehicle()

    def update(self):
        if self.carro is None:
            return
        tecla = logic.keyboard.inputs
        forca = 0.0
        if tecla[events.WKEY].active:
            forca = -1500.0
        elif tecla[events.SKEY].active:
            forca = 800.0
        volante = 0.0
        if tecla[events.AKEY].active:
            volante = 0.4
        elif tecla[events.DKEY].active:
            volante = -0.4

        for roda in range(self.carro.getNumWheels()):
            self.carro.applyEngineForce(forca, roda)
            self.carro.applyBraking(0.0, roda)
        self.carro.setSteeringValue(volante, 0)
        self.carro.setSteeringValue(volante, 1)
```

Anexe no chassi. As rodas 0 e 1 são as duas primeiras da lista do painel (as que esterçam).

:::note
O sinal da força depende de para onde o chassi aponta. Se o carro andar de ré com W, troque os sinais.
:::

## Salvar o acerto do carro

`vehicle.savePreset("//acerto.json")` grava massa, suspensão, atrito e rodas num arquivo. `vehicle.loadPreset(...)` reaplica o acerto no mesmo carro, por exemplo para trocar entre "asfalto" e "terra".

:::caution
`savePreset()` falha se o campo **Ray Cast Mask** do veículo estiver no valor padrão (0): a engine grava internamente -1 e a própria validação recusa esse valor. Defina o Ray Cast Mask manualmente no painel Vehicle antes de salvar o acerto.
:::
