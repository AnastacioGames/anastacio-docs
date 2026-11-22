# KX_GameObject - methods and functions

Part of [KX_GameObject](KX_GameObject.md).

## endObject()

Delete this object, can be used in place of the EndObject Actuator.

The actual removal of the object from the scene is delayed.

## shatter(origin=None, burst=None)

Break this destructible object now, replacing it by the pieces of its Fragments group.
On an object that is also explosive, it detonates as well.

- **`origin`**: The point the pieces fly away from, the object's position by default.
  - type: 3D Vector
- **`burst`**: The speed given to the pieces away from origin, the panel's Burst Speed by default.
  - type: float

**Returns:** The new pieces, an empty list if the object is not destructible or has already broken.

**Return type:** list of `KX_GameObject`

## detonate()

Make this explosive object explode now: a blast like `KX_Scene.explode` with the panel's settings,
the Effect object, and the removal of the object. A destructible explosive breaks as well.

**Returns:** False if the object is not explosive or has already exploded.

**Return type:** boolean

## dent(point, direction, impulse)

Dent this deformable object (Deformation panel) as a hit of the given strength: the vertices within
the panel's Radius of point move along direction (into the object) by
(impulse - Dent Impulse) * Depth, limited by Max Depth. Only this instance changes, other objects
sharing the mesh keep their shape.

- **`point`**: hit point in world space.
  - type: 3D vector
- **`direction`**: hit direction in world space, flipped to point into the object.
  - type: 3D vector
- **`impulse`**: hit strength (N*s), compared with Dent Impulse.
  - type: float

**Returns:** False if the object is not deformable, the impulse is too weak or no vertex moved.

**Return type:** boolean

## resetDent()

Restore the shape of a dented object.

**Returns:** False if the object was never dented.

**Return type:** boolean

## replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False)

Replace the mesh of this object with a new mesh. This works the same was as the actuator.

- **`mesh`**: mesh to replace or the meshes name.
  - type: `MeshProxy` or string
- **`useDisplayMesh`**: when enabled the display mesh will be replaced (optional argument).
  - type: boolean
- **`usePhysicsMesh`**: when enabled the physics mesh will be replaced (optional argument).
  - type: boolean

## setVisible(visible[, recursive])

Sets the game object's visible flag.

- **`visible`**: the visible state to set.
  - type: boolean
- **`recursive`**: optional argument to set all childrens visibility flag too, defaults to False if no value passed.
  - type: boolean

## setOcclusion(occlusion[, recursive])

Sets the game object's occlusion capability.

- **`occlusion`**: the state to set the occlusion to.
  - type: boolean
- **`recursive`**: optional argument to set all childrens occlusion flag too, defaults to False if no value passed.
  - type: boolean

## alignAxisToVect(vect, axis=2, factor=1.0)

Aligns any of the game object's axis along the given vector.

- **`vect`**: a vector to align the axis.
  - type: 3D vector
- **`axis`**: The axis you want to align * 0: X axis * 1: Y axis * 2: Z axis
  - type: integer
- **`factor`**: Only rotate a feaction of the distance to the target vector (0.0 - 1.0)
  - type: float

## getAxisVect(vect)

Returns the axis vector rotates by the object's worldspace orientation.
This is the equivalent of multiplying the vector by the orientation matrix.

- **`vect`**: a vector to align the axis.
  - type: 3D Vector

**Returns:** The vector in relation to the objects rotation.

**Return type:** 3d vector.

## applyMovement(movement[, local])

Sets the game object's movement.

- **`movement`**: movement vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" movement ie: relative to world orientation. * True: get the "local" movement ie: relative to object orientation. Default to False if not passed.
- **`local`**: boolean

## applyRotation(rotation[, local])

Sets the game object's rotation.

- **`rotation`**: rotation vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" rotation ie: relative to world orientation. * True: get the "local" rotation ie: relative to object orientation. Default to False if not passed.
- **`local`**: boolean

## applyForce(force[, local])

Sets the game object's force.

This requires a dynamic object.

