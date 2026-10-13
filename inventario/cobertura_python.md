# Cobertura Python dos controles de jogo

Gerado por `tools/api_inventario.py`. Compara somente controles RNA de recursos de jogo com bindings Python; não afirma que todo controle do editor deve virar API.

**Total:** 118 expostos · 10 sem binding · 0 só de editor.

## Partículas GPU

| Controle RNA/editor | API Python encontrada | Estado |
|---|---|---|
| `billboard_mode` | `billboardMode` | exposto |
| `blend_mode` | `blendMode` | exposto |
| `burst_interval` | `burstInterval` | exposto |
| `collision_bounce` | `collisionBounce` | exposto |
| `collision_friction` | `collisionFriction` | exposto |
| `collision_ground_object` | `collisionGroundObject` | **sem binding** |
| `collision_height` | `collisionHeight` | exposto |
| `collision_mode` | `collisionMode` | exposto |
| `color` | `color` | exposto |
| `color_curve` | `colorCurve` | **sem binding** |
| `drag` | `drag` | exposto |
| `emission_angle` | `emissionAngle` | exposto |
| `emission_direction` | `emissionDirection` | exposto |
| `emission_mode` | `emissionMode` | exposto |
| `emit_from` | `emitFrom` | **sem binding** |
| `emitter_position` | `emitterPosition` | exposto |
| `emitter_radius` | `emitterRadius` | exposto |
| `enabled` | `enabled` | exposto |
| `end_color` | `endColor` | exposto |
| `end_size` | `endSize` | exposto |
| `fragment_shader_path` | `fragmentShaderPath` | exposto |
| `gravity` | `gravity` | exposto |
| `lifetime` | `lifetime` | exposto |
| `particle_count` | `particleCount` | exposto |
| `particle_look` | `particleLook` | **sem binding** |
| `size` | `size` | exposto |
| `size_curve` | `sizeCurve` | **sem binding** |
| `texture` | `texture` | exposto |
| `use_backface_culling` | `useBackfaceCulling` | exposto |
| `use_burst_on_start` | `useBurstOnStart` | **sem binding** |
| `use_color_curve` | `useColorCurve` | **sem binding** |
| `use_debug_ui` | `useDebugUi` | exposto |
| `use_fragment_shader` | `useFragmentShader` | **sem binding** |
| `use_size_curve` | `useSizeCurve` | **sem binding** |
| `use_vortex` | `useVortex` | exposto |
| `velocity` | `velocity` | exposto |
| `velocity_randomness` | `velocityRandomness` | exposto |
| `vortex_height` | `vortexHeight` | exposto |
| `vortex_radius_top` | `vortexRadiusTop` | exposto |
| `vortex_rotation_speed` | `vortexRotationSpeed` | exposto |

## Explosão

| Controle RNA/editor | API Python encontrada | Estado |
|---|---|---|
| `blast_speed` | `blastSpeed` | exposto |
| `effect` | `explosionEffect` | exposto |
| `effect_life` | `effectLife` | exposto |
| `fire_amount` | `fireAmount` | exposto |
| `fire_color` | `fireColor` | exposto |
| `force` | `explosionForce` | exposto |
| `fuse` | `fuse` | exposto |
| `impact_impulse` | `impactImpulse` | exposto |
| `mark` | `groundMark` | exposto |
| `mark_life` | `markLife` | exposto |
| `mark_size` | `markSize` | exposto |
| `particle_size` | `particleSize` | exposto |
| `particle_style` | `particleStyle` | exposto |
| `radius` | `explosionRadius` | exposto |
| `smoke_amount` | `smokeAmount` | exposto |
| `smoke_color` | `smokeColor` | exposto |
| `smoke_duration` | `smokeDuration` | exposto |
| `spark_amount` | `sparkAmount` | exposto |
| `spark_color` | `sparkColor` | exposto |
| `up_bias` | `upBias` | exposto |
| `use_chain_reaction` | `useChainReaction` | exposto |
| `use_explode_on_impact` | `useExplodeOnImpact` | exposto |
| `use_ground_mark` | `useGroundMark` | exposto |
| `use_mark_nearby` | `useMarkNearby` | exposto |
| `use_occlusion` | `useOcclusion` | exposto |
| `use_particle_explosion` | `useParticleExplosion` | exposto |

## Clima do World

