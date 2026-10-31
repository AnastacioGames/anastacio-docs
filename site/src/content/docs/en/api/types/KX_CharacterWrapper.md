---
title: "KX_CharacterWrapper"
description: "Range.types.KX_CharacterWrapper class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`KX_GameObject`](../../types/kx_gameobject/), [`Range.constraints`](../../modulos/constraints/)
:::



A wrapper to expose character physics options.

:::note
When the character's object is removed, every method and attribute of the wrapper raises
`ReferenceError`. Suspending physics keeps the character, so the wrapper still works.
:::

### onGround

Whether or not the character is on the ground. (read-only)

**Type:** boolean

### gravity

The gravity value used for the character.

**Type:** float

### fallSpeed

The character falling speed.

**Type:** float

### maxJumps

The maximum number of jumps a character can perform before having to touch the ground. By default this is set to 1. 2 allows for a double jump, etc.

**Type:** int in [0, 255], default 1

### jumpCount

The current jump count. This can be used to have different logic for a single jump versus a double jump. For example, a different animation for the second jump.

**Type:** int

### jumpSpeed

The character jumping speed.

**Type:** float

### maxSlope

The maximum slope which the character can climb.

**Type:** float

### walkDirection

The speed and direction the character is traveling in using world coordinates. This should be used instead of applyMovement() to properly move the character.

**Type:** Vector((x, y, z))

### jump()

The character jumps based on it's jump speed.

### jumpDirection

The direction the character is jumping.

**Type:** Vector((x, y, z))

### setVelocity(velocity, time, local=False)

Sets the character's linear velocity for a given period.

This method sets character's velocity through it's center of mass during a period.

- **`velocity`**: Linear velocity vector.
  - type: 3D Vector
- **`time`**: Period while applying linear velocity.
  - type: float
- **`local`**:  * False: you get the "global" velocity ie: relative to world orientation. * True: you get the "local" velocity ie: relative to object orientation.
  - type: boolean

### smoothMovement

Smooth movement caused by walking direction.

**Type:** float (0.0 to 1.0)

### posture

Current posture (the collision shape in use). Setting it asks for a new posture;
standing up waits until there is room above the character (see `canStand`).

**Type:** string, one of `'STAND'`, `'CROUCH'`, `'CRAWL'`, `'JUMP_TUCK'`

### canStand

True when there is room to stand up from the current posture.

**Type:** boolean (read-only)

### running

Run mode: while True the character walks with the object's Run Speed factor.

**Type:** boolean

### reset()

Resets the character velocity and walk direction.

