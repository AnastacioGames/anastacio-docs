# KX_Camera

Base class: [`KX_GameObject`](KX_GameObject.md)

> **See also:**
[`KX_Scene`](KX_Scene.md), [`KX_2DFilterManager`](KX_2DFilterManager.md), [`KX_GameObject`](KX_GameObject.md), [`Range.render`](Range.render.md)

A Camera object.

```python

# Pick the object under the mouse.
import Range

scene = Range.logic.getCurrentScene()
x, y = Range.logic.mouse.position

hit = scene.active_camera.getScreenRay(x, y, 100.0)

if hit is not None:
    print(hit.name)
```

```python

# Check whether an object is inside the view of the camera.
import Range

scene = Range.logic.getCurrentScene()
cam = scene.active_camera
enemy = scene.objects["Enemy"]

if cam.sphereInsideFrustum(enemy.worldPosition, 1.0) != cam.OUTSIDE:
    print("Enemy on screen")
```

```python

# Shake the camera for half a second, as in an explosion.
import Range

cam = Range.logic.getCurrentScene().active_camera
cam.shake(0.8, 0.5)
```

```python

# Zoom in by closing the field of view.
import Range

cam = Range.logic.getCurrentScene().active_camera
cam.fov = 30.0
```

```python

# Split screen: this camera takes the left half of the window.
import Range

cam = Range.logic.getCurrentController().owner
width = Range.render.getWindowWidth()
height = Range.render.getWindowHeight()

cam.useViewport = True
cam.setViewport(0, 0, width // 2, height)
```

## INSIDE

See `sphereInsideFrustum` and `boxInsideFrustum`

### INTERSECT

See `sphereInsideFrustum` and `boxInsideFrustum`

### OUTSIDE

See `sphereInsideFrustum` and `boxInsideFrustum`

### lens

The camera's lens value.

**Type:** float

### lodDistanceFactor

The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

**Type:** float

### fov

The camera's field of view value.

**Type:** float

### ortho_scale

The camera's view scale when in orthographic mode.

**Type:** float

### near

The camera's near clip distance.

**Type:** float

### far

The camera's far clip distance.

**Type:** float

### shift_x

The camera's horizontal shift.

**Type:** float

### shift_y

The camera's vertical shift.

**Type:** float

### perspective

True if this camera has a perspective transform, False for an orthographic projection.

**Type:** boolean

### frustum_culling

True if this camera is frustum culling.

**Type:** boolean

### activityCulling

True if this camera is used to compute object distance for object activity culling.

**Type:** boolean

### projection_matrix

This camera's 4x4 projection matrix.

> **Note:**
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).

**Type:** 4x4 Matrix [[float]]

### projectionMatrixLeft

This camera's 4x4 left eye projection matrix.

> **Note:**
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).

**Type:** 4x4 Matrix [[float]]

### projectionMatrixRight

This camera's 4x4 right eye projection matrix.

> **Note:**
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).

**Type:** 4x4 Matrix [[float]]

### modelview_matrix

This camera's 4x4 model view matrix. (read-only).

**Type:** 4x4 Matrix [[float]]

> **Note:**
This matrix is regenerated every frame from the camera's position and orientation. Also, this is the identity matrix prior to rendering the first frame (any Python done on frame 1).

### camera_to_world

This camera's camera to world transform. (read-only).

**Type:** 4x4 Matrix [[float]]

> **Note:**
This matrix is regenerated every frame from the camera's position and orientation.

### world_to_camera

This camera's world to camera transform. (read-only).

**Type:** 4x4 Matrix [[float]]

> **Note:**
Regenerated every frame from the camera's position and orientation.

> **Note:**
This is camera_to_world inverted.

### useViewport

True when the camera is used as a viewport, set True to enable a viewport for this camera.

**Type:** boolean

### viewport

The viewport rectangle used for the last render of this camera, in pixels (read-only).
Ratios set in the editor are already resolved against the window.

**Type:** list [left, bottom, right, top]

### sphereInsideFrustum(centre, radius)

Tests the given sphere against the view frustum.

- **`centre`**: The centre of the sphere (in world coordinates.)
  - type: list [x, y, z]
- **`radius`**: the radius of the sphere
  - type: float

**Returns:** `INSIDE`, `OUTSIDE` or `INTERSECT`

**Return type:** integer

> **Note:**
When the camera is first initialized the result will be invalid because the projection matrix has not been set.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# A sphere of radius 4.0 located at [x, y, z] = [1.0, 1.0, 1.0]
if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
    # Sphere is inside frustum !
    # Do something useful !
else:
    # Sphere is outside frustum
