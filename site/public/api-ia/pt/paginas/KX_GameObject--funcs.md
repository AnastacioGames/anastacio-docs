# KX_GameObject - métodos e funções

Parte de [KX_GameObject](KX_GameObject.md).

## endObject()

Apaga este objeto. Pode substituir o atuador End Object.

A remoção de fato do objeto da cena acontece um pouco depois.

## shatter(origin=None, burst=None)

Quebra este objeto destrutível agora, trocando-o pelos pedaços do grupo Fragments. Se o objeto também for explosivo, ele detona junto.

- **`origin`**: O ponto de onde os pedaços se afastam; por padrão, a posição do objeto.
  - tipo: 3D Vector
- **`burst`**: A velocidade dada aos pedaços para longe de origin; por padrão, o Burst Speed do painel.
  - tipo: float

**Retorna:** Os pedaços novos, ou uma lista vazia se o objeto não é destrutível ou já quebrou.

**Tipo do retorno:** list of `KX_GameObject`

## detonate()

Faz este objeto explosivo explodir agora: uma explosão como `KX_Scene.explode` com os ajustes do painel, o objeto Effect e a remoção do objeto. Um explosivo destrutível também quebra.

**Retorna:** False se o objeto não é explosivo ou já explodiu.

**Tipo do retorno:** boolean

## dent(point, direction, impulse)

Amassa este objeto deformável (painel Deformation) como um impacto da força dada: os vértices dentro do Radius do painel em volta de point andam na direção direction (para dentro do objeto) (impulse - Dent Impulse) * Depth, limitado por Max Depth. Só esta instância muda; outros objetos que usam a mesma malha mantêm a forma.

- **`point`**: Ponto atingido, no espaço do mundo.
  - tipo: 3D vector
- **`direction`**: Direção do impacto no espaço do mundo, invertida para apontar para dentro do objeto.
  - tipo: 3D vector
- **`impulse`**: Força do impacto (N*s), comparada com o Dent Impulse.
  - tipo: float

**Retorna:** False se o objeto não é deformável, se o impulso é fraco demais ou se nenhum vértice se moveu.

**Tipo do retorno:** boolean

## resetDent()

Restaura a forma de um objeto amassado.

**Retorna:** False se o objeto nunca foi amassado.

**Tipo do retorno:** boolean

## replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False)

Troca a malha deste objeto por outra. Funciona do mesmo jeito que o atuador.

- **`mesh`**: A malha nova, ou o nome dela.
  - tipo: `MeshProxy` or string
- **`useDisplayMesh`**: Se ligado, troca a malha visível (argumento opcional).
  - tipo: boolean
- **`usePhysicsMesh`**: Se ligado, troca a malha da física (argumento opcional).
  - tipo: boolean

## setVisible(visible[, recursive])

Define se o objeto está visível.

- **`visible`**: O estado de visibilidade a definir.
  - tipo: boolean
- **`recursive`**: Argumento opcional para aplicar a visibilidade também a todos os filhos. Se não for passado, vale False.
  - tipo: boolean

## setOcclusion(occlusion[, recursive])

Define se o objeto participa do occlusion culling.

- **`occlusion`**: O estado de oclusão a definir.
  - tipo: boolean
- **`recursive`**: Argumento opcional para aplicar a oclusão também a todos os filhos. Se não for passado, vale False.
  - tipo: boolean

## alignAxisToVect(vect, axis=2, factor=1.0)

Alinha um dos eixos do objeto com o vetor dado.

- **`vect`**: O vetor com o qual alinhar o eixo.
  - tipo: 3D vector
- **`axis`**: O eixo a alinhar * 0: eixo X * 1: eixo Y * 2: eixo Z
  - tipo: integer
- **`factor`**: Gira só uma fração do caminho até o vetor alvo (0.0 a 1.0).
  - tipo: float

## getAxisVect(vect)

Devolve o vetor do eixo girado pela orientação do objeto no mundo. Equivale a multiplicar o vetor pela matriz de orientação.

- **`vect`**: O vetor com o qual alinhar o eixo.
  - tipo: 3D Vector

**Retorna:** O vetor em relação à rotação do objeto.

**Tipo do retorno:** 3d vector.

## applyMovement(movement[, local])

Move o objeto.

- **`movement`**: O vetor de movimento.
  - tipo: 3D Vector
