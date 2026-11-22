# KX_GameObject - attributes

Part of [KX_GameObject](KX_GameObject.md).

## name

The object's name.

**Type:** string

## mass

The object's mass

**Type:** float

> **Note:**
The object must have a physics controller for the mass to be applied, otherwise the mass value will be returned as 0.0.

## friction

The object's friction

**Type:** float

## isSuspendDynamics

The object's dynamic state (read-only).

**Type:** boolean

> **Tip:**
:py:meth:`suspendDynamics` and :py:meth:`restoreDynamics` allow you to change the state.

## linearDamping

The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the :py`setDamping` method.

**Type:** float between 0 and 1 inclusive.

> **Note:**
The object must have a physics controller for the linear damping to be applied, otherwise the value will be returned as 0.0.

## angularDamping

The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the :py`setDamping` method.

**Type:** float between 0 and 1 inclusive.

> **Note:**
The object must have a physics controller for the angular damping to be applied, otherwise the value will be returned as 0.0.

## linVelocityMin

Enforces the object keeps moving at a minimum velocity.

**Type:** float

> **Note:**
Applies to dynamic and rigid body objects only.

> **Note:**
A value of 0.0 disables this option.

> **Note:**
While objects are stationary the minimum velocity will not be applied.

## linVelocityMax

Clamp the maximum linear velocity to prevent objects moving beyond a set speed.

**Type:** float

> **Note:**
Applies to dynamic and rigid body objects only.

> **Note:**
A value of 0.0 disables this option (rather than setting it stationary).

## angularVelocityMin

Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this.

**Type:** non-negative float

> **Note:**
Applies to dynamic and rigid body objects only.
While objects are stationary the minimum velocity will not be applied.

## angularVelocityMax

Clamp the maximum angular velocity to prevent objects rotating beyond a set speed.
A value of 0.0 disables clamping; it does not stop rotation.

**Type:** non-negative float

> **Note:**
Applies to dynamic and rigid body objects only.

## localInertia

the object's inertia vector in local coordinates. Read only.

**Type:** Vector((ix, iy, iz))

## parent

The object's parent object. (read-only).

**Type:** `KX_GameObject` or None

## groupMembers

Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned.

**Type:** `EXP_ListValue` of `KX_GameObject` or None

## groupObject

Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group.

**Type:** `KX_GameObject` or None

## collisionGroup

The object's collision group.

**Type:** bitfield

## collisionMask

The object's collision mask.

**Type:** bitfield

## collisionCallbacks

A list of functions to be called when a collision occurs.

**Type:** list of functions and/or methods

Callbacks should either accept one argument `(object)`, or four
arguments `(object, point, normal, points)`. For simplicity, per
colliding object the first collision point is reported in second
and third argument.