```

### boxInsideFrustum(box)

Tests the given box against the view frustum.

- **`box`**: Eight (8) corner points of the box (in world coordinates), or a `KX_GameObject` to test its world bounding box.
  - type: list of lists or `KX_GameObject`

**Returns:** `INSIDE`, `OUTSIDE` or `INTERSECT`

> **Note:**
When the camera is first initialized the result will be invalid because the projection matrix has not been set.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Box to test...
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
  # Box is inside/intersects frustum !
  # Do something useful !
else:
  # Box is outside the frustum !
```

To test a game object, pass the object itself. It is the same as passing its world corners
from `getBoundBoxCorners`:

```python

if cam.boxInsideFrustum(obj) != cam.OUTSIDE:
    print(obj.name, "is visible (at least partly)")

# same result:
cam.boxInsideFrustum(obj.getBoundBoxCorners('WORLD'))
```

### pointInsideFrustum(point)

Tests the given point against the view frustum.

- **`point`**: The point to test (in world coordinates.)
  - type: 3D Vector

**Returns:** True if the given point is inside this camera's viewing frustum.

**Return type:** boolean

> **Note:**
When the camera is first initialized the result will be invalid because the projection matrix has not been set.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Test point [0.0, 0.0, 0.0]
if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
  # Point is inside frustum !
  # Do something useful !
else:
  # Box is outside the frustum !
```

### getCameraToWorld()

Returns the camera-to-world transform.

**Returns:** the camera-to-world transform matrix.

**Return type:** matrix (4x4 list)

### getWorldToCamera()

Returns the world-to-camera transform.

This returns the inverse matrix of getCameraToWorld().

**Returns:** the world-to-camera transform matrix.

**Return type:** matrix (4x4 list)

### setOnTop()

Set this cameras viewport ontop of all other viewport.

### setViewport(left, bottom, right, top)

Sets the region of this viewport on the screen in pixels.

Use `Range.render.getWindowHeight` and `Range.render.getWindowWidth` to calculate values relative to the entire display.

- **`left`**: left pixel coordinate of this viewport
  - type: integer
- **`bottom`**: bottom pixel coordinate of this viewport
  - type: integer
- **`right`**: right pixel coordinate of this viewport
  - type: integer
- **`top`**: top pixel coordinate of this viewport
  - type: integer

### getScreenPosition(object)

Gets the position of an object projected on screen space.

```python

# For an object in the middle of the screen, coord = [0.5, 0.5]
coord = camera.getScreenPosition(object)
```

- **`object`**: object name or list [x, y, z]
  - type: `KX_GameObject` or 3D Vector

**Returns:** the object's position in screen coordinates.

**Return type:** list [x, y]

### getScreenVect(x, y)

Gets the vector from the camera position in the screen coordinate direction.

- **`x`**: X Axis
  - type: float
- **`y`**: Y Axis
  - type: float

**Return type:** 3D Vector

**Returns:** The vector from screen coordinate.

```python

# Gets the vector of the camera front direction:
m_vect = camera.getScreenVect(0.5, 0.5)
```

### getScreenRay(x, y, dist, property="", xray=False, mask=0xFFFF)

Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop.
The ray is similar to KX_GameObject->rayCastTo.

- **`x`**: X Axis
  - type: float
- **`y`**: Y Axis
  - type: float
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
  - type: float
- **`property`**: property name that object must have; can be omitted => detect any object
  - type: string
- **`xray`**: the ray goes through objects without the property, like the X-Ray option of the Mouse sensor
  - type: boolean
- **`mask`**: collision mask, only objects of these collision groups are hit
  - type: bitfield

**Return type:** `KX_GameObject`

**Returns:** the first object hit or None if no object or object does not match prop

```python

