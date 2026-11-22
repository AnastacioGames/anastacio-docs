# KX_MeshBuilderSlot

> **Veja também:**
[`KX_MeshBuilder`](KX_MeshBuilder.md), [`KX_Mesh`](KX_Mesh.md)

Classe `Range.types.KX_MeshBuilderSlot`.

```python
# Adiciona um quadrado feito de dois triângulos.
points = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
ids = [slot.addVertex(point) for point in points]

slot.addIndex([ids[0], ids[1], ids[2]])
slot.addIndex([ids[0], ids[2], ids[3]])
slot.recalculateNormals()
```

```python
# Mostra o que o slot tem.
print(len(slot.vertices), len(slot.indices))
print(slot.uvCount, slot.colorCount)
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### addIndex(indices)

 `método`

Acrescenta índices de vértices (lista de inteiros) aos primitivos e, se for malha de triângulos, aos triângulos.

### addPrimitiveIndex(indices)

 `método`

Acrescenta índices só à lista de primitivos (desenho).

### addTriangleIndex(indices)

 `método`

Acrescenta índices só à lista de triângulos (física e raios).

### addVertex(position, normal=None, tangent=None, uvs=None, colors=None)

 `método`

Acrescenta um vértice. `uvs` e `colors` são listas, uma entrada por camada.

**Retorna:** `int`

### recalculateNormals()

 `método`

Recalcula as normais dos vértices a partir dos triângulos.

### removePrimitiveIndex(start, end=-1)

 `método`

Remove índices de primitivos de `start` até `end`.

### removeTriangleIndex(start, end=-1)

 `método`

Remove índices de triângulos de `start` até `end`.

### removeVertex(start, end=-1)

 `método`

Remove vértices de `start` até `end`.

### colorCount

 `atributo · só leitura`

Quantas camadas de cor de vértice o slot tem.

### indices

 `atributo · só leitura`

Lista dos índices de primitivos.

### material

 `atributo`

Material do slot.

### primitive

 `atributo · só leitura`

Tipo de primitivo do slot (pontos, linhas ou triângulos).

### triangleIndices

 `atributo · só leitura`

Lista dos índices de triângulos.

### uvCount

 `atributo · só leitura`

Quantas camadas de UV o slot tem.

### vertices

 `atributo · só leitura`

Lista dos vértices do slot.
