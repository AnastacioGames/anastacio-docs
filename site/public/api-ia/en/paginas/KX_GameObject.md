# KX_GameObject

Base class: [`SCA_IObject`](SCA_IObject.md)

> **See also:**
[`KX_Scene`](KX_Scene.md), [`KX_Mesh`](KX_Mesh.md), [`KX_PythonComponent`](KX_PythonComponent.md), [`KX_VehicleWrapper`](KX_VehicleWrapper.md), [`KX_ParticleSystem`](KX_ParticleSystem.md)

All game objects are derived from this class.

Properties assigned to game objects are accessible as attributes of this class.

> **Note:**
Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError,
if an object may have been removed since last accessing it use the `invalid` attribute to check.

KX_GameObject can be subclassed to extend functionality. For example:

```python

import Range

class CustomGameObject(Range.types.KX_GameObject):
    RATE = 0.05

    def __init__(self, old_owner):
        # "old_owner" can just be ignored. At this point, "self" is
        # already the object in the scene, and "old_owner" has been
        # destroyed.

        # New attributes can be defined - but we could also use a game
        # property, like "self['rate']".
        self.rate = CustomGameObject.RATE

    def update(self):
        self.worldPosition.z += self.rate

        # switch direction
        if self.worldPosition.z > 1.0:
            self.rate = -CustomGameObject.RATE
        elif self.worldPosition.z < 0.0:
            self.rate = CustomGameObject.RATE

# Called first
def mutate(cont):
    old_object = cont.owner
    mutated_object = CustomGameObject(cont.owner)

    # After calling the constructor above, references to the old object
    # should not be used.
    assert(old_object is not mutated_object)
    assert(old_object.invalid)
    assert(mutated_object is cont.owner)

# Called later - note we are now working with the mutated object.
def update(cont):
    cont.owner.update()
```

When subclassing objects other than empties and meshes, the specific type
should be used - e.g. inherit from `BL_ArmatureObject` when the object
to mutate is an armature.

```python

# Move and turn the object with W and A. Run it every frame (Always sensor with True Pulse).
import Range

obj = Range.logic.getCurrentController().owner
keys = Range.logic.keyboard.events

if keys[Range.events.WKEY]:
    obj.applyMovement((0, 0.1, 0), True)
if keys[Range.events.AKEY]:
    obj.applyRotation((0, 0, 0.05), True)
```

```python

# Read and change game properties.
import Range

obj = Range.logic.getCurrentController().owner

obj["health"] = obj.get("health", 100) - 10

if obj["health"] <= 0:
    obj.endObject()
```

```python

# Look for the ground under the object.
import Range

obj = Range.logic.getCurrentController().owner
below = obj.worldPosition - obj.getAxisVect((0, 0, 1))

hit, point, normal = obj.rayCast(below, obj, 10.0)

if hit is not None:
    print(hit.name, point)
```

```python

# Chase the player when it comes close.
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

# Play the frames 1 to 30 of an action.
import Range

obj = Range.logic.getCurrentController().owner

if not obj.isPlayingAction():
    obj.playAction("Walk", 1, 30)
```

```python

# Attach the object to a hand, and release it later.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner

obj.setParent(scene.objects["Hand"])

# Later:
obj.removeParent()
```

Overview. The items are in the parts below:

- [attributes](KX_GameObject--props.md) (121 items)
- [methods and functions](KX_GameObject--funcs.md) (106 items)