- **`force`**: force vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" force ie: relative to world orientation. * True: get the "local" force ie: relative to object orientation. Default to False if not passed.
  - type: boolean

## applyTorque(torque[, local])

Sets the game object's torque.

This requires a dynamic object.

- **`torque`**: torque vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" torque ie: relative to world orientation. * True: get the "local" torque ie: relative to object orientation. Default to False if not passed.
  - type: boolean

## getLinearVelocity([local])

Gets the game object's linear velocity.

This method returns the game object's velocity through it's center of mass, ie no angular velocity component.

- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - type: boolean

**Returns:** the object's linear velocity.

**Return type:** Vector((vx, vy, vz))

## setLinearVelocity(velocity[, local])

Sets the game object's linear velocity.

This method sets game object's velocity through it's center of mass,
ie no angular velocity component.

This requires a dynamic object.

- **`velocity`**: linear velocity vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - type: boolean

## getAngularVelocity([local])

Gets the game object's angular velocity.

- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - type: boolean

**Returns:** the object's angular velocity.

**Return type:** Vector((vx, vy, vz))

## setAngularVelocity(velocity[, local])

Sets the game object's angular velocity.

This requires a dynamic object.

- **`velocity`**: angular velocity vector.
  - type: boolean
- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.

## getVelocity([point])

Gets the game object's velocity at the specified point.

Gets the game object's velocity at the specified point, including angular
components.

- **`point`**: optional point to return the velocity for, in local coordinates, defaults to (0, 0, 0) if no value passed.
  - type: 3D Vector

**Returns:** the velocity at the specified point.

**Return type:** Vector((vx, vy, vz))

## getReactionForce()

Gets the game object's reaction force.

The reaction force is the force applied to this object over the last simulation timestep.
This also includes impulses, eg from collisions.

**Returns:** the reaction force of this object.

**Return type:** Vector((fx, fy, fz))

> **Note:**
This is not implimented at the moment.

## applyImpulse(point, impulse[, local])

Applies an impulse to the game object.

This will apply the specified impulse to the game object at the specified point.
If point != position, applyImpulse will also change the object's angular momentum.
Otherwise, only linear momentum will change.

- **`point`**: the point to apply the impulse to (in world or local coordinates)
  - type: point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
- **`impulse`**: impulse vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" impulse ie: relative to world coordinates with world orientation. * True: get the "local" impulse ie: relative to local coordinates with object orientation. Default to False if not passed.
  - type: boolean

## setDamping(linear_damping, angular_damping)

Sets both the :py`linearDamping` and :py`angularDamping` simultaneously. This is more efficient than setting both properties individually.

- **`linear_damping`**: Linear ("translational") damping factor.
  - type: float ∈ [0, 1]
- **`angular_damping`**: Angular ("rotational") damping factor.
  - type: float ∈ [0, 1]

## suspendPhysics([freeConstraints])

Suspends physics for this object.

- **`freeConstraints`**: When set to `True` physics constraints used by the object are deleted. Else when `False` (the default) constraints are restored when restoring physics.
  - type: bool

## restorePhysics()

Resumes physics for this object. Also reinstates collisions.

## suspendDynamics([ghost])

Suspends dynamics physics for this object.

- **`ghost`**: When set to `True`, collisions with the object will be ignored, similar to the "ghost" checkbox in Blender. When `False` (the default), the object becomes static but still collide with other objects.
  - type: bool

> **Tip:**
:py:attr:`isSuspendDynamics` allows you to inspect whether the object is in a suspended state.

## restoreDynamics()

Resumes dynamics physics for this object. Also reinstates collisions; the object will no longer be a ghost.

> **Note:**
The objects linear velocity will be applied from when the dynamics were suspended.

## enableRigidBody()

Enables rigid body physics for this object.

Rigid body physics allows the object to roll on collisions.

## disableRigidBody()

Disables rigid body physics for this object.

## setParent(parent, compound=True, ghost=True)

Sets this object's parent.
Control the shape status with the optional compound and ghost parameters:

In that case you can control if it should be ghost or not:

