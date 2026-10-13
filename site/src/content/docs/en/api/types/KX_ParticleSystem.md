---
title: "KX_ParticleSystem"
description: "Range.types.KX_ParticleSystem class reference"
---

:::tip[See also]
[`KX_GameObject`](../../types/kx_gameobject/), [`KX_Scene`](../../types/kx_scene/)
:::

Class `Range.types.KX_ParticleSystem`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### burst()

 <small>method</small>

Releases all particles at once on the next frame. Only on emitters with `burstMode` on.

### billboardMode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

How particles face the camera: `'FULL'` or `'VERTICAL'` (rotates only on the vertical axis).

### blendMode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

How particles blend with the scene: `'ALPHA'` or `'ADDITIVE'`. An unknown value raises `ValueError`.

### burstInterval

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Interval in seconds between automatic bursts in burst mode.

### burstMode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

`True` emits in bursts (explosions); `False` emits continuously.

### collisionBounce

 <small>attribute</small>

How much a particle bounces when it hits (0 = no bounce).

### collisionFriction

 <small>attribute</small>

Particle friction when sliding after a hit.

### collisionHeight

 <small>attribute</small>

Ground plane height when `collisionMode` is 1.

### collisionMode

 <small>attribute</small>

Particle collision: 0 none, 1 ground plane, 2 with what is on screen (screen-space).

### color

 <small>attribute</small>

Initial particle color `[r, g, b, a]`.

### debugUI

 <small>attribute · read-only</small>

`True` when the particle system debug panel is open.

### drag

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Air resistance: how much particles slow down over time.

### emissionAngle

 <small>attribute</small>

Emission cone opening, in degrees.

### emissionDirection

 <small>attribute</small>

Direction `[x, y, z]` particles are emitted in.

### emissionMode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Emission mode: `'CONTINUOUS'` or `'BURST'` (all at once). `burstMode` follows this value.

### emitterPosition

 <small>attribute</small>

Emitter position `[x, y, z]` relative to the object.

### emitterRadius

 <small>attribute</small>

Radius of the area particles spawn from.

### enabled

 <small>attribute</small>

Turns emission on or off.

### endColor

 <small>attribute</small>

Particle color `[r, g, b, a]` at the end of its life (the color fades from `color` to it).

### endSize

 <small>attribute</small>

Particle size at the end of its life.

### fragmentShaderPath

 <small>attribute</small>

Path to your own `.glsl` to draw the particles. Empty goes back to the default look.

### gravity

 <small>attribute</small>

Gravity applied to particles.

### lifetime

 <small>attribute</small>

Lifetime of each particle, in seconds.

### particleCount

 <small>attribute</small>

Maximum number of live particles.

### size

 <small>attribute</small>

Initial particle size.

### texture

 <small>attribute</small>

Path of the image used on particles. Empty removes the texture.

### useBackfaceCulling

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Whether particles stop being drawn when seen from behind.

### useDebugUi

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Shows the emitter debug panel during the game.

### useVortex

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns on the vortex: particles rise spinning around the emitter.

### velocity

 <small>attribute</small>

Initial particle velocity.

### velocityRandomness

 <small>attribute</small>

Random variation of the initial velocity (0 = all the same).

### vortexHeight

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Vortex height.

### vortexRadiusTop

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Vortex radius at the top.

### vortexRotationSpeed

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Vortex rotation speed.

