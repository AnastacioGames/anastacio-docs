# KX_SceneActuator

Classe base: [`SCA_IActuator`](SCA_IActuator.md)

Logic brick do atuador Scene.

> **Caution:**
Atuadores de cena que usam um nome de cena são ignorados se, no início do jogo, a cena com esse nome não existir ou estiver vazia

Isto gera um aviso no console:

```text

Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene
```

## scene

o nome da cena para trocar/sobrepor/pôr por baixo/remover/suspender/retomar.

**Tipo:** string

### camera

a câmera para a qual trocar.

**Tipo:** `KX_Camera` on read, string or `KX_Camera` on write

> **Note:**
Ao definir o atributo, dá para usar um `KX_Camera` ou o nome da câmera.

### useRestart

Use True para reiniciar a cena.

**Tipo:** boolean

### mode

O modo do atuador.

**Tipo:** integer from 0 to 5.
