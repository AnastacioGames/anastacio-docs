---
title: "KX_GameObject"
description: "Referência da classe Range.types.KX_GameObject"
---

Classe base: [`SCA_IObject`](../sca_iobject/)



All game objects are derived from this class.

Properties assigned to game objects are accessible as attributes of this class.

:::note
Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError,
if an object may have been removed since last accessing it use the `invalid` attribute to check.
:::

KX_GameObject can be subclassed to extend functionality. For example:

``python

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
``

When subclassing objects other than empties and meshes, the specific type
should be used - e.g. inherit from `BL_ArmatureObject` when the object
to mutate is an armature.

### name

The object's name.

**Tipo:** string

### mass

The object's mass

**Tipo:** float

:::note
The object must have a physics controller for the mass to be applied, otherwise the mass value will be returned as 0.0.
:::

### friction

The object's friction

**Tipo:** float

### isSuspendDynamics

The object's dynamic state (read-only).

**Tipo:** boolean

:::tip
:py`suspendDynamics` and :py`restoreDynamics` allow you to change the state.
:::

### linearDamping

The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the :py`setDamping` method.

**Tipo:** float between 0 and 1 inclusive.

:::note
The object must have a physics controller for the linear damping to be applied, otherwise the value will be returned as 0.0.
:::

### angularDamping

The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the :py`setDamping` method.

**Tipo:** float between 0 and 1 inclusive.

:::note
The object must have a physics controller for the angular damping to be applied, otherwise the value will be returned as 0.0.
:::

### linVelocityMin

Enforces the object keeps moving at a minimum velocity.

**Tipo:** float

:::note
Applies to dynamic and rigid body objects only.
:::

:::note
A value of 0.0 disables this option.
:::

:::note
While objects are stationary the minimum velocity will not be applied.
:::

### linVelocityMax

Clamp the maximum linear velocity to prevent objects moving beyond a set speed.

**Tipo:** float

:::note
Applies to dynamic and rigid body objects only.
:::

:::note
A value of 0.0 disables this option (rather than setting it stationary).
:::

### angularVelocityMin

Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this.

**Tipo:** non-negative float

:::note
Applies to dynamic and rigid body objects only.
While objects are stationary the minimum velocity will not be applied.
:::

### angularVelocityMax

Clamp the maximum angular velocity to prevent objects rotating beyond a set speed.
A value of 0.0 disables clamping; it does not stop rotation.

**Tipo:** non-negative float

:::note
Applies to dynamic and rigid body objects only.
:::

### localInertia

the object's inertia vector in local coordinates. Read only.

**Tipo:** Vector((ix, iy, iz))

### parent

The object's parent object. (read-only).

**Tipo:** `KX_GameObject` or None

### groupMembers

Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned.

**Tipo:** `EXP_ListValue` of `KX_GameObject` or None

### groupObject

Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group.

**Tipo:** `KX_GameObject` or None

### collisionGroup

The object's collision group.

**Tipo:** bitfield

### collisionMask

The object's collision mask.

**Tipo:** bitfield

### collisionCallbacks

A list of functions to be called when a collision occurs.

**Tipo:** list of functions and/or methods

Callbacks should either accept one argument `(object)`, or four
arguments `(object, point, normal, points)`. For simplicity, per
colliding object the first collision point is reported in second
and third argument.

``python

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
``

:::note
For backward compatibility, a callback with variable number of
arguments (using `*args`) will be passed only the `object`
argument. Only when there is more than one fixed argument (not
counting `self` for methods) will the four-argument form be
used.
:::

### scene

The object's scene. (read-only).

**Tipo:** `KX_Scene` or None

### visible

visibility flag.

**Tipo:** boolean

:::note
Game logic will still run for invisible objects.
:::

### layer

The layer mask used for shadow and real-time cube map render.

**Tipo:** bitfield

### cullingBox

The object's bounding volume box used for culling.

**Tipo:** `KX_BoundingBox`

### culled

Returns True if the object is culled, else False.

:::caution
This variable returns an invalid value if it is called outside the scene's callbacks `KX_Scene.pre_draw` and `KX_Scene.post_draw`.
:::

**Tipo:** boolean (read only)

### color

The object color of the object. [r, g, b, a]

**Tipo:** `mathutils.Vector`

### occlusion

occlusion capability flag.