- **`local`**: * False: movimento "global", relativo à orientação do mundo. * True: movimento "local", relativo à orientação do objeto. Se não for passado, vale False.
- **`local`**: boolean

## applyRotation(rotation[, local])

Gira o objeto.

- **`rotation`**: O vetor de rotação.
  - tipo: 3D Vector
- **`local`**: * False: rotação "global", relativa à orientação do mundo. * True: rotação "local", relativa à orientação do objeto. Se não for passado, vale False.
- **`local`**: boolean

## applyForce(force[, local])

Aplica uma força ao objeto.

Exige um objeto dinâmico.

- **`force`**: O vetor de força.
  - tipo: 3D Vector
- **`local`**: * False: força "global", relativa à orientação do mundo. * True: força "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

## applyTorque(torque[, local])

Aplica um torque ao objeto.

Exige um objeto dinâmico.

- **`torque`**: O vetor de torque.
  - tipo: 3D Vector
- **`local`**: * False: torque "global", relativo à orientação do mundo. * True: torque "local", relativo à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

## getLinearVelocity([local])

Lê a velocidade linear do objeto.

Este método devolve a velocidade do objeto no centro de massa, sem a parte angular.

- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

**Retorna:** A velocidade linear do objeto.

**Tipo do retorno:** Vector((vx, vy, vz))

## setLinearVelocity(velocity[, local])

Define a velocidade linear do objeto.

Este método define a velocidade do objeto no centro de massa, sem a parte angular.

Exige um objeto dinâmico.

- **`velocity`**: O vetor de velocidade linear.
  - tipo: 3D Vector
- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

## getAngularVelocity([local])

Lê a velocidade angular do objeto.

- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

**Retorna:** A velocidade angular do objeto.

**Tipo do retorno:** Vector((vx, vy, vz))

## setAngularVelocity(velocity[, local])

Define a velocidade angular do objeto.

Exige um objeto dinâmico.

- **`velocity`**: O vetor de velocidade angular.
  - tipo: boolean
- **`local`**: * False: velocidade "global", relativa à orientação do mundo. * True: velocidade "local", relativa à orientação do objeto. Se não for passado, vale False.

## getVelocity([point])

Lê a velocidade do objeto no ponto indicado.

Lê a velocidade do objeto no ponto indicado, incluindo a parte angular.

- **`point`**: Ponto opcional onde medir a velocidade, em coordenadas locais. Se não for passado, vale (0, 0, 0).
  - tipo: 3D Vector

**Retorna:** A velocidade no ponto indicado.

**Tipo do retorno:** Vector((vx, vy, vz))

## getReactionForce()

Lê a força de reação do objeto.

A força de reação é a força aplicada a este objeto no último passo da simulação. Inclui também impulsos, como os de colisões.

**Retorna:** A força de reação deste objeto.

**Tipo do retorno:** Vector((fx, fy, fz))

> **Note:**
Isto ainda não está implementado.

## applyImpulse(point, impulse[, local])

Aplica um impulso ao objeto.

Aplica o impulso dado ao objeto no ponto indicado. Se point for diferente da posição, applyImpulse também muda o momento angular do objeto; caso contrário, só o momento linear muda.

- **`point`**: O ponto onde aplicar o impulso (em coordenadas do mundo ou locais).
  - tipo: point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
- **`impulse`**: O vetor de impulso.
  - tipo: 3D Vector
- **`local`**: * False: impulso "global", relativo às coordenadas e à orientação do mundo. * True: impulso "local", relativo às coordenadas e à orientação do objeto. Se não for passado, vale False.
  - tipo: boolean

## setDamping(linear_damping, angular_damping)

Define `linearDamping` e `angularDamping` de uma vez. É mais eficiente do que definir cada um separadamente.

- **`linear_damping`**: Fator de amortecimento linear (de translação).
  - tipo: float ∈ [0, 1]
- **`angular_damping`**: Fator de amortecimento angular (de rotação).
  - tipo: float ∈ [0, 1]

## suspendPhysics([freeConstraints])

Suspende a física deste objeto.

- **`freeConstraints`**: Se for `True`, as constraints de física usadas pelo objeto são apagadas. Se for `False` (o padrão), as constraints voltam quando a física é restaurada.
  - tipo: bool

## restorePhysics()

Retoma a física deste objeto e volta a ligar as colisões.

## suspendDynamics([ghost])

Suspende a física dinâmica deste objeto.

