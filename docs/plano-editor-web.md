# Plano: divisão "Editor Web" no site

Objetivo: documentar para o usuário final o editor da Anastacio que roda no navegador, e manter essa documentação
atualizada automaticamente, como já acontece com a API e as páginas da engine.

O editor web vive em outro repositório (`D:\AnastacioEditorWeb`, remoto `AnastacioGames/AnastacioEditorWeb`).
Este repositório só **lê** de lá, igual faz com a engine. A fronteira entre os dois lados está em
`D:\AnastacioEditorWeb\docs\fronteira-engine-editor-web.md` (interno, não vai para o site).

## 1. O que é público e o que é interno

| Público (vai para o site) | Interno (fica nos docs dos repos) |
|---|---|
| O que é o editor web e como abrir (navegador, sem instalar) | Fronteira engine ↔ editor web |
| Editores disponíveis (objetos, materiais, animação, Dope Sheet etc.) | `build_web_editor`, emsdk, quando recompilar o wasm |
| `bpy` no navegador: o que funciona e o que não funciona | `nucleo_*.c`, `EMSCRIPTEN_KEEPALIVE`, `txPonte()` |
| Diferenças para o editor desktop | Harness de teste (`testar_navegador.cjs`) |
| Uma linha em "Por dentro da engine" explicando que reaproveita o núcleo em wasm | Regras de commit e branches |

## 2. Estrutura de páginas

Nova seção da barra lateral, **Editor Web** (traduções: en "Web editor", es "Editor web", ru "Веб-редактор"),
entre "Recursos" e "Por dentro da engine". Páginas em `site/src/content/docs/editor-web/`:

1. `index.md`: o que é, como abrir, limites e diferença para o desktop.
2. `editores.md`: lista dos editores e do que cada um já faz (gerada, ver seção 3).
3. `bpy.md`: **Python no navegador**: tabela do que é suportado (`objects.new`, `meshes.new` + `from_pydata`,
   `materials.new`, `data.materials.append`, `location`, `select_set`, `duplicate`, `remove`) e do que não é
   (`bmesh`, edição de vértices etc.), com exemplos que rodam de verdade no editor.
4. `desktop-vs-web.md`: tabela curta de diferenças (só se `index.md` ficar grande).

Em **Por dentro da engine** (`por-dentro/`): um parágrafo em `editor-para-jogo.md` ou `plataformas.md` dizendo que o
editor web é um projeto separado que reaproveita o núcleo da engine compilado para wasm. Sem detalhes de build.

As traduções (en/es/ru) seguem o fluxo já existente de `traducao/`.

## 3. Atualização automática

Já existem dois mecanismos para as partes da engine:

- **API**: `tools/api_inventario.py` + `tools/gerar_paginas.py` geram `api/` a partir do código da engine.
- **Guias escritos à mão**: `tools/checar_engine.py` compara o frontmatter (`fontes:` e `conferido:`) com o git da engine
  e lista as páginas desatualizadas.

Para o editor web, montar o equivalente com **duas peças**:

### 3.1 Páginas geradas (o que dá para extrair do código)

Novo script `tools/gerar_editor_web.py --editor D:/AnastacioEditorWeb`, que lê do repo do editor web:

- **`bpy.md`**: o `BPY_SHIM` em `prototipo/partes/bpy_web.js` (classes e métodos Python expostos). Os docstrings e as
  descrições em português vêm de `conteudo/descricoes_editor_web.json` (mesmo formato do `descricoes.json`). Itens
  novos sem descrição aparecem como pendentes, como na API.
- **`editores.md`**: lista dos `nucleo_*.c` e de `prototipo/partes/*`, um por editor (a divisão por editor já existe no
  repo do editor web), com a descrição vinda de `conteudo/editores_web.json`.
- Saída em `inventario/editor_web_inventario.{json,md}`, no mesmo molde do inventário da API, para o `git diff
  inventario/` mostrar o que mudou.
- Regra igual à da API: **não editar à mão** os arquivos gerados; texto novo vai no JSON de descrições.

### 3.2 Páginas escritas à mão (`index.md`, `desktop-vs-web.md`)

Usar o mesmo frontmatter que o `checar_engine.py` já entende, mas apontando para o repo do editor web:

```yaml
repo: AnastacioEditorWeb      # novo campo; ausente = engine
fontes:
  - prototipo/partes/bpy_web.js
  - wasm/nucleo_objetos.c
conferido: <commit do editor web>
```

Mudança em `tools/checar_engine.py`: aceitar `--editor-web <caminho>` e escolher o repo conforme o campo `repo:` de
cada página (padrão engine). `--marcar`, `--diff` e o relatório funcionam igual para os dois repos.

### 3.3 Rotina e automação

- **Local** (padrão atual): ao mexer no editor web, rodar `gerar_editor_web.py` e `checar_engine.py`, revisar o diff,
  commitar. Acrescentar a seção "Editor web" ao README deste repo, ao lado de "Como atualizar a documentação".
- **Gancho no repo do editor web**: uma linha na checklist de commit do `AnastacioEditorWeb` ("mexeu em `bpy_web.js` ou
  `nucleo_*.c`: rodar o checar do site"). Opcional: hook `pre-push` local que só avisa, sem bloquear.
- **CI**: a Action `deploy.yml` hoje só compila o site. Acrescentar um job `verificar` que clona o editor web (público)
  e roda `gerar_editor_web.py --verificar`, falhando se os arquivos gerados estiverem diferentes do commitado. Assim
  ninguém publica o site com `bpy.md` defasado. Decidir na etapa 4 se o CI também roda `checar_engine.py` (hoje roda só
  localmente).
- `situacao-da-doc.md` ganha uma linha por página do editor web (itens, documentados, pendentes).

## 4. Etapas

1. **Esqueleto**: criar `editor-web/` com `index.md` e a seção na barra lateral (`astro.config.mjs`), incluindo
   traduções do rótulo. Frontmatter com `repo:`, `fontes:` e `conferido:`.
2. **`checar_engine.py`**: suporte ao campo `repo:` e a `--editor-web`; testar com as páginas novas e com as antigas
   (nenhuma pode mudar de resultado).
3. **`gerar_editor_web.py`** + JSONs de descrições: gerar `bpy.md` e `editores.md`; escrever as descrições em português.
4. **Exemplos**: exemplos de `bpy` em `conteudo/exemplos.txt`, cada um **executado no editor web** com
   `testar_navegador.cjs` antes de entrar na página; estender `checar_exemplos.py` para conferir os nomes contra o
   `BPY_SHIM`.
5. **Por dentro da engine**: parágrafo sobre o wasm.
6. **Automação**: job do CI, README, checklist do repo do editor web, linhas em `situacao-da-doc.md`.
7. **Traduções** en/es/ru e `checar-links.mjs` passando; publicar (commit + push na `main`).

## 5. Critérios de pronto

- `checar_engine.py` mostra as páginas do editor web como `[ok]` e acusa `[DESATUALIZADA]` quando o `bpy_web.js` muda.
- `gerar_editor_web.py` roda sem pendentes e sem diff espúrio.
- Todo exemplo da página `bpy.md` foi executado no editor web.
- O site compila e `checar-links.mjs` passa.
- Nenhum detalhe interno (build, wasm, emsdk) aparece nas páginas públicas.

## 6. Pontos a decidir

- O repo do editor web é público? O job de CI só consegue clonar se for (ou com um token).
- O editor web já tem endereço publicado para o site linkar em "como abrir"? Sem ele, a página `index.md` fica sem o
  botão de abrir.
- O CI deve bloquear o deploy por página desatualizada, ou só avisar?