**Tipo:** boolean

### physicsCulling

True if the object suspends its physics depending on its nearest distance to any camera.

**Tipo:** boolean

### physicsCullingVelocity

Stop physics after the object stops.

**Tipo:** boolean

### logicCulling

True if the object suspends its logic and animation depending on its nearest distance to any camera.

**Tipo:** boolean

### logicCullingComponents

No Suspend execution of object components.

**Tipo:** boolean

### physicsCullingRadius

Suspend object's physics if this radius is smaller than its nearest distance to any camera
and `physicsCulling` set to `True`.

**Tipo:** float

### logicCullingRadius

Suspend object's logic and animation if this radius is smaller than its nearest distance to any camera
and `logicCulling` set to `True`.

**Tipo:** float

### position

The object's position. [x, y, z] On write: local position, on read: world position

:::danger[Obsoleto use `localPosition` and `worldPosition`.]

:::

**Tipo:** `mathutils.Vector`

### orientation

The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation

:::danger[Obsoleto use `localOrientation` and `worldOrientation`.]

:::

**Tipo:** `mathutils.Matrix`

### scaling

The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling

:::danger[Obsoleto use `localScale` and `worldScale`.]

:::

**Tipo:** `mathutils.Vector`

### localOrientation

The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.

**Tipo:** `mathutils.Matrix`

### worldOrientation

The object's world orientation. 3x3 Matrix.

**Tipo:** `mathutils.Matrix`

### localScale

The object's local scaling factor. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

### worldScale

The object's world scaling factor. [sx, sy, sz]

**Tipo:** `mathutils.Vector`

### localPosition

The object's local position. [x, y, z]

**Tipo:** `mathutils.Vector`

### worldPosition

The object's world position. [x, y, z]

**Tipo:** `mathutils.Vector`

### localTransform

The object's local space transform matrix. 4x4 Matrix.

**Tipo:** `mathutils.Matrix`

### worldTransform

The object's world space transform matrix. 4x4 Matrix.

**Tipo:** `mathutils.Matrix`

### localLinearVelocity

The object's local linear velocity. [x, y, z]

**Tipo:** `mathutils.Vector`

### worldLinearVelocity

The object's world linear velocity. [x, y, z]

**Tipo:** `mathutils.Vector`

### localAngularVelocity

The object's local angular velocity. [x, y, z]

**Tipo:** `mathutils.Vector`

### worldAngularVelocity

The object's world angular velocity. [x, y, z]

**Tipo:** `mathutils.Vector`

### gravity

The object's gravity. [x, y, z]

**Tipo:** `mathutils.Vector`

### timeOffset

adjust the slowparent delay at runtime.

**Tipo:** float

### state

the game object's state bitmask, using the first 30 bits, one bit must always be set.

**Tipo:** int

### meshes

a list meshes for this object.

**Tipo:** list of `KX_Mesh`

:::note
Most objects use only 1 mesh.
:::

:::note
Changes to this list will not update the KX_GameObject.
:::

### batchGroup

The object batch group containing the batched mesh.

**Tipo:** `KX_BatchGroup`

### sensors

a sequence of `SCA_ISensor` objects with string/index lookups and iterator support.

**Tipo:** list

:::note
This attribute is experimental and may be removed (but probably wont be).
:::

:::note
Changes to this list will not update the KX_GameObject.
:::

### controllers

a sequence of `SCA_IController` objects with string/index lookups and iterator support.

**Tipo:** list of `SCA_ISensor`

:::note
This attribute is experimental and may be removed (but probably wont be).
:::

:::note
Changes to this list will not update the KX_GameObject.
:::

### actuators

a list of `SCA_IActuator` with string/index lookups and iterator support.

**Tipo:** list

:::note
This attribute is experemental and may be removed (but probably wont be).
:::

:::note
Changes to this list will not update the KX_GameObject.
:::

### attrDict

get the objects internal python attribute dictionary for direct (faster) access.

**Tipo:** dict

### components

All python components.

**Tipo:** `EXP_ListValue` of `KX_PythonComponent`'s

### children

direct children of this object, (read-only).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

### childrenRecursive

all children of this object including children's children, (read-only).

**Tipo:** `EXP_ListValue` of `KX_GameObject`'s

### life

The number of frames until the object ends, assumes one frame is 1/50 second (read-only).

**Tipo:** float