- **`ghost`**: Se for `True`, as colisões com o objeto são ignoradas, como a opção "ghost" do Blender. Se for `False` (o padrão), o objeto fica estático mas continua colidindo com os outros.
  - tipo: bool

> **Tip:**
`isSuspendDynamics` mostra se o objeto está suspenso.

## restoreDynamics()

Retoma a física dinâmica deste objeto e volta a ligar as colisões; o objeto deixa de ser ghost.

> **Note:**
O objeto volta com a velocidade linear que tinha quando a dinâmica foi suspensa.

## enableRigidBody()

Liga a física de corpo rígido deste objeto.

Com a física de corpo rígido, o objeto rola ao colidir.

## disableRigidBody()

Desliga a física de corpo rígido deste objeto.

## setParent(parent, compound=True, ghost=True)

Define o pai deste objeto. Os parâmetros opcionais compound e ghost controlam a forma de colisão:

Nesse caso, dá para escolher se ele fica ghost ou não:

- **`parent`**: O novo objeto pai.
  - tipo: `KX_GameObject`
- **`compound`**: Se a forma deve ser somada à forma composta do pai. * True: a forma do objeto entra na forma composta do pai. * False: o objeto mantém a própria forma.
  - tipo: boolean
- **`ghost`**: Se o objeto deve ficar ghost enquanto tiver pai. * True: fica ghost enquanto tiver pai. * False: continua sólido enquanto tiver pai.
  - tipo: boolean

> **Note:**
Se o objeto for do tipo sensor, ele continua ghost, seja qual for o parâmetro ghost.

## removeParent()

Remove o pai deste objeto.

## getPhysicsId()

Devolve o objeto de dados do usuário ligado ao controlador de física deste objeto.

## getPropertyNames()

Lê a lista com os nomes de todas as propriedades.

**Retorna:** Os nomes de todas as propriedades deste objeto.

**Tipo do retorno:** list

## getBoundBoxSize()

Tamanho da caixa envolvente (`cullingBox`) nos eixos do próprio objeto, com a escala de mundo.

**Retorna:** largura, profundidade e altura.

**Tipo do retorno:** `mathutils.Vector`

## getBoundBoxCorners(space='WORLD')

Os 8 cantos da caixa envolvente. O canto `i` usa o X máximo com o bit 0 ligado, o Y máximo com o bit 1 e o Z máximo com o bit 2; assim, `[0]` é o canto mínimo e `[7]` o máximo.

- **`space`**: `'WORLD'` (posições no mundo), `'OFFSET'` (a partir de `worldPosition`, com rotação e escala) ou `'LOCAL'` (espaço do objeto, sem escala).
  - tipo: string

**Tipo do retorno:** list of `mathutils.Vector`

Os cantos `'WORLD'` podem ser passados direto para `boxInsideFrustum`, para testar se o objeto está na visão da câmera.

## getBoundBoxVolume()

Compatibilidade com scripts da Range 1.x: retorna `[volume, canto1, ..., canto8]`. O volume usa a escala de mundo e os cantos são os `'OFFSET'` de `getBoundBoxCorners`; assim, `obj.worldPosition + box[i]` é um canto no mundo.

**Tipo do retorno:** list

## getDistanceTo(other)

- **`other`**: Um ponto ou outro `KX_GameObject` até onde medir a distância.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** A distância até o outro objeto ou ponto.

**Tipo do retorno:** float

## getVectTo(other)

Devolve o vetor e a distância até outro objeto ou ponto. O vetor vem normalizado, a não ser que a distância seja 0; nesse caso, vem um vetor de tamanho zero.

- **`other`**: Um ponto ou outro `KX_GameObject` até onde calcular o vetor e a distância.
  - tipo: `KX_GameObject` or list [x, y, z]

**Retorna:** (distância, vetorGlobal(3), vetorLocal(3))

**Tipo do retorno:** 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))

## rayCastTo(other, dist=0, prop="")

Olha na direção de outro ponto ou objeto e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop.

O raio sempre sai do centro do objeto, ignorando o próprio objeto. Ele vai até o centro de outro objeto ou até um ponto [x, y, z]. Use rayCast() se precisar do ponto atingido.

- **`other`**: [x, y, z] ou objeto na direção do qual o raio é lançado
  - tipo: `KX_GameObject` or 3-tuple
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`prop`**: Nome da propriedade que o objeto precisa ter; se omitido, detecta qualquer objeto
  - tipo: string

