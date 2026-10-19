---
title: Carga rápida (Load Mode y Cook)
description: Deja objetos fuera de la carga, créalos solo cuando se necesiten y cocina la escena para que abra más rápido.
---

Una escena grande tarda en abrir porque el motor convierte todos los objetos antes del primer frame. Anastacio tiene dos herramientas para eso:

- **Load Mode**: elige qué objetos se cargan con la escena y cuáles esperan para después.
- **Cook**: guarda en un archivo `.cooked` lo que la conversión calcula (física, mallas, shaders), para no volver a calcularlo.

## Load Mode

Selecciona un objeto y abre **Properties > Object**, panel **Load Object with Scene**. Hay tres modos:

| Modo | Qué sucede |
|---|---|
| **With Scene** | Predeterminado. El objeto se crea con la escena. |
| **On Demand** | Queda fuera de la carga. Se crea cuando un script lo pide o cuando un Add Object lo usa por primera vez. |
| **Editor Only** | Nunca entra al juego. Útil para objetos de referencia, cámaras de trabajo, blockout. |

El modo se aplica a los objetos seleccionados y a sus hijos.

### Crear un objeto On Demand desde un script

(`cena` = escena, `chefe` = jefe, `tiro` = disparo, `arma` = arma: el código es el probado en la página en portugués.)

```python
import Range

cena = Range.logic.getCurrentScene()
chefe = cena.convertObject("Chefe")
```

Si `Chefe` está en una capa activa, aparece en la escena. Si está en una capa inactiva, va a `objectsInactive` y queda listo para `addObject`:

```python
cena.convertObject("Tiro")
tiro = cena.addObject("Tiro", cena.objects["Arma"], 120)
```

`cena.unconvertedObjects` lista los nombres que aún se pueden crear de esta forma.

### Con Logic Bricks

El actuador **Add Object** ya entiende On Demand: el objeto se crea la primera vez que el actuador se dispara, y las siguientes veces solo se hacen copias. No hace falta script.

## Cook

El botón **Cook** está en el panel Render y junto a Play en la cabecera. Ejecuta la escena una vez y escribe, junto al `.blend`, un archivo `.cooked` con:

- formas de colisión (Convex Hull y Triangle Mesh) ya calculadas;
- buffers de malla, normales y tangentes;
- shaders compilados para tu tarjeta gráfica.

En la siguiente carga, el motor lee el archivo en lugar de calcular. En pruebas, la carga de una escena bajó de unos 2,4 s a menos de 0,5 s.

- El `.blend` debe estar guardado (sin archivo guardado el botón aparece deshabilitado).
- **Clear Cooked** borra la caché. Si cambias una malla no necesitas borrarla: la parte modificada se recalcula.
- En el juego exportado, el `.cooked` va incluido. Los shaders se guardan en la computadora del jugador en el primer inicio, que muestra una pantalla de preparación.

## Medir

`Range.logic.getLoadLog()` muestra cuánto tardó cada etapa de la carga. Úsalo antes y después de Cook para ver la ganancia.

```python
import Range

for etapa in Range.logic.getLoadLog():
    print(etapa)
```
