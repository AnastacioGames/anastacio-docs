---
title: "KX_Mesh"
description: "Referência da classe Range.types.KX_Mesh"
---

Classe base: [`EXP_Value`](../exp_value/)



Um objeto de malha.

Só dá para mudar as propriedades dos vértices de uma malha, não a topologia dela.

Para usar malhas bem, é bom saber um pouco de como a game engine lida com elas.

#. Mesh Objects are converted from Blender at scene load.
#. The Converter groups polygons by Material.  This means they can be sent to the renderer efficiently.  A material holds:

#. The texture.
#. The Blender material.
#. The Tile properties
#. The face properties - (From the "Texture Face" panel)
#. Transparency & z sorting
#. Light layer
#. Polygon shape (triangle/quad)
#. Game Object

#. Vertices will be split by face if necessary.  Vertices can only be shared between faces if:

#. They are at the same position
#. UV coordinates are the same
#. Their normals are the same (both polygons are "Set Smooth")
#. They are the same color, for example: a cube has 24 vertices: 6 faces with 4 vertices per face.

O jeito certo de percorrer todos os `KX_VertexProxy` de um game object

```python

from Range import logic

cont = logic.getCurrentController()
object = cont.owner

for mesh in object.meshes:
   for m_index in range(len(mesh.materials)):
      for v_index in range(mesh.getVertexArrayLength(m_index)):
         vertex = mesh.getVertex(m_index, v_index)
         # Faça algo com o vértice aqui...
         # ... ex.: pinta o vértice de vermelho.
         vertex.color = [1.0, 0.0, 0.0, 1.0]
```

### materials

**Tipo:** list of `KX_BlenderMaterial` type

### numPolygons

**Tipo:** integer

### numMaterials

**Tipo:** integer

### polygons

Devolve a lista de polígonos desta malha.

**Tipo:** `KX_PolyProxy` list (read only)

### getMaterialName(matid)

Pega o nome do material indicado.

- **`matid`**: o material indicado.
  - tipo: integer

**Retorna:** o nome do material ligado.

**Tipo do retorno:** string

### getTextureName(matid)

Pega o nome da textura do material indicado.

- **`matid`**: o material indicado
  - tipo: integer

**Retorna:** o nome da textura do material ligado.

**Tipo do retorno:** string

### getVertexArrayLength(matid)

Pega o tamanho do array de vértices ligado ao material indicado.

Há um array de vértices para cada material.

- **`matid`**: o material indicado
  - tipo: integer

**Retorna:** o número de vértices no array de vértices.

**Tipo do retorno:** integer

### getVertex(matid, index)

Pega o vértice indicado da malha.

- **`matid`**: o material indicado
  - tipo: integer
- **`index`**: o índice no array de vértices.
  - tipo: integer

**Retorna:** um objeto de vértice.

**Tipo do retorno:** `KX_VertexProxy`

### getPolygon(index)

Pega o polígono indicado da malha.

- **`index`**: número do polígono
  - tipo: integer

**Retorna:** um objeto de polígono.

**Tipo do retorno:** `KX_PolyProxy`

### transform(matid, matrix)

Transforma os vértices de uma malha.

- **`matid`**: índice do material; -1 transforma todos.
  - tipo: integer
- **`matrix`**: matriz de transformação.
  - tipo: 4x4 matrix [[float]]

### transformUV(matid, matrix, uv_index=-1, uv_index_from=-1)

Transforma as UVs dos vértices de uma malha.

- **`matid`**: índice do material; -1 transforma todos.
  - tipo: integer
- **`matrix`**: matriz de transformação.
  - tipo: 4x4 matrix [[float]]
- **`uv_index`**: índice de UV opcional; -1 para todos, senão 0 ou 1.
  - tipo: integer
- **`uv_index_from`**: índice de UV opcional de onde copiar; -1 para transformar a UV atual.
  - tipo: integer

### replaceMaterial(matid, material)

Troca o material do slot `matid` pelo material `material`.

- **`matid`**: O índice do material.
  - tipo: integer
- **`material`**: O material substituto.
  - tipo: `KX_BlenderMaterial`

:::caution
Trocar o material de uma malha usada por muitos objetos pode ser lento. Não chame esta função a cada frame
:::

### copy()

Devolve uma cópia da malha.

**Retorna:** uma cópia da malha em uso.

**Tipo do retorno:** `KX_Mesh`.

### constructBvh(transform=mathutils.Matrix.Identity(4), epsilon=0)

Devolve uma árvore BVH baseada na geometria da malha. Os índices dos elementos da árvore são iguais aos índices dos polígonos.

- **`transform`**: A matriz de transformação 4x4 aplicada aos vértices.
  - tipo: `mathutils.Matrix`
- **`epsilon`**: O epsilon de distância da árvore.
  - tipo: float

**Retorna:** Uma árvore BVH baseada na geometria da malha.

**Tipo do retorno:** `mathutils.bvhtree.BVHTree`

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### destruct()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