```python

# Function form
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

# Method form
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
For backward compatibility, a callback with variable number of
arguments (using `*args`) will be passed only the `object`
argument. Only when there is more than one fixed argument (not
counting `self` for methods) will the four-argument form be
used.

## scene

The object's scene. (read-only).

**Type:** `KX_Scene` or None

## visible

visibility flag.

**Type:** boolean

> **Note:**
Game logic will still run for invisible objects.

## layer

The layer mask used for shadow and real-time cube map render.

**Type:** bitfield

## cullingBox

The object's bounding volume box used for culling.

**Type:** `KX_BoundingBox`

## culled

Returns True if the object is culled, else False.

> **Caution:**
This variable returns an invalid value if it is called outside the scene's callbacks `KX_Scene.pre_draw` and `KX_Scene.post_draw`.

**Type:** boolean (read only)

## color

The object color of the object. [r, g, b, a]

**Type:** `mathutils.Vector`

## occlusion

occlusion capability flag.

**Type:** boolean

## physicsCulling

True if the object suspends its physics depending on its nearest distance to any camera.

**Type:** boolean

## physicsCullingVelocity

Stop physics after the object stops.

**Type:** boolean

## logicCulling

True if the object suspends its logic and animation depending on its nearest distance to any camera.

**Type:** boolean

## logicCullingComponents

No Suspend execution of object components.

**Type:** boolean

## physicsCullingRadius

Suspend object's physics if this radius is smaller than its nearest distance to any camera
and `physicsCulling` set to `True`.

**Type:** float

## logicCullingRadius

Suspend object's logic and animation if this radius is smaller than its nearest distance to any camera
and `logicCulling` set to `True`.

**Type:** float

## ~~position~~

The object's position. [x, y, z] On write: local position, on read: world position

> **Deprecated use :data:`localPosition` and :data:`worldPosition`.:**

**Type:** `mathutils.Vector`

## ~~orientation~~

The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation

> **Deprecated use :data:`localOrientation` and :data:`worldOrientation`.:**

**Type:** `mathutils.Matrix`

## ~~scaling~~

The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling

> **Deprecated use :data:`localScale` and :data:`worldScale`.:**

**Type:** `mathutils.Vector`

## localOrientation

The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.

**Type:** `mathutils.Matrix`

## worldOrientation

The object's world orientation. 3x3 Matrix.

**Type:** `mathutils.Matrix`

## localScale

The object's local scaling factor. [sx, sy, sz]

**Type:** `mathutils.Vector`

## worldScale

The object's world scaling factor. [sx, sy, sz]

**Type:** `mathutils.Vector`

## localPosition

The object's local position. [x, y, z]

**Type:** `mathutils.Vector`

## worldPosition

The object's world position. [x, y, z]

**Type:** `mathutils.Vector`

## localTransform

The object's local space transform matrix. 4x4 Matrix.

**Type:** `mathutils.Matrix`

## worldTransform

The object's world space transform matrix. 4x4 Matrix.

**Type:** `mathutils.Matrix`

## localLinearVelocity

The object's local linear velocity. [x, y, z]

**Type:** `mathutils.Vector`

## worldLinearVelocity

The object's world linear velocity. [x, y, z]

**Type:** `mathutils.Vector`

## localAngularVelocity

The object's local angular velocity. [x, y, z]

**Type:** `mathutils.Vector`

## worldAngularVelocity

The object's world angular velocity. [x, y, z]

**Type:** `mathutils.Vector`

## gravity

The object's gravity. [x, y, z]

**Type:** `mathutils.Vector`

## timeOffset

adjust the slowparent delay at runtime.

**Type:** float

## state

the game object's state bitmask, using the first 30 bits, one bit must always be set.

**Type:** int

## meshes

a list meshes for this object.

**Type:** list of `KX_Mesh`

> **Note:**
Most objects use only 1 mesh.

> **Note:**
Changes to this list will not update the KX_GameObject.

## batchGroup

The object batch group containing the batched mesh.

**Type:** `KX_BatchGroup`

## sensors

a sequence of `SCA_ISensor` objects with string/index lookups and iterator support.

**Type:** list

> **Note:**
This attribute is experimental and may be removed (but probably wont be).

> **Note:**
Changes to this list will not update the KX_GameObject.

## controllers

a sequence of `SCA_IController` objects with string/index lookups and iterator support.

**Type:** list of `SCA_ISensor`

> **Note:**
This attribute is experimental and may be removed (but probably wont be).

> **Note:**
Changes to this list will not update the KX_GameObject.

## actuators

a list of `SCA_IActuator` with string/index lookups and iterator support.

**Type:** list

> **Note:**
This attribute is experemental and may be removed (but probably wont be).

> **Note:**
Changes to this list will not update the KX_GameObject.

## attrDict

get the objects internal python attribute dictionary for direct (faster) access.

**Type:** dict

## components

All python components.

**Type:** `EXP_ListValue` of `KX_PythonComponent`'s

## children

direct children of this object, (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`'s

## childrenRecursive

all children of this object including children's children, (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`'s

## life

The number of frames until the object ends, assumes one frame is 1/50 second (read-only).

**Type:** float

## debug

If true, the object's debug properties will be displayed on screen.

**Type:** boolean

## debugRecursive

If true, the object's and children's debug properties will be displayed on screen.

**Type:** boolean

## currentLodLevel

The index of the level of detail (LOD) currently used by this object (read-only).

**Type:** int

## lodLevelMax