- **`parent`**: new parent object.
  - type: `KX_GameObject`
- **`compound`**: whether the shape should be added to the parent compound shape. * True: the object shape should be added to the parent compound shape. * False: the object should keep its individual shape.
  - type: boolean
- **`ghost`**: whether the object should be ghost while parented. * True: if the object should be made ghost while parented. * False: if the object should be solid while parented.
  - type: boolean

> **Note:**
If the object type is sensor, it stays ghost regardless of ghost parameter

## removeParent()

Removes this objects parent.

## getPhysicsId()

Returns the user data object associated with this game object's physics controller.

## getPropertyNames()

Gets a list of all property names.

**Returns:** All property names for this object.

**Return type:** list

## getBoundBoxSize()

Size of the bounding box (`cullingBox`) along the object's own axes, with its world scale.

**Returns:** width, depth and height.

**Return type:** `mathutils.Vector`

## getBoundBoxCorners(space='WORLD')

The 8 corners of the bounding box. Corner `i` uses the max X when bit 0 is set, max Y for bit 1
and max Z for bit 2, so `[0]` is the minimum corner and `[7]` the maximum one.

- **`space`**: `'WORLD'` (positions in the world), `'OFFSET'` (from `worldPosition`, with rotation and scale) or `'LOCAL'` (object space, without scale).
  - type: string

**Return type:** list of `mathutils.Vector`

The `'WORLD'` corners can be passed straight to
`boxInsideFrustum` to test if the object is in the camera view.

## getBoundBoxVolume()

Compatibility with Range 1.x scripts: returns `[volume, corner1, ..., corner8]`. The volume uses
the world scale and the corners are the `'OFFSET'` ones of `getBoundBoxCorners`, so
`obj.worldPosition + box[i]` is a corner in the world.

**Return type:** list

## getDistanceTo(other)

- **`other`**: a point or another `KX_GameObject` to measure the distance to.
  - type: `KX_GameObject` or list [x, y, z]

**Returns:** distance to another object or point.

**Return type:** float

## getVectTo(other)

Returns the vector and the distance to another object or point.
The vector is normalized unless the distance is 0, in which a zero length vector is returned.

- **`other`**: a point or another `KX_GameObject` to get the vector and distance to.
  - type: `KX_GameObject` or list [x, y, z]

**Returns:** (distance, globalVector(3), localVector(3))

**Return type:** 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))

## rayCastTo(other, dist=0, prop="")

Look towards another point/object and find first object hit within dist that matches prop.

The ray is always casted from the center of the object, ignoring the object itself.
The ray is casted towards the center of another object or an explicit [x, y, z] point.
Use rayCast() if you need to retrieve the hit point

- **`other`**: [x, y, z] or object towards which the ray is casted
  - type: `KX_GameObject` or 3-tuple
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
  - type: float
- **`prop`**: property name that object must have; can be omitted => detect any object
  - type: string

**Returns:** the first object hit or None if no object or object does not match prop

**Return type:** `KX_GameObject`

## rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF)

Look from a point/object to another point/object and find first object hit within dist that matches prop.
if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
if poly is 1, returns a 4-tuple with in addition a `KX_PolyProxy` as 4th element.
if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.

```python

# shoot along the axis gun-gunAim (gunAim should be collision-free)
obj, point, normal = gun.rayCast(gunAim, None, 50)
if obj:
   # do something
   pass
```

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
  - type: `KX_GameObject` or 3-tuple
- **`objfrom`**: [x, y, z] or object from which the ray is casted; None or omitted => use self object center
  - type: `KX_GameObject` or 3-tuple or None
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to to
  - type: float
- **`prop`**: property name that object must have; can be omitted or "" => detect any object
  - type: string
- **`face`**: normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
  - type: integer
- **`xray`**: X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
  - type: integer
- **`poly`**: polygon option: 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit. * 0 or omitted: return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit * 1: return value is a 4-tuple and the 4th element is a `KX_PolyProxy` or None if no hit or the object doesn't use a mesh collision shape. * 2: return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
  - type: integer