### debug

If true, the object's debug properties will be displayed on screen.

**Tipo:** boolean

### debugRecursive

If true, the object's and children's debug properties will be displayed on screen.

**Tipo:** boolean

### currentLodLevel

The index of the level of detail (LOD) currently used by this object (read-only).

**Tipo:** int

### lodManager

Return the lod manager of this object.
Needed to access to lod manager to set attributes of levels of detail of this object.
The lod manager is shared between instance objects and can be changed to use the lod levels of an other object.
If the lod manager is set to `None` the object's mesh backs to the mesh of the previous first lod level.

**Tipo:** `KX_LodManager`

### isDestructible

True if Physics > Destruction is enabled on this object, also for objects on an inactive layer (read-only).

**Tipo:** boolean

### isExplosive

True if Physics > Explosive is enabled on this object, also for objects on an inactive layer (read-only).

**Tipo:** boolean

### breakImpulse

The impulse that breaks this destructible object, from a collision or from `KX_Scene.explode`.
Starts with the panel's Break Impulse; changing it affects only this instance.
Reads 0.0 on objects that are not destructible, and setting it on them raises AttributeError.

**Tipo:** float

### fuse

Seconds left before this explosive object detonates. The fuse counts from the moment the object enters
the game (scene start or `KX_Scene.addObject`). 0.0 means no fuse; setting a value lights it.
Setting it on an object that is not explosive raises AttributeError.

**Tipo:** float

### onBreak

A list of functions called when this object breaks, with the arguments `(object, fragments)`.
They run right after the fragments enter the scene, before any explosion pushes them.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Tipo:** list of functions and/or methods

``python

def on_break(obj, fragments):
    print('%s broke into %d pieces' % (obj.name, len(fragments)))

controller.owner.onBreak.append(on_break)
``

### onExplode

A list of functions called when this object explodes, with the arguments `(object, position)`.
On an object that is both destructible and explosive, they run after `onBreak`.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Tipo:** list of functions and/or methods

### onDent

A list of functions called when this deformable object dents (collision, explosion or

**meth:** `dent`), with the arguments `(object, point, impulse)`: world hit point (the blast center

for an explosion) and hit strength, e.g. to play a metal sound or spawn sparks there.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Tipo:** list of functions and/or methods

### endObject()

Delete this object, can be used in place of the EndObject Actuator.

The actual removal of the object from the scene is delayed.

### shatter(origin=None, burst=None)

Break this destructible object now, replacing it by the pieces of its Fragments group.
On an object that is also explosive, it detonates as well.

- **`origin`**: The point the pieces fly away from, the object's position by default.
  - tipo: 3D Vector
- **`burst`**: The speed given to the pieces away from origin, the panel's Burst Speed by default.
  - tipo: float

**Retorna:** The new pieces, an empty list if the object is not destructible or has already broken.

**Tipo do retorno:** list of `KX_GameObject`

### detonate()

Make this explosive object explode now: a blast like `KX_Scene.explode` with the panel's settings,
the Effect object, and the removal of the object. A destructible explosive breaks as well.

**Retorna:** False if the object is not explosive or has already exploded.

**Tipo do retorno:** boolean

### dent(point, direction, impulse)

Dent this deformable object (Deformation panel) as a hit of the given strength: the vertices within
the panel's Radius of point move along direction (into the object) by
(impulse - Dent Impulse) * Depth, limited by Max Depth. Only this instance changes, other objects
sharing the mesh keep their shape.

- **`point`**: hit point in world space.
  - tipo: 3D vector
- **`direction`**: hit direction in world space, flipped to point into the object.
  - tipo: 3D vector
- **`impulse`**: hit strength (N*s), compared with Dent Impulse.
  - tipo: float

**Retorna:** False if the object is not deformable, the impulse is too weak or no vertex moved.

**Tipo do retorno:** boolean

### resetDent()

Restore the shape of a dented object.

**Retorna:** False if the object was never dented.

**Tipo do retorno:** boolean

### replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False)

Replace the mesh of this object with a new mesh. This works the same was as the actuator.

- **`mesh`**: mesh to replace or the meshes name.
  - tipo: `MeshProxy` or string
- **`useDisplayMesh`**: when enabled the display mesh will be replaced (optional argument).
  - tipo: boolean
