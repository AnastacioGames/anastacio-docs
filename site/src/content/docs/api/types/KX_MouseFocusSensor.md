---
title: "KX_MouseFocusSensor"
description: "Referência da classe Range.types.KX_MouseFocusSensor"
---

Classe base: [`SCA_MouseSensor`](../sca_mousesensor/)



O sensor Mouse focus detecta quando o mouse está sobre o game object atual.

O sensor Mouse focus transforma as coordenadas do mouse do espaço 2D do dispositivo para o espaço 3D e lança um raio a partir da câmera.

### raySource

A origem do raio no espaço do mundo (a posição da vista).

**Tipo:** list (vector of 3 floats)

### rayTarget

O alvo do raio no espaço do mundo.

**Tipo:** list (vector of 3 floats)

### rayDirection

`rayTarget` - `raySource`, normalizado.

**Tipo:** list (normalized vector of 3 floats)

### hitObject

o último objeto sob o mouse.

**Tipo:** `KX_GameObject` or None

### hitPosition

A posição, no espaço do mundo, da interseção do raio.

**Tipo:** list (vector of 3 floats)

### hitNormal

a normal, no espaço do mundo, da face no ponto de interseção.

**Tipo:** list (normalized vector of 3 floats)

### hitUV

as coordenadas UV no ponto de interseção.

**Tipo:** list (vector of 2 floats)

Se o objeto não tem mapeamento UV, devolve [0, 0].

As coordenadas UV não são normalizadas; podem ser < 0 ou > 1 dependendo do mapeamento UV.

### usePulseFocus

Quando ligado, passar o mouse sobre outro objeto gera um pulso (só usado com a opção 'Mouse Over Any' do sensor).

**Tipo:** boolean

### useXRay

Se ligado, o sensor enxerga através de game objects que não têm a propriedade ou o material escolhido.

**Tipo:** boolean

### mask

A máscara de colisão (16 layers mapeadas num inteiro de 16 bits) combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só os objetos em que `collisionGroup & mask` é verdadeiro podem ser atingidos.

**Tipo:** bitfield

### propName

A propriedade ou o material que o sensor procura.

**Tipo:** string

### useMaterial

Define se o sensor procura uma propriedade ou um material. KX_True = procura material; KX_False = procura propriedade.

**Tipo:** boolean

