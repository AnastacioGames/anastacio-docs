---
title: "KX_Scene"
description: "Referência da classe Range.types.KX_Scene"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



An active scene that gives access to objects, cameras, lights and scene attributes.

The activity culling stuff is supposed to disable logic bricks when their owner gets too far
from the active camera.  It was taken from some code lurking at the back of KX_Scene - who knows
what it does!

``python

from Range import logic

# get the scene
scene = logic.getCurrentScene()

# print all the objects in the scene
for object in scene.objects:
   print(object.name)

# get an object named 'Cube'
object = scene.objects["Cube"]

# get the first object in the scene.
object = scene.objects[0]
``

``python

# Get the depth of an object in the camera view.
from Range import logic

object = logic.getCurrentController().owner
cam = logic.getCurrentScene().active_camera

# Depth is negative and decreasing further from the camera
depth = object.position[0]*cam.world_to_camera[2][0] + object.position[1]*cam.world_to_camera[2][1] + object.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]
``

@bug: All attributes are read only at the moment.

### name

The scene's name, (read-only).

**Tipo:** string

### objects

A list of objects in the scene, (read-only).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### objectsInactive

A list of objects on background layers (used for the addObject actuator), (read-only).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### lights

A list of lights in the scene, (read-only).

**Tipo:** `EXP_ListValue` of `KX_LightObject`

### cameras

A list of cameras in the scene, (read-only).

**Tipo:** `EXP_ListValue` of `KX_Camera`

### texts

A list of texts in the scene, (read-only).

**Tipo:** `EXP_ListValue` of `KX_FontObject`

### active_camera

The current active camera.

**Tipo:** `KX_Camera`

:::note
This can be set directly from python to avoid using the `KX_SceneActuator`.
:::

### overrideCullingCamera

The override camera used for scene culling, if set to None the culling is proceeded with the camera used to render.

**Tipo:** `KX_Camera` or None

### world

The current active world, (read-only).

**Tipo:** `KX_WorldInfo`

### filterManager

The scene's 2D filter manager, (read-only).

**Tipo:** `KX_2DFilterManager`

### suspended

True if the scene is suspended, (read-only).

**Tipo:** boolean

### activityCulling

True if the scene allow object activity culling.

**Tipo:** boolean

### dbvt_culling

True when Dynamic Bounding box Volume Tree is set (read-only).

**Tipo:** boolean

### pre_draw

A list of callables to be run before the render step. The callbacks can take as argument the rendered camera.

**Tipo:** list

### post_draw

A list of callables to be run after the render step.

**Tipo:** list

### pre_draw_setup

A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed).
The callbacks can take as argument the rendered camera, the camera could be temporary in case of stereo rendering.

**Tipo:** list

### onRemove

A list of callables to run when the scene is destroyed.

``python

@scene.onRemove.append
def callback(scene):
      print('exiting %s...' % scene.name)
``

**Tipo:** list

### gravity

The scene gravity using the world x, y and z axis.

**Tipo:** Vector((gx, gy, gz))

### maxDebris

The number of fragments of broken objects kept alive in the scene; past it the oldest are removed.
Starts with Scene > Game Physics > Max Debris. 0 means no limit. Lowering it removes the extra pieces at once.

**Tipo:** integer in [0, 100000]

### explode(position, radius=5.0, force=20.0, upBias=0.3, occlusion=True, mask=0xFFFF, ignore=None)

Radial impulse on the dynamic objects around position, falling to zero at radius
(`force * (1 - distance / radius)`). Destructible objects hit above their `KX_GameObject.breakImpulse`
break and their pieces are pushed, sharing the impulse by mass. Explosive objects hit above their Impact
Impulse (with Chain Reaction on) detonate on the next frame.

- **`position`**: The center of the blast.
  - tipo: 3D Vector
- **`radius`**: The distance the blast reaches.
  - tipo: float
- **`force`**: The impulse at the center.
  - tipo: float
- **`upBias`**: How much the push is tilted upwards, 0.0 is straight away from the center.
  - tipo: float
- **`occlusion`**: If True, static geometry between the center and an object shields it.
  - tipo: boolean
- **`mask`**: The collision groups reached.
  - tipo: bitfield
- **`ignore`**: An object or a list of objects left out.
  - tipo: `KX_GameObject` or list

**Retorna:** The objects reached (not the new pieces).

**Tipo do retorno:** list of `KX_GameObject`

### addObject(object, reference, time=0.0)

Adds an object to the scene like the Add Object Actuator would.

- **`object`**: The (name of the) object to add.
  - tipo: `KX_GameObject` or string
- **`reference`**: The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
  - tipo: `KX_GameObject` or string
- **`time`**: The lifetime of the added object, in frames (assumes one frame is 1/50 second). A time of 0.0 means the object will last forever (optional).
  - tipo: float

**Retorna:** The newly added object.

**Tipo do retorno:** `KX_GameObject`

### end()

Removes the scene from the game.

### restart()

Restarts the scene.

### replace(scene)

Replaces this scene with another one.

- **`scene`**: The name of the scene to replace this scene with.
  - tipo: string

**Retorna:** True if the scene exists and was scheduled for addition, False otherwise.

**Tipo do retorno:** boolean

### suspend()

Suspends this scene.

### resume()

Resume this scene.

### get(key, default=None)

Return the value matching key, or the default value if its not found.

**Retorna:** The key value or a default.

### drawObstacleSimulation()

Draw debug visualization of obstacle simulation.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### convertObject()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### play_cutscene()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### release_cutscene_trigger()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### restart_cutscene()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### stop_cutscene()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### speakers

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### thread_logic_1

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### unconvertedObjects

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### worldSun

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