# Gets an object with a property "wall" in front of the camera within a distance of 100:
target = camera.getScreenRay(0.5, 0.5, 100, "wall")
```

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### shake(trauma, duration=0.0)

 `method`

Shakes the camera. `trauma` goes from 0 to 1 and adds to the World earthquake. With `duration`, the shake fades in that time; without it, it decreases at `shakeDecay` per second.

### cameraSpeed

*(new in Anastacio)* `attribute · read-only`

Current camera speed (units per second), used by speed-based effects.

### catEyeStrength

*(new in Anastacio)* `attribute`

Strength of the "cat eye" bokeh of the depth of field (DOF), from 0.0 to 1.0: circles get flattened near the edges.

### chromaticStrength

*(new in Anastacio)* `attribute`

Chromatic aberration strength, from 0.0 to 5.0.

### directionalBlurMax

*(new in Anastacio)* `attribute`

Directional blur limit (trail when turning the camera), from 0.0 to 0.2.

### directionalBlurStrength

*(new in Anastacio)* `attribute`

Directional blur strength, from 0.0 to 2.0.

### dofBlur

*(new in Anastacio)* `attribute`

Maximum depth of field (DOF) blur size, from 0 to 32.

### dofQuality

*(new in Anastacio)* `attribute`

DOF quality: 0 low, 1 medium, 2 high.

### droneAmplitude

*(new in Anastacio)* `attribute`

Sway amplitude of the Drone tracking mode (0 to 20).

### droneFrequency

*(new in Anastacio)* `attribute`

Sway frequency of the Drone mode (0 to 20).

### fisheyeStrength

*(new in Anastacio)* `attribute`

Fisheye distortion, from -1.0 (pincushion) to 1.0 (barrel).

### focusDistance

*(new in Anastacio)* `attribute · read-only`

Focus distance used this frame, after smoothing.

### focusManualDistance

*(new in Anastacio)* `attribute`

Focus distance when `focusMode` is 0 (manual).

### focusMode

*(new in Anastacio)* `attribute`

How focus is chosen: 0 manual (`focusManualDistance`), 1 object (`focusObject`), 2 property (`focusProperty`), 3 automatic (ray at the screen point).

### focusObject

*(new in Anastacio)* `attribute`

Object in focus when `focusMode` is 1. `None` for none.

### focusPosition

*(new in Anastacio)* `attribute · read-only`

World position of the focus point, or `None`.

### focusProperty

*(new in Anastacio)* `attribute`

Name of the game property used when `focusMode` is 2: focuses the closest object that has it true.

### focusRange

*(new in Anastacio)* `attribute`

Distance range around the focus that stays sharp.

### focusScreenPosition

*(new in Anastacio)* `attribute · read-only`

Screen position (0 to 1) of the focus point.

### focusSmooth

*(new in Anastacio)* `attribute`

Focus change smoothing, from 0 (instant) to 10.

### focusTarget

*(new in Anastacio)* `attribute · read-only`

Object in focus right now, or `None`.

### focusValid

*(new in Anastacio)* `attribute · read-only`

`True` when focus found a target this frame.

### gazeDirection

*(new in Anastacio)* `attribute · read-only`

Direction the camera is looking at, in world space.

### shakeAmplitude

*(new in Anastacio)* `attribute`

Maximum shake amplitude (0 to 0.5).

### shakeDecay

*(new in Anastacio)* `attribute`

How much the shake decreases per second (0 to 20).

### shakeFrequency

*(new in Anastacio)* `attribute`

Shake frequency (0 to 60).

### shakeTrauma

*(new in Anastacio)* `attribute · read-only`

Current shake trauma (0 to 1).

### speedBlurMaxSpeed

*(new in Anastacio)* `attribute`

Speed at which the speed blur reaches its maximum.

### speedBlurStrength

*(new in Anastacio)* `attribute`

Speed blur strength, from 0.0 to 2.0.

### speedOverride

*(new in Anastacio)* `attribute`

Speed used by the effects instead of the real speed. -1 turns it off and goes back to the real one.

### trackBank

*(new in Anastacio)* `attribute`

Camera side tilt in tracking turns (0 to 5).

### trackDeadzone

*(new in Anastacio)* `attribute`

Tracking dead zone: the target can move within this screen margin without the camera turning (0 to 0.5).

### trackLimit

*(new in Anastacio)* `attribute`

Maximum angle, in radians, tracking can turn the camera.

### trackMode

*(new in Anastacio)* `attribute`

Tracking mode: 0 off, 1 look at target, 2 drone.

### trackOrientation

*(new in Anastacio)* `attribute · read-only`

Orientation computed by tracking this frame.

### trackScreenOffset

*(new in Anastacio)* `attribute`

Target offset `[x, y]` on screen, from -0.5 to 0.5.

### trackSpeed

*(new in Anastacio)* `attribute`

How fast the camera turns to the target (0 to 10).

### useBlurProtect

*(new in Anastacio)* `attribute`

Protects the center of the screen from blurs.

### useCatEye

*(new in Anastacio)* `attribute`

Turns on cat eye bokeh in the DOF.

### useChromatic

*(new in Anastacio)* `attribute`

Turns on chromatic aberration.

### useChromaticSpeed

*(new in Anastacio)* `attribute`

Makes chromatic aberration grow with speed.

### useDirectionalBlur

*(new in Anastacio)* `attribute`

Turns on directional blur.

### useDof

*(new in Anastacio)* `attribute`

Turns on depth of field (DOF).

### useShakeRoll

*(new in Anastacio)* `attribute`

The shake also rolls the camera around the view axis.

### useSpeedBlur

*(new in Anastacio)* `attribute`

Turns on speed blur.

### useTrackUpLock

*(new in Anastacio)* `attribute`

Keeps the camera "up" fixed during tracking.

### useVignette

*(new in Anastacio)* `attribute`

Turns on the vignette (dark edges).

### vignetteRadius

*(new in Anastacio)* `attribute`

Vignette radius (0 to 2).

### vignetteStrength

*(new in Anastacio)* `attribute`

Vignette strength (0 to 1).