- **`usePhysicsMesh`**: when enabled the physics mesh will be replaced (optional argument).
  - tipo: boolean

### setVisible(visible[, recursive])

Sets the game object's visible flag.

- **`visible`**: the visible state to set.
  - tipo: boolean
- **`recursive`**: optional argument to set all childrens visibility flag too, defaults to False if no value passed.
  - tipo: boolean

### setOcclusion(occlusion[, recursive])

Sets the game object's occlusion capability.

- **`occlusion`**: the state to set the occlusion to.
  - tipo: boolean
- **`recursive`**: optional argument to set all childrens occlusion flag too, defaults to False if no value passed.
  - tipo: boolean

### alignAxisToVect(vect, axis=2, factor=1.0)

Aligns any of the game object's axis along the given vector.

- **`vect`**: a vector to align the axis.
  - tipo: 3D vector
- **`axis`**: The axis you want to align * 0: X axis * 1: Y axis * 2: Z axis
  - tipo: integer
- **`factor`**: Only rotate a feaction of the distance to the target vector (0.0 - 1.0)
  - tipo: float

### getAxisVect(vect)

Returns the axis vector rotates by the object's worldspace orientation.
This is the equivalent of multiplying the vector by the orientation matrix.

- **`vect`**: a vector to align the axis.
  - tipo: 3D Vector

**Retorna:** The vector in relation to the objects rotation.

**Tipo do retorno:** 3d vector.

### applyMovement(movement[, local])

Sets the game object's movement.

- **`movement`**: movement vector.
  - tipo: 3D Vector
- **`local`**:  * False: get the "global" movement ie: relative to world orientation. * True: get the "local" movement ie: relative to object orientation. Default to False if not passed.
- **`local`**: boolean

### applyRotation(rotation[, local])

Sets the game object's rotation.

- **`rotation`**: rotation vector.
  - tipo: 3D Vector
- **`local`**:  * False: get the "global" rotation ie: relative to world orientation. * True: get the "local" rotation ie: relative to object orientation. Default to False if not passed.
- **`local`**: boolean

### applyForce(force[, local])

Sets the game object's force.

This requires a dynamic object.

- **`force`**: force vector.
  - tipo: 3D Vector
- **`local`**:  * False: get the "global" force ie: relative to world orientation. * True: get the "local" force ie: relative to object orientation. Default to False if not passed.
  - tipo: boolean

### applyTorque(torque[, local])

Sets the game object's torque.

This requires a dynamic object.

- **`torque`**: torque vector.
  - tipo: 3D Vector
- **`local`**:  * False: get the "global" torque ie: relative to world orientation. * True: get the "local" torque ie: relative to object orientation. Default to False if not passed.
  - tipo: boolean

### getLinearVelocity([local])

Gets the game object's linear velocity.

This method returns the game object's velocity through it's center of mass, ie no angular velocity component.

- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - tipo: boolean

**Retorna:** the object's linear velocity.

**Tipo do retorno:** Vector((vx, vy, vz))

### setLinearVelocity(velocity[, local])

Sets the game object's linear velocity.

This method sets game object's velocity through it's center of mass,
ie no angular velocity component.

This requires a dynamic object.

- **`velocity`**: linear velocity vector.
  - tipo: 3D Vector
- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - tipo: boolean

### getAngularVelocity([local])

Gets the game object's angular velocity.

- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - tipo: boolean

**Retorna:** the object's angular velocity.

**Tipo do retorno:** Vector((vx, vy, vz))

### setAngularVelocity(velocity[, local])

Sets the game object's angular velocity.

This requires a dynamic object.

- **`velocity`**: angular velocity vector.
  - tipo: boolean
- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.

### getVelocity([point])

Gets the game object's velocity at the specified point.

Gets the game object's velocity at the specified point, including angular
components.

- **`point`**: optional point to return the velocity for, in local coordinates, defaults to (0, 0, 0) if no value passed.
  - tipo: 3D Vector

**Retorna:** the velocity at the specified point.

**Tipo do retorno:** Vector((vx, vy, vz))

### getReactionForce()

Gets the game object's reaction force.

The reaction force is the force applied to this object over the last simulation timestep.
This also includes impulses, eg from collisions.

**Retorna:** the reaction force of this object.

**Tipo do retorno:** Vector((fx, fy, fz))

:::note
This is not implimented at the moment.
:::