Highest level of detail (LOD) index this object may switch to; -1 (default) means no limit. Farther levels
are skipped while it is set, e.g. a ragdoll character keeps a mesh level instead of a sitting impostor card.

**Type:** int (-1 to 255)

## lodManager

Return the lod manager of this object.
Needed to access to lod manager to set attributes of levels of detail of this object.
The lod manager is shared between instance objects and can be changed to use the lod levels of an other object.
If the lod manager is set to `None` the object's mesh backs to the mesh of the previous first lod level.

**Type:** `KX_LodManager`

## isDestructible

True if Physics > Destruction is enabled on this object, also for objects on an inactive layer (read-only).

**Type:** boolean

## isExplosive

True if Physics > Explosive is enabled on this object, also for objects on an inactive layer (read-only).

**Type:** boolean

## breakImpulse

The impulse that breaks this destructible object, from a collision or from `KX_Scene.explode`.
Starts with the panel's Break Impulse; changing it affects only this instance.
Reads 0.0 on objects that are not destructible, and setting it on them raises AttributeError.

**Type:** float

## fuse

Seconds left before this explosive object detonates. The fuse counts from the moment the object enters
the game (scene start or `KX_Scene.addObject`). 0.0 means no fuse; setting a value lights it.
Setting it on an object that is not explosive raises AttributeError.

**Type:** float

## explosionRadius

Radius of the blast of this explosive object, in meters. Like every attribute of the
Explosive panel below, setting it on an object that is not explosive raises AttributeError.

**Type:** float

## explosionForce

Impulse of the blast at its center; it falls to 0 at `explosionRadius`.

**Type:** float

## upBias

Extra upward push of the blast (0 to 5), so objects fly up instead of sliding on the floor.

**Type:** float

## useOcclusion

Static geometry between the blast and an object shields it.

**Type:** bool

## explosionEffect

Object of an inactive layer added at the blast (fire, smoke, a sound). It must be an object of the scene file.

**Type:** `KX_GameObject` or None

## effectLife

Seconds `explosionEffect` lives (0 = until its own logic removes it).

**Type:** float

## useParticleExplosion

Built-in GPU particle explosion (core, smoke and debris) at the blast.

**Type:** bool

## particleSize

Size preset of the particle explosion: `'TINY'`, `'SMALL'`, `'MEDIUM'`, `'LARGE'` or `'HUGE'`.
It also scales the ground mark.

**Type:** str

## particleStyle

What the particle explosion is made of: `'FIRE'`, `'ELECTRIC'`, `'CONCRETE'` or `'WATER'`.
Setting it resets `fireColor`, `smokeColor` and `sparkColor` to the colors of the style.

**Type:** str

## fireColor

Tint of the core of the particle explosion (white = the natural colors of the style).

**Type:** Vector((r, g, b))

## smokeColor

Color of the smoke (dust cloud, mist) of the particle explosion when it is born.

**Type:** Vector((r, g, b))

## sparkColor

Color of the sparks (debris, droplets) of the particle explosion.

**Type:** Vector((r, g, b))

## fireAmount

How many core particles, relative to the size preset (0 to 4, 0 = none).

**Type:** float

## smokeAmount

How much smoke, relative to the size preset (0 to 4, 0 = none).

**Type:** float

## sparkAmount

How many sparks, relative to the size preset (0 to 4, 0 = none).

**Type:** float

## smokeDuration

How long the smoke lasts, relative to the style (0.2 to 4).

**Type:** float

## blastSpeed

How hard the particles are thrown out, relative to the size preset (0.2 to 4).

**Type:** float

## useGroundMark

Paint the material of `groundMark` on the static surface under the blast.

**Type:** bool

## useMarkNearby

With `useGroundMark`: also paint a smaller mark on the objects around the blast (12 closest).

**Type:** bool

## groundMark

Mesh object of an inactive layer whose material is the ground mark. It must be an object of the scene file.

**Type:** `KX_GameObject` or None

## markSize

Size of the ground mark, relative to `particleSize` (0.1 to 4).

**Type:** float

## markLife

Seconds the ground mark stays (0 = forever).

**Type:** float

## onBreak

A list of functions called when this object breaks, with the arguments `(object, fragments)`.
They run right after the fragments enter the scene, before any explosion pushes them.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Type:** list of functions and/or methods

