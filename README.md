# Anastacio Docs

Site da documentação da API Python da Anastacio Engine (hospedado no GitHub Pages) e as ferramentas que geram o conteúdo dele.

O código da engine fica em outro repositório (`D:\AnastacioEngine`). Este repositório só lê de lá.

## Pastas

| Pasta | O que tem |
|---|---|
| `tools/` | Scripts. `api_inventario.py` levanta toda a API a partir do C++ da engine. |
| `inventario/` | Saída do inventário: `api_inventario.md` (relatório para revisar) e `api_inventario.json` (dados). |
| `prototipo/` | Protótipo visual aprovado do site (`site-prototipo.html`, abre direto no navegador). |
| `site/` | (a criar) Projeto Astro Starlight do site. |

## Como atualizar a documentação

Sempre que a engine ganhar funções novas:

1. **Rodar o inventário**
   ```
   python tools/api_inventario.py --engine D:/AnastacioEngine
   ```
   Demora ~2 min porque consulta o git da engine para saber quando cada item entrou. `--sem-origem` pula essa parte.

2. **Revisar `inventario/api_inventario.md`**
   - **novo**: existe no C++ e não está nos `.rst` da Range. Marcado com ✦data quando entrou depois de 15/09/2026 (commit `28775369`, snapshot inicial do código), ou seja, com certeza é da Anastacio.
   - **sem doc**: está no `.rst` mas sem descrição.
   - **só no rst**: documentado mas não achado no C++ (removido, herdado de classe base ou registrado de outro jeito).
   - Comparar com a versão anterior pelo `git diff inventario/` mostra só o que mudou.

3. **Escrever o conteúdo** dos itens novos (descrição, tipos, exemplo) nos arquivos de conteúdo do site.

4. **Publicar**: commit + push; a GitHub Action gera o site.

## Regras do conteúdo

- Nome principal do módulo é `Range`, com **R maiúsculo** (`import Range`, `from Range import logic`). A Range usou maiúscula para não confundir com a função `range()` do Python.
- `import bge` também funciona: a engine registra cada `Range.<módulo>` também como `bge.<módulo>`.
- Módulos: `Range.logic`, `Range.types`, `Range.render`, `Range.events`, `Range.constraints`, `Range.application` (`bge.app` no rst antigo), `Range.texture`, `Range.imgui`, `Range.network`, `Range.network.steam`.
- Cada item recebe um selo: **da Range**, **alterado na Anastacio** ou **novo na Anastacio**.

## Fontes que o inventário lê (na engine)

- Bindings das classes: tabelas `PyMethodDef X::Methods[]` e `PyAttributeDef X::Attributes[]` em `source/source/gameengine/**/*.cpp`.
- Funções e constantes dos módulos: `KX_PythonInit.cpp`, `KX_PyNetwork.cpp`, `KX_PyConstraintBinding.cpp`, `KXImgui/KX_PythonImgui.cpp`, `VideoTexture/blendVideoTex.cpp`.
- Documentação herdada: `source/doc/python_api/rst/` (módulos) e `rst/bge_types/` (classes).

## Visual do site

Fundo escuro com dourado/laranja da marca, degradê dourado escuro → preto no topo, cubo dourado rachado (`source/release/windows/icons/anastacio-engine-cube-splash-v2.png` na engine), banner da Anastacio Games na página Sobre. Ver `prototipo/site-prototipo.html`.
