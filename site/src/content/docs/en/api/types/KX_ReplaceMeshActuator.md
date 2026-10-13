---
title: "KX_ReplaceMeshActuator"
description: "Range.types.KX_ReplaceMeshActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Edit Object actuator, in Replace Mesh mode.

:::caution
Replace mesh actuators will be ignored if at game start, the named mesh doesn't exist.

This will generate a warning in the console

```text

Error: GameObject 'Name' ReplaceMeshActuator 'ActuatorName' without object
```
:::

```python

# Level-of-detail
# Switch a game object's mesh based on its depth in the camera view.
# +----------+     +-----------+     +-------------------------------------+
# | Always   +-----+ Python    +-----+ Edit Object (Replace Mesh) LOD.Mesh |
# +----------+     +-----------+     +-------------------------------------+
from Range import logic

# List detail meshes here
# Mesh (name, near, far)
# Meshes overlap so that they don't 'pop' when on the edge of the distance.
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

# Depth is negative and decreasing further from the camera
depth = Depth(object.position, camera.world_to_camera[2])

newmesh = None
curmesh = None
# Find the lowest detail mesh for depth
for mesh in meshes:
  if depth < mesh[1] and depth > mesh[2]:
    newmesh = mesh
  if "ME" + object.name + mesh[0] == actuator.getMesh():
      curmesh = mesh

if newmesh != None and "ME" + object.name + newmesh[0] != actuator.mesh:
  # The mesh is a different mesh - switch it.
  # Check the current mesh is not a better fit.
  if curmesh == None or curmesh[1] < depth or curmesh[2] > depth:
    actuator.mesh = object.name + newmesh[0]
    cont.activate(actuator)
```

### mesh

`MeshProxy` or the name of the mesh that will replace the current one.

Set to None to disable actuator.

**Type:** `MeshProxy` or None if no mesh is set

### useDisplayMesh

when true the displayed mesh is replaced.

**Type:** boolean

### usePhysicsMesh

when true the physics mesh is replaced.

**Type:** boolean

### instantReplaceMesh()

Immediately replace mesh without delay.