```python

def on_break(obj, fragments):
    print('%s broke into %d pieces' % (obj.name, len(fragments)))

controller.owner.onBreak.append(on_break)
```

## onExplode

A list of functions called when this object explodes, with the arguments `(object, position)`.
On an object that is both destructible and explosive, they run after `onBreak`.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Type:** list of functions and/or methods

## onDent

A list of functions called when this deformable object dents (collision, explosion or
`dent`), with the arguments `(object, point, impulse)`: world hit point (the blast center
for an explosion) and hit strength, e.g. to play a metal sound or spawn sparks there.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Type:** list of functions and/or methods

## activitycullingdistance

*(new in Anastacio)* `attribute · read-only`

Distance from this object to the camera, computed by Activity Culling.

## angularVelocity

*(new in Anastacio)* `attribute`

Angular velocity. Read in local coordinates, written in world coordinates.

## animationEventManager

*(new in Anastacio)* `attribute · read-only`

Manager of the object animation events (`KX_AnimationEventManager`).

## anisotropicFriction

*(new in Anastacio)* `attribute`

Turns on per-axis (anisotropic) friction.

## anisotropicFrictionCoefficients

*(new in Anastacio)* `attribute`

Friction `[x, y, z]` on each axis when `anisotropicFriction` is on.

## bendAngle

*(new in Anastacio)* `attribute`

How much the object bends on each impact.

## bendAxis

*(new in Anastacio)* `attribute`

Axis the object bends on: `'X'`, `'Y'` or `'Z'`.

## bendMaxAngle

*(new in Anastacio)* `attribute`

Maximum angle the object can bend.

## burstSpeed

*(new in Anastacio)* `attribute`

Speed at which fragments fly out when the object breaks.

## debrisLifetime

*(new in Anastacio)* `attribute`

Lifetime of the fragments after breaking.

## decal

*(new in Anastacio)* `attribute`

Object used as a scratch decal on collisions, or `None`. It must be an object in the scene file.

## decalLife

*(new in Anastacio)* `attribute`

Lifetime of each decal.

## decalSize

*(new in Anastacio)* `attribute`

Decal size.

## dentImpulse

*(new in Anastacio)* `attribute`

Minimum collision impulse to dent the object.

## fragments

*(new in Anastacio)* `attribute`

Name of the group with the fragments used when the object breaks, or `None`. Only on destructible objects; otherwise raises `AttributeError`.

## hiddenFromCamera

*(new in Anastacio)* `attribute`

Camera that must not show this object (e.g. your own car in split screen), or `None`.

## impactImpulse

*(new in Anastacio)* `attribute`

Minimum collision impulse for an explosive object to detonate.

## isDeformable

*(new in Anastacio)* `attribute · read-only`

`True` if the object has the deformation settings on (dent, bend, decals).

## linearVelocity

*(new in Anastacio)* `attribute`

Linear velocity. Read in local coordinates, written in world coordinates.

## maxDecals

*(new in Anastacio)* `attribute`

Maximum number of decals on this object at the same time.

## parentRecursive

*(new in Anastacio)* `attribute · read-only`

List of all parents above the object, from closest to farthest.

## particles

*(new in Anastacio)* `attribute · read-only`

Object particle system (`KX_ParticleSystem`), or `None`.

## particlesMix

*(new in Anastacio)* `attribute · read-only`

Second (mix) particle system of the object, or `None`.

## passIndex

*(new in Anastacio)* `attribute`

Object Pass Index, used to separate objects in filters and effects.

## useBreakOnCollision

*(new in Anastacio)* `attribute`

Whether the object breaks on collision.

## useChainReaction

*(new in Anastacio)* `attribute`

Whether this object explosion detonates other explosives nearby.

## useDentOnCollision

*(new in Anastacio)* `attribute`

Whether the object dents on collision.

## useExplodeOnImpact

*(new in Anastacio)* `attribute`

Whether the explosive object detonates on an impact above `impactImpulse`.

## useInheritVelocity

*(new in Anastacio)* `attribute`

Whether fragments inherit the object velocity when it breaks.