- **`mask`**: collision mask: The collision mask (16 layers mapped to a 16-bit integer) is combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.
  - type: bitfield

**Returns:** (object, hitpoint, hitnormal) or (object, hitpoint, hitnormal, polygon) or (object, hitpoint, hitnormal, polygon, hituv). * object, hitpoint and hitnormal are None if no hit. * polygon is valid only if the object is valid and is a static object, a dynamic object using mesh collision shape or a soft body object, otherwise it is None * hituv is valid only if polygon is valid and the object has a UV mapping, otherwise it is None

**Return type:**  * 3-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz)) * or 4-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`) * or 5-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`, 2-tuple (u, v))

> **Note:**
The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points.

## collide(obj)

Test if this object collides object `obj`.

- **`obj`**: the object to test collision with
  - type: string or `KX_GameObject`

**Returns:** (collide, points) * collide, True if this object collides object `obj` * points, contact point data of the collision or None

**Return type:** 2-tuple (boolean, list of `KX_CollisionContactPoint` or None)

## setCollisionMargin(margin)

Set the objects collision margin.

- **`margin`**: the collision margin distance in blender units.
  - type: float

> **Note:**
If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError.

## sendMessage(subject, body="", to="")

Sends a message.

- **`subject`**: The subject of the message
  - type: string
- **`body`**: The body of the message (optional)
  - type: string
- **`to`**: The name of the object to send the message to (optional)
  - type: string

## reinstancePhysicsMesh(gameObject, meshObject, dupli)

Updates the physics system with the changed mesh.

If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

- **`gameObject`**: optional argument, set the physics shape from this gameObjets mesh.
  - type: string, `KX_GameObject` or None
- **`meshObject`**: optional argument, set the physics shape from this mesh.
  - type: string, `MeshProxy` or None
- **`dupli`**: optional argument, duplicate the physics shape.
  - type: boolean

**Returns:** True if reinstance succeeded, False if it failed.

**Return type:** boolean

> **Note:**
If this object has instances the other instances will be updated too.

> **Note:**
The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as the Subdivision Surface modifier).

> **Caution:**
Only triangle mesh and convex hull type objects are supported currently.

> **Caution:**
If the object is a part of a compound object it will fail (parent or child)

> **Caution:**
Rebuilding the physics mesh can be slow, running many times per second will give a performance hit.

> **Caution:**
Duplicate the physics mesh can use much more memory, use this option only for duplicated meshes else use :py`replacePhysicsShape`.

## replacePhysicsShape(gameObject)

Replace the current physics shape.

- **`gameObject`**: set the physics shape from this gameObjets.
  - type: string, `KX_GameObject`

**Returns:** True if replace succeeded, False if it failed.

**Return type:** boolean

> **Caution:**
Triangle mesh shapes are not supported.

## get(key[, default])

Return the value matching key, or the default value if its not found.
- **`key`**: the matching key
  - type: string
- **`default`**: optional default value is the key isn't matching, defaults to None if no value passed.

**Returns:** The key value or a default.

## playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=KX_ACTION_BLEND_BLEND)

Plays an action.

- **`name`**: the name of the action
  - type: string
- **`start`**: the start frame of the action
  - type: float
- **`end`**: the end frame of the action
  - type: float
- **`layer`**: the layer the action will play in (actions in different layers are added/blended together)
  - type: integer
- **`priority`**: only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
  - type: integer
- **`blendin`**: the amount of blending between this animation and the previous one on this layer
  - type: float
- **`play_mode`**: the play mode
  - type: one of `these constants`
- **`layer_weight`**: how much of the previous layer to use for blending
  - type: float
- **`ipo_flags`**: flags for the old IPO behaviors (force, etc)
  - type: int bitfield
- **`speed`**: the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
  - type: float
- **`blend_mode`**: how to blend this layer with previous layers
  - type: one of `these constants`

## stopAction([layer])

Stop playing the action on the given layer.

- **`layer`**: The layer to stop playing, defaults to 0 if no value passed.
  - type: integer

