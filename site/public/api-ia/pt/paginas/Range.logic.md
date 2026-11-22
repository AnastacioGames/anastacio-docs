# Range.logic

> **Veja também:**
[`KX_GameObject`](KX_GameObject.md), [`KX_Scene`](KX_Scene.md), [`Range.events`](Range.events.md), [`SCA_PythonController`](SCA_PythonController.md)

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

## Introdução

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

## Variáveis

## Sensor de armature

Veja `Range.types.KX_ArmatureSensor.type`

## Sensor de radar

Veja `Range.types.KX_RadarSensor`

## Sensor de raio

Veja `Range.types.KX_RaySensor`

## Atuador de ação

Veja `Range.types.BL_ActionActuator`

## Atuador de armature

Veja `Range.types.BL_ArmatureActuator.type`

## Atuador de constraint

Veja `Range.types.KX_ConstraintActuator.option`

* Vale para a constraint de distância:

## Atuador dinâmico

Veja `Range.types.KX_SCA_DynamicActuator`

## Atuador de jogo

Veja `Range.types.KX_GameActuator`

## Distribuições aleatórias

Veja `Range.types.SCA_RandomActuator`

## Atuador de cena

Veja `Range.types.KX_SceneActuator`

## Atuador de som

Veja `Range.types.KX_SoundActuator`

## Atuador de steering

Veja `Range.types.KX_SteeringActuator.behavior`

## Atuador TrackTo

Veja `Range.types.KX_TrackToActuator`

## Canal de armature

Veja `Range.types.BL_ArmatureChannel.rotation_mode`

Observação: os modos euler têm os nomes da interface do Blender, mas a ordem real dos eixos é invertida

## Constraint de armature

Veja `Range.types.BL_ArmatureConstraint.type`

## Estado da entrada

Veja `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

## KX_GameObject

Veja `Range.types.KX_GameObject.playAction`

## Botões do mouse

Veja `Range.types.SCA_MouseSensor`

## Estados

Veja `Range.types.KX_StateActuator`

Visão geral. Os itens estão nas partes abaixo:

- [atributos](Range.logic--props.md) (6 itens)
- [métodos e funções](Range.logic--funcs.md) (66 itens)
- [constantes](Range.logic--consts.md) (283 itens)
