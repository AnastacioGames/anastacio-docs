---
title: "SCA_PythonController"
description: "Referência da classe Range.types.SCA_PythonController"
---

Classe base: [`SCA_IController`](../sca_icontroller/)



Um controlador Python usa um script Python para ativar seus atuadores, com base nos seus sensores.

### owner

O objeto ao qual o controlador está ligado.

**Tipo:** `KX_GameObject`

### script

O valor desta variável depende do modo de execução.

* No modo de execução 'Script', este valor contém o script Python inteiro numa única string (não o nome do script, como seria de esperar), que pode ser modificada para rodar outros scripts.
* No modo de execução 'Module', este valor contém uma string de uma linha: o nome do módulo e a função, "module.func" ou "package.modile.func", em que os nomes de módulo são textblocks Python ou scripts externos.

**Tipo:** string

:::note
Depois que isto é definido, o nome do script usado nos avisos não muda mais.
:::

### mode

o modo de execução deste controlador (somente leitura).

* Script: 0, executa o `script` como código Python.
* Module: 1, executa o `script` como módulo e função.

**Tipo:** integer

### activate(actuator)

Ativa um atuador ligado a este controlador.

- **`actuator`**: O atuador sobre o qual operar.
  - tipo: actuator or the actuator name as a string

### deactivate(actuator)

Desativa um atuador ligado a este controlador.

- **`actuator`**: O atuador sobre o qual operar.
  - tipo: actuator or the actuator name as a string

