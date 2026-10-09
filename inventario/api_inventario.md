# Inventário da API Python

Gerado por `tools/docs/api_inventario.py`. Módulos expostos como `Range.<módulo>` e `bge.<módulo>`.

**Total:** 105 classes, 8 módulos | documentados 1018 · sem doc 248 · novos 509 · só no rst 111

Legenda: **novo** = existe no C++ e não está no rst (provável função da Anastacio); **sem doc** = está no rst sem descrição; **só no rst** = documentado mas não achado no C++ (removido, herdado de classe base ou definido de outro jeito).

## Módulos

| Nome | Itens | Documentados | Sem doc | Novos | Só no rst | rst? |
|---|---:|---:|---:|---:|---:|:---:|
| `Range.logic` | 340 | 149 | 137 | 49 | 5 | sim |
| `Range.imgui` | 42 | 0 | 0 | 42 | 0 | **não** |
| `Range.network` | 41 | 0 | 0 | 41 | 0 | **não** |
| `Range.render` | 67 | 45 | 0 | 21 | 1 | sim |
| `Range.events` | 135 | 9 | 111 | 15 | 0 | sim |
| `Range.network.steam` | 9 | 0 | 0 | 9 | 0 | **não** |
| `Range.constraints` | 52 | 43 | 0 | 8 | 1 | sim |
| `Range.texture` | 36 | 4 | 0 | 0 | 32 | sim |

## Classes (Range.types)

