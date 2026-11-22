# KX_ParticleSystem

> **See also:**
[`KX_GameObject`](KX_GameObject.md), [`KX_Scene`](KX_Scene.md)

Class `Range.types.KX_ParticleSystem`.

```python
# Change the fire of the object while the game runs.
import Range

own = Range.logic.getCurrentController().owner
particles = own.particles

if particles is not None:
    particles.particleCount = 200
    particles.lifetime = 1.5
    particles.blendMode = "ADDITIVE"
```

```python
# A single explosion.
import Range

particles = Range.logic.getCurrentController().owner.particles

particles.emissionMode = "BURST"
particles.burst()
```

```python
# Stop emitting.
import Range

particles = Range.logic.getCurrentController().owner.particles
particles.enabled = False
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### burst()

 `method`

Releases all particles at once on the next frame. Only on emitters with `burstMode` on.

### billboardMode

*(new in Anastacio)* `attribute`

How particles face the camera: `'FULL'` or `'VERTICAL'` (rotates only on the vertical axis).

### blendMode

*(new in Anastacio)* `attribute`

How particles blend with the scene: `'ALPHA'` or `'ADDITIVE'`. An unknown value raises `ValueError`.

### burstInterval

*(new in Anastacio)* `attribute`

Interval in seconds between automatic bursts in burst mode.

### burstMode

*(new in Anastacio)* `attribute`

`True` emits in bursts (explosions); `False` emits continuously.

### collisionBounce

 `attribute`

How much a particle bounces when it hits (0 = no bounce).

### collisionFriction

 `attribute`

Particle friction when sliding after a hit.

### collisionHeight

 `attribute`

Ground plane height when `collisionMode` is 1.

### collisionMode

 `attribute`

Particle collision: 0 none, 1 ground plane, 2 with what is on screen (screen-space).

### color

 `attribute`

Initial particle color `[r, g, b, a]`.

### debugUI

 `attribute · read-only`

`True` when the particle system debug panel is open.

### drag

*(new in Anastacio)* `attribute`

Air resistance: how much particles slow down over time.

### emissionAngle

 `attribute`

Emission cone opening, in degrees.

### emissionDirection

 `attribute`

Direction `[x, y, z]` particles are emitted in.

### emissionMode

*(new in Anastacio)* `attribute`

Emission mode: `'CONTINUOUS'` or `'BURST'` (all at once). `burstMode` follows this value.

### emitterPosition

 `attribute`

Emitter position `[x, y, z]` relative to the object.

### emitterRadius

 `attribute`

Radius of the area particles spawn from.

### enabled

 `attribute`

Turns emission on or off.

### endColor

 `attribute`

Particle color `[r, g, b, a]` at the end of its life (the color fades from `color` to it).

### endSize

 `attribute`

Particle size at the end of its life.

### flipbook

*(new in Anastacio)* `attribute`

Flipbook animation of the particle texture, as a `(columns, rows, cycles, random)` tuple. When assigning, `cycles` (default 1.0) and `random` (default `False`) are optional: `ps.flipbook = (4, 4)`.

### fragmentShaderPath

 `attribute`

Path to your own `.glsl` to draw the particles. Empty goes back to the default look.

### gravity

 `attribute`

Gravity applied to particles.

### lifetime

 `attribute`

Lifetime of each particle, in seconds.

### particleCount

 `attribute`

Maximum number of live particles.

### size

 `attribute`

Initial particle size.

### texture

 `attribute`

Path of the image used on particles. Empty removes the texture.

### useBackfaceCulling

*(new in Anastacio)* `attribute`

Whether particles stop being drawn when seen from behind.

### useDebugUi

*(new in Anastacio)* `attribute`

Shows the emitter debug panel during the game.

### useObjectRotation

*(new in Anastacio)* `attribute`

`True` makes gravity, velocity, direction, offset and the vortex axis follow the owner object rotation.

### useVortex

*(new in Anastacio)* `attribute`

Turns on the vortex: particles rise spinning around the emitter.

### velocity

 `attribute`

Initial particle velocity.

### velocityRandomness

 `attribute`

Random variation of the initial velocity (0 = all the same).

### vortexHeight

*(new in Anastacio)* `attribute`

Vortex height.

### vortexRadiusTop

*(new in Anastacio)* `attribute`

Vortex radius at the top.

### vortexRotationSpeed

*(new in Anastacio)* `attribute`

Vortex rotation speed.
