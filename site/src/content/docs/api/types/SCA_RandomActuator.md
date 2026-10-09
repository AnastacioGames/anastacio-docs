---
title: "SCA_RandomActuator"
description: "Referência da classe Range.types.SCA_RandomActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Random

### seed

Semente do gerador de números aleatórios.

**Tipo:** integer.

Sementes iguais produzem séries iguais. Se a semente for 0, o gerador produz o mesmo valor em toda chamada.

### para1

o primeiro parâmetro da distribuição ativa.

**Tipo:** float, read-only.

Veja a documentação dos tipos de gerador para o significado deste valor.

### para2

o segundo parâmetro da distribuição ativa.

**Tipo:** float, read-only

Veja a documentação dos tipos de gerador para o significado deste valor.

### distribution

Tipo de distribuição (somente leitura). Pode ser uma `destas constantes`

**Tipo:** integer

### propName

o nome da propriedade que recebe o valor aleatório.

**Tipo:** string

Se os tipos do gerador e da propriedade não combinarem, a atribuição é ignorada.

### setBoolConst(value)

Faz este gerador produzir um valor booleano constante.

- **`value`**: O valor a devolver.
  - tipo: boolean

### setBoolUniform()

Faz este gerador produzir uma distribuição booleana uniforme.

O gerador gera True ou False com 50% de chance.

### setBoolBernouilli(value)

Faz este gerador produzir uma distribuição de Bernoulli.

- **`value`**: Define a proporção de valores False a produzir. * 0.0: sempre gera True * 1.0: sempre gera False
  - tipo: float

### setIntConst(value)

Faz este gerador produzir sempre o valor dado.

- **`value`**: o valor que este gerador produz.
  - tipo: integer

### setIntUniform(lower_bound, upper_bound)

Faz este gerador produzir um valor aleatório entre os limites inferior e superior dados (inclusive).

  - tipo: integer
  - tipo: integer

### setIntPoisson(value)

Gera um número com distribuição de Poisson.

Faz uma série de testes de Bernoulli com o parâmetro value. Devolve o número de tentativas até ter sucesso.

  - tipo: float

### setFloatConst(value)

Sempre gera o valor dado.

  - tipo: float

### setFloatUniform(lower_bound, upper_bound)

Gera um float aleatório entre lower_bound e upper_bound com distribuição uniforme.

  - tipo: float
  - tipo: float

### setFloatNormal(mean, standard_deviation)

Gera um float aleatório da distribuição normal dada.

- **`mean`**: O valor médio dos números gerados
  - tipo: float
- **`standard_deviation`**: O desvio padrão dos números gerados.
  - tipo: float

### setFloatNegativeExponential(half_life)

Gera números com distribuição exponencial negativa.

O "tempo" de meia-vida é definido por half_life.

  - tipo: float