| Nome | Itens | Documentados | Sem doc | Novos | Só no rst | rst? |
|---|---:|---:|---:|---:|---:|:---:|
| `KX_GameObject` | 187 | 118 | 0 | 69 | 0 | sim |
| `KX_Camera` | 80 | 31 | 0 | 49 | 0 | sim |
| `KX_Speaker` | 41 | 0 | 0 | 41 | 0 | **não** |
| `KX_ParticleSystem` | 21 | 0 | 0 | 21 | 0 | **não** |
| `KX_WorldInfo` | 36 | 19 | 0 | 17 | 0 | sim |
| `KX_MeshBuilderSlot` | 15 | 0 | 0 | 15 | 0 | **não** |
| `KX_2DFilterManager` | 17 | 3 | 0 | 14 | 0 | sim |
| `KX_VehicleWrapper` | 30 | 16 | 0 | 14 | 0 | sim |
| `KX_Scene` | 37 | 28 | 0 | 9 | 0 | sim |
| `EXP_BaseListValue` | 7 | 0 | 0 | 7 | 0 | **não** |
| `KX_PythonJoystick` | 15 | 8 | 0 | 7 | 0 | sim |
| `KX_VRHeadSensor` | 6 | 0 | 0 | 6 | 0 | **não** |
| `KX_InputSystem` | 5 | 0 | 0 | 5 | 0 | **não** |
| `Texture` | 24 | 0 | 0 | 5 | 19 | sim |
| `KX_InputTable` | 4 | 0 | 0 | 4 | 0 | **não** |
| `KX_MeshBuilder` | 4 | 0 | 0 | 4 | 0 | **não** |
| `KX_PythonMotion` | 11 | 7 | 0 | 4 | 0 | sim |
| `KX_ChangeColorActuator` | 3 | 0 | 0 | 3 | 0 | **não** |
| `KX_FontObject` | 7 | 4 | 0 | 3 | 0 | sim |
| `KX_RaySensor` | 14 | 11 | 0 | 3 | 0 | sim |
| `KX_SteeringActuator` | 14 | 11 | 0 | 3 | 0 | sim |
| `BL_ActionActuator` | 12 | 10 | 0 | 2 | 0 | sim |
| `KX_AnimationEvent` | 2 | 0 | 0 | 2 | 0 | **não** |
| `KX_GameActuator` | 4 | 2 | 0 | 2 | 0 | sim |
| `KX_MovementSensor` | 2 | 0 | 0 | 2 | 0 | **não** |
| `KX_PythonMouse` | 8 | 6 | 0 | 2 | 0 | sim |
| `EXP_BaseListWrapper` | 1 | 0 | 0 | 1 | 0 | **não** |
| `KX_AnimationEventManager` | 1 | 0 | 0 | 1 | 0 | **não** |
| `KX_BlenderMaterial` | 16 | 15 | 0 | 1 | 0 | sim |
| `KX_BoundingBox` | 6 | 5 | 0 | 1 | 0 | sim |
| `KX_LightObject` | 25 | 24 | 0 | 1 | 0 | sim |
| `KX_LightningActuator` | 1 | 0 | 0 | 1 | 0 | **não** |
| `KX_LodManager` | 3 | 2 | 0 | 1 | 0 | sim |
| `KX_Mesh` | 15 | 14 | 0 | 1 | 0 | sim |
| `SCA_DelaySensor` | 5 | 4 | 0 | 1 | 0 | sim |
| `SCA_ISensor` | 14 | 13 | 0 | 1 | 0 | sim |
| `SCA_MouseSensor` | 4 | 3 | 0 | 1 | 0 | sim |
| `BL_ArmatureActuator` | 6 | 6 | 0 | 0 | 0 | sim |
| `BL_ArmatureBone` | 15 | 0 | 0 | 0 | 15 | sim |
| `BL_ArmatureChannel` | 34 | 2 | 0 | 0 | 32 | sim |
| `BL_ArmatureConstraint` | 14 | 14 | 0 | 0 | 0 | sim |
| `BL_ArmatureObject` | 4 | 4 | 0 | 0 | 0 | sim |
| `BL_Shader` | 26 | 26 | 0 | 0 | 0 | sim |
| `BL_Texture` | 19 | 19 | 0 | 0 | 0 | sim |
| `EXP_PyObjectPlus` | 1 | 1 | 0 | 0 | 0 | sim |
| `EXP_Value` | 1 | 1 | 0 | 0 | 0 | sim |
| `KX_2DFilter` | 6 | 6 | 0 | 0 | 0 | sim |
| `KX_2DFilterOffScreen` | 4 | 4 | 0 | 0 | 0 | sim |
| `KX_AddObjectActuator` | 6 | 6 | 0 | 0 | 0 | sim |
| `KX_ArmatureSensor` | 3 | 3 | 0 | 0 | 0 | sim |
| `KX_BatchGroup` | 5 | 5 | 0 | 0 | 0 | sim |
| `KX_CameraActuator` | 6 | 6 | 0 | 0 | 0 | sim |
| `KX_CharacterWrapper` | 13 | 13 | 0 | 0 | 0 | sim |
| `KX_CollisionContactPoint` | 8 | 8 | 0 | 0 | 0 | sim |
| `KX_CollisionSensor` | 6 | 6 | 0 | 0 | 0 | sim |
| `KX_ConstraintActuator` | 11 | 11 | 0 | 0 | 0 | sim |
| `KX_ConstraintWrapper` | 7 | 7 | 0 | 0 | 0 | sim |
| `KX_CubeMap` | 0 | 0 | 0 | 0 | 0 | sim |
| `KX_DynamicActuator` | 2 | 2 | 0 | 0 | 0 | sim |
| `KX_EndObjectActuator` | 0 | 0 | 0 | 0 | 0 | sim |
| `KX_LibLoadStatus` | 5 | 5 | 0 | 0 | 0 | sim |
| `KX_LodLevel` | 7 | 7 | 0 | 0 | 0 | sim |
| `KX_MouseActuator` | 14 | 14 | 0 | 0 | 0 | sim |
| `KX_MouseFocusSensor` | 12 | 12 | 0 | 0 | 0 | sim |
| `KX_NavMeshObject` | 8 | 8 | 0 | 0 | 0 | sim |
| `KX_NearSensor` | 2 | 2 | 0 | 0 | 0 | sim |
| `KX_NetworkMessageActuator` | 4 | 4 | 0 | 0 | 0 | sim |
| `KX_NetworkMessageSensor` | 4 | 4 | 0 | 0 | 0 | sim |
| `KX_ObjectActuator` | 18 | 18 | 0 | 0 | 0 | sim |
| `KX_ParentActuator` | 4 | 4 | 0 | 0 | 0 | sim |
| `KX_PlanarMap` | 1 | 1 | 0 | 0 | 0 | sim |
| `KX_PolyProxy` | 20 | 20 | 0 | 0 | 0 | sim |
| `KX_PythonComponent` | 5 | 1 | 0 | 0 | 4 | sim |
| `KX_PythonKeyboard` | 7 | 7 | 0 | 0 | 0 | sim |
| `KX_RadarSensor` | 5 | 5 | 0 | 0 | 0 | sim |
| `KX_ReplaceMeshActuator` | 4 | 4 | 0 | 0 | 0 | sim |
| `KX_SceneActuator` | 4 | 4 | 0 | 0 | 0 | sim |
| `KX_SoundActuator` | 17 | 17 | 0 | 0 | 0 | sim |
| `KX_StateActuator` | 2 | 2 | 0 | 0 | 0 | sim |
| `KX_TextureRenderer` | 8 | 8 | 0 | 0 | 0 | sim |
| `KX_TrackToActuator` | 5 | 5 | 0 | 0 | 0 | sim |
| `KX_VertexProxy` | 28 | 28 | 0 | 0 | 0 | sim |
| `KX_VisibilityActuator` | 3 | 3 | 0 | 0 | 0 | sim |
| `SCA_2DFilterActuator` | 5 | 5 | 0 | 0 | 0 | sim |
| `SCA_ANDController` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_ActuatorSensor` | 1 | 1 | 0 | 0 | 0 | sim |
| `SCA_AlwaysSensor` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_AnimationEventSensor` | 0 | 0 | 0 | 0 | 0 | **não** |
| `SCA_IController` | 4 | 4 | 0 | 0 | 0 | sim |
| `SCA_ILogicBrick` | 3 | 2 | 0 | 0 | 1 | sim |
| `SCA_IObject` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_InputEvent` | 8 | 8 | 0 | 0 | 0 | sim |
| `SCA_JoystickSensor` | 15 | 15 | 0 | 0 | 0 | sim |
| `SCA_KeyboardSensor` | 9 | 9 | 0 | 0 | 0 | sim |
| `SCA_NANDController` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_NORController` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_ORController` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_PropertyActuator` | 3 | 3 | 0 | 0 | 0 | sim |
| `SCA_PropertySensor` | 5 | 5 | 0 | 0 | 0 | sim |
| `SCA_PythonController` | 5 | 4 | 0 | 0 | 1 | sim |
| `SCA_RandomActuator` | 15 | 15 | 0 | 0 | 0 | sim |
| `SCA_RandomSensor` | 2 | 2 | 0 | 0 | 0 | sim |
| `SCA_VibrationActuator` | 8 | 8 | 0 | 0 | 0 | sim |
| `SCA_XNORController` | 0 | 0 | 0 | 0 | 0 | sim |
| `SCA_XORController` | 0 | 0 | 0 | 0 | 0 | sim |

