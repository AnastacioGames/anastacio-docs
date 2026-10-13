---
title: "KX_ReplaceMeshActuator"
description: "Referência da classe Range.types.KX_ReplaceMeshActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Atuador Edit Object, no modo Replace Mesh.

:::caution
Atuadores Replace Mesh são ignorados se, no início do jogo, a malha com o nome indicado não existir.

Isto gera um aviso no console

```text

Error: GameObject 'Name' ReplaceMeshActuator 'ActuatorName' without object
```
:::

```python

# Nível de detalhe
# Troca a malha de um game object conforme a profundidade dele na vista da câmera.
# +----------+     +-----------+     +-------------------------------------+
# | Always   +-----+ Python    +-----+ Edit Object (Replace Mesh) LOD.Mesh |
# +----------+     +-----------+     +-------------------------------------+
from Range import logic

# Liste aqui as malhas de detalhe
# Malha (nome, perto, longe)
# As malhas se sobrepõem para não "pipocar" na borda da distância.
meshes = ((".Hi", 0.0, -20.0),
      (".Med", -15.0, -50.0),
      (".Lo", -40.0, -100.0)
    )

cont = logic.getCurrentController()
object = cont.owner
actuator = cont.actuators["LOD." + obj.name]
camera = logic.getCurrentScene().active_camera

def Depth(pos, plane):
  return pos[0]*plane[0] + pos[1]*plane[1] + pos[2]*plane[2] + plane[3]

# A profundidade é negativa e diminui conforme se afasta da câmera
depth = Depth(object.position, camera.world_to_camera[2])

newmesh = None
curmesh = None
# Acha a malha de menor detalhe para a profundidade
for mesh in meshes:
  if depth < mesh[1] and depth > mesh[2]:
    newmesh = mesh
  if "ME" + object.name + mesh[0] == actuator.getMesh():
      curmesh = mesh

if newmesh != None and "ME" + object.name + newmesh[0] != actuator.mesh:
  # A malha é diferente - troca.
  # Confere se a malha atual não serve melhor.
  if curmesh == None or curmesh[1] < depth or curmesh[2] > depth:
    actuator.mesh = object.name + newmesh[0]
    cont.activate(actuator)
```

### mesh

`MeshProxy` ou o nome da malha que vai substituir a atual.

Use None para desligar o atuador.

**Tipo:** `MeshProxy` or None if no mesh is set

### useDisplayMesh

com true, a malha exibida é substituída.

**Tipo:** boolean

### usePhysicsMesh

com true, a malha de física é substituída.

**Tipo:** boolean

### instantReplaceMesh()

Substitui a malha na hora, sem atraso.

