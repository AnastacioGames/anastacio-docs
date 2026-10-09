---
title: "KX_CharacterWrapper"
description: "Referência da classe Range.types.KX_CharacterWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A wrapper to expose character physics options.

### onGround

Whether or not the character is on the ground. (read-only)

**Tipo:** boolean

### gravity

The gravity value used for the character.

**Tipo:** float

### fallSpeed

The character falling speed.

**Tipo:** float

### maxJumps

The maximum number of jumps a character can perform before having to touch the ground. By default this is set to 1. 2 allows for a double jump, etc.

**Tipo:** int in [0, 255], default 1

### jumpCount

The current jump count. This can be used to have different logic for a single jump versus a double jump. For example, a different animation for the second jump.

**Tipo:** int

### jumpSpeed

The character jumping speed.

**Tipo:** float

### maxSlope

The maximum slope which the character can climb.

**Tipo:** float

### walkDirection

The speed and direction the character is traveling in using world coordinates. This should be used instead of applyMovement() to properly move the character.

**Tipo:** Vector((x, y, z))

### jump()

The character jumps based on it's jump speed.

### jumpDirection

The direction the character is jumping.

**Tipo:** Vector((x, y, z))

### setVelocity(velocity, time, local=False)

Sets the character's linear velocity for a given period.

This method sets character's velocity through it's center of mass during a period.

- **`velocity`**: Linear velocity vector.
  - tipo: 3D Vector
- **`time`**: Period while applying linear velocity.
  - tipo: float
- **`local`**:  * False: you get the "global" velocity ie: relative to world orientation. * True: you get the "local" velocity ie: relative to object orientation.
  - tipo: boolean

### smoothMovement

Smooth movement caused by walking direction.

**Tipo:** float (0.0 to 1.0)

### reset()

Resets the character velocity and walk direction.

