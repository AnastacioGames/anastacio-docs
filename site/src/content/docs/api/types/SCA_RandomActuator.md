---
title: "SCA_RandomActuator"
description: "Referência da classe Range.types.SCA_RandomActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Random Actuator

### seed

Seed of the random number generator.

**Tipo:** integer.

Equal seeds produce equal series. If the seed is 0, the generator will produce the same value on every call.

### para1

the first parameter of the active distribution.

**Tipo:** float, read-only.

Refer to the documentation of the generator types for the meaning of this value.

### para2

the second parameter of the active distribution.

**Tipo:** float, read-only

Refer to the documentation of the generator types for the meaning of this value.

### distribution

Distribution type. (read-only). Can be one of `these constants`

**Tipo:** integer

### propName

the name of the property to set with the random value.

**Tipo:** string

If the generator and property types do not match, the assignment is ignored.

### setBoolConst(value)

Sets this generator to produce a constant boolean value.

- **`value`**: The value to return.
  - tipo: boolean

### setBoolUniform()

Sets this generator to produce a uniform boolean distribution.

The generator will generate True or False with 50% chance.

### setBoolBernouilli(value)

Sets this generator to produce a Bernouilli distribution.

- **`value`**: Specifies the proportion of False values to produce. * 0.0: Always generate True * 1.0: Always generate False
  - tipo: float

### setIntConst(value)

Sets this generator to always produce the given value.

- **`value`**: the value this generator produces.
  - tipo: integer

### setIntUniform(lower_bound, upper_bound)

Sets this generator to produce a random value between the given lower and upper bounds (inclusive).

  - tipo: integer
  - tipo: integer

### setIntPoisson(value)

Generate a Poisson-distributed number.

This performs a series of Bernouilli tests with parameter value. It returns the number of tries needed to achieve succes.

  - tipo: float

### setFloatConst(value)

Always generate the given value.

  - tipo: float

### setFloatUniform(lower_bound, upper_bound)

Generates a random float between lower_bound and upper_bound with a uniform distribution.

  - tipo: float
  - tipo: float

### setFloatNormal(mean, standard_deviation)

Generates a random float from the given normal distribution.

- **`mean`**: The mean (average) value of the generated numbers
  - tipo: float
- **`standard_deviation`**: The standard deviation of the generated numbers.
  - tipo: float

### setFloatNegativeExponential(half_life)

Generate negative-exponentially distributed numbers.

The half-life 'time' is characterized by half_life.

  - tipo: float