### applyImpulse(point, impulse[, local])

Applies an impulse to the game object.

This will apply the specified impulse to the game object at the specified point.
If point != position, applyImpulse will also change the object's angular momentum.
Otherwise, only linear momentum will change.

- **`point`**: the point to apply the impulse to (in world or local coordinates)
  - tipo: point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
- **`impulse`**: impulse vector.
  - tipo: 3D Vector
- **`local`**:  * False: get the "global" impulse ie: relative to world coordinates with world orientation. * True: get the "local" impulse ie: relative to local coordinates with object orientation. Default to False if not passed.
  - tipo: boolean

### setDamping(linear_damping, angular_damping)

Sets both the :py`linearDamping` and :py`angularDamping` simultaneously. This is more efficient than setting both properties individually.

- **`linear_damping`**: Linear ("translational") damping factor.
  - tipo: float ∈ [0, 1]
- **`angular_damping`**: Angular ("rotational") damping factor.
  - tipo: float ∈ [0, 1]

### suspendPhysics([freeConstraints])

Suspends physics for this object.

- **`freeConstraints`**: When set to `True` physics constraints used by the object are deleted. Else when `False` (the default) constraints are restored when restoring physics.
  - tipo: bool

### restorePhysics()

Resumes physics for this object. Also reinstates collisions.

### suspendDynamics([ghost])

Suspends dynamics physics for this object.

- **`ghost`**: When set to `True`, collisions with the object will be ignored, similar to the "ghost" checkbox in Blender. When `False` (the default), the object becomes static but still collide with other objects.
  - tipo: bool

:::tip
:py`isSuspendDynamics` allows you to inspect whether the object is in a suspended state.
:::

### restoreDynamics()

Resumes dynamics physics for this object. Also reinstates collisions; the object will no longer be a ghost.

:::note
The objects linear velocity will be applied from when the dynamics were suspended.
:::

### enableRigidBody()

Enables rigid body physics for this object.

Rigid body physics allows the object to roll on collisions.

### disableRigidBody()

Disables rigid body physics for this object.

### setParent(parent, compound=True, ghost=True)

Sets this object's parent.
Control the shape status with the optional compound and ghost parameters:

In that case you can control if it should be ghost or not:

- **`parent`**: new parent object.
  - tipo: `KX_GameObject`
- **`compound`**: whether the shape should be added to the parent compound shape. * True: the object shape should be added to the parent compound shape. * False: the object should keep its individual shape.
  - tipo: boolean
- **`ghost`**: whether the object should be ghost while parented. * True: if the object should be made ghost while parented. * False: if the object should be solid while parented.
  - tipo: boolean

:::note
If the object type is sensor, it stays ghost regardless of ghost parameter
:::

### removeParent()

Removes this objects parent.

### getPhysicsId()

Returns the user data object associated with this game object's physics controller.

### getPropertyNames()

Gets a list of all property names.

**Retorna:** All property names for this object.

**Tipo do retorno:** list

### getDistanceTo(other)

- **`other`**: a point or another `KX_GameObject` to measure the distance to.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** distance to another object or point.

**Tipo do retorno:** float

### getVectTo(other)

Returns the vector and the distance to another object or point.
The vector is normalized unless the distance is 0, in which a zero length vector is returned.

- **`other`**: a point or another `KX_GameObject` to get the vector and distance to.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** (distance, globalVector(3), localVector(3))

**Tipo do retorno:** 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))

### rayCastTo(other, dist=0, prop="")

Look towards another point/object and find first object hit within dist that matches prop.

The ray is always casted from the center of the object, ignoring the object itself.
The ray is casted towards the center of another object or an explicit [x, y, z] point.
Use rayCast() if you need to retrieve the hit point

- **`other`**: [x, y, z] or object towards which the ray is casted
  - tipo: `KX_GameObject` or 3-tuple
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
  - tipo: float
- **`prop`**: property name that object must have; can be omitted => detect any object
  - tipo: string

**Retorna:** the first object hit or None if no object or object does not match prop

**Tipo do retorno:** `KX_GameObject`

### rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF)

Look from a point/object to another point/object and find first object hit within dist that matches prop.
if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
if poly is 1, returns a 4-tuple with in addition a `KX_PolyProxy` as 4th element.
if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.

``python

