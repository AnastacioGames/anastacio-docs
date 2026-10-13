# Roteiro de teste dos guias em rascunho

Páginas com `draft: true` não saem no site publicado. Depois do teste OK: tirar `draft`, pôr no sidebar (astro.config.mjs), tirar prints (marcados `<!-- PRINT -->`) e traduzir para en/.

## clima.md
- Cena: plano + Cubo, World com Rain ligado. Componente `Clima` no Cubo.
- Esperado: chuva fraca; aos 5 s chuva forte, poças e um raio.
- Conferir: nome do painel de clima na aba World; `scene.world` existe no componente.

## camera-fx.md
- Câmera com Focus Object = Cubo, Tracking Look At. Mover o Cubo: câmera gira.
- `TremerNoEspaco`: Espaço treme a câmera.
- Snippet do menu (`useSpeedBlur`...) e `changeGrainValues(True, 0.3)` sem erro.

## load-mode.md
- Objeto "Chefe" On Demand: não aparece ao abrir; `convertObject("Chefe")` cria.
- "Tiro" On Demand em camada inativa + addObject.
- Cook com .blend salvo gera .cooked; `getLoadLog()` imprime dicts.

## veiculos.md
- Demo Vehicle: VehiclePlayerComponent dirige (W/S/A/D, Espaço, Shift).
- `DirigirSimples` no chassi: confirmar sinal da força e índices das rodas que esterçam.
- `savePreset("//acerto.json")` / `loadPreset`.

## multiplayer.md
- Conferir em qual aba fica o painel Network do objeto (bl_context "game").
- Duas instâncias: Criar sala / Entrar 127.0.0.1.
- `Partida`: on_player_join é chamado também para o host (cliente 0)? Se não, criar o boneco do host em on_connect(0).
- `network.input()` no cliente: retorna None ou dá erro? (Partida.update roda em todos.)
- Bonecos se movem nos dois lados.
