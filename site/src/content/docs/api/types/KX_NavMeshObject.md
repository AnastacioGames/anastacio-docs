---
title: "KX_NavMeshObject"
description: "Referência da classe Range.types.KX_NavMeshObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)

:::tip[Veja também]
[`KX_SteeringActuator`](../../types/kx_steeringactuator/)
:::



Interface Python para usar e controlar navigation meshes.

Uma navigation mesh com a propriedade de jogo Boolean `dynamic_navmesh` igual a True é construída em tiles quando o jogo começa, para que obstáculos possam recortá-la em tempo de execução. Objetos com "Create Obstacle" recortam automaticamente; `addObstacle` adiciona qualquer outro objeto. Os caminhos podem ser um pouco diferentes dos da navigation mesh estática.

```python

# Acha um caminho do objeto até o jogador.
import Range

scene = Range.logic.getCurrentScene()
owner = Range.logic.getCurrentController().owner

navmesh = scene.objects["Navmesh"]
player = scene.objects["Player"]

path = navmesh.findPath(owner.worldPosition, player.worldPosition)
print(len(path), "points")
```

```python

# Confere se há parede até o jogador: fator abaixo de 1.0 quer dizer que o raio parou antes.
import Range

scene = Range.logic.getCurrentScene()
owner = Range.logic.getCurrentController().owner

navmesh = scene.objects["Navmesh"]
player = scene.objects["Player"]

if navmesh.raycast(owner.worldPosition, player.worldPosition) < 1.0:
    print("Something is in the way")
```

```python

# Desenha a navigation mesh para depurar. Rode a cada frame (sensor Always com True Pulse).
import Range

navmesh = Range.logic.getCurrentScene().objects["Navmesh"]
navmesh.draw(Range.logic.RM_TRIS)
```

```python

# Navigation mesh dinâmica: uma caixa bloqueia a passagem e depois libera.
import Range

scene = Range.logic.getCurrentScene()
navmesh = scene.objects["Navmesh"]
crate = scene.objects["Crate"]

if navmesh.dynamic:
    navmesh.addObstacle(crate, 1.5)

# Depois, quando a caixa sair:
navmesh.removeObstacle(crate)
```

### dynamic

True quando a navigation mesh foi construída em tiles e obstáculos podem recortá-la (somente leitura).

**Tipo:** boolean

### version

Aumenta quando a navigation mesh é reconstruída ou termina de mudar por causa de obstáculos (somente leitura). Caminhos achados com uma versão mais antiga podem atravessar obstáculos novos.

**Tipo:** integer

### findPath(start, goal)

Acha o caminho do ponto de início até o ponto de destino.

- **`start`**: o ponto de início
- **`start`**: Vetor 3D
- **`goal`**: o ponto de destino
- **`start`**: Vetor 3D

**Retorna:** um caminho como lista de pontos

**Tipo do retorno:** list of points

### raycast(start, goal)

Lança um raio do ponto de início até o ponto de destino.

- **`start`**: o ponto de início
- **`start`**: Vetor 3D
- **`goal`**: o ponto de destino
- **`start`**: Vetor 3D

**Retorna:** o fator de acerto

**Tipo do retorno:** float

### draw(mode)

Desenha uma malha de depuração da navigation mesh. Numa navigation mesh dinâmica, os cilindros de obstáculo são desenhados em amarelo.

- **`mode`**: o modo de desenho (uma `destas constantes`)
- **`mode`**: inteiro

**Retorna:** None

### rebuild()

Reconstrói a navigation mesh.

**Retorna:** None

### addObstacle(object, radius=0.0)

Faz o objeto recortar todas as navigation meshes dinâmicas da cena, acompanhando-o quando ele se move. Chamar de novo muda o raio. Não tem efeito em navigation meshes estáticas.

- **`object`**: o obstáculo, na mesma cena da navigation mesh
  - tipo: `KX_GameObject` or string
- **`radius`**: o raio, no mundo, do cilindro do obstáculo; 0.0 usa o raio do "Create Obstacle" do objeto ou metade do tamanho da bounding box
  - tipo: float

**Retorna:** None

### removeObstacle(object)

Faz o objeto parar de recortar as navigation meshes dinâmicas, inclusive objetos com "Create Obstacle".

- **`object`**: o obstáculo
  - tipo: `KX_GameObject` or string

**Retorna:** None