# shoot along the axis gun-gunAim (gunAim should be collision-free)
obj, point, normal = gun.rayCast(gunAim, None, 50)
if obj:
   # do something
   pass
``

The face parameter determines the orientation of the normal.

* 0 => hit normal is always oriented towards the ray origin (as if you casted the ray from outside)
* 1 => hit normal is the real face normal (only for mesh object, otherwise face has no effect)

The ray has X-Ray capability if xray parameter is 1, otherwise the first object hit (other than self object) stops the ray.
The prop and xray parameters interact as follow.

* prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray.
* prop off, xray on : idem.
* prop on, xray off: return closest hit if it matches prop, no hit otherwise.
* prop on, xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray.

The `KX_PolyProxy` 4th element of the return tuple when poly=1 allows to retrieve information on the polygon hit by the ray.
If there is no hit or the hit object is not a static mesh, None is returned as 4th element.

The ray ignores collision-free objects and faces that dont have the collision flag enabled, you can however use ghost objects.

- **`objto`**: [x, y, z] or object to which the ray is casted
  - tipo: `KX_GameObject` or 3-tuple
- **`objfrom`**: [x, y, z] or object from which the ray is casted; None or omitted => use self object center
  - tipo: `KX_GameObject` or 3-tuple or None
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to to
  - tipo: float
- **`prop`**: property name that object must have; can be omitted or "" => detect any object
  - tipo: string
- **`face`**: normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
  - tipo: integer
- **`xray`**: X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
  - tipo: integer
- **`poly`**: polygon option: 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit. * 0 or omitted: return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit * 1: return value is a 4-tuple and the 4th element is a `KX_PolyProxy` or None if no hit or the object doesn't use a mesh collision shape. * 2: return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
  - tipo: integer
- **`mask`**: collision mask: The collision mask (16 layers mapped to a 16-bit integer) is combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.
  - tipo: bitfield

**Retorna:** (object, hitpoint, hitnormal) or (object, hitpoint, hitnormal, polygon) or (object, hitpoint, hitnormal, polygon, hituv). * object, hitpoint and hitnormal are None if no hit. * polygon is valid only if the object is valid and is a static object, a dynamic object using mesh collision shape or a soft body object, otherwise it is None * hituv is valid only if polygon is valid and the object has a UV mapping, otherwise it is None

**Tipo do retorno:**  * 3-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz)) * or 4-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`) * or 5-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`, 2-tuple (u, v))

:::note
The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points.
:::

### collide(obj)

Test if this object collides object `obj`.

- **`obj`**: the object to test collision with
  - tipo: string or `KX_GameObject`

**Retorna:** (collide, points) * collide, True if this object collides object `obj` * points, contact point data of the collision or None

**Tipo do retorno:** 2-tuple (boolean, list of `KX_CollisionContactPoint` or None)

### setCollisionMargin(margin)

Set the objects collision margin.

- **`margin`**: the collision margin distance in blender units.
  - tipo: float

:::note
If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError.
:::

### sendMessage(subject, body="", to="")

Sends a message.

- **`subject`**: The subject of the message
  - tipo: string
- **`body`**: The body of the message (optional)
  - tipo: string
- **`to`**: The name of the object to send the message to (optional)
  - tipo: string

### reinstancePhysicsMesh(gameObject, meshObject, dupli)

Updates the physics system with the changed mesh.

If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

- **`gameObject`**: optional argument, set the physics shape from this gameObjets mesh.
  - tipo: string, `KX_GameObject` or None
- **`meshObject`**: optional argument, set the physics shape from this mesh.
  - tipo: string, `MeshProxy` or None
- **`dupli`**: optional argument, duplicate the physics shape.
  - tipo: boolean

**Retorna:** True if reinstance succeeded, False if it failed.

**Tipo do retorno:** boolean

:::note
If this object has instances the other instances will be updated too.
:::

:::note
The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as the Subdivision Surface modifier).
:::

:::caution
Only triangle mesh and convex hull type objects are supported currently.
:::

:::caution
If the object is a part of a compound object it will fail (parent or child)
:::

:::caution
Rebuilding the physics mesh can be slow, running many times per second will give a performance hit.
:::

:::caution
Duplicate the physics mesh can use much more memory, use this option only for duplicated meshes else use :py`replacePhysicsShape`.
:::

### replacePhysicsShape(gameObject)

