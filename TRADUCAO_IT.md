# Tradução para Italiano (IT) — Mapeamento

> Documento de planejamento. Objetivo: listar exatamente **quais arquivos precisam existir em italiano** para a aplicação ter uma segunda versão completa, trocável via seletor, sem tocar na lógica das páginas. Depois de revisado, os arquivos listados aqui podem ser passados um a um para uma LLM mais simples fazer a tradução literal do conteúdo.

Baseado na análise do repositório em `2026-09-13` (branch `release/0809260830`). Ver também [README.md](README.md), que documenta a arquitetura de conteúdo (`application_content` vs `course_content`) usada como base deste mapeamento.

---

## 1. Como a aplicação já está preparada pra isso

A base de código **já foi pensada pra multi-idioma** — não por acidente: o próprio [README.md](README.md#a-aula-em-si-é-html-não-json) já cita o exemplo de um dia existir `course_content/en/...`. O padrão é: cada pasta de conteúdo tem uma subpasta por idioma (`pt_br` hoje), e o `.html` de cada página aponta pra ela através de duas variáveis JS:

```js
var APP_CONTENT = '../application_content/pt_br/';
var COURSE_CONTENT = '../course_content/pt_br/';
```

(esse trecho existe, hoje com o idioma fixo, em `index.html` e em todos os arquivos de `pages/*.html` que já têm conteúdo).

**Decisão deste mapeamento:** seguir exatamente esse padrão, criando:

- `application_content/it/` (irmã de `application_content/pt_br/`)
- `course_content/it/` (irmã de `course_content/pt_br/`)

**Não** duplicar `index.html` nem nada dentro de `pages/` — essas páginas são só a casca (layout), o texto vem inteiro dos JSON via `fetch`. Duplicar `.html` também exigiria manter duas cópias da mesma lógica JS sincronizadas pra sempre, o que é o oposto de "trocar via seletor". O seletor de idioma deve funcionar do mesmo jeito que o seletor de tema em [assets/theme.js](assets/theme.js): guarda a escolha (ex.: `localStorage`), e cada página decide `APP_CONTENT`/`COURSE_CONTENT` em runtime a partir disso — sem navegar pra outra URL.

> Ideia de referência que já existe no repo, mas em outra frente (não faz parte do site, ver seção 4): `content_generation/jupyter_notebooks_ita/` já é uma tradução paralela dos notebooks de `content_generation/jupyter_notebooks/`. Mesmo espírito, pasta diferente.

---

## 2. Arquivos a criar em `application_content/it/`

Espelho 1:1 de `application_content/pt_br/`, mesmo nome de arquivo:

| Criar | Espelha | Conteúdo | Ação |
|---|---|---|---|
| `application_content/it/index.json` | `pt_br/index.json` (8,4 KB) | Textos da home | Traduzir |
| `application_content/it/bootcamps.json` | `pt_br/bootcamps.json` (3,4 KB) | Textos da listagem de bootcamps | Traduzir |
| `application_content/it/bootcamp.json` | `pt_br/bootcamp.json` (3,6 KB) | Textos da página de 1 bootcamp | Traduzir |
| `application_content/it/modules.json` | `pt_br/modules.json` (4,7 KB) | Textos da listagem de módulos (inclui filtro de nível/tópico) | Traduzir |
| `application_content/it/module.json` | `pt_br/module.json` (5,8 KB) | Textos da tela de estudo (sidebar, quiz, checkpoint, pager…) | Traduzir |
| `application_content/it/projects.json` | `pt_br/projects.json` (4,1 KB) | Textos da listagem de projetos (inclui filtro de nível/tópico) | Traduzir |
| `application_content/it/project.json` | `pt_br/project.json` (3,3 KB) | Textos da página de 1 projeto | Traduzir |
| `application_content/it/lesson.json` | `pt_br/lesson.json` (**vazio**) | — | Pular (ver seção 4) |
| `application_content/it/contact.json` | `pt_br/contact.json` (**vazio**) | — | Pular (ver seção 4) |

---

## 3. Arquivos a criar em `course_content/it/`

### 3.1 Catálogo (JSON)

| Criar | Espelha | Conteúdo |
|---|---|---|
| `course_content/it/bootcamps.json` | `pt_br/bootcamps.json` (9,4 KB) | Catálogo dos bootcamps (`title`, `description`, `outcome`, `level`, `detail.curriculum[]`, `detail.creator`…) |
| `course_content/it/modules.json` | `pt_br/modules.json` (5,6 KB) | Catálogo dos módulos (`title`, `description`, `level`, `skills[]`…) |
| `course_content/it/projects.json` | `pt_br/projects.json` (29 KB — o maior arquivo do projeto) | Catálogo dos projetos, com `detail.introHtml`, `objectiveHtml`, `requirements[]`, `challenges[]`, `tips[]` |
| `course_content/it/lessons.json` | `pt_br/lessons.json` (17,8 KB) | Catálogo das aulas: `title`, `navTitle`, `badge`, `readTime`, `resources[]`, e o campo `content` apontando pro `.html` da aula |

### 3.2 Conteúdo das aulas (HTML) — `course_content/it/python-na-pratica/`

43 arquivos `.html`, mesma árvore de pastas de `course_content/pt_br/python-na-pratica/`. **34 estão ligados a uma aula em `lessons.json`** (marcados ✅); os **9 `projeto-pratico.html`** (um por módulo) ainda não são referenciados por nenhum JSON hoje — nem na versão pt_br — mas devem ser traduzidos do mesmo jeito, já que fazem parte do conteúdo publicado na pasta (⚠️, ver nota abaixo).

```
course_content/it/python-na-pratica/
├── python-variaveis-e-tipos-de-dados/     (módulo 1 — bootcamp_id: ready-to-deploy)
│   ├── colab.html          ✅
│   ├── variaveis.html      ✅
│   ├── numeros.html        ✅
│   ├── strings.html        ✅
│   ├── booleanos.html      ✅
│   └── projeto-pratico.html    ⚠️ não referenciado em lessons.json
├── python-estruturas-de-dados/            (bootcamp_id: python-na-pratica)
│   ├── listas.html         ✅
│   ├── dicionarios.html    ✅
│   ├── conjuntos.html      ✅
│   └── projeto-pratico.html    ⚠️
├── python-fluxo-condicional-e-repeticao/  (bootcamp_id: python-na-pratica)
│   ├── condicionais.html   ✅
│   ├── for.html            ✅
│   ├── excecoes.html       ✅
│   └── projeto-pratico.html    ⚠️
├── python-arquivos-e-funcoes/             (bootcamp_id: python-na-pratica)
│   ├── funcoes.html                ✅
│   ├── escopo.html                 ✅
│   ├── leitura-de-arquivos.html    ✅
│   ├── escrita-de-arquivos.html    ✅
│   └── projeto-pratico.html    ⚠️
├── python-programacao-funcional/          (bootcamp_id: python-na-pratica)
│   ├── lambda.html         ✅
│   ├── map.html            ✅
│   ├── filter.html         ✅
│   ├── reduce.html         ✅
│   └── projeto-pratico.html    ⚠️
├── python-programacao-orientada-a-objetos/ (bootcamp_id: python-na-pratica)
│   ├── teoria.html         ✅
│   ├── classes.html        ✅
│   ├── objetos.html        ✅
│   ├── heranca.html        ✅
│   └── projeto-pratico.html    ⚠️
├── python-modulos-e-pacotes/              (bootcamp_id: python-na-pratica)
│   ├── modulos.html        ✅
│   ├── import.html         ✅
│   ├── pacotes.html        ✅
│   ├── pip.html            ✅
│   └── projeto-pratico.html    ⚠️
├── python-tratamento-de-erros/            (bootcamp_id: python-na-pratica)
│   ├── tipos-de-erros.html             ✅
│   ├── erros-de-sintaxe.html           ✅
│   ├── erros-de-logica.html            ✅
│   ├── erros-em-tempo-de-execucao.html ✅
│   └── projeto-pratico.html    ⚠️
└── python-scripting/                      (bootcamp_id: python-na-pratica)
    ├── instalando-o-python.html            ✅
    ├── criando-arquivos-de-script.html     ✅
    ├── executando-codigo-no-terminal.html  ✅
    └── projeto-pratico.html    ⚠️
```

**Total: 4 JSON + 43 HTML = 47 arquivos em `course_content/it/`.**

---

## 4. Fora do escopo (não criar / não traduzir agora)

| Caminho | Por quê |
|---|---|
| `pages/lesson.html`, `pages/contact.html` | Placeholders **vazios** (0 bytes) mesmo na versão pt_br — a funcionalidade ainda não foi implementada. Nada a traduzir até existirem. |
| `application_content/pt_br/lesson.json`, `contact.json` | Idem — vazios, sem conteúdo fonte pra traduzir. |
| `reference/application_reference_design/**` | O próprio README diz: é material de mockup/referência de design, **não faz parte da aplicação**. |
| `content_generation/**` | Pipeline separado de geração dos notebooks Jupyter (`.ipynb`), não é servido pelo site. Já tem sua própria versão italiana em `content_generation/jupyter_notebooks_ita/` — projeto paralelo, fora do escopo deste mapeamento. |

---

## 5. Atenção: isso sozinho **não é suficiente** — pequenos ajustes de código

Duplicar os arquivos acima traduz o **conteúdo**, mas há detalhes de código que também precisam de atenção pra tudo realmente virar italiano quando o seletor trocar de idioma. Status atualizado depois de implementar o seletor em `index.html`:

1. **`<html lang="pt-BR">`** — era hardcoded e nunca alterado via JS. ✅ **Já corrigido em `index.html`**: `render()` agora faz `document.documentElement.lang = c.lang` (o campo já existia em todo `application_content/*.json`), e um script no `<head>` aplica o idioma salvo antes da primeira pintura, igual ao padrão do `assets/theme.js`. **Ainda falta replicar isso nos 6 arquivos de `pages/`** (`bootcamps.html`, `bootcamp.html`, `modules.html`, `module.html`, `projects.html`, `project.html`) quando o seletor for levado pra lá.

2. **`<title>` e `<meta name="description">`** — na verdade **já eram dinâmicos** em todas as páginas (correção a este documento: a suposição inicial estava errada). Todo `.html` já faz `document.title = c.meta.title` (ou `fill(c.meta.titleFormat, …)` nas páginas de detalhe) e reescreve a tag `<meta name="description">` no load. Ou seja, assim que `application_content/it/*.json` existe, esses dois campos já saem certos automaticamente — nenhum ajuste extra necessário.

3. **`assets/theme.js`** — o seletor de tema (claro/escuro/sistema) tem textos fixos em português direto no JS, fora de qualquer JSON: `LABELS = { light: 'Claro', dark: 'Escuro', system: 'Sistema' }`, `'Selecionar tema (atual: …)'`, `'Tema: …'`, `'Tema da página'` (linhas 46-92 do arquivo). Ainda não traduzido — o seletor de idioma implementado em `index.html` foi feito à parte, sem mexer nesse arquivo compartilhado.

> Status: `index.html` já resolve os itens 1 e 2 sozinho. O que falta é levar o mesmo seletor (e o mesmo `documentElement.lang`) para as páginas em `pages/`, e traduzir os textos fixos de `assets/theme.js` quando fizer sentido.

---

## 6. Diretrizes para quem for traduzir (a LLM mais simples)

### Traduzir
- Qualquer valor de string "de leitura humana": `title`, `label`, `description`, `lead`, `kicker`, `placeholder`, `aria*Label`, `*Html` (contém HTML puro, tipo `<strong>`/`<code>` — traduzir o texto, preservar as tags), `readTime`, `badge`, `name` (nome de recurso em `resources[]`), `outcome`, `objectiveHtml`, `introHtml`, `requirements[]`, `challenges[]`, `tips[]`, `data-exp` dos quizzes, texto corrido dentro do `.html` da aula (`<p>`, `<li>`, `<h2>`, `<blockquote>`, cabeçalhos de tabela).
- `level` (`"Iniciante"`, `"Intermediário"`, `"Avançado"`) — mas leia a nota da seção 6.1 antes, tem um efeito colateral.
- `skills[]` — são exibidas como tags/pills e também usadas como chave do filtro de tópico. Pode traduzir (ex.: `"variaveis"` → `"variabili"`), mas mantenha o estilo *slug* (minúsculo, sem espaço/acento, hífen se precisar de duas palavras) e use o **mesmo texto em todo `course_content/it/`** sempre que for o mesmo conceito — senão o filtro conta o mesmo tópico como dois diferentes.

### NÃO traduzir (copiar como está)
- Chaves do JSON, `id`, `module_id`, `bootcamp_id`, `content` (caminho do `.html` da aula — mesma estrutura de pastas, então o valor **não muda**, só o idioma na URL usada por `COURSE_CONTENT`), `href`/URLs, `published` (data ISO), `hot`/`rating`/`nodes`/`value` (números), e campos que são valores técnicos de estilo, não texto: `variant` (`"primary"`/`"outline"`), `style` (`"solid"`), `icon`, `tone`, `external`, `free`.
- `detail.modulos[]` (lista de **ids** de módulos praticados num projeto) — são identificadores, viram link (`module.html?id=…`), não rótulo.
- Dentro do `.html` da aula: tudo que estiver dentro de `<pre><code class="language-python">…</code></pre>` é **código real**, não prosa. Regra prática e segura pra uma LLM simples: **não tocar em blocos de código**, nem em comentários `#`, porque comentários costumam citar exatamente o valor/saída mostrado na linha seguinte (ex.: `print(cidade)  # São Paulo`) — traduzir só o comentário e não o valor quebra a coerência do exemplo. Onde houver `data-expected="…"` num checkpoint (ainda não existe nenhum na versão pt_br atual, mas o formato já é suportado — ver README), esse valor é a saída exata esperada do código e **nunca** deve ser traduzido/alterado.

### 6.1 Atenção — dependência entre arquivos (fácil de quebrar)

`application_content/<lang>/modules.json` e `application_content/<lang>/projects.json` guardam a lista de níveis usada no **filtro**, e cada nível tem um `id`/`value` que precisa bater exatamente com o nível normalizado (minúsculo, sem acento) que vem de `course_content/<lang>/modules.json` / `projects.json`. A normalização usada pelo código é:

```js
norm(s) = s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
```

Ou seja: se `course_content/it/projects.json` tiver `"level": "Avanzato"`, então `application_content/it/projects.json` precisa ter `{ "id": "avanzato", "label": "Avanzato" }` — **os dois arquivos, os dois traduzidos de forma consistente**. Se só um lado for traduzido (ou o `id` não for recalculado a partir do novo `label`), a seção daquele nível fica **vazia silenciosamente** na tela (sem erro visível).

Sugestão de tradução pronta pra usar (evita ter que recalcular o `norm()` na mão):

| pt_br (`label`/`level`) | it (`label`/`level` sugerido) | `id`/`value` resultante |
|---|---|---|
| Iniciante | Principiante | `principiante` |
| Intermediário | Intermedio | `intermedio` |
| Avançado | Avanzato | `avanzato` |

Isso afeta 2 pares de arquivo:
- `application_content/it/modules.json` (campo `filters.levels[].value`) ⟷ `course_content/it/modules.json` (campo `level` de cada módulo)
- `application_content/it/projects.json` (campo `filters.levels[].id`) ⟷ `course_content/it/projects.json` (campo `level` de cada projeto)

(`bootcamps.json` também tem `level`, mas é só exibido como texto — pode traduzir livremente, não alimenta nenhum filtro.)

---

## 7. Checklist final

**`application_content/it/`**
- [x] `index.json`
- [x] `bootcamps.json`
- [x] `bootcamp.json`
- [x] `modules.json` — níveis traduzidos como `principiante`/`intermedio`/`avanzato`, consistente com `course_content/it/modules.json`
- [x] `module.json`
- [x] `projects.json` — níveis traduzidos como `principiante`/`intermedio`/`avanzato`, consistente com `course_content/it/projects.json`
- [x] `project.json`
- [ ] ~~`lesson.json`~~ — fora do escopo (vazio)
- [ ] ~~`contact.json`~~ — fora do escopo (vazio)

**`course_content/it/`**
- [x] `bootcamps.json`
- [x] `modules.json`
- [x] `projects.json` (29 KB, o maior arquivo)
- [x] `lessons.json`
- [x] 43 arquivos `.html` em `python-na-pratica/**` — estrutura de pastas conferida 1:1 contra `pt_br`, código Python 100% preservado, tags HTML balanceadas

**Seletor de idioma**
- [x] Implementado em `index.html`: botão 🇧🇷/🇮🇹 no header, `localStorage` (`primo-lang`), troca `APP_CONTENT`/`COURSE_CONTENT` e recarrega a página
- [x] `document.documentElement.lang` dinâmico em `index.html` (via `render()` + script antecipado no `<head>`)
- [x] `document.title` / `<meta description>` — já eram dinâmicos em todas as páginas, nenhum ajuste necessário

**Seletor de idioma — agora em todas as páginas**
- [x] Extraído para `assets/lang.js` (compartilhado, mesmo padrão de `assets/theme.js`) e CSS movido para `assets/theme.css`
- [x] Incluído em `index.html` + as 6 páginas de `pages/` (`bootcamps`, `bootcamp`, `modules`, `module`, `projects`, `project`)
- [x] `document.documentElement.lang` dinâmico em todas elas (via `renderShell`/`render` de cada página + aplicação antecipada em `lang.js`)
- [x] Sintaxe JS de todas as páginas validada com `node --check`

**Ainda pendente**
- [ ] Traduzir os labels fixos de `assets/theme.js` (seletor de tema: "Claro"/"Escuro"/"Sistema"), caso quisermos o seletor de tema também em italiano
- [ ] Revisão humana da tradução das 43 aulas (feita por agentes automatizados seguindo as diretrizes da seção 6 — vale uma passada de revisão antes de publicar)
- [ ] `pages/lesson.html` e `pages/contact.html` continuam fora do escopo (vazios, sem implementação nem em pt_br)
