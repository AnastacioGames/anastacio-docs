# Anastacio Engine - Referência da API Python

Versão em arquivo único da referência da API, para busca e IA local (RAG). Cada função e propriedade tem um título próprio.

123 pages, 2182 entries (functions, properties and constants).

## Índice

**Módulos**

- [Range.audio](#rangeaudio)
- [Range.constraints](#rangeconstraints)
- [Range.events](#rangeevents)
- [Range.imgui](#rangeimgui)
- [Range.logic](#rangelogic)
- [Range.network](#rangenetwork)
- [Range.network.steam](#rangenetworksteam)
- [Range.render](#rangerender)
- [Range.texture](#rangetexture)
- [Range.track](#rangetrack)

**Tipos**

- [BL_ActionActuator](#bl_actionactuator)
- [BL_ArmatureActuator](#bl_armatureactuator)
- [BL_ArmatureBone](#bl_armaturebone)
- [BL_ArmatureChannel](#bl_armaturechannel)
- [BL_ArmatureConstraint](#bl_armatureconstraint)
- [BL_ArmatureObject](#bl_armatureobject)
- [BL_Shader](#bl_shader)
- [BL_Texture](#bl_texture)
- [EXP_BaseListValue](#exp_baselistvalue)
- [EXP_BaseListWrapper](#exp_baselistwrapper)
- [EXP_ListValue](#exp_listvalue)
- [EXP_PropValue](#exp_propvalue)
- [EXP_PyObjectPlus](#exp_pyobjectplus)
- [EXP_Value](#exp_value)
- [KX_2DFilter](#kx_2dfilter)
- [KX_2DFilterManager](#kx_2dfiltermanager)
- [KX_2DFilterOffScreen](#kx_2dfilteroffscreen)
- [KX_AddObjectActuator](#kx_addobjectactuator)
- [KX_AnimationEvent](#kx_animationevent)
- [KX_AnimationEventManager](#kx_animationeventmanager)
- [KX_ArmatureSensor](#kx_armaturesensor)
- [KX_BatchGroup](#kx_batchgroup)
- [KX_BlenderMaterial](#kx_blendermaterial)
- [KX_BoundingBox](#kx_boundingbox)
- [KX_Camera](#kx_camera)
- [KX_CameraActuator](#kx_cameraactuator)
- [KX_ChangeColorActuator](#kx_changecoloractuator)
- [KX_CharacterWrapper](#kx_characterwrapper)
- [KX_CollisionContactPoint](#kx_collisioncontactpoint)
- [KX_CollisionSensor](#kx_collisionsensor)
- [KX_ConstraintActuator](#kx_constraintactuator)
- [KX_ConstraintWrapper](#kx_constraintwrapper)
- [KX_CubeMap](#kx_cubemap)
- [KX_DynamicActuator](#kx_dynamicactuator)
- [KX_EndObjectActuator](#kx_endobjectactuator)
- [KX_FontObject](#kx_fontobject)
- [KX_GameActuator](#kx_gameactuator)
- [KX_GameObject](#kx_gameobject)
- [KX_InputSystem](#kx_inputsystem)
- [KX_InputTable](#kx_inputtable)
- [KX_LibLoadStatus](#kx_libloadstatus)
- [KX_LightningActuator](#kx_lightningactuator)
- [KX_LightObject](#kx_lightobject)
- [KX_LodLevel](#kx_lodlevel)
- [KX_LodManager](#kx_lodmanager)
- [KX_Mesh](#kx_mesh)
- [KX_MeshBuilder](#kx_meshbuilder)
- [KX_MeshBuilderSlot](#kx_meshbuilderslot)
- [KX_MicrophoneSensor](#kx_microphonesensor)
- [KX_MouseActuator](#kx_mouseactuator)
- [KX_MouseFocusSensor](#kx_mousefocussensor)
- [KX_MovementSensor](#kx_movementsensor)
- [KX_NavMeshObject](#kx_navmeshobject)
- [KX_NearSensor](#kx_nearsensor)
- [KX_NetworkMessageActuator](#kx_networkmessageactuator)
- [KX_NetworkMessageSensor](#kx_networkmessagesensor)
- [KX_ObjectActuator](#kx_objectactuator)
- [KX_ParentActuator](#kx_parentactuator)
- [KX_ParticleSystem](#kx_particlesystem)
- [KX_PlanarMap](#kx_planarmap)
- [KX_PolyProxy](#kx_polyproxy)
- [KX_PythonComponent](#kx_pythoncomponent)
- [KX_PythonJoystick](#kx_pythonjoystick)
- [KX_PythonKeyboard](#kx_pythonkeyboard)
- [KX_PythonMotion](#kx_pythonmotion)
- [KX_PythonMouse](#kx_pythonmouse)
- [KX_RadarSensor](#kx_radarsensor)
- [KX_RaySensor](#kx_raysensor)
- [KX_ReplaceMeshActuator](#kx_replacemeshactuator)
- [KX_Scene](#kx_scene)
- [KX_SceneActuator](#kx_sceneactuator)
- [KX_SoundActuator](#kx_soundactuator)
- [KX_Speaker](#kx_speaker)
- [KX_StateActuator](#kx_stateactuator)
- [KX_SteeringActuator](#kx_steeringactuator)
- [KX_TextureRenderer](#kx_texturerenderer)
- [KX_TrackToActuator](#kx_tracktoactuator)
- [KX_VehicleWrapper](#kx_vehiclewrapper)
- [KX_VertexProxy](#kx_vertexproxy)
- [KX_VideoActuator](#kx_videoactuator)
- [KX_VisibilityActuator](#kx_visibilityactuator)
- [KX_VoiceActuator](#kx_voiceactuator)
- [KX_VRHeadSensor](#kx_vrheadsensor)
- [KX_WorldInfo](#kx_worldinfo)
- [SCA_2DFilterActuator](#sca_2dfilteractuator)
- [SCA_ActuatorSensor](#sca_actuatorsensor)
- [SCA_AlwaysSensor](#sca_alwayssensor)
- [SCA_ANDController](#sca_andcontroller)
- [SCA_AnimationEventSensor](#sca_animationeventsensor)
- [SCA_DelaySensor](#sca_delaysensor)
- [SCA_IActuator](#sca_iactuator)
- [SCA_IController](#sca_icontroller)
- [SCA_ILogicBrick](#sca_ilogicbrick)
- [SCA_InputEvent](#sca_inputevent)
- [SCA_IObject](#sca_iobject)
- [SCA_ISensor](#sca_isensor)
- [SCA_JoystickSensor](#sca_joysticksensor)
- [SCA_KeyboardSensor](#sca_keyboardsensor)
- [SCA_MouseSensor](#sca_mousesensor)
- [SCA_NANDController](#sca_nandcontroller)
- [SCA_NORController](#sca_norcontroller)
- [SCA_ORController](#sca_orcontroller)
- [SCA_PropertyActuator](#sca_propertyactuator)
- [SCA_PropertySensor](#sca_propertysensor)
- [SCA_PythonController](#sca_pythoncontroller)
- [SCA_RandomActuator](#sca_randomactuator)
- [SCA_RandomSensor](#sca_randomsensor)
- [SCA_VibrationActuator](#sca_vibrationactuator)
- [SCA_WaitActuator](#sca_waitactuator)
- [SCA_XNORController](#sca_xnorcontroller)
- [SCA_XORController](#sca_xorcontroller)
- [Texture](#texture)
- [TrackLine](#trackline)

---

# Módulos

---

## Range.audio

Módulo `Range.audio` da Anastacio Engine. Também acessível como `bge.audio`.

```python
# Liga o microfone e lê o nível da voz.
import Range

if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

print("Voice:", Range.audio.microphoneLevel())
```

```python
# Grava a voz e toca de volta com efeito de robô.
import Range

Range.audio.microphoneRecordStart()

# Depois, quando o jogador parar de falar.
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

```python
# Controla um módulo do World Sound pelo nome.
import Range

Range.audio.play("Music", fade=2.0)
Range.audio.setVolume("Music", 0.5)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### edit(sound, start=0, end=-1, fade_in=0, fade_out=0, normalize=False)

*(novo na Anastacio)* `função`

Corta, aplica fades e normaliza um som; igual a `aud.edit`.

**Retorna:** `aud.Sound`

#### getVolume(module)

*(novo na Anastacio)* `função`

Volume do módulo; `None` se ele não existe.

**Retorna:** `float`

#### isLive()

*(novo na Anastacio)* `função`

`True` enquanto o microfone está sendo ouvido.

**Retorna:** `bool`

#### isPlaying(module)

*(novo na Anastacio)* `função`

`True` enquanto um som do módulo toca.

**Retorna:** `bool`

#### microphone()

*(novo na Anastacio)* `função`

O `aud.Microphone` em uso, para uso avançado; `None` antes de ligar.

**Retorna:** `aud.Microphone`

#### microphoneDropped()

*(novo na Anastacio)* `função`

Quantas vezes o áudio se perdeu porque o jogo travou.

**Retorna:** `int`

#### microphoneError()

*(novo na Anastacio)* `função`

Motivo de o microfone não ter aberto.

**Retorna:** `str`

#### microphoneIsRecording()

*(novo na Anastacio)* `função`

`True` enquanto grava.

**Retorna:** `bool`

#### microphoneLevel()

*(novo na Anastacio)* `função`

Nível da voz agora, de 0 a 1.

**Retorna:** `float`

#### microphonePeak()

*(novo na Anastacio)* `função`

Pico com queda lenta, de 0 a 1.

**Retorna:** `float`

#### microphoneRecordingSeconds()

*(novo na Anastacio)* `função`

Duração da gravação em andamento, em segundos.

**Retorna:** `float`

#### microphoneRecordStart()

*(novo na Anastacio)* `função`

Começa a gravar.

#### microphoneRecordStop(slot="last")

*(novo na Anastacio)* `função`

Para e guarda a gravação com o nome `slot`. Retorna o `aud.Sound` ou `None`.

**Retorna:** `aud.Sound`

#### microphoneSave(slot, path)

*(novo na Anastacio)* `função`

Salva uma gravação em WAV. Caminho relativo vai para a pasta do jogo (Web: `/saves`).

#### microphoneStart(device="")

*(novo na Anastacio)* `função`

Liga o microfone. Na Web, chame depois de um clique ou toque. `False` se não abrir.

**Retorna:** `bool`

#### microphoneState()

*(novo na Anastacio)* `função`

Estado do microfone: `'closed'`, `'pending'`, `'granted'`, `'denied'` ou `'error'`.

**Retorna:** `str`

#### microphoneStop()

*(novo na Anastacio)* `função`

Desliga o microfone.

#### modules()

*(novo na Anastacio)* `função`

Nomes dos módulos do World Sound carregados até agora.

**Retorna:** `list`

#### next(module)

*(novo na Anastacio)* `função`

Music: passa para a próxima faixa.

#### pause(module)

*(novo na Anastacio)* `função`

Pausa todos os sons do módulo onde estão.

#### play(module, sound="", fade=-1.0)

*(novo na Anastacio)* `função`

Toca um som de um módulo do World Sound, ou retoma o módulo pausado. Sem `sound`, Music toca a faixa atual e Ambient toca todas as camadas. `fade` em segundos; negativo usa o Fade do módulo. `False` se o módulo ou o som não existe.

**Retorna:** `bool`

#### playing(module)

*(novo na Anastacio)* `função`

Nomes dos sons tocando agora (Music: a faixa atual).

**Retorna:** `list`

#### playLive(effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(novo na Anastacio)* `função`

Faz ouvir o microfone agora, com efeito de voz. Só um por vez; chamar de novo troca o efeito. Use fones: caixas de som realimentam o microfone.

#### playVoice(sound, effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(novo na Anastacio)* `função`

Toca uma gravação (nome ou `aud.Sound`) com efeito de voz; veja `voicePresets()`. `reverb=True` usa o reverb da área ou do World. `False` se a gravação ou o efeito não existe.

**Retorna:** `bool`

#### previous(module)

*(novo na Anastacio)* `função`

Music: volta para a faixa anterior.

#### recording(slot)

*(novo na Anastacio)* `função`

O `aud.Sound` de uma gravação, ou `None`.

**Retorna:** `aud.Sound`

#### recordings()

*(novo na Anastacio)* `função`

Nomes das gravações guardadas até agora.

**Retorna:** `list`

#### resume(module)

*(novo na Anastacio)* `função`

Continua de onde `pause(module)` parou.

#### setRecording(slot, sound)

*(novo na Anastacio)* `função`

Guarda um `aud.Sound` com um nome. `None` remove.

#### setVolume(module, volume)

*(novo na Anastacio)* `função`

Define o volume do módulo, de 0.0 a 1.0.

#### sounds(module)

*(novo na Anastacio)* `função`

Nomes dos sons do módulo.

**Retorna:** `list`

#### stop(module, sound="", fade=-1.0)

*(novo na Anastacio)* `função`

Para um módulo do World Sound, ou só um dos sons dele. `fade` em segundos; negativo usa o Fade do módulo.

#### stopLive()

*(novo na Anastacio)* `função`

Para de ouvir o microfone.

#### voiceFx(sound, preset, amount=1.0)

*(novo na Anastacio)* `função`

Aplica um efeito de voz; igual a `aud.voice_fx`.

**Retorna:** `aud.Sound`

#### voicePresets(live=False)

*(novo na Anastacio)* `função`

Nomes dos efeitos de voz.

**Retorna:** `list`

---

## Range.constraints

> **Veja também:**
[`KX_VehicleWrapper`](#kx_vehiclewrapper), [`KX_CharacterWrapper`](#kx_characterwrapper), [`KX_ConstraintWrapper`](#kx_constraintwrapper)

A Bullet Physics cuida da detecção de colisão e da dinâmica de corpos rígidos da game engine.

Recursos:

- Simulação de veículos.
- Constraints de corpo rígido: hinge e ponto a ponto (ball socket).
- Acesso às configurações internas da física,
como o tempo de desativação, e recursos de depuração

> **Note:**
Como esta API não é bem documentada, pode não ficar claro que valores usar nos parâmetros. Em geral, os amortecimentos devem ficar entre 0 e 1 e as rigidezes não devem passar muito de 10.

```python
# Liga dois objetos com uma dobradiça.
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
frame = scene.objects["Frame"]

hinge = constraints.createConstraint(
    door.getPhysicsId(), frame.getPhysicsId(),
    constraints.LINEHINGE_CONSTRAINT,
    0.0, 0.0, 1.0)
```

```python
# Muda a gravidade do mundo e a qualidade do solver.
from Range import constraints

constraints.setGravity(0.0, 0.0, -3.7)
constraints.setNumIterations(20)
```

```python
# Mostra as formas de colisão durante os testes.
from Range import constraints

constraints.setDebugMode(constraints.DBG_DRAWWIREFRAME)
```

```python
# Remove uma constraint pelo id.
from Range import constraints

constraints.removeConstraint(hinge.constraint_id)
```

### Exemplos

> **Tip:**
Para mais exemplos da física Bullet e de como usá-la, veja o [fórum do pybullet](https://pybullet.org/Bullet/phpBB3/viewforum.php?f=17)_.

### Funções

#### createConstraint( \

physicsid_1, physicsid_2, constraint_type, \ pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, \ axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0)

Cria uma constraint.

- **`physicsid_1`**: O physics id do primeiro objeto da constraint.
  - tipo: int
- **`physicsid_2`**: O physics id do segundo objeto da constraint.
  - tipo: int
- **`constraint_type`**: O tipo da constraint; veja `Create Constraint Constants`_.
  - tipo: int
- **`pivot_x`**: Posição X do pivô (opcional).
  - tipo: float
- **`pivot_y`**: Posição Y do pivô (opcional).
  - tipo: float
- **`pivot_z`**: Posição Z do pivô (opcional).
  - tipo: float
- **`axis_x`**: Ângulo do eixo X em graus (opcional).
  - tipo: float
- **`axis_y`**: Ângulo do eixo Y em graus (opcional).
  - tipo: float
- **`axis_z`**: Ângulo do eixo Z em graus (opcional).
  - tipo: float
- **`flag`**: 128 para desligar a colisão entre os corpos ligados (opcional).
  - tipo: int

**Retorna:** Um wrapper de constraint.

**Tipo do retorno:** `KX_ConstraintWrapper`

#### createVehicle(physicsid)

Cria uma constraint de veículo.

- **`physicsid`**: O physics id do objeto chassi da constraint.
  - tipo: int

**Retorna:** Um wrapper de constraint de veículo.

**Tipo do retorno:** `KX_VehicleWrapper`

#### exportBulletFile(filename)

Exporta um arquivo que representa o mundo da dinâmica (em geral com extensão `.bullet`).

Veja [Bullet binary serialization](http://bulletphysics.org/mediawiki-1.5.8/index.php/Bullet_binary_serialization)_.

- **`filename`**: Caminho do arquivo.
  - tipo: str

#### getAppliedImpulse(constraintId)

- **`constraintId`**: O id da constraint.
  - tipo: int

**Retorna:** O último impulso aplicado.

**Tipo do retorno:** float

#### getVehicleConstraint(constraintId)

- **`constraintId`**: O id da constraint de veículo.
  - tipo: int

**Retorna:** Um objeto de constraint de veículo.

**Tipo do retorno:** `KX_VehicleWrapper`

#### getCharacter(gameobj)

- **`gameobj`**: O game object com a física de personagem.
  - tipo: `KX_GameObject`

**Retorna:** Wrapper de personagem.

**Tipo do retorno:** `KX_CharacterWrapper`

#### removeConstraint(constraintId)

Remove uma constraint.

- **`constraintId`**: O id da constraint a remover.
  - tipo: int

#### setCcdMode(ccdMode)

> **Note:**
Muito experimental, não recomendado

Define o modo de CCD (detecção contínua de colisão) no ambiente de física.

- **`ccdMode`**: O novo modo de CCD.
  - tipo: int

#### setContactBreakingTreshold(breakingTreshold)

> **Note:**
Um padrão razoável é 0.02 (se as unidades forem metros)

Define limites ligados ao gerenciamento de pontos de contato.

- **`breakingTreshold`**: O novo limite de quebra de contato.
  - tipo: float

#### setDeactivationAngularTreshold(angularTreshold)

Define o limite de velocidade angular.

- **`angularTreshold`**: Novo limite angular de desativação.
  - tipo: float

#### setDeactivationLinearTreshold(linearTreshold)

Define o limite de velocidade linear.

- **`linearTreshold`**: Novo limite linear de desativação.
  - tipo: float

#### setDeactivationTime(time)

Define o tempo depois do qual um corpo rígido parado é desativado.

- **`time`**: O tempo de desativação.
  - tipo: float

#### setDebugMode(mode)

Define o modo de depuração.

- **`mode`**: O novo modo de depuração; veja `Debug Mode Constants`_.
  - tipo: int

#### setGravity(x, y, z)

Define a força da gravidade.

- **`x`**: Força da gravidade em X.
  - tipo: float
- **`y`**: Força da gravidade em Y.
  - tipo: float
- **`z`**: Força da gravidade em Z.
  - tipo: float

#### setLinearAirDamping(damping)

> **Note:**
Não implementado

Define o amortecimento linear do ar para corpos rígidos.

#### setNumIterations(numiter)

Define o número de iterações de um solver de constraints iterativo.

- **`numiter`**: Novo número de iterações.
  - tipo: int

#### setLinearSlop(slop)

Define a tolerância de penetração de contato da cena de física ativa. Um valor positivo deixa os objetos se sobreporem até `slop` unidades do Blender antes de o solver do Bullet aplicar a correção de posição. O padrão é `0.0`.

É uma configuração do solver para a cena inteira: afeta todos os contatos físicos da cena ativa. Não muda a margem de colisão de um objeto nem o ponto em que as colisões são detectadas. Use valores pequenos, adequados à escala da cena.

- **`slop`**: Tolerância de penetração em unidades do Blender. Use um valor finito e não negativo.
  - tipo: float

#### setNumTimeSubSteps(numsubstep)

Define o número de substeps de cada passo da física. Troca qualidade por desempenho.

- **`numsubstep`**: Novo número de substeps.
  - tipo: int

#### setSolverDamping(damping)

> **Note:**
Muito experimental, não recomendado

Define a constante de amortecimento de um solver baseado em penalidade.

- **`damping`**: Novo amortecimento do solver.
  - tipo: float

#### setSolverTau(tau)

> **Note:**
Muito experimental, não recomendado

Define a constante de mola de um solver baseado em penalidade.

- **`tau`**: Novo tau do solver.
  - tipo: float

#### setSolverType(solverType)

> **Note:**
Muito experimental, não recomendado

Define o tipo do solver.

- **`solverType`**: O novo tipo do solver.
  - tipo: int

#### setSorConstant(sor)

> **Note:**
Muito experimental, não recomendado

Define a constante de sobre-relaxação sucessiva.

- **`sor`**: Novo valor de sor.
  - tipo: float

#### setUseEpa(epa)

> **Note:**
Não implementado

### Constantes

#### error

String constante simbólica que indica erro.

**Tipo:** str

### Constantes de modo de depuração

Modo de depuração a usar com `setDebugMode`.

#### DBG_NODEBUG

Sem depuração.

#### DBG_DRAWWIREFRAME

Desenha wireframe na depuração.

#### DBG_DRAWAABB

Desenha a Axis Aligned Bounding Box na depuração.

#### DBG_DRAWFREATURESTEXT

Desenha o texto dos recursos na depuração.

#### DBG_DRAWCONTACTPOINTS

Desenha os pontos de contato na depuração.

#### DBG_NOHELPTEXT

Depuração sem texto de ajuda.

#### DBG_DRAWTEXT

Desenha texto na depuração.

#### DBG_PROFILETIMINGS

Desenha os tempos de profile na depuração.

#### DBG_ENABLESATCOMPARISION

Liga a comparação sat na depuração.

#### DBG_DISABLEBULLETLCP

Desliga o LCP do Bullet.

#### DBG_ENABLECCD

Liga a detecção contínua de colisão na depuração.

#### DBG_DRAWCONSTRAINTS

Desenha as constraints na depuração.

#### DBG_DRAWCONSTRAINTLIMITS

Desenha os limites das constraints na depuração.

#### DBG_FASTWIREFRAME

Desenha um wireframe rápido na depuração.

### Constantes de criação de constraint

Tipo de constraint a usar com `createConstraint`.

#### POINTTOPOINT_CONSTRAINT

.. to do

#### LINEHINGE_CONSTRAINT

.. to do

#### ANGULAR_CONSTRAINT

.. to do

#### CONETWIST_CONSTRAINT

.. to do

#### VEHICLE_CONSTRAINT

.. to do

#### GENERIC_6DOF_CONSTRAINT

.. to do

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### setErp(value)

 `função`

ERP do solver de física: quanto da penetração entre objetos é corrigida por passo (padrão 0.2).

#### setErp2(value)

 `função`

ERP usado com o split impulse (padrão 0.8).

#### setGlobalCfm(value)

 `função`

CFM global: deixa contatos e juntas mais "macios" (padrão 0.0).

#### setMaxGyroscopicForce(value)

 `função`

Limite da força giroscópica (só no modo explícito).

#### setSplitImpulse(enabled)

 `função`

Resolve posição e velocidade dos contatos separadamente. Evita objetos "pulando" ao se separar.

#### setSplitImpulsePenetrationThreshold(value)

 `função`

Penetração a partir da qual o split impulse é usado (padrão -0.04).

#### setSplitImpulseTurnErp(value)

 `função`

Correção de rotação do split impulse (padrão 0.1).

#### setWarmstartingFactor(value)

 `função`

Quanto o solver reaproveita o resultado do frame anterior (0.0 a 1.0).

---

## Range.events

> **Veja também:**
[`KX_PythonKeyboard`](#kx_pythonkeyboard), [`KX_PythonMouse`](#kx_pythonmouse), [`SCA_InputEvent`](#sca_inputevent), [`SCA_KeyboardSensor`](#sca_keyboardsensor)

```python
# Faz algo uma vez só, no quadro em que a tecla foi apertada.
import Range

keys = Range.logic.keyboard.inputs

if keys[Range.events.SPACEKEY].activated:
    print("Jump")
```

```python
# Lê os botões do mouse do mesmo jeito.
import Range

buttons = Range.logic.mouse.inputs

if buttons[Range.events.LEFTMOUSE].active:
    print("Shooting")
```

```python
# Mostra o nome de cada tecla pressionada.
import Range

for code in Range.logic.keyboard.activeInputs:
    print(Range.events.EventToString(code))
```

### Introdução

Este módulo guarda as constantes de teclas usadas pelo SCA_KeyboardSensor.

```python

# Configura um sensor de teclado conectado para aceitar F1
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' é um sensor de teclado
sensor = co.sensors["Keyboard"]
sensor.key = Range.events.F1KEY
```

```python

# Faz o esquema de todas as teclas
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' é um sensor de teclado
sensor = co.sensors["Keyboard"]

for key, input in sensor.inputs:
	# key[0] == Range.events.keycode = event.type, key[1] = input
	if Range.logic.KX_INPUT_JUST_ACTIVATED in input.queue:
		if key == Range.events.WKEY:
			# Ativa para a frente!
		if key == Range.events.SKEY:
			# Ativa para trás!
		if key == Range.events.AKEY:
			# Ativa para a esquerda!
		if key == Range.events.DKEY:
			# Ativa para a direita!
```

```python

# O esquema de todas as teclas sem sensor de teclado (mas você vai
# precisar de um sensor Always com o modo pulse ligado)
import Range

# Só encurtando os nomes aqui
keyboard = Range.logic.keyboard
JUST_ACTIVATED = Range.logic.KX_INPUT_JUST_ACTIVATED

if JUST_ACTIVATED in keyboard.inputs[Range.events.WKEY].queue:
	print("Activate Forward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.SKEY].queue:
	print("Activate Backward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.AKEY].queue:
	print("Activate Left!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.DKEY].queue:
	print("Activate Right!")
```

### Funções

#### EventToString(event)

Devolve o nome em texto de um evento de tecla. Gera ValueError se o evento for inválido.

- **`event`**: Constante de evento de tecla de `Range.events` ou do sensor de teclado.
  - tipo: int

**Tipo do retorno:** string

#### EventToCharacter(event, shift)

Devolve o nome em texto de um evento de tecla. Devolve um texto vazio se o evento não puder virar um caractere.

  - tipo: int
- **`event`**: Constante de evento de tecla de `Range.events` ou do sensor de teclado.
  - tipo: bool
- **`shift`**: Defina como true se o shift estiver apertado.

**Tipo do retorno:** string

### Teclas (constantes)

### Teclas do mouse

#### LEFTMOUSE

Botão esquerdo do mouse.

#### MIDDLEMOUSE

Botão do meio do mouse (clique na rodinha).

#### RIGHTMOUSE

Botão direito do mouse.

#### WHEELUPMOUSE

Rodinha do mouse girando para cima.

#### WHEELDOWNMOUSE

Rodinha do mouse girando para baixo.

#### LEFTTHUMBMOUSE

Botão lateral de trás do mouse (voltar).

#### RIGHTTHUMBMOUSE

Botão lateral da frente do mouse (avançar).

#### BUTTON6MOUSE

Botão extra 6 do mouse.

#### BUTTON7MOUSE

Botão extra 7 do mouse.

#### MOUSEX

Movimento horizontal do mouse.

#### MOUSEY

### Teclas do teclado

### Letras

#### AKEY

Tecla A.

#### BKEY

Tecla B.

#### CKEY

Tecla C.

#### DKEY

Tecla D.

#### EKEY

Tecla E.

#### FKEY

Tecla F.

#### GKEY

Tecla G.

#### HKEY

Tecla H.

#### IKEY

Tecla I.

#### JKEY

Tecla J.

#### KKEY

Tecla K.

#### LKEY

Tecla L.

#### MKEY

Tecla M.

#### NKEY

Tecla N.

#### OKEY

Tecla O.

#### PKEY

Tecla P.

#### QKEY

Tecla Q.

#### RKEY

Tecla R.

#### SKEY

Tecla S.

#### TKEY

Tecla T.

#### UKEY

Tecla U.

#### VKEY

Tecla V.

#### WKEY

Tecla W.

#### XKEY

Tecla X.

#### YKEY

Tecla Y.

#### ZKEY

### Números

#### ZEROKEY

Tecla 0 da fileira de números (não a do teclado numérico).

#### ONEKEY

Tecla 1 da fileira de números (não a do teclado numérico).

#### TWOKEY

Tecla 2 da fileira de números (não a do teclado numérico).

#### THREEKEY

Tecla 3 da fileira de números (não a do teclado numérico).

#### FOURKEY

Tecla 4 da fileira de números (não a do teclado numérico).

#### FIVEKEY

Tecla 5 da fileira de números (não a do teclado numérico).

#### SIXKEY

Tecla 6 da fileira de números (não a do teclado numérico).

#### SEVENKEY

Tecla 7 da fileira de números (não a do teclado numérico).

#### EIGHTKEY

Tecla 8 da fileira de números (não a do teclado numérico).

#### NINEKEY

### Teclas modificadoras

#### CAPSLOCKKEY

Tecla Caps Lock.

#### LEFTCTRLKEY

Tecla Ctrl da esquerda.

#### LEFTALTKEY

Tecla Alt da esquerda.

#### RIGHTALTKEY

Tecla Alt da direita (AltGr).

#### RIGHTCTRLKEY

Tecla Ctrl da direita.

#### RIGHTSHIFTKEY

Tecla Shift da direita.

#### LEFTSHIFTKEY

### Setas

#### LEFTARROWKEY

Seta para a esquerda.

#### DOWNARROWKEY

Seta para baixo.

#### RIGHTARROWKEY

Seta para a direita.

#### UPARROWKEY

### Teclado numérico

#### PAD0

Tecla 0 do teclado numérico.

#### PAD1

Tecla 1 do teclado numérico.

#### PAD2

Tecla 2 do teclado numérico.

#### PAD3

Tecla 3 do teclado numérico.

#### PAD4

Tecla 4 do teclado numérico.

#### PAD5

Tecla 5 do teclado numérico.

#### PAD6

Tecla 6 do teclado numérico.

#### PAD7

Tecla 7 do teclado numérico.

#### PAD8

Tecla 8 do teclado numérico.

#### PAD9

Tecla 9 do teclado numérico.

#### PADPERIOD

Tecla ponto do teclado numérico.

#### PADSLASHKEY

Tecla / do teclado numérico.

#### PADASTERKEY

Tecla * do teclado numérico.

#### PADMINUS

Tecla - do teclado numérico.

#### PADENTER

Tecla Enter do teclado numérico.

#### PADPLUSKEY

### Teclas de função

#### F1KEY

Tecla F1.

#### F2KEY

Tecla F2.

#### F3KEY

Tecla F3.

#### F4KEY

Tecla F4.

#### F5KEY

Tecla F5.

#### F6KEY

Tecla F6.

#### F7KEY

Tecla F7.

#### F8KEY

Tecla F8.

#### F9KEY

Tecla F9.

#### F10KEY

Tecla F10.

#### F11KEY

Tecla F11.

#### F12KEY

Tecla F12.

#### F13KEY

Tecla F13.

#### F14KEY

Tecla F14.

#### F15KEY

Tecla F15.

#### F16KEY

Tecla F16.

#### F17KEY

Tecla F17.

#### F18KEY

Tecla F18.

#### F19KEY

### Outras teclas

#### ACCENTGRAVEKEY

Tecla acento grave (`).

#### BACKSLASHKEY

Tecla barra invertida (\).

#### BACKSPACEKEY

Tecla Backspace.

#### COMMAKEY

Tecla vírgula (,).

#### DELKEY

Tecla Delete.

#### ENDKEY

Tecla End.

#### EQUALKEY

Tecla igual (=).

#### ESCKEY

Tecla Esc.

#### HOMEKEY

Tecla Home.

#### INSERTKEY

Tecla Insert.

#### LEFTBRACKETKEY

Tecla colchete esquerdo ([).

#### LINEFEEDKEY

Tecla Line Feed (rara em teclados atuais).

#### MINUSKEY

Tecla menos (-).

#### PAGEDOWNKEY

Tecla Page Down.

#### PAGEUPKEY

Tecla Page Up.

#### PAUSEKEY

Tecla Pause.

#### PERIODKEY

Tecla ponto (.).

#### QUOTEKEY

Tecla aspas (').

#### RIGHTBRACKETKEY

Tecla colchete direito (]).

#### RETKEY (Deprecated: use bge.events.ENTERKEY)

#### ENTERKEY

Tecla Enter.

#### SEMICOLONKEY

Tecla ponto e vírgula (;).

#### SLASHKEY

Tecla barra (/).

#### SPACEKEY

Barra de espaço.

#### TABKEY

Tecla Tab.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### JOYSTICKA

 `constante`

Botão A do controle.

#### JOYSTICKB

 `constante`

Botão B do controle.

#### JOYSTICKBACK

 `constante`

Botão Back/Select do controle.

#### JOYSTICKGUIDE

 `constante`

Botão Guide (botão central) do controle.

#### JOYSTICKLEFTSHOUDER

 `constante`

Botão ombro esquerdo (LB) do controle.

#### JOYSTICKLEFTSTICK

 `constante`

Botão clique do analógico esquerdo do controle.

#### JOYSTICKPADDOWN

 `constante`

Botão direcional para baixo do controle.

#### JOYSTICKPADLEFT

 `constante`

Botão direcional para a esquerda do controle.

#### JOYSTICKPADRIGHT

 `constante`

Botão direcional para a direita do controle.

#### JOYSTICKPADUP

 `constante`

Botão direcional para cima do controle.

#### JOYSTICKRIGHTSHOUDER

 `constante`

Botão ombro direito (RB) do controle.

#### JOYSTICKRIGHTSTICK

 `constante`

Botão clique do analógico direito do controle.

#### JOYSTICKX

 `constante`

Botão X do controle.

#### JOYSTICKY

 `constante`

Botão Y do controle.

#### OSKEY

 `constante`

Tecla do sistema (Windows/Command).

---

## Range.imgui

> **Veja também:**
[`Range.render`](#rangerender), [`Range.logic`](#rangelogic)

Módulo `Range.imgui` da Anastacio Engine. Também acessível como `bge.imgui`.

```python
# Uma janela de pausa, desenhada a cada quadro por um componente.
import Range
import Range.imgui as imgui

class PauseMenu(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.volume = 0.5
        imgui.set_game_ui_open(True)

    def update(self):
        w, h = imgui.get_display_size()
        imgui.set_next_window_size(300, 200, imgui.COND_FIRST_USE_EVER)
        imgui.set_next_window_pos(w / 2 - 150, h / 2 - 100)

        is_open, want_close = imgui.begin("Pause", closable=True)
        if is_open:
            changed, self.volume = imgui.slider_float("Volume", self.volume, 0.0, 1.0)
            imgui.separator()
            if imgui.button("Quit", width=240):
                Range.logic.endGame()
        imgui.end()
```

```python
# Os widgets comuns retornam se mudaram e o novo valor.
changed, self.fullscreen = imgui.checkbox("Full screen", self.fullscreen)
changed, self.quality = imgui.slider_int("Quality", self.quality, 0, 3)
imgui.same_line()
imgui.text("Level: {}".format(self.quality))
```

```python
# Muda a cor de um botão.
imgui.push_style_color(imgui.COL_BUTTON, 0.8, 0.2, 0.2, 1.0)
imgui.button("Delete save")
imgui.pop_style_color()
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### begin(name, closable=False)

 `função`

Abre uma janela com o título `name`. Tudo que você desenhar até `end()` fica dentro dela. Com `closable=True` a janela ganha o botão X, e `want_close` vira True quando ele é clicado. Sempre chame `end()` depois, mesmo se `is_open` for False.

**Retorna:** `(is_open, want_close)`

#### begin_popup_modal(name, closable=False)

 `função`

Desenha o popup modal aberto antes com `open_popup(name)`. Só chame `end_popup()` quando `is_open` for True.

**Retorna:** `(is_open, want_close)`

#### button(label, width=0, height=0)

 `função`

Botão com o texto `label`. Devolve True no quadro em que é clicado. Largura e altura 0 ajustam ao texto.

**Retorna:** `bool`

#### checkbox(label, value)

 `função`

Caixa de marcar. Passe o valor atual em `value` e guarde `new_value`; `changed` é True quando o jogador clicou.

**Retorna:** `(changed, new_value)`

#### close_current_popup()

 `função`

Fecha o popup aberto.

#### color_edit3(label, r, g, b)

 `função`

Seletor de cor RGB (valores de 0 a 1). Devolve a cor nova.

**Retorna:** `(changed, r, g, b)`

#### color_edit4(label, r, g, b, a)

 `função`

Seletor de cor RGBA com transparência (valores de 0 a 1).

**Retorna:** `(changed, r, g, b, a)`

#### combo(label, current_item, items)

 `função`

Lista suspensa. `items` é uma lista de textos e `current_item` o índice escolhido.

**Retorna:** `(changed, new_item)`

#### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 `função`

-- desenhado acima de todas as janelas, para fades

#### end()

 `função`

Fecha a janela começada com `begin()`.

#### end_popup()

 `função`

Fecha o bloco de um popup.

#### get_cursor_pos()

 `função`

Posição onde o próximo item será desenhado, relativa à janela atual.

**Retorna:** `(x, y)`

#### get_cursor_screen_pos()

 `função`

Posição onde o próximo item será desenhado, em pixels da tela.

**Retorna:** `(x, y)`

#### get_display_size()

 `função`

Tamanho da área de desenho em pixels. Útil para posicionar janelas e HUD.

**Retorna:** `(width, height)`

#### get_io_want_capture_keyboard()

 `função`

True quando a interface está usando o teclado (por exemplo, digitando num campo). Use para não mover o personagem nessa hora.

**Retorna:** `bool`

#### get_io_want_capture_mouse()

 `função`

True quando o mouse está sobre a interface. Use para ignorar cliques do jogo nessa hora.

**Retorna:** `bool`

#### image(texture_id, w, h)

 `função`

-- texture_id é um bind code OpenGL puro

#### input_text(label, value, max_length=256)

 `função`

Campo de texto editável. `max_length` limita o número de caracteres.

**Retorna:** `(changed, new_value)`

#### invisible_button(label, width, height)

 `função`

Área clicável sem desenho. Bom para colocar sobre uma imagem. Devolve True quando clicada.

**Retorna:** `bool`

#### listbox(label, current_item, items, height_items=-1)

 `função`

Lista com rolagem. `height_items` é quantas linhas aparecem (-1 = automático).

**Retorna:** `(changed, new_item)`

#### load_default_font(size)

*(novo na Anastacio)* `função`

**Retorna:** `font_id or None -- engine font with icons; None until built next frame`

#### load_font(path, size)

 `função`

Carrega uma fonte .ttf/.otf no tamanho dado. Chame uma vez só; a fonte fica pronta no quadro seguinte. Use o id em `push_font()`.

**Retorna:** `font_id`

#### open_popup(name)

 `função`

Abre o popup com esse nome.

#### pop_font()

 `função`

Volta à fonte anterior a `push_font()`.

#### pop_item_width()

*(novo na Anastacio)* `função`

Volta à largura anterior a `push_item_width()`.

#### pop_style_color(count=1)

 `função`

Desfaz as últimas `count` cores de `push_style_color()`.

#### pop_style_var(count=1)

*(novo na Anastacio)* `função`

Desfaz os últimos `count` estilos de `push_style_var()`.

#### push_font(font_id)

 `função`

Usa outra fonte até `pop_font()`.

#### push_item_width(width)

*(novo na Anastacio)* `função`

-- >0 pixels, <0 alinhado à direita da borda da janela (-1 = largura total)

#### push_style_color(idx, r, g, b, a)

 `função`

-- idx é uma das constantes imgui.COL_*

#### push_style_var(idx, value)

*(novo na Anastacio)* `função`

ou push_style_var(idx, x, y) -- idx é uma das imgui.STYLE_*

#### radio_button(label, active)

 `função`

Botão de opção. `active` diz se ele é o escolhido; quando `pressed` for True, guarde essa opção como a escolhida do grupo.

**Retorna:** `pressed`

#### same_line()

 `função`

Coloca o próximo item na mesma linha do anterior.

#### separator()

 `função`

Desenha uma linha separadora.

#### set_cursor_pos(x, y)

 `função`

-- posição relativa à janela atual

#### set_game_ui_open(open)

 `função`

-- liga/desliga a entrada + libera o mouse para a UI de jogo desenhada em Python

#### set_next_item_width(width)

*(novo na Anastacio)* `função`

-- mesma convenção de push_item_width, só para o próximo widget

#### set_next_window_pos(x, y, cond=COND_ALWAYS)

 `função`

Posição da próxima janela, em pixels.

#### set_next_window_size(w, h, cond=COND_ALWAYS)

 `função`

Tamanho da próxima janela, em pixels.

#### slider_float(label, value, min, max)

 `função`

Barra deslizante para número decimal entre `min` e `max`.

**Retorna:** `(changed, new_value)`

#### slider_int(label, value, min, max)

 `função`

Barra deslizante para número inteiro entre `min` e `max`.

**Retorna:** `(changed, new_value)`

#### text(text)

 `função`

Mostra um texto.

---

## Range.logic

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`KX_Scene`](#kx_scene), [`Range.events`](#rangeevents), [`SCA_PythonController`](#sca_pythoncontroller)

```python
# Guarda um valor entre cenas e entre sessões do jogo.
import Range

Range.logic.globalDict["level"] = 3
Range.logic.saveGlobalDict()
```

```python
# Lê de volta quando o jogo abre.
import Range

Range.logic.loadGlobalDict()
level = Range.logic.globalDict.get("level", 1)
print("Level:", level)
```

```python
# Move o objeto pelo teclado, na mesma velocidade em qualquer taxa de quadros.
import Range

own = Range.logic.getCurrentController().owner
keys = Range.logic.keyboard.inputs

if keys[Range.events.WKEY].active:
    own.applyMovement((0.0, 0.1, 0.0), True)
```

```python
# Deixa o jogo inteiro em câmera lenta para um momento dramático.
import Range

Range.logic.setTimeScale(0.3)
Range.logic.setAnimationsUseTimeScale(True)
```

```python
# Carrega outro arquivo com o jogo rodando.
import Range

path = Range.logic.expandPath("//levels/forest.range")
status = Range.logic.LibLoad(path, "Scene", asynchronous=True)
print(status.libraryName)
```

```python
# Envia uma mensagem que um sensor Message pode receber.
import Range

Range.logic.sendMessage("door_open", "north")
```

### Introdução

Módulo com as funções de lógica do jogo, importado automaticamente no namespace dos controladores Python.

```python

# Para pegar o controlador que está rodando este script Python:
cont = Range.logic.getCurrentController() # Range.logic é importado automaticamente

# Para pegar o objeto do jogo onde está este controlador:
obj = cont.owner
```

Os métodos de `KX_GameObject`, `KX_Camera` ou `KX_LightObject` ficam disponíveis conforme o tipo do objeto

```python

# Para pegar um sensor ligado a este controlador.
# "sensorname" é o nome do sensor como foi definido na interface do Blender.
# +---------------------+  +--------+
# | Sensor "sensorname" +--+ Python +
# +---------------------+  +--------+
sens = cont.sensors["sensorname"]

# Para pegar a lista de todos os sensores:
sensors = co.sensors
```

Veja a referência de cada sensor para os métodos disponíveis:

* `KX_MouseFocusSensor`
* `KX_NearSensor`
* `KX_NetworkMessageSensor`
* `KX_RadarSensor`
* `KX_RaySensor`
* `KX_CollisionSensor`
* `SCA_DelaySensor`
* `SCA_JoystickSensor`
* `SCA_KeyboardSensor`
* `SCA_MouseSensor`
* `SCA_PropertySensor`
* `SCA_RandomSensor`
Você também pode acessar os atuadores ligados ao controlador

```python

# Para pegar um atuador ligado ao controlador:
# +--------+  +-------------------------+
# + Python +--+ Actuator "actuatorname" |
# +--------+  +-------------------------+
actuator = co.actuators["actuatorname"]

# Ativa um atuador
controller.activate(actuator)
```

Veja a referência de cada atuador para os métodos disponíveis

* `BL_ActionActuator`
* `KX_CameraActuator`
* `KX_ConstraintActuator`
* `KX_GameActuator`
* `KX_MouseActuator`
* `KX_NetworkMessageActuator`
* `KX_ObjectActuator`
* `KX_ParentActuator`
* `KX_SCA_AddObjectActuator`
* `KX_SCA_DynamicActuator`
* `KX_SCA_EndObjectActuator`
* `KX_SCA_ReplaceMeshActuator`
* `KX_SceneActuator`
* `KX_SoundActuator`
* `KX_StateActuator`
* `KX_TrackToActuator`
* `KX_VisibilityActuator`
* `SCA_2DFilterActuator`
* `SCA_PropertyActuator`
* `SCA_RandomActuator`
A maioria dos métodos dos logic bricks dá acesso às propriedades que aparecem nos botões de lógica. Consulte a documentação dos logic bricks para saber como cada um funciona.

Também há métodos para acessar a `Range.types.KX_Scene` atual

```python

# Pega a cena atual
scene = Range.logic.getCurrentScene()

# Pega a câmera atual
cam = scene.active_camera
```

As matrizes usadas pela engine são **por linha** (row major): `matrix[row][col] = float`

`Range.types.KX_Camera` tem alguns exemplos usando matrizes.

### Variáveis

#### globalDict

Um dicionário que é mantido quando outro arquivo blend é carregado; serve para guardar inventário e outras variáveis entre cenas e arquivos blend. Ele também pode ser gravado num arquivo e carregado depois com os atuadores de carregar/salvar jogo.

> **Note:**
só tipos nativos do Python, como int/string/bool/float/tuplas/listas, podem ser salvos; GameObjects, atuadores etc. não funcionam como esperado.

#### keyboard

O teclado atual, dentro de um objeto `SCA_PythonKeyboard`.

#### mouse

O mouse atual, dentro de um objeto `SCA_PythonMouse`.

#### motion

Os sensores de movimento do aparelho (giroscópio, acelerômetro, inclinação), dentro de um objeto `KX_PythonMotion`.

#### joysticks

Lista dos `SCA_PythonJoystick` conectados. O tamanho da lista é o número máximo de joysticks suportados. Se não houver joystick numa posição, ela vale None.

#### inputSystem

Os mapas de entrada do jogo, um `KX_InputSystem`. Eles são carregados dos arquivos JSON da pasta KeyMapping, ao lado do arquivo do jogo.

### Funções gerais

#### getCurrentController()

Pega o controlador Python ligado a este script.

**Tipo do retorno:** `Range.types.SCA_PythonController`

#### getCurrentScene()

Pega a cena atual.

**Tipo do retorno:** `Range.types.KX_Scene`

#### getSceneList()

Pega a lista das cenas carregadas na engine agora.

**Tipo do retorno:** list of `Range.types.KX_Scene`

> **Note:**
As cenas do arquivo blend que não foram convertidas não aparecem nesta lista. Ela só traz cenas como as de overlay.

#### getInactiveSceneNames()

Pega a lista dos nomes das cenas que não estão carregadas na engine.

**Tipo do retorno:** list of string

#### loadGlobalDict()

Carrega Range.logic.globalDict de um arquivo.

#### saveGlobalDict()

Salva Range.logic.globalDict num arquivo.

#### startGame(blend)

Carrega o arquivo blend.

- **`blend`**: O nome do arquivo blend
  - tipo: string

#### endGame()

Encerra o jogo atual.

#### restartGame()

Reinicia o jogo atual recarregando o arquivo .blend (a última versão salva, não o que está rodando agora).

#### LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

Converte todos os datablocks do tipo indicado do arquivo blend indicado.

- **`blend`**: O caminho do arquivo blend (ou o nome a usar para a biblioteca, se data for passado)
  - tipo: string
- **`type`**: O tipo de datablock (por enquanto só "Action", "Mesh" e "Scene" são suportados)
  - tipo: string
- **`data`**: Dados binários de um arquivo blend (opcional)
  - tipo: bytes
- **`load_actions`**: Procura e carrega todas as ações da cena, não só as ações "ativas" (só para o tipo Scene)
  - tipo: bool
- **`verbose`**: Se mostra ou não informações de depuração (ex.: "SceneName: Scene")
  - tipo: bool
- **`load_scripts`**: Se carrega ou não também os datablocks de texto (pode ser desligado para mais segurança)
  - tipo: bool   
- **`asynchronous`**: Se carrega ou não de forma assíncrona (em outra thread). Por enquanto só o tipo "Scene" suporta isso.
  - tipo: bool
- **`scene`**: Cena onde juntar os dados carregados; se for `None`, usa a cena atual.
  - tipo: `Range.types.KX_Scene` or string

**Tipo do retorno:** `Range.types.KX_LibLoadStatus`

> **Note:**
Bibliotecas carregadas de forma assíncrona não ficam disponíveis logo que LibLoad() retorna. Use o KX_LibLoadStatus devolvido para saber quando elas estão prontas.

#### LibNew(name, type, data)

Usa dados de um datablock que já existe e carrega como uma biblioteca nova.

- **`name`**: Um nome único para a biblioteca, usado depois para removê-la
  - tipo: string
- **`type`**: O tipo de datablock (por enquanto só "Mesh" é suportado)
  - tipo: string
- **`data`**: Lista com os nomes dos datablocks a carregar
  - tipo: list of strings

#### LibFree(name)

Libera uma biblioteca, removendo todos os objetos e malhas dela das cenas ativas.

- **`name`**: O nome da biblioteca a liberar (o nome usado em LibNew)
  - tipo: string

#### LibList()

Devolve a lista das bibliotecas carregadas agora.

**Tipo do retorno:** list [str]

#### setLibLoadFrameBudget([ms])

Tempo por frame, em milissegundos, que o LibLoad assíncrono pode gastar juntando as bibliotecas carregadas à cena (texturas, shaders, objetos). O padrão de 8 mantém o frame rate do jogo; uma tela de carregamento pode aumentar (ex.: 30) para terminar antes com frame rate menor, e depois voltar o valor.

- **`ms`**: Novo limite; se omitido, só devolve o atual.
  - tipo: float

**Retorna:** O limite atual em milissegundos.

**Tipo do retorno:** float

#### addScene(name, overlay=1, asynchronous=False)

Carrega uma cena na engine.

> **Note:**
Esta função não tem efeito na hora: a cena entra na fila e é adicionada no próximo ciclo de lógica, quando aparece em `getSceneList`

- **`name`**: O nome da cena
  - tipo: string
- **`overlay`**: Overlay ou underlay (opcional)
  - tipo: integer
- **`asynchronous`**: Compila os shaders da cena aos poucos a cada frame (limite de `setLibLoadFrameBudget`) antes de a cena entrar em `getSceneList`, para a tela de carregamento continuar desenhando; a lógica da cena só começa depois disso.
  - tipo: boolean

#### sendMessage(subject, body="", to="", message_from="")

Envia uma mensagem para os sensores de qualquer cena ativa.

- **`subject`**: O assunto da mensagem
  - tipo: string
- **`body`**: O corpo da mensagem (opcional)
  - tipo: string
- **`to`**: O nome do objeto que vai receber a mensagem (opcional)
  - tipo: string
- **`message_from`**: O nome do objeto de onde a mensagem vem (opcional)
  - tipo: string

#### setGravity(gravity)

Define a gravidade do mundo.

- **`gravity`**: O vetor de gravidade
  - tipo: Vector((fx, fy, fz))

#### getSpectrum() (Deprecated)

Devolve uma lista de 512 pontos da placa de som. Só funciona com o driver de som fmod.

**Tipo do retorno:** list [float], len(getSpectrum()) == 512

#### getMaxLogicFrame()

Pega o número máximo de frames de lógica por frame de render.

**Retorna:** O número máximo de frames de lógica por frame de render

**Tipo do retorno:** integer

#### setMaxLogicFrame(maxlogic)

Define o número máximo de frames de lógica executados por frame de render. Não afeta a física, que continua rodando no frame rate completo.

- **`maxlogic`**: O novo número máximo de frames de lógica por frame de render. Valores válidos: 1..5
  - tipo: integer

#### ~~getMaxPhysicsFrame()~~

> **Obsoleto :**
Nenhuma parte da engine usa este limite; o valor definido aqui não tem efeito. Fica só por compatibilidade com scripts antigos. Ele também não controla mais o culling de sombras, que antes usava esta mesma configuração.

Pega o último valor passado para `setMaxPhysicsFrame`.

**Retorna:** O último valor definido (padrão: 5)

**Tipo do retorno:** integer

#### ~~setMaxPhysicsFrame(maxphysics)~~

> **Obsoleto :**
Nenhuma parte da engine usa este limite; chamar isto não tem efeito na física nem nas sombras. Fica só por compatibilidade com scripts antigos.

Guarda o valor para ler depois com `getMaxPhysicsFrame`. Era documentado como o número máximo de passos de física por frame de render, mas nenhum código da engine lê o valor para isso.

- **`maxphysics`**: O novo número máximo de passos de física por frame de render. Valores válidos: 1..5.
  - tipo: integer

#### getLogicTicRate()

Pega a frequência de atualização da lógica.

**Retorna:** A frequência da lógica em Hz

**Tipo do retorno:** float

#### setLogicTicRate(ticrate)

Define a frequência de atualização da lógica.

A frequência da lógica é quantas vezes por segundo os logic bricks são executados. O padrão é 60 Hz.

- **`ticrate`**: A nova frequência da lógica (em Hz).
  - tipo: float

#### getPhysicsTicRate()

Pega a frequência de atualização da física

**Retorna:** A frequência da física em Hz

**Tipo do retorno:** float

#### setPhysicsTicRate(ticrate)

Define a frequência de atualização da física

A frequência da física é quantas vezes por segundo a física é executada. O padrão é 60 Hz.

- **`ticrate`**: A nova frequência (em Hz).
  - tipo: float

#### getExitKey()

Pega a tecla usada para sair da engine

**Retorna:** A tecla (padrão: `Range.events.ESCKEY`)

**Tipo do retorno:** int

#### setExitKey(key)

Define a tecla usada para sair da engine

- **`key`**: Uma constante de tecla de `Range.events`
  - tipo: int

#### NextFrame()

Renderiza o próximo frame (se o Python estiver no controle)

#### setRender(render)

Define a opção global que controla o render da cena. Se for True, o render acontece depois do frame de lógica. Se for False, o render é pulado e outro frame de lógica começa na hora.

> **Note:**
Com o render desligado, o VSync da GPU não limita mais os frames por segundo, mas a opção *Use Frame Rate* continua regulando o fps. Para rodar o máximo de frames possível, desmarque essa opção (Render Properties, painel System).

- **`render`**: A opção de render
  - tipo: bool

#### getRender()

Pega o valor atual da opção global de render

**Retorna:** O valor da opção

**Tipo do retorno:** bool

### Funções de tempo

#### getClockTime()

Pega o tempo de render atual da engine, em segundos. É o tempo de simulação correspondente à próxima cena que será renderizada.

**Tipo do retorno:** double

#### getFrameTime()

Pega o tempo de frame atual da engine, em segundos. É o tempo de simulação correspondente à chamada atual da lógica. Em geral, é este o tempo que interessa.

**Tipo do retorno:** double

#### getRealTime()

Pega quantos segundos reais (do relógio do sistema) passaram desde o começo da simulação.

**Tipo do retorno:** double

#### getTimeScale()

Pega o multiplicador entre o tempo real e o tempo da simulação. O padrão é 1.0. Valores maiores que 1.0 deixam a simulação mais rápida que o tempo real; valores menores, mais lenta.

**Tipo do retorno:** double

#### setTimeScale(time_scale)

Define o multiplicador entre o tempo real e o tempo da simulação. Valores maiores que 1.0 deixam a simulação mais rápida que o tempo real; valores menores, mais lenta. Valores muito altos podem deixar a física instável.

A escala vale para todos os relógios do jogo: física, timers, `getFrameTime`, actions e cutscenes. O valor 0.0 pausa a lógica, então nenhum logic brick ou script roda até a escala mudar de novo; retome de fora da lógica do jogo, ou pause com `KX_Scene.suspend`.

- **`time_scale`**: O novo multiplicador de tempo.

#### setAnimationsUseTimeScale(use)

Escolhe se as ações seguem o `setTimeScale`. Com `False` o relógio das animações avança pelo passo de lógica sem escala, então as ações tocam em velocidade normal enquanto física, timers e lógica continuam escalados. Padrão `True`.

- **`use`**: `True` para escalar as animações, `False` para mantê-las em velocidade normal.
  - tipo: bool

#### getAnimationsUseTimeScale()

**Retorna:** `True` se as ações seguem a escala de tempo.

**Tipo do retorno:** bool

#### ~~getUseExternalClock()~~

> **Obsoleto 0.5.5:**
A flag não tem efeito; a simulação sempre usa o próprio relógio.

**Tipo do retorno:** bool

#### ~~setUseExternalClock(use_external_clock)~~

> **Obsoleto 0.5.5:**
Não tem efeito na simulação e emite um `DeprecationWarning`.

- **`use_external_clock`**: A nova configuração

#### setClockTime(new_time)

Define o próximo valor do relógio da simulação. É melhor usar este método numa função main própria em Python: chamá-lo num logic brick pode travar o sistema facilmente (se o tempo não avançar o bastante para rodar pelo menos o próximo passo de lógica).

- **`new_time`**: O próximo valor do relógio da engine (em segundos).

### Funções utilitárias

#### expandPath(path)

Converte um caminho interno do Blender num caminho de verdade do sistema de arquivos.

Use / como separador de pastas no caminho. Use '//' no começo para um caminho relativo; o Blender troca isso pela pasta do .blend ou do executável atual para formar o caminho completo. A função também converte o separador para o formato do sistema.

- **`path`**: O caminho a converter/expandir.
  - tipo: string

**Retorna:** O caminho convertido

**Tipo do retorno:** string

#### getAverageFrameRate()

Pega o frame rate médio estimado de todas as cenas ativas, não só da atual.

**Retorna:** O frame rate médio estimado, em frames por segundo

**Tipo do retorno:** float

#### getBlendFileList(path = "//")

Devolve a lista dos arquivos blend na mesma pasta do arquivo blend aberto, ou na pasta passada como argumento.

- **`path`**: Pasta opcional, que é expandida (como em expandPath) para o caminho completo.
  - tipo: string

**Retorna:** Lista de nomes de arquivo, sem a pasta na frente

**Tipo do retorno:** list

#### getRandomFloat()

Devolve um número decimal aleatório no intervalo [0 - 1)

#### PrintGLInfo()

Mostra no console as informações das extensões GL

#### PrintMemInfo()

Mostra no console as estatísticas da engine

#### getProfileInfo()

Devolve um dicionário Python com as mesmas informações do profiler na tela. As chaves são as categorias do profiler, e os valores são tuplas com o tempo gasto (em ms) no primeiro elemento e a porcentagem do tempo total no segundo.

#### getRenderStats()

Devolve um dicionário Python com contadores inteiros do último frame completo, os mesmos números que as consultas de render do Debug Mode mostram. Diferente dos tempos de `getProfileInfo`, eles não dependem do hardware nem do relógio, por isso são o que testes A/B devem comparar.

Contadores do rasterizador, cobrindo todas as passadas do frame (câmera principal, sombras, filtros 2D):

* `drawCalls`: draw calls feitas.
* `materialBinds`: binds de material (programa de shader).
* `lightBinds`: envios dos uniforms das luzes da cena e das lâmpadas com sombra. O conjunto de luzes é constante por camada de luz, então isto conta quantas vezes os mesmos valores foram reenviados.

Contadores da cena ativa:

* `cullingTotal`, `cullingTested`, `cullingVisible`: objetos na lista de render, testados contra o frustum/DBVT e achados visíveis, na última passada de culling da câmera principal.
* `lightsTotal`, `lightsShadowUpdated`, `shadowPasses`: luzes da cena, luzes cujo buffer de sombra foi atualizado e passadas de sombra renderizadas (cada divisão de cascata conta como uma).
* `sensors`, `controllersTriggered`, `actuatorsUpdated`: sensores registrados e controladores/atuadores executados no frame de lógica. Atenção: estes dois são contados enquanto o frame roda, e um controlador Python que chama esta função faz parte desse frame; ele só vê o que rodou antes dele, então num controlador o valor costuma ser 0. A sobreposição do Debug Mode lê os valores depois do frame e mostra a contagem completa. Os contadores do rasterizador e do culling não têm esse problema: sempre vêm do último frame completo.

### Constantes

#### KX_TRUE

Valor verdadeiro usado por alguns módulos.

#### KX_FALSE

Valor falso usado por alguns módulos.

### Sensores

### Estado do sensor

#### KX_SENSOR_INACTIVE

Estado do sensor: desligado.

#### KX_SENSOR_JUST_ACTIVATED

Estado do sensor: acabou de ligar neste quadro.

#### KX_SENSOR_ACTIVE

Estado do sensor: continua ligado.

#### KX_SENSOR_JUST_DEACTIVATED

### Sensor de armature

Veja `Range.types.KX_ArmatureSensor.type`

#### KX_ARMSENSOR_STATE_CHANGED

Detecta que a constraint mudou de estado (ativa/inativa)

**Valor:** `0`

#### KX_ARMSENSOR_LIN_ERROR_BELOW

Detecta que o erro linear da constraint passou de um limite

**Valor:** `1`

#### KX_ARMSENSOR_LIN_ERROR_ABOVE

Detecta que o erro linear da constraint ficou abaixo de um limite

**Valor:** `2`

#### KX_ARMSENSOR_ROT_ERROR_BELOW

Detecta que o erro de rotação da constraint passou de um limite

**Valor:** `3`

#### KX_ARMSENSOR_ROT_ERROR_ABOVE

Detecta que o erro de rotação da constraint ficou abaixo de um limite

**Valor:** `4`

### Sensor de propriedade

#### KX_PROPSENSOR_EQUAL

Ativa quando a propriedade é igual ao valor do sensor.

**Valor:** `1`

#### KX_PROPSENSOR_NOTEQUAL

Ativa quando a propriedade é diferente do valor do sensor.

**Valor:** `2`

#### KX_PROPSENSOR_INTERVAL

Ativa quando a propriedade está entre os limites indicados.

**Valor:** `3`

#### KX_PROPSENSOR_CHANGED

Ativa quando a propriedade muda

**Valor:** `4`

#### KX_PROPSENSOR_EXPRESSION

Ativa quando a expressão confere

**Valor:** `5`

#### KX_PROPSENSOR_LESSTHAN

Ativa quando a propriedade é menor que o valor do sensor

**Valor:** `6`

#### KX_PROPSENSOR_GREATERTHAN

Ativa quando a propriedade é maior que o valor do sensor

**Valor:** `7`

### Sensor de radar

Veja `Range.types.KX_RadarSensor`

#### KX_RADAR_AXIS_POS_X

Sensor Radar: cone apontando para o eixo +X do objeto.

#### KX_RADAR_AXIS_POS_Y

Sensor Radar: cone apontando para o eixo +Y do objeto.

#### KX_RADAR_AXIS_POS_Z

Sensor Radar: cone apontando para o eixo +Z do objeto.

#### KX_RADAR_AXIS_NEG_X

Sensor Radar: cone apontando para o eixo -X do objeto.

#### KX_RADAR_AXIS_NEG_Y

Sensor Radar: cone apontando para o eixo -Y do objeto.

#### KX_RADAR_AXIS_NEG_Z

### Sensor de raio

Veja `Range.types.KX_RaySensor`

#### KX_RAY_AXIS_POS_X

Sensor Ray: raio lançado no eixo +X do objeto.

#### KX_RAY_AXIS_POS_Y

Sensor Ray: raio lançado no eixo +Y do objeto.

#### KX_RAY_AXIS_POS_Z

Sensor Ray: raio lançado no eixo +Z do objeto.

#### KX_RAY_AXIS_NEG_X

Sensor Ray: raio lançado no eixo -X do objeto.

#### KX_RAY_AXIS_NEG_Y

Sensor Ray: raio lançado no eixo -Y do objeto.

#### KX_RAY_AXIS_NEG_Z

### Atuadores

### Atuador de ação

Veja `Range.types.BL_ActionActuator`

#### KX_ACTIONACT_PLAY

Atuador Action: toca a animação uma vez.

#### KX_ACTIONACT_PINGPONG

Atuador Action: toca para frente e, na próxima ativação, para trás.

#### KX_ACTIONACT_FLIPPER

Atuador Action: toca enquanto ativo e volta ao início quando desliga.

#### KX_ACTIONACT_LOOPSTOP

Atuador Action: repete enquanto o sensor estiver ativo.

#### KX_ACTIONACT_LOOPEND

Atuador Action: repete e, ao desligar, termina a volta atual.

#### KX_ACTIONACT_PROPERTY

### Atuador de armature

Veja `Range.types.BL_ArmatureActuator.type`

#### KX_ACT_ARMATURE_RUN

Só garante que a armature será atualizada no próximo frame gráfico. É o único modo contínuo do atuador: roda sozinho uma vez por frame até um controlador pará-lo

**Valor:** `0`

#### KX_ACT_ARMATURE_ENABLE

Liga a constraint.

**Valor:** `1`

#### KX_ACT_ARMATURE_DISABLE

Desliga a constraint (os valores da constraint em tempo de jogo não são atualizados).

**Valor:** `2`

#### KX_ACT_ARMATURE_SETTARGET

Troca o alvo e o subalvo da constraint.

**Valor:** `3`

#### KX_ACT_ARMATURE_SETWEIGHT

Muda o peso da constraint (só IK).

**Valor:** `4`

#### KX_ACT_ARMATURE_SETINFLUENCE

Muda a influência da constraint.

**Valor:** `5`

### Atuador de constraint

Veja `Range.types.KX_ConstraintActuator.option`

* Vale para a constraint de distância:

#### KX_CONSTRAINTACT_NORMAL

Ativa o alinhamento à superfície

#### KX_CONSTRAINTACT_DISTANCE

Ativa o controle de distância

#### KX_CONSTRAINTACT_LOCAL

A direção do raio segue o eixo local

* Vale para a constraint de campo de força:

#### KX_CONSTRAINTACT_DOROTFH

O campo de força também age na rotação

* Vale para as duas:

#### KX_CONSTRAINTACT_MATERIAL

Detecta material em vez de propriedade

#### KX_CONSTRAINTACT_PERMANENT

Não desativa se o raio não atingir o alvo

Veja `Range.types.KX_ConstraintActuator.limit`

#### KX_CONSTRAINTACT_LOCX

Limita a coordenada X.

#### KX_CONSTRAINTACT_LOCY

Limita a coordenada Y

#### KX_CONSTRAINTACT_LOCZ

Limita a coordenada Z

#### KX_CONSTRAINTACT_ROTX

Limita a rotação X

#### KX_CONSTRAINTACT_ROTY

Limita a rotação Y

#### KX_CONSTRAINTACT_ROTZ

Limita a rotação Z

#### KX_CONSTRAINTACT_DIRNX

Define a distância ao longo do eixo X negativo

#### KX_CONSTRAINTACT_DIRNY

Define a distância ao longo do eixo Y negativo

#### KX_CONSTRAINTACT_DIRNZ

Define a distância ao longo do eixo Z negativo

#### KX_CONSTRAINTACT_DIRPX

Define a distância ao longo do eixo X positivo

#### KX_CONSTRAINTACT_DIRPY

Define a distância ao longo do eixo Y positivo

#### KX_CONSTRAINTACT_DIRPZ

Define a distância ao longo do eixo Z positivo

#### KX_CONSTRAINTACT_ORIX

Define a orientação do eixo X

#### KX_CONSTRAINTACT_ORIY

Define a orientação do eixo Y

#### KX_CONSTRAINTACT_ORIZ

Define a orientação do eixo Z

#### KX_CONSTRAINTACT_FHNX

Define o campo de força ao longo do eixo X negativo

#### KX_CONSTRAINTACT_FHNY

Define o campo de força ao longo do eixo Y negativo

#### KX_CONSTRAINTACT_FHNZ

Define o campo de força ao longo do eixo Z negativo

#### KX_CONSTRAINTACT_FHPX

Define o campo de força ao longo do eixo X positivo

#### KX_CONSTRAINTACT_FHPY

Define o campo de força ao longo do eixo Y positivo

#### KX_CONSTRAINTACT_FHPZ

Define o campo de força ao longo do eixo Z positivo

### Atuador dinâmico

Veja `Range.types.KX_SCA_DynamicActuator`

#### KX_DYN_RESTORE_DYNAMICS

Atuador Dynamic: volta a ter física.

#### KX_DYN_DISABLE_DYNAMICS

Atuador Dynamic: desliga a física do objeto.

#### KX_DYN_ENABLE_RIGID_BODY

Atuador Dynamic: liga o modo corpo rígido (rotação pela física).

#### KX_DYN_DISABLE_RIGID_BODY

Atuador Dynamic: desliga o modo corpo rígido.

#### KX_DYN_SET_MASS

### Atuador de jogo

Veja `Range.types.KX_GameActuator`

#### KX_GAME_LOAD

Atuador Game: carrega outro arquivo de jogo.

#### KX_GAME_START

Atuador Game: inicia outro arquivo de jogo.

#### KX_GAME_RESTART

Atuador Game: reinicia o jogo.

#### KX_GAME_QUIT

Atuador Game: fecha o jogo.

#### KX_GAME_SAVECFG

Atuador Game: salva as propriedades globais em arquivo.

#### KX_GAME_LOADCFG

### Atuador de mouse

#### KX_ACT_MOUSE_OBJECT_AXIS_X

Atuador Mouse (look): gira em torno do eixo X do objeto.

#### KX_ACT_MOUSE_OBJECT_AXIS_Y

Atuador Mouse (look): gira em torno do eixo Y do objeto.

#### KX_ACT_MOUSE_OBJECT_AXIS_Z

### Atuador de parentesco

#### KX_PARENT_REMOVE

Atuador Parent: tira o objeto do pai.

#### KX_PARENT_SET

### Distribuições aleatórias

Veja `Range.types.SCA_RandomActuator`

#### KX_RANDOMACT_BOOL_CONST

Atuador Random: verdadeiro/falso fixo.

#### KX_RANDOMACT_BOOL_UNIFORM

Atuador Random: verdadeiro ou falso com 50% de chance cada.

#### KX_RANDOMACT_BOOL_BERNOUILLI

Atuador Random: verdadeiro com a chance que você definir.

#### KX_RANDOMACT_INT_CONST

Atuador Random: número inteiro fixo.

#### KX_RANDOMACT_INT_UNIFORM

Atuador Random: inteiro sorteado entre um mínimo e um máximo.

#### KX_RANDOMACT_INT_POISSON

Atuador Random: inteiro com distribuição de Poisson (média definida).

#### KX_RANDOMACT_FLOAT_CONST

Atuador Random: número decimal fixo.

#### KX_RANDOMACT_FLOAT_UNIFORM

Atuador Random: decimal sorteado entre um mínimo e um máximo.

#### KX_RANDOMACT_FLOAT_NORMAL

Atuador Random: decimal com distribuição normal (média e desvio).

#### KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

### Atuador de cena

Veja `Range.types.KX_SceneActuator`

#### KX_SCENE_RESTART

Atuador Scene: reinicia a cena.

#### KX_SCENE_SET_SCENE

Atuador Scene: troca para outra cena.

#### KX_SCENE_SET_CAMERA

Atuador Scene: troca a câmera ativa.

#### KX_SCENE_ADD_FRONT_SCENE

Atuador Scene: adiciona uma cena por cima (overlay, como HUD).

#### KX_SCENE_ADD_BACK_SCENE

Atuador Scene: adiciona uma cena por baixo (fundo).

#### KX_SCENE_REMOVE_SCENE

Atuador Scene: remove uma cena.

#### KX_SCENE_SUSPEND

Atuador Scene: pausa uma cena.

#### KX_SCENE_RESUME

### Atuador de som

Veja `Range.types.KX_SoundActuator`

#### KX_SOUNDACT_PLAYSTOP

Atuador Sound: toca enquanto o sensor estiver ativo e para quando desligar.

**Valor:** `1`

#### KX_SOUNDACT_PLAYEND

Atuador Sound: toca o som inteiro uma vez.

**Valor:** `2`

#### KX_SOUNDACT_LOOPSTOP

Atuador Sound: repete enquanto o sensor estiver ativo.

**Valor:** `3`

#### KX_SOUNDACT_LOOPEND

Atuador Sound: repete e, ao desligar, termina a volta atual.

**Valor:** `4`

#### KX_SOUNDACT_LOOPBIDIRECTIONAL

Atuador Sound: toca para frente e para trás em repetição.

**Valor:** `5`

#### KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

**Valor:** `6`

### Atuador de steering

Veja `Range.types.KX_SteeringActuator.behavior`

#### KX_STEERING_SEEK

Atuador Steering: vai até o alvo.

**Valor:** `1`

#### KX_STEERING_FLEE

Atuador Steering: foge do alvo.

**Valor:** `2`

#### KX_STEERING_PATHFOLLOWING

**Valor:** `3`

### Atuador TrackTo

Veja `Range.types.KX_TrackToActuator`

#### KX_TRACK_UPAXIS_POS_X

Atuador Track To: eixo +X do objeto fica para cima.

#### KX_TRACK_UPAXIS_POS_Y

Atuador Track To: eixo +Y do objeto fica para cima.

#### KX_TRACK_UPAXIS_POS_Z

Atuador Track To: eixo +Z do objeto fica para cima.

#### KX_TRACK_TRAXIS_POS_X

Atuador Track To: eixo +X do objeto aponta para o alvo.

#### KX_TRACK_TRAXIS_POS_Y

Atuador Track To: eixo +Y do objeto aponta para o alvo.

#### KX_TRACK_TRAXIS_POS_Z

Atuador Track To: eixo +Z do objeto aponta para o alvo.

#### KX_TRACK_TRAXIS_NEG_X

Atuador Track To: eixo -X do objeto aponta para o alvo.

#### KX_TRACK_TRAXIS_NEG_Y

Atuador Track To: eixo -Y do objeto aponta para o alvo.

#### KX_TRACK_TRAXIS_NEG_Z

### Diversos

### Filtro 2D

#### RAS_2DFILTER_BLUR

Atuador 2D Filter: desfoque.

**Valor:** `2`

#### RAS_2DFILTER_CUSTOMFILTER

Filtro personalizado; o código é definido pela propriedade shaderText.

**Valor:** `12`

#### RAS_2DFILTER_DILATION

Atuador 2D Filter: dilatação (clareia bordas).

**Valor:** `4`

#### RAS_2DFILTER_DISABLED

Desliga o filtro que está ativo agora

**Valor:** `-1`

#### RAS_2DFILTER_ENABLED

Liga o filtro que foi desligado antes

**Valor:** `-2`

#### RAS_2DFILTER_EROSION

Atuador 2D Filter: erosão (escurece bordas).

**Valor:** `5`

#### RAS_2DFILTER_GRAYSCALE

Atuador 2D Filter: tons de cinza.

**Valor:** `9`

#### RAS_2DFILTER_INVERT

Atuador 2D Filter: cores invertidas.

**Valor:** `11`

#### RAS_2DFILTER_LAPLACIAN

Atuador 2D Filter: detecção de bordas (Laplace).

**Valor:** `6`

#### RAS_2DFILTER_MOTIONBLUR

Cria e liga filtros prontos

**Valor:** `1`

#### RAS_2DFILTER_NOFILTER

Desliga e destrói o filtro que está ativo agora

**Valor:** `0`

#### RAS_2DFILTER_PREWITT

Atuador 2D Filter: detecção de bordas (Prewitt).

**Valor:** `8`

#### RAS_2DFILTER_SEPIA

Atuador 2D Filter: sépia.

**Valor:** `10`

#### RAS_2DFILTER_SHARPEN

Atuador 2D Filter: nitidez.

**Valor:** `3`

#### RAS_2DFILTER_SOBEL

**Valor:** `7`

#### RAS_2DFILTER_SOBEL

**Valor:** `14`

### Canal de armature

Veja `Range.types.BL_ArmatureChannel.rotation_mode`

Observação: os modos euler têm os nomes da interface do Blender, mas a ordem real dos eixos é invertida

#### ROT_MODE_QUAT

Usa o quaternion do atributo rotation para atualizar a rotação do osso.

**Valor:** `0`

#### ROT_MODE_XYZ

Usa euler_rotation e aplica os ângulos nos eixos Z, Y, X do osso, nessa ordem.

**Valor:** `1`

#### ROT_MODE_XZY

Usa euler_rotation e aplica os ângulos nos eixos Y, Z, X do osso, nessa ordem.

**Valor:** `2`

#### ROT_MODE_YXZ

Usa euler_rotation e aplica os ângulos nos eixos Z, X, Y do osso, nessa ordem.

**Valor:** `3`

#### ROT_MODE_YZX

Usa euler_rotation e aplica os ângulos nos eixos X, Z, Y do osso, nessa ordem.

**Valor:** `4`

#### ROT_MODE_ZXY

Usa euler_rotation e aplica os ângulos nos eixos Y, X, Z do osso, nessa ordem.

**Valor:** `5`

#### ROT_MODE_ZYX

Usa euler_rotation e aplica os ângulos nos eixos X, Y, Z do osso, nessa ordem.

**Valor:** `6`

### Constraint de armature

Veja `Range.types.BL_ArmatureConstraint.type`

#### CONSTRAINT_TYPE_TRACKTO

Tipo de restrição de bone: Track To (aponta para um alvo).

#### CONSTRAINT_TYPE_KINEMATIC

Tipo de restrição de bone: IK (cinemática inversa).

#### CONSTRAINT_TYPE_ROTLIKE

Tipo de restrição de bone: Copy Rotation.

#### CONSTRAINT_TYPE_LOCLIKE

Tipo de restrição de bone: Copy Location.

#### CONSTRAINT_TYPE_MINMAX

Tipo de restrição de bone: Floor (limite mín./máx.).

#### CONSTRAINT_TYPE_SIZELIKE

Tipo de restrição de bone: Copy Scale.

#### CONSTRAINT_TYPE_LOCKTRACK

Tipo de restrição de bone: Locked Track.

#### CONSTRAINT_TYPE_STRETCHTO

Tipo de restrição de bone: Stretch To.

#### CONSTRAINT_TYPE_CLAMPTO

Tipo de restrição de bone: Clamp To (prende a uma curva).

#### CONSTRAINT_TYPE_TRANSFORM

Tipo de restrição de bone: Transformation.

#### CONSTRAINT_TYPE_DISTLIMIT

Veja `Range.types.BL_ArmatureConstraint.ik_type`

#### CONSTRAINT_IK_COPYPOSE

A constraint tenta igualar a posição e, se for o caso, a rotação do alvo.

**Valor:** `0`

#### CONSTRAINT_IK_DISTANCE

A constraint mantém uma certa distância do alvo, conforme ik_mode

**Valor:** `1`

Veja `Range.types.BL_ArmatureConstraint.ik_flag`

#### CONSTRAINT_IK_FLAG_TIP

Ligado quando a constraint age na cabeça do osso e não na ponta

**Valor:** `1`

#### CONSTRAINT_IK_FLAG_ROT

Ligado quando a constraint tenta igualar a orientação do alvo

**Valor:** `2`

#### CONSTRAINT_IK_FLAG_STRETCH

Ligado quando a armature pode esticar (só os ossos com fator de estiramento > 0.0)

**Valor:** `16`

#### CONSTRAINT_IK_FLAG_POS

Ligado quando a constraint tenta igualar a posição do alvo.

**Valor:** `32`

Veja `Range.types.BL_ArmatureConstraint.ik_mode`

#### CONSTRAINT_IK_MODE_INSIDE

A constraint tenta manter o osso a no máximo ik_dist do alvo

**Valor:** `0`

#### CONSTRAINT_IK_MODE_OUTSIDE

A constraint tenta manter o osso a mais de ik_dist do alvo

**Valor:** `1`

#### CONSTRAINT_IK_MODE_ONSURFACE

A constraint tenta manter o osso exatamente a ik_dist do alvo.

**Valor:** `2`

### Material do Blender

#### BL_DST_ALPHA

Fator de mistura (blend) do material: alfa de destino. Usado em setBlending().

#### BL_DST_COLOR

Fator de mistura (blend) do material: cor de destino. Usado em setBlending().

#### BL_ONE

Fator de mistura (blend) do material: um (cor inteira). Usado em setBlending().

#### BL_ONE_MINUS_DST_ALPHA

Fator de mistura (blend) do material: 1 menos o alfa de destino. Usado em setBlending().

#### BL_ONE_MINUS_DST_COLOR

Fator de mistura (blend) do material: 1 menos a cor de destino. Usado em setBlending().

#### BL_ONE_MINUS_SRC_ALPHA

Fator de mistura (blend) do material: 1 menos o alfa de origem. Usado em setBlending().

#### BL_ONE_MINUS_SRC_COLOR

Fator de mistura (blend) do material: 1 menos a cor de origem. Usado em setBlending().

#### BL_SRC_ALPHA

Fator de mistura (blend) do material: alfa de origem. Usado em setBlending().

#### BL_SRC_ALPHA_SATURATE

Fator de mistura (blend) do material: alfa de origem saturado. Usado em setBlending().

#### BL_SRC_COLOR

Fator de mistura (blend) do material: cor de origem. Usado em setBlending().

#### BL_ZERO

### Estado da entrada

Veja `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

#### KX_INPUT_NONE

Estado de tecla/botão: solto.

#### KX_INPUT_JUST_ACTIVATED

Estado de tecla/botão: acabou de ser apertado.

#### KX_INPUT_ACTIVE

Estado de tecla/botão: continua apertado.

#### KX_INPUT_JUST_RELEASED

### KX_GameObject

Veja `Range.types.KX_GameObject.playAction`

#### KX_ACTION_MODE_PLAY

Toca a ação uma vez.

**Valor:** `0`

#### KX_ACTION_MODE_LOOP

Repete a ação em loop.

**Valor:** `1`

#### KX_ACTION_MODE_PING_PONG

Toca a ação para a frente e, quando termina, volta para trás.

**Valor:** `2`

#### KX_ACTION_BLEND_BLEND

Mistura as camadas por interpolação linear

**Valor:** `0`

#### KX_ACTION_BLEND_ADD

Soma as camadas

**Valor:** `1`

### Botões do mouse

Veja `Range.types.SCA_MouseSensor`

#### KX_MOUSE_BUT_LEFT

Botão esquerdo do mouse (para o sensor de mouse).

#### KX_MOUSE_BUT_MIDDLE

Botão do meio do mouse (para o sensor de mouse).

#### KX_MOUSE_BUT_RIGHT

### Modos de desenho da malha de navegação

#### RM_WALLS

Desenha só as paredes.

#### RM_POLYS

Desenha só os polígonos.

#### RM_TRIS

Desenha a malha de triângulos.

### Shader

#### VIEWMATRIX

Uniforme de shader com a matriz visão (mundo → câmera). Usado em setUniformDef().

#### VIEWMATRIX_INVERSE

Uniforme de shader com a matriz visão (mundo → câmera), inversa. Usado em setUniformDef().

#### VIEWMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz visão (mundo → câmera), inversa transposta. Usado em setUniformDef().

#### VIEWMATRIX_TRANSPOSE

Uniforme de shader com a matriz visão (mundo → câmera), transposta. Usado em setUniformDef().

#### MODELMATRIX

Uniforme de shader com a matriz modelo (objeto → mundo). Usado em setUniformDef().

#### MODELMATRIX_INVERSE

Uniforme de shader com a matriz modelo (objeto → mundo), inversa. Usado em setUniformDef().

#### MODELMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz modelo (objeto → mundo), inversa transposta. Usado em setUniformDef().

#### MODELMATRIX_TRANSPOSE

Uniforme de shader com a matriz modelo (objeto → mundo), transposta. Usado em setUniformDef().

#### MODELVIEWMATRIX

Uniforme de shader com a matriz modelo × visão. Usado em setUniformDef().

#### MODELVIEWMATRIX_INVERSE

Uniforme de shader com a matriz modelo × visão, inversa. Usado em setUniformDef().

#### MODELVIEWMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz modelo × visão, inversa transposta. Usado em setUniformDef().

#### MODELVIEWMATRIX_TRANSPOSE

Uniforme de shader com a matriz modelo × visão, transposta. Usado em setUniformDef().

#### CAM_POS

Posição da câmera atual

#### CONSTANT_TIMER

Uniforme de shader com o tempo do jogo, para animar efeitos.

#### EYE

Usa um timer como valor do uniform.

#### SHD_TANGENT

### Estados

Veja `Range.types.KX_StateActuator`

#### KX_STATE1

Máscara do estado 1 dos logic bricks.

#### KX_STATE2

Máscara do estado 2 dos logic bricks.

#### KX_STATE3

Máscara do estado 3 dos logic bricks.

#### KX_STATE4

Máscara do estado 4 dos logic bricks.

#### KX_STATE5

Máscara do estado 5 dos logic bricks.

#### KX_STATE6

Máscara do estado 6 dos logic bricks.

#### KX_STATE7

Máscara do estado 7 dos logic bricks.

#### KX_STATE8

Máscara do estado 8 dos logic bricks.

#### KX_STATE9

Máscara do estado 9 dos logic bricks.

#### KX_STATE10

Máscara do estado 10 dos logic bricks.

#### KX_STATE11

Máscara do estado 11 dos logic bricks.

#### KX_STATE12

Máscara do estado 12 dos logic bricks.

#### KX_STATE13

Máscara do estado 13 dos logic bricks.

#### KX_STATE14

Máscara do estado 14 dos logic bricks.

#### KX_STATE15

Máscara do estado 15 dos logic bricks.

#### KX_STATE16

Máscara do estado 16 dos logic bricks.

#### KX_STATE17

Máscara do estado 17 dos logic bricks.

#### KX_STATE18

Máscara do estado 18 dos logic bricks.

#### KX_STATE19

Máscara do estado 19 dos logic bricks.

#### KX_STATE20

Máscara do estado 20 dos logic bricks.

#### KX_STATE21

Máscara do estado 21 dos logic bricks.

#### KX_STATE22

Máscara do estado 22 dos logic bricks.

#### KX_STATE23

Máscara do estado 23 dos logic bricks.

#### KX_STATE24

Máscara do estado 24 dos logic bricks.

#### KX_STATE25

Máscara do estado 25 dos logic bricks.

#### KX_STATE26

Máscara do estado 26 dos logic bricks.

#### KX_STATE27

Máscara do estado 27 dos logic bricks.

#### KX_STATE28

Máscara do estado 28 dos logic bricks.

#### KX_STATE29

Máscara do estado 29 dos logic bricks.

#### KX_STATE30

Veja `Range.types.KX_StateActuator.operation`

#### KX_STATE_OP_CLR

Subtrai bits da máscara de estados

**Valor:** `0`

#### KX_STATE_OP_CPY

Copia a máscara de estados

**Valor:** `1`

#### KX_STATE_OP_NEG

Inverte bits da máscara de estados

**Valor:** `2`

#### KX_STATE_OP_SET

Soma bits à máscara de estados

**Valor:** `3`

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### deltaTime()

 `função`

Tempo, em segundos, desde o frame anterior. Multiplique movimentos por ele para não depender do FPS.

**Retorna:** `float`

#### freeUnconvertedData(scene)

*(novo na Anastacio)* `função`

Só no jogo exportado: libera a geometria usada só por objetos da cena deixados de fora pela opção **Convert**. Eles não poderão mais ser convertidos. Retorna os bytes liberados.

**Retorna:** `int`

#### getAnimationRate()

 `função`

Taxa de atualização das animações (vezes por segundo).

**Retorna:** `float`

#### getGraphicsCardRenderer()

 `função`

Nome da placa de vídeo.

**Retorna:** `str`

#### getGraphicsCardVendor()

 `função`

Fabricante da placa de vídeo.

**Retorna:** `str`

#### getLoadLog(clear=False)

*(novo na Anastacio)* `função`

Relatório dos últimos carregamentos de cena: dicts com `scene`, `stage`, `ms`, `detail` e `total`. Com `clear=True`, limpa depois de ler.

**Retorna:** `list`

#### getMessages(to, subject='')

*(novo na Anastacio)* `função`

Mensagens `(assunto, corpo)` que um sensor Message do objeto `to` recebe neste frame.

**Retorna:** `list`

#### getObjectConvert(scene, object)

*(novo na Anastacio)* `função`

Valor da opção **Convert** do objeto na cena.

**Retorna:** `bool`

#### getProcessorName()

 `função`

Nome do processador.

**Retorna:** `str`

#### getRangeFileList(path='')

 `função`

Arquivos `.range` na pasta do jogo atual (ou em `path`).

**Retorna:** `list`

#### getRasecFileList(path='')

 `função`

Arquivos `.rasec` na pasta do jogo atual (ou em `path`).

**Retorna:** `list`

#### getRenderRate()

 `função`

Taxa de desenho (vezes por segundo).

**Retorna:** `float`

#### preloadScene(name)

*(novo na Anastacio)* `função`

Converte uma cena com antecedência, no fim deste frame (shaders e texturas incluídos), sem adicioná-la. Depois, um `addScene` ou `replaceScene` dela só insere a cena pronta, sem travar. Chame enquanto uma tela de carregamento estiver aparecendo. Devolve `False` se a cena não existir.

**Retorna:** `bool`

#### setAnimationRate(rate)

 `função`

Muda a taxa de atualização das animações.

#### setNeedsParents(count)

 `função`

Quantas vezes por frame a hierarquia de pais é atualizada (de 3 para 1 economiza CPU).

#### setObjectConvert(scene, object, convert, children=True)

*(novo na Anastacio)* `função`

Muda a opção **Convert** de um objeto numa cena que ainda não foi carregada. Retorna quantos objetos mudaram.

**Retorna:** `int`

#### setRenderRate(rate)

 `função`

Muda a taxa de desenho.

#### KX_GAME_SCREENSHOT

 `constante`

Modo do atuador Game: tira um print da tela.

#### KX_JOYSTICK_BUT_A

 `constante`

Botão A do controle.

#### KX_JOYSTICK_BUT_B

 `constante`

Botão B do controle.

#### KX_JOYSTICK_BUT_BACK

 `constante`

Botão Back/Select do controle.

#### KX_JOYSTICK_BUT_GUIDE

 `constante`

Botão Guide (botão central) do controle.

#### KX_JOYSTICK_BUT_LEFTSHOUDER

 `constante`

Botão ombro esquerdo (LB) do controle.

#### KX_JOYSTICK_BUT_LEFTSTICK

 `constante`

Botão clique do analógico esquerdo do controle.

#### KX_JOYSTICK_BUT_PADDOWN

 `constante`

Botão direcional para baixo do controle.

#### KX_JOYSTICK_BUT_PADLEFT

 `constante`

Botão direcional para a esquerda do controle.

#### KX_JOYSTICK_BUT_PADRIGHT

 `constante`

Botão direcional para a direita do controle.

#### KX_JOYSTICK_BUT_PADUP

 `constante`

Botão direcional para cima do controle.

#### KX_JOYSTICK_BUT_RIGHTSHOUDER

 `constante`

Botão ombro direito (RB) do controle.

#### KX_JOYSTICK_BUT_RIGHTSTICK

 `constante`

Botão clique do analógico direito do controle.

#### KX_JOYSTICK_BUT_X

 `constante`

Botão X do controle.

#### KX_JOYSTICK_BUT_Y

 `constante`

Botão Y do controle.

#### KX_MOUSE_BUT_BUTTON6

 `constante`

Botão 6 do mouse.

#### KX_MOUSE_BUT_BUTTON7

 `constante`

Botão 7 do mouse.

#### KX_MOUSE_BUT_LEFTTHUMBMOUSE

 `constante`

Botão lateral esquerdo do mouse (polegar).

#### KX_MOUSE_BUT_RIGHTTHUMBMOUSE

 `constante`

Botão lateral direito do mouse (polegar).

#### KX_MOVEMENT_ALL_AXIS

 `constante`

Sensor Movement: vigia todos os eixos.

#### KX_MOVEMENT_AXIS_NEG_X

 `constante`

Sensor Movement: eixo -X.

#### KX_MOVEMENT_AXIS_NEG_Y

 `constante`

Sensor Movement: eixo -Y.

#### KX_MOVEMENT_AXIS_NEG_Z

 `constante`

Sensor Movement: eixo -Z.

#### KX_MOVEMENT_AXIS_POS_X

 `constante`

Sensor Movement: eixo +X.

#### KX_MOVEMENT_AXIS_POS_Y

 `constante`

Sensor Movement: eixo +Y.

#### KX_MOVEMENT_AXIS_POS_Z

 `constante`

Sensor Movement: eixo +Z.

#### RAS_2DFILTER_BLOOM

 `constante`

Filtro 2D: Bloom.

#### RAS_2DFILTER_FXAA

 `constante`

Filtro 2D: FXAA.

#### RAS_2DFILTER_LIGHTSCATTER

 `constante`

Filtro 2D: raios de luz (light scattering).

#### RAS_2DFILTER_OUTLINE

 `constante`

Filtro 2D: contorno (outline).

#### RAS_2DFILTER_SSAO

 `constante`

Filtro 2D: oclusão de ambiente (SSAO).

#### RAS_2DFILTER_SSR

 `constante`

Filtro 2D: reflexos em tela (SSR).

#### RAS_2DFILTER_TONEMAP

 `constante`

Filtro 2D: tonemap.

---

## Range.network

> **Veja também:**
`Range.network.steam`, [`KX_GameObject`](#kx_gameobject), [`KX_Scene`](#kx_scene)

Módulo `Range.network` da Anastacio Engine. Também acessível como `bge.network`.

```python
# Abre uma sala, ou entra em uma pelo endereço.
from Range import network

def connected(client_id):
    print("Connected as", client_id)

def refused(reason, detail):
    print("Refused:", reason, detail)

network.on_connect(connected)
network.on_reject(refused)

# No host:
network.host(port=7777, max_players=4, room_name="Friends")

# No cliente:
network.join("192.168.0.10:7777")
```

```python
# Sincroniza a posição e a vida de um objeto. Chame antes de host() ou join().
import Range
from Range import network

own = Range.logic.getCurrentController().owner
network.replicate(own, ["life"], transform=True, velocity=True)
```

```python
# Só o servidor cria o jogador de quem entra.
from Range import network

def player_joined(client_id, name):
    print(name, "joined")
    network.spawn("Player", owner=client_id, position=(0.0, 0.0, 1.0))

network.on_player_join(player_joined)
```

```python
# Só o dono do objeto lê o teclado.
import Range
from Range import network

own = Range.logic.getCurrentController().owner

if network.is_owner(own):
    pressed = Range.logic.keyboard.inputs[Range.events.WKEY].active
    network.set_input(bytes([1 if pressed else 0]))
```

```python
# Chat do lobby.
from Range import network

def message(client_id, text):
    print(client_id, text)

network.on_chat(message)
network.send_chat("Ready!")
network.set_ready(True)
```

```python
# Chama uma função em todos os jogadores. Registre do mesmo jeito em todos.
from Range import network

@network.rpc(target="all")
def say_hello(text):
    print(text)

network.call("say_hello", "Hello!")
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### call(name, *args, obj=None)

*(novo na Anastacio)* `função`

Chama uma RPC do jogo registrada com `@rpc`. Com `obj`, vira chamada do objeto (alvo `'owner'` e `owner_only` usam o dono dele). `False` quando recusada aqui (sem sessão, alvo errado...).

**Retorna:** `bool`

#### change_scene(name)

*(novo na Anastacio)* `função`

Só o servidor: troca a cena da sessão durante a partida. Os clientes carregam a mesma cena e recebem tudo de novo quando ela termina de carregar.

#### despawn(obj)

*(novo na Anastacio)* `função`

Só o servidor: remove um objeto replicado em todos os jogadores.

**Retorna:** `bool`

#### disconnect()

*(novo na Anastacio)* `função`

Sai da sessão. No host, fecha a sala para todos.

#### discover_lan()

*(novo na Anastacio)* `função`

Procura salas na rede local sem travar o jogo. Chame cerca de uma vez por segundo; cada item é um dict com os dados da sala.

**Retorna:** `list`

#### host(port=0, max_players=0, room_name='', password='', dedicated=False, websocket_port=-1, transport='enet')

*(novo na Anastacio)* `função`

Abre um servidor (sala). Valores zero ou vazios usam o painel Network da cena. `dedicated=True` não cria jogador local; `websocket_port` aceita clientes Web; `transport` é `'enet'` (LAN/IP) ou `'steam'`.

**Retorna:** `bool`

#### input(client)

*(novo na Anastacio)* `função`

Só o servidor: input do cliente aplicado neste tick (0 = host), ou `None`.

**Retorna:** `bytes`

#### input_stats(client)

*(novo na Anastacio)* `função`

Só o servidor: como os inputs do cliente chegaram (atrasados, repetidos, faltando...), ou `None`.

**Retorna:** `dict`

#### is_owner(obj)

*(novo na Anastacio)* `função`

`True` se este jogador é o dono do objeto.

**Retorna:** `bool`

#### join(address, password='', transport='enet')

*(novo na Anastacio)* `função`

Entra numa sala. `address` aceita `'host'`, `'host:porta'` ou `'[ipv6]:porta'`. O resultado chega por `on_connect` ou `on_reject`.

**Retorna:** `bool`

#### net_id(obj)

*(novo na Anastacio)* `função`

Id de rede do objeto; 0 quando ele não é replicado.

**Retorna:** `int`

#### on_chat(fn)

*(novo na Anastacio)* `função`

Registra `fn(client_id, text)`, chamada a cada mensagem do chat do lobby.

#### on_connect(fn)

*(novo na Anastacio)* `função`

Registra `fn(client_id)`, chamada ao conectar (cliente) ou quando a sala abre (host, com 0).

#### on_disconnect(fn)

*(novo na Anastacio)* `função`

Registra `fn(reason, detail)`, chamada ao sair da sessão. `reason` é uma constante `DISCONNECT_*` (1 a 5).

#### on_lobby(fn)

*(novo na Anastacio)* `função`

Registra `fn()`, chamada quando o host volta a sessão para o lobby.

#### on_player_join(fn)

*(novo na Anastacio)* `função`

Só o servidor: registra `fn(client_id, name)`, chamada quando um jogador entra.

#### on_player_leave(fn)

*(novo na Anastacio)* `função`

Só o servidor: registra `fn(client_id)`, chamada quando um jogador sai.

#### on_reject(fn)

*(novo na Anastacio)* `função`

Registra `fn(reason, detail)`, chamada quando o servidor recusa a entrada. `reason` é uma constante `REJECT_*` (1 a 6).

#### on_scene(fn)

*(novo na Anastacio)* `função`

Registra `fn(scene_name)`, chamada quando a sessão trocou de cena e ela terminou de carregar (servidor e clientes).

#### on_start(fn)

*(novo na Anastacio)* `função`

Registra `fn()`, chamada quando o host começa a partida.

#### owner(obj)

*(novo na Anastacio)* `função`

Id do cliente dono do objeto, ou `None` se ele não é replicado.

**Retorna:** `int`

#### predict(obj, fn)

*(novo na Anastacio)* `função`

`fn(obj, input)` move o objeto por um tick com o input do dono (bytes): no servidor a cada tick e no cliente dono à frente do servidor (predição, corrigida pelos snapshots). Registre em todos os jogadores; `None` desliga.

**Retorna:** `bool`

#### prediction_stats(obj)

*(novo na Anastacio)* `função`

Só no cliente: estatísticas da predição do objeto (correções etc.), ou `None`.

**Retorna:** `dict`

#### raycast_past(origin, direction, distance=100.0, client=-1, ignore=None, max_rewind_ms=400)

*(novo na Anastacio)* `função`

Só o servidor: raio contra as hitboxes como o cliente as via (compensação de lag, até 1 s atrás); `client=-1` usa o momento atual. Retorna `(obj, ponto, distância)` ou `None`.

**Retorna:** `tuple`

#### replicate(obj, props, transform=True, velocity=False, angular_velocity=False, always_relevant=False, priority=1.0, quantize=None)

*(novo na Anastacio)* `função`

Faz o mesmo que a caixa **Replicate**: sincroniza o objeto pela rede. Chame antes de `host()`/`join()`, na mesma ordem em todos os jogadores. `props` lista as propriedades de jogo enviadas (pode ser vazia); `quantize={nome: (min, max, bits)}` manda propriedades Float com menos bits. Retorna o id de rede.

**Retorna:** `int`

#### return_to_lobby()

*(novo na Anastacio)* `função`

Só o host: encerra a partida, zera o "pronto" dos jogadores e avisa os clientes (`on_lobby`). Trocar de cena fica por conta do jogo.

**Retorna:** `bool`

#### send_chat(text)

*(novo na Anastacio)* `função`

Envia uma mensagem no chat do lobby, até 200 bytes em UTF-8. Recebida por `on_chat`.

**Retorna:** `bool`

#### set_client_view(client, center=None, radius=None)

*(novo na Anastacio)* `função`

Só o servidor: centro (objeto ou posição) e raio de relevância de um cliente; objetos fora do raio não são enviados. Raio 0 envia tudo. Sem centro, usa o primeiro objeto do cliente. Tudo `None` volta ao **Relevance Radius** da cena.

#### set_hitbox(obj, radius, half_height=0.0)

*(novo na Anastacio)* `função`

Só o servidor: esfera (ou cápsula no Z local) guardada por 1 s de histórico para `raycast_past()`. Raio 0 remove.

**Retorna:** `bool`

#### set_input(data)

*(novo na Anastacio)* `função`

Input do jogador local (bytes, até 57), enviado a cada tick até mudar, junto com o instante em que os objetos remotos estavam sendo desenhados (compensação de lag). Chame todo frame.

#### set_owner(obj, client)

*(novo na Anastacio)* `função`

Só o servidor: passa o objeto para outro dono (id do cliente; 0 = host).

**Retorna:** `bool`

#### set_ready(ready)

*(novo na Anastacio)* `função`

No lobby, marca este jogador como pronto (`True`) ou não (`False`).

#### set_simulation(latency_ms, jitter_ms, loss_percent)

*(novo na Anastacio)* `função`

Simula uma rede ruim (atraso, variação e perda de pacotes) no próximo `host()`/`join()`. Útil para testar.

#### spawn(prototype, owner=0, position=None, orientation=None)

*(novo na Anastacio)* `função`

Só o servidor: cria uma cópia do objeto inativo `prototype` (nome) e a replica para todos. `owner` é o id do cliente dono (0 = host).

**Retorna:** `KX_GameObject`

#### start_game()

*(novo na Anastacio)* `função`

Só o host: começa a partida. Retorna `False` se algum jogador não está pronto. Os clientes recebem `on_start`.

**Retorna:** `bool`

#### view_time(client=0)

*(novo na Anastacio)* `função`

No cliente: o instante `(tick, alpha)` em que os objetos remotos são desenhados. No servidor: o instante que o cliente mandou com o último input. `None` sem sessão.

**Retorna:** `tuple`

---

## Range.network.steam

> **Veja também:**
[`Range.network`](#rangenetwork)

Módulo `Range.network.steam` da Anastacio Engine. Também acessível como `bge.network.steam`.

```python
# Carrega a Steam e mostra quem está jogando.
import Range
from Range.network import steam

dll = Range.logic.expandPath("//AnastacioSteam.dll")
steam.initialize(dll, 480)

info = steam.status()
if info["ready"]:
    print("Steam id:", info["steam_id"], steam.language())
```

```python
# Desbloqueia uma conquista.
from Range.network import steam

if not steam.achievement("FIRST_WIN"):
    steam.achievement("FIRST_WIN", unlock=True)
```

```python
# Trata eventos de lobby e convites.
from Range.network import steam

for event in steam.poll_events():
    print(event["type"], event["name"], event["members"])
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### achievement(name, unlock=False)

*(novo na Anastacio)* `função`

Consulta uma conquista (achievement) da Steam pelo nome da API; com `unlock=True`, desbloqueia.

**Retorna:** `bool`

#### connection_routes()

*(novo na Anastacio)* `função`

Rota de cada jogador conectado: dicts com `peer`, `steam_id` e `route` (`'direct'`, `'relay'` ou `'unknown'`). Vazia sem jogadores.

**Retorna:** `list`

#### force_relay(force)

*(novo na Anastacio)* `função`

Com `True`, desliga a conexão direta e força os servidores de relay da Steam. Chame depois de `initialize()` e antes de abrir a sessão.

#### initialize(absolute_dll_path, app_id)

*(novo na Anastacio)* `função`

Carrega o complemento opcional `AnastacioSteam.dll` (caminho absoluto) com o AppID do jogo (1 a 4294967295). Só Windows 64 bits, com o jogo rodando; não existe na Web. O componente de multiplayer faz isso sozinho quando **enable_steam** está ligado.

#### language()

*(novo na Anastacio)* `função`

Idioma do jogo escolhido na Steam (ex.: `'brazilian'`); vazio sem Steam.

**Retorna:** `str`

#### poll_events()

*(novo na Anastacio)* `função`

Retira os eventos pendentes de lobby e convites. Cada item é um dict com `type`, `lobby_id`, `host_id`, `port`, `members`, `capacity`, `name` e `detail`.

**Retorna:** `list`

#### shutdown()

*(novo na Anastacio)* `função`

Descarrega a Steam. Desconecte a sessão antes. Fechar o jogo também descarrega.

#### status()

*(novo na Anastacio)* `função`

`{'loaded': bool, 'ready': bool, 'steam_id': int}`: se a DLL carregou, se a Steam está pronta e o SteamID do jogador.

**Retorna:** `dict`

---

## Range.render

> **Veja também:**
[`KX_Camera`](#kx_camera), [`KX_2DFilterManager`](#kx_2dfiltermanager), [`Range.logic`](#rangelogic)

```python
# Mostra o mouse e usa uma configuração mais leve em máquinas fracas.
import Range

Range.render.showMouse(True)
Range.render.setAnisotropicFiltering(4)
Range.render.setVsync(Range.render.VSYNC_ON)
```

```python
# Reduz a resolução sozinho quando a taxa de quadros cai.
import Range

Range.render.setDynamicResolution(True, targetFPS=60, minScale=50, maxScale=100, step=5)
print("Scale:", Range.render.getRenderScale())
```

```python
# Desenha uma linha vermelha do objeto até a origem do mundo.
import Range

own = Range.logic.getCurrentController().owner
Range.render.drawLine(own.worldPosition, (0.0, 0.0, 0.0), (1.0, 0.0, 0.0))
```

```python
# Muda a janela e salva uma captura de tela.
import Range

Range.render.setWindowSize(1280, 720)
print(Range.render.getWindowWidth(), Range.render.getWindowHeight())
Range.render.makeScreenshot("//screenshot_#.png")
```

```python
# Controla o volume geral em um menu de opções.
import Range

Range.render.setMasterVolume(0.5)
print(Range.render.getMasterVolume())
```

### Introdução

Exemplo usando um `Range.types.SCA_MouseSensor` e dois `Range.types.KX_ObjectActuator` para fazer o mouse look:

> **Note:**
Também dá para fazer isso com o `Range.types.KX_MouseActuator`.

```python

# Para usar um sensor de movimento do mouse "Mouse" e um
# atuador de movimento para olhar com o mouse:
import Range

# scale define a velocidade do movimento
scale = 1.0, 0.5

co = Range.logic.getCurrentController()
obj = co.owner
mouse = co.sensors["Mouse"]
lmotion = co.actuators["LMove"]
wmotion = co.actuators["WMove"]

# Converte as coordenadas do mouse para ver quanto o mouse andou.
def mousePos():
   x = (Range.render.getWindowWidth() / 2 - mouse.position[0]) * scale[0]
   y = (Range.render.getWindowHeight() / 2 - mouse.position[1]) * scale[1]
   return (x, y)

pos = mousePos()

# Define o quanto mover: X é aplicado em coordenadas do mundo...
wmotion.useLocalTorque = False
wmotion.torque = ((0.0, 0.0, pos[0]))

# ...Y é aplicado em coordenadas locais
lmotion.useLocalTorque = True
lmotion.torque = ((-pos[1], 0.0, 0.0))

# Ativa os dois atuadores
co.activate(lmotion)
co.activate(wmotion)

# Centraliza o mouse
Range.render.setMousePosition(int(Range.render.getWindowWidth() / 2), int(Range.render.getWindowHeight() / 2))
```

### Constantes

#### KX_TEXFACE_MATERIAL

Obsoleto.

Materiais definidos pelas configurações de texture face.

#### KX_BLENDER_MULTITEX_MATERIAL

Obsoleto.

Materiais que imitam os materiais do Blender com multitextura.

#### KX_BLENDER_GLSL_MATERIAL

Obsoleto.

Materiais que imitam os materiais do Blender com GLSL.

Desliga o vsync; liga o vsync; liga o vsync adaptativo, se suportado. O vsync adaptativo liga o vsync quando o frame rate está acima da taxa de atualização do monitor e desliga quando o frame rate fica baixo demais.

#### LEFT_EYE

Olho esquerdo em uso no render estereoscópico.

#### RIGHT_EYE

Olho direito em uso no render estereoscópico.

### HDR

#### HDR_NONE

Usa formato de imagem com 8 bits por canal.

#### HDR_HALF_FLOAT

Usa formato de imagem com float de 16 bits por canal.

#### HDR_FULL_FLOAT

Usa formato de imagem com float de 32 bits por canal.

### Funções

#### getWindowWidth()

Pega a largura da janela (em pixels)

**Tipo do retorno:** integer

#### getWindowHeight()

Pega a altura da janela (em pixels)

**Tipo do retorno:** integer

#### setWindowSize(width, height)

Define a largura e a altura da janela (em pixels). Também funciona em tela cheia.

> **Note:**
Só funciona no player separado, não no player embutido no Blender.

- **`width`**: Largura em pixels
  - tipo: integer
- **`height`**: Altura em pixels
  - tipo: integer

#### setFullScreen(enable)

Define se a janela fica em tela cheia ou não.

> **Note:**
Só funciona no player separado, não no player embutido no Blender.

- **`enable`**: `True` para tela cheia, `False` para janela.
  - tipo: bool

#### getFullScreen()

Diz se a janela está em tela cheia.

> **Note:**
Só funciona no player separado, não no player embutido no Blender; lá sempre devolve False.

**Tipo do retorno:** bool

#### getDisplayDimensions()

Pega as dimensões da tela (por exemplo, do monitor) em pixels. Pode devolver o tamanho da área inteira, somando todos os monitores; por exemplo, `(3840, 1080)` para dois monitores 1080p lado a lado.

**Tipo do retorno:** tuple (width, height)

#### makeScreenshot(filename)

Grava um arquivo de imagem com o que está na tela no fim do frame.

A imagem é gravada em *'filename'*. O caminho pode ser absoluto (ex.: `/home/foo/image`) ou relativo, começando com `//` (ex.: `//image`). Caminhos absolutos não funcionam igual em todos os sistemas. Se o nome tiver um `#`, ele é trocado por um número que aumenta a cada vez, para tirar vários prints sem sobrescrever os anteriores (ex.: `image-#`).

As configurações da imagem vêm das configurações de render (formato do arquivo e seus ajustes, gamma, conversão de espaço de cor etc.). A resolução da imagem é a do framebuffer, ou seja, o tamanho e a proporção da janela. No player separado, em vez do embutido, só arquivos PNG são suportados, e as conversões de cor extras também não.

- **`filename`**: Caminho e nome do arquivo a gravar
  - tipo: string

#### enableVisibility(visible)

Obsoleto; não faz nada.

#### showMouse(visible)

Mostra ou esconde o cursor do mouse do sistema.

- **`visible`**:
  - tipo: boolean

#### setMousePosition(x, y)

Define a posição do cursor do mouse.

- **`x`**: Coordenada X, em pixels da tela.
  - tipo: integer
- **`y`**: Coordenada Y, em pixels da tela.
  - tipo: integer

#### setBackgroundColor(rgba)

Obsoleto e não funciona mais. Use `Range.types.KX_WorldInfo.horizonColor` ou `Range.types.KX_WorldInfo.zenithColor`.

#### setEyeSeparation(eyesep)

Define a separação dos olhos no modo estéreo. Em geral, distância focal/30 dá um valor confortável.

- **`eyesep`**: A distância entre o olho esquerdo e o direito.
  - tipo: float

#### getEyeSeparation()

Pega a separação dos olhos atual do modo estéreo.

**Tipo do retorno:** float

#### setFocalLength(focallength)

Define a distância focal do modo estéreo. O valor inicial é a distância focal da câmera atual.

- **`focallength`**: A distância focal.
  - tipo: float

#### getFocalLength()

Pega a distância focal atual do modo estéreo.

**Tipo do retorno:** float

#### getStereoEye()

Pega qual olho estereoscópico está sendo renderizado agora. Serve principalmente num callback `Range.types.KX_Scene.pre_draw`, para ajustar as matrizes de projeção da câmera para cada olho.

**Tipo do retorno:** LEFT_EYE, RIGHT_EYE

#### setMaterialMode(mode)

Obsoleto e não funciona mais.

Define o modo de material usado no render OpenGL.

- **`mode`**: Modo de material
  - tipo: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

> **Note:**
As mudanças só valem para cenas criadas depois.

#### getMaterialMode(mode)

Obsoleto e não funciona mais.

Pega o modo de material usado no render OpenGL.

**Tipo do retorno:** KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

#### setGLSLMaterialSetting(setting, enable)

Liga ou desliga uma configuração de material GLSL.

- **`setting`**:
  - tipo: string (lights, shaders, shadows, ramps, nodes, extra_textures)
- **`enable`**:
  - tipo: boolean

#### getGLSLMaterialSetting(setting)

Pega o estado de uma configuração de material GLSL.

- **`setting`**:
  - tipo: string (lights, shaders, shadows, ramps, nodes, extra_textures)

**Tipo do retorno:** boolean

#### setAnisotropicFiltering(level)

Define o nível de filtragem anisotrópica das texturas.

- **`level`**: O novo nível de filtragem anisotrópica
  - tipo: integer (must be one of 1, 2, 4, 8, 16)

> **Note:**
Limitado ao máximo suportado pela placa de vídeo. O jogo exportado começa com 8.

#### getAnisotropicFiltering()

Pega o nível de filtragem anisotrópica das texturas.

**Tipo do retorno:** integer (one of 1, 2, 4, 8, 16)

#### setAntiAliasing(level)

Define o nível de anti-aliasing.

- **`level`**: O novo nível de anti-aliasing
  - tipo: integer (must be one of 0, 2, 4, 8, 16)

> **Note:**
Mudar este valor recria todos os buffers fora da tela, o que pode ser lento.

#### getAntiAliasing()

Pega o nível de anti-aliasing configurado.

**Tipo do retorno:** integer (one of 0, 2, 4, 8, 16)

#### setMipmapping(value)

Muda como o mipmapping é usado.

  - tipo: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

> **Note:**
Alternar entre NEAREST e LINEAR, ou desligá-los, muda apenas os filtros. Com os mipmaps desligados, as texturas são exibidas sem filtragem (nearest), útil para pixel art.

#### getMipmapping()

Pega a configuração atual de mipmapping.

**Tipo do retorno:** RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

#### setTextureQuality(level)

Qualidade de textura para um menu gráfico: mantenha apenas a textura de alta resolução no projeto e descarte seus maiores níveis de mipmap ao enviá-la para a placa de vídeo.

* `0`: tamanho completo
* `1`: metade do tamanho (1/4 da memória de vídeo)
* `2`: um quarto do tamanho (1/16 da memória de vídeo)

As texturas nunca ficam menores que 256 pixels em seu maior lado, e texturas sem mipmaps (ou com mipmapping desligado) mantêm seu tamanho. Arquivos DDS pulam os níveis armazenados no arquivo.

- **`level`**: 0, 1 or 2
  - tipo: integer

> **Note:**
Configure no menu, não a cada frame. No editor, o valor é restaurado quando o jogo termina.

#### getTextureQuality()

**Retorna:** a qualidade de textura atual (0 completa, 1 metade, 2 um quarto).

**Tipo do retorno:** integer

#### drawLine(fromVec,toVec,color)

Desenha uma linha na cena 3D.

- **`fromVec`**: O começo da linha
  - tipo: list [x, y, z]
- **`toVec`**: O fim da linha
  - tipo: list [x, y, z]
- **`color`**: A cor da linha
  - tipo: list [r, g, b, a]

#### enableMotionBlur(factor)

Liga o efeito de motion blur.

- **`factor`**: A intensidade do motion blur.
  - tipo: float [0.0 - 1.0]

#### disableMotionBlur()

Desliga o efeito de motion blur.

#### showFramerate(enable)

Mostra ou esconde o frame rate.

- **`enable`**:
  - tipo: boolean

#### showProfile(enable)

Mostra ou esconde o profiler.

- **`enable`**:
  - tipo: boolean

#### showProperties(enable)

Mostra ou esconde as propriedades de depuração.

- **`enable`**:
  - tipo: boolean

#### autoDebugList(enable)

Liga ou desliga a inclusão automática das propriedades de depuração na lista.

- **`enable`**:
  - tipo: boolean

#### clearDebugList()

Limpa a lista de propriedades de depuração.

#### setVsync(value)

Define o vsync

- **`value`**: Um destes: VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
  - tipo: integer

#### getVsync()

Pega o valor atual do vsync

**Tipo do retorno:** One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE

#### setDynamicResolution(enabled, targetFPS=60, minScale=50, maxScale=100, step=5)

Versão em tempo de jogo das configurações de Dynamic Resolution da cena. A cena 3D é renderizada numa escala do tamanho da janela e esticada para a tela; a janela em si não muda. Com a resolução dinâmica, a escala desce `step` quando o tempo de GPU do frame passa do alvo e sobe de novo quando sobra tempo. `minScale == maxScale` dá uma escala de render fixa. Fica pausada enquanto "Show Render Queries" estiver ligado (os dois usam uma consulta de tempo da GPU).

- **`enabled`**: False renderiza a 100%.
  - tipo: boolean
- **`targetFPS`**: O frame rate com que o tempo de GPU é comparado.
  - tipo: integer
- **`minScale`**: Escala mínima, em porcentagem (25-100).
  - tipo: integer
- **`maxScale`**: Escala máxima, em porcentagem (25-100).
  - tipo: integer
- **`step`**: Quanto a escala muda a cada ajuste, em porcentagem (1-25).
  - tipo: integer

#### getRenderScale()

A escala de render atual; 1.0 = resolução completa.

**Tipo do retorno:** float

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### getMasterVolume()

 `função`

Volume geral do som do jogo, de 0 a 1. Veja `setMasterVolume()`.

**Retorna:** `volume`

#### getStereoMode()

*(novo na Anastacio)* `função`

pega o modo estéreo

#### getVRChromaticAberration()

*(novo na Anastacio)* `função`

pega a correção de aberração cromática da lente VR

#### getVRLensStrength()

*(novo na Anastacio)* `função`

pega a intensidade da distorção da lente VR

#### setCustomMouse(path)

 `função`

Usa a imagem em `path` como cursor do mouse.

#### setMasterVolume(volume)

 `função`

-- volume em [0, 1], aplicado ao dispositivo de áudio real da engine

#### setStereoMode()

*(novo na Anastacio)* `função`

define o modo estéreo (constantes STEREO_*)

#### setVRChromaticAberration()

*(novo na Anastacio)* `função`

define a correção de aberração cromática da lente VR (0..0.1, padrão 0.01)

#### setVRLensStrength()

*(novo na Anastacio)* `função`

define a intensidade da distorção da lente VR (0..1, padrão 0.3)

#### showDebugPhysics(enabled)

 `função`

Mostra ou esconde as formas de colisão da física.

#### RAS_MIPMAP_LINEAR

 `constante`

Mipmap linear (mais suave).

#### RAS_MIPMAP_NEAREST

 `constante`

Mipmap pelo mais próximo.

#### RAS_MIPMAP_NONE

 `constante`

Sem mipmap.

#### STEREO_ABOVEBELOW

 `constante`

Estéreo: uma imagem em cima da outra.

#### STEREO_ANAGLYPH

 `constante`

Estéreo: anaglifo (óculos vermelho/ciano).

#### STEREO_INTERLACED

 `constante`

Estéreo: linhas intercaladas.

#### STEREO_NOSTEREO

 `constante`

Sem estéreo.

#### STEREO_SIDEBYSIDE

 `constante`

Estéreo: lado a lado.

#### VSYNC_ADAPTIVE

 `constante`

VSync adaptativo: sincroniza, mas não trava quando o FPS cai.

#### VSYNC_OFF

 `constante`

VSync desligado.

#### VSYNC_ON

 `constante`

VSync ligado.

---

## Range.texture

> **Veja também:**
[`Texture`](#texture), [`KX_BlenderMaterial`](#kx_blendermaterial), [`BL_Texture`](#bl_texture)

```python
# Mostra um vídeo no material do objeto.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

if "video" not in own:
    matID = texture.materialID(own, "MAscreen")
    tex = texture.Texture(own, matID)
    tex.source = texture.VideoFFmpeg(Range.logic.expandPath("//movie.mp4"))
    tex.source.play()
    own["video"] = tex

own["video"].refresh(True)
```

```python
# Troca a imagem de um material com o jogo rodando.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.refresh(False)
own["poster"] = tex
```

```python
# Faz uma imagem de espelho com outra câmera.
import Range
from Range import texture

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageRender(scene, scene.objects["SecurityCamera"])
own["monitor"] = tex
own["monitor"].refresh(True)
```

### Introdução

O módulo `Range.texture` permite manipular texturas durante o jogo. A textura pode vir de várias fontes: arquivos de vídeo, arquivos de imagem, captura de vídeo, buffer de memória, render de câmera ou uma mistura disso. Os arquivos de vídeo e imagem podem ser carregados da Internet usando uma URL em vez de um nome de arquivo. Também dá para aplicar filtros nas imagens antes de enviá-las à GPU, para efeitos de vídeo: blue screen, faixa de cor, cinza, normal map. `Range.texture` usa o FFmpeg para carregar imagens e vídeos. Todos os formatos e codecs que o FFmpeg suporta são suportados por `Range.texture`, incluindo, entre outros:

* AVI
* Ogg
* Xvid
* Theora
* câmera dv1394
* placa de captura video4linux (inclui muitas webcams)
* placa de captura videoForWindows (inclui muitas webcams)
* JPG

### Como funciona

O princípio é simples: primeiro você identifica uma textura num objeto existente com a função `materialID`, depois cria uma nova textura com conteúdo dinâmico e troca as duas texturas na GPU.

A game engine não percebe a troca e continua mostrando o objeto como sempre, só que agora você controla a textura.

Quando o objeto de textura é apagado, a textura nova é apagada e a antiga é restaurada.

### Preparando o jogo

Antes de usar o módulo `Range.texture`, você precisa de objetos com texturas aplicadas do jeito certo.

Imagine que você quer uma televisão mostrando programas ao vivo no jogo. Você cria um objeto televisão e aplica por UV uma textura diferente no lugar da tela, por exemplo `tv.png`. A aparência dessa textura não importa; provavelmente você vai querer um cinza escuro para simular a TV desligada. Quando a televisão precisar ligar, você cria uma textura dinâmica a partir de uma placa de captura de vídeo e usa no lugar de `tv.png`: a tela da TV ganha vida.

Há dois jeitos de definir texturas que `Range.texture` consegue pegar:

- Textura UV simples.
- Material do Blender com canal de textura de imagem.

Como `Range.texture` trabalha no nível da textura, ele é compatível com todos os recursos de textura da game engine: GLSL, multitextura, shaders personalizados etc.

### Exemplos

### Classes de vídeo

### Classe `VideoFFmpeg(file, capture=-1, rate=25.0, width=0, height=0)`

Fonte de vídeo FFmpeg, usada para arquivos de vídeo, capturas de vídeo ou streams de vídeo.

- **`file`**: Caminho do vídeo a carregar; se capture >= 0 no Windows, este parâmetro não é usado.
  - tipo: str
- **`capture`**: Número do dispositivo de captura; se >= 0, a webcam correspondente é usada (opcional).
  - tipo: int
- **`rate`**: Taxa de captura (opcional, só usado se capture >= 0).
  - tipo: float
- **`width`**: Largura da captura (opcional, só usado se capture >= 0).
  - tipo: int
- **`height`**: Altura da captura (opcional, só usado se capture >= 0).
  - tipo: int

#### status

Status do vídeo (somente leitura).

**Tipo:** int

**Valor:** `see `FFmpeg Video and Image Status`_.`

#### range

O tempo de início e fim da reprodução, em segundos desde o começo. Por padrão, o vídeo inteiro.

**Tipo:** sequence of two floats

#### repeat

Número de vezes que o vídeo repete; -1 para repetir sem parar.

**Tipo:** int

#### framerate

Frame rate relativo: <1.0 para lento, >1.0 para rápido.

**Tipo:** float

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### scale

Use True para ligar o algoritmo rápido de escala por vizinho mais próximo. A largura e a altura da textura precisam ser potência de 2. Se o tamanho da imagem do vídeo não for potência de 2, é preciso reescalar. Por padrão, `Range.texture` usa a função `gluScaleImage()`, precisa mas lenta. O melhor é reescalar o vídeo antes, para não precisar escalar em tempo de execução!

**Tipo:** bool

#### flip

Com True, a imagem é espelhada na vertical. O FFmpeg sempre entrega a imagem de cabeça para baixo, por isso este atributo vem True por padrão.

**Tipo:** bool

#### filter

Um filtro adicional aplicado no vídeo antes de enviá-lo à GPU.

**Tipo:** one of: * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### preseek

Número de frames de pré-busca.

**Tipo:** int

#### deinterlace

Desentrelaça a imagem.

**Tipo:** bool

#### play()

Toca (reinicia) o vídeo.

**Retorna:** Se o vídeo estava pronto ou parado.

**Tipo do retorno:** bool

#### pause()

Pausa o vídeo.

**Retorna:** Se o vídeo estava tocando.

**Tipo do retorno:** bool

#### stop()

Para o vídeo (play toca de novo desde o início).

**Retorna:** Se o vídeo estava tocando.

**Tipo do retorno:** bool

#### refresh(buffer=None, format="RGBA", timestamp=-1.0)

Atualiza o vídeo: pega o status e, se quiser, copia o frame para um buffer externo.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str
- **`timestamp`**: Um timestamp opcional (em segundos desde o início do filme) do frame a copiar para o buffer.
  - tipo: float

**Retorna:** veja `FFmpeg Video and Image Status`_.

**Tipo do retorno:** int

### Classes de imagem

### Classe `ImageFFmpeg(file)`

Fonte de imagem FFmpeg, usada para arquivos de imagem e imagens da web.

- **`file`**: Caminho da imagem a carregar.
  - tipo: str

#### status

Status da imagem (somente leitura).

**Tipo:** int

**Valor:** `see `FFmpeg Video and Image Status`_.`

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

#### flip

Espelha a imagem na vertical.

**Tipo:** bool

#### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### refresh(buffer=None, format="RGBA")

Atualiza a imagem: pega o status e, se quiser, copia o frame para um buffer externo.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

**Retorna:** veja `FFmpeg Video and Image Status`_.

**Tipo do retorno:** int

#### reload(newname=None)

Recarrega a imagem, ou seja, abre de novo.

- **`newname`**: Caminho para uma nova imagem (opcional).
  - tipo: str

### Classe `ImageBuff(width, height, color=0, scale=False)`

Imagem vinda da memória da aplicação. Para imagens geradas pelo computador, aplicativos de desenho.

- **`width`**: Largura da imagem.
  - tipo: int
- **`height`**: Altura da imagem.
  - tipo: int
- **`color`**: Valor para iniciar os canais RGB. O buffer iniciado terá todos os pixels em (color, color, color, 255) (opcional).
  - tipo: int in [0, 255]
- **`scale`**: A imagem usa escala (opcional).
  - tipo: bool

#### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Espelha a imagem na vertical.

**Tipo:** bool

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### load(imageBuffer, width, height)

Carrega a imagem de um buffer.

- **`imageBuffer`**: Buffer de onde carregar a imagem.
  - tipo: `Buffer` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Largura da imagem a carregar.
  - tipo: int
- **`height`**: Altura da imagem a carregar.
  - tipo: int

#### plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY)

Atualiza o buffer da imagem.

- **`imageBuffer`**: Buffer de onde carregar os dados novos.
  - tipo: `Buffer`, `ImageBuff` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Largura dos dados a carregar.
  - tipo: int
- **`height`**: Altura dos dados a carregar.
  - tipo: int
- **`positionX`**: Borda esquerda da região onde desenhar.
  - tipo: int
- **`positionY`**: Borda de cima da região onde desenhar.
  - tipo: int
- **`mode`**: Modo de desenho; veja `Image Blending Modes`_.
  - tipo: int

#### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### Classe `ImageMirror(scene, observer, mirror, material=0, width, height, samples, hdr)`

Fonte de imagem a partir de um espelho.

- **`scene`**: Cena de onde a imagem deve ser tirada.
  - tipo: `KX_Scene`
- **`observer`**: Objeto de referência do espelho (o objeto de onde o espelho é olhado, por exemplo uma câmera).
  - tipo: `KX_GameObject`
- **`mirror`**: Objeto que tem o espelho.
  - tipo: `KX_GameObject`
- **`material`**: ID do material do espelho usado no reflexo (opcional).
  - tipo: int
- **`width`**: Largura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`height`**: Altura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`samples`**: Amostras do buffer de render fora da tela (opcional).
  - tipo: integer
- **`hdr`**: Formato da imagem fora da tela (opcional).
  - tipo: One of `these constants`

#### alpha

Usa alpha na textura.

**Tipo:** bool

#### horizon

Cor do horizonte.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

#### zenith

Cor do zênite.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

#### background

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

Obsoleto; use `Range.texture.ImageMirror.horizon` ou `Range.texture.ImageMirror.zenith`.

#### updateShadow

Força a atualização do buffer de sombras se houver diferença entre a imagem renderizada e as sombras.

**Tipo:** bool

#### colorBindCode

Bind code da textura de cor fora da tela.

**Tipo:** integer

#### capsize

Tamanho da área de render.

**Tipo:** sequence of two ints

#### clip

Distância de recorte.

**Tipo:** float in [0.01, 5000.0]

#### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Espelha a imagem na vertical.

**Tipo:** bool

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### refresh(buffer=None, format="RGBA")

Atualiza a imagem: renderiza e copia a imagem para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é renderizada e copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

#### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

#### whole

Usa a viewport inteira no render.

**Tipo:** bool

### Classe `ImageMix`

Mixer de imagens, usado para misturar várias fontes de imagem.

#### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Espelha a imagem na vertical.

**Tipo:** bool

#### getSource(id)

Pega a fonte de imagem.

- **`id`**: Identificador da fonte a pegar.
  - tipo: str

**Retorna:** Fonte de imagem.

**Tipo do retorno:** one of... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

#### getWeight(id)

Pega o peso da fonte de imagem.

- **`id`**: Identificador da fonte.
  - tipo: str

**Retorna:** Peso da fonte.

**Tipo do retorno:** int

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### refresh(buffer=None, format="RGBA")

Atualiza a imagem: calcula e copia a imagem para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é calculada e copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

#### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### setSource(id, image)

Define a fonte de imagem; todas as fontes precisam ter o mesmo tamanho.

- **`id`**: Identificador da fonte a definir.
  - tipo: str
- **`image`**: Fonte de imagem do tipo... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

#### setWeight(id, weight)

Define o peso da fonte de imagem; a soma dos pesos deve ser 256 para ter intensidade de cor completa na saída.

- **`id`**: Identificador da fonte.
  - tipo: str
- **`weight`**: Peso da fonte.
  - tipo: int

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

### Classe `ImageRender(scene, camera, width, height, samples, hdr)`

Fonte de imagem a partir do render de uma câmera não ativa. O render é feito num framebuffer object personalizado se fbo for passado; senão, no framebuffer padrão.

- **`scene`**: Cena de onde a imagem deve ser tirada.
  - tipo: `KX_Scene`
- **`camera`**: Câmera de onde a imagem deve ser tirada.
  - tipo: `KX_Camera`
- **`width`**: Largura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`height`**: Altura do buffer de render fora da tela (opcional).
  - tipo: integer
- **`samples`**: Amostras do buffer de render fora da tela (opcional).
  - tipo: integer
- **`hdr`**: Formato da imagem fora da tela (opcional).
  - tipo: One of `these constants`

#### alpha

Usa alpha na textura.

**Tipo:** bool

#### horizon

Cor do horizonte.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

#### zenith

Cor do zênite.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

#### background

Cor de fundo.

**Tipo:** float list [r, g, b, a] in [0.0, 1.0]

Obsoleto; use `Range.texture.ImageRender.horizon` ou `Range.texture.ImageRender.zenith`.

#### updateShadow

Força a atualização do buffer de sombras se houver diferença entre a imagem renderizada e as sombras.

**Tipo:** bool

#### colorBindCode

Bind code da textura de cor fora da tela.

**Tipo:** integer

#### capsize

Tamanho da área de render.

**Tipo:** sequence of two ints

#### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Espelha a imagem na vertical.

**Tipo:** bool

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

#### whole

Usa a viewport inteira no render.

**Tipo:** bool

#### depth

Usa o componente de profundidade do render como array de float; não serve como fonte de textura, só deve ser usado com Range.texture.imageToArray(mode='F').

**Tipo:** bool

#### zbuff

Usa o componente de profundidade do render como cor em tons de cinza; serve como fonte de textura.

**Tipo:** bool

#### render()

Renderiza a cena, mas ainda não extrai os pixels. A função volta assim que os comandos de render são enviados à GPU. O render continua assíncrono na GPU enquanto o host faz outras tarefas. Para terminar o render, chame `refresh` diretamente ou atualize a textura da qual este objeto é a fonte. Este método serve para fazer render assíncrono com o melhor desempenho: chame render() no frame n e refresh() no frame n+1, para dar o máximo de tempo à GPU para renderizar enquanto a game engine faz outras tarefas.

**Retorna:** True se o render foi iniciado, False se não dá para renderizar (por exemplo, a câmera está ativa)

**Tipo do retorno:** bool

#### refresh()

#### refresh(buffer, format="RGBA")

Atualiza: renderiza e, se quiser, copia a imagem para um buffer externo, depois invalida o conteúdo atual. O render pode ter sido iniciado antes com o método `render`; nesse caso esta função só espera as operações de render terminarem. Chamada sem argumento, os pixels não são extraídos, mas o render com certeza está completo quando a função volta. Isso só faz sentido com render fora da tela num alvo de textura (veja `offScreenCreate`).

- **`buffer`**: Um objeto que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada. A transferência para o buffer é ideal se a imagem não precisar de processamento, o que acontece com `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` e nenhum filtro.
  - tipo: any buffer type of sufficient size
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

**Retorna:** True se o render terminou, False se não dá para renderizar (por exemplo, a câmera está ativa)

**Tipo do retorno:** bool

### Classe `ImageViewport`

Fonte de imagem a partir da viewport renderizada pela câmera ativa. Para renderizar de uma câmera não ativa, veja `ImageRender`.

#### alpha

Usa alpha na textura.

**Tipo:** bool

#### capsize

Tamanho da área da viewport capturada.

**Tipo:** sequence of two ints

#### filter

Filtro de pixels.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Espelha a imagem na vertical.

**Tipo:** bool

#### image

Dados da imagem (somente leitura).

**Tipo:** `Buffer` or None

#### position

Canto superior esquerdo da área capturada.

**Tipo:** sequence of two ints

#### refresh(buffer=None, format="RGBA")

Atualiza: copia a viewport para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada. A transferência para o buffer é ideal se a imagem não precisar de processamento, o que acontece com `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` e nenhum filtro.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

#### scale

Escala rápida da imagem (vizinho mais próximo).

**Tipo:** bool

#### size

Tamanho da imagem (somente leitura).

**Tipo:** tuple of two ints

#### valid

Diz se há uma imagem disponível (somente leitura).

**Tipo:** bool

#### whole

Usa a viewport inteira na captura.

**Tipo:** bool

#### depth

Usa o componente de profundidade da viewport como array de float; não serve como fonte de textura, só deve ser usado com `Range.texture.imageToArray(mode='F')`.

**Tipo:** bool

#### zbuff

Usa o componente de profundidade da viewport como cor em tons de cinza; serve como fonte de textura.

**Tipo:** bool

### Classe `VideoDeckLink(format, capture=0)`

Fonte de imagem de um stream de vídeo externo capturado com uma placa DeckLink da Black Magic Design. Antes de usar esta fonte, é preciso instalar um dispositivo DeckLink (placa PCIe ou dispositivo USB) e o pacote 'Desktop Video' (versão 10.4 ou mais nova) no host, como descrito na documentação da DeckLink. Se você também tiver uma placa nVidia Quadro recente, pode aproveitar a tecnologia 'GPUDirect' para enviar os frames capturados à GPU de forma bem eficiente. Para isso, instale o 'DeckLink SDK' versão 10.4 ou mais nova e copie a biblioteca 'dvp.dll' para a pasta de instalação do Blender ou para outro lugar de onde o Blender consiga carregar uma DLL.

- **`format`**: string que descreve o formato de vídeo a capturar.
  - tipo: str
- **`capture`**: Número da placa de onde o vídeo de entrada deve ser capturado.
  - tipo: int
O argumento format deve ser escrito como `<displayMode>/<pixelFormat>[/3D][:<cacheSize>]`, em que `<displayMode>` descreve o tamanho e a taxa do frame e <pixelFormat> a codificação dos pixels. O sufixo opcional `/3D` é usado se o stream for estéreo, com imagens de olho esquerdo e direito. O sufixo opcional `:<cacheSize>` define quantos frames ficam em cache, 8 por padrão. Algumas placas DeckLink não funcionam abaixo de um certo tamanho de cache. O padrão 8 deve servir para todas as placas. Dá para tentar diminuir o cache para usar menos memória. Por exemplo, a 4K Extreme funciona com só 3 frames, a Extreme 2 precisa de 4 e a Intensity Shuttle de 6, e assim por diante. Diminuir o cache pode ajudar quando a DeckLink é usada com GPUDirect: nesse caso todos os frames precisam ficar travados na memória, o que pesa muito. Se diminuir demais, não dá erro, mas também não chega vídeo.

Os valores válidos de `<displayMode>` vêm do enum `BMDDisplayMode` da API DeckLink, sem o prefixo 'bmdMode'. Se um modo que não está nesta lista for adicionado numa versão futura do SDK, também dá para passar as 4 letras do código interno desse modo. O código interno está no arquivo `DeckLinkAPIModes.h`, que faz parte do SDK. Para referência, esta é a lista completa dos modos de exibição suportados com o código interno equivalente:

Códigos internos
- NTSC 'ntsc'
- NTSC2398 	'nt23'
- PAL		'pal '
- NTSCp		'ntsp'
- PALp		'palp'
Modos HD 1080
- HD1080p2398	'23ps'
- HD1080p24	'24ps'
- HD1080p25	'Hp25'
- HD1080p2997	'Hp29'
- HD1080p30	'Hp30'
- HD1080i50	'Hi50'
- HD1080i5994	'Hi59'
- HD1080i6000	'Hi60'
- HD1080p50	'Hp50'
- HD1080p5994	'Hp59'
- HD1080p6000	'Hp60'
Modos HD 720
- HD720p50	'hp50'
- HD720p5994	'hp59'
- HD720p60	'hp60'
Modos 2k
- 2k2398	'2k23'
- 2k24		'2k24'
- 2k25		'2k25'
Modos 4k
- 4K2160p2398	'4k23'
- 4K2160p24	'4k24'
- 4K2160p25	'4k25'
- 4K2160p2997	'4k29'
- 4K2160p30	'4k30'
- 4K2160p50	'4k50'
- 4K2160p5994	'4k59'
- 4K2160p60	'4k60'

A maioria dos nomes é autoexplicativa. Se precisar, consulte a documentação da API DeckLink para mais informações.

Do mesmo jeito, <pixelFormat> vem do enum BMDPixelFormat.

Para referência, esta é a lista completa dos formatos de pixel suportados com o código interno equivalente:

Formatos de pixel
- 8BitYUV	'2vuy'
- 10BitYUV	'v210'
- 8BitARGB	* sem código equivalente *
- 8BitBGRA	'BGRA'
- 10BitRGB	'r210'
- 12BitRGB	'R12B'
- 12BitRGBLE	'R12L'
- 10BitRGBXLE	'R10l'
- 10BitRGBX	'R10b'

Consulte a documentação do DeckLink SDK para a descrição completa desses formatos de pixel. É importante entendê-los, porque a decodificação dos pixels NÃO é feita no VideoTexture, por desempenho. Em vez disso, é preciso usar um shader específico para decodificar o pixel na GPU. Só os formatos '8BitARGB', '8BitBGRA' e '10BitRGBXLE' são mapeados direto para texturas OpenGL RGB float. Os formatos '8BitYUV' e '10BitYUV' são mapeados para textura OpenGL RGB float, mas precisam de shader para decodificar. Os outros formatos são enviados como textura `GL_RED_INTEGER` (ou seja, uma textura só com o canal vermelho, codificado como inteiro sem sinal de 32 bits) e não são recomendados.

Exemplo: `HD1080p24/10BitYUV/3D:4` equivale a `24ps/v210/3D:4` e representa um vídeo estéreo full HD a 24 frames por segundo, com cache de 4 frames.

Embora alguns dispositivos DeckLink consigam detectar o formato de vídeo sozinhos, essa API NÃO está implementada na BGE. Por isso é importante passar a string de formato que corresponde exatamente ao vídeo. Se o formato estiver errado, nenhum frame é capturado. Repare que o formato de pixel que você precisa passar não é necessariamente o formato real do vídeo. Por exemplo, a placa 4K Extreme entrega pixels RGB de 8 bits no formato '10BitRGBXLE'. Use o aplicativo 'Media Express', que vem com o 'Desktop Video', para descobrir qual formato de pixel funciona com um stream de vídeo.

#### status

Status da captura: 1=pronta para uso, 2=capturando, 3=parada

**Tipo:** int

#### framerate

Frame rate da captura, calculado a partir do formato de vídeo.

**Tipo:** float

#### valid

Diz se o atributo image pode ser usado para pegar a imagem. Sempre False nesta implementação (a imagem não fica disponível no Python)

**Tipo:** bool

#### image

Os dados da imagem. Sempre None nesta implementação.

**Tipo:** `Buffer` or None

#### size

O tamanho do frame em pixels. Frames estéreo têm o dobro da altura do frame de vídeo, ou seja, o 3D chega à GPU como uma única imagem em ordem de cima para baixo, com o olho esquerdo em cima.

**Tipo:** (int,int)

#### scale

Não usado neste objeto.

**Tipo:** bool

#### flip

Não usado neste objeto.

**Tipo:** bool

#### filter

Não usado neste objeto.

#### play()

Inicia a captura depois de criar o objeto.

**Retorna:** True se a captura começou, False se não.

**Tipo do retorno:** bool

#### pause()

Para a captura temporariamente. Use play() para reiniciar.

**Retorna:** True se a captura foi pausada, False se não.

**Tipo do retorno:** bool

#### stop()

Para a captura.

**Retorna:** True se a captura foi parada, False se não.

**Tipo do retorno:** bool

### Classes de textura

### Classe `Texture(gameObj, materialID=0, textureID=0, textureObj=None)`

Classe que cria o objeto `Texture`, que carrega a textura dinâmica na GPU.

- **`gameObj`**: Game object em que a textura de vídeo será criada.
  - tipo: `KX_GameObject`
- **`materialID`**: ID do material; o padrão 0 é o primeiro material (opcional).
  - tipo: int
- **`textureID`**: Índice da textura em caso de canal de multitextura; 0 = primeiro canal por padrão. Em textura UV, este parâmetro deve ser sempre 0 (opcional).
  - tipo: int
- **`textureObj`**: Referência a outro objeto `Texture` com bindId compartilhado, se você quiser reaproveitar a textura. Se usar este argumento, não crie nenhuma fonte nesta textura nem precisa atualizá-la: o outro objeto `Texture` fornece a textura para os dois materiais/texturas (opcional).
  - tipo: `Texture`

#### bindId

Nome de bind OpenGL (somente leitura).

**Tipo:** int

#### close()

Fecha a textura dinâmica e restaura a original.

#### mipmap

Textura com mipmap.

**Tipo:** bool

#### refresh(refresh_source, timestamp=-1.0)

Atualiza a textura a partir da fonte.

- **`refresh_source`**: Se também deve atualizar a fonte de imagem da textura.
  - tipo: bool
- **`timestamp`**: Se a textura controla um objeto VideoFFmpeg: timestamp (em segundos desde o início do filme) do frame a carregar; serve para sincronizar vídeo e som passando `time` a ele (opcional).
  - tipo: float

#### source

Fonte da textura.

**Tipo:** one of... * `VideoFFmpeg` * `VideoDeckLink` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

### Classe `DeckLink(cardIdx=0, format="")`

Alguns dispositivos DeckLink podem ser usados para reproduzir vídeo: o host envia frames regularmente para reprodução imediata ou agendada. O vídeo sai pelas interfaces HDMI ou SDI. Esta classe suporta o modo de reprodução imediata: ela tem um atributo source que recebe um dos objetos de fonte do módulo Range.texture. Atualizar o objeto DeckLink faz a fonte de imagem ser calculada e enviada ao dispositivo DeckLink para transmissão imediata nas interfaces de saída. Keying é suportado: permite compor o frame com um vídeo de entrada que passa pela placa DeckLink.

- **`cardIdx`**: Número da placa usada na saída (0 = primeira placa). Repare que os dispositivos DeckLink costumam ser half duplex: servem para captura ou para reprodução, mas não as duas ao mesmo tempo.
  - tipo: int
- **`format`**: String que representa o modo de exibição do vídeo de saída.
  - tipo: str
O valor padrão do argumento format é reservado para detecção automática, mas isso ainda não é suportado (gera erro em tempo de execução), então o formato de vídeo precisa ser passado explicitamente. Se o objetivo for keying (veja os atributos de keying), o formato precisa corresponder exatamente ao vídeo de entrada; senão, pode ser qualquer formato suportado pelo dispositivo (dá erro em tempo de execução se não for). O formato da string é `<displayMode>[/3D]`.

Veja `VideoDeckLink` para a lista de `<displayMode>` aceitos. O sufixo opcional `/3D` cria um vídeo 3D estéreo. Nesse caso, o atributo 'right' também precisa ser definido com a fonte de imagem do olho direito.

Nota: o formato de pixel não é passado aqui porque é sempre BGRA. O canal alpha é usado no keying para misturar a fonte com o vídeo de entrada; fora isso, não é usado. Se for preciso converter para o formato de vídeo nativo, isso é feito dentro do driver ou do dispositivo DeckLink.

#### source

Este atributo precisa receber uma das fontes de imagem. Se o tamanho da imagem não bater exatamente com o do frame, o atributo extend decide o que fazer.

Para o melhor desempenho, a imagem de origem deve ter exatamente o tamanho do frame de saída. Fica ainda mais rápido se a fonte de imagem for ImageViewport ou ImageRender com viewport inteira, flip desligado e sem filtro: o frame buffer GL é copiado direto para o buffer da imagem e dali direto para a placa DeckLink (sem cópias de buffer para buffer dentro do VideoTexture).

**Tipo:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

#### right

Se o formato de vídeo for 3D estéreo, este atributo deve receber uma fonte de imagem que produz as imagens do olho direito. Para renderizar a cena da BGE em 3D, dá para usar 2 câmeras, uma para cada olho, com 2 ImageRender e um buffer de render fora da tela do tamanho do frame de vídeo.

**Tipo:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

#### keying

Diz se o keying está ligado. False (padrão): o frame de saída vai sem mudança para a interface de saída (nesse caso não é preciso vídeo de entrada). True: o frame de saída é misturado com o vídeo de entrada, usando o canal alpha para combinar as duas imagens, e o resultado vai para a interface de saída.

**Tipo:** bool

#### level

Com keying ligado, define o nível de keying de 0 a 255. Este valor é um alpha global que multiplica o canal alpha da fonte de imagem. Use 255 (o padrão) para manter o canal alpha como está, ou 0 para deixar o frame de saída totalmente transparente.

**Tipo:** int

#### extend

Define como a fonte de imagem é mapeada se o tamanho não bater com o do frame de vídeo.
* False (o padrão): mapeia a imagem pixel a pixel.
Se a imagem for menor que o frame, o espaço em volta é preenchido com preto de alpha 0. Se for maior, a imagem é cortada para caber no frame.
* True: a imagem é escalada pelo algoritmo do vizinho mais próximo para caber no frame.
A escala é rápida, mas de baixa qualidade. Para o melhor resultado, ajuste sempre a fonte de imagem ao tamanho do vídeo de saída.

**Tipo:** bool

#### close()

Fecha o dispositivo DeckLink e libera todos os recursos. Depois deste método, o objeto não pode ser reativado; é preciso destruí-lo e criar um novo objeto DeckLink para reiniciar a saída.

#### refresh(refresh_source,ts)

Este método precisa ser chamado com frequência para atualizar o frame de saída no dispositivo DeckLink.

- **`refresh_source`**: True se o buffer de imagem das fontes deve ser invalidado depois de usado para calcular o frame de saída. Isso faz a imagem de origem ser recalculada no próximo refresh, que normalmente é o desejado. False se o buffer da fonte deve continuar válido e ser reaproveitado no próximo refresh. Repare que o dispositivo DeckLink guarda o frame de saída e repete até o host mandar um novo. Então não é preciso atualizar o objeto DeckLink se você sabe que a fonte de imagem não mudou.
  - tipo: bool
- **`ts`**: O timestamp passado ao objeto de fonte de imagem para calcular a imagem. Se não for passado, é usado o relógio da BGE.
  - tipo: float

### Classes de filtro

### Classe `FilterBGR24`

Filtro de origem BGR24.

### Classe `FilterBlueScreen`

Filtro de blue screen. Os canais RGB da cor ficam iguais, e o alpha de saída é obtido assim:

- se o quadrado da distância euclidiana entre a cor RGB
e a cor de referência do filtro for menor que o limite inferior do filtro, o alpha de saída vira 0;
- se esse quadrado for maior que o limite superior do filtro, o alpha de saída vira 255;
- senão, o alpha de saída é interpolado linearmente entre 0 e 255 no intervalo dos limites.

#### color

Cor de referência.

**Tipo:** sequence of three ints

**padrão:** (0, 0, 255)

#### limits

Limites da cor de referência.

**Tipo:** sequence of two ints

**padrão:** (64, 64)

#### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Classe `FilterColor`

Filtro de cálculo de cor. A cor de saída é obtida multiplicando a matriz 4x4 reduzida pela cor de entrada e somando a coluna restante ao resultado.

#### matrix

Matriz [4][5] para o cálculo de cor.

**Tipo:** sequence of four sequences of five ints

**padrão:** ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))

#### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Classe `FilterGray`

Filtro de tons de cinza. As proporções de R, G e B no cinza de saída são 28:151:77.

#### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Classe `FilterLevel`

Filtro de cálculo de níveis. Cada componente de cor de saída é obtido assim:

* se for menor que o valor mínimo correspondente, vira 0;

* se for maior que o valor máximo correspondente, vira 255;

* senão, é interpolado linearmente entre 0 e 255 no intervalo (min, max).

#### levels

Matriz de níveis [4] (min, max).

**Tipo:** sequence of four sequences of two ints

**padrão:** ((0, 255), (0, 255), (0, 255), (0, 255))

#### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Classe `FilterNormal`

Filtro de normal map.

#### colorIdx

Índice da cor usada para calcular a normal (0 - vermelho, 1 - verde, 2 - azul, 3 - alpha).

**Tipo:** int in [0, 3]

**padrão:** 0

#### depth

Profundidade do relevo.

**Tipo:** float

**padrão:** 4.0

#### previous

Filtro de pixels anterior.

**Tipo:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Classe `FilterRGB24`

Devolve um novo objeto de filtro de entrada para usar com `ImageBuff` quando a imagem passada à função `ImageBuff.load` tem o formato de pixel BGR de 3 bytes.

### Classe `FilterRGBA32`

Filtro de origem RGBA32.

### Funções

#### getLastError()

Último erro que aconteceu numa função de Range.texture.

**Retorna:** A descrição do último erro que aconteceu numa função de Range.texture.

**Tipo do retorno:** str

#### imageToArray(image, mode)

Devolve um `Buffer` com a imagem atual guardada num objeto de fonte de textura.

- **`image`**: Objeto de fonte de imagem do tipo: * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`
- **`mode`**: Argumento opcional com o formato de pixel. - Use os caracteres R, G e B para os 3 canais de cor, A para o canal alpha, 0 para forçar um canal fixo em 0 e 1 para forçar um canal fixo em 255. Exemplos: - "BGR" devolve 3 bytes por pixel com os canais azul, verde e vermelho nessa ordem. - "RGB1" devolve 4 bytes por pixel com os canais vermelho, verde e azul nessa ordem e o alpha forçado em 255. - O modo especial "F" devolve a imagem como array de float. Ele só deve ser usado para pegar o buffer de profundidade dos objetos `ImageViewport` e `ImageRender`. O modo padrão é "RGBA".
  - tipo: str

**Retorna:** Um objeto que representa a imagem como array de bytes de uma dimensão, de tamanho (pixel_size*width*height), linha por linha a partir de baixo da imagem. O tamanho e o formato do pixel vêm do parâmetro mode. No modo 'F', o array é de float, de uma dimensão, de tamanho (width*height).

**Tipo do retorno:** `Buffer`

#### materialID(object, name)

Devolve um valor numérico que pode ser usado em `Texture` para criar uma textura dinâmica.

O valor corresponde a um número interno de material que usa a textura identificada por name. name é uma string com o nome da textura com prefixo `IM`, se você quiser identificar a textura diretamente. Isto funciona para tex face básica e para material, desde que o material tenha um canal de textura usando essa textura na primeira posição da pilha de texturas. name também pode ter o prefixo `MA`, para identificar a textura pelo material. Nesse caso, o material precisa ter um canal de textura na primeira posição.

Se o objeto não tiver um material que corresponda a name, é gerado um erro em tempo de execução. Use try/except para pegar a exceção.

Ex.: `Range.texture.materialID(obj, 'IMvideo.png')`

- **`object`**: O game object que usa a textura que você quer tornar dinâmica.
  - tipo: `KX_GameObject`
- **`name`**: Nome da textura/material que você quer tornar dinâmico.
  - tipo: str

**Retorna:** O número interno do material.

**Tipo do retorno:** int

#### setLogFile(filename)

Define o nome de um arquivo de texto onde as mensagens de erro em tempo de execução serão gravadas, além de aparecerem no console Python. Só os erros específicos do módulo VideoTexture são gravados nesse arquivo; erros comuns não são.

- **`filename`**: Nome do arquivo de log de erros.
  - tipo: str

**Retorna:** -1 se o parâmetro name for inválido (não for string); senão, 0.

**Tipo do retorno:** int

### Constantes

### Status de vídeo e imagem do FFmpeg

#### SOURCE_ERROR

#### SOURCE_EMPTY

#### SOURCE_READY

#### SOURCE_PLAYING

#### SOURCE_STOPPED

### Modos de mistura de imagem

Veja [Blend Modes](https://en.wikipedia.org/wiki/Blend_modes) na Wikipédia para referência.

#### IMB_BLEND_MIX

#### IMB_BLEND_ADD

#### IMB_BLEND_SUB

#### IMB_BLEND_MUL

#### IMB_BLEND_LIGHTEN

#### IMB_BLEND_DARKEN

#### IMB_BLEND_ERASE_ALPHA

#### IMB_BLEND_ADD_ALPHA

#### IMB_BLEND_OVERLAY

#### IMB_BLEND_HARDLIGHT

#### IMB_BLEND_COLORBURN

#### IMB_BLEND_LINEARBURN

#### IMB_BLEND_COLORDODGE

#### IMB_BLEND_SCREEN

#### IMB_BLEND_SOFTLIGHT

#### IMB_BLEND_PINLIGHT

#### IMB_BLEND_VIVIDLIGHT

#### IMB_BLEND_LINEARLIGHT

#### IMB_BLEND_DIFFERENCE

#### IMB_BLEND_EXCLUSION

#### IMB_BLEND_HUE

#### IMB_BLEND_SATURATION

#### IMB_BLEND_LUMINOSITY

#### IMB_BLEND_COLOR

#### IMB_BLEND_COPY

#### IMB_BLEND_COPY_RGB

#### IMB_BLEND_COPY_ALPHA

---

## Range.track

Dados de pista gravados pelo Track Tool (`Range.track`; `bge.track` também funciona).

A ferramenta do editor grava uma tabela por amostra do traçado da pista no Text `TRACK_<name>.json` (formato versão 1, veja `docs/plano-track-tool.md`). No jogo, a engine lê esse Text do arquivo carregado (e dos arquivos carregados com `Range.logic.LibLoad`) na primeira vez que `get` pede por ele, guarda pelo nome e responde as consultas em C++. Os resultados batem com a referência em Python puro `range_track.runtime` (scripts/modules) com diferença de até 1 mm.

As unidades são metros e radianos. "Esquerda" é o lado lateral positivo.

```python

import Range

track = Range.track.get("Pista_4")
s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
lap_progress = s / track.length
target = track.racingLine(s + 15.0)
```

#### get(name)

Pista gravada no Text `TRACK_<name>.json` do arquivo do jogo ou de um arquivo carregado com LibLoad. O nome do próprio Text (`"TRACK_Pista_4.json"`) também é aceito. Lida uma vez e guardada em cache; o cache acompanha LibLoad/LibFree e é limpo quando o jogo termina.

- **`name`**: nome da pista (o nome do objeto do traçado).
  - tipo: str

**Retorna:** a pista, ou None quando esse Text não existe.

**Tipo do retorno:** `Track` or None

**Erro:** o Text não é uma pista válida (a mensagem diz o que está errado).

#### names()

Nomes das pistas disponíveis nos arquivos carregados (Texts `TRACK_*.json`).

**Tipo do retorno:** list of str

#### fromJson(text, name="")

Pista montada a partir de um texto JSON no formato gravado (versão 1), para dados guardados em outro lugar.

- **`text`**: texto JSON.
  - tipo: str
- **`name`**: nome usado quando o JSON não tem `name`.
  - tipo: str

**Tipo do retorno:** `Track`

#### reload()

Esquece as pistas em cache: o próximo `get` lê o Text de novo.

### Classe `Track`

Pista gravada. Pegue uma com `get`; ela continua válida depois que o arquivo que a continha é liberado.

Posições podem ser um `mathutils.Vector` ou uma sequência de números. Só com `(x, y)` a altura é ignorada; com `z` a altura escolhe o nível certo em pontes e cruzamentos. `s` dá a volta num circuito fechado e fica preso em `[0, length]` numa pista aberta.

#### project(pos, near=None)

Projeção de uma posição na pista.

Para carros, passe o `s` do frame anterior como `near`: a busca fica a até 50 m dele, então o carro nunca pula para outro trecho da pista que passa perto (grampos, retas paralelas). Quando a posição está a mais de 15 m desse trecho (respawn, teleporte), a pista inteira é buscada, como sem `near`.

```python

s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
```

**Retorna:** `(s, side, dist)`: metros ao longo da pista, `1` à esquerda / `-1` à direita da linha central e a distância lateral até ela (>= 0).

**Tipo do retorno:** tuple (float, int, float)

#### pointAt(s)

Ponto da linha central em `s`.

**Tipo do retorno:** `mathutils.Vector`

#### tangentAt(s)

Direção 3D unitária do sentido da pista em `s`.

**Tipo do retorno:** `mathutils.Vector`

#### lateralAt(s)

Vetor horizontal unitário apontando para a esquerda em `s`.

**Tipo do retorno:** `mathutils.Vector`

#### bankAt(s)

Inclinação lateral (banking) em `s`, em radianos (positivo: a borda esquerda fica mais baixa).

**Tipo do retorno:** float

#### widthAt(s)

Meias larguras do asfalto em `s`.

**Retorna:** `(left, right)`

**Tipo do retorno:** tuple of 2 floats

#### edgeAt(s)

Distância lateral da faixa de borda externa (muro, guard rail) em `s`.

**Retorna:** `(left, right)`

**Tipo do retorno:** tuple of 2 floats

#### racingLine(s)

Ponto da linha de corrida em `s`, sobre a superfície inclinada.

**Tipo do retorno:** `mathutils.Vector`

#### isOnRoad(pos)

True quando `pos` está sobre o asfalto (dentro das meias larguras) e a até 3 m da superfície (altura ignorada sem `z`). Antes do início ou depois do fim de uma pista aberta: False.

**Tipo do retorno:** bool

#### surfaceAt(s)

Nome da superfície da amostra que começa o trecho em `s` (`""` quando a pista não tem nomes de superfície).

**Tipo do retorno:** str

#### name

Nome da pista.

**Tipo:** str

#### length

Comprimento da pista em metros.

**Tipo:** float

#### cyclic

True para um circuito fechado.

**Tipo:** bool

#### count

Número de amostras gravadas.

**Tipo:** int

#### surfaces

Nomes das superfícies.

**Tipo:** list of str

---

# Tipos

---

## BL_ActionActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`BL_ArmatureObject`](#bl_armatureobject), [`KX_AnimationEventManager`](#kx_animationeventmanager)

Os atuadores Action aplicam uma action a um ator.

```python
# Toca parte de uma ação em uma camada separada.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Action"]

act.action = "Wave"
act.frameStart = 1
act.frameEnd = 30
act.layer = 1
act.mode = Range.logic.KX_ACTIONACT_PLAY
cont.activate(act)
```

#### action

O nome da action a usar como action atual.

**Tipo:** string

#### frameStart

Define o frame inicial da animação.

**Tipo:** float

#### frameEnd

Define o frame final da animação.

**Tipo:** float

#### blendIn

Define o número de frames de animação gerados nas transições entre actions.

**Tipo:** float

#### priority

Define a prioridade deste atuador. Atuadores com número de prioridade menor sobrepõem os de número maior.

**Tipo:** integer

#### frame

Define o frame atual da animação.

**Tipo:** float

#### propName

Define a propriedade usada no modo de reprodução FromProp.

**Tipo:** string

#### mode

O modo de operação do atuador. Pode ser uma `destas constantes`.

**Tipo:** integer

#### useContinue

A opção continue das actions, True ou False. Com True, a action sempre toca de onde parou; senão, eventos negativos neste atuador voltam ela ao frame inicial.

**Tipo:** boolean

#### framePropName

O nome da propriedade que recebe o número do frame atual.

**Tipo:** string

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### layer

 `atributo`

Camada de animação (0 a 7) em que o atuador toca a ação. Camadas diferentes tocam ao mesmo tempo.

#### layerWeight

 `atributo`

Peso da camada, de 0.0 a 1.0: quanto esta ação se mistura com as camadas de baixo.

---

## BL_ArmatureActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Os atuadores Armature mudam a condição das constraints em armatures.

```python
# Troca o alvo de uma constraint de osso.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Armature"]

act.type = Range.logic.KX_ACT_ARMATURE_SETTARGET
act.target = Range.logic.getCurrentScene().objects["Ball"]
cont.activate(act)
```

```python
# Diminui a influência da constraint.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Armature"]

act.type = Range.logic.KX_ACT_ARMATURE_SETINFLUENCE
act.influence = 0.5
cont.activate(act)
```

#### type

O tipo de ação que o atuador executa quando está ativo.

Pode ser uma `destas constantes`

**Tipo:** integer

#### constraint

O objeto de constraint que este atuador controla.

**Tipo:** `BL_ArmatureConstraint`

#### target

O objeto que este atuador define como alvo principal da constraint que controla.

**Tipo:** `KX_GameObject`

#### subtarget

O objeto que este atuador define como alvo secundário da constraint que controla.

**Tipo:** `KX_GameObject`.

> **Note:**
Por enquanto, o único alvo secundário é o pole target das constraints IK.

#### weight

O peso que este atuador define na constraint que controla.

**Tipo:** float.

> **Note:**
Por enquanto só a constraint IK tem peso. Deve ser um valor entre 0 e 1.

> **Note:**
Peso 0 desliga a constraint, mas continua atualizando os valores dela em tempo de execução (veja `BL_ArmatureConstraint`)

#### influence

A influência que este atuador define na constraint que controla.

**Tipo:** float.

---

## BL_ArmatureBone

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Proxy para a estrutura de bone do Blender. Todos os campos são somente leitura e seguem os nomes do RNA. Todos os atributos de espaço correspondem à rest pose.

```python
# Lista os ossos com o tamanho e o pai.
import Range

armature = Range.logic.getCurrentController().owner

for channel in armature.channels:
    bone = channel.bone
    parent = bone.parent.name if bone.parent else "-"
    print(bone.name, bone.length, parent)
```

#### name

nome do bone.

**Tipo:** string

#### connected

true quando a cabeça do bone está presa à cauda do pai.

**Tipo:** boolean

#### hinge

true quando o bone não herda rotação nem escala do bone pai.

**Tipo:** boolean

#### inherit_scale

true quando o bone herda a escala do bone pai.

**Tipo:** boolean

#### bbone_segments

número de segmentos de B-bone.

**Tipo:** integer

#### roll

rotação do bone em torno do eixo cabeça-cauda.

**Tipo:** float

#### head

posição da cabeça do bone no espaço do bone pai.

**Tipo:** vector [x, y, z]

#### tail

posição da cabeça do bone no espaço do bone pai.

**Tipo:** vector [x, y, z]

#### length

comprimento do bone.

**Tipo:** float

#### arm_head

posição da cabeça do bone no espaço da armature.

**Tipo:** vector [x, y, z]

#### arm_tail

posição da cauda do bone no espaço da armature.

**Tipo:** vector [x, y, z]

#### arm_mat

matriz da cabeça do bone no espaço da armature.

**Tipo:** matrix [4][4]

> **Note:**
Esta matriz não tem parte de escala.

#### bone_mat

matriz de rotação do bone no espaço do bone pai.

**Tipo:** matrix [3][3]

#### parent

bone pai, ou None para o bone raiz.

**Tipo:** `BL_ArmatureBone`

#### children

lista dos filhos do bone.

**Tipo:** list of `BL_ArmatureBone`

---

## BL_ArmatureChannel

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`BL_ArmatureObject`](#bl_armatureobject), [`BL_ArmatureBone`](#bl_armaturebone)

Proxy para um canal de pose da armature. Permite ler e definir a pose da armature. Os atributos são iguais aos do RNA, mas a maioria é somente leitura.

```python
# Gira a cabeça do personagem por script.
import Range

armature = Range.logic.getCurrentController().owner
head = armature.channels["Head"]

head.rotation_mode = Range.logic.ROT_MODE_XYZ
head.rotation_euler = (0.0, 0.0, 0.5)
armature.update()
```

```python
# Descobre onde um osso está no mundo.
import Range

armature = Range.logic.getCurrentController().owner
hand = armature.channels["Hand.R"]

print(armature.worldTransform * hand.pose_tail)
```

#### name

nome do canal (= nome do bone), somente leitura.

**Tipo:** string

#### bone

devolve o objeto bone correspondente a este canal de pose, somente leitura.

**Tipo:** `BL_ArmatureBone`

#### parent

devolve o canal pai, None se for o canal raiz, somente leitura.

**Tipo:** `BL_ArmatureChannel`

#### has_ik

true se o bone faz parte de uma cadeia IK ativa, somente leitura. Esta flag não é ligada quando uma constraint IK existe mas não está ativa (por exemplo, sem informação de alvo).

**Tipo:** boolean

#### ik_dof_x

true se o bone gira livre no eixo X, somente leitura.

**Tipo:** boolean

#### ik_dof_y

true se o bone gira livre no eixo Y, somente leitura.

**Tipo:** boolean

#### ik_dof_z

true se o bone gira livre no eixo Z, somente leitura.

**Tipo:** boolean

#### ik_limit_x

true se há limite na rotação X, somente leitura.

**Tipo:** boolean

#### ik_limit_y

true se há limite na rotação Y, somente leitura.

**Tipo:** boolean

#### ik_limit_z

true se há limite na rotação Z, somente leitura.

**Tipo:** boolean

#### ik_rot_control

true se a rotação do canal deve ser aplicada como constraint IK, somente leitura.

**Tipo:** boolean

#### ik_lin_control

true se o tamanho do canal deve ser aplicado como constraint IK, somente leitura.

**Tipo:** boolean

#### location

deslocamento da cabeça do bone no espaço local da armature, leitura e escrita.

**Tipo:** vector [X, Y, Z].

> **Note:**
Só dá para mover um bone se ele não estiver conectado ao pai. Uma action tocando na armature pode mudar o valor. Uma cadeia IK não atualiza este valor; veja joint_rotation.

> **Note:**
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`).

#### scale

escala do bone relativa ao pai, leitura e escrita.

**Tipo:** vector [sizeX, sizeY, sizeZ].

> **Note:**
Uma action tocando na armature pode mudar o valor. Uma cadeia IK não atualiza este valor; veja joint_rotation.

> **Note:**
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`)

#### rotation_quaternion

rotação do bone relativa ao pai, como quaternion, leitura e escrita.

**Tipo:** vector [qr, qi, qj, qk].

> **Note:**
Este campo só é usado se rotation_mode for 0. Uma action tocando na armature pode mudar o valor. Uma cadeia IK não atualiza este valor; veja joint_rotation.

> **Note:**
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`)

#### rotation_euler

rotação do bone relativa ao pai, como ângulos de Euler, leitura e escrita.

**Tipo:** vector [X, Y, Z].

> **Note:**
Este campo só é usado se rotation_mode for > 0. Passe os ângulos sempre na ordem [X, Y, Z]; a ordem em que são aplicados ao bone depende de rotation_mode. Uma action tocando na armature pode mudar este campo. Uma cadeia IK não atualiza este valor; veja joint_rotation.

> **Note:**
Mudar este campo não tem efeito imediato; a pose é atualizada quando a armature é atualizada durante o render (veja `BL_ArmatureObject.update`)

#### rotation_mode

Método de atualização da rotação do bone, leitura e escrita.

**Tipo:** integer (one of `these constants`)

#### channel_matrix

matriz da pose no espaço do bone (deformação do bone por action, constraint etc.), somente leitura. Este campo é atualizado depois do render e representa a pose atual.

**Tipo:** matrix [4][4]

#### pose_matrix

matriz da pose no espaço da armature, somente leitura. Este campo é atualizado depois do render e representa a pose atual.

**Tipo:** matrix [4][4]

#### pose_head

posição da cabeça do bone no espaço da armature, somente leitura.

**Tipo:** vector [x, y, z]

#### pose_tail

posição da cauda do bone no espaço da armature, somente leitura.

**Tipo:** vector [x, y, z]

#### ik_min_x

valor mínimo da rotação X em graus (<= 0) quando a rotação X é limitada (veja ik_limit_x), somente leitura.

**Tipo:** float

#### ik_max_x

valor máximo da rotação X em graus (>= 0) quando a rotação X é limitada (veja ik_limit_x), somente leitura.

**Tipo:** float

#### ik_min_y

valor mínimo da rotação Y em graus (<= 0) quando a rotação Y é limitada (veja ik_limit_y), somente leitura.

**Tipo:** float

#### ik_max_y

valor máximo da rotação Y em graus (>= 0) quando a rotação Y é limitada (veja ik_limit_y), somente leitura.

**Tipo:** float

#### ik_min_z

valor mínimo da rotação Z em graus (<= 0) quando a rotação Z é limitada (veja ik_limit_z), somente leitura.

**Tipo:** float

#### ik_max_z

valor máximo da rotação Z em graus (>= 0) quando a rotação Z é limitada (veja ik_limit_z), somente leitura.

**Tipo:** float

#### ik_stiffness_x

rigidez de rotação do bone no eixo X, somente leitura.

**Tipo:** float between 0 and 1

#### ik_stiffness_y

rigidez de rotação do bone no eixo Y, somente leitura.

**Tipo:** float between 0 and 1

#### ik_stiffness_z

rigidez de rotação do bone no eixo Z, somente leitura.

**Tipo:** float between 0 and 1

#### ik_stretch

proporção de mudança de escala permitida; 0 = o bone não muda de tamanho, somente leitura.

**Tipo:** float

#### ik_rot_weight

peso da constraint de rotação quando ik_rot_control está ligado, leitura e escrita.

**Tipo:** float between 0 and 1

#### ik_lin_weight

peso da constraint de tamanho quando ik_lin_control está ligado, leitura e escrita.

**Tipo:** float between 0 and 1

#### joint_rotation

Controla a rotação do bone em termos de ângulo de junta (para aplicações de robótica), leitura e escrita.

Ao escrever neste atributo, você passa um vetor [x, y, z] e um conjunto adequado de ângulos de Euler ou quaternion é calculado conforme rotation_mode.

Ao ler este atributo, a matriz da pose atual é convertida num vetor [x, y, z] que representa os ângulos da junta.

O valor e o significado de x, y e z dependem dos atributos ik_dof_x/ik_dof_y/ik_dof_z:

* Junta de 1 grau de liberdade X, Y ou Z: o valor x, y ou z correspondente é usado como ângulo da junta em radianos
* Junta de 2 graus de liberdade X+Y ou Z+Y: tratada como 2 juntas de 1 grau seguidas, primeiro X ou Z, depois Y. O valor x ou z é usado como ângulo da junta em radianos no eixo X ou Z, seguido de uma rotação de y radianos no novo eixo Y.
* Junta de 2 graus de liberdade X+Z: tratada como uma junta de 2 graus com eixo de rotação no plano X/Z. Os valores x e z são usados como coordenadas do vetor de rotação no plano X/Z.
* Junta de 3 graus de liberdade X+Y+Z: tratada como uma junta de revolução. O vetor [x, y, z] representa o vetor de rotação equivalente que leva a junta da rest pose à nova pose.

**Tipo:** vector [x, y, z]

> **Note:**
O bone precisa fazer parte de uma cadeia IK para você definir os atributos ik_dof_x/ik_dof_y/ik_dof_z pela UI, mas isso atrapalha este atributo, porque o solver de IK sobrescreve a pose. Dá para manter o controle da armature criando uma constraint IK sem terminá-la (por exemplo, sem definir alvo): o solver de IK não roda, mas o painel IK aparece na UI para cada bone da cadeia.

> **Note:**
[0, 0, 0] sempre corresponde à rest pose.

> **Note:**
É preciso pedir a atualização da pose da armature e esperar o próximo frame gráfico para ver o efeito deste atributo (veja `BL_ArmatureObject.update`).

> **Note:**
Depois de definir este atributo, dá para ler o resultado do cálculo nos atributos rotation ou euler_rotation.

---

## BL_ArmatureConstraint

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Proxy para uma constraint de armature. Permite mudar a constraint em tempo real. Obtido por `BL_ArmatureObject`.constraints.

> **Note:**
Nem todas as constraints de armature são suportadas na GE.

```python
# Desliga todas as constraints de um osso.
import Range

armature = Range.logic.getCurrentController().owner

for constraint in armature.constraints:
    if constraint.name.startswith("Hand.L"):
        constraint.enforce = 0.0
```

```python
# Troca o alvo e o peso de um IK.
import Range

armature = Range.logic.getCurrentController().owner
ik = armature.constraints["Foot.L:IK"]

ik.target = Range.logic.getCurrentScene().objects["FootTarget"]
ik.ik_weight = 1.0
```

#### type

Tipo da constraint (somente leitura).

Use uma `destas constantes`.

**Tipo:** integer, one of CONSTRAINT_TYPE_* constants

#### name

Nome da constraint, montado como <bone_name>:<constraint_name>, na lista constraints.

**Tipo:** string

Este nome também é a chave de índice em `BL_ArmatureObject`.

#### enforce

fração do efeito da constraint que é aplicada. Entre 0 e 1.

**Tipo:** float

#### headtail

Posição do alvo entre a cabeça e a cauda do bone alvo: 0=cabeça, 1=cauda.

**Tipo:** float.

> **Note:**
Só é usado se o alvo for um bone (ou seja, se o objeto alvo for uma armature).

#### lin_error

erro linear da constraint em tempo de execução (em unidades do Blender) no frame atual.

É um valor de tempo de execução, atualizado a cada frame pelo solver de IK. Só existe em constraints IK com o solver iTaSC.

**Tipo:** float

#### rot_error

Erro de rotação da constraint em tempo de execução (em radianos) no frame atual.

**Tipo:** float.

É um valor de tempo de execução, atualizado a cada frame pelo solver de IK. Só existe em constraints IK com o solver iTaSC.

Só é definido se a constraint tiver parte de rotação, por exemplo, uma constraint IK CopyPose+Rotation.

#### target

Objeto alvo principal da constraint. A posição deste objeto na GE é usada como alvo da constraint.

**Tipo:** `KX_GameObject`.

#### subtarget

Objeto alvo secundário da constraint. A posição deste objeto na GE é usada como alvo secundário da constraint.

**Tipo:** `KX_GameObject`.

Por enquanto isto só é usado como pole target em constraints IK.

#### active

True se a constraint está ativa.

**Tipo:** boolean

> **Note:**
Uma constraint inativa não atualiza lin_error nem rot_error.

#### ik_weight

Peso da constraint IK, entre 0 e 1.

Só definido para constraints IK.

**Tipo:** float

#### ik_type

Tipo de constraint IK (somente leitura).

Use uma `destas constantes`.

**Tipo:** integer.

#### ik_flag

Combinação das flags de opção da constraint IK (somente leitura).

Use uma `destas constantes`.

**Tipo:** integer

#### ik_dist

Distância que a constraint tenta manter do alvo; só usada quando ik_type=CONSTRAINT_IK_DISTANCE.

**Tipo:** float

#### ik_mode

Use uma `destas constantes`.

Modo adicional da constraint IK. Por enquanto só é usado na constraint Distance:

**Tipo:** integer

---

## BL_ArmatureObject

Classe base: [`KX_GameObject`](#kx_gameobject)

> **Veja também:**
[`BL_ArmatureChannel`](#bl_armaturechannel), [`BL_ArmatureBone`](#bl_armaturebone), [`BL_ArmatureConstraint`](#bl_armatureconstraint), [`BL_ActionActuator`](#bl_actionactuator)

Um objeto armature.

```python
# Soma uma rotação ao osso por cima da animação.
import Range

armature = Range.logic.getCurrentController().owner

armature.setBoneRotationOffset("Spine", (0.2, 0.0, 0.0))
```

```python
# Devolve o osso para a animação.
import Range

armature = Range.logic.getCurrentController().owner

armature.clearBoneRotationOffset("Spine")
```

```python
# Lista os canais.
import Range

armature = Range.logic.getCurrentController().owner

for channel in armature.channels:
    print(channel.name)
```

#### constraints

A lista de constraints de armature definidas nesta armature. Os elementos podem ser acessados por índice ou por string. O formato da chave em string é '<bone_name>:<constraint_name>'.

**Tipo:** list of `BL_ArmatureConstraint`

#### channels

A lista de canais da armature. Os elementos podem ser acessados por índice ou pelo nome do bone.

**Tipo:** list of `BL_ArmatureChannel`

#### update()

Garante que a armature será atualizada no próximo frame gráfico.

Isto não é necessário se um KX_ArmatureActuator no modo run estiver ativo ou se uma action estiver tocando. Use esta função nos outros casos. Ela precisa ser chamada a cada frame para garantir que a armature seja atualizada continuamente.

#### draw()

Desenha linhas que representam a armature, para vê-la em tempo real.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### clearBoneRotationOffset(bone=None)

 `método`

Remove a rotação extra de um osso, ou de todos quando `bone` é omitido.

#### setBoneRotationOffset(bone, rotation)

 `método`

Rotação extra num osso por cima das actions que estão tocando, no espaço local do osso. `rotation`: euler XYZ (3 valores, radianos) ou quaternion (4 valores, w x y z). Fica até `clearBoneRotationOffset()`.

---

## BL_Shader

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`KX_BlenderMaterial`](#kx_blendermaterial), [`KX_2DFilter`](#kx_2dfilter)

BL_Shader é uma classe usada para compilar e usar scripts de shader personalizados. Suporta vertex, fragment e geometry shaders. O shader é compilado com um cabeçalho gerado para os três scripts. Esse cabeçalho define a diretiva `#version`, então o usuário não deve definir a sua própria `#version`.

```python
# Troca o shader de um material e envia um valor para ele.
import Range

VERTEX = """
void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
"""

FRAGMENT = """
uniform float brightness;

void main()
{
    gl_FragColor = vec4(vec3(brightness), 1.0);
}
"""

own = Range.logic.getCurrentController().owner
material = own.meshes[0].materials[0]
shader = material.getShader()

if shader is not None and not shader.isValid():
    shader.setSource(VERTEX, FRAGMENT, True)

shader.setUniform1f("brightness", 0.8)
```

```python
# Deixa a engine preencher uma matriz ou a posição da câmera sozinha.
import Range

own = Range.logic.getCurrentController().owner
shader = own.meshes[0].materials[0].getShader()

shader.setUniformDef("cameraPosition", Range.logic.CAM_POS)
```

#### enabled

Liga o shader para uso.

**Tipo:** boolean

#### objectCallbacks

A lista de callbacks Python executados quando o shader é usado para renderizar um objeto. Todas as funções recebem como argumento o objeto sendo renderizado.

```python

def callback(object):
    print("render object %r" % object.name)
```

**Tipo:** list of functions and/or methods

#### bindCallbacks

A lista de callbacks Python executados quando o shader começa a ser usado no render.

**Tipo:** list of functions and/or methods

#### setUniformfv(name, fList)

Define um uniform com uma lista de valores float

- **`name`**: o nome do uniform
  - tipo: string
- **`fList`**: uma lista (2, 3 ou 4 elementos) de valores float
  - tipo: list[float]

#### delSource()

Limpa o shader. Use este método antes de mudar o código com `setSource`.

#### getFragmentProg()

Devolve o fragment program.

**Retorna:** O fragment program.

**Tipo do retorno:** string

#### getVertexProg()

Pega o vertex program.

**Retorna:** O vertex program.

**Tipo do retorno:** string

#### isValid()

Verifica se o shader é válido.

**Retorna:** True se o shader é válido

**Tipo do retorno:** boolean

#### setAttrib(enum)

Define a location do atributo. (O parâmetro é ignorado por enquanto e o valor de "tangent" é sempre usado.)

- **`enum`**: valor da location do atributo
  - tipo: integer

#### setSampler(name, index)

Define o índice de sampler de textura do uniform.

- **`name`**: Nome do uniform
  - tipo: string
- **`index`**: Índice do sampler de textura.
  - tipo: integer

#### setSource(vertexProgram, fragmentProgram, apply)

Define os programas de vertex e fragment

- **`vertexProgram`**: Vertex program
  - tipo: string
- **`fragmentProgram`**: Fragment program
  - tipo: string
- **`apply`**: Liga o shader.
  - tipo: boolean

#### setSourceList(sources, apply)

Define os programas de vertex, fragment e geometry shader.

- **`sources`**: Dicionário com todos os programas. As chaves `vertex`, `fragment` e `geometry` representam os programas de mesmo nome. `geometry` é opcional. Este dicionário pode ficar parecido com: .. code-block:: python sources = { "vertex" : vertexProgram, "fragment" : fragmentProgram, "geometry" : geometryProgram }
  - tipo: dict
- **`apply`**: Liga o shader.
  - tipo: boolean

#### setUniform1f(name, fx)

Define um uniform com 1 valor float.

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: Valor do uniform
  - tipo: float

#### setUniform1i(name, ix)

Define um uniform com um valor inteiro.

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: o valor do uniform
  - tipo: integer

#### setUniform2f(name, fx, fy)

Define um uniform com 2 valores float

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: primeiro valor float
  - tipo: float
- **`fy`**: segundo valor float
  - tipo: float

#### setUniform2i(name, ix, iy)

Define um uniform com 2 valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: primeiro valor inteiro
  - tipo: integer
- **`iy`**: segundo valor inteiro
  - tipo: integer

#### setUniform3f(name, fx, fy, fz)

Define um uniform com 3 valores float.

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: primeiro valor float
  - tipo: float
- **`fy`**: segundo valor float
  - tipo: float
- **`fz`**: terceiro valor float
  - tipo: float

#### setUniform3i(name, ix, iy, iz)

Define um uniform com 3 valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: primeiro valor inteiro
  - tipo: integer
- **`iy`**: segundo valor inteiro
  - tipo: integer
- **`iz`**: terceiro valor inteiro
  - tipo: integer

#### setUniform4f(name, fx, fy, fz, fw)

Define um uniform com 4 valores float.

- **`name`**: o nome do uniform
  - tipo: string
- **`fx`**: primeiro valor float
  - tipo: float
- **`fy`**: segundo valor float
  - tipo: float
- **`fz`**: terceiro valor float
  - tipo: float
- **`fw`**: quarto valor float
  - tipo: float

#### setUniform4i(name, ix, iy, iz, iw)

Define um uniform com 4 valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`ix`**: primeiro valor inteiro
  - tipo: integer
- **`iy`**: segundo valor inteiro
  - tipo: integer
- **`iz`**: terceiro valor inteiro
  - tipo: integer
- **`iw`**: quarto valor inteiro
  - tipo: integer

#### setUniformDef(name, type)

Define um novo uniform

- **`name`**: o nome do uniform
  - tipo: string
- **`type`**: tipo do uniform, uma `destas constantes`
  - tipo: integer

#### setUniformMatrix3(name, mat, transpose)

Define um uniform com uma matriz 3x3

- **`name`**: o nome do uniform
  - tipo: string
- **`mat`**: Uma matriz 3x3 [[f, f, f], [f, f, f], [f, f, f]]
  - tipo: 3x3 matrix
- **`transpose`**: use True para transpor a matriz
  - tipo: boolean

#### setUniformMatrix4(name, mat, transpose)

Define um uniform com uma matriz 4x4

- **`name`**: o nome do uniform
  - tipo: string
- **`mat`**: Uma matriz 4x4 [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
  - tipo: 4x4 matrix
- **`transpose`**: use True para transpor a matriz
  - tipo: boolean

#### setUniformiv(name, iList)

Define um uniform com uma lista de valores inteiros

- **`name`**: o nome do uniform
  - tipo: string
- **`iList`**: uma lista (2, 3 ou 4 elementos) de valores inteiros
  - tipo: list[integer]

#### setUniformEyef(name)

Define um uniform com um valor float que indica o olho sendo renderizado no modo estéreo: 0.0 para o olho esquerdo, 0.5 para o direito. Fora do modo estéreo, o valor fica fixo em 0.0. O uso típico é no modo estéreo, para ler texturas estéreo com as imagens dos olhos esquerdo e direito em ordem de cima para baixo.

- **`name`**: o nome do uniform
  - tipo: string

#### validate()

Valida o objeto de shader.

---

## BL_Texture

Classe base: [`EXP_Value`](#exp_value)

Um objeto de textura com os atributos de uma textura de material.

```python
# Faz a primeira textura do material deslizar.
import Range

own = Range.logic.getCurrentController().owner
texture = own.meshes[0].materials[0].textures[0]

offset = texture.uvOffset
offset.x += 0.01
texture.uvOffset = offset
```

```python
# Controla quanto a textura afeta a cor.
import Range

own = Range.logic.getCurrentController().owner
texture = own.meshes[0].materials[0].textures[0]

texture.diffuseFactor = 0.5
texture.emit = 1.0
```

#### diffuseIntensity

Quanto a textura afeta a refletividade difusa.

**Tipo:** float

#### diffuseFactor

Quanto a textura afeta a cor difusa.

**Tipo:** float

#### alpha

Quanto a textura afeta o alpha.

**Tipo:** float

#### specularIntensity

Quanto a textura afeta a refletividade especular.

**Tipo:** float

#### specularFactor

Quanto a textura afeta a cor especular.

**Tipo:** float

#### hardness

Quanto a textura afeta a hardness.

**Tipo:** float

#### emit

Quanto a textura afeta a emissão.

**Tipo:** float

#### mirror

Quanto a textura afeta a cor de espelho.

**Tipo:** float

#### normal

Quanto a textura afeta os valores de normal.

**Tipo:** float

#### parallaxBump

Altura do parallax occlusion mapping.

**Tipo:** float

#### parallaxStep

Número de passos para fazer o efeito de parallax.

**Tipo:** float

#### lodBias

Bias aplicado ao mipmapping.

**Tipo:** float

#### bindCode

Bind code/Id/número da textura.

**Tipo:** integer

#### renderer

Texture renderer desta textura.

**Tipo:** `KX_CubeMap`, `KX_PlanarMap` or None

#### ior

Índice de refração usado para calcular a refração.

**Tipo:** float (1.0 to 50.0)

#### refractionRatio

Quanto da refração é misturada com a reflexão.

**Tipo:** float (0.0 to 1.0)

#### uvOffset

Deslocamento aplicado às coordenadas UV da textura (principalmente translação nos eixos U e V).

**Tipo:** `mathutils.Vector`

#### uvSize

Escala aplicada às coordenadas UV da textura.

**Tipo:** `mathutils.Vector`

#### uvRotation

Rotação aplicada às coordenadas UV da textura.

**Tipo:** float (radians)

---

## EXP_BaseListValue

Classe `Range.types.EXP_BaseListValue`.

```python
# Procura um objeto sem erro caso ele não exista.
import Range

objects = Range.logic.getCurrentScene().objects

door = objects.get("Door")
if door is not None:
    print(objects.index(door))
```

```python
# Filtra por nome e propriedade. Os dois são expressões regulares.
import Range

objects = Range.logic.getCurrentScene().objects

for enemy in objects.filter("Enemy.*", "life"):
    print(enemy.name)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### append(item)

 `método`

Acrescenta um item no fim da lista. Só funciona em listas criadas pelo script; listas internas da engine (ex.: `scene.objects`) não podem ser alteradas.

#### count(item)

 `método`

Quantas vezes o item aparece na lista.

**Retorna:** `int`

#### filter(name, prop='')

 `método`

Nova lista só com os itens cujo nome contém `name` e que têm a propriedade de jogo `prop`. Pelo menos um dos dois precisa ser preenchido.

**Retorna:** `EXP_ListValue`

#### from_id(id)

 `método`

Procura o item pelo `id()` do Python. Útil para guardar a referência de um objeto como número.

**Retorna:** `object`

#### get(key, default=None)

 `método`

Item com esse nome, ou `default` se não existir. Ex.: `scene.objects.get('Player')`.

**Retorna:** `object`

#### index(item)

 `método`

Posição do item na lista. Dá erro se ele não estiver nela.

**Retorna:** `int`

#### reverse()

 `método`

Inverte a ordem da lista. Só em listas criadas pelo script.

---

## EXP_BaseListWrapper

Classe `Range.types.EXP_BaseListWrapper`.

```python
# Essas listas funcionam por nome ou por índice, como sensores ou canais.
import Range

armature = Range.logic.getCurrentController().owner

head = armature.channels.get("Head")
first = armature.channels[0]
print(head, first)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### get(key, default=None)

 `método`

Item com esse nome, ou `default` se não existir.

**Retorna:** `object`

---

## EXP_ListValue

Classe base: [`EXP_PropValue`](#exp_propvalue)

Este é um objeto parecido com lista, usado internamente pela game engine, que na maioria dos casos se comporta como uma lista Python.

Além da busca normal por índice (`val= clist[i]`), EXP_ListValue aceita busca por string (`val= scene.objects["Cube"]`)

Outras operações, como `len(clist)`, `list(clist)` e `clist[0:10]`, também são suportadas.

```python
# Percorre os objetos da cena.
import Range

objects = Range.logic.getCurrentScene().objects

for obj in objects:
    print(obj.name)
```

```python
# Procura um com valor padrão.
import Range

objects = Range.logic.getCurrentScene().objects

print(objects.get("Player", None))
print(len(objects.filter("Coin.*")))
```

#### append(val)

Adiciona um item à lista (como o append do Python)

> **Caution:**
Adicionar valores à lista pode travar o jogo quando a lista é usada internamente pela game engine.

#### count(val)

Conta quantas vezes um valor aparece na lista.

**Retorna:** número de ocorrências

**Tipo do retorno:** integer

#### index(val)

Devolve o índice de um valor na lista.

**Retorna:** O índice do valor na lista.

**Tipo do retorno:** integer

#### reverse()

Inverte a ordem da lista.

#### get(key, default=None)

Devolve o valor da chave, ou o valor padrão se a chave não existir.

**Retorna:** O valor da chave ou o padrão.

#### filter(name, prop)

Devolve uma lista dos itens cujo nome casa com a regex `name` e que têm uma propriedade que casa com a regex `prop`. Se `name` estiver vazio, todos os itens são verificados; se `prop` estiver vazio, as propriedades não são verificadas.

**Retorna:** A lista dos itens que casam.

#### from_id(id)

Esta é uma função feita para a game engine devolver um valor com um id específico.

Como os nomes de objeto nem sempre são únicos, o id de um objeto pode ser usado para pegá-lo no EXP_ValueList.

Exemplo:

```python

myObID=id(gameObject)
ob= scene.objects.from_id(myObID)
```

Em que `myObID` é um int ou long vindo da função id.

A vantagem é que dá para guardar o id em lugares onde não dá para guardar um gameObject.

> **Caution:**
O id vem de um endereço de memória e muda a cada vez que a game engine inicia.

> **Caution:**
O id não pode ser guardado como inteiro em propriedades de game object, porque elas têm um intervalo limitado em que o id pode não caber. Em vez disso, guarde o id como propriedade de jogo string e converta de volta para inteiro para usar no from_id.

---

## EXP_PropValue

Classe base: [`EXP_Value`](#exp_value)

Esta classe não tem funções Python

```python
# Esta é uma classe base interna e não está em Range.types. Confira a classe base pública.
import Range

own = Range.logic.getCurrentController().owner

print(isinstance(own, Range.types.EXP_Value))
```

---

## EXP_PyObjectPlus

EXP_PyObjectPlus é a classe base da maioria dos outros tipos da Game Engine.

```python
# Confere se um objeto não foi removido antes de usar uma referência guardada.
import Range

own = Range.logic.getCurrentController().owner
target = own.get("target")

if target is not None and not target.invalid:
    print(target.worldPosition)
```

#### invalid

Testa se o objeto foi liberado pela game engine e não é mais válido.

Normalmente isso não é problema, mas ao guardar dados da game engine no módulo GameLogic, em KX_Scenes ou em outros KX_GameObjects, é possível manter uma referência a dados inválidos. Chamar um atributo ou método de um objeto inválido levanta um SystemError.

O atributo invalid permite testar esse caso sem tratar exceções.

**Tipo:** boolean

---

## EXP_Value

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Esta classe é a base de outras classes.

```python
# Todo valor com nome tem o atributo name.
import Range

cont = Range.logic.getCurrentController()

print(cont.owner.name)
print(cont.name)
```

#### name

O nome deste objeto derivado de EXP_Value (somente leitura).

**Tipo:** string

---

## KX_2DFilter

Classe base: [`BL_Shader`](#bl_shader)

> **Veja também:**
[`KX_2DFilterManager`](#kx_2dfiltermanager), [`KX_2DFilterOffScreen`](#kx_2dfilteroffscreen), [`BL_Shader`](#bl_shader)

Objeto de shader de filtro 2D. Pode ser alterado com as funções de `BL_Shader`.

> **Caution:**
O vertex shader não deve aplicar as transformações de modelview e projeção. Ele deve ficar parecido com:

```glsl

void main()
{
    gl_Position = gl_Vertex;
}
```

#### mipmap

Pede a geração de mipmaps da textura de render `bgl_RenderedTexture`. Acessar um nível de mipmap fica parecido com:

```glsl

uniform sampler2D bgl_RenderedTexture;

void main()
{
    float level = 2.0; // mipmap level
    gl_FragColor = textureLod(bgl_RenderedTexture, gl_TexCoord[0].st, level);
}
```

**Tipo:** boolean

#### offScreen

O off screen personalizado em que o filtro renderiza (somente leitura).

**Tipo:** `Range.types.KX_2DFilterOffScreen` or None

#### setTexture(index, bindCode, samplerName="")

Coloca o bind code de textura `bindCode` no slot `index`. Toda chamada a `setTexture` deve vir seguida de uma chamada a `BL_Shader.setSampler` com o mesmo `index` se `sampleName` não for passado.

- **`index`**: O slot da textura.
  - tipo: integer
- **`bindCode`**: O bind code/Id da textura.
  - tipo: integer
- **`samplerName`**: O nome do sampler do shader ligado a `index`, se `samplerName` for passado à função (opcional).
  - tipo: string

#### setCubeMap(index, bindCode, samplerName="")

Coloca o bind code de textura cube map `bindCode` no slot `index`. Toda chamada a `setCubeMap` deve vir seguida de uma chamada a `BL_Shader.setSampler` com o mesmo `index` se `sampleName` não for passado.

- **`index`**: O slot da textura.
  - tipo: integer
- **`bindCode`**: O bind code/Id da textura cube map.
  - tipo: integer
- **`samplerName`**: O nome do sampler do shader ligado a `index`, se `samplerName` for passado à função (opcional).
  - tipo: string

#### addOffScreen(slots, depth=False, width=-1, height=-1, hdr=bge.render.HDR_NONE, mipmap=False)

Registra um off screen personalizado para o filtro renderizar.

- **`slots`**: O número de texturas de cor ligadas ao off screen, de 0 a 8 (8 excluído).
  - tipo: integer
- **`depth`**: True se o off screen usa uma textura de profundidade (opcional).
  - tipo: boolean
- **`width`**: A largura do off screen; -1 se ele pode ser redimensionado dinamicamente quando as dimensões da viewport mudam (opcional).
  - tipo: integer
- **`height`**: A altura do off screen; -1 se ele pode ser redimensionado dinamicamente quando as dimensões da viewport mudam (opcional).
  - tipo: integer
- **`hdr`**: A qualidade de imagem HDR das texturas de cor (opcional).
  - tipo: one of `these constants`
- **`mipmap`**: True se a textura de cor gera mipmaps no fim do render do filtro (opcional).
  - tipo: boolean

> **Note:**
Se o off screen é criado com tamanho dinâmico (`width` e `height` iguais a -1), os bind codes ficam indisponíveis até o próximo render do filtro e podem mudar quando a viewport é redimensionada.

#### removeOffScreen()

Remove o registro do off screen personalizado em que o filtro renderiza.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### recompile(fragmentProgram=None)

 `método`

Compila um novo código GLSL. Sem argumento, relê o arquivo de texto externo (se o filtro veio de um) ou recompila o código atual. Retorna `True` se deu certo; senão veja `compileLog`.

**Retorna:** `bool`

#### setUniform(name, value)

 `método`

Define um uniform do shader pelo nome. O tipo vem do shader (float, vec2-4, int, ivec2-4, bool, mat3, mat4 ou arrays deles). O valor continua valendo depois de um `recompile()`.

#### activeUniforms

*(novo na Anastacio)* `atributo · só leitura`

Lista dos uniforms usados pelo shader, como tuplas `(nome, tipo, tamanho)`.

#### compileLog

*(novo na Anastacio)* `atributo · só leitura`

Mensagens da última compilação do shader (erros e avisos). Vazio quando compilou sem problemas.

#### sourceName

*(novo na Anastacio)* `atributo · só leitura`

Nome do texto ou arquivo de onde veio o código do filtro.

#### sourcePath

*(novo na Anastacio)* `atributo · só leitura`

Caminho do arquivo externo `.glsl` do filtro; vazio quando o código está dentro do `.range`.

---

## KX_2DFilterManager

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`KX_2DFilter`](#kx_2dfilter), [`KX_2DFilterOffScreen`](#kx_2dfilteroffscreen), [`KX_Camera`](#kx_camera)

Gerenciador de filtros 2D, usado para adicionar, remover e achar filtros numa cena.

```python
# Adiciona um filtro pronto e depois um personalizado.
import Range

manager = Range.logic.getCurrentScene().filterManager

manager.addFilter(0, Range.logic.RAS_2DFILTER_SEPIA)

GLSL = """
uniform sampler2D bgl_RenderedTexture;
in vec4 bgl_TexCoord;
out vec4 fragColor;

void main()
{
    fragColor = texture(bgl_RenderedTexture, bgl_TexCoord.xy) * 0.5;
}
"""
manager.addFilter(1, Range.logic.RAS_2DFILTER_CUSTOMFILTER, GLSL)
```

```python
# Remove um filtro.
import Range

manager = Range.logic.getCurrentScene().filterManager

if manager.getFilter(0) is not None:
    manager.removeFilter(0)
```

```python
# Ajusta os efeitos das opções gráficas.
import Range

manager = Range.logic.getCurrentScene().filterManager

manager.changeBloomValues(True, 0.6, 0.8)
manager.changeFxaaValues(True)
manager.changeGrainValues(True, 0.1)
```

#### addFilter(index, type, fragmentProgram="", owner=None, mipmap=False)

Adiciona um filtro no passe `index`, do tipo `type`, com o fragment program se for filtro personalizado.

- **`index`**: O índice do passe do filtro.
  - tipo: integer
- **`type`**: O tipo do filtro, um destes: * `Range.logic.RAS_2DFILTER_BLUR` * `Range.logic.RAS_2DFILTER_DILATION` * `Range.logic.RAS_2DFILTER_EROSION` * `Range.logic.RAS_2DFILTER_SHARPEN` * `Range.logic.RAS_2DFILTER_LAPLACIAN` * `Range.logic.RAS_2DFILTER_PREWITT` * `Range.logic.RAS_2DFILTER_SOBEL` * `Range.logic.RAS_2DFILTER_GRAYSCALE` * `Range.logic.RAS_2DFILTER_SEPIA` * `Range.logic.RAS_2DFILTER_OUTLINE` * `Range.logic.RAS_2DFILTER_CUSTOMFILTER`
  - tipo: integer
- **`fragmentProgram`**: O fragment program do shader do filtro. Só é usado se `type` for `Range.logic.RAS_2DFILTER_CUSTOMFILTER`; se vazio ou omitido, o filtro é criado sem shader, esperando uma chamada a `BL_Shader.setSourceList` (opcional).
  - tipo: string
- **`owner`**: Objeto cujas propriedades de jogo alimentam os uniforms de mesmo nome, como no atuador Filter 2D (opcional).
  - tipo: `KX_GameObject`
- **`mipmap`**: Gera mipmaps da imagem de entrada do filtro (opcional).
  - tipo: boolean

**Retorna:** O filtro 2D.

**Tipo do retorno:** `KX_2DFilter`

#### setBuiltinFilterEnabled(type, enabled=True)

Liga ou desliga um filtro embutido, mantendo os valores atuais dele, como faz o atuador Filter 2D.

- **`type`**: `Range.logic.RAS_2DFILTER_FXAA`, `RAS_2DFILTER_BLOOM`, `RAS_2DFILTER_TONEMAP`, `RAS_2DFILTER_SSAO`, `RAS_2DFILTER_LIGHTSCATTER` ou `RAS_2DFILTER_SSR`.
  - tipo: integer
- **`enabled`**: O novo estado.
  - tipo: boolean

**Retorna:** False quando o filtro não está disponível.

**Tipo do retorno:** boolean

#### removeFilter(index)

Remove o filtro do passe `index`.

- **`index`**: O índice do passe do filtro.
  - tipo: integer

#### getFilter(index)

Devolve o filtro do passe `index`.

**aviso:** Se o filtro 2D for adicionado por um `SCA_2DFilterActuator`, ele só fica disponível depois que o programa do filtro 2D for linkado. O script Python que pega o filtro precisa rodar um frame depois. Dá para usar um sensor Delay.

- **`index`**: O índice do passe do filtro.
  - tipo: integer

**Retorna:** O filtro no passe indicado, ou None.

**Tipo do retorno:** `KX_2DFilter` or None

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### changeBloomValues(enabled, intensity, threshold)

 `método`

Liga/desliga o Bloom da cena e muda intensidade e limiar de brilho.

#### changeFxaaValues(enabled)

 `método`

Liga ou desliga o FXAA (anti-serrilhado) da cena.

#### changeGrainValues(enabled, strength)

 `método`

Liga/desliga o grão de filme e muda a força.

#### changeLightScatterValues(enabled, step_max, step_size, threshold, intensity)

 `método`

Liga/desliga os raios de luz (light scattering) e muda passos, tamanho do passo, limiar e intensidade.

#### changeSSAOValues(enabled, samples, strength, distance, attenuation)

 `método`

Liga/desliga a oclusão de ambiente (SSAO) e muda amostras, força, distância e atenuação.

#### changeSSGIValues(enabled, radius=3.0, strength=1.0, rays=4, steps=8, thickness=0.1, divisor=0)

 `método`

Liga/desliga a iluminação global em tela (SSGI) e muda seus parâmetros. `divisor` 1, 2 ou 4 muda a resolução do traçado; 0 mantém. O SSGI precisa estar ligado na cena antes do Play.

#### changeSSRValues(enabled, step_max, bias, max_distance)

 `método`

Liga/desliga os reflexos em tela (SSR) e muda passos, bias e distância máxima.

#### changeTonemapValues(enabled, exposure, gamma)

 `método`

Liga/desliga o tonemap e muda exposição e gamma.

#### compositor

*(novo na Anastacio)* `atributo · só leitura`

Filtro gerado pela árvore do Compositor da cena (Use Nodes). Nós Value e RGB mudam ao vivo com `compositor.setUniform()`. Só leitura.

#### fxaaEdgeThreshold

*(novo na Anastacio)* `atributo`

Contraste mínimo, relativo, para uma borda receber FXAA, de 0.0 a 1.0. Valores menores suavizam mais bordas.

#### fxaaEdgeThresholdMin

*(novo na Anastacio)* `atributo`

Contraste mínimo absoluto para o FXAA agir, de 0.0 a 1.0. Evita processar áreas escuras.

#### fxaaEnabled

*(novo na Anastacio)* `atributo`

Liga ou desliga o FXAA da cena (Scene > Post-process). `True` ou `False`.

#### fxaaSearchSteps

*(novo na Anastacio)* `atributo`

Número de passos da busca de bordas do FXAA (inteiro, a partir de 2). Mais passos pegam bordas mais longas e custam mais.

#### fxaaSubpix

*(novo na Anastacio)* `atributo`

Quanto o FXAA suaviza detalhes menores que um pixel, de 0.0 a 1.0.

#### grainEnabled

*(novo na Anastacio)* `atributo`

Liga ou desliga o grão de filme da cena.

#### grainStrength

*(novo na Anastacio)* `atributo`

Força do grão de filme, de 0.0 a 1.0.

#### taaEnabled

*(novo na Anastacio)* `atributo`

Liga ou desliga o TAA (anti-aliasing temporal) da cena (Render > TAA). `True` ou `False`. Suaviza bordas misturando quadros com a câmera levemente deslocada Em tela dividida e em estéreo só a nitidez é aplicada.

#### taaSharpen

*(novo na Anastacio)* `atributo`

Nitidez aplicada depois do TAA, de 0.0 a 1.0 (padrão 0.25). Compensa o leve desfoque da mistura de quadros.

---

## KX_2DFilterOffScreen

Classe base: [`EXP_Value`](#exp_value)

Off screen personalizado de filtro 2D.

```python
# Lê o tamanho da imagem em que um filtro escreve.
import Range

manager = Range.logic.getCurrentScene().filterManager
offScreen = manager.getFilter(0).offScreen

if offScreen is not None:
    print(offScreen.width, offScreen.height)
    print(offScreen.colorBindCodes, offScreen.depthBindCode)
```

#### width

A largura do off screen; -1 se o off screen pode ser redimensionado dinamicamente (somente leitura).

**Tipo:** integer

#### height

A altura do off screen; -1 se o off screen pode ser redimensionado dinamicamente (somente leitura).

**Tipo:** integer

#### colorBindCodes

O bind code das texturas de cor ligadas ao off screen (somente leitura).

> **Caution:**
Se o off screen pode ser redimensionado dinamicamente (`width` ou `height` igual a -1), os bind codes podem mudar.

**Tipo:** list of 8 integers

#### depthBindCode

O bind code da textura de profundidade ligada ao off screen (somente leitura).

> **Caution:**
Se o off screen pode ser redimensionado dinamicamente (`width` ou `height` igual a -1), o bind code pode mudar.

**Tipo:** integer

---

## KX_AddObjectActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Edit Object (no modo Add Object)

> **Caution:**
Um atuador Add Object é ignorado se, no início do jogo, o objeto ligado não existir (ou estiver vazio) ou estiver numa layer ativa.

```text

Error: GameObject 'Name' has a AddObjectActuator 'ActuatorName' without object (in 'nonactive' layer)
```

#### object

o objeto que este atuador adiciona.

**Tipo:** `KX_GameObject` or None

#### objectLastCreated

o último objeto adicionado por este atuador (somente leitura).

**Tipo:** `KX_GameObject` or None

#### time

o tempo de vida dos objetos adicionados, em frames. Use 0 para desligar a remoção automática.

**Tipo:** float

#### linearVelocity

a velocidade linear inicial dos objetos adicionados.

**Tipo:** list [vx, vy, vz]

#### angularVelocity

a velocidade angular inicial dos objetos adicionados.

**Tipo:** list [vx, vy, vz]

#### instantAddObject()

adiciona o objeto sem precisar chamar SCA_PythonController.activate()

> **Note:**
Use objectLastCreated para pegar o objeto recém-criado.

---

## KX_AnimationEvent

Classe `Range.types.KX_AnimationEvent`.

```python
# Mostra quantas vezes cada evento da animação disparou.
import Range

own = Range.logic.getCurrentController().owner

for event in own.animationEventManager.events:
    print(event.triggers, event.getFireCount())
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### getFireCount(index=-1)

 `método`

Quantas vezes o gatilho de número `index` disparou. Com -1, soma todos os gatilhos.

**Retorna:** `int`

#### triggers

 `atributo · só leitura`

Lista dos frames da animação em que o evento dispara.

---

## KX_AnimationEventManager

> **Veja também:**
[`KX_AnimationEvent`](#kx_animationevent), [`SCA_AnimationEventSensor`](#sca_animationeventsensor)

Classe `Range.types.KX_AnimationEventManager`.

```python
# Toca um som de passo nos quadros marcados na animação.
import Range

cont = Range.logic.getCurrentController()
own = cont.owner

fired = sum(event.getFireCount() for event in own.animationEventManager.events)

if fired != own.get("steps", 0):
    own["steps"] = fired
    cont.activate("StepSound")
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### events

 `atributo · só leitura`

Lista dos eventos de animação (`KX_AnimationEvent`) do objeto.

---

## KX_ArmatureSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

O sensor de armature detecta condições em armatures.

```python
# Reage quando o erro do IK fica grande demais.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Armature"]

sensor.type = Range.logic.KX_ARMSENSOR_LIN_ERROR_ABOVE
sensor.value = 0.1

if sensor.positive:
    print("Bone cannot reach the target:", sensor.constraint.name)
```

#### type

O tipo de medida que o sensor faz quando está ativo.

Pode ser uma `destas constantes`

**Tipo:** integer.

#### constraint

O objeto de constraint que este sensor observa.

**Tipo:** `BL_ArmatureConstraint`

#### value

O limite usado na comparação com o erro da constraint. O erro linear só é atualizado em constraints IK CopyPose/Distance com o solver iTaSC. O erro de rotação só é atualizado em constraints IK CopyPose+rotação com o solver iTaSC. O erro linear em CopyPose é sempre >= 0: é a norma da distância entre o alvo e o bone. O erro de rotação em CopyPose é sempre >= 0: é a norma do vetor de rotação equivalente entre as orientações do bone e do alvo. O erro linear em Distance pode ser positivo se a distância entre o bone e o alvo for maior que a desejada, e negativo se for menor.

**Tipo:** float

---

## KX_BatchGroup

Classe base: [`EXP_Value`](#exp_value)

O batch group é uma classe que contém uma malha resultante da junção das malhas usadas por objetos. As malhas são juntadas com a transformação dos objetos que as usam. Uma instância desta classe não pertence a um objeto, mas é compartilhada entre objetos. Por isso, uma instância de `KX_BatchGroup` precisa ser criada passando como argumento uma lista de pelo menos um objeto com as malhas a juntar. Dá para fazer isso de um jeito parecido com:

```python

import Range

scene = Range.logic.getCurrentScene()

batchGroup = Range.types.KX_BatchGroup([scene.objects["Cube"], scene.objects["Plane"]])
```

> **Caution:**
Configurações de render próprias de cada objeto, como `KX_GameObject.layer` e `KX_GameObject.color`, são compartilhadas ao usar batch groups. Elas vêm do objeto `referenceObject`.

```python

# Junta todos os objetos com a propriedade rock para desenhar com menos chamadas.
import Range

scene = Range.logic.getCurrentScene()
rocks = [obj for obj in scene.objects if "rock" in obj]

group = Range.types.KX_BatchGroup(rocks)
print(len(group.objects))
```

```python

# Tira um objeto do grupo antes de mexer só nele.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.split([obj])
```

```python

# Desfaz o grupo e devolve a malha original de cada objeto.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.destruct()
```

#### objects

A lista dos objetos juntados (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

#### referenceObject

O objeto usado para as configurações de render (layer, cor...).

#### merge(objects)

Junta as malhas usando a transformação dos objetos que as usam.

- **`objects`**: Os objetos a juntar.
  - tipo: `EXP_ListValue` of `KX_GameObject`

#### split(objects)

Separa as malhas dos objetos e restaura as malhas originais.

- **`objects`**: Os objetos a separar.
  - tipo: `EXP_ListValue` of `KX_GameObject`

#### destruct()

Destrói o batch group e restaura todos os objetos para as malhas originais.

---

## KX_BlenderMaterial

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`BL_Shader`](#bl_shader), [`BL_Texture`](#bl_texture), [`KX_Mesh`](#kx_mesh)

Esta é a interface para os materiais na game engine.

Os materiais definem o estado de render aplicado aos objetos de malha.

O exemplo abaixo mostra uma configuração simples de shader GLSL que mistura dinamicamente dois canais de textura num material. Todos os materiais do objeto que roda este script devem ter duas texturas usando UV maps separados nos dois primeiros canais de textura.

O código funciona nos modos de render Multitexture e GLSL.

```python

from Range import logic

vertex_shader = """

void main(void)
{
   // simple projection of the vertex position to view space
   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
   // coordinate of the 1st texture channel
   gl_TexCoord[0] = gl_MultiTexCoord0;
   // coordinate of the 2nd texture channel
   gl_TexCoord[1] = gl_MultiTexCoord1;
}
"""

fragment_shader ="""

uniform sampler2D texture_0;
uniform sampler2D texture_1;
uniform float factor;

void main(void)
{
   vec4 color_0 = texture2D(texture_0, gl_TexCoord[0].st);
   vec4 color_1 = texture2D(texture_1, gl_TexCoord[1].st);
   gl_FragColor = mix(color_0, color_1, factor);
}
"""

object = logic.getCurrentController().owner

for mesh in object.meshes:
    for material in mesh.materials:
        shader = material.getShader()
        if shader is not None:
            if not shader.isValid():
                shader.setSource(vertex_shader, fragment_shader, True)

            # pega o primeiro canal de textura do material
            shader.setSampler('texture_0', 0)
            # pega o segundo canal de textura do material
            shader.setSampler('texture_1', 1)
            # passa outro uniform para o shader
            shader.setUniform1f('factor', 0.3)
```

#### shader

O shader do material.

**Tipo:** `BL_Shader`

#### blending

Inteiros usados na mistura de pixels, (src, dst), iguais aos do método setBlending.

**Tipo:** (integer, integer)

#### getShader()

Devolve o shader do material.

**Retorna:** o shader do material

**Tipo do retorno:** `BL_Shader`

#### ~~getTextureBindcode(textureslot)~~

Devolve o bind code/id/número/nome OpenGL da textura do material.

> **Obsoleto use :py:meth:`bge.types.BL_Texture.bindCode`:**

- **`textureslot`**: Define o número do slot de textura
  - tipo: integer

**Retorna:** o bind code/id/número/nome OpenGL da textura do material

**Tipo do retorno:** integer

#### alpha

A transparência alpha do material.

**Tipo:** float between 0.0 and 1.0 inclusive

#### hardness

Quão dura (nítida) é a reflexão especular do material.

**Tipo:** integer between 1 and 511 inclusive

#### emit

Quantidade de luz emitida.

**Tipo:** float between 0.0 and 2.0 inclusive

#### ambient

Quantidade de luz ambiente no material.

**Tipo:** float between 0.0 and 1.0 inclusive

#### specularAlpha

Transparência alpha das áreas especulares.

**Tipo:** float between 0.0 and 1.0 inclusive (alpha must be < 1.0)

#### specularIntensity

Quão intensa (brilhante) é a reflexão especular do material.

**Tipo:** float between 0.0 and 1.0 inclusive

#### diffuseIntensity

A quantidade de reflexão difusa do material.

**Tipo:** float between 0.0 and 1.0 inclusive

#### specularColor

A cor especular do material.

**Tipo:** `mathutils.Color`

#### diffuseColor

A cor difusa do material.

**Tipo:** `mathutils.Color`

#### textures

Lista de todas as texturas do material.

**Tipo:** List of `BL_Texture` (read only)

#### setScriptUniform(name, value)

Define um uniform `u_` declarado no Texto dos nós GLSL Script deste material (`uniform float u_speed;`). O valor é enviado à GPU no próximo desenho, sem recompilar o shader. Um uniform cujo socket está ligado a outro nó não é afetado.

- **`name`**: Nome do uniform, como foi escrito no Texto (`"u_speed"`).
  - tipo: string
- **`value`**: Um número ou uma sequência de até 4 números para vec2/vec3/vec4.
  - tipo: float or sequence of floats

**Retorna:** True quando o material possui esse uniform.

**Tipo do retorno:** boolean

#### getScriptUniform(name)

Valor atual de um uniform `u_` dos nós GLSL Script deste material.

- **`name`**: Nome do uniform.
  - tipo: string

**Retorna:** Um float, uma tupla (2 valores para vec2, 3 para vec3 e 4 para vec4) ou None quando não existe esse uniform.

#### setBlending(src, dest)

Define as funções aritméticas de cor dos pixels.

- **`src`**: Define como os fatores de mistura de origem de vermelho, verde, azul e alpha são calculados; um destes... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - tipo: int
- **`dest`**: Define como os fatores de mistura de destino de vermelho, verde, azul e alpha são calculados; um destes... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - tipo: int

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### passIndex

 `atributo`

Pass Index do material, usado para separar materiais em filtros e efeitos.

---

## KX_BoundingBox

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Uma caixa de volume de um game object. Usada para ler e alterar a caixa de volume ou AABB.

```python

from Range import logic
from mathutils import Vector

owner = logic.getCurrentController().owner
box = owner.cullingBox

# Desliga a atualização automática para permitir modificar a caixa.
box.autoUpdate = False

print(box)
# Aumenta a altura da caixa em 1.
box.max = box.max + Vector((0, 0, 1))

print(box)
```

```python

# Lê o tamanho da caixa do objeto.
import Range

box = Range.logic.getCurrentController().owner.cullingBox

size = box.max - box.min
print("Size:", size)
print("Center:", box.center)
print("Radius:", box.radius)
print("Volume:", box.volume)
```

#### min

O ponto mínimo da bounding box nos eixos x, y e z.

**Tipo:** `mathutils.Vector`

#### max

O ponto máximo da bounding box nos eixos x, y e z.

**Tipo:** `mathutils.Vector`

#### center

O centro da bounding box (somente leitura).

**Tipo:** `mathutils.Vector`

#### radius

O raio da bounding box (somente leitura).

**Tipo:** float

#### autoUpdate

Permite atualizar a bounding box se a malha for modificada.

**Tipo:** boolean

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### volume

 `atributo · só leitura`

Volume da caixa delimitadora (largura × altura × profundidade).

---

## KX_Camera

Classe base: [`KX_GameObject`](#kx_gameobject)

> **Veja também:**
[`KX_Scene`](#kx_scene), [`KX_2DFilterManager`](#kx_2dfiltermanager), [`KX_GameObject`](#kx_gameobject), [`Range.render`](#rangerender)

Um objeto de câmera.

```python

# Pega o objeto que está embaixo do mouse.
import Range

scene = Range.logic.getCurrentScene()
x, y = Range.logic.mouse.position

hit = scene.active_camera.getScreenRay(x, y, 100.0)

if hit is not None:
    print(hit.name)
```

```python

# Confere se um objeto está dentro da visão da câmera.
import Range

scene = Range.logic.getCurrentScene()
cam = scene.active_camera
enemy = scene.objects["Enemy"]

if cam.sphereInsideFrustum(enemy.worldPosition, 1.0) != cam.OUTSIDE:
    print("Enemy on screen")
```

```python

# Treme a câmera por meio segundo, como em uma explosão.
import Range

cam = Range.logic.getCurrentScene().active_camera
cam.shake(0.8, 0.5)
```

```python

# Aproxima a imagem fechando o campo de visão.
import Range

cam = Range.logic.getCurrentScene().active_camera
cam.fov = 30.0
```

```python

# Tela dividida: esta câmera fica com a metade esquerda da janela.
import Range

cam = Range.logic.getCurrentController().owner
width = Range.render.getWindowWidth()
height = Range.render.getWindowHeight()

cam.useViewport = True
cam.setViewport(0, 0, width // 2, height)
```

#### INSIDE

Veja `sphereInsideFrustum` e `boxInsideFrustum`

#### INTERSECT

Veja `sphereInsideFrustum` e `boxInsideFrustum`

#### OUTSIDE

Veja `sphereInsideFrustum` e `boxInsideFrustum`

#### lens

O valor da lente da câmera.

**Tipo:** float

#### lodDistanceFactor

Fator que multiplica a distância até a câmera para ajustar os níveis de detalhe. Um valor < 1.0 faz a distância usada para calcular os níveis de detalhe diminuir.

**Tipo:** float

#### fov

O campo de visão da câmera.

**Tipo:** float

#### ortho_scale

A escala da visão da câmera no modo ortográfico.

**Tipo:** float

#### near

A distância de corte próxima (near clip) da câmera.

**Tipo:** float

#### far

A distância de corte distante (far clip) da câmera.

**Tipo:** float

#### shift_x

O deslocamento horizontal da câmera.

**Tipo:** float

#### shift_y

O deslocamento vertical da câmera.

**Tipo:** float

#### perspective

True se a câmera usa projeção em perspectiva; False para projeção ortográfica.

**Tipo:** boolean

#### frustum_culling

True se a câmera faz frustum culling.

**Tipo:** boolean

#### activityCulling

True se esta câmera é usada para calcular a distância dos objetos no culling de atividade.

**Tipo:** boolean

#### projection_matrix

A matriz de projeção 4x4 da câmera.

> **Note:**
Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).

**Tipo:** 4x4 Matrix [[float]]

#### projectionMatrixLeft

A matriz de projeção 4x4 do olho esquerdo.

> **Note:**
Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).

**Tipo:** 4x4 Matrix [[float]]

#### projectionMatrixRight

A matriz de projeção 4x4 do olho direito.

> **Note:**
Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).

**Tipo:** 4x4 Matrix [[float]]

#### modelview_matrix

A matriz model view 4x4 da câmera (somente leitura).

**Tipo:** 4x4 Matrix [[float]]

> **Note:**
Esta matriz é recalculada a cada frame a partir da posição e da orientação da câmera. Antes do primeiro frame renderizado, é a matriz identidade (vale para qualquer Python rodado no frame 1).

#### camera_to_world

A transformação da câmera para o mundo (somente leitura).

**Tipo:** 4x4 Matrix [[float]]

> **Note:**
Esta matriz é recalculada a cada frame a partir da posição e da orientação da câmera.

#### world_to_camera

A transformação do mundo para a câmera (somente leitura).

**Tipo:** 4x4 Matrix [[float]]

> **Note:**
Recalculada a cada frame a partir da posição e da orientação da câmera.

> **Note:**
É a inversa de camera_to_world.

#### useViewport

True quando a câmera é usada como viewport; defina True para ligar uma viewport para esta câmera.

**Tipo:** boolean

#### viewport

Retângulo da viewport usado no último render desta câmera, em pixels (somente leitura). Proporções definidas no editor já vêm convertidas para a janela.

**Tipo:** list [left, bottom, right, top]

#### sphereInsideFrustum(centre, radius)

Testa a esfera dada contra o frustum da visão.

- **`centre`**: O centro da esfera (em coordenadas do mundo).
  - tipo: list [x, y, z]
- **`radius`**: O raio da esfera
  - tipo: float

**Retorna:** `INSIDE`, `OUTSIDE` ou `INTERSECT`

**Tipo do retorno:** integer

> **Note:**
Logo que a câmera é iniciada, o resultado é inválido, porque a matriz de projeção ainda não foi definida.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Uma esfera de raio 4.0 em [x, y, z] = [1.0, 1.0, 1.0]
if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
    # A esfera está dentro do frustum!
    # Faça algo útil!
else:
    # A esfera está fora do frustum
```

#### boxInsideFrustum(box)

Testa a caixa dada contra o frustum da visão.

- **`box`**: Oito (8) pontos dos cantos da caixa (em coordenadas do mundo), ou um `KX_GameObject` para testar a caixa delimitadora dele no mundo.
  - tipo: list of lists or `KX_GameObject`

**Retorna:** `INSIDE`, `OUTSIDE` ou `INTERSECT`

> **Note:**
Logo que a câmera é iniciada, o resultado é inválido, porque a matriz de projeção ainda não foi definida.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Caixa a testar...
box = []
box.append([-1.0, -1.0, -1.0])
box.append([-1.0, -1.0,  1.0])
box.append([-1.0,  1.0, -1.0])
box.append([-1.0,  1.0,  1.0])
box.append([ 1.0, -1.0, -1.0])
box.append([ 1.0, -1.0,  1.0])
box.append([ 1.0,  1.0, -1.0])
box.append([ 1.0,  1.0,  1.0])

if (cam.boxInsideFrustum(box) != cam.OUTSIDE):
  # A caixa está dentro ou cruza o frustum!
  # Faça algo útil!
else:
  # A caixa está fora do frustum!
```

Para testar um objeto do jogo, passe o próprio objeto. É o mesmo que passar os cantos dele no mundo, vindos de `getBoundBoxCorners`:

```python

if cam.boxInsideFrustum(obj) != cam.OUTSIDE:
    print(obj.name, "is visible (at least partly)")

# mesmo resultado:
cam.boxInsideFrustum(obj.getBoundBoxCorners('WORLD'))
```

#### pointInsideFrustum(point)

Testa o ponto dado contra o frustum da visão.

- **`point`**: O ponto a testar (em coordenadas do mundo).
  - tipo: 3D Vector

**Retorna:** True se o ponto está dentro do frustum de visão desta câmera.

**Tipo do retorno:** boolean

> **Note:**
Logo que a câmera é iniciada, o resultado é inválido, porque a matriz de projeção ainda não foi definida.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Testa o ponto [0.0, 0.0, 0.0]
if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
  # O ponto está dentro do frustum!
  # Faça algo útil!
else:
  # A caixa está fora do frustum!
```

#### getCameraToWorld()

Devolve a transformação da câmera para o mundo.

**Retorna:** A matriz de transformação da câmera para o mundo.

**Tipo do retorno:** matrix (4x4 list)

#### getWorldToCamera()

Devolve a transformação do mundo para a câmera.

Devolve a inversa de getCameraToWorld().

**Retorna:** A matriz de transformação do mundo para a câmera.

**Tipo do retorno:** matrix (4x4 list)

#### setOnTop()

Coloca a viewport desta câmera por cima de todas as outras.

#### setViewport(left, bottom, right, top)

Define a região desta viewport na tela, em pixels.

Use `Range.render.getWindowHeight` e `Range.render.getWindowWidth` para calcular valores relativos à tela inteira.

- **`left`**: Coordenada da esquerda desta viewport, em pixels
  - tipo: integer
- **`bottom`**: Coordenada de baixo desta viewport, em pixels
  - tipo: integer
- **`right`**: Coordenada da direita desta viewport, em pixels
  - tipo: integer
- **`top`**: Coordenada de cima desta viewport, em pixels
  - tipo: integer

#### getScreenPosition(object)

Pega a posição de um objeto projetada na tela.

```python

# Para um objeto no meio da tela, coord = [0.5, 0.5]
coord = camera.getScreenPosition(object)
```

- **`object`**: Nome do objeto ou lista [x, y, z]
  - tipo: `KX_GameObject` or 3D Vector

**Retorna:** A posição do objeto em coordenadas de tela.

**Tipo do retorno:** list [x, y]

#### getScreenVect(x, y)

Pega o vetor que sai da posição da câmera na direção da coordenada de tela.

- **`x`**: Eixo X
  - tipo: float
- **`y`**: Eixo Y
  - tipo: float

**Tipo do retorno:** 3D Vector

**Retorna:** O vetor a partir da coordenada de tela.

```python

# Pega o vetor da direção da frente da câmera:
m_vect = camera.getScreenVect(0.5, 0.5)
```

#### getScreenRay(x, y, dist, property="", xray=False, mask=0xFFFF)

Olha na direção de uma coordenada de tela (x, y) e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop. O raio funciona como KX_GameObject->rayCastTo.

- **`x`**: Eixo X
  - tipo: float
- **`y`**: Eixo Y
  - tipo: float
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`property`**: Nome da propriedade que o objeto precisa ter; se omitido, detecta qualquer objeto
  - tipo: string
- **`xray`**: O raio atravessa os objetos que não têm a propriedade, como a opção X-Ray do sensor Mouse
  - tipo: boolean
- **`mask`**: Máscara de colisão; o raio só atinge objetos destes grupos de colisão
  - tipo: bitfield

**Tipo do retorno:** `KX_GameObject`

**Retorna:** O primeiro objeto atingido, ou None se não atingir nada ou se o objeto não tiver a propriedade

```python

# Pega um objeto com a propriedade "wall" na frente da câmera, a até 100 de distância:
target = camera.getScreenRay(0.5, 0.5, 100, "wall")
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### shake(trauma, duration=0.0)

 `método`

Treme a câmera. `trauma` vai de 0 a 1 e soma com o terremoto do World. Com `duration`, o tremor some nesse tempo; sem, diminui no ritmo de `shakeDecay` por segundo.

#### cameraSpeed

*(novo na Anastacio)* `atributo · só leitura`

Velocidade atual da câmera (unidades por segundo), usada pelos efeitos ligados à velocidade.

#### catEyeStrength

*(novo na Anastacio)* `atributo`

Força do bokeh "olho de gato" do desfoque (DOF), de 0.0 a 1.0: os círculos ficam achatados perto das bordas.

#### chromaticStrength

*(novo na Anastacio)* `atributo`

Força da aberração cromática, de 0.0 a 5.0.

#### directionalBlurMax

*(novo na Anastacio)* `atributo`

Limite do desfoque direcional (rastro ao girar a câmera), de 0.0 a 0.2.

#### directionalBlurStrength

*(novo na Anastacio)* `atributo`

Força do desfoque direcional, de 0.0 a 2.0.

#### dofBlur

*(novo na Anastacio)* `atributo`

Tamanho máximo do desfoque de profundidade (DOF), de 0 a 32.

#### dofQuality

*(novo na Anastacio)* `atributo`

Qualidade do DOF: 0 baixa, 1 média, 2 alta.

#### droneAmplitude

*(novo na Anastacio)* `atributo`

Amplitude do balanço do modo de rastreio Drone (0 a 20).

#### droneFrequency

*(novo na Anastacio)* `atributo`

Frequência do balanço do modo Drone (0 a 20).

#### fisheyeStrength

*(novo na Anastacio)* `atributo`

Distorção olho de peixe, de -1.0 (almofada) a 1.0 (barril).

#### focusDistance

*(novo na Anastacio)* `atributo · só leitura`

Distância de foco usada neste frame, depois de suavizada.

#### focusManualDistance

*(novo na Anastacio)* `atributo`

Distância de foco quando `focusMode` é 0 (manual).

#### focusMode

*(novo na Anastacio)* `atributo`

Como o foco é escolhido: 0 manual (`focusManualDistance`), 1 objeto (`focusObject`), 2 propriedade (`focusProperty`), 3 automático (raio no ponto da tela).

#### focusObject

*(novo na Anastacio)* `atributo`

Objeto em foco quando `focusMode` é 1. `None` para nenhum.

#### focusPosition

*(novo na Anastacio)* `atributo · só leitura`

Posição no mundo do ponto em foco, ou `None`.

#### focusProperty

*(novo na Anastacio)* `atributo`

Nome da propriedade de jogo usada quando `focusMode` é 2: foca o objeto mais próximo que a tiver verdadeira.

#### focusRange

*(novo na Anastacio)* `atributo`

Faixa de distância, em volta do foco, que continua nítida.

#### focusScreenPosition

*(novo na Anastacio)* `atributo · só leitura`

Posição na tela (0 a 1) do ponto em foco.

#### focusSmooth

*(novo na Anastacio)* `atributo`

Suavização da troca de foco, de 0 (instantânea) a 10.

#### focusTarget

*(novo na Anastacio)* `atributo · só leitura`

Objeto que está em foco agora, ou `None`.

#### focusValid

*(novo na Anastacio)* `atributo · só leitura`

`True` quando o foco achou um alvo neste frame.

#### gazeDirection

*(novo na Anastacio)* `atributo · só leitura`

Direção para onde a câmera está olhando, no mundo.

#### shakeAmplitude

*(novo na Anastacio)* `atributo`

Amplitude máxima do tremor (0 a 0.5).

#### shakeDecay

*(novo na Anastacio)* `atributo`

Quanto o tremor diminui por segundo (0 a 20).

#### shakeFrequency

*(novo na Anastacio)* `atributo`

Frequência do tremor (0 a 60).

#### shakeTrauma

*(novo na Anastacio)* `atributo · só leitura`

Trauma atual do tremor (0 a 1).

#### speedBlurMaxSpeed

*(novo na Anastacio)* `atributo`

Velocidade em que o desfoque de velocidade chega ao máximo.

#### speedBlurStrength

*(novo na Anastacio)* `atributo`

Força do desfoque de velocidade, de 0.0 a 2.0.

#### speedOverride

*(novo na Anastacio)* `atributo`

Velocidade usada pelos efeitos no lugar da velocidade real. -1 desliga e volta a usar a real.

#### trackBank

*(novo na Anastacio)* `atributo`

Inclinação lateral da câmera nas curvas do rastreio (0 a 5).

#### trackDeadzone

*(novo na Anastacio)* `atributo`

Zona morta do rastreio: o alvo pode se mover nessa margem da tela sem a câmera virar (0 a 0.5).

#### trackLimit

*(novo na Anastacio)* `atributo`

Ângulo máximo, em radianos, que o rastreio pode girar a câmera.

#### trackMode

*(novo na Anastacio)* `atributo`

Modo de rastreio: 0 desligado, 1 olhar para o alvo, 2 drone.

#### trackOrientation

*(novo na Anastacio)* `atributo · só leitura`

Orientação calculada pelo rastreio neste frame.

#### trackScreenOffset

*(novo na Anastacio)* `atributo`

Deslocamento `[x, y]` do alvo na tela, de -0.5 a 0.5.

#### trackSpeed

*(novo na Anastacio)* `atributo`

Velocidade com que a câmera vira para o alvo (0 a 10).

#### useBlurProtect

*(novo na Anastacio)* `atributo`

Protege o centro da tela dos desfoques.

#### useCatEye

*(novo na Anastacio)* `atributo`

Liga o bokeh olho de gato no DOF.

#### useChromatic

*(novo na Anastacio)* `atributo`

Liga a aberração cromática.

#### useChromaticSpeed

*(novo na Anastacio)* `atributo`

Faz a aberração cromática aumentar com a velocidade.

#### useDirectionalBlur

*(novo na Anastacio)* `atributo`

Liga o desfoque direcional.

#### useDof

*(novo na Anastacio)* `atributo`

Liga a profundidade de campo (DOF).

#### useShakeRoll

*(novo na Anastacio)* `atributo`

O tremor também gira a câmera em volta do eixo de visão.

#### useSpeedBlur

*(novo na Anastacio)* `atributo`

Liga o desfoque de velocidade.

#### useTrackUpLock

*(novo na Anastacio)* `atributo`

Mantém o "para cima" da câmera fixo durante o rastreio.

#### useVignette

*(novo na Anastacio)* `atributo`

Liga a vinheta (bordas escuras).

#### vignetteRadius

*(novo na Anastacio)* `atributo`

Raio da vinheta (0 a 2).

#### vignetteStrength

*(novo na Anastacio)* `atributo`

Força da vinheta (0 a 1).

---

## KX_CameraActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Aplica mudanças a uma câmera.

```python
# Faz a câmera seguir outro objeto, a uma distância definida.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Camera"]

act.object = Range.logic.getCurrentScene().objects["Car"]
act.min = 4.0
act.max = 8.0
act.height = 2.5
act.damping = 0.1
cont.activate(act)
```

#### damping

força do movimento de seguir da câmera.

**Tipo:** float

#### axis

O eixo da câmera: (0, 1, 2) para `XYZ` positivo, (3, 4, 5) para `XYZ` negativo.

**Tipo:** int

#### min

distância mínima até o objeto alvo mantida pelo atuador.

**Tipo:** float

#### max

distância máxima a manter do objeto alvo.

**Tipo:** float

#### height

altura a manter acima do objeto alvo.

**Tipo:** float

#### object

o objeto que este atuador segue.

**Tipo:** `KX_GameObject` or None

---

## KX_ChangeColorActuator

Classe `Range.types.KX_ChangeColorActuator`.

```python
# Muda aos poucos a cor do objeto para vermelho.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["ChangeColor"]

act.color = [1.0, 0.0, 0.0, 1.0]
act.useLerp = True
act.lerp = 0.2
cont.activate(act)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### color

 `atributo`

Cor `[r, g, b, a]` aplicada pelo atuador.

#### lerp

 `atributo`

Velocidade da transição de cor quando `useLerp` está ligado (0.1 a 1.0).

#### useLerp

 `atributo`

Faz a cor mudar aos poucos em vez de trocar de uma vez.

---

## KX_CharacterWrapper

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`Range.constraints`](#rangeconstraints)

Um wrapper que expõe as opções de física de personagem.

> **Note:**
Quando o objeto do personagem é removido, todo método e atributo do wrapper gera `ReferenceError`. Suspender a física mantém o personagem, então o wrapper continua funcionando.

```python
# Anda e pula com um objeto Character.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
character = constraints.getCharacter(own)
keys = Range.logic.keyboard.inputs

speed = 0.1 if keys[Range.events.WKEY].active else 0.0
character.walkDirection = (0.0, speed, 0.0)

if keys[Range.events.SPACEKEY].activated and character.onGround:
    character.jump()
```

```python
# Abaixa, e levanta quando houver espaço.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
character = constraints.getCharacter(own)
crouch = Range.logic.keyboard.inputs[Range.events.LEFTCTRLKEY].active

if crouch:
    character.posture = "CROUCH"
elif character.canStand:
    character.posture = "STAND"
```

```python
# Permite pulo duplo.
import Range
from Range import constraints

character = constraints.getCharacter(Range.logic.getCurrentController().owner)

character.maxJumps = 2
character.jumpSpeed = 8.0
```

#### onGround

Se o personagem está no chão ou não (somente leitura).

**Tipo:** boolean

#### gravity

O valor de gravidade usado para o personagem.

**Tipo:** float

#### fallSpeed

A velocidade de queda do personagem.

**Tipo:** float

#### maxJumps

O número máximo de pulos que o personagem pode dar antes de tocar o chão. O padrão é 1. 2 permite pulo duplo, e assim por diante.

**Tipo:** int in [0, 255], default 1

#### jumpCount

A contagem de pulos atual. Serve para ter lógicas diferentes para pulo simples e pulo duplo, por exemplo, uma animação diferente no segundo pulo.

**Tipo:** int

#### jumpSpeed

A velocidade de pulo do personagem.

**Tipo:** float

#### maxSlope

A inclinação máxima que o personagem consegue subir.

**Tipo:** float

#### walkDirection

A velocidade e a direção em que o personagem anda, em coordenadas do mundo. Use isto em vez de applyMovement() para mover o personagem do jeito certo.

**Tipo:** Vector((x, y, z))

#### jump()

O personagem pula com base na sua velocidade de pulo.

#### jumpDirection

A direção em que o personagem pula.

**Tipo:** Vector((x, y, z))

#### setVelocity(velocity, time, local=False)

Define a velocidade linear do personagem por um período.

Este método define a velocidade do personagem pelo centro de massa durante um período.

- **`velocity`**: Vetor de velocidade linear.
  - tipo: 3D Vector
- **`time`**: Período em que a velocidade linear é aplicada.
  - tipo: float
- **`local`**: * False: velocidade "global", ou seja, relativa à orientação do mundo. * True: velocidade "local", ou seja, relativa à orientação do objeto.
  - tipo: boolean

#### smoothMovement

Suaviza o movimento causado pela direção de caminhada.

**Tipo:** float (0.0 to 1.0)

#### posture

Postura atual (a forma de colisão em uso). Atribuir pede uma nova postura; ficar em pé espera até haver espaço acima do personagem (veja `canStand`).

**Tipo:** string, one of `'STAND'`, `'CROUCH'`, `'CRAWL'`, `'JUMP_TUCK'`

#### canStand

True quando há espaço para ficar em pé a partir da postura atual.

**Tipo:** boolean (read-only)

#### running

Modo corrida: enquanto True o personagem anda com o fator Run Speed do objeto.

**Tipo:** boolean

#### reset()

Zera a velocidade e a direção de caminhada do personagem.

---

## KX_CollisionContactPoint

Classe base: [`EXP_Value`](#exp_value)

Um ponto de contato de colisão passado aos callbacks de colisão.

```python

import Range

def oncollision(object, point, normal, points):
    print("Hit by", object)
    for point in points:
        print(point.localPointA)
        print(point.localPointB)
        print(point.worldPoint)
        print(point.normal)
        print(point.combinedFriction)
        print(point.combinedRestitution)
        print(point.appliedImpulse)

cont = Range.logic.getCurrentController()
own = cont.owner
own.collisionCallbacks = [oncollision]
```

#### localPointA

O ponto de contato no espaço do objeto dono.

**Tipo:** `mathutils.Vector`

#### localPointB

O ponto de contato no espaço do objeto colisor.

**Tipo:** `mathutils.Vector`

#### worldPoint

O ponto de contato no espaço do mundo.

**Tipo:** `mathutils.Vector`

#### normal

A normal do contato no espaço do objeto dono.

**Tipo:** `mathutils.Vector`

#### combinedFriction

O atrito combinado do objeto dono e do colisor.

**Tipo:** float

#### combinedRollingFriction

O atrito de rolagem combinado do objeto dono e do colisor.

**Tipo:** float

#### combinedRestitution

A restituição combinada do objeto dono e do colisor.

**Tipo:** float

#### appliedImpulse

O impulso aplicado ao objeto dono.

**Tipo:** float

---

## KX_CollisionSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

O sensor de colisão detecta colisões entre objetos.

```python
# Mostra o que bateu no objeto.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Collision"]

if sensor.positive:
    for obj in sensor.hitObjectList:
        print(obj.name)
```

```python
# Só detecta objetos com a propriedade coin.
import Range

sensor = Range.logic.getCurrentController().sensors["Collision"]

sensor.propName = "coin"
sensor.useMaterial = False
```

#### propName

A propriedade ou o material com que colidir.

**Tipo:** string

#### useMaterial

Define se o sensor procura uma propriedade ou um material. KX_True = procura material; KX_False = procura propriedade.

**Tipo:** boolean

#### usePulseCollision

Quando ligado, mudanças no conjunto de objetos em colisão geram um pulso.

**Tipo:** boolean

#### hitObject

O último objeto que colidiu (somente leitura).

**Tipo:** `KX_GameObject` or None

#### hitObjectList

Uma lista dos objetos em colisão (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

#### hitMaterial

O material do objeto na face atingida pelo raio (somente leitura).

**Tipo:** string

---

## KX_ConstraintActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Um atuador Constraint limita a posição, rotação, distância ou orientação de um objeto.

```python
# Mantém o objeto a uma distância do chão.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Constraint"]

act.distance = 1.5
act.rayLength = 5.0
act.damp = 10
cont.activate(act)
```

#### damp

Constante de tempo da constraint, em frames (não usada pela constraint Force field).

**Tipo:** integer

#### rotDamp

Constante de tempo da rotação, em frames (só para a constraint de distância); 0 = usa damp também na rotação.

**Tipo:** integer

#### direction

A direção de referência, em coordenadas do mundo, da constraint de orientação.

**Tipo:** `mathutils.Vector`

#### option

Combinação binária `destas constantes`

**Tipo:** integer

#### time

tempo de ativação do atuador. O atuador se desliga depois desse número de frames. Com 0, o atuador não tem limite de tempo.

**Tipo:** integer

#### propName

o nome da propriedade ou material para a detecção por raio da constraint de distância.

**Tipo:** string

#### min

O limite inferior da constraint. Nas constraints de rotação e orientação, é em radianos.

**Tipo:** float

#### distance

a distância alvo da constraint de distância.

**Tipo:** float

#### max

o limite superior da constraint. Nas constraints de rotação e orientação, é em radianos.

**Tipo:** float

#### rayLength

o comprimento do raio da constraint de distância.

**Tipo:** float

#### limit

tipo de constraint. Use uma `destas constantes`

**Tipo:** integer.

---

## KX_ConstraintWrapper

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

KX_ConstraintWrapper

> **Note:**
Quando a constraint é apagada (`Range.constraints.removeConstraint` ou removendo um dos seus objetos), todo método e atributo do wrapper gera `ReferenceError`. Suspender a física mantém a constraint, então o wrapper continua funcionando.

```python
# Limita quanto uma dobradiça pode abrir.
import math
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
frame = scene.objects["Frame"]

hinge = constraints.createConstraint(
    door.getPhysicsId(), frame.getPhysicsId(),
    constraints.LINEHINGE_CONSTRAINT)

hinge.setParam(3, 0.0, math.radians(90.0))
```

```python
# Quebra a ligação quando a força é grande demais.
hinge.breakingThreshold = 50.0
print(hinge.constraint_id, hinge.enabled)
```

#### getConstraintId(val)

Devolve o ID da constraint

**Retorna:** o ID da constraint

**Tipo do retorno:** integer

#### setParam(axis, value0, value1)

Define os limites da constraint

- **`axis`**:
  - tipo: integer

> **Note:**
* Lowerlimit == Upperlimit -> o eixo fica travado
* Lowerlimit > Upperlimit -> o eixo fica livre
* Lowerlimit < Upperlimit -> o eixo fica limitado a esse intervalo

Para PHY_LINEHINGE_CONSTRAINT = 2 ou PHY_ANGULAR_CONSTRAINT = 3:

axis = 3 é um limite da constraint, com valor de limite inferior/superior
* 3: ângulo do eixo X

- **`value0 (min)`**: Define o limite mínimo do eixo
  - tipo: float
- **`value1 (max)`**: Define o limite máximo do eixo
  - tipo: float
Para PHY_CONE_TWIST_CONSTRAINT = 4:

axis = 3..5 são limites da constraint, valores de limite superior
* 3: ângulo do eixo X
* 4: ângulo do eixo Y
* 5: ângulo do eixo Z

- **`value0 (min)`**: Define o limite mínimo do eixo
  - tipo: float
- **`value1 (max)`**: Define o limite máximo do eixo
  - tipo: float
Para PHY_GENERIC_6DOF_CONSTRAINT = 12:

axis = 0..2 são limites da constraint, com valor de limite inferior/superior
* 0: posição no eixo X
* 1: posição no eixo Y
* 2: posição no eixo Z

axis = 3..5 são ângulos (Euler) relativos da constraint, em radianos
* 3: ângulo do eixo X
* 4: ângulo do eixo Y
* 5: ângulo do eixo Z

- **`value0 (min)`**: Define o limite mínimo do eixo
  - tipo: float
- **`value1 (max)`**: Define o limite máximo do eixo
  - tipo: float
axis = 6..8 são motores de translação, com value0 = velocidade alvo, value1 = força máxima do motor
* 6: posição no eixo X
* 7: posição no eixo Y
* 8: posição no eixo Z

axis = 9..11 são motores de rotação, com value0 = velocidade alvo, value1 = força máxima do motor
* 9: ângulo do eixo X
* 10: ângulo do eixo Y
* 11: ângulo do eixo Z

- **`value0 (speed)`**: Define a velocidade linear do eixo
  - tipo: float Range: -10,000.00 to 10,000.00
- **`value1 (force)`**: Define o limite de força máxima do eixo
  - tipo: float Range: -10,000.00 to 10,000.00
axis = 12..14 são molas lineares em cada posição de liberdade
* 12: posição no eixo X
* 13: posição no eixo Y
* 14: posição no eixo Z

axis = 15..17 são molas angulares em cada ângulo de liberdade, em radianos
* 15: ângulo do eixo X
* 16: ângulo do eixo Y
* 17: ângulo do eixo Z

- **`value0 (stiffness)`**: Define a rigidez da mola
  - tipo: float
- **`value1 (damping)`**: Tendência da mola de voltar à posição original
  - tipo: float 1.0 = springs back to original position (no damping) 0.0 = don't springs back

#### getParam(axis)

Pega a posição ou o ângulo de Euler de uma constraint 6DOF genérica

- **`axis`**:
  - tipo: integer
axis = 0..2 são valores de constraint linear
* 0: posição no eixo X
* 1: posição no eixo Y
* 2: posição no eixo Z

**Retorna:** posição

**Tipo do retorno:** float

axis = 3..5 são ângulos (Euler) relativos da constraint, em radianos
* 3: ângulo do eixo X
* 4: ângulo do eixo Y
* 5: ângulo do eixo Z

**Retorna:** ângulo

**Tipo do retorno:** float

#### constraint_id

Devolve o ID da constraint (somente leitura)

**Tipo:** integer

#### constraint_type

Devolve o tipo da constraint (somente leitura)

**Tipo:** integer - `POINTTOPOINT_CONSTRAINT` - `LINEHINGE_CONSTRAINT` - `ANGULAR_CONSTRAINT` - `CONETWIST_CONSTRAINT` - `VEHICLE_CONSTRAINT` - `GENERIC_6DOF_CONSTRAINT`

#### breakingThreshold

O limite de impulso que quebra a constraint; se a constraint quebrar, `enabled` vira `False`.

**Tipo:** float greater or equal to 0

#### enabled

O status da constraint. Use `True` para restaurar uma constraint depois de quebrada.

**Tipo:** boolean

---

## KX_CubeMap

Classe base: [`KX_TextureRenderer`](#kx_texturerenderer)

> **Veja também:**
[`KX_PlanarMap`](#kx_planarmap), [`KX_TextureRenderer`](#kx_texturerenderer)

API Python para texturas de cube map em tempo real.

```python

import Range

scene = Range.logic.getCurrentScene()
# O objeto que usa um cube map em tempo real no material.
obj = scene.objects["Suzanne"]

mat = obj.meshes[0].materials[0]
# Pega o cube map em tempo real a partir da textura do material.
cubemap = mat.textures[0].renderer

# Põe a posição de render na posição do objeto "Cube".
cubemap.viewpointObject = scene.objects["Cube"]

# Muda o clip start e o clip end do culling.
cubemap.clipStart = 5.0
cubemap.clipEnd = 20.0

# Desliga o render na terceira layer.
cubemap.ignoreLayers = (1 << 2)

# Desliga a atualização por frame.
cubemap.autoUpdate = False
# Pede atualização só neste frame.
cubemap.update()
```

---

## KX_DynamicActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Dynamic.

```python
# Muda a massa do objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_SET_MASS
act.mass = 5.0
cont.activate(act)
```

```python
# Desliga a física do objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_DISABLE_DYNAMICS
cont.activate(act)
```

#### mode

**Tipo:** integer

o tipo de operação do atuador, 0-4

* KX_DYN_RESTORE_DYNAMICS(0)
* KX_DYN_DISABLE_DYNAMICS(1)
* KX_DYN_ENABLE_RIGID_BODY(2)
* KX_DYN_DISABLE_RIGID_BODY(3)
* KX_DYN_SET_MASS(4)

#### mass

o valor de massa para a operação KX_DYN_SET_MASS.

**Tipo:** float

---

## KX_EndObjectActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Edit Object (no modo End Object)

Este atuador não tem métodos Python.

```python
# Remove o objeto quando a vida acaba.
import Range

cont = Range.logic.getCurrentController()

if cont.owner["life"] <= 0:
    cont.activate(cont.actuators["EndObject"])
```

---

## KX_FontObject

Classe base: [`KX_GameObject`](#kx_gameobject)

Um objeto de fonte.

```python

# Mostra uma mensagem sobre a tecla de saída usando um objeto de fonte.
import Range

co = Range.logic.getCurrentController()
font = co.owner

exit_key = Range.events.EventToString(Range.logic.getExitKey())

if exit_key.endswith("KEY"):
    exit_key = exit_key[:-3]

font.text = "Press key '%s' to quit the game." % exit_key
```

```python

# Mostra a pontuação guardada em uma propriedade de jogo.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Score: %d" % font["score"]
```

```python

# Centraliza o texto no eixo X, usando a largura atual dele.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Game Over"
font.localPosition.x = -font.dimensions.x / 2
```

```python

# Revela o texto letra por letra. Rode a cada frame (sensor Always com True Pulse).
import Range

font = Range.logic.getCurrentController().owner

if font.visibleCharacters < font.characterCount:
    font.visibleCharacters += 1
```

```python

# Coloca uma sombra escura atrás do texto.
import Range

font = Range.logic.getCurrentController().owner
font.useShadows = True
font.shadowColor = [0.0, 0.0, 0.0, 0.8]
font.shadowOffset = [0.02, -0.02]
```

#### text

O texto mostrado por este objeto de fonte.

**Tipo:** string

#### resolution

A resolução da fonte.

> **Caution:**
Resoluções altas podem usar muita memória e travar.

**Tipo:** float (0.1 to 50.0)

#### size

O tamanho (fator de escala) do objeto de fonte, a partir da origem dele (afeta a resolução do texto).

> **Caution:**
Tamanhos grandes podem usar muita memória e travar.

**Tipo:** float (0.0001 to 40.0)

#### dimensions

O tamanho (largura e altura) do texto atual, em unidades do Blender.

**Tipo:** `mathutils.Vector`

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### atlas

*(novo na Anastacio)* `atributo`

Nome do texto que guarda o Bitmap Atlas usado para desenhar, `""` para o atlas do próprio texto ou `None` para nenhum atlas.

#### characterCount

*(novo na Anastacio)* `atributo · só leitura`

Número total de caracteres do texto. Só leitura.

#### font

*(novo na Anastacio)* `atributo`

Nome da fonte do texto (a fonte que aparece nas propriedades do Text), ou `None`. Trocar redesenha o texto na hora; nome que não existe no arquivo gera `ValueError`.

#### lines

*(novo na Anastacio)* `atributo · só leitura`

Lista com as linhas do texto depois da quebra. Só leitura.

#### page

*(novo na Anastacio)* `atributo`

Página atual da caixa de texto, a partir de 0. Valores fora do intervalo são limitados à última página válida.

#### pageCount

*(novo na Anastacio)* `atributo · só leitura`

Número de páginas da caixa de texto. Só leitura.

#### shadowColor

 `atributo`

Cor `[r, g, b, a]` da sombra do texto.

#### shadowOffset

 `atributo`

Deslocamento `[x, y]` da sombra do texto.

#### textBox

*(novo na Anastacio)* `atributo`

Tamanho `(largura, altura)` da caixa de texto. O texto quebra as linhas e se divide em páginas para caber nela; `(0, 0)` desliga.

#### translationKey

*(novo na Anastacio)* `atributo`

Chave da tabela de idiomas (`locale/translations.csv`). Com chave, o texto mostra a tradução do idioma atual de `Range.locale` e troca sozinho quando o idioma muda. `""` desliga.

#### useLanguageFont

*(novo na Anastacio)* `atributo`

Quando `True`, o texto usa a fonte e o atlas definidos para o idioma atual no `locale/locale.json` (útil para russo, japonês etc.).

#### useShadows

 `atributo`

Liga a sombra do texto.

#### visibleCharacters

*(novo na Anastacio)* `atributo`

Quantos caracteres aparecem, para o efeito de máquina de escrever. `-1` mostra tudo.

---

## KX_GameActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

O atuador de jogo carrega um novo arquivo .blend, reinicia o .blend atual ou fecha o jogo.

```python
# Reinicia o jogo.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Game"]

act.mode = Range.logic.KX_GAME_RESTART
cont.activate(act)
```

```python
# Abre outro arquivo de jogo.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Game"]

act.mode = Range.logic.KX_GAME_START
act.fileName = "//level2.range"
cont.activate(act)
```

#### fileName

o novo arquivo .blend a carregar.

**Tipo:** string

#### mode

O modo deste atuador. Pode ser uma `destas constantes`

**Tipo:** Int

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### extensionName

 `atributo`

Extensão do arquivo usado pelos modos de salvar/carregar o jogo.

#### saveLocation

 `atributo`

Pasta onde o atuador salva e carrega o jogo.

---

## KX_GameObject

Classe base: [`SCA_IObject`](#sca_iobject)

> **Veja também:**
[`KX_Scene`](#kx_scene), [`KX_Mesh`](#kx_mesh), [`KX_PythonComponent`](#kx_pythoncomponent), [`KX_VehicleWrapper`](#kx_vehiclewrapper), [`KX_ParticleSystem`](#kx_particlesystem)

Todos os objetos do jogo derivam desta classe.

As propriedades de jogo do objeto podem ser acessadas como atributos desta classe.

> **Note:**
Chamar QUALQUER método ou atributo de um objeto que já foi removido da cena gera SystemError. Se o objeto pode ter sido removido desde o último acesso, confira antes com o atributo `invalid`.

KX_GameObject pode ser herdado para estender o que ele faz. Por exemplo:

```python

import Range

class CustomGameObject(Range.types.KX_GameObject):
    RATE = 0.05

    def __init__(self, old_owner):
        # "old_owner" pode ser ignorado. Neste ponto, "self" já é
        # o objeto na cena, e "old_owner" já foi
        # destruído.

        # Dá para criar atributos novos, mas também poderíamos usar uma
        # propriedade de jogo, como "self['rate']".
        self.rate = CustomGameObject.RATE

    def update(self):
        self.worldPosition.z += self.rate

        # inverte a direção
        if self.worldPosition.z > 1.0:
            self.rate = -CustomGameObject.RATE
        elif self.worldPosition.z < 0.0:
            self.rate = CustomGameObject.RATE

# Chamado primeiro
def mutate(cont):
    old_object = cont.owner
    mutated_object = CustomGameObject(cont.owner)

    # Depois de chamar o construtor acima, as referências ao objeto antigo
    # não devem mais ser usadas.
    assert(old_object is not mutated_object)
    assert(old_object.invalid)
    assert(mutated_object is cont.owner)

# Chamado depois. Repare que agora estamos usando o objeto transformado.
def update(cont):
    cont.owner.update()
```

Ao herdar de objetos que não são vazios nem malhas, use o tipo específico. Por exemplo, herde de `BL_ArmatureObject` quando o objeto a transformar for uma armature.

```python

# Move e gira o objeto com W e A. Rode a cada frame (sensor Always com True Pulse).
import Range

obj = Range.logic.getCurrentController().owner
keys = Range.logic.keyboard.events

if keys[Range.events.WKEY]:
    obj.applyMovement((0, 0.1, 0), True)
if keys[Range.events.AKEY]:
    obj.applyRotation((0, 0, 0.05), True)
```

```python

# Lê e muda propriedades de jogo.
import Range

obj = Range.logic.getCurrentController().owner

obj["health"] = obj.get("health", 100) - 10

if obj["health"] <= 0:
    obj.endObject()
```

```python

# Procura o chão embaixo do objeto.
import Range

obj = Range.logic.getCurrentController().owner
below = obj.worldPosition - obj.getAxisVect((0, 0, 1))

hit, point, normal = obj.rayCast(below, obj, 10.0)

if hit is not None:
    print(hit.name, point)
```

```python

# Persegue o jogador quando ele chega perto.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner
player = scene.objects["Player"]

if obj.getDistanceTo(player) < 15.0:
    distance, direction, local = obj.getVectTo(player)
    obj.alignAxisToVect(direction, 1, 0.1)
    obj.applyMovement((0, 0.05, 0), True)
```

```python

# Toca os frames 1 a 30 de uma action.
import Range

obj = Range.logic.getCurrentController().owner

if not obj.isPlayingAction():
    obj.playAction("Walk", 1, 30)
```

```python

# Prende o objeto em uma mão e solta depois.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner

obj.setParent(scene.objects["Hand"])

# Depois:
obj.removeParent()
```

#### name

O nome do objeto.

**Tipo:** string

#### mass

A massa do objeto.

**Tipo:** float

> **Note:**
O objeto precisa de um controlador de física para a massa valer; sem ele, a massa é lida como 0.0.

#### friction

O atrito do objeto.

**Tipo:** float

#### isSuspendDynamics

O estado dinâmico do objeto (somente leitura).

**Tipo:** boolean

> **Tip:**
`suspendDynamics` e `restoreDynamics` permitem mudar esse estado.

#### linearDamping

O amortecimento linear do objeto, também chamado de amortecimento de translação. Pode ser definido junto com o amortecimento angular pelo método `setDamping`.

**Tipo:** float between 0 and 1 inclusive.

> **Note:**
O objeto precisa de um controlador de física para o amortecimento linear valer; sem ele, o valor é lido como 0.0.

#### angularDamping

O amortecimento angular do objeto, também chamado de amortecimento de rotação. Pode ser definido junto com o amortecimento linear pelo método `setDamping`.

**Tipo:** float between 0 and 1 inclusive.

> **Note:**
O objeto precisa de um controlador de física para o amortecimento angular valer; sem ele, o valor é lido como 0.0.

#### linVelocityMin

Obriga o objeto a continuar se movendo com uma velocidade mínima.

**Tipo:** float

> **Note:**
Vale só para objetos dinâmicos e rígidos.

> **Note:**
O valor 0.0 desliga esta opção.

> **Note:**
Enquanto o objeto está parado, a velocidade mínima não é aplicada.

#### linVelocityMax

Limita a velocidade linear máxima, para o objeto não passar de uma certa velocidade.

**Tipo:** float

> **Note:**
Vale só para objetos dinâmicos e rígidos.

> **Note:**
O valor 0.0 desliga esta opção (não deixa o objeto parado).

#### angularVelocityMin

Obriga o objeto a continuar girando com uma velocidade mínima. O valor 0.0 desliga.

**Tipo:** non-negative float

> **Note:**
Vale só para objetos dinâmicos e rígidos. Enquanto o objeto está parado, a velocidade mínima não é aplicada.

#### angularVelocityMax

Limita a velocidade angular máxima, para o objeto não girar além de uma certa velocidade. O valor 0.0 desliga o limite; não para a rotação.

**Tipo:** non-negative float

> **Note:**
Vale só para objetos dinâmicos e rígidos.

#### localInertia

O vetor de inércia do objeto em coordenadas locais. Somente leitura.

**Tipo:** Vector((ix, iy, iz))

#### parent

O objeto pai deste objeto (somente leitura).

**Tipo:** `KX_GameObject` or None

#### groupMembers

Devolve a lista de membros do grupo se o objeto for um objeto de grupo (instância de dupli group); caso contrário, devolve None.

**Tipo:** `EXP_ListValue` of `KX_GameObject` or None

#### groupObject

Devolve o objeto de grupo (instância de dupli group) a que o objeto pertence, ou None se ele não faz parte de um grupo.

**Tipo:** `KX_GameObject` or None

#### collisionGroup

O grupo de colisão do objeto.

**Tipo:** bitfield

#### collisionMask

A máscara de colisão do objeto.

**Tipo:** bitfield

#### collisionCallbacks

Lista de funções chamadas quando acontece uma colisão.

**Tipo:** list of functions and/or methods

As funções devem aceitar um argumento `(object)` ou quatro argumentos `(object, point, normal, points)`. Para simplificar, o primeiro ponto de colisão de cada objeto colidido vem no segundo e no terceiro argumento.

```python

# Como função
def callback_four(object, point, normal, points):
    print('Hit by %r with %i contacts points' % (object.name, len(points)))

def callback_three(object, point, normal):
    print('Hit by %r at %s with normal %s' % (object.name, point, normal))

def callback_one(object):
    print('Hit by %r' % object.name)

def register_callback(controller):
    controller.owner.collisionCallbacks.append(callback_four)
    controller.owner.collisionCallbacks.append(callback_three)
    controller.owner.collisionCallbacks.append(callback_one)

# Como método
class YourGameEntity(Range.types.KX_GameObject):
    def __init__(self, old_owner):
        self.collisionCallbacks.append(self.on_collision_four)
        self.collisionCallbacks.append(self.on_collision_three)
        self.collisionCallbacks.append(self.on_collision_one)

    def on_collision_four(self, object, point, normal, points):
        print('Hit by %r with %i contacts points' % (object.name, len(points)))

    def on_collision_three(self, object, point, normal):
        print('Hit by %r at %s with normal %s' % (object.name, point, normal))

    def on_collision_one(self, object):
        print('Hit by %r' % object.name)
```

> **Note:**
Por compatibilidade, uma função com número variável de argumentos (usando `*args`) recebe só o argumento `object`. A forma com quatro argumentos só é usada quando há mais de um argumento fixo (sem contar o `self` dos métodos).

#### scene

A cena do objeto (somente leitura).

**Tipo:** `KX_Scene` or None

#### visible

Indica se o objeto está visível.

**Tipo:** boolean

> **Note:**
A lógica do jogo continua rodando para objetos invisíveis.

#### layer

A máscara de camadas usada no render de sombras e de cube maps em tempo real.

**Tipo:** bitfield

#### cullingBox

A caixa de volume do objeto, usada no culling.

**Tipo:** `KX_BoundingBox`

#### culled

Devolve True se o objeto foi descartado pelo culling; caso contrário, False.

> **Caution:**
Esta variável devolve um valor inválido se for lida fora dos callbacks da cena `KX_Scene.pre_draw` e `KX_Scene.post_draw`.

**Tipo:** boolean (read only)

#### color

A cor do objeto. [r, g, b, a]

**Tipo:** `mathutils.Vector`

#### occlusion

Indica se o objeto participa do occlusion culling.

**Tipo:** boolean

#### physicsCulling

True se o objeto suspende a física conforme a distância até a câmera mais próxima.

**Tipo:** boolean

#### physicsCullingVelocity

Para a física depois que o objeto para.

**Tipo:** boolean

#### logicCulling

True se o objeto suspende a lógica e a animação conforme a distância até a câmera mais próxima.

**Tipo:** boolean

#### logicCullingComponents

Não suspende a execução dos componentes do objeto.

**Tipo:** boolean

#### physicsCullingRadius

Suspende a física do objeto se este raio for menor que a distância até a câmera mais próxima e `physicsCulling` estiver `True`.

**Tipo:** float

#### logicCullingRadius

Suspende a lógica e a animação do objeto se este raio for menor que a distância até a câmera mais próxima e `logicCulling` estiver `True`.

**Tipo:** float

#### ~~position~~

A posição do objeto. [x, y, z] Na escrita: posição local; na leitura: posição no mundo.

> **Obsoleto use :data:`localPosition` and :data:`worldPosition`.:**

**Tipo:** `mathutils.Vector`

#### ~~orientation~~

A orientação do objeto. Matriz 3x3. Também aceita um Quaternion ou um vetor Euler. Na escrita: orientação local; na leitura: orientação no mundo.

> **Obsoleto use :data:`localOrientation` and :data:`worldOrientation`.:**

**Tipo:** `mathutils.Matrix`

#### ~~scaling~~

O fator de escala do objeto. [sx, sy, sz] Na escrita: escala local; na leitura: escala no mundo.

> **Obsoleto use :data:`localScale` and :data:`worldScale`.:**

**Tipo:** `mathutils.Vector`

#### localOrientation

A orientação local do objeto. Matriz 3x3. Também aceita um Quaternion ou um vetor Euler.

**Tipo:** `mathutils.Matrix`

#### worldOrientation

A orientação do objeto no mundo. Matriz 3x3.

**Tipo:** `mathutils.Matrix`

#### localScale

O fator de escala local do objeto. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

#### worldScale

O fator de escala do objeto no mundo. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

#### localPosition

A posição local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

#### worldPosition

A posição do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

#### localTransform

A matriz de transformação local do objeto. Matriz 4x4.

**Tipo:** `mathutils.Matrix`

#### worldTransform

A matriz de transformação do objeto no mundo. Matriz 4x4.

**Tipo:** `mathutils.Matrix`

#### localLinearVelocity

A velocidade linear local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

#### worldLinearVelocity

A velocidade linear do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

#### localAngularVelocity

A velocidade angular local do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

#### worldAngularVelocity

A velocidade angular do objeto no mundo. [x, y, z]

**Tipo:** `mathutils.Vector`

#### gravity

A gravidade do objeto. [x, y, z]

**Tipo:** `mathutils.Vector`

#### timeOffset

Ajusta o atraso do slow parent durante o jogo.

**Tipo:** float

#### state

A máscara de estados do objeto, usando os 30 primeiros bits; pelo menos um bit precisa estar ligado.

**Tipo:** int

#### meshes

Lista das malhas deste objeto.

**Tipo:** list of `KX_Mesh`

> **Note:**
A maioria dos objetos usa só 1 malha.

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

#### batchGroup

O grupo de batch que contém a malha agrupada do objeto.

**Tipo:** `KX_BatchGroup`

#### sensors

Uma sequência de objetos `SCA_ISensor`, com busca por nome/índice e suporte a iteração.

**Tipo:** list

> **Note:**
Este atributo é experimental e pode ser removido (mas provavelmente não será).

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

#### controllers

Uma sequência de objetos `SCA_IController`, com busca por nome/índice e suporte a iteração.

**Tipo:** list of `SCA_ISensor`

> **Note:**
Este atributo é experimental e pode ser removido (mas provavelmente não será).

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

#### actuators

Uma lista de `SCA_IActuator`, com busca por nome/índice e suporte a iteração.

**Tipo:** list

> **Note:**
Este atributo é experimental e pode ser removido (mas provavelmente não será).

> **Note:**
Mudar esta lista não atualiza o KX_GameObject.

#### attrDict

Dá o dicionário interno de atributos Python do objeto, para acesso direto (mais rápido).

**Tipo:** dict

#### components

Todos os componentes Python.

**Tipo:** `EXP_ListValue` of `KX_PythonComponent`'s

#### children

Os filhos diretos deste objeto (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

#### childrenRecursive

Todos os filhos deste objeto, incluindo os filhos dos filhos (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

#### life

Quantos frames faltam para o objeto acabar, considerando um frame como 1/50 de segundo (somente leitura).

**Tipo:** float

#### debug

Se for True, as propriedades de depuração do objeto aparecem na tela.

**Tipo:** boolean

#### debugRecursive

Se for True, as propriedades de depuração do objeto e dos filhos aparecem na tela.

**Tipo:** boolean

#### currentLodLevel

O índice do nível de detalhe (LOD) que o objeto está usando agora (somente leitura).

**Tipo:** int

#### lodManager

Devolve o gerenciador de LOD do objeto, necessário para configurar os níveis de detalhe dele. O gerenciador é compartilhado entre as instâncias e pode ser trocado para usar os níveis de LOD de outro objeto. Se for definido como `None`, a malha do objeto volta a ser a do primeiro nível de LOD anterior.

**Tipo:** `KX_LodManager`

#### isDestructible

True se Physics > Destruction estiver ligado neste objeto, inclusive em objetos de camadas inativas (somente leitura).

**Tipo:** boolean

#### isExplosive

True se Physics > Explosive estiver ligado neste objeto, inclusive em objetos de camadas inativas (somente leitura).

**Tipo:** boolean

#### breakImpulse

O impulso que quebra este objeto destrutível, vindo de uma colisão ou de `KX_Scene.explode`. Começa com o Break Impulse do painel; mudar o valor afeta só esta instância. Em objetos que não são destrutíveis, lê 0.0, e escrever gera AttributeError.

**Tipo:** float

#### fuse

Segundos que faltam para este objeto explosivo detonar. O pavio conta a partir do momento em que o objeto entra no jogo (início da cena ou `KX_Scene.addObject`). 0.0 significa sem pavio; definir um valor acende o pavio. Em objetos que não são explosivos, escrever gera AttributeError.

**Tipo:** float

#### explosionRadius

Raio da explosão deste objeto explosivo, em metros. Como todos os atributos do painel Explosive abaixo, levanta `AttributeError` se o objeto não for explosivo.

**Tipo:** float

#### explosionForce

Impulso da explosão no centro; cai até 0 em `explosionRadius`.

**Tipo:** float

#### upBias

Empurrão extra para cima (0 a 5), para os objetos voarem em vez de deslizarem no chão.

**Tipo:** float

#### useOcclusion

Se a geometria estática entre a explosão e um objeto protege esse objeto.

**Tipo:** bool

#### explosionEffect

Objeto de uma camada inativa adicionado no ponto da explosão (fogo, fumaça, som), ou `None`. Precisa ser um objeto do arquivo da cena.

**Tipo:** `KX_GameObject` or None

#### effectLife

Segundos de vida do `explosionEffect` (0 = até a lógica dele o remover).

**Tipo:** float

#### useParticleExplosion

Liga a explosão de partículas GPU embutida (núcleo, fumaça e detritos).

**Tipo:** bool

#### particleSize

Tamanho da explosão de partículas: `'TINY'`, `'SMALL'`, `'MEDIUM'`, `'LARGE'` ou `'HUGE'`. Também escala a marca no chão.

**Tipo:** str

#### particleStyle

Do que a explosão é feita: `'FIRE'`, `'ELECTRIC'`, `'CONCRETE'` ou `'WATER'`. Mudar o estilo volta `fireColor`, `smokeColor` e `sparkColor` para as cores do estilo.

**Tipo:** str

#### fireColor

Tinta do núcleo da explosão de partículas (branco = cores naturais do estilo).

**Tipo:** Vector((r, g, b))

#### smokeColor

Cor da fumaça (nuvem de poeira, névoa) quando nasce.

**Tipo:** Vector((r, g, b))

#### sparkColor

Cor das faíscas (detritos, gotas).

**Tipo:** Vector((r, g, b))

#### fireAmount

Quantidade de partículas do núcleo, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

#### smokeAmount

Quantidade de fumaça, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

#### sparkAmount

Quantidade de faíscas, relativa ao tamanho (0 a 4, 0 = nenhuma).

**Tipo:** float

#### smokeDuration

Quanto tempo a fumaça dura, relativo ao estilo (0.2 a 4).

**Tipo:** float

#### blastSpeed

Força com que as partículas são lançadas, relativa ao tamanho (0.2 a 4).

**Tipo:** float

#### useGroundMark

Pinta o material de `groundMark` na superfície estática embaixo da explosão.

**Tipo:** bool

#### useMarkNearby

Com `useGroundMark`: pinta também uma marca menor nos objetos em volta da explosão (os 12 mais próximos).

**Tipo:** bool

#### groundMark

Objeto de malha de uma camada inativa cujo material é a marca no chão, ou `None`. Precisa ser um objeto do arquivo da cena.

**Tipo:** `KX_GameObject` or None

#### markSize

Tamanho da marca no chão, relativo a `particleSize` (0.1 a 4).

**Tipo:** float

#### markLife

Segundos que a marca fica no chão (0 = para sempre).

**Tipo:** float

#### onBreak

Lista de funções chamadas quando este objeto quebra, com os argumentos `(object, fragments)`. Elas rodam logo depois de os fragmentos entrarem na cena, antes de qualquer explosão empurrá-los. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

```python

def on_break(obj, fragments):
    print('%s broke into %d pieces' % (obj.name, len(fragments)))

controller.owner.onBreak.append(on_break)
```

#### onExplode

Lista de funções chamadas quando este objeto explode, com os argumentos `(object, position)`. Num objeto que é destrutível e explosivo ao mesmo tempo, elas rodam depois de `onBreak`. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

#### onDent

Lista de funções chamadas quando este objeto deformável amassa (colisão, explosão ou `dent`), com os argumentos `(object, point, impulse)`: o ponto atingido no mundo (o centro da explosão, no caso de explosão) e a força do impacto, por exemplo para tocar um som de metal ou soltar faíscas ali. Funções definidas num objeto de camada inativa são copiadas para todo objeto adicionado a partir dele.

**Tipo:** list of functions and/or methods

#### endObject()

Apaga este objeto. Pode substituir o atuador End Object.

A remoção de fato do objeto da cena acontece um pouco depois.

#### shatter(origin=None, burst=None)

Quebra este objeto destrutível agora, trocando-o pelos pedaços do grupo Fragments. Se o objeto também for explosivo, ele detona junto.

- **`origin`**: O ponto de onde os pedaços se afastam; por padrão, a posição do objeto.
  - tipo: 3D Vector
- **`burst`**: A velocidade dada aos pedaços para longe de origin; por padrão, o Burst Speed do painel.
  - tipo: float

**Retorna:** Os pedaços novos, ou uma lista vazia se o objeto não é destrutível ou já quebrou.

**Tipo do retorno:** list of `KX_GameObject`

#### detonate()

Faz este objeto explosivo explodir agora: uma explosão como `KX_Scene.explode` com os ajustes do painel, o objeto Effect e a remoção do objeto. Um explosivo destrutível também quebra.

**Retorna:** False se o objeto não é explosivo ou já explodiu.

**Tipo do retorno:** boolean

#### dent(point, direction, impulse)

Amassa este objeto deformável (painel Deformation) como um impacto da força dada: os vértices dentro do Radius do painel em volta de point andam na direção direction (para dentro do objeto) (impulse - Dent Impulse) * Depth, limitado por Max Depth. Só esta instância muda; outros objetos que usam a mesma malha mantêm a forma.

- **`point`**: Ponto atingido, no espaço do mundo.
  - tipo: 3D vector
- **`direction`**: Direção do impacto no espaço do mundo, invertida para apontar para dentro do objeto.
  - tipo: 3D vector
- **`impulse`**: Força do impacto (N*s), comparada com o Dent Impulse.
  - tipo: float

**Retorna:** False se o objeto não é deformável, se o impulso é fraco demais ou se nenhum vértice se moveu.

**Tipo do retorno:** boolean

#### resetDent()

Restaura a forma de um objeto amassado.

**Retorna:** False se o objeto nunca foi amassado.

**Tipo do retorno:** boolean

#### replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False)

Troca a malha deste objeto por outra. Funciona do mesmo jeito que o atuador.

- **`mesh`**: A malha nova, ou o nome dela.
  - tipo: `MeshProxy` or string
- **`useDisplayMesh`**: Se ligado, troca a malha visível (argumento opcional).
  - tipo: boolean
- **`usePhysicsMesh`**: Se ligado, troca a malha da física (argumento opcional).
  - tipo: boolean

#### setVisible(visible[, recursive])

Define se o objeto está visível.

- **`visible`**: O estado de visibilidade a definir.
  - tipo: boolean
- **`recursive`**: Argumento opcional para aplicar a visibilidade também a todos os filhos. Se não for passado, vale False.
  - tipo: boolean

#### setOcclusion(occlusion[, recursive])

Define se o objeto participa do occlusion culling.

- **`occlusion`**: O estado de oclusão a definir.
  - tipo: boolean
- **`recursive`**: Argumento opcional para aplicar a oclusão também a todos os filhos. Se não for passado, vale False.
  - tipo: boolean

#### alignAxisToVect(vect, axis=2, factor=1.0)

Alinha um dos eixos do objeto com o vetor dado.

- **`vect`**: O vetor com o qual alinhar o eixo.
  - tipo: 3D vector
- **`axis`**: O eixo a alinhar * 0: eixo X * 1: eixo Y * 2: eixo Z
  - tipo: integer
- **`factor`**: Gira só uma fração do caminho até o vetor alvo (0.0 a 1.0).
  - tipo: float

#### getAxisVect(vect)

Devolve o vetor do eixo girado pela orientação do objeto no mundo. Equivale a multiplicar o vetor pela matriz de orientação.

- **`vect`**: O vetor com o qual alinhar o eixo.
  - tipo: 3D Vector

**Retorna:** O vetor em relação à rotação do objeto.

**Tipo do retorno:** 3d vector.

#### applyMovement(movement[, local])

Move o objeto.

- **`movement`**: O vetor de movimento.
  - tipo: 3D Vector
- **`local`**: * False: movimento "global", relativo à orientação do mundo. * True: movimento "local", relativo à orientação do objeto. Se não for passado, vale False.
- **`local`**: boolean

#### applyRotation(rotation[, local])

Gira o objeto.

- **`rotation`**: O vetor de rotação.
  - tipo: 3D Vector
- **`local`**: * False: rotação "global", relativa à orientação do mundo. * True: rotação "local", relativa à orientação do objeto. Se não for passado, vale False.
- **`local`**: boolean

#### applyForce(force[, local])

Aplica uma força ao objeto.

Exige um objeto dinâmico.

- **`force`**: O vetor de força.
  - tipo: 3D Vector
- **`local`**: * False: força "global", relativa à orientação do mundo. * True: força "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

#### applyTorque(torque[, local])

Aplica um torque ao objeto.

Exige um objeto dinâmico.

- **`torque`**: O vetor de torque.
  - tipo: 3D Vector
- **`local`**: * False: torque "global", relativo à orientação do mundo. * True: torque "local", relativo à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

#### getLinearVelocity([local])

Lê a velocidade linear do objeto.

Este método devolve a velocidade do objeto no centro de massa, sem a parte angular.

- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

**Retorna:** A velocidade linear do objeto.

**Tipo do retorno:** Vector((vx, vy, vz))

#### setLinearVelocity(velocity[, local])

Define a velocidade linear do objeto.

Este método define a velocidade do objeto no centro de massa, sem a parte angular.

Exige um objeto dinâmico.

- **`velocity`**: O vetor de velocidade linear.
  - tipo: 3D Vector
- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

#### getAngularVelocity([local])

Lê a velocidade angular do objeto.

- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

**Retorna:** A velocidade angular do objeto.

**Tipo do retorno:** Vector((vx, vy, vz))

#### setAngularVelocity(velocity[, local])

Define a velocidade angular do objeto.

Exige um objeto dinâmico.

- **`velocity`**: O vetor de velocidade angular.
  - tipo: boolean
- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.

#### getVelocity([point])

Lê a velocidade do objeto no ponto indicado.

Lê a velocidade do objeto no ponto indicado, incluindo a parte angular.

- **`point`**: Ponto opcional onde medir a velocidade, em coordenadas locais. Se não for passado, vale (0, 0, 0).
  - tipo: 3D Vector

**Retorna:** A velocidade no ponto indicado.

**Tipo do retorno:** Vector((vx, vy, vz))

#### getReactionForce()

Lê a força de reação do objeto.

A força de reação é a força aplicada a este objeto no último passo da simulação. Inclui também impulsos, como os de colisões.

**Retorna:** A força de reação deste objeto.

**Tipo do retorno:** Vector((fx, fy, fz))

> **Note:**
Isto ainda não está implementado.

#### applyImpulse(point, impulse[, local])

Aplica um impulso ao objeto.

Aplica o impulso dado ao objeto no ponto indicado. Se point for diferente da posição, applyImpulse também muda o momento angular do objeto; caso contrário, só o momento linear muda.

- **`point`**: O ponto onde aplicar o impulso (em coordenadas do mundo ou locais).
  - tipo: point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
- **`impulse`**: O vetor de impulso.
  - tipo: 3D Vector
- **`local`**: * False: impulso "global", relativo às coordenadas e à orientação do mundo. * True: impulso "local", relativo às coordenadas e à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

#### setDamping(linear_damping, angular_damping)

Define `linearDamping` e `angularDamping` de uma vez. É mais eficiente do que definir cada um separadamente.

- **`linear_damping`**: Fator de amortecimento linear (de translação).
  - tipo: float ∈ [0, 1]
- **`angular_damping`**: Fator de amortecimento angular (de rotação).
  - tipo: float ∈ [0, 1]

#### suspendPhysics([freeConstraints])

Suspende a física deste objeto.

- **`freeConstraints`**: Se for `True`, as constraints de física usadas pelo objeto são apagadas. Se for `False` (o padrão), as constraints voltam quando a física é restaurada.
  - tipo: bool

#### restorePhysics()

Retoma a física deste objeto e volta a ligar as colisões.

#### suspendDynamics([ghost])

Suspende a física dinâmica deste objeto.

- **`ghost`**: Se for `True`, as colisões com o objeto são ignoradas, como a opção "ghost" do Blender. Se for `False` (o padrão), o objeto fica estático mas continua colidindo com os outros.
  - tipo: bool

> **Tip:**
`isSuspendDynamics` mostra se o objeto está suspenso.

#### restoreDynamics()

Retoma a física dinâmica deste objeto e volta a ligar as colisões; o objeto deixa de ser ghost.

> **Note:**
O objeto volta com a velocidade linear que tinha quando a dinâmica foi suspensa.

#### enableRigidBody()

Liga a física de corpo rígido deste objeto.

Com a física de corpo rígido, o objeto rola ao colidir.

#### disableRigidBody()

Desliga a física de corpo rígido deste objeto.

#### setParent(parent, compound=True, ghost=True)

Define o pai deste objeto. Os parâmetros opcionais compound e ghost controlam a forma de colisão:

Nesse caso, dá para escolher se ele fica ghost ou não:

- **`parent`**: O novo objeto pai.
  - tipo: `KX_GameObject`
- **`compound`**: Se a forma deve ser somada à forma composta do pai. * True: a forma do objeto entra na forma composta do pai. * False: o objeto mantém a própria forma.
  - tipo: boolean
- **`ghost`**: Se o objeto deve ficar ghost enquanto tiver pai. * True: fica ghost enquanto tiver pai. * False: continua sólido enquanto tiver pai.
  - tipo: boolean

> **Note:**
Se o objeto for do tipo sensor, ele continua ghost, seja qual for o parâmetro ghost.

#### removeParent()

Remove o pai deste objeto.

#### getPhysicsId()

Devolve o objeto de dados do usuário ligado ao controlador de física deste objeto.

#### getPropertyNames()

Lê a lista com os nomes de todas as propriedades.

**Retorna:** Os nomes de todas as propriedades deste objeto.

**Tipo do retorno:** list

#### getBoundBoxSize()

Tamanho da caixa envolvente (`cullingBox`) nos eixos do próprio objeto, com a escala de mundo.

**Retorna:** largura, profundidade e altura.

**Tipo do retorno:** `mathutils.Vector`

#### getBoundBoxCorners(space='WORLD')

Os 8 cantos da caixa envolvente. O canto `i` usa o X máximo com o bit 0 ligado, o Y máximo com o bit 1 e o Z máximo com o bit 2; assim, `[0]` é o canto mínimo e `[7]` o máximo.

- **`space`**: `'WORLD'` (posições no mundo), `'OFFSET'` (a partir de `worldPosition`, com rotação e escala) ou `'LOCAL'` (espaço do objeto, sem escala).
  - tipo: string

**Tipo do retorno:** list of `mathutils.Vector`

Os cantos `'WORLD'` podem ser passados direto para `boxInsideFrustum`, para testar se o objeto está na visão da câmera.

#### getBoundBoxVolume()

Compatibilidade com scripts da Range 1.x: retorna `[volume, canto1, ..., canto8]`. O volume usa a escala de mundo e os cantos são os `'OFFSET'` de `getBoundBoxCorners`; assim, `obj.worldPosition + box[i]` é um canto no mundo.

**Tipo do retorno:** list

#### getDistanceTo(other)

- **`other`**: Um ponto ou outro `KX_GameObject` até onde medir a distância.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** A distância até o outro objeto ou ponto.

**Tipo do retorno:** float

#### getVectTo(other)

Devolve o vetor e a distância até outro objeto ou ponto. O vetor vem normalizado, a não ser que a distância seja 0; nesse caso, vem um vetor de tamanho zero.

- **`other`**: Um ponto ou outro `KX_GameObject` até onde calcular o vetor e a distância.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** (distância, vetorGlobal(3), vetorLocal(3))

**Tipo do retorno:** 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))

#### rayCastTo(other, dist=0, prop="")

Olha na direção de outro ponto ou objeto e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop.

O raio sempre sai do centro do objeto, ignorando o próprio objeto. Ele vai até o centro de outro objeto ou até um ponto [x, y, z]. Use rayCast() se precisar do ponto atingido.

- **`other`**: [x, y, z] ou objeto na direção do qual o raio é lançado
  - tipo: `KX_GameObject` or 3-tuple
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`prop`**: Nome da propriedade que o objeto precisa ter; se omitido, detecta qualquer objeto
  - tipo: string

**Retorna:** O primeiro objeto atingido, ou None se não atingir nada ou se o objeto não tiver a propriedade

**Tipo do retorno:** `KX_GameObject`

#### rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF)

Olha de um ponto ou objeto até outro e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop. Se poly for 0, devolve uma tupla de 3 com o objeto, o ponto e a normal atingidos, ou (None, None, None) se não atingir nada. Se poly for 1, devolve uma tupla de 4 com um `KX_PolyProxy` como 4º elemento. Se poly for 2, devolve uma tupla de 5 com um vetor 2D com a coordenada UV do ponto atingido como 5º elemento.

```python

# atira ao longo do eixo gun-gunAim (gunAim não deve ter colisão)
obj, point, normal = gun.rayCast(gunAim, None, 50)
if obj:
   # faz alguma coisa
   pass
```

O parâmetro face define a orientação da normal.

* 0 => a normal sempre aponta para a origem do raio (como se o raio viesse de fora)
* 1 => a normal é a normal real da face (só para malhas; nos outros casos face não tem efeito)

Se xray for 1, o raio atravessa objetos (raio X); caso contrário, o primeiro objeto atingido (fora o próprio) para o raio. Os parâmetros prop e xray funcionam juntos assim:

* prop desligado, xray desligado: devolve o acerto mais próximo, ou nada se não houver objeto em todo o comprimento do raio.
* prop desligado, xray ligado: o mesmo.
* prop ligado, xray desligado: devolve o acerto mais próximo se ele tiver prop; caso contrário, nada.
* prop ligado, xray ligado: devolve o acerto mais próximo que tenha prop, ou nada se nenhum objeto com prop estiver em todo o comprimento do raio.

O `KX_PolyProxy` que vem como 4º elemento quando poly=1 dá informações sobre o polígono atingido. Se não atingir nada, ou se o objeto atingido não for uma malha estática, o 4º elemento é None.

O raio ignora objetos sem colisão e faces sem a opção de colisão, mas pode atingir objetos ghost.

- **`objto`**: [x, y, z] ou objeto até onde o raio é lançado
  - tipo: `KX_GameObject` or 3-tuple
- **`objfrom`**: [x, y, z] ou objeto de onde o raio sai; None ou omitido usa o centro do próprio objeto
  - tipo: `KX_GameObject` or 3-tuple or None
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`prop`**: Nome da propriedade que o objeto precisa ter; omitido ou "" detecta qualquer objeto
  - tipo: string
- **`face`**: Opção de normal: 1 devolve a normal da face; 0 ou omitido aponta a normal para a origem
  - tipo: integer
- **`xray`**: Opção de raio X: 1 pula os objetos que não têm prop; 0 ou omitido para no primeiro objeto
  - tipo: integer
- **`poly`**: Opção de polígono: 0, 1 ou 2 para devolver uma tupla de 3, 4 ou 5 com dados da face atingida. * 0 ou omitido: tupla de 3 (object, hitpoint, hitnormal), ou (None, None, None) se não atingir nada. * 1: tupla de 4, com um `KX_PolyProxy` como 4º elemento, ou None se não atingir nada ou se o objeto não usar forma de colisão de malha. * 2: tupla de 5, com uma tupla (u, v) da coordenada UV do ponto atingido como 5º elemento, ou None se não atingir nada, se o objeto não usar forma de colisão de malha ou não tiver mapeamento UV.
  - tipo: integer
- **`mask`**: Máscara de colisão: a máscara (16 camadas num inteiro de 16 bits) é combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só podem ser atingidos os objetos em que `collisionGroup & mask` for verdadeiro.
  - tipo: bitfield

**Retorna:** (object, hitpoint, hitnormal), ou (object, hitpoint, hitnormal, polygon), ou (object, hitpoint, hitnormal, polygon, hituv). * object, hitpoint e hitnormal são None se não atingir nada. * polygon só é válido se o objeto for válido e for estático, dinâmico com forma de colisão de malha ou soft body; senão é None. * hituv só é válido se polygon for válido e o objeto tiver mapeamento UV; senão é None.

**Tipo do retorno:**  * 3-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz)) * or 4-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`) * or 5-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`, 2-tuple (u, v))

> **Note:**
O raio ignora o objeto que chamou o método. Ele sai do centro do objeto, ou vai até ele, ou usa pontos [x, y, z].

#### collide(obj)

Testa se este objeto colide com o objeto `obj`.

- **`obj`**: O objeto com o qual testar a colisão
  - tipo: string or `KX_GameObject`

**Retorna:** (collide, points) * collide: True se este objeto colide com `obj` * points: os pontos de contato da colisão, ou None

**Tipo do retorno:** 2-tuple (boolean, list of `KX_CollisionContactPoint` or None)

#### setCollisionMargin(margin)

Define a margem de colisão do objeto.

- **`margin`**: A distância da margem de colisão, em unidades do Blender.
  - tipo: float

> **Note:**
Se este objeto não tiver controlador de física (ID de física zero), esta função gera RuntimeError.

#### sendMessage(subject, body="", to="")

Envia uma mensagem.

- **`subject`**: O assunto da mensagem
  - tipo: string
- **`body`**: O corpo da mensagem (opcional)
  - tipo: string
- **`to`**: O nome do objeto que vai receber a mensagem (opcional)
  - tipo: string

#### reinstancePhysicsMesh(gameObject, meshObject, dupli)

Atualiza a física com a malha alterada.

Sem argumentos, a malha da física é recriada a partir da primeira malha do objeto.

- **`gameObject`**: Argumento opcional: cria a forma de física a partir da malha deste objeto.
  - tipo: string, `KX_GameObject` or None
- **`meshObject`**: Argumento opcional: cria a forma de física a partir desta malha.
  - tipo: string, `MeshProxy` or None
- **`dupli`**: Argumento opcional: duplica a forma de física.
  - tipo: boolean

**Retorna:** True se a recriação deu certo, False se falhou.

**Tipo do retorno:** boolean

> **Note:**
Se este objeto tiver instâncias, elas também são atualizadas.

> **Note:**
O argumento gameObject tem a vantagem de converter a malha com os modificadores aplicados (como o Subdivision Surface).

> **Caution:**
Por enquanto, só objetos com malha de triângulos ou convex hull são suportados.

> **Caution:**
Falha se o objeto fizer parte de um objeto composto (pai ou filho).

> **Caution:**
Recriar a malha da física pode ser lento; rodar isso muitas vezes por segundo pesa no desempenho.

> **Caution:**
Duplicar a malha da física pode gastar bem mais memória; use esta opção só em malhas duplicadas, senão use `replacePhysicsShape`.

#### replacePhysicsShape(gameObject)

Troca a forma de física atual.

- **`gameObject`**: Cria a forma de física a partir deste objeto.
  - tipo: string, `KX_GameObject`

**Retorna:** True se a troca deu certo, False se falhou.

**Tipo do retorno:** boolean

> **Caution:**
Formas de malha de triângulos não são suportadas.

#### get(key[, default])

Devolve o valor da chave, ou o valor padrão se a chave não existir.
- **`key`**: A chave procurada
  - tipo: string
- **`default`**: Valor padrão opcional se a chave não existir; se não for passado, vale None.

**Retorna:** O valor da chave ou o padrão.

#### playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=KX_ACTION_BLEND_BLEND)

Toca uma ação.

- **`name`**: O nome da ação
  - tipo: string
- **`start`**: O frame inicial da ação
  - tipo: float
- **`end`**: O frame final da ação
  - tipo: float
- **`layer`**: A camada onde a ação vai tocar (ações em camadas diferentes são somadas/misturadas)
  - tipo: integer
- **`priority`**: Só toca esta ação se não houver outra tocando nesta camada com prioridade maior (número menor)
  - tipo: integer
- **`blendin`**: Quanto misturar esta animação com a anterior nesta camada
  - tipo: float
- **`play_mode`**: O modo de reprodução
  - tipo: one of `these constants`
- **`layer_weight`**: Quanto da camada anterior usar na mistura
  - tipo: float
- **`ipo_flags`**: Flags dos comportamentos antigos de IPO (force etc.)
  - tipo: int bitfield
- **`speed`**: A velocidade da ação como fator (1.0 = normal, 2.0 = o dobro etc.)
  - tipo: float
- **`blend_mode`**: Como misturar esta camada com as anteriores
  - tipo: one of `these constants`

#### stopAction([layer])

Para a ação que está tocando na camada indicada.

- **`layer`**: A camada a parar; se não for passada, vale 0.
  - tipo: integer

#### getActionFrame([layer])

Lê o frame atual da ação que está tocando na camada indicada.

- **`layer`**: A camada de onde ler o frame; se não for passada, vale 0.
  - tipo: integer

**Retorna:** O frame atual da ação

**Tipo do retorno:** float

#### getActionName([layer])

Lê o nome da ação que está tocando na camada indicada.

- **`layer`**: A camada de onde ler o nome da ação; se não for passada, vale 0.
  - tipo: integer

**Retorna:** O nome da ação atual

**Tipo do retorno:** string

#### setActionFrame(frame[, layer])

Define o frame atual da ação que está tocando na camada indicada.

- **`layer`**: A camada onde definir o frame; se não for passada, vale 0.
  - tipo: integer
- **`frame`**: O frame para onde levar a ação
  - tipo: float

#### isPlayingAction([layer])

Verifica se há uma ação tocando na camada indicada.

- **`layer`**: A camada a verificar; se não for passada, vale 0.
  - tipo: integer

**Retorna:** Se a ação está tocando ou não

**Tipo do retorno:** boolean

#### playNLA(speed=1.0, loop=True)

Toca as faixas do NLA de uma armature, como o NLA Editor faz. Faixas e strips mutadas são puladas, o Solo é respeitado e as faixas são misturadas de baixo para cima (Replace e Add, influência, blend in/out, repeat, scale, reverse e extrapolação). Ações tocadas com `playAction` são misturadas por cima do resultado do NLA.

Chamar de novo enquanto o NLA está tocando, com os mesmos argumentos, não reinicia; por isso pode ser chamado todo frame.

Ainda não suportado: strips de transição e meta, modos Subtract/Multiply (tocados como Replace), curvas de tempo da strip e NLA em objetos que não são armatures.

- **`speed`**: Velocidade de reprodução (1.0 = taxa de quadros de animação da cena, 0.0 = parado, use `setNLAFrame`; negativa toca de trás para frente a partir do último frame).
  - tipo: float
- **`loop`**: Recomeça da primeira strip depois que a última termina; senão, segura o último frame.
  - tipo: boolean

**Retorna:** True quando o NLA começou (o objeto é uma armature com pelo menos uma strip).

**Tipo do retorno:** boolean

#### stopNLA()

Para a reprodução do NLA. A armature mantém a pose atual.

#### isPlayingNLA()

**Retorna:** True enquanto o NLA está tocando (False depois que um NLA sem loop chegou ao fim).

**Tipo do retorno:** boolean

#### getNLAFrame()

**Retorna:** O frame atual do NLA.

**Tipo do retorno:** float

#### setNLAFrame(frame)

Pula o NLA para o frame dado, limitado ao intervalo das strips.

- **`frame`**: O frame do NLA.
  - tipo: float

#### addDebugProperty (name[, debug])

Adiciona uma propriedade à lista de depuração.

- **`name`**: O nome da propriedade a adicionar à lista de depuração.
  - tipo: string
- **`debug`**: O estado de depuração; se não for passado, vale True.
  - tipo: boolean

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### getCurvePoints()

 `método`

`getCurvePoints(world=True)`: pontos da primeira spline de um objeto Curve, como lista de `Vector`. Coordenadas do mundo por padrão; `world=False` devolve em coordenadas locais. Lista vazia se o objeto não for uma curva.

#### getTurnTo(other)

 `método`

Vetor local deste objeto até outro objeto ou ponto. Útil para saber para que lado virar.

**Retorna:** `Vector`

#### getVehicle()

*(novo na Anastacio)* `método`

O veículo criado pelo painel Vehicle deste objeto, ou `None`.

**Retorna:** `KX_VehicleWrapper`

#### getVehicleGearboxType()

*(novo na Anastacio)* `método`

Tipo de câmbio configurado no painel Vehicle.

**Retorna:** `int`

#### getVehicleGearRatios()

*(novo na Anastacio)* `método`

Relações das marchas configuradas no painel Vehicle.

**Retorna:** `tuple`

#### getVehicleMaxRPM()

*(novo na Anastacio)* `método`

Rotação máxima do motor configurada no painel Vehicle.

**Retorna:** `float`

#### getVehicleMaxTorque()

*(novo na Anastacio)* `método`

Torque máximo do motor configurado no painel Vehicle.

**Retorna:** `float`

#### getVehicleSteeringWheel()

*(novo na Anastacio)* `método`

Objeto do volante configurado no painel Vehicle, ou `None`.

**Retorna:** `KX_GameObject`

#### is_playing_take()

 `método`

`True` enquanto um Take do Rec Play move este objeto.

**Retorna:** `bool`

#### lookAt(vect, axis=2, factor=1.0)

*(novo na Anastacio)* `método`

Vira o objeto para que o eixo `axis` (0=X, 1=Y, 2=Z) aponte na direção `vect`. `factor` abaixo de 1 vira só uma parte (suaviza).

#### play_take(name)

 `método`

Toca o que um Take do Rec Play gravou deste objeto. `False` se não gravou nada dele.

**Retorna:** `bool`

#### resumeAnimations()

*(novo na Anastacio)* `método`

Retoma as animações pausadas por `suspendAnimations()`.

#### setActionLayerSpeed(layer, speed)

 `método`

Muda a velocidade da ação que toca na camada `layer`.

#### setActionLayerWeight(layer, layerWeight)

 `método`

Muda o peso (0 a 1) da camada de animação `layer`.

#### setCcdMotionThreshold(threshold)

*(novo na Anastacio)* `método`

Velocidade a partir da qual a detecção contínua de colisão (CCD) entra, evitando que objetos rápidos atravessem paredes.

#### setCcdSweptSphereRadius(radius)

*(novo na Anastacio)* `método`

Raio da esfera usada pela detecção contínua de colisão (CCD).

#### setHalfAnimations(enabled)

*(novo na Anastacio)* `método`

Com `True`, atualiza as animações do objeto em frames alternados, para economizar CPU.

#### setSoftAnchorsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez das âncoras.

#### setSoftAngularStiffness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez angular.

#### setSoftClusterSolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de clusters.

#### setSoftContactsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez dos contatos.

#### setSoftDampingCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): amortecimento.

#### setSoftDragCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): arrasto do ar.

#### setSoftDriftSolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de deriva.

#### setSoftDynamicFrictionCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): atrito dinâmico.

#### setSoftKineticContactsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez do contato com objetos cinemáticos.

#### setSoftLiftCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): sustentação (lift).

#### setSoftLinearStiffness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez linear.

#### setSoftPoseMatching(enabled)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): liga a tentativa de voltar à forma original.

#### setSoftPoseMatchingCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): força com que volta à forma original.

#### setSoftPositionSolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de posição.

#### setSoftPressureCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): pressão interna (efeito balão).

#### setSoftRigidContactsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez do contato com corpos rígidos.

#### setSoftVelocitiesCorrectionFactor(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): fator de correção das velocidades.

#### setSoftVelocitySolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de velocidade.

#### setSoftVolume(volume)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): volume que o corpo tenta manter.

#### setSoftVolumeConversationCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): conservação de volume.

#### setSoftVsKineticHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez contra corpos cinemáticos (clusters).

#### setSoftVsKineticImpulseSplitCluster(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): divisão de impulso contra corpos cinemáticos (clusters).

#### setSoftVsRigidHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez contra corpos rígidos (clusters).

#### setSoftVsRigidImpulseSplitCluster(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): divisão de impulso contra corpos rígidos (clusters).

#### setSoftVsSoftHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez contra outros corpos moles (clusters).

#### setSoftVsSoftImpulseSplitCluster(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): divisão de impulso contra outros corpos moles (clusters).

#### setVehicleGearRatios(relacoes)

*(novo na Anastacio)* `método`

Troca as relações de marcha do veículo. Recebe uma lista de números, uma por marcha.

#### setVehicleMaxRPM(valor)

*(novo na Anastacio)* `método`

Muda em jogo a rotação máxima (RPM) do motor do veículo (número >= 0).

#### setVehicleMaxTorque(valor)

*(novo na Anastacio)* `método`

Muda em jogo o torque máximo do motor do veículo deste objeto (número >= 0).

#### stop_take()

 `método`

Para o Take deste objeto e o devolve à lógica e à física.

#### strikeLightning(bolt=True)

 `método`

um raio cai agora (a chuva precisa estar ligada)

#### suspendAnimations()

*(novo na Anastacio)* `método`

Pausa todas as animações do objeto até `resumeAnimations()`.

#### activitycullingdistance

*(novo na Anastacio)* `atributo · só leitura`

Distância deste objeto até a câmera calculada pelo Activity Culling.

#### angularVelocity

*(novo na Anastacio)* `atributo`

Velocidade angular. Lê em coordenadas locais e escreve em coordenadas do mundo.

#### animationEventManager

*(novo na Anastacio)* `atributo · só leitura`

Gerenciador dos eventos de animação do objeto (`KX_AnimationEventManager`).

#### anisotropicFriction

*(novo na Anastacio)* `atributo`

Liga o atrito diferente por eixo (anisotrópico).

#### anisotropicFrictionCoefficients

*(novo na Anastacio)* `atributo`

Atrito `[x, y, z]` em cada eixo quando `anisotropicFriction` está ligado.

#### bendAngle

*(novo na Anastacio)* `atributo`

Quanto o objeto entorta a cada impacto.

#### bendAxis

*(novo na Anastacio)* `atributo`

Eixo em que o objeto entorta: `'X'`, `'Y'` ou `'Z'`.

#### bendMaxAngle

*(novo na Anastacio)* `atributo`

Ângulo máximo que o objeto pode entortar.

#### burstSpeed

*(novo na Anastacio)* `atributo`

Velocidade com que os fragmentos saem quando o objeto quebra.

#### debrisLifetime

*(novo na Anastacio)* `atributo`

Tempo de vida dos fragmentos depois da quebra.

#### decal

*(novo na Anastacio)* `atributo`

Objeto usado como decalque de arranhão nas colisões, ou `None`. Precisa ser um objeto do arquivo da cena.

#### decalLife

*(novo na Anastacio)* `atributo`

Tempo de vida de cada decalque.

#### decalSize

*(novo na Anastacio)* `atributo`

Tamanho dos decalques.

#### dentImpulse

*(novo na Anastacio)* `atributo`

Impulso mínimo de colisão para amassar o objeto.

#### fragments

*(novo na Anastacio)* `atributo`

Nome do grupo com os fragmentos usados quando o objeto quebra, ou `None`. Só em objetos destrutíveis; senão levanta `AttributeError`.

#### hiddenFromCamera

*(novo na Anastacio)* `atributo`

Câmera que não deve mostrar este objeto (ex.: o próprio carro no split screen), ou `None`.

#### impactImpulse

*(novo na Anastacio)* `atributo`

Impulso mínimo de colisão para um objeto explosivo detonar.

#### isDeformable

*(novo na Anastacio)* `atributo · só leitura`

`True` se o objeto tem as configurações de deformação ligadas (amassar, entortar, decalques).

#### linearVelocity

*(novo na Anastacio)* `atributo`

Velocidade linear. Lê em coordenadas locais e escreve em coordenadas do mundo.

#### maxDecals

*(novo na Anastacio)* `atributo`

Número máximo de decalques ao mesmo tempo neste objeto.

#### parentRecursive

*(novo na Anastacio)* `atributo · só leitura`

Lista de todos os pais acima do objeto, do mais próximo ao mais distante.

#### particles

*(novo na Anastacio)* `atributo · só leitura`

Sistema de partículas do objeto (`KX_ParticleSystem`), ou `None`.

#### particlesMix

*(novo na Anastacio)* `atributo · só leitura`

Segundo sistema de partículas (mistura) do objeto, ou `None`.

#### passIndex

*(novo na Anastacio)* `atributo`

Pass Index do objeto, usado para separar objetos em filtros e efeitos.

#### useBreakOnCollision

*(novo na Anastacio)* `atributo`

Se o objeto quebra ao colidir.

#### useChainReaction

*(novo na Anastacio)* `atributo`

Se a explosão deste objeto detona outros explosivos por perto.

#### useDentOnCollision

*(novo na Anastacio)* `atributo`

Se o objeto amassa ao colidir.

#### useExplodeOnImpact

*(novo na Anastacio)* `atributo`

Se o objeto explosivo detona ao sofrer um impacto acima de `impactImpulse`.

#### useInheritVelocity

*(novo na Anastacio)* `atributo`

Se os fragmentos herdam a velocidade do objeto ao quebrar.

---

## KX_InputSystem

> **Veja também:**
[`KX_InputTable`](#kx_inputtable), [`KX_PythonKeyboard`](#kx_pythonkeyboard), [`KX_PythonJoystick`](#kx_pythonjoystick)

Classe `Range.types.KX_InputSystem`.

```python
# Lista os mapas e as ações carregados.
import Range

for mapName, tables in Range.logic.inputSystem.inputMaps.items():
    print(mapName, list(tables))
```

```python
# Salva uma nova sensibilidade escolhida no menu de opções. Argumentos: mapa, ação, binding, valor.
import Range

system = Range.logic.inputSystem

if system.changeSensitivity("Player", "Jump", "keyboard", 0.5):
    system.reloadInputMaps()
```

```python
# Troca a tecla de uma ação. O mapa é o arquivo KeyMapping/Player.json, ao lado do jogo.
import Range

system = Range.logic.inputSystem

if system.changeKeyMap("Player", "Jump", "keyboard", "BUTTON", Range.events.SPACEKEY):
    system.reloadInputMaps()
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### changeJoystickIndex(inputMap, inputTable, name, value)

 `método`

Troca qual controle (índice do joystick) uma ação usa.

#### changeKeyMap(inputMap, inputTable, name, keyType, value)

 `método`

Troca a tecla ou botão ligado a uma ação. Use para menus de "redefinir controles".

#### changeSensitivity(inputMap, inputTable, name, value)

 `método`

Troca a sensibilidade de uma ação (ex.: do mouse ou do analógico).

#### reloadInputMaps()

 `método`

Recarrega os mapas de entrada do arquivo. É lento; evite chamar várias vezes.

#### inputMaps

 `atributo · só leitura`

Dicionário `{mapa: {tabela: KX_InputTable}}` com todos os mapas de entrada carregados.

---

## KX_InputTable

> **Veja também:**
[`KX_InputSystem`](#kx_inputsystem)

Classe `Range.types.KX_InputTable`.

```python
# Usa uma ação sem saber qual tecla está ligada a ela.
import Range

maps = Range.logic.inputSystem.inputMaps
jump = maps["Player"]["Jump"]

if jump.activated:
    print("Jump")
```

```python
# Lê um eixo.
import Range

move = Range.logic.inputSystem.inputMaps["Player"]["Move"]

if move.active:
    print(move.values)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### activated

 `atributo · só leitura`

`True` no frame em que a ação acabou de ser acionada.

#### active

 `atributo · só leitura`

`True` enquanto a ação está acionada.

#### released

 `atributo · só leitura`

`True` no frame em que a ação acabou de ser solta.

#### values

 `atributo · só leitura`

Valores atuais da ação: `True`/`False` num botão simples (`VECTOR1D`); tupla com 2 ou 3 números em eixos 2D ou 3D.

---

## KX_LibLoadStatus

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Um objeto com informações sobre uma operação LibLoad().

```python

# Mostra uma mensagem quando um LibLoad assíncrono termina
import Range

def finished_cb(status):
    print("Library (%s) loaded in %.2fms." % (status.libraryName, status.timeTaken))

Range.logic.LibLoad('myblend.blend', 'Scene', asynchronous=True).onFinish = finished_cb
```

```python

# Tela de carregamento: mostra o progresso. Rode update a cada frame (sensor Always com True Pulse).
import Range

status = Range.logic.LibLoad("//level2.range", "Scene", asynchronous=True)

def update(cont):
    cont.owner.text = "Loading %d%%" % (status.progress * 100)

    if status.finished:
        cont.owner.text = "Ready"
```

```python

# Adiciona um objeto assim que o arquivo dele termina de carregar.
import Range

def finished(status):
    print(status.libraryName, status.timeTaken)
    Range.logic.getCurrentScene().addObject("Enemy")

status = Range.logic.LibLoad("//enemies.range", "Scene", asynchronous=True)
status.onFinish = finished
```

#### onFinish

Um callback chamado quando o carregamento da lib termina.

**Tipo:** callable

#### finished

O status atual do carregamento da lib.

**Tipo:** boolean

#### progress

O progresso atual do carregamento da lib, como valor normalizado de 0.0 a 1.0.

**Tipo:** float

#### libraryName

O nome da biblioteca sendo carregada (o primeiro argumento de LibLoad).

**Tipo:** string

#### timeTaken

O tempo, em segundos, que o carregamento levou (0 até a operação terminar).

**Tipo:** float

---

## KX_LightningActuator

Classe `Range.types.KX_LightningActuator`.

```python
# Dispara um clarão com o raio visível.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Lightning"]

act.bolt = True
cont.activate(act)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### bolt

*(novo na Anastacio)* `atributo`

Liga o raio visível do relâmpago, além do clarão.

---

## KX_LightObject

Classe base: [`KX_GameObject`](#kx_gameobject)

> **Veja também:**
[`KX_WorldInfo`](#kx_worldinfo), [`KX_Scene`](#kx_scene)

!Painel Lamp no editor, com os tipos Point, Sun, Spot, Hemi e Area

Uma luz do jogo: o objeto **Lamp** do editor (Add > Lamp). O tipo escolhido no painel Lamp é lido no Python com `type`:

- **Point**: `NORMAL`, ilumina em todas as direções a partir de um ponto, como uma lâmpada comum.
- **Sun**: `SUN`, luz paralela vinda de longe, para a luz do dia.
- **Spot**: `SPOT`, um cone de luz, como uma lanterna.
- **Hemi**: `HEMI`, luz suave vinda de uma meia esfera, sem sombras.
- **Area**: não tem tipo próprio no jogo e é lida como `NORMAL`.

**Fake (GPU Particle)**, no mesmo menu Add > Lamp, não é uma luz: é uma malha com uma partícula brilhante, então não é um `KX_LightObject`.

```python

# Confere o tipo da lâmpada ou muda durante o jogo.
import Range

light = Range.logic.getCurrentController().owner

if light.type == light.NORMAL:
    print("Point lamp")
elif light.type == light.SUN:
    print("Sun lamp")
elif light.type == light.SPOT:
    print("Spot lamp")
elif light.type == light.HEMI:
    print("Hemi lamp")

light.type = light.SPOT  # transforma em uma lâmpada Spot
```

```python

# Liga uma luz vermelha de alerta.
import Range

co = Range.logic.getCurrentController()
light = co.owner

light.energy = 1.0
light.color = [1.0, 0.0, 0.0]
```

```python

# Pisca como uma tocha. Rode a cada frame (sensor Always com True Pulse).
import random
import Range

light = Range.logic.getCurrentController().owner
light.energy = random.uniform(0.8, 1.2)
```

```python

# Liga ou desliga a luz. Uma luz invisível não atualiza a sombra.
import Range

light = Range.logic.getCurrentController().owner
light.visible = not light.visible
```

```python

# Opção de qualidade da sombra. Tamanhos maiores ficam mais nítidos, mas usam mais memória de vídeo.
# Luzes Point mantêm o Size definido no editor.
import Range

light = Range.logic.getCurrentController().owner
light.shadowMapSize = 1024  # por exemplo 512, 1024, 2048 ou 4096
```

```python

# Para de redesenhar a sombra a cada frame quando a cena muda pouco.
import Range

light = Range.logic.getCurrentController().owner
light.staticShadow = True

# Depois, ao mover algo que projeta sombra, redesenha uma vez.
light.updateShadow()
```

```python

# Fecha o cone de uma luz Spot e suaviza a borda.
import Range

light = Range.logic.getCurrentController().owner
if light.type == light.SPOT:
    light.spotsize = 45.0  # ângulo do cone em graus
    light.spotblend = 0.3  # suavidade da borda, de 0 a 1
```

#### SPOT

Uma luz spot. Veja o atributo `type`

#### SUN

Uma luz pontual sem atenuação. Veja o atributo `type`

#### NORMAL

Uma luz pontual. Veja o atributo `type`

#### HEMI

Uma luz hemi. Veja o atributo `type`

#### type

O tipo da luz: SPOT, SUN ou NORMAL

#### energy

O brilho desta luz.

**Tipo:** float

#### shadowClipStart

O início do corte do shadow map; objetos mais perto que isso não geram sombra.

**Tipo:** float (read only)

#### shadowClipEnd

O fim do corte do shadow map; objetos além disso não geram sombra.

**Tipo:** float (read only)

#### shadowFrustumSize

Tamanho do frustum usado para criar o shadow map.

**Tipo:** float (read only)

#### shadowBindId

O número/id de bind da textura de sombra no OpenGL.

**Tipo:** int (read only)

#### shadowMapType

O tipo de shadow map (0 -> Simples; 1 -> Variance)

**Tipo:** int (read only)

#### shadowBias

O bias de amostragem do buffer de sombra.

**Tipo:** float (read only)

#### shadowBleedBias

O bias para reduzir o vazamento de luz nos shadow maps do tipo variance.

**Tipo:** float (read only)

#### useShadow

Devolve True se a luz tem a opção Shadow ligada; caso contrário, False.

**Tipo:** boolean (read only)

#### shadowColor

A cor das sombras desta luz. Preto = (0.0, 0.0, 0.0), branco = (1.0, 1.0, 1.0).

**Tipo:** `mathutils.Color` (read only)

#### shadowMatrix

Matriz que converte um vetor do espaço da câmera para o espaço de profundidade do buffer de sombra.

Calculada como: mat4_perspective_to_depth * mat4_lamp_to_perspective * mat4_world_to_lamp * mat4_cam_to_world.

mat4_perspective_to_depth é uma matriz fixa, definida assim:

0.5 0.0 0.0 0.5 0.0 0.5 0.0 0.5 0.0 0.0 0.5 0.5 0.0 0.0 0.0 1.0

Observação:

Existe uma matriz dessas para cada lâmpada que projeta sombra na cena.

**Tipo:** Matrix4x4 (read only)

#### distance

A distância máxima que esta luz ilumina (só luzes SPOT e NORMAL).

**Tipo:** float

#### color

A cor desta luz. Preto = [0.0, 0.0, 0.0], branco = [1.0, 1.0, 1.0].

**Tipo:** list [r, g, b]

#### lin_attenuation

A parte linear da atenuação desta luz (só luzes SPOT e NORMAL).

**Tipo:** float

#### quad_attenuation

A parte quadrática da atenuação desta luz (só luzes SPOT e NORMAL).

**Tipo:** float

#### spotsize

O ângulo do cone da luz spot, em graus (só luzes SPOT).

**Tipo:** float in [0 - 180].

#### spotblend

A distribuição da intensidade da luz spot (só luzes SPOT).

**Tipo:** float in [0 - 1]

> **Note:**
Valores mais altos deixam a luz mais concentrada.

#### shadowMapSize

Resolução do mapa de sombras em pixels (o Size da lâmpada). Ao definir este valor, o buffer de sombras é redimensionado em tempo real sem recompilar shaders, permitindo uma opção de qualidade de sombras (por exemplo, 512 / 1024 / 2048). Mapas de sombra em cascata mantêm sua proporção em relação a ele. Retorna 0 quando a lâmpada não possui buffer de sombras. Lâmpadas Point mantêm seu próprio tamanho.

**Tipo:** integer from 64 to 16384 (clamped to the graphics card maximum).

#### staticShadow

Liga as sombras estáticas. Por padrão (staticShadow=False), a sombra da lâmpada é recalculada a cada frame. Quando isso não for preciso, defina staticShadow=True e chame `updateShadow` para pedir uma atualização da sombra.

**Tipo:** boolean.

#### updateShadow()

Pede para a sombra ser atualizada no próximo frame, se a lâmpada usa sombra estática. Veja `staticShadow`.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### autoShadowUpdate

*(novo na Anastacio)* `atributo`

Quando `False`, a sombra desta luz para de ser recalculada a cada frame (economiza GPU em cenas paradas).

---

## KX_LodLevel

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Um nível de LOD do lod manager de um game object.

```python

# Lista os níveis de detalhe do objeto.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    for lod in obj.lodManager.levels:
        print(lod.level, lod.distance, lod.useMesh, lod.useMaterial)
```

```python

# Vê qual nível o objeto está usando agora.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    lod = obj.lodManager.levels[obj.currentLodLevel]
    print(lod.level, lod.mesh)
```

#### mesh

A malha usada neste nível de LOD (somente leitura).

**Tipo:** `RAS_MeshObject`

#### level

O número do nível de LOD (somente leitura).

**Tipo:** integer

#### distance

Distância a partir da qual este nível de detalhe é usado (somente leitura).

**Tipo:** float (0.0 to infinite)

#### hysteresis

Mudança mínima do fator de distância, em porcentagem, para voltar ao nível de detalhe anterior (somente leitura).

**Tipo:** float [0.0 to 100.0]

#### useMesh

True se o nível de LOD usa uma malha diferente da malha original do objeto (somente leitura).

**Tipo:** boolean

#### useMaterial

True se o nível de LOD usa um material diferente do material original da malha do objeto (somente leitura).

**Tipo:** boolean

#### useHysteresis

True se o nível de LOD usa substituição de histerese (somente leitura).

**Tipo:** boolean

---

## KX_LodManager

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Esta classe tem a lista de todos os níveis de detalhe usados por um game object.

```python

# Opção gráfica: valores acima de 1.0 trocam mais cedo para os níveis simples.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.distanceFactor = 2.0
```

```python

# Usa os mesmos níveis de detalhe em outro objeto.
import Range

scene = Range.logic.getCurrentScene()
scene.objects["TreeB"].lodManager = scene.objects["TreeA"].lodManager
```

```python

# Troca também a malha de física quando o nível muda.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.updatePhysics = True
```

#### levels

Devolve a lista de todos os níveis de detalhe do lod manager.

**Tipo:** list of `KX_LodLevel`

#### distanceFactor

Multiplicador da distância até a câmera.

**Tipo:** float

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### updatePhysics

 `atributo`

Também troca a malha de física quando o nível de detalhe (LOD) muda.

---

## KX_Mesh

Classe base: [`EXP_Value`](#exp_value)

> **Veja também:**
[`KX_MeshBuilder`](#kx_meshbuilder), [`KX_PolyProxy`](#kx_polyproxy), [`KX_VertexProxy`](#kx_vertexproxy), [`KX_BlenderMaterial`](#kx_blendermaterial)

Um objeto de malha.

Só dá para mudar as propriedades dos vértices de uma malha, não a topologia dela.

Para usar malhas bem, é bom saber um pouco de como a game engine lida com elas.

#. Mesh Objects are converted from Blender at scene load.
#. The Converter groups polygons by Material.  This means they can be sent to the renderer efficiently.  A material holds:

#. The texture.
#. The Blender material.
#. The Tile properties
#. The face properties - (From the "Texture Face" panel)
#. Transparency & z sorting
#. Light layer
#. Polygon shape (triangle/quad)
#. Game Object

#. Vertices will be split by face if necessary.  Vertices can only be shared between faces if:

#. They are at the same position
#. UV coordinates are the same
#. Their normals are the same (both polygons are "Set Smooth")
#. They are the same color, for example: a cube has 24 vertices: 6 faces with 4 vertices per face.

O jeito certo de percorrer todos os `KX_VertexProxy` de um game object

```python

from Range import logic

cont = logic.getCurrentController()
object = cont.owner

for mesh in object.meshes:
   for m_index in range(len(mesh.materials)):
      for v_index in range(mesh.getVertexArrayLength(m_index)):
         vertex = mesh.getVertex(m_index, v_index)
         # Faça algo com o vértice aqui...
         # ... ex.: pinta o vértice de vermelho.
         vertex.color = [1.0, 0.0, 0.0, 1.0]
```

#### materials

**Tipo:** list of `KX_BlenderMaterial` type

#### numPolygons

**Tipo:** integer

#### numMaterials

**Tipo:** integer

#### polygons

Devolve a lista de polígonos desta malha.

**Tipo:** `KX_PolyProxy` list (read only)

#### getMaterialName(matid)

Pega o nome do material indicado.

- **`matid`**: o material indicado.
  - tipo: integer

**Retorna:** o nome do material ligado.

**Tipo do retorno:** string

#### getTextureName(matid)

Pega o nome da textura do material indicado.

- **`matid`**: o material indicado
  - tipo: integer

**Retorna:** o nome da textura do material ligado.

**Tipo do retorno:** string

#### getVertexArrayLength(matid)

Pega o tamanho do array de vértices ligado ao material indicado.

Há um array de vértices para cada material.

- **`matid`**: o material indicado
  - tipo: integer

**Retorna:** o número de vértices no array de vértices.

**Tipo do retorno:** integer

#### getVertex(matid, index)

Pega o vértice indicado da malha.

- **`matid`**: o material indicado
  - tipo: integer
- **`index`**: o índice no array de vértices.
  - tipo: integer

**Retorna:** um objeto de vértice.

**Tipo do retorno:** `KX_VertexProxy`

#### getPolygon(index)

Pega o polígono indicado da malha.

- **`index`**: número do polígono
  - tipo: integer

**Retorna:** um objeto de polígono.

**Tipo do retorno:** `KX_PolyProxy`

#### transform(matid, matrix)

Transforma os vértices de uma malha.

- **`matid`**: índice do material; -1 transforma todos.
  - tipo: integer
- **`matrix`**: matriz de transformação.
  - tipo: 4x4 matrix [[float]]

#### transformUV(matid, matrix, uv_index=-1, uv_index_from=-1)

Transforma as UVs dos vértices de uma malha.

- **`matid`**: índice do material; -1 transforma todos.
  - tipo: integer
- **`matrix`**: matriz de transformação.
  - tipo: 4x4 matrix [[float]]
- **`uv_index`**: índice de UV opcional; -1 para todos, senão 0 ou 1.
  - tipo: integer
- **`uv_index_from`**: índice de UV opcional de onde copiar; -1 para transformar a UV atual.
  - tipo: integer

#### replaceMaterial(matid, material)

Troca o material do slot `matid` pelo material `material`.

- **`matid`**: O índice do material.
  - tipo: integer
- **`material`**: O material substituto.
  - tipo: `KX_BlenderMaterial`

> **Caution:**
Trocar o material de uma malha usada por muitos objetos pode ser lento. Não chame esta função a cada frame

#### copy()

Devolve uma cópia da malha.

**Retorna:** uma cópia da malha em uso.

**Tipo do retorno:** `KX_Mesh`.

#### constructBvh(transform=mathutils.Matrix.Identity(4), epsilon=0)

Devolve uma árvore BVH baseada na geometria da malha. Os índices dos elementos da árvore são iguais aos índices dos polígonos.

- **`transform`**: A matriz de transformação 4x4 aplicada aos vértices.
  - tipo: `mathutils.Matrix`
- **`epsilon`**: O epsilon de distância da árvore.
  - tipo: float

**Retorna:** Uma árvore BVH baseada na geometria da malha.

**Tipo do retorno:** `mathutils.bvhtree.BVHTree`

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### destruct()

 `método`

Apaga a malha da memória. Use só em malhas criadas por script que nenhum objeto usa mais.

---

## KX_MeshBuilder

> **Veja também:**
[`KX_MeshBuilderSlot`](#kx_meshbuilderslot), [`KX_Mesh`](#kx_mesh), [`KX_GameObject`](#kx_gameobject)

Classe `Range.types.KX_MeshBuilder`.

```python
# Cria um triângulo por script e coloca no objeto.
import Range

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder("Triangle", scene, ["UVMap"], ["Col"])
slot = builder.addSlot(own.meshes[0].materials[0])

a = slot.addVertex((0.0, 0.0, 0.0))
b = slot.addVertex((1.0, 0.0, 0.0))
c = slot.addVertex((0.0, 1.0, 0.0))
slot.addIndex([a, b, c])
slot.recalculateNormals()

own.replaceMesh(builder.finish())
```

```python
# Copia uma malha existente para alterar. Guarde o construtor em uma variável enquanto usa os slots.
import Range

own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder.FromMesh("Copy", own.meshes[0])
print(len(builder.slots))
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### addSlot(material, primitive=0)

 `método`

Cria uma parte da malha com o material dado. `primitive`: 0 triângulos (padrão), 1 pontos, 2 linhas.

**Retorna:** `KX_MeshBuilderSlot`

#### finish()

 `método`

Monta a malha com os slots e a registra na cena. Depois use `obj.replaceMesh()` para colocá-la num objeto.

**Retorna:** `KX_Mesh`

#### FromMesh(name, mesh)

 `método`

Cria um construtor a partir de uma malha existente, para copiá-la e editá-la.

**Retorna:** `KX_MeshBuilder`

#### slots

 `atributo · só leitura`

Lista dos slots (`KX_MeshBuilderSlot`) da malha.

---

## KX_MeshBuilderSlot

> **Veja também:**
[`KX_MeshBuilder`](#kx_meshbuilder), [`KX_Mesh`](#kx_mesh)

Classe `Range.types.KX_MeshBuilderSlot`.

```python
# Adiciona um quadrado feito de dois triângulos.
points = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
ids = [slot.addVertex(point) for point in points]

slot.addIndex([ids[0], ids[1], ids[2]])
slot.addIndex([ids[0], ids[2], ids[3]])
slot.recalculateNormals()
```

```python
# Mostra o que o slot tem.
print(len(slot.vertices), len(slot.indices))
print(slot.uvCount, slot.colorCount)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### addIndex(indices)

 `método`

Acrescenta índices de vértices (lista de inteiros) aos primitivos e, se for malha de triângulos, aos triângulos.

#### addPrimitiveIndex(indices)

 `método`

Acrescenta índices só à lista de primitivos (desenho).

#### addTriangleIndex(indices)

 `método`

Acrescenta índices só à lista de triângulos (física e raios).

#### addVertex(position, normal=None, tangent=None, uvs=None, colors=None)

 `método`

Acrescenta um vértice. `uvs` e `colors` são listas, uma entrada por camada.

**Retorna:** `int`

#### recalculateNormals()

 `método`

Recalcula as normais dos vértices a partir dos triângulos.

#### removePrimitiveIndex(start, end=-1)

 `método`

Remove índices de primitivos de `start` até `end`.

#### removeTriangleIndex(start, end=-1)

 `método`

Remove índices de triângulos de `start` até `end`.

#### removeVertex(start, end=-1)

 `método`

Remove vértices de `start` até `end`.

#### colorCount

 `atributo · só leitura`

Quantas camadas de cor de vértice o slot tem.

#### indices

 `atributo · só leitura`

Lista dos índices de primitivos.

#### material

 `atributo`

Material do slot.

#### primitive

 `atributo · só leitura`

Tipo de primitivo do slot (pontos, linhas ou triângulos).

#### triangleIndices

 `atributo · só leitura`

Lista dos índices de triângulos.

#### uvCount

 `atributo · só leitura`

Quantas camadas de UV o slot tem.

#### vertices

 `atributo · só leitura`

Lista dos vértices do slot.

---

## KX_MicrophoneSensor

Sensor Microphone: reage à voz do jogador.

```python
# Abre a boca do personagem enquanto o jogador fala.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Microphone"]
cont.owner["mouth"] = sensor.level
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### hold

*(novo na Anastacio)* `atributo`

Segundos, de 0 a 60: quanto a fala se mantém positiva, ou quanto silêncio é preciso.

#### level

*(novo na Anastacio)* `atributo · só leitura`

Nível da voz agora (só leitura).

#### mode

*(novo na Anastacio)* `atributo`

Modo: `0` falando (nível acima de `threshold`), `1` pico (um pulso, como palma ou sopro), `2` silêncio (depois de `hold` segundos abaixo de `threshold`).

#### peak

*(novo na Anastacio)* `atributo · só leitura`

Pico da voz (só leitura).

#### propName

*(novo na Anastacio)* `atributo`

Nome da propriedade do objeto ligada ao sensor.

#### threshold

*(novo na Anastacio)* `atributo`

Nível de voz que dispara o sensor, de 0 a 1.

---

## KX_MouseActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

O atuador Mouse controla a visibilidade do cursor do mouse e gira o objeto pai conforme o movimento do mouse.

```python
# Visão em primeira pessoa com limites para olhar para cima e para baixo.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Mouse"]

act.sensitivity = [2.0, 2.0]
act.limit_y = [-80.0, 80.0]
act.visible = False
cont.activate(act)
```

```python
# Centraliza a visão de novo.
import Range

act = Range.logic.getCurrentController().actuators["Mouse"]
act.reset()
```

#### reset()

Desfaz a rotação causada pelo atuador Mouse.

#### visible

A visibilidade do cursor do mouse.

**Tipo:** boolean

#### use_axis_x

O movimento do mouse no eixo x afeta a rotação do objeto.

**Tipo:** boolean

#### use_axis_y

O movimento do mouse no eixo y afeta a rotação do objeto.

**Tipo:** boolean

#### threshold

Quanto o mouse precisa andar antes de a rotação começar.

**Tipo:** `mathutils.Vector`

Os valores da lista devem ficar entre 0.0 e 0.5.

#### reset_x

O mouse fica travado no centro da tela no eixo x.

**Tipo:** boolean

#### reset_y

O mouse fica travado no centro da tela no eixo y.

**Tipo:** boolean

#### object_axis

O eixo 3D do objeto que gira com o movimento do mouse. ([x, y])

**Tipo:** list (vector of 2 integers from 0 to 2)

* KX_ACT_MOUSE_OBJECT_AXIS_X
* KX_ACT_MOUSE_OBJECT_AXIS_Y
* KX_ACT_MOUSE_OBJECT_AXIS_Z

#### local_x

A rotação causada pelo movimento do mouse no eixo x é local.

**Tipo:** boolean

#### local_y

A rotação causada pelo movimento do mouse no eixo y é local.

**Tipo:** boolean

#### sensitivity

Quanto de rotação o movimento do mouse nos eixos x e y causa.

**Tipo:** `mathutils.Vector`

Valores negativos invertem a rotação.

#### limit_x

Os ângulos mínimo e máximo de rotação causada pelo movimento do mouse no eixo x, em graus. limit_x[0] é o mínimo, limit_x[1] é o máximo.

**Tipo:** `mathutils.Vector`

#### limit_y

Os ângulos mínimo e máximo de rotação causada pelo movimento do mouse no eixo y, em graus. limit_y[0] é o mínimo, limit_y[1] é o máximo.

**Tipo:** `mathutils.Vector`

#### angle

O deslocamento de rotação atual causado pelo atuador Mouse, em graus.

**Tipo:** `mathutils.Vector`

---

## KX_MouseFocusSensor

Classe base: [`SCA_MouseSensor`](#sca_mousesensor)

O sensor Mouse focus detecta quando o mouse está sobre o game object atual.

O sensor Mouse focus transforma as coordenadas do mouse do espaço 2D do dispositivo para o espaço 3D e lança um raio a partir da câmera.

```python
# Seleciona o que está embaixo do mouse.
import Range

sensor = Range.logic.getCurrentController().sensors["MouseOver"]

if sensor.positive:
    print(sensor.hitObject.name, sensor.hitPosition)
```

#### raySource

A origem do raio no espaço do mundo (a posição da vista).

**Tipo:** list (vector of 3 floats)

#### rayTarget

O alvo do raio no espaço do mundo.

**Tipo:** list (vector of 3 floats)

#### rayDirection

`rayTarget` - `raySource`, normalizado.

**Tipo:** list (normalized vector of 3 floats)

#### hitObject

o último objeto sob o mouse.

**Tipo:** `KX_GameObject` or None

#### hitPosition

A posição, no espaço do mundo, da interseção do raio.

**Tipo:** list (vector of 3 floats)

#### hitNormal

a normal, no espaço do mundo, da face no ponto de interseção.

**Tipo:** list (normalized vector of 3 floats)

#### hitUV

as coordenadas UV no ponto de interseção.

**Tipo:** list (vector of 2 floats)

Se o objeto não tem mapeamento UV, devolve [0, 0].

As coordenadas UV não são normalizadas; podem ser < 0 ou > 1 dependendo do mapeamento UV.

#### usePulseFocus

Quando ligado, passar o mouse sobre outro objeto gera um pulso (só usado com a opção 'Mouse Over Any' do sensor).

**Tipo:** boolean

#### useXRay

Se ligado, o sensor enxerga através de game objects que não têm a propriedade ou o material escolhido.

**Tipo:** boolean

#### mask

A máscara de colisão (16 layers mapeadas num inteiro de 16 bits) combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só os objetos em que `collisionGroup & mask` é verdadeiro podem ser atingidos.

**Tipo:** bitfield

#### propName

A propriedade ou o material que o sensor procura.

**Tipo:** string

#### useMaterial

Define se o sensor procura uma propriedade ou um material. KX_True = procura material; KX_False = procura propriedade.

**Tipo:** boolean

---

## KX_MovementSensor

Classe `Range.types.KX_MovementSensor`.

```python
# Dispara quando o objeto se move em qualquer eixo.
import Range

sensor = Range.logic.getCurrentController().sensors["Movement"]

sensor.axis = 6
sensor.threshold = 0.05

if sensor.positive:
    print("Moving")
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### axis

 `atributo`

Eixo vigiado: 0 a 2 = +X, +Y, +Z; 3 a 5 = -X, -Y, -Z; 6 = todos.

#### threshold

 `atributo`

Quanto o objeto precisa se mover para o sensor disparar.

---

## KX_NavMeshObject

Classe base: [`KX_GameObject`](#kx_gameobject)

> **Veja também:**
[`KX_SteeringActuator`](#kx_steeringactuator)

Interface Python para usar e controlar navigation meshes.

Uma navigation mesh com a propriedade de jogo Boolean `dynamic_navmesh` igual a True é construída em tiles quando o jogo começa, para que obstáculos possam recortá-la em tempo de execução. Objetos com "Create Obstacle" recortam automaticamente; `addObstacle` adiciona qualquer outro objeto. Os caminhos podem ser um pouco diferentes dos da navigation mesh estática.

```python

# Acha um caminho do objeto até o jogador.
import Range

scene = Range.logic.getCurrentScene()
owner = Range.logic.getCurrentController().owner

navmesh = scene.objects["Navmesh"]
player = scene.objects["Player"]

path = navmesh.findPath(owner.worldPosition, player.worldPosition)
print(len(path), "points")
```

```python

# Confere se há parede até o jogador: fator abaixo de 1.0 quer dizer que o raio parou antes.
import Range

scene = Range.logic.getCurrentScene()
owner = Range.logic.getCurrentController().owner

navmesh = scene.objects["Navmesh"]
player = scene.objects["Player"]

if navmesh.raycast(owner.worldPosition, player.worldPosition) < 1.0:
    print("Something is in the way")
```

```python

# Desenha a navigation mesh para depurar. Rode a cada frame (sensor Always com True Pulse).
import Range

navmesh = Range.logic.getCurrentScene().objects["Navmesh"]
navmesh.draw(Range.logic.RM_TRIS)
```

```python

# Navigation mesh dinâmica: uma caixa bloqueia a passagem e depois libera.
import Range

scene = Range.logic.getCurrentScene()
navmesh = scene.objects["Navmesh"]
crate = scene.objects["Crate"]

if navmesh.dynamic:
    navmesh.addObstacle(crate, 1.5)

# Depois, quando a caixa sair:
navmesh.removeObstacle(crate)
```

#### dynamic

True quando a navigation mesh foi construída em tiles e obstáculos podem recortá-la (somente leitura).

**Tipo:** boolean

#### version

Aumenta quando a navigation mesh é reconstruída ou termina de mudar por causa de obstáculos (somente leitura). Caminhos achados com uma versão mais antiga podem atravessar obstáculos novos.

**Tipo:** integer

#### findPath(start, goal)

Acha o caminho do ponto de início até o ponto de destino.

- **`start`**: o ponto de início
- **`start`**: Vetor 3D
- **`goal`**: o ponto de destino
- **`start`**: Vetor 3D

**Retorna:** um caminho como lista de pontos

**Tipo do retorno:** list of points

#### raycast(start, goal)

Lança um raio do ponto de início até o ponto de destino.

- **`start`**: o ponto de início
- **`start`**: Vetor 3D
- **`goal`**: o ponto de destino
- **`start`**: Vetor 3D

**Retorna:** o fator de acerto

**Tipo do retorno:** float

#### draw(mode)

Desenha uma malha de depuração da navigation mesh. Numa navigation mesh dinâmica, os cilindros de obstáculo são desenhados em amarelo.

- **`mode`**: o modo de desenho (uma `destas constantes`)
- **`mode`**: inteiro

**Retorna:** None

#### rebuild()

Reconstrói a navigation mesh.

**Retorna:** None

#### addObstacle(object, radius=0.0)

Faz o objeto recortar todas as navigation meshes dinâmicas da cena, acompanhando-o quando ele se move. Chamar de novo muda o raio. Não tem efeito em navigation meshes estáticas.

- **`object`**: o obstáculo, na mesma cena da navigation mesh
  - tipo: `KX_GameObject` or string
- **`radius`**: o raio, no mundo, do cilindro do obstáculo; 0.0 usa o raio do "Create Obstacle" do objeto ou metade do tamanho da bounding box
  - tipo: float

**Retorna:** None

#### removeObstacle(object)

Faz o objeto parar de recortar as navigation meshes dinâmicas, inclusive objetos com "Create Obstacle".

- **`object`**: o obstáculo
  - tipo: `KX_GameObject` or string

**Retorna:** None

---

## KX_NearSensor

Classe base: [`KX_CollisionSensor`](#kx_collisionsensor)

O sensor near é uma forma especializada de sensor de toque.

```python
# Abre a porta quando alguém chega perto e só fecha mais longe.
import Range

sensor = Range.logic.getCurrentController().sensors["Near"]

sensor.distance = 3.0
sensor.resetDistance = 5.0

if sensor.positive:
    print(sensor.hitObject.name, "is near")
```

#### distance

O sensor near ativa quando um objeto está dentro desta distância.

**Tipo:** float

#### resetDistance

O sensor near desativa quando o objeto passa desta distância.

**Tipo:** float

---

## KX_NetworkMessageActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Message

```python
# Envia uma mensagem para objetos da cena.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Message"]

act.subject = "door_open"
act.body = "north"
act.usePropBody = False
cont.activate(act)
```

#### propName

As mensagens só são enviadas para objetos com o nome de propriedade indicado.

**Tipo:** string

#### subject

O campo assunto da mensagem.

**Tipo:** string

#### body

O corpo da mensagem.

**Tipo:** string

#### usePropBody

Envia uma propriedade em vez de uma mensagem com corpo normal.

**Tipo:** boolean

---

## KX_NetworkMessageSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

O logic brick do sensor Message.

Por enquanto só redes loopback (locais) são suportadas.

```python
# Lê as mensagens que chegaram neste quadro.
import Range

sensor = Range.logic.getCurrentController().sensors["Message"]

if sensor.positive:
    for subject, body in zip(sensor.subjects, sensor.bodies):
        print(subject, body)
```

#### subject

O assunto que o sensor procura.

**Tipo:** string

#### frameMessageCount

O número de mensagens recebidas desde o último frame (somente leitura).

**Tipo:** integer

#### subjects

A lista dos assuntos das mensagens recebidas (somente leitura).

**Tipo:** list of strings

#### bodies

A lista dos corpos das mensagens recebidas (somente leitura).

**Tipo:** list of strings

---

## KX_ObjectActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

O atuador de objeto ("Motion Actuator") aplica força, torque, deslocamento, deslocamento angular, velocidade ou velocidade angular a um objeto. O controle servo permite regular a força para atingir uma velocidade alvo.

```python
# Anda para frente com velocidade constante.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Motion"]

act.linV = (0.0, 5.0, 0.0)
act.useLocalLinV = True
cont.activate(act)
```

```python
# Empurra o objeto e gira.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Motion"]

act.force = (0.0, 0.0, 50.0)
act.torque = (0.0, 0.0, 2.0)
cont.activate(act)
```

#### force

A força aplicada pelo atuador.

**Tipo:** Vector((x, y, z))

#### useLocalForce

Flag que diz se a força é local.

**Tipo:** boolean

#### torque

O torque aplicado pelo atuador.

**Tipo:** Vector((x, y, z))

#### useLocalTorque

Flag que diz se o torque é local.

**Tipo:** boolean

#### dLoc

O vetor de deslocamento aplicado pelo atuador.

**Tipo:** Vector((x, y, z))

#### useLocalDLoc

Flag que diz se o dLoc é local.

**Tipo:** boolean

#### dRot

O vetor de deslocamento angular aplicado pelo atuador

**Tipo:** Vector((x, y, z))

> **Note:**
Como o deslocamento é aplicado a cada frame, é preciso ajustá-lo pelo frame rate, ou a experiência de jogo vai depender da velocidade do computador do jogador.

#### useLocalDRot

Flag que diz se o dRot é local.

**Tipo:** boolean

#### linV

A velocidade linear aplicada pelo atuador.

**Tipo:** Vector((x, y, z))

#### useLocalLinV

Flag que diz se a velocidade linear é local.

**Tipo:** boolean

> **Note:**
Esta é a velocidade alvo dos controladores servo.

#### angV

A velocidade angular aplicada pelo atuador.

**Tipo:** Vector((x, y, z))

#### useLocalAngV

Flag que diz se a velocidade angular é local.

**Tipo:** boolean

#### damping

O parâmetro de amortecimento do controlador servo.

**Tipo:** short

#### forceLimitX

O limite mín./máx. de força no eixo X, e liga ou desliga os limites no controlador servo.

**Tipo:** list [min(float), max(float), bool]

#### forceLimitY

O limite mín./máx. de força no eixo Y, e liga ou desliga os limites no controlador servo.

**Tipo:** list [min(float), max(float), bool]

#### forceLimitZ

O limite mín./máx. de força no eixo Z, e liga ou desliga os limites no controlador servo.

**Tipo:** list [min(float), max(float), bool]

#### pid

Os coeficientes PID do controlador servo.

**Tipo:** list of floats [proportional, integral, derivate]

#### reference

O objeto usado como referência para calcular a velocidade no controlador servo.

**Tipo:** `KX_GameObject` or None

---

## KX_ParentActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

O atuador parent define ou remove o objeto pai de um objeto.

```python
# Prende o objeto em outro.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Parent"]

act.mode = Range.logic.KX_PARENT_SET
act.object = Range.logic.getCurrentScene().objects["Hand"]
act.ghost = True
cont.activate(act)
```

```python
# Solta.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Parent"]

act.mode = Range.logic.KX_PARENT_REMOVE
cont.activate(act)
```

#### object

o objeto que este atuador define como pai.

**Tipo:** `KX_GameObject` or None

#### mode

O modo deste atuador.

**Tipo:** integer from 0 to 1.

#### compound

Se a forma do objeto deve ser adicionada à forma composta do pai ao fazer o parent.

Só tem efeito se o pai já for uma forma composta.

**Tipo:** boolean

#### ghost

Se o objeto deve virar ghost ao fazer o parent. Só tem efeito se a forma não for adicionada à forma composta do pai.

**Tipo:** boolean

---

## KX_ParticleSystem

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`KX_Scene`](#kx_scene)

Classe `Range.types.KX_ParticleSystem`.

```python
# Muda o fogo do objeto com o jogo rodando.
import Range

own = Range.logic.getCurrentController().owner
particles = own.particles

if particles is not None:
    particles.particleCount = 200
    particles.lifetime = 1.5
    particles.blendMode = "ADDITIVE"
```

```python
# Uma explosão só.
import Range

particles = Range.logic.getCurrentController().owner.particles

particles.emissionMode = "BURST"
particles.burst()
```

```python
# Para de emitir.
import Range

particles = Range.logic.getCurrentController().owner.particles
particles.enabled = False
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### burst()

 `método`

Solta todas as partículas de uma vez no próximo frame. Só em emissores com `burstMode` ligado.

#### billboardMode

*(novo na Anastacio)* `atributo`

Como as partículas ficam viradas para a câmera: `'FULL'` ou `'VERTICAL'` (gira só no eixo vertical).

#### blendMode

*(novo na Anastacio)* `atributo`

Como as partículas se misturam com a cena: `'ALPHA'` ou `'ADDITIVE'`. Valor desconhecido levanta `ValueError`.

#### burstInterval

*(novo na Anastacio)* `atributo`

Intervalo, em segundos, entre as rajadas automáticas do modo burst.

#### burstMode

*(novo na Anastacio)* `atributo`

`True` emite em rajadas (explosões); `False` emite sem parar.

#### collisionBounce

 `atributo`

Quanto a partícula quica ao bater (0 = não quica).

#### collisionFriction

 `atributo`

Atrito da partícula ao deslizar depois de bater.

#### collisionHeight

 `atributo`

Altura do plano do chão quando `collisionMode` é 1.

#### collisionMode

 `atributo`

Colisão das partículas: 0 nenhuma, 1 plano do chão, 2 com o que aparece na tela (screen-space).

#### color

 `atributo`

Cor inicial `[r, g, b, a]` das partículas.

#### debugUI

 `atributo · só leitura`

`True` quando o painel de depuração do sistema de partículas está aberto.

#### drag

*(novo na Anastacio)* `atributo`

Resistência do ar: quanto as partículas perdem velocidade com o tempo.

#### emissionAngle

 `atributo`

Abertura do cone de emissão, em graus.

#### emissionDirection

 `atributo`

Direção `[x, y, z]` em que as partículas saem.

#### emissionMode

*(novo na Anastacio)* `atributo`

Modo de emissão: `'CONTINUOUS'` ou `'BURST'` (todas de uma vez). `burstMode` acompanha este valor.

#### emitterPosition

 `atributo`

Posição `[x, y, z]` do emissor em relação ao objeto.

#### emitterRadius

 `atributo`

Raio da área de onde as partículas nascem.

#### enabled

 `atributo`

Liga ou desliga a emissão.

#### endColor

 `atributo`

Cor `[r, g, b, a]` da partícula no fim da vida (a cor vai mudando de `color` até ela).

#### endSize

 `atributo`

Tamanho da partícula no fim da vida.

#### flipbook

*(novo na Anastacio)* `atributo`

#### fragmentShaderPath

 `atributo`

Caminho de um `.glsl` próprio para desenhar as partículas. Vazio volta ao visual padrão.

#### gravity

 `atributo`

Gravidade aplicada às partículas.

#### lifetime

 `atributo`

Tempo de vida de cada partícula, em segundos.

#### particleCount

 `atributo`

Quantidade máxima de partículas vivas.

#### size

 `atributo`

Tamanho inicial das partículas.

#### texture

 `atributo`

Caminho da imagem usada nas partículas. Vazio remove a textura.

#### useBackfaceCulling

*(novo na Anastacio)* `atributo`

Se as partículas deixam de ser desenhadas quando vistas por trás.

#### useDebugUi

*(novo na Anastacio)* `atributo`

Mostra o painel de depuração do emissor durante o jogo.

#### useObjectRotation

*(novo na Anastacio)* `atributo`

#### useVortex

*(novo na Anastacio)* `atributo`

Liga o redemoinho: as partículas sobem girando em volta do emissor.

#### velocity

 `atributo`

Velocidade inicial das partículas.

#### velocityRandomness

 `atributo`

Variação aleatória da velocidade inicial (0 = todas iguais).

#### vortexHeight

*(novo na Anastacio)* `atributo`

Altura do redemoinho.

#### vortexRadiusTop

*(novo na Anastacio)* `atributo`

Raio do redemoinho no topo.

#### vortexRotationSpeed

*(novo na Anastacio)* `atributo`

Velocidade de rotação do redemoinho.

---

## KX_PlanarMap

Classe base: [`KX_TextureRenderer`](#kx_texturerenderer)

> **Veja também:**
[`KX_CubeMap`](#kx_cubemap), [`KX_TextureRenderer`](#kx_texturerenderer)

API Python para texturas de planar map em tempo real.

```python
# Atualiza um espelho só quando precisa.
import Range

own = Range.logic.getCurrentController().owner
mirror = own.meshes[0].materials[0].textures[0].renderer

mirror.autoUpdate = False
mirror.update()
print(mirror.normal)
```

#### normal

Normal do plano usada para calcular a orientação de reflexão ou refração da câmera de render.

**Tipo:** `mathutils.Vector`

---

## KX_PolyProxy

Classe base: [`SCA_IObject`](#sca_iobject)

Um polígono guarda o índice dos vértices que o formam.

Nota: os atributos do polígono são somente leitura; para mudar as configurações de um vértice, pegue o vertex proxy.

```python
# Descobre o material da face atingida por um raio.
import Range

own = Range.logic.getCurrentController().owner
hit, point, normal, poly = own.rayCast((0, 0, -10), own, 20.0, "", 0, 0, 1)

if poly is not None:
    print(poly.material_name, poly.getNumVertex())
```

```python
# Lê os vértices da primeira face de uma malha.
import Range

mesh = Range.logic.getCurrentController().owner.meshes[0]
poly = mesh.getPolygon(0)

for i in range(poly.getNumVertex()):
    print(poly.getVertexIndex(i))
```

#### material_name

O nome do material do polígono; vazio se não houver material.

**Tipo:** string

#### material

O material do polígono.

**Tipo:** `KX_BlenderMaterial`

#### texture_name

O nome da textura do polígono.

**Tipo:** string

#### material_id

O índice do material do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

#### v1

índice do primeiro vértice do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

#### v2

índice do segundo vértice do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

#### v3

índice do terceiro vértice do polígono; use para pegar o vertex proxy a partir do mesh proxy.

**Tipo:** integer

#### ~~v4~~

> **Obsoleto polygons are triangles.:**

**Tipo:** integer

#### visible

estado de visibilidade do polígono: 1=visível, 0=invisível.

**Tipo:** integer

#### collide

estado de colisão do polígono: 1=recebe colisão, 0=sem colisão.

**Tipo:** integer

#### vertices

Devolve a lista de vértices deste polígono.

**Tipo:** `KX_VertexProxy` list (read only)

#### getMaterialName()

Devolve o nome do material do polígono com o prefixo MA

**Retorna:** nome do material

**Tipo do retorno:** string

#### getMaterial()

**Retorna:** O material do polígono

**Tipo do retorno:** `KX_BlenderMaterial`

#### getTextureName()

**Retorna:** O nome da textura

**Tipo do retorno:** string

#### getMaterialIndex()

Devolve o índice do material bucket do polígono. Este índice e os devolvidos por getVertexIndex() são necessários para pegar o vertex proxy a partir de `MeshProxy`.

**Retorna:** o índice do material na malha

**Tipo do retorno:** integer

#### getNumVertex()

Devolve o número de vértices do polígono.

**Retorna:** número de vértices.

**Tipo do retorno:** integer

#### isVisible()

Diz se o polígono está visível ou não

**Retorna:** 0=invisível, 1=visível

**Tipo do retorno:** boolean

#### isCollider()

Diz se o polígono recebe colisão ou não

**Retorna:** 0=sem colisão, 1=recebe colisão

**Tipo do retorno:** integer

#### getVertexIndex(vertex)

Devolve o índice, na malha, de um vértice do polígono. Este índice e o devolvido por getMaterialIndex() são necessários para pegar o vertex proxy a partir de `MeshProxy`.

- **`vertex`**: índice do vértice no polígono: 0->2
- **`vertex`**: inteiro

**Retorna:** índice do vértice na malha

**Tipo do retorno:** integer

#### getMesh()

Devolve um mesh proxy

**Retorna:** mesh proxy

**Tipo do retorno:** `MeshProxy`

---

## KX_PythonComponent

Classe base: [`EXP_Value`](#exp_value)

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`SCA_PythonController`](#sca_pythoncontroller)

Um componente Python pode ser comparado a logic bricks Python com parâmetros. O componente Python é um script carregado pela UI; esse script define uma classe de componente herdando de `KX_PythonComponent`. Essa classe precisa ter um dicionário de propriedades, `args`, e duas funções padrão: `start` e `update`.

O script precisa ter extensão .py.

As propriedades do componente são carregadas do atributo `args` pela UI no carregamento. Quando o jogo começa, a função `start` é chamada recebendo um dicionário com o nome e o valor das propriedades. A função `update` é chamada a cada frame na etapa de lógica, antes dos logic bricks; o papel dela é tratar e processar tudo.

O exemplo de componente a seguir move e gira o objeto ao apertar as teclas W, A, S e D.

```python

import Range
from collections import OrderedDict

class ThirdPerson(Range.types.KX_PythonComponent):
    """Basic third person controls

    W: move forward
    A: turn left
    S: move backward
    D: turn right

    """

    #

    args = OrderedDict([
        ("Move Speed", 0.1),
        ("Turn Speed", 0.04)
    ])

    def start(self, args):
        self.move_speed = args['Move Speed']
        self.turn_speed = args['Turn Speed']

    def update(self):
        keyboard = Range.logic.keyboard.events

        move = 0
        rotate = 0

        if keyboard[Range.events.WKEY]:
            move += self.move_speed
        if keyboard[Range.events.SKEY]:
            move -= self.move_speed

        if keyboard[Range.events.AKEY]:
            rotate += self.turn_speed
        if keyboard[Range.events.DKEY]:
            rotate -= self.turn_speed

        self.object.applyMovement((0, move, 0), True)
        self.object.applyRotation((0, 0, rotate), True)
```

Como os componentes são carregados pela primeira vez fora do bge, `bge` é um módulo falso que só contém a classe `KX_PythonComponent`, para não importar todos os módulos do bge. Isso é mais seguro, mas dá problema no carregamento quando o usuário quer usar funções ou atributos dos módulos do bge além da classe `KX_PythonComponent`. A saída é não chamar essas funções no carregamento fora da Range. Para detectar isso, o módulo bge tem o atributo `__component__` quando é importado fora da Range.

O exemplo de componente a seguir adiciona um objeto "Cube" na inicialização e o move no eixo x a cada update. Ele mostra que dá para usar funções da cena e carregar o componente fora do bge definindo atributos globais numa condição no começo do script.

```python

import Range

if not hasattr(bge, "__component__"):
    global scene
    scene = Range.logic.getCurrentScene()

class Component(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        scene.addObject("Cube")

    def update(self):
        scene.objects["Cube"].worldPosition.x += 0.1
```

Os tipos de propriedade suportados são float, integer, boolean, string, set (para enumeração) e Vector 2D, 3D e 4D. O exemplo a seguir mostra todos esses tipos.

```python

from Range import *
from mathutils import *
from collections import OrderedDict

class Component(types.KX_PythonComponent):
     args = OrderedDict([
         ("Float", 58.6),
         ("Integer", 150),
         ("Boolean", True),
         ("String", "Cube"),
         ("Enum", {"Enum 1", "Enum 2", "Enum 3"}),
         ("Vector 2D", Vector((0.8, 0.7))),
         ("Vector 3D", Vector((0.4, 0.3, 0.1))),
         ("Vector 4D", Vector((0.5, 0.2, 0.9, 0.6)))
     ])

     def start(self, args):
         print(args)

     def update(self):
         pass
```

```python

# Componente que gira o objeto, com a velocidade definida no editor.
import Range
from collections import OrderedDict

class Spinner(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Speed", 0.02),
    ])

    def start(self, args):
        self.speed = args["Speed"]

    def update(self):
        self.object.applyRotation((0, 0, self.speed), True)
```

```python

# Componente que segue outro objeto, escolhido pelo nome no editor.
import Range
from collections import OrderedDict

class Follow(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Target", "Player"),
        ("Speed", 0.05),
    ])

    def start(self, args):
        self.target = self.object.scene.objects[args["Target"]]
        self.speed = args["Speed"]

    def update(self):
        distance, direction, local = self.object.getVectTo(self.target)
        self.object.worldPosition += direction * self.speed

    def dispose(self):
        print("Component removed")
```

#### object

O objeto dono do componente.

**Tipo:** `KX_GameObject`

#### args

Dicionário das propriedades do componente; as chaves são strings e o valor pode ser: float, integer, Vector(2D/3D/4D), set, string.

**Tipo:** dict

#### start(args)

Inicializa o componente.

- **`args`**: O dicionário com o nome e o valor das propriedades.
  - tipo: dict

> **Caution:**
Esta função precisa ser herdada na classe do componente Python.

#### update()

Processa a lógica do componente.

> **Caution:**
Esta função precisa ser herdada na classe do componente Python.

#### dispose()

Função chamada quando o componente é destruído.

> **Caution:**
Esta função precisa ser herdada na classe do componente Python.

---

## KX_PythonJoystick

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`SCA_JoystickSensor`](#sca_joysticksensor), [`Range.events`](#rangeevents), [`KX_InputSystem`](#kx_inputsystem)

Uma interface Python para um joystick.

```python
# Anda com o analógico esquerdo e pula com um botão.
import Range

joystick = Range.logic.joysticks[0]

if joystick is not None:
    x, y = joystick.axisValues[0], joystick.axisValues[1]
    print(x, y)

    if 0 in joystick.activeButtons:
        print("Jump")
```

```python
# Vibra por meio segundo.
import Range

joystick = Range.logic.joysticks[0]

if joystick is not None and joystick.hasVibration:
    joystick.strengthLeft = 0.8
    joystick.strengthRight = 0.8
    joystick.duration = 500
    joystick.startVibration()
```

#### name

O nome dado ao joystick pelo sistema operacional (somente leitura)

**Tipo:** string

#### activeButtons

Uma lista dos valores dos botões ativos (somente leitura)

**Tipo:** list

#### axisValues

O estado dos eixos do joystick, como uma lista de `numAxis` valores (somente leitura).

**Tipo:** list of ints.

Cada um dá o valor de um eixo entre -1.0 e 1.0, conforme o quanto o eixo está empurrado; 0 quando solto. Os 2 primeiros valores são usados pela maioria dos joysticks e gamepads para o controle de direção. O 3º e o 4º só existem em alguns joysticks e podem ser usados para controles quaisquer.

* esquerda:[-1.0, 0.0, ...]
* direita:[1.0, 0.0, ...]
* up:[0.0, -1.0, ...]
* baixo:[0.0, 1.0, ...]

#### hatValues (Deprecated. Use :data:`activeButtons` instead)

O estado dos hats do joystick, como uma lista de `numHats` valores (somente leitura).

**Tipo:** list of ints

Cada um dá a direção do hat de 1 a 12; 0 quando inativo.

As direções do hat são estas...

* 0:Nenhuma
* 1:Up
* 2:Direita
* 4:Baixo
* 8:Esquerda
* 3:Cima - Direita
* 6:Baixo - Direita
* 12:Baixo - Esquerda
* 9:Cima - Esquerda

#### numAxis

O número de eixos do joystick neste índice (somente leitura).

**Tipo:** integer

#### numButtons

O número de botões do joystick neste índice (somente leitura).

**Tipo:** integer

#### numHats (Deprecated. Use :data:`numButtons` instead)

O número de hats do joystick neste índice (somente leitura).

**Tipo:** integer

#### startVibration()

Começa a vibração.

**Retorna:** None

#### stopVibration()

Para a vibração.

**Retorna:** None

#### strengthLeft

Força do motor de baixa frequência do joystick (em geral fica à esquerda).

**Tipo:** float (0.0 to 1.0)

#### strengthRight

Força do motor de alta frequência do joystick (em geral fica à direita).

**Tipo:** float (0.0 to 1.0)

#### duration

Duração da vibração em milissegundos.

**Tipo:** integer (0 to infinite)

#### isVibrating

Verifica o status da vibração do joystick

**Tipo:** bool (true vibrating and false stopped)

#### hasVibration

Verifica se o joystick suporta vibração

**Tipo:** bool (true supported and false not supported)

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### stopVibration()

 `método`

Para a vibração do controle.

#### duration

 `atributo`

Duração da vibração, em milissegundos.

#### hasVibration

 `atributo · só leitura`

`True` se o controle suporta vibração.

#### inputs

 `atributo · só leitura`

Dicionário `{botão: SCA_InputEvent}` com o estado de cada botão do controle.

#### isVibrating

 `atributo · só leitura`

`True` enquanto o controle está vibrando.

#### strengthLeft

 `atributo`

Força do motor de vibração esquerdo (0 a 1).

#### strengthRight

 `atributo`

Força do motor de vibração direito (0 a 1).

---

## KX_PythonKeyboard

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`Range.events`](#rangeevents), [`SCA_InputEvent`](#sca_inputevent), [`KX_PythonMouse`](#kx_pythonmouse)

O teclado atual.

```python
# Confere as teclas pelo estado.
import Range

keyboard = Range.logic.keyboard

if keyboard.inputs[Range.events.ESCKEY].activated:
    print("Pause")
```

```python
# Lê o texto digitado e usa a área de transferência.
import Range

keyboard = Range.logic.keyboard

print(keyboard.text)
keyboard.setClipboard("Saved code: 1234")
print(keyboard.getClipboard())
```

#### inputs

Dicionário com a entrada de cada tecla do teclado (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~events~~

Dicionário com o estado de cada evento ou tecla do teclado (somente leitura).

> **Obsoleto use :data:`inputs`:**

**Tipo:** dictionary {`keycode`:`status`, ...}

#### activeInputs

Dicionário com a entrada só das teclas ativas (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~active_events~~

Dicionário com o estado só dos eventos ou teclas ativas (somente leitura).

> **Obsoleto use :data:`activeInputs`:**

**Tipo:** dictionary {`keycode`:`status`, ...}

#### text

O texto unicode digitado no último frame.

**Tipo:** string

#### getClipboard()

Lê o texto da área de transferência.

**Tipo do retorno:** string

#### setClipboard(text)

Define o texto da área de transferência.

- **`text`**: O novo texto da área de transferência
  - tipo: string

---

## KX_PythonMotion

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Sensores de movimento do dispositivo (celular ou tablet), disponíveis como `Range.logic.motion`.

Os valores vêm do navegador no runtime Web (`DeviceMotionEvent` e `DeviceOrientationEvent`), inclusive no app Android, que roda o runtime Web dentro de uma WebView. Nas outras plataformas ainda não há fonte de sensores: `available` é `False`, os vetores são zero e `tilt` é `(0.0, 0.0)`, para que o mesmo script rode em todo lugar.

Os vetores usam os eixos da tela como ela está sendo mostrada, em retrato ou paisagem: x para a direita, y para o topo da tela e z para fora da tela, na direção do jogador.

Um objeto controlado pela inclinação:

```python

from Range import logic, events

def main(cont):
    own = cont.owner
    if logic.mouse.inputs[events.LEFTMOUSE].activated:  # um toque na tela
        logic.motion.calibrate()
    x, y = logic.motion.tilt
    own.applyForce((x * 20.0, y * 20.0, 0.0))
```

#### available

`True` enquanto os sensores estão mandando dados. Vira `False` quando nenhuma leitura chegou no último segundo (sem sensor, navegador de desktop, página em segundo plano) (somente leitura).

**Tipo:** boolean

#### gyroscope

Velocidade de rotação em torno de cada eixo da tela, em radianos por segundo (somente leitura).

**Tipo:** `mathutils.Vector`

#### accelerometer

Aceleração incluindo a gravidade, em m/s². Com o dispositivo parado, deitado de face para cima, fica perto de `(0, 0, 9.8)` (somente leitura).

**Tipo:** `mathutils.Vector`

#### gravity

Só a gravidade, em m/s², apontando para cima como em `accelerometer`. Quando o dispositivo não informa a aceleração sem gravidade, ela é estimada a partir de `accelerometer` com um filtro passa-baixa (somente leitura).

**Tipo:** `mathutils.Vector`

#### orientation

Ângulos de orientação do dispositivo `(alpha, beta, gamma)` em graus, exatamente como o navegador entrega. Seguem os eixos do dispositivo, não os da tela (somente leitura).

**Tipo:** `mathutils.Vector`

#### tilt

Quanto o dispositivo está inclinado em relação à posição neutra, de -1.0 a 1.0 em cada eixo: a direção da tela para onde uma bola rolaria. `x` é positivo quando a borda direita da tela desce, `y` quando a borda de cima desce. A posição neutra é o dispositivo deitado, até `calibrate` ser chamado (somente leitura).

**Tipo:** tuple (float, float)

#### calibrate()

Usa a posição atual como neutra para `tilt`, para o jogador segurar o dispositivo do jeito que preferir.

**Retorna:** `True` se havia uma leitura do sensor para calibrar, `False` se não.

**Tipo do retorno:** boolean

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### recenter()

*(novo na Anastacio)* `método`

Usa a direção atual da cabeça (VR) como "frente". `False` se o sensor não está pronto.

**Retorna:** `bool`

#### headOrientation

*(novo na Anastacio)* `atributo · só leitura`

Orientação da cabeça (matriz 3×3), já recentralizada.

#### recenterTime

*(novo na Anastacio)* `atributo`

Tempo, em segundos, para recentralizar sozinho quando a cabeça fica parada (0 desliga).

#### smoothing

*(novo na Anastacio)* `atributo`

Suavização do movimento da cabeça (0 a 5).

---

## KX_PythonMouse

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`Range.events`](#rangeevents), [`SCA_InputEvent`](#sca_inputevent), [`KX_PythonKeyboard`](#kx_pythonkeyboard)

O mouse atual.

> **Caution:**
A normalização do mouse usa a coordenada máxima da largura e da altura, ou seja, `Range.render.getWindowWidth() - 1` ou `Range.render.getWindowHeight() - 1`.

Um script que põe o mouse no centro fica parecido com este exemplo:

```python

import Range

w, h = Range.render.getWindowWidth() - 1, Range.render.getWindowHeight() - 1
center_x, center_y = (w // 2) / w, (h // 2) / h

Range.logic.mouse.position = center_x, center_y
```

Repare no uso da divisão inteira para arredondar uma coordenada.

#### inputs

Dicionário com a entrada de cada evento do mouse (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~events~~

Dicionário com o estado de cada evento do mouse (somente leitura).

> **Obsoleto use :data:`inputs`:**

**Tipo:** dictionary {`keycode`:`status`, ...}

#### activeInputs

Dicionário com a entrada só dos eventos ativos do mouse (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~active_events~~

Dicionário com o estado só dos eventos ativos do mouse (somente leitura).

> **Obsoleto use :data:`activeInputs`:**

**Tipo:** dictionary {`keycode`:`status`, ...}

#### position

A posição x e y normalizada do cursor do mouse.

**Tipo:** tuple (x, y)

#### visible

A visibilidade do cursor do mouse.

**Tipo:** boolean

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### reCenter()

 `método`

Volta o cursor para o centro da janela (útil em câmera em primeira pessoa).

#### deltaPosition

 `atributo · só leitura`

Quanto o mouse se moveu desde o último frame, `(x, y)`.

---

## KX_RadarSensor

Classe base: [`KX_NearSensor`](#kx_nearsensor)

O sensor radar é um sensor near com um objeto sensor em forma de cone.

```python
# Detecta inimigos no cone definido no editor. Distância e ângulo são só de leitura.
import Range

sensor = Range.logic.getCurrentController().sensors["Radar"]

print(sensor.distance, sensor.angle)

if sensor.positive:
    print(sensor.hitObject.name)
```

#### coneOrigin

A origem do cone usado no teste. A origem fica no meio do cone (somente leitura).

**Tipo:** `mathutils.Vector`

#### coneTarget

O centro da face de baixo do cone usado no teste (somente leitura).

**Tipo:** `mathutils.Vector`

#### distance

A altura do cone usado no teste.

**Tipo:** float

#### angle

O ângulo do cone (em graus) usado no teste.

**Tipo:** float

#### axis

O eixo em que o cone do radar é lançado.

**Tipo:** integer from 0 to 5

KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z, KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z

---

## KX_RaySensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Um sensor Ray detecta o primeiro objeto numa direção.

```python
# Mostra o que está à frente do objeto.
import Range

sensor = Range.logic.getCurrentController().sensors["Ray"]

sensor.range = 10.0
sensor.axis = Range.logic.KX_RAY_AXIS_POS_Y

if sensor.positive:
    print(sensor.hitObject.name, sensor.hitPosition, sensor.hitNormal)
```

#### propName

A propriedade que o raio procura.

**Tipo:** string

#### range

A distância do raio.

**Tipo:** float

#### useMaterial

Se procura um material ou não (false = propriedade).

**Tipo:** boolean

#### useXRay

Se usa XRay ou não.

**Tipo:** boolean

#### mask

A máscara de colisão (16 layers mapeadas num inteiro de 16 bits) combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só os objetos em que `collisionGroup & mask` é verdadeiro podem ser atingidos.

**Tipo:** bitfield

#### hitObject

O game object atingido pelo raio (somente leitura).

**Tipo:** `KX_GameObject`

#### hitPosition

A posição (em coordenadas do mundo) em que o objeto foi atingido pelo raio (somente leitura).

**Tipo:** `mathutils.Vector`

#### hitNormal

A normal (em coordenadas do mundo) do objeto no ponto em que foi atingido pelo raio (somente leitura).

**Tipo:** `mathutils.Vector`

#### hitMaterial

O material do objeto na face atingida pelo raio (somente leitura).

**Tipo:** string

#### rayDirection

A direção do raio (em coordenadas do mundo) (somente leitura).

**Tipo:** `mathutils.Vector`

#### axis

O eixo para onde o raio aponta.

**Tipo:** integer from 0 to 5

* KX_RAY_AXIS_POS_X
* KX_RAY_AXIS_POS_Y
* KX_RAY_AXIS_POS_Z
* KX_RAY_AXIS_NEG_X
* KX_RAY_AXIS_NEG_Y
* KX_RAY_AXIS_NEG_Z

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### gazeAngle

*(novo na Anastacio)* `atributo`

Tolerância do olhar (0 a 1): quanto o alvo pode estar fora do centro do raio.

#### gazeProgress

*(novo na Anastacio)* `atributo · só leitura`

Progresso do olhar fixo, de 0 a 1. Chega a 1 depois de `gazeTime` segundos olhando o alvo.

#### gazeTime

*(novo na Anastacio)* `atributo`

Tempo, em segundos, olhando o alvo para o sensor disparar (0 a 30).

---

## KX_ReplaceMeshActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Edit Object, no modo Replace Mesh.

> **Caution:**
Atuadores Replace Mesh são ignorados se, no início do jogo, a malha com o nome indicado não existir.

Isto gera um aviso no console

```text

Error: GameObject 'Name' ReplaceMeshActuator 'ActuatorName' without object
```

```python

# Nível de detalhe
# Troca a malha de um game object conforme a profundidade dele na vista da câmera.
# +----------+     +-----------+     +-------------------------------------+
# | Always   +-----+ Python    +-----+ Edit Object (Replace Mesh) LOD.Mesh |
# +----------+     +-----------+     +-------------------------------------+
from Range import logic

# Liste aqui as malhas de detalhe
# Malha (nome, perto, longe)
# As malhas se sobrepõem para não "pipocar" na borda da distância.
meshes = ((".Hi", 0.0, -20.0),
      (".Med", -15.0, -50.0),
      (".Lo", -40.0, -100.0)
    )

cont = logic.getCurrentController()
object = cont.owner
actuator = cont.actuators["LOD." + obj.name]
camera = logic.getCurrentScene().active_camera

def Depth(pos, plane):
  return pos[0]*plane[0] + pos[1]*plane[1] + pos[2]*plane[2] + plane[3]

# A profundidade é negativa e diminui conforme se afasta da câmera
depth = Depth(object.position, camera.world_to_camera[2])

newmesh = None
curmesh = None
# Acha a malha de menor detalhe para a profundidade
for mesh in meshes:
  if depth < mesh[1] and depth > mesh[2]:
    newmesh = mesh
  if "ME" + object.name + mesh[0] == actuator.getMesh():
      curmesh = mesh

if newmesh != None and "ME" + object.name + newmesh[0] != actuator.mesh:
  # A malha é diferente - troca.
  # Confere se a malha atual não serve melhor.
  if curmesh == None or curmesh[1] < depth or curmesh[2] > depth:
    actuator.mesh = object.name + newmesh[0]
    cont.activate(actuator)
```

#### mesh

`MeshProxy` ou o nome da malha que vai substituir a atual.

Use None para desligar o atuador.

**Tipo:** `MeshProxy` or None if no mesh is set

#### useDisplayMesh

com true, a malha exibida é substituída.

**Tipo:** boolean

#### usePhysicsMesh

com true, a malha de física é substituída.

**Tipo:** boolean

#### instantReplaceMesh()

Substitui a malha na hora, sem atraso.

---

## KX_Scene

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`KX_Camera`](#kx_camera), [`KX_WorldInfo`](#kx_worldinfo), [`KX_2DFilterManager`](#kx_2dfiltermanager), [`Range.logic`](#rangelogic)

Uma cena ativa, que dá acesso a objetos, câmeras, luzes e atributos da cena.

O culling de atividade deveria desligar os logic bricks quando o dono deles fica longe demais da câmera ativa. Ele veio de um código antigo escondido no KX_Scene, e ninguém sabe ao certo o que faz.

```python

from Range import logic

# pega a cena
scene = logic.getCurrentScene()

# mostra todos os objetos da cena
for object in scene.objects:
   print(object.name)

# pega o objeto chamado 'Cube'
object = scene.objects["Cube"]

# pega o primeiro objeto da cena.
object = scene.objects[0]
```

```python

# Pega a profundidade de um objeto na visão da câmera.
from Range import logic

object = logic.getCurrentController().owner
cam = logic.getCurrentScene().active_camera

# A profundidade é negativa e diminui conforme se afasta da câmera
depth = object.position[0]*cam.world_to_camera[2][0] + object.position[1]*cam.world_to_camera[2][1] + object.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]
```

@bug: Por enquanto todos os atributos são somente leitura.

```python

# Adiciona uma bala na arma. Ela some depois de 120 frames.
import Range

scene = Range.logic.getCurrentScene()
gun = Range.logic.getCurrentController().owner

bullet = scene.addObject("Bullet", gun, 120)
bullet.worldLinearVelocity = gun.getAxisVect((0, 30, 0))
```

```python

# Troca para outra câmera.
import Range

scene = Range.logic.getCurrentScene()
scene.active_camera = scene.cameras["CameraBack"]
```

```python

# Pausa ou retoma outra cena, como a fase atrás de um menu de pausa.
import Range

level = Range.logic.getSceneList()["Level"]

if level.suspended:
    level.resume()
else:
    level.suspend()
```

```python

# Procura objetos pela propriedade e vai para a próxima fase.
import Range

scene = Range.logic.getCurrentScene()
coins = [obj for obj in scene.objects if "coin" in obj]

if not coins:
    scene.replace("Level2")
```

```python

# Roda uma função logo antes de cada frame ser desenhado.
import Range

def before_draw():
    print("Drawing")

scene = Range.logic.getCurrentScene()
scene.pre_draw.append(before_draw)
```

#### name

O nome da cena (somente leitura).

**Tipo:** string

#### objects

Lista dos objetos da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

#### objectsInactive

Lista dos objetos nas camadas de fundo, usados pelo atuador Add Object (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

#### lights

Lista das luzes da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_LightObject`

#### cameras

Lista das câmeras da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_Camera`

#### texts

Lista dos textos da cena (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_FontObject`

#### active_camera

A câmera ativa atual.

**Tipo:** `KX_Camera`

> **Note:**
Pode ser definida direto pelo Python, sem precisar do `KX_SceneActuator`.

#### overrideCullingCamera

Câmera usada no lugar da padrão para o culling da cena. Se for None, o culling usa a câmera que está renderizando.

**Tipo:** `KX_Camera` or None

#### world

O mundo ativo atual (somente leitura).

**Tipo:** `KX_WorldInfo`

#### filterManager

O gerenciador de filtros 2D da cena (somente leitura).

**Tipo:** `KX_2DFilterManager`

#### suspended

True se a cena estiver suspensa (somente leitura).

**Tipo:** boolean

#### activityCulling

True se a cena permite o culling de atividade dos objetos.

**Tipo:** boolean

#### dbvt_culling

True quando a árvore de volumes dinâmica (DBVT) está ligada (somente leitura).

**Tipo:** boolean

#### pre_draw

Lista de funções chamadas antes da etapa de render. Elas podem receber como argumento a câmera que está renderizando.

**Tipo:** list

#### post_draw

Lista de funções chamadas depois da etapa de render.

**Tipo:** list

#### pre_draw_setup

Lista de funções chamadas antes da preparação do desenho, ou seja, antes de calcular as matrizes de visão e projeção. Elas podem receber como argumento a câmera que está renderizando; essa câmera pode ser temporária no render estéreo.

**Tipo:** list

#### onRemove

Lista de funções chamadas quando a cena é destruída.

```python

@scene.onRemove.append
def callback(scene):
      print('exiting %s...' % scene.name)
```

**Tipo:** list

#### gravity

A gravidade da cena nos eixos x, y e z do mundo.

**Tipo:** Vector((gx, gy, gz))

#### maxDebris

Quantos fragmentos de objetos quebrados ficam vivos na cena; acima disso, os mais antigos são removidos. Começa com o valor de Scene > Game Physics > Max Debris. 0 significa sem limite. Diminuir o valor remove os pedaços excedentes na hora.

**Tipo:** integer in [0, 100000]

#### explode(position, radius=5.0, force=20.0, upBias=0.3, occlusion=True, mask=0xFFFF, ignore=None)

Impulso radial nos objetos dinâmicos em volta de position, que cai a zero em radius (`force * (1 - distance / radius)`). Objetos destrutíveis atingidos acima do seu `KX_GameObject.breakImpulse` quebram e os pedaços são empurrados, dividindo o impulso pela massa. Objetos explosivos atingidos acima do seu Impact Impulse (com Chain Reaction ligado) detonam no frame seguinte.

- **`position`**: O centro da explosão.
  - tipo: 3D Vector
- **`radius`**: A distância que a explosão alcança.
  - tipo: float
- **`force`**: O impulso no centro.
  - tipo: float
- **`upBias`**: Quanto o empurrão é inclinado para cima; 0.0 empurra reto para longe do centro.
  - tipo: float
- **`occlusion`**: Se True, a geometria estática entre o centro e um objeto o protege.
  - tipo: boolean
- **`mask`**: Os grupos de colisão atingidos.
  - tipo: bitfield
- **`ignore`**: Um objeto ou uma lista de objetos que ficam de fora.
  - tipo: `KX_GameObject` or list

**Retorna:** Os objetos atingidos (sem contar os pedaços novos).

**Tipo do retorno:** list of `KX_GameObject`

#### addObject(object, reference, time=0.0)

Adiciona um objeto à cena, como o atuador Add Object faria.

- **`object`**: O objeto a adicionar (ou o nome dele).
  - tipo: `KX_GameObject` or string
- **`reference`**: O objeto (ou o nome dele) de onde copiar posição, orientação e escala (opcional). Se o objeto adicionado for uma luz e não houver referência, a camada da luz será a camada ativa da cena do Blender.
  - tipo: `KX_GameObject` or string
- **`time`**: O tempo de vida do objeto adicionado, em frames (considera um frame como 1/50 de segundo). 0.0 significa que o objeto dura para sempre (opcional).
  - tipo: float

**Retorna:** O objeto recém-adicionado.

**Tipo do retorno:** `KX_GameObject`

#### end()

Remove a cena do jogo.

#### restart()

Reinicia a cena.

#### replace(scene)

Troca esta cena por outra.

- **`scene`**: O nome da cena que vai substituir esta.
  - tipo: string

**Retorna:** True se a cena existe e foi agendada para entrar, False caso contrário.

**Tipo do retorno:** boolean

#### suspend()

Suspende esta cena.

#### resume()

Retoma esta cena.

#### get(key, default=None)

Devolve o valor da chave, ou o valor padrão se a chave não existir.

**Retorna:** O valor da chave ou o padrão.

#### drawObstacleSimulation()

Desenha a visualização de depuração da simulação de obstáculos.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### convertObject(name, children=True)

 `método`

Cria agora um objeto que ficou de fora no carregamento pela opção **Convert** (e os filhos não convertidos). Vai para `objects` se estiver numa camada ativa, senão para `objectsInactive` (pronto para `addObject`). Um objeto já convertido é retornado como está.

**Retorna:** `KX_GameObject`

#### getQualityPreset()

*(sem documentação)* `método`

#### play_cutscene(sequence=0)

 `método`

Começa a Cutscene nativa da cena. Retorna `True` se deu certo.

**Retorna:** `bool`

#### play_take(name)

 `método`

Toca um Take do Rec Play em todos os atores. `True` se o Take existe.

**Retorna:** `bool`

#### release_cutscene_trigger(name)

 `método`

Libera um evento **Wait Trigger** da Cutscene esperando por `name`. `True` se ela estava esperando agora; senão o gatilho fica guardado para o próximo Wait Trigger com esse nome. Uma mensagem com assunto `name` faz o mesmo.

**Retorna:** `bool`

#### restart_cutscene()

 `método`

Reinicia a Cutscene ativa e remove os objetos que ela criou.

#### setQualityPreset()

*(sem documentação)* `método`

#### skip_cutscene()

 `método`

Pula para o fim da Cutscene em andamento: falas, esperas, caminhos de câmera e fades são descartados; os outros eventos que faltam rodam (volta da câmera, destravar, troca de cena). Retorna `False` se nada estava tocando. Tab ou o botão Start do controle fazem o mesmo, a menos que `Range.logic.globalDict["cutscene_skip"]` seja `False`.

#### stop_cutscene()

 `método`

Para a Cutscene e remove os objetos que ela criou.

#### speakers

 `atributo · só leitura`

Lista dos objetos de som (`KX_Speaker`) da cena.

#### takes

*(novo na Anastacio)* `atributo · só leitura`

Nomes dos Takes do Rec Play da cena (só leitura).

#### thread_logic_1

 `atributo`

Lista de funções chamadas na thread de lógica paralela, a cada frame. Mesmo uso de `pre_draw`.

#### unconvertedObjects

*(novo na Anastacio)* `atributo · só leitura`

Nomes dos objetos que ainda podem ser criados com `convertObject()`.

#### visible

*(novo na Anastacio)* `atributo`

#### worldSun

 `atributo · só leitura`

Luz Sun ligada ao World (posição do sol do céu), ou `None`.

---

## KX_SceneActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Logic brick do atuador Scene.

> **Caution:**
Atuadores de cena que usam um nome de cena são ignorados se, no início do jogo, a cena com esse nome não existir ou estiver vazia

Isto gera um aviso no console:

```text

Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene
```

#### scene

o nome da cena para trocar/sobrepor/pôr por baixo/remover/suspender/retomar.

**Tipo:** string

#### camera

a câmera para a qual trocar.

**Tipo:** `KX_Camera` on read, string or `KX_Camera` on write

> **Note:**
Ao definir o atributo, dá para usar um `KX_Camera` ou o nome da câmera.

#### useRestart

Use True para reiniciar a cena.

**Tipo:** boolean

#### mode

O modo do atuador.

**Tipo:** integer from 0 to 5.

---

## KX_SoundActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

> **Veja também:**
[`KX_Speaker`](#kx_speaker)

Atuador Sound.

`startSound`, `pauseSound` e `stopSound` não exigem que o atuador esteja ativo: agem na hora, desde que o atuador tenha sido ativado pelo menos uma vez.

```python
# Toca um som com tom variado.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Sound"]

act.pitch = 0.9 + Range.logic.getRandomFloat() * 0.2
act.volume = 0.8
act.startSound()
```

```python
# Pausa e para.
import Range

act = Range.logic.getCurrentController().actuators["Sound"]

act.pauseSound()
act.stopSound()
```

#### volume

O volume (ganho) do som.

**Tipo:** float

#### time

A posição atual no stream de áudio (em segundos).

**Tipo:** float

#### pitch

O pitch do som.

**Tipo:** float

#### mode

O modo de operação do atuador. Pode ser uma `destas constantes`

**Tipo:** integer

#### sound

O som que o atuador deve tocar.

**Tipo:** Audaspace factory

#### is3D

Se o atuador usa som 3D ou não (somente leitura)

**Tipo:** boolean

#### volume_maximum

O ganho máximo do som, não importa quão perto ele esteja.

**Tipo:** float

#### volume_minimum

O ganho mínimo do som, não importa quão longe ele esteja.

**Tipo:** float

#### distance_reference

A distância em que o som tem ganho 1.0.

**Tipo:** float

#### distance_maximum

A distância máxima em que dá para ouvir o som.

**Tipo:** float

#### attenuation

O fator de influência no volume conforme a distância.

**Tipo:** float

#### cone_angle_inner

O ângulo do cone interno.

**Tipo:** float

#### cone_angle_outer

O ângulo do cone externo.

**Tipo:** float

#### cone_volume_outer

O ganho fora do cone externo (o ganho dentro do cone externo é interpolado entre este valor e o ganho normal do cone interno).

**Tipo:** float

#### startSound()

Começa o som.

**Retorna:** None

#### pauseSound()

Pausa o som.

**Retorna:** None

#### stopSound()

Para o som.

**Retorna:** None

---

## KX_Speaker

> **Veja também:**
[`KX_SoundActuator`](#kx_soundactuator), [`KX_Scene`](#kx_scene)

Classe `Range.types.KX_Speaker`.

```python
# Controla um speaker da cena.
import Range

scene = Range.logic.getCurrentScene()

for speaker in scene.speakers:
    speaker.volume = 0.5
    speaker.pitch = 1.0
    speaker.Play()
```

```python
# Pausa, recomeça ou para.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.Pause()
speaker.Restart()
speaker.Stop()
```

```python
# Som que abaixa com a distância.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.distance_reference = 2.0
speaker.distance_maximum = 40.0
speaker.attenuation = 1.0
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### GetActiveEffect()

 `método`

Efeito de som ativo: 0 nenhum, 1 reverb.

**Retorna:** `int`

#### GetActiveEffectFilter()

 `método`

Filtro ativo: 0 nenhum, 1 passa-baixa, 2 passa-alta, 3 passa-banda.

**Retorna:** `int`

#### Pause()

 `método`

Pausa o som.

#### Play()

 `método`

Toca o som.

#### RemoveEffect()

 `método`

Remove o efeito de som.

#### Restart()

 `método`

Toca o som desde o começo.

#### SetEffect(effectType, filterType=0)

 `método`

Aplica um efeito: `effectType` 1 = reverb; `filterType` 0 nenhum, 1 passa-baixa, 2 passa-alta, 3 passa-banda. Depois disso as áreas de reverb deixam este Speaker em paz.

#### SetSound(sound, cache=False)

 `método`

Troca o som (um `aud.Sound`). Com `cache=True`, guarda o som decodificado na memória.

#### Stop()

 `método`

Para o som.

#### attenuation

 `atributo`

Quanto o volume cai com a distância (som 3D).

#### catkey

 `atributo`

Chave da categoria de som no gerenciador de reprodução, ou `None`.

#### cone_angle_inner

 `atributo`

Ângulo, em graus, do cone em que o som toca no volume cheio.

#### cone_angle_outer

 `atributo`

Ângulo, em graus, do cone fora do qual o volume é `cone_volume_outer`.

#### cone_volume_outer

 `atributo`

Volume fora do cone externo.

#### distance_maximum

 `atributo`

Distância a partir da qual o volume para de cair.

#### distance_reference

 `atributo`

Distância em que o som toca no volume normal.

#### filter_gain

 `atributo`

Ganho geral do filtro.

#### filter_gainhf

 `atributo`

Ganho das frequências altas no filtro.

#### filter_gainlf

 `atributo`

Ganho das frequências baixas no filtro.

#### is3D

 `atributo · só leitura`

`True` se o som é posicional (3D).

#### mode

 `atributo`

Modo de reprodução: 1 toca até o fim, 2 repete, 3 repete indo e voltando.

#### pitch

 `atributo`

Tom (velocidade) do som. 1.0 é normal.

#### playbackManager

 `atributo`

Gerenciador de reprodução (`aud.PlaybackManager`) usado pelo Speaker, ou `None`.

#### reverb_air_absorption_gain_hf

 `atributo`

Reverb: absorção das altas frequências pelo ar.

#### reverb_decay_hf_ratio

 `atributo`

Reverb: quanto as altas frequências somem mais rápido que as baixas.

#### reverb_decay_limit_hf

 `atributo`

Reverb: limita o decaimento das altas frequências.

#### reverb_decay_time

 `atributo`

Reverb: tempo, em segundos, que o eco leva para sumir.

#### reverb_density

 `atributo`

Reverb: densidade dos ecos.

#### reverb_diffusion

 `atributo`

Reverb: espalhamento dos ecos.

#### reverb_gain

 `atributo`

Reverb: volume geral do efeito.

#### reverb_gain_hf

 `atributo`

Reverb: volume das altas frequências.

#### reverb_late_reverb_delay

 `atributo`

Reverb: atraso da cauda do eco.

#### reverb_late_reverb_gain

 `atributo`

Reverb: volume da cauda do eco.

#### reverb_reflections_delay

 `atributo`

Reverb: atraso das primeiras reflexões.

#### reverb_reflections_gain

 `atributo`

Reverb: volume das primeiras reflexões.

#### reverb_room_rolloff_factor

 `atributo`

Reverb: quanto o efeito cai com a distância.

#### sound

 `atributo`

Som atual (`aud.Sound`), ou `None`.

#### time

 `atributo`

Posição atual do som, em segundos. Pode ser mudada para pular.

#### volume

 `atributo`

Volume do som.

#### volume_maximum

 `atributo`

Volume máximo, mesmo de perto.

#### volume_minimum

 `atributo`

Volume mínimo, mesmo de longe.

---

## KX_StateActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

O atuador State muda a máscara de estado do objeto pai.

```python
# Liga o estado 2 do objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["State"]

act.operation = Range.logic.KX_STATE_OP_SET
act.mask = Range.logic.KX_STATE2
cont.activate(act)
```

#### operation

Tipo de operação de bits aplicada à máscara de estado do objeto.

Você pode usar uma `destas constantes`

**Tipo:** integer

#### mask

Valor que define os bits que serão modificados pela operação.

Os bits que valem 1 na máscara são atualizados no estado do objeto.

Os bits que valem 0 ficam sem mudança, exceto na operação Copy, que copia a máscara para o estado do objeto.

**Tipo:** integer

---

## KX_SteeringActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

> **Veja também:**
[`KX_NavMeshObject`](#kx_navmeshobject)

Atuador Steering para navegação.

```python
# Segue o jogador usando uma malha de navegação.
import Range

cont = Range.logic.getCurrentController()
scene = Range.logic.getCurrentScene()
act = cont.actuators["Steering"]

act.behavior = Range.logic.KX_STEERING_PATHFOLLOWING
act.target = scene.objects["Player"]
act.navmesh = scene.objects["Navmesh"]
act.velocity = 3.0
act.distance = 1.0
cont.activate(act)
```

#### behavior

O comportamento de steering a usar.

**Tipo:** one of `these constants`

#### velocity

Módulo da velocidade

**Tipo:** float

#### acceleration

Aceleração máxima

**Tipo:** float

#### turnspeed

Velocidade máxima de giro

**Tipo:** float

#### distance

Distância de relaxamento

**Tipo:** float

#### target

Objeto alvo

**Tipo:** `KX_GameObject`

#### navmesh

Navigation mesh

**Tipo:** `KX_GameObject`

#### selfterminated

Termina quando o alvo é alcançado

**Tipo:** boolean

#### enableVisualization

Liga a visualização de depuração

**Tipo:** boolean

#### pathUpdatePeriod

Período de atualização do caminho

**Tipo:** int

#### path

Lista de pontos do caminho.

**Tipo:** list of `mathutils.Vector`

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### facingMode

 `atributo`

Para onde o objeto vira ao andar: 0 não vira, 1 a 3 = eixo +X, +Y, +Z, 4 a 6 = -X, -Y, -Z.

#### lockZVelocity

 `atributo`

Não mexe na velocidade vertical (Z) do objeto.

#### steeringVec

 `atributo · só leitura`

Vetor de direção calculado pelo atuador neste frame.

---

## KX_TextureRenderer

Classe base: [`EXP_Value`](#exp_value)

API Python para objetos que fazem um render guardado numa textura.

```python
# Atualiza um reflexo só a cada alguns quadros para poupar tempo.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.autoUpdate = False
own["frames"] = own.get("frames", 0) + 1

if own["frames"] % 10 == 0:
    renderer.update()
```

```python
# Usa outro ponto de vista e uma distância menor.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.viewpointObject = Range.logic.getCurrentScene().objects["Probe"]
renderer.clipEnd = 50.0
```

#### autoUpdate

Define se o texture renderer é atualizado automaticamente a cada frame.

**Tipo:** boolean

#### viewpointObject

O objeto de onde o texture renderer vai renderizar a cena.

**Tipo:** `KX_GameObject`

#### enabled

Liga o render da cena pelo texture renderer.

**Tipo:** boolean

#### ignoreLayers

As layers a ignorar no render.

**Tipo:** bitfield

#### clipStart

O plano near da matriz de projeção, usado no culling.

**Tipo:** float

#### clipEnd

O plano far da matriz de projeção, usado no culling.

**Tipo:** float

#### lodDistanceFactor

Fator que multiplica a distância até a câmera para ajustar os níveis de detalhe. Um valor < 1.0 faz a distância usada para calcular os níveis de detalhe diminuir.

**Tipo:** float

#### update()

Pede para atualizar este texture renderer na etapa de render. Só tem efeito quando `autoUpdate` está desligado.

---

## KX_TrackToActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Edit Object no modo Track To.

> **Caution:**
Atuadores Track To são ignorados se, no início do jogo, o objeto a seguir for inválido.

Isto gera um aviso no console:

```text

GameObject 'Name' no object in EditObjectActuator 'ActuatorName'
```

#### object

o objeto que este atuador segue.

**Tipo:** `KX_GameObject` or None

#### time

o tempo, em frames, de atraso do movimento de seguir.

**Tipo:** integer

#### use3D

o movimento de seguir usa 3D.

**Tipo:** boolean

#### upAxis

O eixo que aponta para cima.

**Tipo:** integer from 0 to 2

* KX_TRACK_UPAXIS_POS_X
* KX_TRACK_UPAXIS_POS_Y
* KX_TRACK_UPAXIS_POS_Z

#### trackAxis

O eixo que aponta para o objeto alvo.

**Tipo:** integer from 0 to 5

* KX_TRACK_TRAXIS_POS_X
* KX_TRACK_TRAXIS_POS_Y
* KX_TRACK_TRAXIS_POS_Z
* KX_TRACK_TRAXIS_NEG_X
* KX_TRACK_TRAXIS_NEG_Y
* KX_TRACK_TRAXIS_NEG_Z

---

## KX_VehicleWrapper

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`KX_GameObject`](#kx_gameobject), [`Range.constraints`](#rangeconstraints), [`KX_CharacterWrapper`](#kx_characterwrapper)

KX_VehicleWrapper

TODO - descrição

```python
# Cria um veículo com quatro rodas. Os objetos das rodas precisam estar em No Collision.
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

vehicle = constraints.createVehicle(own.getPhysicsId())
own["vehicle_id"] = vehicle.getConstraintId()

wheels = (
    ("WheelFL", (-1.0, 1.5, 0.0), True),
    ("WheelFR", (1.0, 1.5, 0.0), True),
    ("WheelRL", (-1.0, -1.5, 0.0), False),
    ("WheelRR", (1.0, -1.5, 0.0), False),
)

for name, position, steering in wheels:
    vehicle.addWheel(scene.objects[name], position, (0, 0, -1), (-1, 0, 0), 0.4, 0.5, steering)
```

```python
# Dirige a cada quadro.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
vehicle = constraints.getVehicleConstraint(own["vehicle_id"])
keys = Range.logic.keyboard.inputs

force = -800.0 if keys[Range.events.WKEY].active else 0.0
steer = 0.3 if keys[Range.events.AKEY].active else 0.0

for wheel in range(vehicle.getNumWheels()):
    vehicle.applyEngineForce(force, wheel)

vehicle.setSteeringValue(steer, 0)
vehicle.setSteeringValue(steer, 1)
print(vehicle.getCurrentSpeedKmh())
```

```python
# Ajusta a suspensão de cada roda.
for wheel in range(vehicle.getNumWheels()):
    vehicle.setSuspensionStiffness(20.0, wheel)
    vehicle.setSuspensionDamping(2.0, wheel)
    vehicle.setSuspensionCompression(4.0, wheel)
    vehicle.setTyreFriction(2.0, wheel)
```

#### addWheel(wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering)

Adiciona uma roda ao veículo

- **`wheel`**: O objeto a usar como roda.
  - tipo: `KX_GameObject` or a `KX_GameObject` name
- **`attachPos`**: A posição onde prender a roda, relativa ao centro do objeto chassi.
  - tipo: vector of 3 floats
- **`downDir`**: O vetor de direção apontando para baixo, até onde o veículo deve colidir com o chão.
  - tipo: vector of 3 floats
- **`axleDir`**: O eixo em torno do qual a roda gira, relativo ao chassi.
  - tipo: vector of 3 floats
- **`suspensionRestLength`**: O comprimento da suspensão quando nenhuma força está sendo aplicada.
  - tipo: float
- **`wheelRadius`**: O raio da roda (metade do diâmetro).
  - tipo: float
- **`hasSteering`**: True se a roda deve virar com o volante; em geral usado nas rodas da frente.
  - tipo: boolean

#### applyBraking(force, wheelIndex)

Aplica uma força de freio à roda indicada

- **`force`**: a força de freio
  - tipo: float
- **`wheelIndex`**: índice da roda em que a força deve ser aplicada
  - tipo: integer

#### applyEngineForce(force, wheelIndex)

Aplica uma força de motor à roda indicada

- **`force`**: a força do motor
  - tipo: float
- **`wheelIndex`**: índice da roda em que a força deve ser aplicada
  - tipo: integer

#### getConstraintId()

Pega o ID da constraint

**Retorna:** o id da constraint

**Tipo do retorno:** integer

#### getConstraintType()

Devolve o tipo da constraint.

**Retorna:** tipo da constraint

**Tipo do retorno:** integer

#### getNumWheels()

Devolve o número de rodas.

**Retorna:** o número de rodas deste veículo

**Tipo do retorno:** integer

#### getWheelOrientationQuaternion(wheelIndex)

Devolve a orientação da roda como quaternion.

- **`wheelIndex`**: o índice da roda
  - tipo: integer

**Retorna:** TODO Descrição

**Tipo do retorno:** TODO - type should be quat as per method name but from the code it looks like a matrix

#### getWheelPosition(wheelIndex)

Devolve a posição da roda indicada

- **`wheelIndex`**: o índice da roda
  - tipo: integer

**Retorna:** vetor de posição

**Tipo do retorno:** list[x, y, z]

#### getWheelRotation(wheelIndex)

Devolve a rotação da roda indicada

- **`wheelIndex`**: o índice da roda
  - tipo: integer

**Retorna:** a rotação da roda

**Tipo do retorno:** float

#### setRollInfluence(rollInfluece, wheelIndex)

Define a influência de rolagem da roda indicada. Quanto maior a influência, mais o veículo tende a capotar nas curvas.

- **`rollInfluece`**: a influência de rolagem da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

#### setSteeringValue(steering, wheelIndex)

Define o esterço da roda indicada

- **`steering`**: o esterço da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

#### setSuspensionCompression(compression, wheelIndex)

Define a compressão da roda indicada

- **`compression`**: a compressão da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

#### setSuspensionDamping(damping, wheelIndex)

Define o amortecimento da roda indicada

- **`damping`**: o amortecimento da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

#### setSuspensionStiffness(stiffness, wheelIndex)

Define a rigidez da roda indicada

- **`stiffness`**: a rigidez da roda
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

#### setTyreFriction(friction, wheelIndex)

Define o atrito do pneu da roda indicada

- **`friction`**: o atrito do pneu
  - tipo: float
- **`wheelIndex`**: o índice da roda
  - tipo: integer

#### rayMask

Define a máscara do ray cast.

**Tipo:** bitfield

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### getCoordinateSystem()

 `método`

Eixos `(direita, cima, frente)` do veículo (0=X, 1=Y, 2=Z).

**Retorna:** `tuple`

#### getCurrentSpeedKmh()

 `método`

Velocidade atual em km/h.

**Retorna:** `float`

#### getCurrentSpeedMps()

 `método`

Velocidade atual em metros por segundo.

**Retorna:** `float`

#### getForwardVector()

 `método`

Direção da frente do veículo, no mundo.

**Retorna:** `Vector`

#### getWheelConfig(wheelIndex)

 `método`

Configuração da roda: `connectionPoint`, `downDirection`, `axleDirection`, `suspensionRestLength`, `wheelRadius`, `hasSteering` e `isDriveWheel`.

**Retorna:** `dict`

#### getWheelState(wheelIndex)

 `método`

Estado da roda neste tick: posição e orientação no mundo, `rotation`, `isInContact`, ponto e normal do contato, `suspensionForce` e mais.

**Retorna:** `dict`

#### loadPreset(path)

 `método`

Carrega um preset de veículo (arquivo) e aplica neste veículo.

#### rebuildPreset(path, wheelObjects)

 `método`

Recria as rodas a partir do preset, usando os objetos dados (um por roda). Use Empties com física **No Collision** como rodas.

#### resetSuspension()

 `método`

Volta a suspensão ao estado de repouso (útil depois de teleportar o carro).

#### savePreset(path)

 `método`

Salva a configuração atual do veículo num arquivo de preset.

#### setCoordinateSystem(right, up, forward)

 `método`

Define quais eixos (0=X, 1=Y, 2=Z) são direita, cima e frente. Precisa usar os três eixos sem repetir.

#### setSuspensionRestLength(valor, wheelIndex)

*(novo na Anastacio)* `método`

Muda o comprimento de repouso da suspensão de uma roda (valor positivo). Aplicado no próximo passo da física.

#### setWheelIsDriveWheel(wheelIndex, isDriveWheel)

 `método`

Define se a roda recebe tração do motor.

#### setWheelRadius(valor, wheelIndex)

*(novo na Anastacio)* `método`

Muda o raio de uma roda (valor positivo). Aplicado no próximo passo da física.

#### constraint_id

 `atributo · só leitura`

Id da restrição (constraint) física do veículo.

#### constraint_type

 `atributo · só leitura`

Tipo da restrição física do veículo.

---

## KX_VertexProxy

Classe base: [`SCA_IObject`](#sca_iobject)

Um vértice guarda informações de posição, UV, cor e normal.

Nota: a simulação de física NÃO é atualizada por enquanto; a física não reage a mudanças na posição do vértice.

```python
# Levanta um pouco todos os vértices de uma malha.
import Range

mesh = Range.logic.getCurrentController().owner.meshes[0]

for i in range(mesh.getVertexArrayLength(0)):
    vertex = mesh.getVertex(0, i)
    vertex.z += 0.01
```

```python
# Pinta os vértices de vermelho.
import Range

mesh = Range.logic.getCurrentController().owner.meshes[0]

for i in range(mesh.getVertexArrayLength(0)):
    mesh.getVertex(0, i).color = (1.0, 0.0, 0.0, 1.0)
```

#### XYZ

A posição do vértice.

**Tipo:** Vector((x, y, z))

#### UV

As coordenadas de textura do vértice.

**Tipo:** Vector((u, v))

#### uvs

A lista de coordenadas de textura do vértice.

**Tipo:** list of Vector((u, v))

#### normal

A normal do vértice.

**Tipo:** Vector((nx, ny, nz))

#### tangent

A tangente do vértice (somente leitura), calculada a partir do UV map usado pelo nó Normal Map ou Tangent do material (o UV map ativo por padrão). O componente w guarda o sinal da bitangente.

**Tipo:** Vector((tx, ty, tz, w))

#### color

A cor do vértice.

**Tipo:** Vector((r, g, b, a))

Preto = [0.0, 0.0, 0.0, 1.0], branco = [1.0, 1.0, 1.0, 1.0]

#### colors

A lista de cores do vértice.

**Tipo:** list of Vector((r, g, b, a))

#### x

A coordenada x do vértice.

**Tipo:** float

#### y

A coordenada y do vértice.

**Tipo:** float

#### z

A coordenada z do vértice.

**Tipo:** float

#### u

A coordenada de textura u do vértice.

**Tipo:** float

#### v

A coordenada de textura v do vértice.

**Tipo:** float

#### u2

A segunda coordenada de textura u do vértice.

**Tipo:** float

#### v2

A segunda coordenada de textura v do vértice.

**Tipo:** float

#### r

O componente vermelho da cor do vértice. 0.0 <= r <= 1.0.

**Tipo:** float

#### g

O componente verde da cor do vértice. 0.0 <= g <= 1.0.

**Tipo:** float

#### b

O componente azul da cor do vértice. 0.0 <= b <= 1.0.

**Tipo:** float

#### a

O componente alpha da cor do vértice. 0.0 <= a <= 1.0.

**Tipo:** float

#### getXYZ()

Pega a posição deste vértice.

**Retorna:** a posição deste vértice em coordenadas locais.

**Tipo do retorno:** Vector((x, y, z))

#### setXYZ(pos)

Define a posição deste vértice.

**Tipo:** Vector((x, y, z))

- **`pos`**: a nova posição deste vértice em coordenadas locais.

#### getUV()

Pega as coordenadas UV (de textura) deste vértice.

**Retorna:** as coordenadas UV (de textura) deste vértice.

**Tipo do retorno:** Vector((u, v))

#### setUV(uv)

Define as coordenadas UV (de textura) deste vértice.

**Tipo:** Vector((u, v))

#### getUV2()

Pega as 2ªs coordenadas UV (de textura) deste vértice.

**Retorna:** as coordenadas UV (de textura) deste vértice.

**Tipo do retorno:** Vector((u, v))

#### setUV2(uv, unit)

Define as 2ªs coordenadas UV (de textura) deste vértice.

**Tipo:** Vector((u, v))

- **`unit`**: argumento opcional, FLAT==1, SECOND_UV==2; o padrão é SECOND_UV
- **`unit`**: inteiro

#### getRGBA()

Pega a cor deste vértice.

A cor é representada como quatro bytes empacotados num inteiro, no formato RGBA.

Como o Python não tem como pegar cada byte sem deslocamento de bits, use o módulo struct para acessar a cor de um jeito independente da máquina.

Por isso, é recomendado usar os atributos r, g, b e a ou o atributo color.

```python

import struct;
col = struct.unpack('4B', struct.pack('I', v.getRGBA()))
# col = (r, g, b, a)
# black = (  0, 0, 0, 255)
# white = (255, 255, 255, 255)
```

**Retorna:** cor empacotada. Inteiro de 4 bytes com um byte por canal de cor, no formato RGBA.

**Tipo do retorno:** integer

#### setRGBA(col)

Define a cor deste vértice.

Veja getRGBA() para o formato de col e os problemas dele. Use os atributos r, g, b e a ou o atributo color.

setRGBA() também aceita uma lista de quatro componentes como argumento col. A lista representa a cor como [r, g, b, a], com preto = [0.0, 0.0, 0.0, 1.0] e branco = [1.0, 1.0, 1.0, 1.0]

```python

v.setRGBA(0xff0000ff) # Vermelho
v.setRGBA(0xff00ff00) # Verde em little endian, roxo transparente em big endian
v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Vermelho
v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Verde em todas as plataformas.
```

- **`col`**: a nova cor deste vértice, no formato RGBA empacotado.
  - tipo: integer or list [r, g, b, a]

#### getNormal()

Pega o vetor normal deste vértice.

**Retorna:** vetor normal normalizado.

**Tipo do retorno:** Vector((nx, ny, nz))

#### setNormal(normal)

Define o vetor normal deste vértice.

**Tipo:** sequence of floats [r, g, b]

- **`normal`**: a nova normal deste vértice.

---

## KX_VideoActuator

Classe `Range.types.KX_VideoActuator`.

```python
# Pausa o vídeo de outro objeto.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Video"]

act.object = "Screen"
act.mode = 1
cont.activate(act)
```

```python
# Avança dez segundos.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Video"]

act.mode = 5
act.seconds = 10.0
act.useRelative = True
cont.activate(act)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### mode

*(novo na Anastacio)* `atributo`

Ação sobre o Video Player: `0` Play, `1` Pause, `2` Toggle, `3` Stop, `4` Restart, `5` Seek.

#### object

*(novo na Anastacio)* `atributo`

Objeto com o Video Player que o actuator controla (`KX_GameObject`, nome ou `None`).

#### seconds

*(novo na Anastacio)* `atributo`

Posição em segundos usada pelo modo Seek.

#### useRelative

*(novo na Anastacio)* `atributo`

No modo Seek, se `True`, `seconds` é somado à posição atual em vez de ser absoluto.

---

## KX_VisibilityActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Visibility.

```python
# Esconde o objeto e os filhos.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Visibility"]

act.visibility = False
act.useRecursion = True
cont.activate(act)
```

#### visibility

se o atuador deixa o objeto pai visível ou invisível.

**Tipo:** boolean

#### useOcclusion

se o atuador torna o objeto pai um occluder ou não.

**Tipo:** boolean

#### useRecursion

se a visibilidade/oclusão deve ser propagada a todos os filhos do objeto.

**Tipo:** boolean

---

## KX_VoiceActuator

Atuador Voice: grava, toca e salva a voz do jogador.

```python
# Troca o efeito de voz antes de tocar.
import Range

cont = Range.logic.getCurrentController()
voice = cont.actuators["Voice"]
voice.effect = "RADIO"
cont.activate(voice)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### amount

*(novo na Anastacio)* `atributo`

Intensidade do efeito, de 0 a 1.

#### effect

*(novo na Anastacio)* `atributo`

Efeito de voz, como `NONE`, `CHIPMUNK`, `GIANT`, `ROBOT`, `RADIO`, `ECHO` ou `CAVE`.

#### maxSeconds

*(novo na Anastacio)* `atributo`

Tempo máximo de gravação em segundos, de 0 a 600.

#### mode

*(novo na Anastacio)* `atributo`

Ação: `0` gravar, `1` tocar, `2` ao vivo, `3` parar, `4` salvar.

#### slot

*(novo na Anastacio)* `atributo`

Nome da gravação usada pelo atuador.

#### useReverb

*(novo na Anastacio)* `atributo`

Usa o reverb da área ou do World.

#### volume

*(novo na Anastacio)* `atributo`

Volume, de 0 a 4.

---

## KX_VRHeadSensor

Classe `Range.types.KX_VRHeadSensor`.

```python
# Confirma com um aceno de cabeça.
import Range

sensor = Range.logic.getCurrentController().sensors["VRHead"]

sensor.mode = 4
sensor.time = 1.0

if sensor.positive:
    print("Yes")
```

```python
# Lê a rotação atual da cabeça.
import Range

sensor = Range.logic.getCurrentController().sensors["VRHead"]

print(sensor.yaw, sensor.pitch, sensor.roll)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### angle

*(novo na Anastacio)* `atributo`

Ângulo, em radianos, que a cabeça precisa girar para o gesto contar (0 a 1.6).

#### mode

*(novo na Anastacio)* `atributo`

Gesto detectado: 0 olhar para cima, 1 para baixo, 2 inclinar à esquerda, 3 à direita, 4 acenar "sim", 5 balançar "não".

#### pitch

*(novo na Anastacio)* `atributo · só leitura`

Inclinação atual da cabeça para cima/baixo.

#### roll

*(novo na Anastacio)* `atributo · só leitura`

Inclinação atual da cabeça para os lados.

#### time

*(novo na Anastacio)* `atributo`

Tempo, em segundos, para completar o gesto (0.05 a 10).

#### yaw

*(novo na Anastacio)* `atributo · só leitura`

Giro atual da cabeça para a esquerda/direita.

---

## KX_WorldInfo

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **Veja também:**
[`KX_Scene`](#kx_scene), [`KX_LightObject`](#kx_lightobject), [`KX_Camera`](#kx_camera)

Um objeto de mundo.

```python

# Deixa a cor da névoa vermelha.
import Range

sce = Range.logic.getCurrentScene()

sce.world.mistColor = [1.0, 0.0, 0.0]
```

```python

# Liga a névoa e aproxima da câmera.
import Range

world = Range.logic.getCurrentScene().world
world.mistEnable = True
world.mistStart = 5.0
world.mistDistance = 40.0
```

```python

# Liga a chuva e lê de volta o valor atual.
import Range

world = Range.logic.getCurrentScene().world
world.setWeather("rain", True)
print(world.getWeather("rain"))
```

```python

# Luz de fim de tarde: horizonte quente e luz ambiente mais fraca.
import Range

world = Range.logic.getCurrentScene().world
world.horizonColor = [1.0, 0.5, 0.2]
world.ambientColor = [0.2, 0.15, 0.1]
```

#### KX_MIST_QUADRATIC

Tipo de atenuação quadrática usada para esmaecer a névoa.

#### KX_MIST_LINEAR

Tipo de atenuação linear usada para esmaecer a névoa.

#### KX_MIST_INV_QUADRATIC

Tipo de atenuação quadrática inversa usada para esmaecer a névoa.

#### mistEnable

Devolve o estado da névoa.

**Tipo:** bool

#### mistStart

O ponto de início da névoa.

**Tipo:** float

#### mistDistance

A distância, a partir do ponto de início, para a névoa chegar a 100%.

**Tipo:** float

#### mistIntensity

A intensidade da névoa.

**Tipo:** float

#### mistType

O tipo de névoa: deve ser KX_MIST_QUADRATIC, KX_MIST_LINEAR ou KX_MIST_INV_QUADRATIC

#### mistColor

A cor da névoa. Preto = [0.0, 0.0, 0.0], branco = [1.0, 1.0, 1.0]. A névoa e a cor de fundo devem ter sempre a mesma cor.

**Tipo:** `mathutils.Color`

#### horizonColor

A cor do horizonte. Preto = [0.0, 0.0, 0.0, 1.0], branco = [1.0, 1.0, 1.0, 1.0]. A névoa e a cor do horizonte devem ter sempre a mesma cor.

**Tipo:** `mathutils.Vector`

#### zenithColor

A cor do zênite. Preto = [0.0, 0.0, 0.0, 1.0], branco = [1.0, 1.0, 1.0, 1.0].

**Tipo:** `mathutils.Vector`

#### ambientColor

A cor da luz ambiente. Preto = [0.0, 0.0, 0.0], branco = [1.0, 1.0, 1.0].

**Tipo:** `mathutils.Color`

#### exposure

Quantidade de correção de cor exponencial da luz.

**Tipo:** float between 0.0 and 1.0 inclusive

#### range

O intervalo de cor que será mapeado para 0 - 1.

**Tipo:** float between 0.2 and 5.0 inclusive

#### envLightEnergy

A energia da luz de ambiente.

**Tipo:** float from 0.0 to infinite

#### envLightEnabled

Devolve True se Environment Lighting estiver ligado; senão, False

**Tipo:** bool (read only)

#### envLightColor

White: devolve 0 SkyColor: devolve 1 SkyTexture: devolve 2

**Tipo:** int (read only)

#### setWeather(name, value)

Muda uma configuração de clima do World em tempo de execução (o prefixo "weather." é opcional). Booleanos: `rain`, `ripples`, `splash`, `puddles`, `puddle_ssr`, `ripple_puddle_only`, `splash_puddle_only` (os dois também ligam `puddles`), `aura`, `lightning`, `lightning_side`, `clouds`, `lens_flare`, `mist`. Floats: `rain_intensity`, `rain_density`, `rain_speed`, `rain_wind`, `rain_darken`, `rain_streak_width`, `ripple_intensity`, `ripple_normal`, `ripple_size`, `ripple_rate`, `splash_normal`, `splash_min_up`, `splash_size`, `splash_rate`, `splash_intensity`, `splash_distance`, `puddle_amount`, `puddle_size`, `puddle_darkness`, `puddle_reflection`, `puddle_distance`, `puddle_min_up`, `aura_size`, `aura_rate`, `aura_intensity`, `aura_distance`, `lightning_rate`, `lightning_intensity`, `lightning_distance`, `lightning_width`, `cloud_coverage`, `cloud_scale`, `cloud_speed`, `flare_scale`, `flare_intensity`, `mist_*`.

Superfícies molhadas (chuva): booleano `wet`; inteiro `wet_smooth_quality` (0 Off, 1 Low, 2 Medium, 3 High); floats `wet_darkness` (0-1), `wet_gloss` (0-1), `wet_distance` (metros), `wet_dry_time` (segundos), `wet_smooth_strength` (0-1), `wet_smooth_radius` (0.25-4), `wet_smooth_angle` (Keep Edges, em radianos) e `wet_smooth_distance` (metros).

Nuvens, Sky Layers e Nuvens Volumétricas (as chaves de ligar precisam do passe de nuvens, criado no carregamento quando qualquer um dos três está ligado no World): booleanos `use_sky_layers`, `use_volumetric_clouds`, `vcloud_shadow_enable`; inteiros `cloud_detail` (1-8), `vcloud_quality` (0 Low, 1 Medium, 2 High); floats `cloud_color_r/_g/_b`, `vcloud_coverage`, `vcloud_scale`, `vcloud_speed`, `vcloud_altitude`, `vcloud_thickness`, `vcloud_density`, `vcloud_detail_scale`, `vcloud_silver_intensity`, `vcloud_shadow_strength`, `vcloud_color_r/_g/_b`.

Fog - Volumetric: booleanos `vfog`, `vfog_use_lamps`, `vfog_use_shafts`, `vfog_use_sun_shafts`, `vfog_volumes_only`, `vfog_use_wind`, `vfog_use_time_of_day`, `vfog_use_layer`, `vfog_use_reach_clouds`; inteiros `vfog_quality` (0 Low, 1 Medium, 2 High), `vfog_max_lights` (1-8); floats `vfog_density`, `vfog_base`, `vfog_falloff`, `vfog_distance`, `vfog_noise_scale`, `vfog_noise_amount`, `vfog_speed`, `vfog_anisotropy`, `vfog_edge`, `vfog_light_intensity`, `vfog_sun_intensity`, `vfog_shaft_intensity`, `vfog_ambient`, `vfog_morning_boost`, `vfog_wind_direction` (graus), `vfog_dust` (0-1, partículas de poeira nos feixes de luz), `vfog_color_r/_g/_b`. A resolução da neblina é fixa no carregamento.

```python

scene.world.setWeather("aura", True)
scene.world.setWeather("splash_size", 1.5)
```

- **`name`**: nome da configuração
  - tipo: string
- **`value`**: novo valor
  - tipo: bool or float

**Erro:** nome de configuração desconhecido

#### strikeLightning(bolt=True)

Dispara um raio agora (World > Rain precisa estar ligado; os raios automáticos podem ficar desligados).

- **`bolt`**: mostra o raio; False dá só um clarão distante atrás das nuvens
  - tipo: bool

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### getWeather(name)

*(novo na Anastacio)* `método`

valor atual de uma configuração de clima do World (bool ou float)

#### atmosphereAltitude

*(novo na Anastacio)* `atributo`

Altitude do observador na atmosfera.

#### atmosphereIntensity

*(novo na Anastacio)* `atributo`

Intensidade do céu atmosférico.

#### atmosphereMieDensity

*(novo na Anastacio)* `atributo`

Densidade do espalhamento Mie (névoa e halo em volta do sol).

#### atmosphereMieDirection

*(novo na Anastacio)* `atributo`

Direção do espalhamento Mie: quanto o brilho se concentra perto do sol.

#### atmosphereRayleighColor

*(novo na Anastacio)* `atributo`

Cor do espalhamento Rayleigh (o azul do céu), como `[r, g, b]`. Valores negativos viram 0.

#### atmosphereRayleighDensity

*(novo na Anastacio)* `atributo`

Densidade do espalhamento Rayleigh.

#### auroraColors

*(novo na Anastacio)* `atributo`

Paleta de cores da aurora: `'GREEN'`, `'CLASSIC'` ou `'SHIFTING'`.

#### backgroundColor

 `atributo`

Cor de fundo `[r, g, b]` do World.

#### moonBrightness

*(novo na Anastacio)* `atributo`

Brilho da lua.

#### moonSize

*(novo na Anastacio)* `atributo`

Tamanho da lua no céu.

#### skyType

*(novo na Anastacio)* `atributo`

Tipo de céu do World: `'FLAT'`, `'GRADIENT'`, `'PROCEDURAL'` ou `'ATMOSPHERIC'`. Mudar recompila o shader do world no frame seguinte; materiais de objetos mantêm o tipo de céu com que foram compilados.

#### starStyle

*(novo na Anastacio)* `atributo`

Estilo das estrelas: `'SIMPLE'`, `'REALISTIC'` ou `'CONSTELLATIONS'`.

#### sunSize

 `atributo`

Tamanho do sol no céu (0 a 1).

#### useSkyAurora

*(novo na Anastacio)* `atributo`

Liga ou desliga a aurora no céu.

#### useSkyMoon

*(novo na Anastacio)* `atributo`

Liga ou desliga a lua no céu. Muda na hora, sem recompilar o shader.

#### useSkyStars

*(novo na Anastacio)* `atributo`

Liga ou desliga as estrelas no céu.

---

## SCA_2DFilterActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Cria, liga e desliga filtros 2D.

As propriedades a seguir não têm efeito imediato. É preciso ativar o atuador para ver o resultado. O atuador não é persistente: ele para sozinho depois de configurar o filtro, mas o filtro continua ativo. Para parar um filtro, ative o atuador com 'type' igual a `RAS_2DFILTER_DISABLED` ou `RAS_2DFILTER_NOFILTER`.

```python
# Liga o filtro deste atuador.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Filter"]

act.mode = Range.logic.RAS_2DFILTER_SEPIA
act.passNumber = 0
cont.activate(act)
```

#### shaderText

código-fonte do shader personalizado.

**Tipo:** string

#### disableMotionBlur

ação no motion blur: 0=liga, 1=desliga.

**Tipo:** integer

#### mode

Tipo de filtro 2D; use uma `destas constantes`.

**Tipo:** integer

#### passNumber

número de ordem do filtro na pilha de filtros 2D. Os filtros rodam em ordem crescente de passNb.

Só pode haver um filtro por passNb.

**Tipo:** integer (0-100)

#### value

argumento do filtro de motion blur.

**Tipo:** float (0.0-100.0)

---

## SCA_ActuatorSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

O sensor Actuator detecta mudanças no estado de um atuador do objeto pai. Ele gera um pulso positivo quando o atuador é ativado e um pulso negativo quando é desativado.

```python
# Espera uma ação terminar antes de continuar.
import Range

sensor = Range.logic.getCurrentController().sensors["ActuatorDone"]

sensor.actuator = "Wait"
sensor.mode = 1

if sensor.positive:
    print("Finished")
```

#### actuator

o nome do atuador que o sensor está monitorando.

**Tipo:** string

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### mode

*(novo na Anastacio)* `atributo`

`0` Active: verdadeiro enquanto o actuator monitorado está ativo. `1` Finished: dá um pulso quando o actuator termina (ex.: Wait, Action, Video).

---

## SCA_AlwaysSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Este sensor está sempre ativo.

```python
# Roda um script uma vez só, quando o objeto começa.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Always"]

sensor.usePosPulseMode = False

if sensor.positive:
    cont.owner["life"] = 100
```

```python
# Repete a cada 30 quadros de lógica.
import Range

sensor = Range.logic.getCurrentController().sensors["Always"]

sensor.usePosPulseMode = True
sensor.skippedTicks = 30
```

---

## SCA_ANDController

Classe base: [`SCA_IController`](#sca_icontroller)

Um controlador AND só ativa quando todos os sensores ligados estão ativos.

Não há métodos Python especiais para este controlador.

```python
# Com um controlador AND, os atuadores rodam quando todos os sensores estão positivos. Este script mostra a mesma regra.
import Range

cont = Range.logic.getCurrentController()

if all(sensor.positive for sensor in cont.sensors):
    print("All sensors are on")
```

---

## SCA_AnimationEventSensor

Classe `Range.types.SCA_AnimationEventSensor`.

```python
# Dispara nos quadros marcados na animação.
import Range

cont = Range.logic.getCurrentController()

if cont.sensors["AnimationEvent"].positive:
    print("Step")
```

---

## SCA_DelaySensor

Classe base: [`SCA_ISensor`](#sca_isensor)

O sensor Delay gera disparos positivos e negativos em momentos precisos, contados em frames. O parâmetro delay define a duração do período OFF inicial. Um disparo positivo é gerado no fim desse período.

O parâmetro duration define a duração do período ON que vem depois do OFF. Há um disparo negativo no fim do período ON. Se duration for 0, o sensor fica ON e não há disparo negativo.

O sensor roda o ciclo OFF-ON uma vez, a menos que a opção repeat esteja ligada: aí o ciclo OFF-ON se repete sem parar (ou só o OFF, se duration for 0).

Use `SCA_ISensor.reset` a qualquer momento para reiniciar o sensor.

```python
# Dispara 60 quadros de lógica depois que o objeto começa.
import Range

sensor = Range.logic.getCurrentController().sensors["Delay"]

sensor.delay = 60
sensor.duration = 10
sensor.repeat = False
```

#### delay

duração do período OFF inicial em número de frames; 0 para disparar na hora.

**Tipo:** integer.

#### duration

duração do período ON em número de frames, depois do período OFF inicial.

Se duration for maior que 0, um disparo negativo é enviado no fim do pulso ON.

**Tipo:** integer

#### repeat

1 se o ciclo OFF-ON deve se repetir sem parar, 0 se deve rodar uma vez.

**Tipo:** integer

#### repeatTimes

Número de vezes que o atuador vai repetir.

**Tipo:** integer.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### useDelta

 `atributo`

Conta o atraso em segundos (tempo real) em vez de frames lógicos.

---

## SCA_IActuator

Classe base: [`SCA_ILogicBrick`](#sca_ilogicbrick)

Classe base de todos os logic bricks de atuador.

```python
# Todos os atuadores são ligados e desligados pelo controlador.
import Range

cont = Range.logic.getCurrentController()

for act in cont.actuators:
    if cont.sensors[0].positive:
        cont.activate(act)
    else:
        cont.deactivate(act)
```

---

## SCA_IController

Classe base: [`SCA_ILogicBrick`](#sca_ilogicbrick)

Classe base de todos os logic bricks de controlador.

```python
# Lista o que está ligado a este controlador.
import Range

cont = Range.logic.getCurrentController()

print([sensor.name for sensor in cont.sensors])
print([act.name for act in cont.actuators])
```

```python
# Roda este controlador antes dos outros.
import Range

Range.logic.getCurrentController().useHighPriority = True
```

#### state

A máscara de bits de estado do controlador. Pode ser usada com o estado do GameObject para testar se o controlador está ativo.

**Tipo:** int bitmask

#### sensors

Uma lista dos sensores ligados a este controlador.

**Tipo:** sequence supporting index/string lookups and iteration.

> **Note:**
Os sensores não pertencem necessariamente ao mesmo objeto.

> **Note:**
Quando objetos são instanciados em dupligroups, as ligações com objetos de fora do dupligroup podem se perder.

#### actuators

Uma lista dos atuadores ligados a este controlador.

**Tipo:** sequence supporting index/string lookups and iteration.

> **Note:**
Os sensores não pertencem necessariamente ao mesmo objeto.

> **Note:**
Quando objetos são instanciados em dupligroups, as ligações com objetos de fora do dupligroup podem se perder.

#### useHighPriority

Quando ligado, o controlador sempre roda antes de todos os outros controladores que não têm isto ligado.

**Tipo:** boolen

> **Note:**
A ordem de execução entre controladores de alta prioridade não é garantida.

---

## SCA_ILogicBrick

Classe base: [`EXP_Value`](#exp_value)

Classe base de todos os logic bricks.

```python
# Sensores, controladores e atuadores conhecem o objeto deles.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors[0]

print(sensor.owner.name, sensor.name, sensor.executePriority)
```

#### executePriority

Define a ordem em que os controladores são avaliados e os atuadores são ativados (prioridade menor roda primeiro).

**Tipo:** executePriority: int

#### owner

O game object ao qual este logic brick está ligado (somente leitura).

**Tipo:** `KX_GameObject` or None in exceptional cases.

#### name

O nome deste logic brick (somente leitura).

**Tipo:** string

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### fireCount

*(novo na Anastacio)* `atributo · só leitura`

---

## SCA_InputEvent

Classe base: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Eventos de uma entrada de teclado ou mouse.

```python
# Os três momentos de uma tecla.
import Range

space = Range.logic.keyboard.inputs[Range.events.SPACEKEY]

if space.activated:
    print("Pressed")
if space.active:
    print("Held")
if space.released:
    print("Released")
```

```python
# Valor da roda do mouse neste quadro.
import Range

wheel = Range.logic.mouse.inputs[Range.events.WHEELUPMOUSE]

if wheel.active:
    print(wheel.values[-1])
```

#### status

Lista dos estados da entrada desde o último frame. Pode conter `Range.logic.KX_INPUT_NONE` e `Range.logic.KX_INPUT_ACTIVE`. A lista sempre tem um valor. O primeiro valor da lista é o último valor da lista no frame anterior (somente leitura).

**Tipo:** list of integer.

#### queue

Lista dos eventos da entrada desde o último frame. Pode conter `Range.logic.KX_INPUT_JUST_ACTIVATED` e `Range.logic.KX_INPUT_JUST_RELEASED`. A lista pode estar vazia (somente leitura).

**Tipo:** list of integer.

#### values

Lista dos valores da entrada desde o último frame. No teclado contém 1 ou 0; no mouse, a coordenada do mouse ou o movimento da roda. A lista sempre tem um valor; só nas entradas de teclado o tamanho dela é o de `queue` + 1. O primeiro valor da lista é o último valor da lista no frame anterior (somente leitura).

Exemplo para pegar as coordenadas do mouse sem normalizar:

```python

import Range

x = Range.logic.mouse.inputs[Range.events.MOUSEX].values[-1]
y = Range.logic.mouse.inputs[Range.events.MOUSEY].values[-1]

print("Mouse non-normalized position: x: {0}, y: {1}".format(x, y))
```

**Tipo:** list of integer.

#### inactive

True se a entrada estava inativa desde o último frame.

**Tipo:** boolean

#### active

True se a entrada estava ativa desde o último frame.

**Tipo:** boolean

#### activated

True se a entrada foi ativada desde o último frame.

**Tipo:** boolean

#### released

True se a entrada foi solta desde o último frame.

**Tipo:** boolean

#### type

O tipo da entrada. Uma `destas constantes`

**Tipo:** integer

---

## SCA_IObject

Classe base: [`EXP_Value`](#exp_value)

Esta classe não tem funções Python

```python

# Todo objeto do jogo também é um SCA_IObject.
import Range

obj = Range.logic.getCurrentController().owner
print(isinstance(obj, Range.types.SCA_IObject))
```

---

## SCA_ISensor

Classe base: [`SCA_ILogicBrick`](#sca_ilogicbrick)

Classe base de todos os logic bricks de sensor.

```python
# Separa o quadro de apertar do quadro de soltar.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

if sensor.triggered and sensor.positive:
    print("Pressed")
elif sensor.triggered:
    print("Released")
```

```python
# Usa o estado do sensor.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

if sensor.status == Range.logic.KX_SENSOR_JUST_ACTIVATED:
    print("Just pressed")
```

```python
# Inverte o resultado do sensor.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

sensor.invert = True
sensor.reset()
```

#### usePosPulseMode

Flag que liga e desliga o modo de pulso positivo.

**Tipo:** boolean

#### useNegPulseMode

Flag que liga e desliga o modo de pulso negativo.

**Tipo:** boolean

#### frequency

A frequência dos sensores em modo de pulso. (Obsoleto: use SCA_ISensor.skippedTicks)

**Tipo:** integer

#### skippedTicks

Número de ticks de lógica pulados entre 2 pulsos ativos

**Tipo:** integer

#### level

level: opção que define se detecta o nível ou a transição de borda ao entrar num estado. Só faz diferença em transições de estado de lógica (atuador State). Um detector de nível gera um pulso na hora, negativo ou positivo conforme a condição do sensor, assim que o estado é ativado. Um detector de borda espera uma mudança de estado antes de gerar um pulso. nota: exclusivo com `tap`; ligar este desliga `tap`.

**Tipo:** boolean

#### tap

Quando ligado, só sensores que acabaram de ativar mandam um evento positivo; depois disso os controladores os veem como negativos. Assim, uma tecla segura age como se fosse tocada só por um instante. nota: exclusivo com `level`; ligar este desliga `level`.

**Tipo:** boolean

#### invert

Flag que define se este sensor ativa com eventos positivos ou negativos.

**Tipo:** boolean

#### triggered

True se este sensor está em estado positivo (somente leitura).

**Tipo:** boolean

#### positive

True se este sensor está em estado positivo (somente leitura).

**Tipo:** boolean

#### pos_ticks

O número de ticks desde o último pulso positivo (somente leitura).

**Tipo:** int

#### neg_ticks

O número de ticks desde o último pulso negativo (somente leitura).

**Tipo:** int

#### status

O status do sensor (somente leitura): pode ser uma `destas constantes`.

**Tipo:** int

> **Note:**
Este atributo prático combina os valores dos atributos triggered e positive.

#### reset()

Reinicia o estado interno do sensor; o efeito depende do tipo de sensor e das configurações.

O sensor volta ao estado inicial, como se tivesse acabado de ser ativado.

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### useDeltaTime

 `atributo`

Usa o tempo real (delta time) para os intervalos do sensor em vez de contar frames.

---

## SCA_JoystickSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Este sensor detecta eventos do joystick do jogador.

```python
# Lê os eixos do sensor.
import Range

sensor = Range.logic.getCurrentController().sensors["Joystick"]

if sensor.connected:
    print(sensor.axisValues)
```

```python
# Mostra quais botões estão apertados.
import Range

sensor = Range.logic.getCurrentController().sensors["Joystick"]

print(sensor.getButtonActiveList())

if sensor.getButtonStatus(0):
    print("First button")
```

#### axisValues

O estado dos eixos do joystick, como uma lista de `numAxis` valores (somente leitura).

**Tipo:** list of ints.

Cada um dá o valor de um eixo entre -32767 e 32767, conforme o quanto o eixo está empurrado; 0 quando solto. Os 2 primeiros valores são usados pela maioria dos joysticks e gamepads para o controle de direção. O 3º e o 4º só existem em alguns joysticks e podem ser usados para controles quaisquer.

* esquerda:[-32767, 0, ...]
* direita:[32767, 0, ...]
* up:[0, -32767, ...]
* baixo:[0, 32767, ...]

#### axisSingle

como `axisValues`, mas devolve um único valor de eixo, definido pelo sensor (somente leitura).

**Tipo:** integer

> **Note:**
Use só em sensores do tipo "Single Axis"; senão, levanta um erro.

#### hatValues (Deprecated. Use :data:button instead)

O estado dos hats do joystick, como uma lista de `numHats` valores (somente leitura).

**Tipo:** list of ints

Cada um dá a direção do hat de 1 a 12; 0 quando inativo.

As direções do hat são estas...

* 0:Nenhuma
* 1:Up
* 2:Direita
* 4:Baixo
* 8:Esquerda
* 3:Cima - Direita
* 6:Baixo - Direita
* 12:Baixo - Esquerda
* 9:Cima - Esquerda

#### hatSingle (Deprecated. Use :data:button instead)

Como `hatValues`, mas devolve uma única direção de hat, definida pelo sensor (somente leitura).

**Tipo:** integer

#### numAxis

O número de eixos do joystick neste índice (somente leitura).

**Tipo:** integer

#### numButtons

O número de botões do joystick neste índice (somente leitura).

**Tipo:** integer

#### numHats (Deprecated. Use :data:numButtons instead)

O número de hats do joystick neste índice (somente leitura).

**Tipo:** integer

#### connected

True se há um joystick conectado neste índice (somente leitura).

**Tipo:** boolean

#### index

O índice do joystick a usar (de 0 a 7). O primeiro joystick é sempre 0.

**Tipo:** integer

#### threshold

Limite do eixo. Movimentos do eixo abaixo deste limite não disparam evento. Use valores entre 0 e 32767; valores menores são mais sensíveis.

**Tipo:** integer

#### button

O índice do botão a que o sensor reage (primeiro botão = 0). Com a opção "All Events" ligada, esta opção não tem efeito.

**Tipo:** integer

#### axis

O eixo a que este sensor reage, como uma lista de dois valores [axisIndex, axisDirection]

* axisIndex: o índice do eixo usado para detectar movimento, 1=controle de direção principal, 2=controle de direção secundário.
* axisDirection: 0=direita, 1=cima, 2=esquerda, 3=baixo.

**Tipo:** [integer, integer]

#### hat (Deprecated. Use :data:button instead)

O hat a que o sensor reage, como uma lista de dois valores: [hatIndex, hatDirection]

* hatIndex: o índice do hat usado para detectar movimento, 1=hat principal, 2=hat secundário (4 no máximo).
* hatDirection: 1-12.

**Tipo:** [integer, integer]

#### getButtonActiveList()

**Retorna:** Uma lista com os índices dos botões apertados agora.

**Tipo do retorno:** list

#### getButtonStatus(buttonIndex)

- **`buttonIndex`**: o índice do botão, 0=primeiro botão
  - tipo: integer

**Retorna:** Se o botão indicado está apertado agora.

**Tipo do retorno:** boolean

---

## SCA_KeyboardSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Um sensor de teclado detecta as teclas apertadas pelo jogador.

Veja o módulo `Range.events` para os códigos de tecla.

```python
# Vigia todas as teclas e mostra as apertadas.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

sensor.useAllKeys = True

for code, event in sensor.inputs.items():
    if event.active:
        print(Range.events.EventToString(code))
```

```python
# Troca a tecla por script.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

sensor.key = Range.events.EKEY
```

#### key

O código da tecla que este sensor procura.

**Tipo:** keycode from `Range.events` module

#### hold1

O código da primeira tecla modificadora que este sensor procura.

**Tipo:** keycode from `Range.events` module

#### hold2

O código da segunda tecla modificadora que este sensor procura.

**Tipo:** keycode from `Range.events` module

#### toggleProperty

O nome da propriedade que indica se as teclas digitadas devem ser registradas como texto.

**Tipo:** string

#### targetProperty

O nome da propriedade que recebe as teclas digitadas, quando elas são registradas como texto.

**Tipo:** string

#### useAllKeys

Define se o sensor aceita todas as teclas.

**Tipo:** boolean

#### inputs

Lista das teclas de entrada que foram apertadas, acabaram de ser soltas ou estão ativas neste frame (somente leitura).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~events~~

Lista das teclas que foram apertadas, acabaram de ser soltas ou estão ativas neste frame (somente leitura).

> **Obsoleto use :data:`inputs`:**

**Tipo:** list [[`keycode`, `status`], ...]

#### getKeyStatus(keycode)

Lê o estado de uma tecla.

- **`keycode`**: O código do botão cujo estado você quer ler; use uma `destas constantes`
  - tipo: integer

**Retorna:** O estado do botão, que pode ser uma `destas constantes`

**Tipo do retorno:** int

---

## SCA_MouseSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Logic brick do sensor de mouse.

```python
# Lê a posição do mouse e o botão esquerdo.
import Range

sensor = Range.logic.getCurrentController().sensors["Mouse"]

print(sensor.position)

if sensor.getButtonStatus(Range.logic.KX_MOUSE_BUT_LEFT) == Range.logic.KX_INPUT_ACTIVE:
    print("Left button held")
```

#### position

As coordenadas [x, y] atuais do mouse, em coordenadas do frame (pixels).

**Tipo:** [integer, interger]

#### mode

O modo do sensor.

**Tipo:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_WHEELUP(4) * KX_MOUSESENSORMODE_WHEELDOWN(5) * KX_MOUSESENSORMODE_MOVEMENT(6)

#### getButtonStatus(button)

Lê o estado de um botão do mouse.

- **`button`**: O código do botão cujo estado você quer ler; use uma `destas constantes`
  - tipo: int

**Retorna:** O estado do botão, que pode ser uma `destas constantes`

**Tipo do retorno:** int

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### holdTime

*(novo na Anastacio)* `atributo`

Tempo, em segundos, segurando o botão para o sensor disparar (0 a 30).

---

## SCA_NANDController

Classe base: [`SCA_IController`](#sca_icontroller)

Um controlador NAND ativa quando nem todos os sensores ligados estão ativos.

Não há métodos Python especiais para este controlador.

```python
# NAND liga os atuadores, a não ser que todos os sensores estejam positivos.
import Range

cont = Range.logic.getCurrentController()

print(not all(sensor.positive for sensor in cont.sensors))
```

---

## SCA_NORController

Classe base: [`SCA_IController`](#sca_icontroller)

Um controlador NOR só ativa quando todos os sensores ligados estão desativados.

Não há métodos Python especiais para este controlador.

```python
# NOR liga os atuadores só quando nenhum sensor está positivo.
import Range

cont = Range.logic.getCurrentController()

print(not any(sensor.positive for sensor in cont.sensors))
```

---

## SCA_ORController

Classe base: [`SCA_IController`](#sca_icontroller)

Um controlador OR ativa quando qualquer sensor ligado ativa.

Não há métodos Python especiais para este controlador.

```python
# OR liga os atuadores quando pelo menos um sensor está positivo.
import Range

cont = Range.logic.getCurrentController()

print(any(sensor.positive for sensor in cont.sensors))
```

---

## SCA_PropertyActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Property

```python
# Troca a propriedade em que este atuador escreve.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Property"]

cont.owner["score"] = 0
act.propName = "score"
act.value = "score + 10"
cont.activate(act)
```

#### propName

a propriedade sobre a qual operar.

**Tipo:** string

#### value

o valor com que o atuador opera.

**Tipo:** string

#### mode

TODO - adicionar as constantes ao dicionário de game logic!.

**Tipo:** integer

---

## SCA_PropertySensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Ativa quando a propriedade do game object corresponde.

```python
# Dispara quando a propriedade life chega a zero.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_EQUAL
sensor.propName = "life"
sensor.value = "0"
```

```python
# Dispara quando o valor está dentro de um intervalo.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_INTERVAL
sensor.propName = "life"
sensor.min = "1"
sensor.max = "20"
```

#### mode

Tipo de verificação da propriedade. Pode ser uma `destas constantes`

**Tipo:** integer.

#### propName

a propriedade com que o sensor opera.

**Tipo:** string

#### value

o valor que o sensor compara com o valor da propriedade.

**Tipo:** string

#### min

o valor mínimo do intervalo usado para avaliar a propriedade no modo interval.

**Tipo:** string

#### max

o valor máximo do intervalo usado para avaliar a propriedade no modo interval.

**Tipo:** string

---

## SCA_PythonController

Classe base: [`SCA_IController`](#sca_icontroller)

> **Veja também:**
[`KX_PythonComponent`](#kx_pythoncomponent), [`SCA_ISensor`](#sca_isensor), [`SCA_IActuator`](#sca_iactuator), [`Range.logic`](#rangelogic)

Um controlador Python usa um script Python para ativar seus atuadores, com base nos seus sensores.

```python
# O começo comum de um script.
import Range

cont = Range.logic.getCurrentController()
own = cont.owner

if cont.sensors["Keyboard"].positive:
    cont.activate("Motion")
else:
    cont.deactivate("Motion")
```

```python
# Modo Module: a engine chama uma função e passa o controlador.
def main(cont):
    print(cont.owner.name, cont.script)
```

#### owner

O objeto ao qual o controlador está ligado.

**Tipo:** `KX_GameObject`

#### script

O valor desta variável depende do modo de execução.

* No modo de execução 'Script', este valor contém o script Python inteiro numa única string (não o nome do script, como seria de esperar), que pode ser modificada para rodar outros scripts.
* No modo de execução 'Module', este valor contém uma string de uma linha: o nome do módulo e a função, "module.func" ou "package.modile.func", em que os nomes de módulo são textblocks Python ou scripts externos.

**Tipo:** string

> **Note:**
Depois que isto é definido, o nome do script usado nos avisos não muda mais.

#### mode

o modo de execução deste controlador (somente leitura).

* Script: 0, executa o `script` como código Python.
* Module: 1, executa o `script` como módulo e função.

**Tipo:** integer

#### activate(actuator)

Ativa um atuador ligado a este controlador.

- **`actuator`**: O atuador sobre o qual operar.
  - tipo: actuator or the actuator name as a string

#### deactivate(actuator)

Desativa um atuador ligado a este controlador.

- **`actuator`**: O atuador sobre o qual operar.
  - tipo: actuator or the actuator name as a string

---

## SCA_RandomActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Random

```python
# Sorteia um número de 1 a 6 e guarda em uma propriedade.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Random"]

cont.owner["dice"] = 0
act.propName = "dice"
act.setIntUniform(1, 6)
cont.activate(act)
```

```python
# Usa um valor decimal em torno de uma média.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Random"]

cont.owner["damage"] = 0.0
act.propName = "damage"
act.setFloatNormal(10.0, 2.0)
cont.activate(act)
```

#### seed

Semente do gerador de números aleatórios.

**Tipo:** integer.

Sementes iguais produzem séries iguais. Se a semente for 0, o gerador produz o mesmo valor em toda chamada.

#### para1

o primeiro parâmetro da distribuição ativa.

**Tipo:** float, read-only.

Veja a documentação dos tipos de gerador para o significado deste valor.

#### para2

o segundo parâmetro da distribuição ativa.

**Tipo:** float, read-only

Veja a documentação dos tipos de gerador para o significado deste valor.

#### distribution

Tipo de distribuição (somente leitura). Pode ser uma `destas constantes`

**Tipo:** integer

#### propName

o nome da propriedade que recebe o valor aleatório.

**Tipo:** string

Se os tipos do gerador e da propriedade não combinarem, a atribuição é ignorada.

#### setBoolConst(value)

Faz este gerador produzir um valor booleano constante.

- **`value`**: O valor a devolver.
  - tipo: boolean

#### setBoolUniform()

Faz este gerador produzir uma distribuição booleana uniforme.

O gerador gera True ou False com 50% de chance.

#### setBoolBernouilli(value)

Faz este gerador produzir uma distribuição de Bernoulli.

- **`value`**: Define a proporção de valores False a produzir. * 0.0: sempre gera True * 1.0: sempre gera False
  - tipo: float

#### setIntConst(value)

Faz este gerador produzir sempre o valor dado.

- **`value`**: o valor que este gerador produz.
  - tipo: integer

#### setIntUniform(lower_bound, upper_bound)

Faz este gerador produzir um valor aleatório entre os limites inferior e superior dados (inclusive).

  - tipo: integer
  - tipo: integer

#### setIntPoisson(value)

Gera um número com distribuição de Poisson.

Faz uma série de testes de Bernoulli com o parâmetro value. Devolve o número de tentativas até ter sucesso.

  - tipo: float

#### setFloatConst(value)

Sempre gera o valor dado.

  - tipo: float

#### setFloatUniform(lower_bound, upper_bound)

Gera um float aleatório entre lower_bound e upper_bound com distribuição uniforme.

  - tipo: float
  - tipo: float

#### setFloatNormal(mean, standard_deviation)

Gera um float aleatório da distribuição normal dada.

- **`mean`**: O valor médio dos números gerados
  - tipo: float
- **`standard_deviation`**: O desvio padrão dos números gerados.
  - tipo: float

#### setFloatNegativeExponential(half_life)

Gera números com distribuição exponencial negativa.

O "tempo" de meia-vida é definido por half_life.

  - tipo: float

---

## SCA_RandomSensor

Classe base: [`SCA_ISensor`](#sca_isensor)

Este sensor ativa aleatoriamente.

```python
# Usa uma semente fixa para repetir a mesma sequência.
import Range

sensor = Range.logic.getCurrentController().sensors["Random"]

sensor.seed = 1234
print(sensor.lastDraw)
```

#### lastDraw

A semente do gerador de números aleatórios.

**Tipo:** integer

#### seed

A semente do gerador de números aleatórios.

**Tipo:** integer

---

## SCA_VibrationActuator

Classe base: [`SCA_IActuator`](#sca_iactuator)

Atuador Vibration.

```python
# Vibra o primeiro controle ao levar um golpe.
import Range

act = Range.logic.getCurrentController().actuators["Vibration"]

if act.hasVibration and not act.isVibrating:
    act.joyindex = 0
    act.strengthLeft = 1.0
    act.strengthRight = 0.5
    act.duration = 300
    act.startVibration()
```

#### joyindex

Índice do joystick.

**Tipo:** integer (0 to 7)

#### strengthLeft

Força do motor de baixa frequência do joystick (em geral fica à esquerda).

**Tipo:** float (0.0 to 1.0)

#### strengthRight

Força do motor de alta frequência do joystick (em geral fica à direita).

**Tipo:** float (0.0 to 1.0)

#### duration

Duração da vibração em milissegundos.

**Tipo:** integer (0 to infinite)

#### isVibrating

Verifica o status da vibração do joystick

**Tipo:** bool (true vibrating and false stopped)

#### hasVibration

Verifica se o joystick suporta vibração

**Tipo:** bool (true supported and false not supported)

#### startVibration()

Começa a vibração.

**Retorna:** None

#### stopVibration()

Para a vibração.

**Retorna:** None

---

## SCA_WaitActuator

Classe `Range.types.SCA_WaitActuator`.

```python
# Espera três segundos.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Wait"]

act.duration = 3.0
act.useRestart = False
cont.activate(act)
```

```python
# Mostra o tempo que falta.
import Range

act = Range.logic.getCurrentController().actuators["Wait"]

if act.waiting:
    print(act.duration - act.elapsed)
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### duration

*(novo na Anastacio)* `atributo`

Tempo de espera em segundos (0 a 100000). Ao receber pulso positivo o actuator começa a contar; quando o tempo passa, ele termina e um sensor **Actuator** em modo Finished dispara.

#### elapsed

*(novo na Anastacio)* `atributo · só leitura`

Segundos já passados desde o início da espera atual.

#### useRestart

*(novo na Anastacio)* `atributo`

Se `True`, um novo pulso positivo durante a espera reinicia a contagem do zero.

#### waiting

*(novo na Anastacio)* `atributo · só leitura`

`True` enquanto o actuator está contando.

---

## SCA_XNORController

Classe base: [`SCA_IController`](#sca_icontroller)

Um controlador XNOR ativa quando todos os sensores ligados estão iguais (ativos ou inativos).

Não há métodos Python especiais para este controlador.

```python
# XNOR liga os atuadores, a não ser que exatamente um sensor esteja positivo.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) != 1)
```

---

## SCA_XORController

Classe base: [`SCA_IController`](#sca_icontroller)

Um controlador XOR ativa quando as entradas estão misturadas, mas não quando todas estão ligadas ou desligadas.

Não há métodos Python especiais para este controlador.

```python
# XOR liga os atuadores quando exatamente um sensor está positivo.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) == 1)
```

---

## Texture

Classe `Range.types.Texture`.

```python
# Coloca uma imagem em um material. Guarde o objeto em uma propriedade, senão ele é liberado.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.mipmap = True
tex.refresh(False)
own["poster"] = tex
```

```python
# Devolve a textura original.
import Range

own = Range.logic.getCurrentController().owner

own["poster"].close()
del own["poster"]
```

### Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

#### close()

 `método`

Fecha o decklink dinâmico e restaura o original

#### refresh()

 `método`

Atualiza o decklink a partir da fonte

#### bindId

 `atributo · só leitura`

Id OpenGL da textura.

#### mipmap

 `atributo`

Usa mipmap na textura (`True`/`False`).

#### source

 `atributo`

Fonte da imagem (vídeo, câmera, imagem...) desenhada na textura.

---

## TrackLine

Polilinha fechada para IA de corrida, calculada em C++. Diz quanto da pista o carro já percorreu, dá o ponto e o lado da pista a uma distância e guarda perfis por ponto (curvatura, velocidade segura). Monte uma vez por pista e compartilhe entre os carros.

A linha é fechada: o último ponto liga no primeiro. `s` é a distância em metros desde o primeiro ponto e dá a volta, então `s` maior que `length` ou negativo funciona.

```python

import Range
from mathutils import Vector

points = curve.getCurvePoints()        # ou o centro da malha da estrada
line = Range.types.TrackLine(points)

d2, s, seg = line.locate(car.worldPosition)               # busca global
d2, s, seg = line.locate(car.worldPosition, seg, 15, 40, 20.0)  # perto do último segmento
target = line.point(s + 12.0)          # 12 m à frente
right = line.side(s)                   # vetor unitário para a direita, ou None
```

- **`points`**: pelo menos 3 pontos (`mathutils.Vector` ou sequências de 3 números).
  - tipo: sequence

#### length

Comprimento total da linha fechada, em metros (só leitura).

**Tipo:** float

#### locate(pos, seg=-1, back=0, ahead=0, lost=0.0)

Segmento da linha mais perto de `pos`.

Com `seg` >= 0 só os segmentos de `seg - back` a `seg + ahead` são testados, o que evita pular para um trecho vizinho da pista. Quando esse resultado fica a mais de `lost` metros (respawn, atalho), ou com `seg` = -1, a linha inteira é procurada.

- **`pos`**: posição em coordenadas do mundo.
  - tipo: `mathutils.Vector`
- **`seg`**: segmento da chamada anterior, -1 se desconhecido.
  - tipo: integer
- **`back`**: segmentos testados atrás de `seg`.
  - tipo: integer
- **`ahead`**: segmentos testados à frente de `seg`.
  - tipo: integer
- **`lost`**: distância em metros que dispara a busca global.
  - tipo: float

**Retorna:** (distância ao quadrado até a linha, `s` em metros, índice do segmento).

**Tipo do retorno:** tuple (float, float, integer)

#### point(s)

Ponto da linha a `s` metros do início.

**Tipo do retorno:** `mathutils.Vector`

#### side(s)

Vetor horizontal unitário apontando para a direita da linha em `s`, ou None onde a linha é vertical ou degenerada.

**Tipo do retorno:** `mathutils.Vector` or None

#### setProfile(name, values)

Guarda um valor por ponto com o nome `name` (curvatura, velocidade segura, qualquer número).

- **`name`**: nome do perfil.
  - tipo: string
- **`values`**: um número por ponto da linha.
  - tipo: sequence of float

#### profile(name, s)

Valor do perfil `name` interpolado em `s` metros.

**Tipo do retorno:** float
