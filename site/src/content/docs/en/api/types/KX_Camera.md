---
title: "KX_Camera"
description: "Range.types.KX_Camera class reference"
---

Base class: [`KX_GameObject`](../kx_gameobject/)

:::tip[See also]
[`KX_Scene`](../../types/kx_scene/), [`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`KX_GameObject`](../../types/kx_gameobject/), [`Range.render`](../../modulos/render/)
:::



A Camera object.

### INSIDE

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

:::note
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

**Type:** 4x4 Matrix [[float]]

### projectionMatrixLeft

This camera's 4x4 left eye projection matrix.

:::note
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

**Type:** 4x4 Matrix [[float]]

### projectionMatrixRight

This camera's 4x4 right eye projection matrix.

:::note
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

**Type:** 4x4 Matrix [[float]]

### modelview_matrix

This camera's 4x4 model view matrix. (read-only).

**Type:** 4x4 Matrix [[float]]

:::note
This matrix is regenerated every frame from the camera's position and orientation. Also, this is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

### camera_to_world

This camera's camera to world transform. (read-only).

**Type:** 4x4 Matrix [[float]]

:::note
This matrix is regenerated every frame from the camera's position and orientation.
:::

### world_to_camera

This camera's world to camera transform. (read-only).

**Type:** 4x4 Matrix [[float]]

:::note
Regenerated every frame from the camera's position and orientation.
:::

:::note
This is camera_to_world inverted.
:::

### useViewport

True when the camera is used as a viewport, set True to enable a viewport for this camera.

**Type:** boolean

### sphereInsideFrustum(centre, radius)

Tests the given sphere against the view frustum.

- **`centre`**: The centre of the sphere (in world coordinates.)
  - type: list [x, y, z]
- **`radius`**: the radius of the sphere
  - type: float

**Returns:** `INSIDE`, `OUTSIDE` or `INTERSECT`

**Return type:** integer

:::note
When the camera is first initialized the result will be invalid because the projection matrix has not been set.
:::

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

- **`box`**: Eight (8) corner points of the box (in world coordinates.)
  - type: list of lists

**Returns:** `INSIDE`, `OUTSIDE` or `INTERSECT`

:::note
When the camera is first initialized the result will be invalid because the projection matrix has not been set.
:::

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

### pointInsideFrustum(point)

Tests the given point against the view frustum.

- **`point`**: The point to test (in world coordinates.)
  - type: 3D Vector

**Returns:** True if the given point is inside this camera's viewing frustum.

**Return type:** boolean

:::note
When the camera is first initialized the result will be invalid because the projection matrix has not been set.
:::

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

 <small>method</small>

Shakes the camera. `trauma` goes from 0 to 1 and adds to the World earthquake. With `duration`, the shake fades in that time; without it, it decreases at `shakeDecay` per second.

### cameraSpeed

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Current camera speed (units per second), used by speed-based effects.

### catEyeStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Strength of the "cat eye" bokeh of the depth of field (DOF), from 0.0 to 1.0: circles get flattened near the edges.

### chromaticStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Chromatic aberration strength, from 0.0 to 5.0.

### directionalBlurMax

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Directional blur limit (trail when turning the camera), from 0.0 to 0.2.

### directionalBlurStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Directional blur strength, from 0.0 to 2.0.

### dofBlur

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Maximum depth of field (DOF) blur size, from 0 to 32.

### dofQuality

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

DOF quality: 0 low, 1 medium, 2 high.

### droneAmplitude

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Sway amplitude of the Drone tracking mode (0 to 20).

### droneFrequency

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Sway frequency of the Drone mode (0 to 20).

### fisheyeStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Fisheye distortion, from -1.0 (pincushion) to 1.0 (barrel).

### focusDistance

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Focus distance used this frame, after smoothing.

### focusManualDistance

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Focus distance when `focusMode` is 0 (manual).

### focusMode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

How focus is chosen: 0 manual (`focusManualDistance`), 1 object (`focusObject`), 2 property (`focusProperty`), 3 automatic (ray at the screen point).

### focusObject

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Object in focus when `focusMode` is 1. `None` for none.

### focusPosition

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

World position of the focus point, or `None`.

### focusProperty

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Name of the game property used when `focusMode` is 2: focuses the closest object that has it true.

### focusRange

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Distance range around the focus that stays sharp.

### focusScreenPosition

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Screen position (0 to 1) of the focus point.

### focusSmooth

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Focus change smoothing, from 0 (instant) to 10.

### focusTarget

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Object in focus right now, or `None`.

### focusValid

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

`True` when focus found a target this frame.

### gazeDirection

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Direction the camera is looking at, in world space.

### shakeAmplitude

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Maximum shake amplitude (0 to 0.5).

### shakeDecay

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

How much the shake decreases per second (0 to 20).

### shakeFrequency

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Shake frequency (0 to 60).

### shakeTrauma

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Current shake trauma (0 to 1).

### speedBlurMaxSpeed

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Speed at which the speed blur reaches its maximum.

### speedBlurStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Speed blur strength, from 0.0 to 2.0.

### speedOverride

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Speed used by the effects instead of the real speed. -1 turns it off and goes back to the real one.

### trackBank

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Camera side tilt in tracking turns (0 to 5).

### trackDeadzone

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Tracking dead zone: the target can move within this screen margin without the camera turning (0 to 0.5).

### trackLimit

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Maximum angle, in radians, tracking can turn the camera.

### trackMode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Tracking mode: 0 off, 1 look at target, 2 drone.

### trackOrientation

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Orientation computed by tracking this frame.

### trackScreenOffset

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Target offset `[x, y]` on screen, from -0.5 to 0.5.

### trackSpeed

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

How fast the camera turns to the target (0 to 10).

### useBlurProtect

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Protects the center of the screen from blurs.

### useCatEye

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on cat eye bokeh in the DOF.

### useChromatic

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on chromatic aberration.

### useChromaticSpeed

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Makes chromatic aberration grow with speed.

### useDirectionalBlur

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on directional blur.

### useDof

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on depth of field (DOF).

### useShakeRoll

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

The shake also rolls the camera around the view axis.

### useSpeedBlur

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on speed blur.

### useTrackUpLock

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Keeps the camera "up" fixed during tracking.

### useVignette

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on the vignette (dark edges).

### vignetteRadius

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Vignette radius (0 to 2).

### vignetteStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Vignette strength (0 to 1).