**Retorna:** O primeiro objeto atingido, ou None se não atingir nada ou se o objeto não tiver a propriedade

**Tipo do retorno:** `KX_GameObject`

## rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF)

Olha de um ponto ou objeto até outro e acha o primeiro objeto atingido dentro de dist que tenha a propriedade prop. Se poly for 0, devolve uma tupla de 3 com o objeto, o ponto e a normal atingidos, ou (None, None, None) se não atingir nada. Se poly for 1, devolve uma tupla de 4 com um `KX_PolyProxy` como 4º elemento. Se poly for 2, devolve uma tupla de 5 com um vetor 2D com a coordenada UV do ponto atingido como 5º elemento.

```python

# atira ao longo do eixo gun-gunAim (gunAim não deve ter colisão)
obj, point, normal = gun.rayCast(gunAim, None, 50)
if obj:
   # faz alguma coisa
   pass
```

O parâmetro face define a orientação da normal.

* 0 => a normal sempre aponta para a origem do raio (como se o raio viesse de fora)
* 1 => a normal é a normal real da face (só para malhas; nos outros casos face não tem efeito)

Se xray for 1, o raio atravessa objetos (raio X); caso contrário, o primeiro objeto atingido (fora o próprio) para o raio. Os parâmetros prop e xray funcionam juntos assim:

* prop desligado, xray desligado: devolve o acerto mais próximo, ou nada se não houver objeto em todo o comprimento do raio.
* prop desligado, xray ligado: o mesmo.
* prop ligado, xray desligado: devolve o acerto mais próximo se ele tiver prop; caso contrário, nada.
* prop ligado, xray ligado: devolve o acerto mais próximo que tenha prop, ou nada se nenhum objeto com prop estiver em todo o comprimento do raio.

O `KX_PolyProxy` que vem como 4º elemento quando poly=1 dá informações sobre o polígono atingido. Se não atingir nada, ou se o objeto atingido não for uma malha estática, o 4º elemento é None.

O raio ignora objetos sem colisão e faces sem a opção de colisão, mas pode atingir objetos ghost.

- **`objto`**: [x, y, z] ou objeto até onde o raio é lançado
  - tipo: `KX_GameObject` or 3-tuple
- **`objfrom`**: [x, y, z] ou objeto de onde o raio sai; None ou omitido usa o centro do próprio objeto
  - tipo: `KX_GameObject` or 3-tuple or None
- **`dist`**: Distância máxima (pode ser negativa, para olhar para trás); 0 ou omitido detecta até o alvo
  - tipo: float
- **`prop`**: Nome da propriedade que o objeto precisa ter; omitido ou "" detecta qualquer objeto
  - tipo: string
- **`face`**: Opção de normal: 1 devolve a normal da face; 0 ou omitido aponta a normal para a origem
  - tipo: integer
- **`xray`**: Opção de raio X: 1 pula os objetos que não têm prop; 0 ou omitido para no primeiro objeto
  - tipo: integer
- **`poly`**: Opção de polígono: 0, 1 ou 2 para devolver uma tupla de 3, 4 ou 5 com dados da face atingida. * 0 ou omitido: tupla de 3 (object, hitpoint, hitnormal), ou (None, None, None) se não atingir nada. * 1: tupla de 4, com um `KX_PolyProxy` como 4º elemento, ou None se não atingir nada ou se o objeto não usar forma de colisão de malha. * 2: tupla de 5, com uma tupla (u, v) da coordenada UV do ponto atingido como 5º elemento, ou None se não atingir nada, se o objeto não usar forma de colisão de malha ou não tiver mapeamento UV.
  - tipo: integer
- **`mask`**: Máscara de colisão: a máscara (16 camadas num inteiro de 16 bits) é combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só podem ser atingidos os objetos em que `collisionGroup & mask` for verdadeiro.
  - tipo: bitfield

**Retorna:** (object, hitpoint, hitnormal), ou (object, hitpoint, hitnormal, polygon), ou (object, hitpoint, hitnormal, polygon, hituv). * object, hitpoint e hitnormal são None se não atingir nada. * polygon só é válido se o objeto for válido e for estático, dinâmico com forma de colisão de malha ou soft body; senão é None. * hituv só é válido se polygon for válido e o objeto tiver mapeamento UV; senão é None.