## getActionFrame([layer])

Gets the current frame of the action playing in the supplied layer.

- **`layer`**: The layer that you want to get the frame from, defaults to 0 if no value passed.
  - type: integer

**Returns:** The current frame of the action

**Return type:** float

## getActionName([layer])

Gets the name of the current action playing in the supplied layer.

- **`layer`**: The layer that you want to get the action name from, defaults to 0 if no value passed.
  - type: integer

**Returns:** The name of the current action

**Return type:** string

## setActionFrame(frame[, layer])

Set the current frame of the action playing in the supplied layer.

- **`layer`**: The layer where you want to set the frame, default to 0 if no value passed.
  - type: integer
- **`frame`**: The frame to set the action to
  - type: float

## isPlayingAction([layer])

Checks to see if there is an action playing in the given layer.

- **`layer`**: The layer to check for a playing action, defaults to 0 if no value passed.
  - type: integer

**Returns:** Whether or not the action is playing

**Return type:** boolean

## playNLA(speed=1.0, loop=True)

Plays the NLA tracks of an armature, like the NLA Editor does. Muted tracks and strips are skipped,
Solo is respected and the tracks are blended from the bottom up (Replace and Add, influence, blend
in/out, repeat, scale, reverse and extrapolation). Actions played with `playAction` are
blended on top of the NLA result.

Calling it again while the NLA is playing with the same arguments keeps it going, so it can be
called every frame.

Not supported yet: transition and meta strips, Subtract/Multiply modes (played as Replace),
strip time curves and NLA on objects that are not armatures.

- **`speed`**: Playback speed (1.0 = scene animation frame rate, 0.0 = stopped, use `setNLAFrame`; negative plays backwards from the last frame).
  - type: float
- **`loop`**: Restart from the first strip after the last one ends, else hold the last frame.
  - type: boolean

**Returns:** True when the NLA started (the object is an armature with at least one strip).

**Return type:** boolean

## stopNLA()

Stops the NLA playback. The armature keeps its current pose.

## isPlayingNLA()

**Returns:** True while the NLA is playing (False after a non-looping NLA reached its end).

**Return type:** boolean

## getNLAFrame()

**Returns:** The current NLA frame.

**Return type:** float

## setNLAFrame(frame)

Jumps the NLA to the given frame, clamped to the range of the strips.

- **`frame`**: The NLA frame.
  - type: float

## addDebugProperty (name[, debug])

Adds a single debug property to the debug list.

- **`name`**: name of the property that added to the debug list.
  - type: string
- **`debug`**: the debug state, default to True is no value passed.
  - type: boolean

## getCurvePoints()

 `method`

`getCurvePoints(world=True)`: points of the first spline of a Curve object, as a list of `Vector`. World space by default; `world=False` returns local space. Empty list if the object is not a curve.

## getTurnTo(other)

 `method`

Local vector from this object to another object or point. Useful to know which way to turn.

**Returns:** `Vector`

## getVehicle()

*(new in Anastacio)* `method`

The vehicle created by this object's Vehicle panel, or `None`.

**Returns:** `KX_VehicleWrapper`

## getVehicleGearboxType()

*(new in Anastacio)* `method`

Gearbox type set in the Vehicle panel.

**Returns:** `int`

## getVehicleGearRatios()

*(new in Anastacio)* `method`

Gear ratios set in the Vehicle panel.

**Returns:** `tuple`

## getVehicleMaxRPM()

*(new in Anastacio)* `method`

Maximum engine RPM set in the Vehicle panel.

**Returns:** `float`

## getVehicleMaxTorque()

*(new in Anastacio)* `method`

Maximum engine torque set in the Vehicle panel.

**Returns:** `float`

## getVehicleSteeringWheel()

*(new in Anastacio)* `method`

Steering wheel object set in the Vehicle panel, or `None`.

**Returns:** `KX_GameObject`

## is_playing_take()

 `method`

`True` while a Rec Play take moves this object.

**Returns:** `bool`