## Itens novos por classe/módulo

Origem pelo git: **176** adicionados depois de 15/09/2026 (Anastacio, marcados com ✦data); **244** já estavam no snapshot inicial do código (Range sem doc ou Anastacio antiga, precisa confirmar).

- **Range.constraints** (source/source/gameengine/Ketsji/KX_PyConstraintBinding.cpp): `setErp`, `setErp2`, `setGlobalCfm`, `setSplitImpulse`, `setSplitImpulsePenetrationThreshold`, `setSplitImpulseTurnErp`, `setWarmstartingFactor`, `setMaxGyroscopicForce`
- **Range.events** (source/source/gameengine/Ketsji/KX_PythonInit.cpp): `OSKEY`, `JOYSTICKA`, `JOYSTICKB`, `JOYSTICKX`, `JOYSTICKY`, `JOYSTICKBACK`, `JOYSTICKGUIDE`, `JOYSTICKLEFTSTICK`, `JOYSTICKRIGHTSTICK`, `JOYSTICKRIGHTSHOUDER`, `JOYSTICKLEFTSHOUDER`, `JOYSTICKPADUP`, `JOYSTICKPADDOWN`, `JOYSTICKPADLEFT`, `JOYSTICKPADRIGHT`
- **Range.imgui** (source/source/gameengine/Ketsji/KXImgui/KX_PythonImgui.cpp): `begin`, `end`, `text`, `button`, `checkbox`, `slider_float`, `slider_int`, `input_text`, `combo`, `listbox`, `radio_button`, `color_edit3`, `color_edit4`, `open_popup`, `begin_popup_modal`, `end_popup`, `close_current_popup`, `push_style_color`, `pop_style_color`, `load_font`, `load_default_font` ✦2026-10-08, `push_style_var` ✦2026-10-08, `pop_style_var` ✦2026-10-08, `push_item_width` ✦2026-10-08, `pop_item_width` ✦2026-10-08, `set_next_item_width` ✦2026-10-08, `push_font`, `pop_font`, `get_display_size`, `draw_rect_filled`, `separator`, `same_line`, `set_next_window_pos`, `set_next_window_size`, `image`, `invisible_button`, `set_cursor_pos`, `get_cursor_pos`, `get_cursor_screen_pos`, `get_io_want_capture_mouse`, `get_io_want_capture_keyboard`, `set_game_ui_open`
- **Range.logic** (source/source/gameengine/Ketsji/KX_PythonInit.cpp): `getMessages` ✦2026-09-30, `setNeedsParents`, `getRenderRate`, `setRenderRate`, `getAnimationRate`, `setAnimationRate`, `deltaTime`, `getRangeFileList`, `getRasecFileList`, `getGraphicsCardVendor`, `getGraphicsCardRenderer`, `getProcessorName`, `setObjectConvert` ✦2026-10-07, `freeUnconvertedData` ✦2026-10-07, `getLoadLog` ✦2026-10-07, `getObjectConvert` ✦2026-10-07, `KX_MOVEMENT_AXIS_POS_X`, `KX_MOVEMENT_AXIS_POS_Y`, `KX_MOVEMENT_AXIS_POS_Z`, `KX_MOVEMENT_AXIS_NEG_X`, `KX_MOVEMENT_AXIS_NEG_Y`, `KX_MOVEMENT_AXIS_NEG_Z`, `KX_MOVEMENT_ALL_AXIS`, `KX_MOUSE_BUT_LEFTTHUMBMOUSE`, `KX_MOUSE_BUT_RIGHTTHUMBMOUSE`, `KX_MOUSE_BUT_BUTTON6`, `KX_MOUSE_BUT_BUTTON7`, `KX_JOYSTICK_BUT_A`, `KX_JOYSTICK_BUT_B`, `KX_JOYSTICK_BUT_X`, `KX_JOYSTICK_BUT_Y`, `KX_JOYSTICK_BUT_BACK`, `KX_JOYSTICK_BUT_GUIDE`, `KX_JOYSTICK_BUT_LEFTSTICK`, `KX_JOYSTICK_BUT_RIGHTSTICK`, `KX_JOYSTICK_BUT_RIGHTSHOUDER`, `KX_JOYSTICK_BUT_LEFTSHOUDER`, `KX_JOYSTICK_BUT_PADUP`, `KX_JOYSTICK_BUT_PADDOWN`, `KX_JOYSTICK_BUT_PADLEFT`, `KX_JOYSTICK_BUT_PADRIGHT`, `RAS_2DFILTER_OUTLINE`, `RAS_2DFILTER_SSAO`, `RAS_2DFILTER_BLOOM`, `RAS_2DFILTER_TONEMAP`, `RAS_2DFILTER_LIGHTSCATTER`, `RAS_2DFILTER_SSR`, `RAS_2DFILTER_FXAA`, `KX_GAME_SCREENSHOT`
- **Range.network** (source/source/gameengine/Ketsji/KX_PyNetwork.cpp): `host` ✦2026-10-04, `join` ✦2026-10-04, `disconnect` ✦2026-10-04, `set_ready` ✦2026-10-04, `send_chat` ✦2026-10-04, `return_to_lobby` ✦2026-10-08, `start_game` ✦2026-10-04, `discover_lan` ✦2026-10-04, `set_simulation` ✦2026-10-04, `replicate` ✦2026-10-04, `spawn` ✦2026-10-04, `despawn` ✦2026-10-04, `set_owner` ✦2026-10-04, `owner` ✦2026-10-04, `is_owner` ✦2026-10-04, `net_id` ✦2026-10-04, `on_connect` ✦2026-10-04, `on_disconnect` ✦2026-10-04, `on_reject` ✦2026-10-04, `on_chat` ✦2026-10-04, `on_start` ✦2026-10-04, `on_lobby` ✦2026-10-08, `on_player_join` ✦2026-10-04, `on_player_leave` ✦2026-10-04, `on_scene` ✦2026-10-04, `change_scene` ✦2026-10-04, `predict` ✦2026-10-04, `set_input` ✦2026-10-04, `input` ✦2026-10-04, `view_time` ✦2026-10-04, `prediction_stats` ✦2026-10-04, `input_stats` ✦2026-10-04, `set_client_view` ✦2026-10-04, `set_hitbox` ✦2026-10-04, `raycast_past` ✦2026-10-04, `call` ✦2026-10-04, `_register_rpc` ✦2026-10-04, `_state` ✦2026-10-04, `_set_player_name` ✦2026-10-04, `_clients` ✦2026-10-04, `_headless` ✦2026-10-04
- **Range.network.steam** (source/source/gameengine/Ketsji/KX_PyNetwork.cpp): `connection_routes` ✦2026-10-08, `_lobby_request` ✦2026-10-08, `poll_events` ✦2026-10-08, `language` ✦2026-10-08, `achievement` ✦2026-10-08, `force_relay` ✦2026-10-08, `initialize` ✦2026-10-08, `status` ✦2026-10-08, `shutdown` ✦2026-10-08
- **Range.render** (source/source/gameengine/Ketsji/KX_PythonInit.cpp): `setCustomMouse`, `setStereoMode` ✦2026-10-01, `setVRLensStrength` ✦2026-10-01, `getVRLensStrength` ✦2026-10-01, `setVRChromaticAberration` ✦2026-10-01, `getVRChromaticAberration` ✦2026-10-01, `getStereoMode` ✦2026-10-01, `setMasterVolume`, `getMasterVolume`, `showDebugPhysics`, `RAS_MIPMAP_NONE`, `RAS_MIPMAP_NEAREST`, `RAS_MIPMAP_LINEAR`, `VSYNC_OFF`, `VSYNC_ON`, `VSYNC_ADAPTIVE`, `STEREO_NOSTEREO`, `STEREO_SIDEBYSIDE`, `STEREO_ABOVEBELOW`, `STEREO_ANAGLYPH`, `STEREO_INTERLACED`
- **BL_ActionActuator** (source/source/gameengine/Converter/BL_ActionActuator.cpp): `layer`, `layerWeight`
- **EXP_BaseListValue** (source/source/gameengine/Expressions/intern/BaseListValue.cpp): `append`, `reverse`, `index`, `count`, `get`, `filter`, `from_id`
- **EXP_BaseListWrapper** (source/source/gameengine/Expressions/intern/BaseListWrapper.cpp): `get`
- **KX_2DFilterManager** (source/source/gameengine/Ketsji/KX_2DFilterManager.cpp): `changeFxaaValues`, `changeTonemapValues`, `changeBloomValues`, `changeGrainValues`, `changeLightScatterValues`, `changeSSRValues`, `changeSSAOValues`, `fxaaEnabled` ✦2026-10-09, `fxaaEdgeThreshold` ✦2026-10-09, `fxaaEdgeThresholdMin` ✦2026-10-09, `fxaaSubpix` ✦2026-10-09, `fxaaSearchSteps` ✦2026-10-09, `grainEnabled` ✦2026-10-09, `grainStrength` ✦2026-10-09
- **KX_AnimationEvent** (source/source/gameengine/Ketsji/KX_AnimationEvent.cpp): `getFireCount`, `triggers` (só leitura)
- **KX_AnimationEventManager** (source/source/gameengine/Ketsji/KX_AnimationEventManager.cpp): `events` (só leitura)
- **KX_BlenderMaterial** (source/source/gameengine/Ketsji/KX_BlenderMaterial.cpp): `passIndex`
- **KX_BoundingBox** (source/source/gameengine/Ketsji/KX_BoundingBox.cpp): `volume` (só leitura)
- **KX_Camera** (source/source/gameengine/Ketsji/KX_Camera.cpp): `shake`, `focusMode` ✦2026-09-29, `focusObject` ✦2026-09-29, `focusProperty` ✦2026-09-29, `focusTarget` (só leitura) ✦2026-09-29, `focusPosition` (só leitura) ✦2026-09-29, `focusDistance` (só leitura) ✦2026-09-29, `focusScreenPosition` (só leitura) ✦2026-09-29, `focusValid` (só leitura) ✦2026-09-29, `focusManualDistance` ✦2026-09-29, `focusRange` ✦2026-09-29, `focusSmooth` ✦2026-09-29, `trackMode` ✦2026-09-29, `trackSpeed` ✦2026-09-29, `trackLimit` ✦2026-09-29, `trackDeadzone` ✦2026-09-29, `trackScreenOffset` ✦2026-09-29, `droneAmplitude` ✦2026-09-29, `droneFrequency` ✦2026-09-29, `trackBank` ✦2026-09-29, `trackOrientation` (só leitura) ✦2026-09-29, `gazeDirection` (só leitura) ✦2026-10-01, `useDof` ✦2026-09-29, `useSpeedBlur` ✦2026-09-29, `useDirectionalBlur` ✦2026-09-29, `useBlurProtect` ✦2026-09-29, `useCatEye` ✦2026-09-29, `useChromatic` ✦2026-09-29, `useChromaticSpeed` ✦2026-09-29, `useVignette` ✦2026-09-29, `useShakeRoll` ✦2026-09-29, `useTrackUpLock` ✦2026-09-29, `dofQuality` ✦2026-09-29, `dofBlur` ✦2026-09-29, `speedBlurStrength` ✦2026-09-29, `speedBlurMaxSpeed` ✦2026-09-29, `speedOverride` ✦2026-09-29, `cameraSpeed` (só leitura) ✦2026-09-29, `directionalBlurStrength` ✦2026-09-29, `directionalBlurMax` ✦2026-09-29, `catEyeStrength` ✦2026-09-29, `chromaticStrength` ✦2026-09-29, `vignetteStrength` ✦2026-09-29, `vignetteRadius` ✦2026-09-29, `fisheyeStrength` ✦2026-09-29, `shakeAmplitude` ✦2026-09-29, `shakeFrequency` ✦2026-09-29, `shakeDecay` ✦2026-09-29, `shakeTrauma` (só leitura) ✦2026-09-29
- **KX_ChangeColorActuator** (source/source/gameengine/Ketsji/KX_ChangeColorActuator.cpp): `useLerp`, `lerp`, `color`
- **KX_FontObject** (source/source/gameengine/Ketsji/KX_FontObject.cpp): `useShadows`, `shadowOffset`, `shadowColor`
- **KX_GameActuator** (source/source/gameengine/Ketsji/KX_GameActuator.cpp): `saveLocation`, `extensionName`
- **KX_GameObject** (source/source/gameengine/Ketsji/KX_GameObject.cpp): `setCcdMotionThreshold`, `setCcdSweptSphereRadius`, `setSoftLinearStiffness`, `setSoftAngularStiffness`, `setSoftVolume`, `setSoftVsRigidHardness`, `setSoftVsKineticHardness`, `setSoftVsSoftHardness`, `setSoftVsRigidImpulseSplitCluster`, `setSoftVsKineticImpulseSplitCluster`, `setSoftVsSoftImpulseSplitCluster`, `setSoftVelocitiesCorrectionFactor`, `setSoftDampingCoefficient`, `setSoftDragCoefficient`, `setSoftLiftCoefficient`, `setSoftPressureCoefficient`, `setSoftVolumeConversationCoefficient`, `setSoftDynamicFrictionCoefficient`, `setSoftPoseMatchingCoefficient`, `setSoftRigidContactsHardness`, `setSoftKineticContactsHardness`, `setSoftContactsHardness`, `setSoftAnchorsHardness`, `setSoftVelocitySolverIterations`, `setSoftPositionSolverIterations`, `setSoftDriftSolverIterations`, `setSoftClusterSolverIterations`, `setSoftPoseMatching`, `lookAt`, `setHalfAnimations`, `suspendAnimations` ✦2026-09-16, `resumeAnimations` ✦2026-09-16, `getVehicle`, `getVehicleSteeringWheel`, `getVehicleMaxTorque`, `getVehicleMaxRPM`, `getVehicleGearRatios`, `getVehicleGearboxType`, `getTurnTo`, `strikeLightning`, `setActionLayerWeight`, `setActionLayerSpeed`, `animationEventManager` (só leitura), `parentRecursive` (só leitura), `anisotropicFriction` ✦2026-10-04, `anisotropicFrictionCoefficients` ✦2026-10-04, `isDeformable` (só leitura) ✦2026-10-09, `fragments` ✦2026-10-09, `burstSpeed` ✦2026-10-09, `debrisLifetime` ✦2026-10-09, `useBreakOnCollision` ✦2026-10-09, `useInheritVelocity` ✦2026-10-09, `impactImpulse` ✦2026-10-09, `useExplodeOnImpact` ✦2026-10-09, `useChainReaction` ✦2026-10-09, `dentImpulse` ✦2026-10-09, `useDentOnCollision` ✦2026-10-09, `bendAxis` ✦2026-10-09, `bendAngle` ✦2026-10-09, `bendMaxAngle` ✦2026-10-09, `decal` ✦2026-10-09, `decalSize` ✦2026-10-09, `decalLife` ✦2026-10-09, `maxDecals` ✦2026-10-09, `passIndex`, `linearVelocity`, `angularVelocity`, `activitycullingdistance` (só leitura), `particles` (só leitura)
- **KX_InputSystem** (source/source/gameengine/Ketsji/KX_InputSystem.cpp): `reloadInputMaps`, `changeKeyMap`, `changeSensitivity`, `changeJoystickIndex`, `inputMaps` (só leitura)
- **KX_InputTable** (source/source/gameengine/Ketsji/KX_InputTable.cpp): `released` (só leitura), `active` (só leitura), `activated` (só leitura), `values` (só leitura)
- **KX_LightObject** (source/source/gameengine/Ketsji/KX_LightObject.cpp): `autoShadowUpdate` ✦2026-10-07
- **KX_LightningActuator** (source/source/gameengine/Ketsji/KX_LightningActuator.cpp): `bolt` ✦2026-10-03
- **KX_LodManager** (source/source/gameengine/Ketsji/KX_LodManager.cpp): `updatePhysics`
- **KX_Mesh** (source/source/gameengine/Ketsji/KX_Mesh.cpp): `destruct`
- **KX_MeshBuilder** (source/source/gameengine/Ketsji/KX_MeshBuilder.cpp): `FromMesh`, `addSlot`, `finish`, `slots` (só leitura)
- **KX_MeshBuilderSlot** (source/source/gameengine/Ketsji/KX_MeshBuilder.cpp): `addVertex`, `addIndex`, `removeVertex`, `addPrimitiveIndex`, `removePrimitiveIndex`, `addTriangleIndex`, `removeTriangleIndex`, `recalculateNormals`, `vertices` (só leitura), `indices` (só leitura), `triangleIndices` (só leitura), `material`, `uvCount` (só leitura), `colorCount` (só leitura), `primitive` (só leitura)
- **KX_MovementSensor** (source/source/gameengine/Ketsji/KX_MovementSensor.cpp): `threshold`, `axis`
- **KX_ParticleSystem** (source/source/gameengine/Ketsji/KX_ParticleSystem.cpp): `gravity`, `lifetime`, `emitterPosition`, `emitterRadius`, `velocity`, `velocityRandomness`, `size`, `color`, `particleCount`, `texture`, `endColor`, `endSize`, `emissionDirection`, `emissionAngle`, `debugUI` (só leitura), `enabled`, `collisionMode`, `collisionHeight`, `collisionBounce`, `collisionFriction`, `fragmentShaderPath`
- **KX_PythonJoystick** (source/source/gameengine/Ketsji/KX_PythonJoystick.cpp): `stopVibration`, `inputs` (só leitura), `duration`, `strengthLeft`, `strengthRight`, `isVibrating` (só leitura), `hasVibration` (só leitura)
- **KX_PythonMotion** (source/source/gameengine/Ketsji/KX_PythonMotion.cpp): `recenter` ✦2026-10-01, `headOrientation` (só leitura) ✦2026-10-01, `smoothing` ✦2026-10-01, `recenterTime` ✦2026-10-01
- **KX_PythonMouse** (source/source/gameengine/Ketsji/KX_PythonMouse.cpp): `reCenter`, `deltaPosition` (só leitura)
- **KX_RaySensor** (source/source/gameengine/Ketsji/KX_RaySensor.cpp): `gazeTime` ✦2026-10-01, `gazeAngle` ✦2026-10-01, `gazeProgress` (só leitura) ✦2026-10-01
- **KX_Scene** (source/source/gameengine/Ketsji/KX_Scene.cpp): `convertObject`, `play_cutscene`, `stop_cutscene`, `restart_cutscene`, `release_cutscene_trigger`, `unconvertedObjects` (só leitura) ✦2026-10-07, `speakers` (só leitura), `worldSun` (só leitura), `thread_logic_1`
- **KX_Speaker** (source/source/gameengine/Ketsji/KX_Speaker.cpp): `Play`, `Restart`, `Pause`, `Stop`, `SetSound`, `GetActiveEffect`, `GetActiveEffectFilter`, `SetEffect`, `RemoveEffect`, `is3D` (só leitura), `volume_maximum`, `volume_minimum`, `distance_reference`, `distance_maximum`, `attenuation`, `cone_angle_inner`, `cone_angle_outer`, `cone_volume_outer`, `sound`, `playbackManager`, `catkey`, `reverb_density`, `reverb_diffusion`, `reverb_gain`, `reverb_gain_hf`, `reverb_decay_time`, `reverb_decay_hf_ratio`, `reverb_reflections_gain`, `reverb_reflections_delay`, `reverb_late_reverb_gain`, `reverb_late_reverb_delay`, `reverb_air_absorption_gain_hf`, `reverb_room_rolloff_factor`, `reverb_decay_limit_hf`, `filter_gain`, `filter_gainlf`, `filter_gainhf`, `time`, `volume`, `pitch`, `mode`
- **KX_SteeringActuator** (source/source/gameengine/Ketsji/KX_SteeringActuator.cpp): `steeringVec` (só leitura), `facingMode`, `lockZVelocity`
- **KX_VRHeadSensor** (source/source/gameengine/Ketsji/KX_VRHeadSensor.cpp): `mode` ✦2026-10-01, `angle` ✦2026-10-01, `time` ✦2026-10-01, `pitch` (só leitura) ✦2026-10-01, `yaw` (só leitura) ✦2026-10-01, `roll` (só leitura) ✦2026-10-01
- **KX_VehicleWrapper** (source/source/gameengine/Ketsji/KX_VehicleWrapper.cpp): `setWheelIsDriveWheel`, `getCurrentSpeedKmh`, `getCurrentSpeedMps`, `getForwardVector`, `getCoordinateSystem`, `setCoordinateSystem`, `resetSuspension`, `getWheelConfig`, `getWheelState`, `savePreset`, `loadPreset`, `rebuildPreset`, `constraint_id` (só leitura), `constraint_type` (só leitura)
- **KX_WorldInfo** (source/source/gameengine/Ketsji/KX_WorldInfo.cpp): `getWeather` ✦2026-10-03, `backgroundColor`, `sunSize`, `skyType` ✦2026-10-09, `useSkyStars` ✦2026-10-09, `starStyle` ✦2026-10-09, `useSkyMoon` ✦2026-10-09, `moonSize` ✦2026-10-09, `moonBrightness` ✦2026-10-09, `useSkyAurora` ✦2026-10-09, `auroraColors` ✦2026-10-09, `atmosphereIntensity` ✦2026-10-09, `atmosphereRayleighColor` ✦2026-10-09, `atmosphereRayleighDensity` ✦2026-10-09, `atmosphereMieDensity` ✦2026-10-09, `atmosphereMieDirection` ✦2026-10-09, `atmosphereAltitude` ✦2026-10-09
- **SCA_DelaySensor** (source/source/gameengine/GameLogic/SCA_DelaySensor.cpp): `useDelta`
- **SCA_ISensor** (source/source/gameengine/GameLogic/SCA_ISensor.cpp): `useDeltaTime`
- **SCA_MouseSensor** (source/source/gameengine/GameLogic/SCA_MouseSensor.cpp): `holdTime` ✦2026-10-01
- **Texture** (source/source/gameengine/VideoTexture/Texture.cpp): `close`, `refresh`, `mipmap`, `source`, `bindId` (só leitura)