**Tipo do retorno:**  * 3-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz)) * or 4-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`) * or 5-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`, 2-tuple (u, v))

> **Note:**
O raio ignora o objeto que chamou o método. Ele sai do centro do objeto, ou vai até ele, ou usa pontos [x, y, z].

## collide(obj)

Testa se este objeto colide com o objeto `obj`.

- **`obj`**: O objeto com o qual testar a colisão
  - tipo: string or `KX_GameObject`

**Retorna:** (collide, points) * collide: True se este objeto colide com `obj` * points: os pontos de contato da colisão, ou None

**Tipo do retorno:** 2-tuple (boolean, list of `KX_CollisionContactPoint` or None)

## setCollisionMargin(margin)

Define a margem de colisão do objeto.

- **`margin`**: A distância da margem de colisão, em unidades do Blender.
  - tipo: float

> **Note:**
Se este objeto não tiver controlador de física (ID de física zero), esta função gera RuntimeError.

## sendMessage(subject, body="", to="")

Envia uma mensagem.

- **`subject`**: O assunto da mensagem
  - tipo: string
- **`body`**: O corpo da mensagem (opcional)
  - tipo: string
- **`to`**: O nome do objeto que vai receber a mensagem (opcional)
  - tipo: string

## reinstancePhysicsMesh(gameObject, meshObject, dupli)

Atualiza a física com a malha alterada.

Sem argumentos, a malha da física é recriada a partir da primeira malha do objeto.

- **`gameObject`**: Argumento opcional: cria a forma de física a partir da malha deste objeto.
  - tipo: string, `KX_GameObject` or None
- **`meshObject`**: Argumento opcional: cria a forma de física a partir desta malha.
  - tipo: string, `MeshProxy` or None
- **`dupli`**: Argumento opcional: duplica a forma de física.
  - tipo: boolean

**Retorna:** True se a recriação deu certo, False se falhou.

**Tipo do retorno:** boolean

> **Note:**
Se este objeto tiver instâncias, elas também são atualizadas.

> **Note:**
O argumento gameObject tem a vantagem de converter a malha com os modificadores aplicados (como o Subdivision Surface).

> **Caution:**
Por enquanto, só objetos com malha de triângulos ou convex hull são suportados.

> **Caution:**
Falha se o objeto fizer parte de um objeto composto (pai ou filho).

> **Caution:**
Recriar a malha da física pode ser lento; rodar isso muitas vezes por segundo pesa no desempenho.

> **Caution:**
Duplicar a malha da física pode gastar bem mais memória; use esta opção só em malhas duplicadas, senão use `replacePhysicsShape`.

## replacePhysicsShape(gameObject)

Troca a forma de física atual.

- **`gameObject`**: Cria a forma de física a partir deste objeto.
  - tipo: string, `KX_GameObject`

**Retorna:** True se a troca deu certo, False se falhou.

**Tipo do retorno:** boolean

> **Caution:**
Formas de malha de triângulos não são suportadas.

## get(key[, default])

Devolve o valor da chave, ou o valor padrão se a chave não existir.
- **`key`**: A chave procurada
  - tipo: string
- **`default`**: Valor padrão opcional se a chave não existir; se não for passado, vale None.

**Retorna:** O valor da chave ou o padrão.

## playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=KX_ACTION_BLEND_BLEND)

Toca uma ação.

- **`name`**: O nome da ação
  - tipo: string
- **`start`**: O frame inicial da ação
  - tipo: float
- **`end`**: O frame final da ação
  - tipo: float
- **`layer`**: A camada onde a ação vai tocar (ações em camadas diferentes são somadas/misturadas)
  - tipo: integer
- **`priority`**: Só toca esta ação se não houver outra tocando nesta camada com prioridade maior (número menor)
  - tipo: integer
- **`blendin`**: Quanto misturar esta animação com a anterior nesta camada
  - tipo: float
- **`play_mode`**: O modo de reprodução
  - tipo: one of `these constants`
- **`layer_weight`**: Quanto da camada anterior usar na mistura
  - tipo: float
- **`ipo_flags`**: Flags dos comportamentos antigos de IPO (force etc.)
  - tipo: int bitfield
- **`speed`**: A velocidade da ação como fator (1.0 = normal, 2.0 = o dobro etc.)
  - tipo: float
- **`blend_mode`**: Como misturar esta camada com as anteriores
  - tipo: one of `these constants`

## stopAction([layer])

