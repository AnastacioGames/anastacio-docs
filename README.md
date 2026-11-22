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
| `docs/` | Planos de trabalho do site. [plano-editor-web.md](docs/plano-editor-web.md): divisão do editor web e sua atualização automática. |

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

   **Exemplos de código:** ficam em `conteudo/exemplos.txt`, em seções `=== <pagina>` separadas por `---`. Cada comentário é escrito como `# inglês ||| português`. O gerador põe os blocos antes do primeiro título da página, onde o botão Mostrar mais os alcança. Depois de gerar, rode `python tools/checar_exemplos.py`: ele confere sintaxe, tradução e se os nomes existem na API.

4. **Ver o site no PC**
   ```
   cd site
   npm install      (só na primeira vez)
   npm run dev      (abre em http://localhost:4321/anastacio-docs/)
   ```

   **Arquivo único para baixar:** depois de gerar, rode `python tools/gerar_md_unico.py`. Ele grava `site/public/anastacio-api-en.md` e `-pt.md` (índice + um título por função), publicados em `/anastacio-docs/anastacio-api-en.md`.

   **Versão fatiada para IA:** rode também `python tools/gerar_api_ia.py`. Ele grava `site/public/api-ia/<pt|en>/` com `INDEX.md` (uma linha por classe/módulo), `paginas/` (uma por classe; as grandes viram visão geral + `--props`, `--funcs`, `--consts`), `busca.json` (um registro por item) e `GUIA.md`/`GUIDE.md` (regras e armadilhas, escritas à mão em `conteudo/guia-ia-<lang>.md`). Também grava `inventario/sem_descricao.md`, a fila de itens sem frase de descrição. O arquivo único de 450 KB é grande demais para o contexto de uma IA; use a versão fatiada. Publicada em `/anastacio-docs/api-ia/pt/`.

   **Servidor MCP:** `tools/anastacio_api_mcp.py` (só biblioteca padrão) serve a versão fatiada com as ferramentas `api_guia`, `api_indice`, `api_buscar`, `api_pagina` e `api_item`. No Claude Code:
   ```
   claude mcp add anastacio-api -- python tools/anastacio_api_mcp.py --lang pt
   claude mcp add anastacio-api -- python tools/anastacio_api_mcp.py --fonte https://anastaciogames.github.io/anastacio-docs/api-ia/pt/
   ```
   (a segunda forma lê a doc publicada, sem clonar o repositório). Ao mudar a API, regere e publique os dois conjuntos (`gerar_md_unico.py` e `gerar_api_ia.py`).

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
