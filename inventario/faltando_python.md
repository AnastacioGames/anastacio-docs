# Recursos da Anastacio sem acesso pelo Python

Levantamento de 2026-10-09. Método: propriedades RNA (o que aparece nos painéis do editor) adicionadas depois do snapshot `28775369` (15/09/2026), cruzadas com os nomes da API Python (`inventario/api_inventario.json`). É heurístico: confirme cada item no código antes de criar o binding.

**Já têm acesso e só precisam de documentação (não criar binding):**
- Chuva, poças, respingos, ondulações, aura, raios, nuvens, lens flare, neblina e terremoto: `KX_WorldInfo.setWeather(nome, valor)` / `getWeather(nome)` com ~60 nomes `weather.*` (lista em `KX_WorldInfo::SetWeatherRuntimeProperty`, `Ketsji/KX_WorldInfo.cpp:153`).
- Camera FX (foco, rastreamento, DOF, borrões etc.): atributos em `KX_Camera`.
- Destruição: `isDestructible`, `isExplosive`, `onBreak`, `onExplode`, `onDent`, `breakImpulse`, `fuse` em `KX_GameObject`.
- Multiplayer: funções de `Range.network` (`host`, `join`, `replicate`…).
- Load Mode: `Range.logic.setObjectConvert/getObjectConvert`, `KX_Scene.convertObject`, `freeUnconvertedData`.

## Tarefa para o Claude no VS Code

Repositório: `D:\AnastacioEngine`. Siga o `AGENTS.md`. Compile com a skill `build-anastacio`.
Padrão de binding: tabelas `PyMethodDef X::Methods[]` / `PyAttributeDef X::Attributes[]` (ex.: `Ketsji/KX_Camera.cpp`, `Ketsji/KX_WorldInfo.cpp`). Leitura e escrita em tempo de jogo, com o nome em camelCase do Python.

### Prioridade 1: mudam o jogo em tempo real

> Feita na engine em 49be685b (2026-10-09): céu, destruição, FXAA/grão e `quantize` em `network.replicate`. `use_interpolate` ficou sem binding porque o runtime não lê esse valor.

1. **Céu (`KX_WorldInfo`)**: o painel tem, mas o Python não acessa.
   `sky_type`, `star_style`, `use_sky_moon`, `moon_size`, `moon_brightness`, `use_sky_aurora`, `aurora_colors`, `atmosphere_altitude`, `atmosphere_intensity`, `atmosphere_mie_density`, `atmosphere_mie_direction`, `atmosphere_rayleigh_color`, `atmosphere_rayleigh_density`.
   Sugestão: entrar como novos nomes do `setWeather` (`sky.moon_size`…) ou como atributos (`world.moonSize`). Decidir e manter um só padrão.
2. **Parâmetros de destruição (`KX_GameObject`)**: só existem os ligados/desligados e callbacks.
   `fragments`, `debris_lifetime`, `impact_impulse`, `dent_impulse`, `burst_speed`, `use_chain_reaction`, `use_break_on_collision`, `use_dent_on_collision`, `use_explode_on_impact`, `use_inherit_velocity`, `decal`, `decal_size`, `decal_life`, `max_decals`, `deform`/`use_deform`, `bend_angle`, `bend_axis`, `bend_max_angle`.
3. **Pós-processo da cena (`KX_Scene` ou `Range.render`)**:
   FXAA (`fxaa_edge_threshold`, `fxaa_edge_threshold_min`, `fxaa_search_steps`, `fxaa_subpix`) e grão (`use_grain`, `grain_strength`; hoje só há `changeGrainValues`, confirmar se cobre).
4. **Sombra automática da luz (`KX_LightObject`)**: `use_auto_shadow_update`.
5. **Rede por objeto (`KX_GameObject`)**: `sync_transform`, `sync_velocity`, `sync_angular_velocity`, `use_interpolate`, `use_always_relevant`, `priority`, `net_id` (confirmar se `replicate()` já cobre).
   Rede por propriedade de jogo: `use_replicate`, `net_bits`, `net_min`, `net_max`.

### Prioridade 2: úteis para quem programa

6. **Status da rede na cena**: `tick_rate`, `snapshot_rate`, `max_players`, `relevance_radius`, `use_late_join`, `use_lan_discovery`, `server_name`, `port`, `websocket_port`, só leitura em `Range.network` (os valores do painel). `host()` já aceita parâmetros.
7. **VR (`Range.render`)**: `vr_head_tracking`, `vr_head_smoothing`, `vr_recenter_time`, `vr_vignette`, `vr_lens_distortion` (já existem `set/getVRLensStrength` e `ChromaticAberration`).
8. **Cutscene por caminho (`KX_Scene`)**: `path_object`, `path_curve`, `path_duration`, `path_follow`, `path_look_at`, `path_set_camera` (já existem `play_cutscene`, `stop_cutscene`, `restart_cutscene`).
9. **Sensor de olhar (VR)**: `use_gaze_highlight`, `use_gaze_reticle`, `use_gaze_self`, `hold`.
10. **Atuadores novos de clima (`rna_actuator.c`)**: `weather_category`, `weather_effect`, `aura_effect`, `cloud_effect`, `earthquake_effect`, `lens_flare_effect`, `lightning_effect`, `mist_effect`, `splash_effect`, `use_lightning_flash_only`, `use_object_from_property`, `object_property`, `use_vr_gaze`, `use_vr_teleport`.
11. **Material**: `use_foliage_optimization`, `foliage_distance`, `game_radius` (só leitura basta).

### Não precisa de Python (configuração de editor ou build)

`game_load_mode`, `use_static_batch`, `use_fast_shader_loading`, `use_shading_nodes`, `game_id`, `game_version`, `uid`, `use_live_ui`, `render_editor_grain`, `use_preview`, todos os `show_*`, `rna_space.c`, `rna_userdef.c`, `rna_screen.c`. A física do Fixed Timestep, o GTAO e o lightmap baked também não têm RNA de jogo nova. Se quiser controlá-los em tempo de jogo, é um pedido separado.

## Ao terminar

Rodar de novo `python D:/AnastacioDocs/tools/api_inventario.py`. Os bindings novos devem aparecer como **novo ✦** no relatório, prontos para documentar.
