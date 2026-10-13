---
title: "KX_ParticleSystem"
description: "Referência da classe Range.types.KX_ParticleSystem"
---

Classe `Range.types.KX_ParticleSystem`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### burst()

 <small>método</small>

Solta todas as partículas de uma vez no próximo frame. Só em emissores com `burstMode` ligado.

### billboardMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Como as partículas ficam viradas para a câmera: `'FULL'` ou `'VERTICAL'` (gira só no eixo vertical).

### blendMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Como as partículas se misturam com a cena: `'ALPHA'` ou `'ADDITIVE'`. Valor desconhecido levanta `ValueError`.

### burstInterval

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Intervalo, em segundos, entre as rajadas automáticas do modo burst.

### burstMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

`True` emite em rajadas (explosões); `False` emite sem parar.

### collisionBounce

 <small>atributo</small>

Quanto a partícula quica ao bater (0 = não quica).

### collisionFriction

 <small>atributo</small>

Atrito da partícula ao deslizar depois de bater.

### collisionHeight

 <small>atributo</small>

Altura do plano do chão quando `collisionMode` é 1.

### collisionMode

 <small>atributo</small>

Colisão das partículas: 0 nenhuma, 1 plano do chão, 2 com o que aparece na tela (screen-space).

### color

 <small>atributo</small>

Cor inicial `[r, g, b, a]` das partículas.

### debugUI

 <small>atributo · só leitura</small>

`True` quando o painel de depuração do sistema de partículas está aberto.

### drag

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Resistência do ar: quanto as partículas perdem velocidade com o tempo.

### emissionAngle

 <small>atributo</small>

Abertura do cone de emissão, em graus.

### emissionDirection

 <small>atributo</small>

Direção `[x, y, z]` em que as partículas saem.

### emissionMode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Modo de emissão: `'CONTINUOUS'` ou `'BURST'` (todas de uma vez). `burstMode` acompanha este valor.

### emitterPosition

 <small>atributo</small>

Posição `[x, y, z]` do emissor em relação ao objeto.

### emitterRadius

 <small>atributo</small>

Raio da área de onde as partículas nascem.

### enabled

 <small>atributo</small>

Liga ou desliga a emissão.

### endColor

 <small>atributo</small>

Cor `[r, g, b, a]` da partícula no fim da vida (a cor vai mudando de `color` até ela).

### endSize

 <small>atributo</small>

Tamanho da partícula no fim da vida.

### fragmentShaderPath

 <small>atributo</small>

Caminho de um `.glsl` próprio para desenhar as partículas. Vazio volta ao visual padrão.

### gravity

 <small>atributo</small>

Gravidade aplicada às partículas.

### lifetime

 <small>atributo</small>

Tempo de vida de cada partícula, em segundos.

### particleCount

 <small>atributo</small>

Quantidade máxima de partículas vivas.

### size

 <small>atributo</small>

Tamanho inicial das partículas.

### texture

 <small>atributo</small>

Caminho da imagem usada nas partículas. Vazio remove a textura.

### useBackfaceCulling

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se as partículas deixam de ser desenhadas quando vistas por trás.

### useDebugUi

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Mostra o painel de depuração do emissor durante o jogo.

### useVortex

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga o redemoinho: as partículas sobem girando em volta do emissor.

### velocity

 <small>atributo</small>

Velocidade inicial das partículas.

### velocityRandomness

 <small>atributo</small>

Variação aleatória da velocidade inicial (0 = todas iguais).

### vortexHeight

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Altura do redemoinho.

### vortexRadiusTop

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Raio do redemoinho no topo.

### vortexRotationSpeed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Velocidade de rotação do redemoinho.