Para a ação que está tocando na camada indicada.

- **`layer`**: A camada a parar; se não for passada, vale 0.
  - tipo: integer

## getActionFrame([layer])

Lê o frame atual da ação que está tocando na camada indicada.

- **`layer`**: A camada de onde ler o frame; se não for passada, vale 0.
  - tipo: integer

**Retorna:** O frame atual da ação

**Tipo do retorno:** float

## getActionName([layer])

Lê o nome da ação que está tocando na camada indicada.

- **`layer`**: A camada de onde ler o nome da ação; se não for passada, vale 0.
  - tipo: integer

**Retorna:** O nome da ação atual

**Tipo do retorno:** string

## setActionFrame(frame[, layer])

Define o frame atual da ação que está tocando na camada indicada.

- **`layer`**: A camada onde definir o frame; se não for passada, vale 0.
  - tipo: integer
- **`frame`**: O frame para onde levar a ação
  - tipo: float

## isPlayingAction([layer])

Verifica se há uma ação tocando na camada indicada.

- **`layer`**: A camada a verificar; se não for passada, vale 0.
  - tipo: integer

**Retorna:** Se a ação está tocando ou não

**Tipo do retorno:** boolean

## playNLA(speed=1.0, loop=True)

Toca as faixas do NLA de uma armature, como o NLA Editor faz. Faixas e strips mutadas são puladas, o Solo é respeitado e as faixas são misturadas de baixo para cima (Replace e Add, influência, blend in/out, repeat, scale, reverse e extrapolação). Ações tocadas com `playAction` são misturadas por cima do resultado do NLA.

Chamar de novo enquanto o NLA está tocando, com os mesmos argumentos, não reinicia; por isso pode ser chamado todo frame.

Ainda não suportado: strips de transição e meta, modos Subtract/Multiply (tocados como Replace), curvas de tempo da strip e NLA em objetos que não são armatures.

- **`speed`**: Velocidade de reprodução (1.0 = taxa de quadros de animação da cena, 0.0 = parado, use `setNLAFrame`; negativa toca de trás para frente a partir do último frame).
  - tipo: float
- **`loop`**: Recomeça da primeira strip depois que a última termina; senão, segura o último frame.
  - tipo: boolean

**Retorna:** True quando o NLA começou (o objeto é uma armature com pelo menos uma strip).

**Tipo do retorno:** boolean

## stopNLA()

Para a reprodução do NLA. A armature mantém a pose atual.

## isPlayingNLA()

**Retorna:** True enquanto o NLA está tocando (False depois que um NLA sem loop chegou ao fim).

**Tipo do retorno:** boolean

## getNLAFrame()

**Retorna:** O frame atual do NLA.

**Tipo do retorno:** float

## setNLAFrame(frame)

Pula o NLA para o frame dado, limitado ao intervalo das strips.

- **`frame`**: O frame do NLA.
  - tipo: float

## addDebugProperty (name[, debug])

Adiciona uma propriedade à lista de depuração.

- **`name`**: O nome da propriedade a adicionar à lista de depuração.
  - tipo: string
- **`debug`**: O estado de depuração; se não for passado, vale True.
  - tipo: boolean

## getCurvePoints()

 `método`

`getCurvePoints(world=True)`: pontos da primeira spline de um objeto Curve, como lista de `Vector`. Coordenadas do mundo por padrão; `world=False` devolve em coordenadas locais. Lista vazia se o objeto não for uma curva.

## getTurnTo(other)

 `método`

Vetor local deste objeto até outro objeto ou ponto. Útil para saber para que lado virar.

**Retorna:** `Vector`

## getVehicle()

*(novo na Anastacio)* `método`

O veículo criado pelo painel Vehicle deste objeto, ou `None`.

**Retorna:** `KX_VehicleWrapper`

## getVehicleGearboxType()

*(novo na Anastacio)* `método`

Tipo de câmbio configurado no painel Vehicle.

**Retorna:** `int`

## getVehicleGearRatios()

*(novo na Anastacio)* `método`

Relações das marchas configuradas no painel Vehicle.

**Retorna:** `tuple`

## getVehicleMaxRPM()

*(novo na Anastacio)* `método`

Rotação máxima do motor configurada no painel Vehicle.

**Retorna:** `float`

## getVehicleMaxTorque()

*(novo na Anastacio)* `método`

Torque máximo do motor configurado no painel Vehicle.

