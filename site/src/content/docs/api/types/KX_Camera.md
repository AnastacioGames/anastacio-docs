---
title: "KX_Camera"
description: "Referência da classe Range.types.KX_Camera"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



A Camera object.

### INSIDE

See `sphereInsideFrustum` and `boxInsideFrustum`

### INTERSECT

See `sphereInsideFrustum` and `boxInsideFrustum`

### OUTSIDE

See `sphereInsideFrustum` and `boxInsideFrustum`

### lens

The camera's lens value.

**Tipo:** float

### lodDistanceFactor

The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

**Tipo:** float

### fov

The camera's field of view value.

**Tipo:** float

### ortho_scale

The camera's view scale when in orthographic mode.

**Tipo:** float

### near

The camera's near clip distance.

**Tipo:** float

### far

The camera's far clip distance.

**Tipo:** float

### shift_x

The camera's horizontal shift.

**Tipo:** float

### shift_y

The camera's vertical shift.

**Tipo:** float

### perspective

True if this camera has a perspective transform, False for an orthographic projection.

**Tipo:** boolean

### frustum_culling

True if this camera is frustum culling.

**Tipo:** boolean

### activityCulling

True if this camera is used to compute object distance for object activity culling.

**Tipo:** boolean

### projection_matrix

This camera's 4x4 projection matrix.

:::note
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

**Tipo:** 4x4 Matrix [[float]]

### projectionMatrixLeft

This camera's 4x4 left eye projection matrix.

:::note
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

**Tipo:** 4x4 Matrix [[float]]

### projectionMatrixRight

This camera's 4x4 right eye projection matrix.

:::note
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

**Tipo:** 4x4 Matrix [[float]]

### modelview_matrix

This camera's 4x4 model view matrix. (read-only).

**Tipo:** 4x4 Matrix [[float]]

:::note
This matrix is regenerated every frame from the camera's position and orientation. Also, this is the identity matrix prior to rendering the first frame (any Python done on frame 1).
:::

### camera_to_world

This camera's camera to world transform. (read-only).

**Tipo:** 4x4 Matrix [[float]]

:::note
This matrix is regenerated every frame from the camera's position and orientation.
:::

### world_to_camera

This camera's world to camera transform. (read-only).

**Tipo:** 4x4 Matrix [[float]]

:::note
Regenerated every frame from the camera's position and orientation.
:::

:::note
This is camera_to_world inverted.
:::

### useViewport

True when the camera is used as a viewport, set True to enable a viewport for this camera.

**Tipo:** boolean

### sphereInsideFrustum(centre, radius)

Tests the given sphere against the view frustum.

- **`centre`**: The centre of the sphere (in world coordinates.)
  - tipo: list [x, y, z]
- **`radius`**: the radius of the sphere
  - tipo: float

**Retorna:** `INSIDE`, `OUTSIDE` or `INTERSECT`

**Tipo do retorno:** integer

:::note
When the camera is first initialized the result will be invalid because the projection matrix has not been set.
:::

``python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# A sphere of radius 4.0 located at [x, y, z] = [1.0, 1.0, 1.0]
if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
    # Sphere is inside frustum !
    # Do something useful !
else:
    # Sphere is outside frustum
``

### boxInsideFrustum(box)

Tests the given box against the view frustum.

- **`box`**: Eight (8) corner points of the box (in world coordinates.)
  - tipo: list of lists

**Retorna:** `INSIDE`, `OUTSIDE` or `INTERSECT`

:::note
When the camera is first initialized the result will be invalid because the projection matrix has not been set.
:::

``python

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
``

### pointInsideFrustum(point)

Tests the given point against the view frustum.

- **`point`**: The point to test (in world coordinates.)
  - tipo: 3D Vector

**Retorna:** True if the given point is inside this camera's viewing frustum.

**Tipo do retorno:** boolean

:::note
When the camera is first initialized the result will be invalid because the projection matrix has not been set.
:::

``python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Test point [0.0, 0.0, 0.0]
if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
  # Point is inside frustum !
  # Do something useful !
else:
  # Box is outside the frustum !
``

### getCameraToWorld()

Returns the camera-to-world transform.

**Retorna:** the camera-to-world transform matrix.

**Tipo do retorno:** matrix (4x4 list)

### getWorldToCamera()

Returns the world-to-camera transform.

This returns the inverse matrix of getCameraToWorld().

**Retorna:** the world-to-camera transform matrix.

**Tipo do retorno:** matrix (4x4 list)

### setOnTop()

Set this cameras viewport ontop of all other viewport.

### setViewport(left, bottom, right, top)

Sets the region of this viewport on the screen in pixels.

Use `Range.render.getWindowHeight` and `Range.render.getWindowWidth` to calculate values relative to the entire display.

- **`left`**: left pixel coordinate of this viewport
  - tipo: integer
- **`bottom`**: bottom pixel coordinate of this viewport
  - tipo: integer
- **`right`**: right pixel coordinate of this viewport
  - tipo: integer
- **`top`**: top pixel coordinate of this viewport
  - tipo: integer

### getScreenPosition(object)

Gets the position of an object projected on screen space.

``python

# For an object in the middle of the screen, coord = [0.5, 0.5]
coord = camera.getScreenPosition(object)
``

- **`object`**: object name or list [x, y, z]
  - tipo: `KX_GameObject` or 3D Vector

**Retorna:** the object's position in screen coordinates.

**Tipo do retorno:** list [x, y]

### getScreenVect(x, y)

Gets the vector from the camera position in the screen coordinate direction.

- **`x`**: X Axis
  - tipo: float
- **`y`**: Y Axis
  - tipo: float

**Tipo do retorno:** 3D Vector

**Retorna:** The vector from screen coordinate.

``python

# Gets the vector of the camera front direction:
m_vect = camera.getScreenVect(0.5, 0.5)
``

### getScreenRay(x, y, dist=inf, property=None)

Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop.
The ray is similar to KX_GameObject->rayCastTo.

- **`x`**: X Axis
  - tipo: float
- **`y`**: Y Axis
  - tipo: float
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
  - tipo: float
- **`property`**: property name that object must have; can be omitted => detect any object
  - tipo: string

**Tipo do retorno:** `KX_GameObject`

**Retorna:** the first object hit or None if no object or object does not match prop

``python

# Gets an object with a property "wall" in front of the camera within a distance of 100:
target = camera.getScreenRay(0.5, 0.5, 100, "wall")
``

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### shake()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### cameraSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### catEyeStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### chromaticStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### directionalBlurMax

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### directionalBlurStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### dofBlur

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### dofQuality

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### droneAmplitude

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### droneFrequency

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### fisheyeStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusDistance

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### focusManualDistance

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusObject

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusPosition

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### focusProperty

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusRange

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusScreenPosition

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### focusSmooth

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### focusTarget

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### focusValid

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### gazeDirection

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### shakeAmplitude

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### shakeDecay

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### shakeFrequency

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### shakeTrauma

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### speedBlurMaxSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### speedBlurStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### speedOverride

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### trackBank

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### trackDeadzone

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### trackLimit

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### trackMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### trackOrientation

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### trackScreenOffset

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### trackSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useBlurProtect

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useCatEye

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useChromatic

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useChromaticSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useDirectionalBlur

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useDof

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useShakeRoll

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useSpeedBlur

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useTrackUpLock

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### useVignette

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### vignetteRadius

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### vignetteStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

