# Guia da IA: programar para a Anastacio Engine

Leia isto uma vez antes de escrever código. Depois consulte `INDEX.md` e abra só as páginas de que precisa.
A Anastacio é uma engine nova: nenhum modelo foi treinado com ela. **Não invente funções.** Se um nome não aparece nas páginas da API, ele não existe.

## Nomes e imports

- O módulo principal é **`Range`**, com **R maiúsculo**: `import Range`, `from Range import logic, events`.
- `bge` também funciona (`Range.logic` e `bge.logic` são o mesmo objeto), mas os exemplos e o validador Web usam `Range`. Em exportação Web, `import bge` gera o aviso `WEB-PY-001`.
- Módulos: `Range.logic` (cena, objetos, tempo, `globalDict`), `Range.types` (classes), `Range.render`, `Range.events` (teclas), `Range.constraints` (física), `Range.application`, `Range.texture`, `Range.imgui`, `Range.network`, `Range.track`.
- Scripts de jogo **não** usam `bpy`: o jogo exportado roda sem ele.

## Duas formas de escrever lógica

**Script em controlador Python** (ligado a sensores por logic bricks):

```python
import Range
from Range import logic, events

cont = logic.getCurrentController()
own = cont.owner                      # KX_GameObject dono do controlador
if logic.keyboard.inputs[events.WKEY].active:
    own.applyMovement((0, 0.1, 0), True)   # True = eixos locais
```

**Componente** (classe Python ligada ao objeto, sem logic bricks). Prefira quando a lógica é toda em Python:

```python
import Range
from Range import logic, events
from collections import OrderedDict

class Mover(Range.types.KX_PythonComponent):
    args = OrderedDict([("Velocidade", 0.1)])   # campos do painel, na ordem escrita

    def start(self, args):          # uma vez, quando o jogo começa
        self.velocidade = args["Velocidade"]

    def update(self):               # todo frame, antes dos logic bricks
        if logic.keyboard.inputs[events.WKEY].active:
            self.object.applyMovement((0, self.velocidade, 0), True)
```

- Em componente, o objeto dono é `self.object` (no script é `cont.owner`).
- Campos com slider, dica, seletor de objeto/cena: `from Range.args import Float, Int, Bool, Text, Choice, Object, Scene, Color, Header` (Smart Components).

## Armadilhas comuns

- **Objeto removido:** chamar QUALQUER método ou atributo de um objeto já removido da cena gera `SystemError`. Se ele pode ter sido removido, confira o atributo `invalid` antes.
- **`endObject()`** vale no fim do quadro, não imediatamente.
- **Tempo:** para movimento independente do FPS use `1.0 / max(logic.getAverageFrameRate(), 1.0)`.
- **Teclado/mouse:** `logic.keyboard.inputs[events.WKEY]` tem `.active` (segurada) e `.activated` (apertada neste frame).
- **Propriedades de jogo** do objeto são acessadas como `obj["nome"]`; `obj.get("nome", padrao)` evita erro se não existir.
- **Dados entre cenas:** `logic.globalDict` (e `logic.saveGlobalDict()` para gravar).
- **Cena:** `obj.scene.addObject("Nome", referencia, tempo_de_vida)`, `scene.replace("Fase2")`, `scene.restart()`.
- Os nomes são **camelCase** (`worldPosition`, `applyMovement`), não snake_case do Blender moderno.

## Como consultar sem estourar o contexto

1. `INDEX.md`: uma linha por classe/módulo.
2. Página da classe, por exemplo `paginas/KX_GameObject.md`. Páginas grandes têm visão geral + partes `--props`, `--funcs`, `--consts`.
3. `busca.json` (ou a ferramenta MCP `api_buscar`) para achar um nome sem saber a classe.
4. Itens marcados *(novo na Anastacio)* não existiam na engine original: confira a descrição, o modelo não os conhece.