**Retorna:** `float`

## getVehicleSteeringWheel()

*(novo na Anastacio)* `método`

Objeto do volante configurado no painel Vehicle, ou `None`.

**Retorna:** `KX_GameObject`

## is_playing_take()

 `método`

`True` enquanto um Take do Rec Play move este objeto.

**Retorna:** `bool`

## lookAt(vect, axis=2, factor=1.0)

*(novo na Anastacio)* `método`

Vira o objeto para que o eixo `axis` (0=X, 1=Y, 2=Z) aponte na direção `vect`. `factor` abaixo de 1 vira só uma parte (suaviza).

## play_take(name)

 `método`

Toca o que um Take do Rec Play gravou deste objeto. `False` se não gravou nada dele.

**Retorna:** `bool`

## resumeAnimations()

*(novo na Anastacio)* `método`

Retoma as animações pausadas por `suspendAnimations()`.

## setActionLayerSpeed(layer, speed)

 `método`

Muda a velocidade da ação que toca na camada `layer`.

## setActionLayerWeight(layer, layerWeight)

 `método`

Muda o peso (0 a 1) da camada de animação `layer`.

## setCcdMotionThreshold(threshold)

*(novo na Anastacio)* `método`

Velocidade a partir da qual a detecção contínua de colisão (CCD) entra, evitando que objetos rápidos atravessem paredes.

## setCcdSweptSphereRadius(radius)

*(novo na Anastacio)* `método`

Raio da esfera usada pela detecção contínua de colisão (CCD).

## setHalfAnimations(enabled)

*(novo na Anastacio)* `método`

Com `True`, atualiza as animações do objeto em frames alternados, para economizar CPU.

## setSoftAnchorsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez das âncoras.

## setSoftAngularStiffness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez angular.

## setSoftClusterSolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de clusters.

## setSoftContactsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez dos contatos.

## setSoftDampingCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): amortecimento.

## setSoftDragCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): arrasto do ar.

## setSoftDriftSolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de deriva.

## setSoftDynamicFrictionCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): atrito dinâmico.

## setSoftKineticContactsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez do contato com objetos cinemáticos.

## setSoftLiftCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): sustentação (lift).

## setSoftLinearStiffness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez linear.

## setSoftPoseMatching(enabled)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): liga a tentativa de voltar à forma original.

## setSoftPoseMatchingCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): força com que volta à forma original.

## setSoftPositionSolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de posição.

## setSoftPressureCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): pressão interna (efeito balão).

## setSoftRigidContactsHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez do contato com corpos rígidos.

## setSoftVelocitiesCorrectionFactor(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): fator de correção das velocidades.

## setSoftVelocitySolverIterations(iterations)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): iterações do solver de velocidade.

## setSoftVolume(volume)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): volume que o corpo tenta manter.

## setSoftVolumeConversationCoefficient(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): conservação de volume.

## setSoftVsKineticHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez contra corpos cinemáticos (clusters).

## setSoftVsKineticImpulseSplitCluster(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): divisão de impulso contra corpos cinemáticos (clusters).

## setSoftVsRigidHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez contra corpos rígidos (clusters).

## setSoftVsRigidImpulseSplitCluster(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): divisão de impulso contra corpos rígidos (clusters).

## setSoftVsSoftHardness(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): rigidez contra outros corpos moles (clusters).

## setSoftVsSoftImpulseSplitCluster(value)

*(novo na Anastacio)* `método`

Física de corpo mole (soft body): divisão de impulso contra outros corpos moles (clusters).

## setVehicleGearRatios(relacoes)

*(novo na Anastacio)* `método`

Troca as relações de marcha do veículo. Recebe uma lista de números, uma por marcha.

## setVehicleMaxRPM(valor)

*(novo na Anastacio)* `método`

Muda em jogo a rotação máxima (RPM) do motor do veículo (número >= 0).

## setVehicleMaxTorque(valor)

*(novo na Anastacio)* `método`

Muda em jogo o torque máximo do motor do veículo deste objeto (número >= 0).

## stop_take()

 `método`

Para o Take deste objeto e o devolve à lógica e à física.

## strikeLightning(bolt=True)

 `método`

um raio cai agora (a chuva precisa estar ligada)

## suspendAnimations()

*(novo na Anastacio)* `método`

Pausa todas as animações do objeto até `resumeAnimations()`.