| Controle RNA/editor | API Python encontrada | Estado |
|---|---|---|
| `cloud_color` | `setWeather/getWeather(cloud_color_r, cloud_color_g, cloud_color_b)` | exposto |
| `cloud_coverage` | `setWeather/getWeather(cloud_coverage)` | exposto |
| `cloud_detail` | `setWeather/getWeather(cloud_detail)` | exposto |
| `cloud_scale` | `setWeather/getWeather(cloud_scale)` | exposto |
| `cloud_speed` | `setWeather/getWeather(cloud_speed)` | exposto |
| `use_clouds` | `setWeather/getWeather(clouds)` | exposto |
| `use_earthquake` | `setWeather/getWeather(earthquake)` | exposto |
| `use_lens_flare` | `setWeather/getWeather(lens_flare)` | exposto |
| `use_rain` | `setWeather/getWeather(rain)` | exposto |
| `use_rain_aura` | `setWeather/getWeather(aura)` | exposto |
| `use_rain_droplets` | `setWeather/getWeather(droplets)` | exposto |
| `use_rain_lightning` | `setWeather/getWeather(lightning)` | exposto |
| `use_rain_lightning_side` | `setWeather/getWeather(lightning_side)` | exposto |
| `use_rain_puddle_ssr` | `setWeather/getWeather(puddle_ssr)` | exposto |
| `use_rain_puddles` | `setWeather/getWeather(puddles)` | exposto |
| `use_rain_ripple` | `setWeather/getWeather(ripples)` | exposto |
| `use_rain_ripple_puddle_only` | `setWeather/getWeather(ripple_puddle_only)` | exposto |
| `use_rain_splash` | `setWeather/getWeather(splash)` | exposto |
| `use_rain_splash_puddle_only` | `setWeather/getWeather(splash_puddle_only)` | exposto |
| `use_sky_layers` | `setWeather/getWeather(use_sky_layers)` | exposto |
| `use_volumetric_clouds` | `setWeather/getWeather(use_volumetric_clouds)` | exposto |
| `use_volumetric_fog` | `setWeather/getWeather(vfog)` | exposto |
| `vcloud_altitude` | `setWeather/getWeather(vcloud_altitude)` | exposto |
| `vcloud_color` | `setWeather/getWeather(vcloud_color_r, vcloud_color_g, vcloud_color_b)` | exposto |
| `vcloud_coverage` | `setWeather/getWeather(vcloud_coverage)` | exposto |
| `vcloud_density` | `setWeather/getWeather(vcloud_density)` | exposto |
| `vcloud_detail_scale` | `setWeather/getWeather(vcloud_detail_scale)` | exposto |
| `vcloud_quality` | `setWeather/getWeather(vcloud_quality)` | exposto |
| `vcloud_scale` | `setWeather/getWeather(vcloud_scale)` | exposto |
| `vcloud_shadow_enable` | `setWeather/getWeather(vcloud_shadow_enable)` | exposto |
| `vcloud_shadow_strength` | `setWeather/getWeather(vcloud_shadow_strength)` | exposto |
| `vcloud_silver_intensity` | `setWeather/getWeather(vcloud_silver_intensity)` | exposto |
| `vcloud_speed` | `setWeather/getWeather(vcloud_speed)` | exposto |
| `vcloud_thickness` | `setWeather/getWeather(vcloud_thickness)` | exposto |
| `vfog_ambient` | `setWeather/getWeather(vfog_ambient)` | exposto |
| `vfog_anisotropy` | `setWeather/getWeather(vfog_anisotropy)` | exposto |
| `vfog_base` | `setWeather/getWeather(vfog_base)` | exposto |
| `vfog_color` | `setWeather/getWeather(vfog_color_r, vfog_color_g, vfog_color_b)` | exposto |
| `vfog_density` | `setWeather/getWeather(vfog_density)` | exposto |
| `vfog_distance` | `setWeather/getWeather(vfog_distance)` | exposto |
| `vfog_dust` | `setWeather/getWeather(vfog_dust)` | exposto |
| `vfog_edge` | `setWeather/getWeather(vfog_edge)` | exposto |
| `vfog_falloff` | `setWeather/getWeather(vfog_falloff)` | exposto |
| `vfog_light_intensity` | `setWeather/getWeather(vfog_light_intensity)` | exposto |
| `vfog_max_lights` | `setWeather/getWeather(vfog_max_lights)` | exposto |
| `vfog_morning_boost` | `setWeather/getWeather(vfog_morning_boost)` | exposto |
| `vfog_noise_amount` | `setWeather/getWeather(vfog_noise_amount)` | exposto |
| `vfog_noise_scale` | `setWeather/getWeather(vfog_noise_scale)` | exposto |
| `vfog_quality` | `setWeather/getWeather(vfog_quality)` | exposto |
| `vfog_resolution` | `` | **sem binding** |
| `vfog_shaft_intensity` | `setWeather/getWeather(vfog_shaft_intensity)` | exposto |
| `vfog_speed` | `setWeather/getWeather(vfog_speed)` | exposto |
| `vfog_sun_intensity` | `setWeather/getWeather(vfog_sun_intensity)` | exposto |
| `vfog_use_lamps` | `setWeather/getWeather(vfog_use_lamps)` | exposto |
| `vfog_use_layer` | `setWeather/getWeather(vfog_use_layer)` | exposto |
| `vfog_use_reach_clouds` | `setWeather/getWeather(vfog_use_reach_clouds)` | exposto |
| `vfog_use_shafts` | `setWeather/getWeather(vfog_use_shafts)` | exposto |
| `vfog_use_sun_shafts` | `setWeather/getWeather(vfog_use_sun_shafts)` | exposto |
| `vfog_use_time_of_day` | `setWeather/getWeather(vfog_use_time_of_day)` | exposto |
| `vfog_use_wind` | `setWeather/getWeather(vfog_use_wind)` | exposto |
| `vfog_volumes_only` | `setWeather/getWeather(vfog_volumes_only)` | exposto |
| `vfog_wind_direction` | `setWeather/getWeather(vfog_wind_direction)` | exposto |
