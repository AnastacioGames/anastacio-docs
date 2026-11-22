# SCA_MouseSensor

Classe base: [`SCA_ISensor`](SCA_ISensor.md)

Logic brick do sensor de mouse.

```python
# Lê a posição do mouse e o botão esquerdo.
import Range

sensor = Range.logic.getCurrentController().sensors["Mouse"]

print(sensor.position)

if sensor.getButtonStatus(Range.logic.KX_MOUSE_BUT_LEFT) == Range.logic.KX_INPUT_ACTIVE:
    print("Left button held")
```

## position

As coordenadas [x, y] atuais do mouse, em coordenadas do frame (pixels).

**Tipo:** [integer, interger]

### mode

O modo do sensor.

Diferente da UPBGE, a Range tem os botões do polegar e os botões 6 e 7 antes da roda, então roda para cima, roda para baixo e movimento valem 8, 9 e 10 (na UPBGE eram 4, 5 e 6). Compare com as constantes Range.logic.KX_MOUSESENSORMODE_* em vez de números. Sensores de mouse de arquivos .blend da UPBGE e da BGE original são convertidos ao abrir o arquivo.

**Tipo:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_LEFTTHUMBMOUSE(4) * KX_MOUSESENSORMODE_RIGHTTHUMBMOUSE(5) * KX_MOUSESENSORMODE_BUTTON6(6) * KX_MOUSESENSORMODE_BUTTON7(7) * KX_MOUSESENSORMODE_WHEELUP(8) * KX_MOUSESENSORMODE_WHEELDOWN(9) * KX_MOUSESENSORMODE_MOVEMENT(10)

### getButtonStatus(button)

Lê o estado de um botão do mouse.

- **`button`**: O código do botão cujo estado você quer ler; use uma `destas constantes`
  - tipo: int

**Retorna:** O estado do botão, que pode ser uma `destas constantes`

**Tipo do retorno:** int

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### holdTime

*(novo na Anastacio)* `atributo`

Tempo, em segundos, segurando o botão para o sensor disparar (0 a 30).
