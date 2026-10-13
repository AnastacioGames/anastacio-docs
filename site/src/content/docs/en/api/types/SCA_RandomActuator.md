---
title: "SCA_RandomActuator"
description: "Range.types.SCA_RandomActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Random Actuator

### seed

Seed of the random number generator.

**Type:** integer.

Equal seeds produce equal series. If the seed is 0, the generator will produce the same value on every call.

### para1

the first parameter of the active distribution.

**Type:** float, read-only.

Refer to the documentation of the generator types for the meaning of this value.

### para2

the second parameter of the active distribution.

**Type:** float, read-only

Refer to the documentation of the generator types for the meaning of this value.

### distribution

Distribution type. (read-only). Can be one of `these constants`

**Type:** integer

### propName

the name of the property to set with the random value.

**Type:** string

If the generator and property types do not match, the assignment is ignored.

### setBoolConst(value)

Sets this generator to produce a constant boolean value.

- **`value`**: The value to return.
  - type: boolean

### setBoolUniform()

Sets this generator to produce a uniform boolean distribution.

The generator will generate True or False with 50% chance.

### setBoolBernouilli(value)

Sets this generator to produce a Bernouilli distribution.

- **`value`**: Specifies the proportion of False values to produce. * 0.0: Always generate True * 1.0: Always generate False
  - type: float

### setIntConst(value)

Sets this generator to always produce the given value.

- **`value`**: the value this generator produces.
  - type: integer

### setIntUniform(lower_bound, upper_bound)

Sets this generator to produce a random value between the given lower and
upper bounds (inclusive).

  - type: integer
  - type: integer

### setIntPoisson(value)

Generate a Poisson-distributed number.

This performs a series of Bernouilli tests with parameter value.
It returns the number of tries needed to achieve succes.

  - type: float

### setFloatConst(value)

Always generate the given value.

  - type: float

### setFloatUniform(lower_bound, upper_bound)

Generates a random float between lower_bound and upper_bound with a
uniform distribution.

  - type: float
  - type: float

### setFloatNormal(mean, standard_deviation)

Generates a random float from the given normal distribution.

- **`mean`**: The mean (average) value of the generated numbers
  - type: float
- **`standard_deviation`**: The standard deviation of the generated numbers.
  - type: float

### setFloatNegativeExponential(half_life)

Generate negative-exponentially distributed numbers.

The half-life 'time' is characterized by half_life.

  - type: float

