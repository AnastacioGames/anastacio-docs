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

