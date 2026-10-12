# Anastacio Docs
## 🚀 Acesse o site aqui!

| 📘 Versão ao Vivo | 🎨 Protótipo | 💻 Rodar Localmente |
|------------------|-------------|-------------------|
| [Site publicado](https://anastacioGames.github.io/anastacio-docs/) | [Visualizar HTML](https://github.com/AnastacioGames/anastacio-docs/blob/main/prototipo/site-prototipo.html) | `cd site && npm install && npm run dev` |
Site da documentação da API Python da Anastacio Engine (hospedado no GitHub Pages) e as ferramentas que geram o conteúdo dele.

O código da engine fica em outro repositório (`D:\AnastacioEngine`). Este repositório só lê de lá.

## Pastas

| Pasta | O que tem |
|---|---|
| `tools/` | Scripts. `api_inventario.py` levanta a API e audita a cobertura Python dos controles de jogo. |
| `inventario/` | Saída do inventário (`api_inventario.*`) e da cobertura (`cobertura_python.*`). |
| `prototipo/` | Protótipo visual aprovado do site (`site-prototipo.html`, abre direto no navegador). |
| `site/` | Projeto Astro Starlight do site. Páginas escritas à mão em `site/src/content/docs/` (início, sobre, guias); `api/` é gerada. |

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
   - Revisar também `inventario/cobertura_python.md`: ele cruza os controles RNA de partículas,
     explosões e clima com os bindings Python e aponta os que ainda não têm acesso em runtime.
     “Sem binding” é uma fila de decisão técnica, não uma ordem para expor todo controle de editor.

3. **Gerar as páginas da API**
   ```
   python tools/gerar_paginas.py --engine D:/AnastacioEngine
   ```
   Apaga e recria `site/src/content/docs/api/`. Junta o texto da Range (`.rst`), o inventário e as docstrings do C++. **Não edite à mão os arquivos de `api/`**: o texto de itens novos deve ir para a docstring no C++ (4º campo do `PyMethodDef`) ou para o `.rst` da engine, e aparece na próxima geração.

   **Tradução:** o texto da Range sai em português quando o trecho está em `traducao/pt.json` (inglês → português). O que falta traduzir fica em `traducao/pendente.json`, separado por página. Para traduzir uma página: escreva um `.txt` em `traducao/lotes/` com uma tradução por linha, na ordem do `pendente.json`, e rode `python tools/aplicar_lote.py <pagina> traducao/lotes/<pagina>.txt`. Código, nomes de funções, parâmetros e tipos continuam em inglês; comentários dos exemplos são traduzidos. Para várias páginas de uma vez, use um arquivo com seções `===== <pagina>` e rode `python tools/aplicar_varios.py <arquivo>` (uma linha `=` mantém o texto original).

   **Itens novos sem docstring:** escreva a descrição em português em `conteudo/descricoes.json` (`{"Classe": {"item": "texto"}}`). Ela aparece na página e ganha da docstring do C++.

4. **Ver o site no PC**
   ```
   cd site
   npm install      (só na primeira vez)
   npm run dev      (abre em http://localhost:4321/anastacio-docs/)
   ```

5. **Publicar**: commit + push na `main`. A Action `.github/workflows/deploy.yml` compila e publica no GitHub Pages.
   Na primeira vez: no GitHub, Settings > Pages > Source = **GitHub Actions**. Se o repositório ou o usuário não forem `AnastacioGames/anastacio-docs`, ajuste `SITE` e `BASE` em `site/astro.config.mjs`.

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
