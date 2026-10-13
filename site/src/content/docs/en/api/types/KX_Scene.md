---
title: "KX_Scene"
description: "Range.types.KX_Scene class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`KX_GameObject`](../../types/kx_gameobject/), [`KX_Camera`](../../types/kx_camera/), [`KX_WorldInfo`](../../types/kx_worldinfo/), [`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`Range.logic`](../../modulos/logic/)
:::



An active scene that gives access to objects, cameras, lights and scene attributes.

The activity culling stuff is supposed to disable logic bricks when their owner gets too far
from the active camera.  It was taken from some code lurking at the back of KX_Scene - who knows
what it does!

```python

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
```

```python

# Get the depth of an object in the camera view.
from Range import logic

object = logic.getCurrentController().owner
cam = logic.getCurrentScene().active_camera

# Depth is negative and decreasing further from the camera
depth = object.position[0]*cam.world_to_camera[2][0] + object.position[1]*cam.world_to_camera[2][1] + object.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]
```

@bug: All attributes are read only at the moment.

### name

The scene's name, (read-only).

**Type:** string

### objects

A list of objects in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`

### objectsInactive

A list of objects on background layers (used for the addObject actuator), (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`

### lights

A list of lights in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_LightObject`

### cameras

A list of cameras in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_Camera`

### texts

A list of texts in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_FontObject`

### active_camera

The current active camera.

**Type:** `KX_Camera`

:::note
This can be set directly from python to avoid using the `KX_SceneActuator`.
:::

### overrideCullingCamera

The override camera used for scene culling, if set to None the culling is proceeded with the camera used to render.

**Type:** `KX_Camera` or None

### world

The current active world, (read-only).

**Type:** `KX_WorldInfo`

### filterManager

The scene's 2D filter manager, (read-only).

**Type:** `KX_2DFilterManager`

### suspended

True if the scene is suspended, (read-only).

**Type:** boolean

### activityCulling

True if the scene allow object activity culling.

**Type:** boolean

### dbvt_culling

True when Dynamic Bounding box Volume Tree is set (read-only).

**Type:** boolean

### pre_draw

A list of callables to be run before the render step. The callbacks can take as argument the rendered camera.

**Type:** list

### post_draw

A list of callables to be run after the render step.

**Type:** list

### pre_draw_setup

A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed).
The callbacks can take as argument the rendered camera, the camera could be temporary in case of stereo rendering.

**Type:** list

### onRemove

A list of callables to run when the scene is destroyed.

```python

@scene.onRemove.append
def callback(scene):
      print('exiting %s...' % scene.name)
```

**Type:** list

### gravity

The scene gravity using the world x, y and z axis.

**Type:** Vector((gx, gy, gz))

### maxDebris

The number of fragments of broken objects kept alive in the scene; past it the oldest are removed.
Starts with Scene > Game Physics > Max Debris. 0 means no limit. Lowering it removes the extra pieces at once.

**Type:** integer in [0, 100000]

### explode(position, radius=5.0, force=20.0, upBias=0.3, occlusion=True, mask=0xFFFF, ignore=None)

Radial impulse on the dynamic objects around position, falling to zero at radius
(`force * (1 - distance / radius)`). Destructible objects hit above their `KX_GameObject.breakImpulse`
break and their pieces are pushed, sharing the impulse by mass. Explosive objects hit above their Impact
Impulse (with Chain Reaction on) detonate on the next frame.

- **`position`**: The center of the blast.
  - type: 3D Vector
- **`radius`**: The distance the blast reaches.
  - type: float
- **`force`**: The impulse at the center.
  - type: float
- **`upBias`**: How much the push is tilted upwards, 0.0 is straight away from the center.
  - type: float
- **`occlusion`**: If True, static geometry between the center and an object shields it.
  - type: boolean
- **`mask`**: The collision groups reached.
  - type: bitfield
- **`ignore`**: An object or a list of objects left out.
  - type: `KX_GameObject` or list

**Returns:** The objects reached (not the new pieces).

**Return type:** list of `KX_GameObject`

### addObject(object, reference, time=0.0)

Adds an object to the scene like the Add Object Actuator would.

- **`object`**: The (name of the) object to add.
  - type: `KX_GameObject` or string
- **`reference`**: The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
  - type: `KX_GameObject` or string
- **`time`**: The lifetime of the added object, in frames (assumes one frame is 1/50 second). A time of 0.0 means the object will last forever (optional).
  - type: float

**Returns:** The newly added object.

**Return type:** `KX_GameObject`

### end()

Removes the scene from the game.

### restart()

Restarts the scene.

### replace(scene)

Replaces this scene with another one.

- **`scene`**: The name of the scene to replace this scene with.
  - type: string

**Returns:** True if the scene exists and was scheduled for addition, False otherwise.

**Return type:** boolean

### suspend()

Suspends this scene.

### resume()

Resume this scene.

### get(key, default=None)

Return the value matching key, or the default value if its not found.

**Returns:** The key value or a default.

### drawObstacleSimulation()

Draw debug visualization of obstacle simulation.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### convertObject(name, children=True)

 <small>method</small>

Creates now an object that was left out at load time by the **Convert** option (and its unconverted children). It goes to `objects` if it is on an active layer, otherwise to `objectsInactive` (ready for `addObject`). An object already converted is returned as is.

**Returns:** `KX_GameObject`

### play_cutscene(sequence=0)

 <small>method</small>

Starts the scene native Cutscene. Returns `True` on success.

**Returns:** `bool`

### release_cutscene_trigger(name)

 <small>method</small>

Releases a Cutscene **Wait Trigger** event waiting for `name`. `True` if it was waiting right now; otherwise the trigger is kept for the next Wait Trigger with that name. A message with subject `name` does the same.

**Returns:** `bool`

### restart_cutscene()

 <small>method</small>

Restarts the active Cutscene and removes the objects it created.

### stop_cutscene()

 <small>method</small>

Stops the Cutscene and removes the objects it created.

### speakers

 <small>attribute · read-only</small>

List of the scene sound objects (`KX_Speaker`).

### thread_logic_1

 <small>attribute</small>

List of functions called every frame on the parallel logic thread. Same usage as `pre_draw`.

### unconvertedObjects

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Names of the objects that can still be created with `convertObject()`.

### worldSun

 <small>attribute · read-only</small>

Sun light linked to the World (sky sun position), or `None`.

