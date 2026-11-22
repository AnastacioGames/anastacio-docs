# KX_ParticleSystem

> **Veja também:**
[`KX_GameObject`](KX_GameObject.md), [`KX_Scene`](KX_Scene.md)

Classe `Range.types.KX_ParticleSystem`.

```python
# Muda o fogo do objeto com o jogo rodando.
import Range

own = Range.logic.getCurrentController().owner
particles = own.particles

if particles is not None:
    particles.particleCount = 200
    particles.lifetime = 1.5
    particles.blendMode = "ADDITIVE"
```

```python
# Uma explosão só.
import Range

particles = Range.logic.getCurrentController().owner.particles

particles.emissionMode = "BURST"
particles.burst()
```

```python
# Para de emitir.
import Range

particles = Range.logic.getCurrentController().owner.particles
particles.enabled = False
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### burst()

 `método`

Solta todas as partículas de uma vez no próximo frame. Só em emissores com `burstMode` ligado.

### billboardMode

*(novo na Anastacio)* `atributo`

Como as partículas ficam viradas para a câmera: `'FULL'` ou `'VERTICAL'` (gira só no eixo vertical).

### blendMode

*(novo na Anastacio)* `atributo`

Como as partículas se misturam com a cena: `'ALPHA'` ou `'ADDITIVE'`. Valor desconhecido levanta `ValueError`.

### burstInterval

*(novo na Anastacio)* `atributo`

Intervalo, em segundos, entre as rajadas automáticas do modo burst.

### burstMode

*(novo na Anastacio)* `atributo`

`True` emite em rajadas (explosões); `False` emite sem parar.

### collisionBounce

 `atributo`

Quanto a partícula quica ao bater (0 = não quica).

### collisionFriction

 `atributo`

Atrito da partícula ao deslizar depois de bater.

### collisionHeight

 `atributo`

Altura do plano do chão quando `collisionMode` é 1.

### collisionMode

 `atributo`

Colisão das partículas: 0 nenhuma, 1 plano do chão, 2 com o que aparece na tela (screen-space).

### color

 `atributo`

Cor inicial `[r, g, b, a]` das partículas.

### debugUI

 `atributo · só leitura`

`True` quando o painel de depuração do sistema de partículas está aberto.

### drag

*(novo na Anastacio)* `atributo`

Resistência do ar: quanto as partículas perdem velocidade com o tempo.

### emissionAngle

 `atributo`

Abertura do cone de emissão, em graus.

### emissionDirection

 `atributo`

Direção `[x, y, z]` em que as partículas saem.

### emissionMode

*(novo na Anastacio)* `atributo`

Modo de emissão: `'CONTINUOUS'` ou `'BURST'` (todas de uma vez). `burstMode` acompanha este valor.

### emitterPosition

 `atributo`

Posição `[x, y, z]` do emissor em relação ao objeto.

### emitterRadius

 `atributo`

Raio da área de onde as partículas nascem.

### enabled

 `atributo`

Liga ou desliga a emissão.

### endColor

 `atributo`

Cor `[r, g, b, a]` da partícula no fim da vida (a cor vai mudando de `color` até ela).

### endSize

 `atributo`

Tamanho da partícula no fim da vida.

### flipbook

*(novo na Anastacio)* `atributo`

### fragmentShaderPath

 `atributo`

Caminho de um `.glsl` próprio para desenhar as partículas. Vazio volta ao visual padrão.

### gravity

 `atributo`

Gravidade aplicada às partículas.

### lifetime

 `atributo`

Tempo de vida de cada partícula, em segundos.

### particleCount

 `atributo`

Quantidade máxima de partículas vivas.

### size

 `atributo`

Tamanho inicial das partículas.

### texture

 `atributo`

Caminho da imagem usada nas partículas. Vazio remove a textura.

### useBackfaceCulling

*(novo na Anastacio)* `atributo`

Se as partículas deixam de ser desenhadas quando vistas por trás.

### useDebugUi

*(novo na Anastacio)* `atributo`

Mostra o painel de depuração do emissor durante o jogo.

### useObjectRotation

*(novo na Anastacio)* `atributo`

### useVortex

*(novo na Anastacio)* `atributo`

Liga o redemoinho: as partículas sobem girando em volta do emissor.

### velocity

 `atributo`

Velocidade inicial das partículas.

### velocityRandomness

 `atributo`

Variação aleatória da velocidade inicial (0 = todas iguais).

### vortexHeight

*(novo na Anastacio)* `atributo`

Altura do redemoinho.

### vortexRadiusTop

*(novo na Anastacio)* `atributo`

Raio do redemoinho no topo.

### vortexRotationSpeed

*(novo na Anastacio)* `atributo`

Velocidade de rotação do redemoinho.