Replace the current physics shape.

- **`gameObject`**: set the physics shape from this gameObjets.
  - tipo: string, `KX_GameObject`

**Retorna:** True if replace succeeded, False if it failed.

**Tipo do retorno:** boolean

:::caution
Triangle mesh shapes are not supported.
:::

### get(key[, default])

Return the value matching key, or the default value if its not found.
- **`key`**: the matching key
  - tipo: string
- **`default`**: optional default value is the key isn't matching, defaults to None if no value passed.

**Retorna:** The key value or a default.

### playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=KX_ACTION_BLEND_BLEND)

Plays an action.

- **`name`**: the name of the action
  - tipo: string
- **`start`**: the start frame of the action
  - tipo: float
- **`end`**: the end frame of the action
  - tipo: float
- **`layer`**: the layer the action will play in (actions in different layers are added/blended together)
  - tipo: integer
- **`priority`**: only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
  - tipo: integer
- **`blendin`**: the amount of blending between this animation and the previous one on this layer
  - tipo: float
- **`play_mode`**: the play mode
  - tipo: one of `these constants`
- **`layer_weight`**: how much of the previous layer to use for blending
  - tipo: float
- **`ipo_flags`**: flags for the old IPO behaviors (force, etc)
  - tipo: int bitfield
- **`speed`**: the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
  - tipo: float
- **`blend_mode`**: how to blend this layer with previous layers
  - tipo: one of `these constants`

### stopAction([layer])

Stop playing the action on the given layer.

- **`layer`**: The layer to stop playing, defaults to 0 if no value passed.
  - tipo: integer

### getActionFrame([layer])

Gets the current frame of the action playing in the supplied layer.

- **`layer`**: The layer that you want to get the frame from, defaults to 0 if no value passed.
  - tipo: integer

**Retorna:** The current frame of the action

**Tipo do retorno:** float

### getActionName([layer])

Gets the name of the current action playing in the supplied layer.

- **`layer`**: The layer that you want to get the action name from, defaults to 0 if no value passed.
  - tipo: integer

**Retorna:** The name of the current action

**Tipo do retorno:** string

### setActionFrame(frame[, layer])

Set the current frame of the action playing in the supplied layer.

- **`layer`**: The layer where you want to set the frame, default to 0 if no value passed.
  - tipo: integer
- **`frame`**: The frame to set the action to
  - tipo: float

### isPlayingAction([layer])

Checks to see if there is an action playing in the given layer.

- **`layer`**: The layer to check for a playing action, defaults to 0 if no value passed.
  - tipo: integer

**Retorna:** Whether or not the action is playing

**Tipo do retorno:** boolean

### addDebugProperty (name[, debug])

Adds a single debug property to the debug list.

- **`name`**: name of the property that added to the debug list.
  - tipo: string
- **`debug`**: the debug state, default to True is no value passed.
  - tipo: boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getTurnTo()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getVehicle()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getVehicleGearboxType()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getVehicleGearRatios()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getVehicleMaxRPM()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getVehicleMaxTorque()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getVehicleSteeringWheel()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### lookAt()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### resumeAnimations()

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

### setActionLayerSpeed()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setActionLayerWeight()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setCcdMotionThreshold()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setCcdSweptSphereRadius()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setHalfAnimations()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftAnchorsHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftAngularStiffness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftClusterSolverIterations()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftContactsHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftDampingCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftDragCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftDriftSolverIterations()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftDynamicFrictionCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftKineticContactsHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftLiftCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftLinearStiffness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftPoseMatching()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftPoseMatchingCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftPositionSolverIterations()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftPressureCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftRigidContactsHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVelocitiesCorrectionFactor()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVelocitySolverIterations()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVolume()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVolumeConversationCoefficient()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVsKineticHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVsKineticImpulseSplitCluster()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVsRigidHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVsRigidImpulseSplitCluster()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVsSoftHardness()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setSoftVsSoftImpulseSplitCluster()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### strikeLightning(bolt=True)

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

a lightning strike now (rain must be on)

### suspendAnimations()

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

### activitycullingdistance

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### angularVelocity

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### animationEventManager

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### anisotropicFriction

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### anisotropicFrictionCoefficients

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### linearVelocity

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### parentRecursive

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### particles

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### passIndex

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