## lookAt(vect, axis=2, factor=1.0)

*(new in Anastacio)* `method`

Turns the object so its `axis` (0=X, 1=Y, 2=Z) points along `vect`. A `factor` below 1 turns only part of the way (smoothing).

## play_take(name)

 `method`

Plays what a Rec Play take recorded of this object. `False` if it recorded nothing of it.

**Returns:** `bool`

## resumeAnimations()

*(new in Anastacio)* `method`

Resumes the animations paused by `suspendAnimations()`.

## setActionLayerSpeed(layer, speed)

 `method`

Changes the speed of the action playing on layer `layer`.

## setActionLayerWeight(layer, layerWeight)

 `method`

Changes the weight (0 to 1) of animation layer `layer`.

## setCcdMotionThreshold(threshold)

*(new in Anastacio)* `method`

Speed above which continuous collision detection (CCD) kicks in, so fast objects don't pass through walls.

## setCcdSweptSphereRadius(radius)

*(new in Anastacio)* `method`

Radius of the sphere used by continuous collision detection (CCD).

## setHalfAnimations(enabled)

*(new in Anastacio)* `method`

With `True`, updates the object animations every other frame to save CPU.

## setSoftAnchorsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: anchor hardness.

## setSoftAngularStiffness(value)

*(new in Anastacio)* `method`

Soft body physics: angular stiffness.

## setSoftClusterSolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: cluster solver iterations.

## setSoftContactsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: contact hardness.

## setSoftDampingCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: damping.

## setSoftDragCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: air drag.

## setSoftDriftSolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: drift solver iterations.

## setSoftDynamicFrictionCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: dynamic friction.

## setSoftKineticContactsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness of contact with kinematic objects.

## setSoftLiftCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: lift.

## setSoftLinearStiffness(value)

*(new in Anastacio)* `method`

Soft body physics: linear stiffness.

## setSoftPoseMatching(enabled)

*(new in Anastacio)* `method`

Soft body physics: tries to go back to the original shape.

## setSoftPoseMatchingCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: how strongly it goes back to the original shape.

## setSoftPositionSolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: position solver iterations.

## setSoftPressureCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: internal pressure (balloon effect).

## setSoftRigidContactsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness of contact with rigid bodies.

## setSoftVelocitiesCorrectionFactor(value)

*(new in Anastacio)* `method`

Soft body physics: velocity correction factor.

## setSoftVelocitySolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: velocity solver iterations.

## setSoftVolume(volume)

*(new in Anastacio)* `method`

Soft body physics: volume the body tries to keep.

## setSoftVolumeConversationCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: volume conservation.

## setSoftVsKineticHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness against kinematic bodies (clusters).

## setSoftVsKineticImpulseSplitCluster(value)

*(new in Anastacio)* `method`

Soft body physics: impulse split against kinematic bodies (clusters).

## setSoftVsRigidHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness against rigid bodies (clusters).

## setSoftVsRigidImpulseSplitCluster(value)

*(new in Anastacio)* `method`

Soft body physics: impulse split against rigid bodies (clusters).

## setSoftVsSoftHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness against other soft bodies (clusters).

## setSoftVsSoftImpulseSplitCluster(value)

*(new in Anastacio)* `method`

Soft body physics: impulse split against other soft bodies (clusters).

## setVehicleGearRatios(ratios)

*(new in Anastacio)* `method`

Replaces the vehicle gear ratios. Takes a list of numbers, one per gear.

## setVehicleMaxRPM(value)

*(new in Anastacio)* `method`

Changes the maximum engine RPM of the vehicle at runtime (number >= 0).

## setVehicleMaxTorque(value)

*(new in Anastacio)* `method`

Changes the maximum engine torque of this object's vehicle at runtime (number >= 0).

## stop_take()

 `method`

Stops the take of this object and gives it back to its logic and physics.

## strikeLightning(bolt=True)

 `method`

a lightning strike now (rain must be on)

## suspendAnimations()

*(new in Anastacio)* `method`

Pauses all object animations until `resumeAnimations()`.
