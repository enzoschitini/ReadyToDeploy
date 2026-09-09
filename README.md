# ReadyToDeploy
Python do zero ao primeiro deploy. Curso completo para iniciantes que querem colocar código em produção.

https://enzoschitini.github.io/ReadyToDeploy/

# Estrutura do Projeto

## Visão Geral

O projeto é organizado em quatro partes, que trabalham em conjunto:

| Parte | Função |
|---|---|
| `index.html` (raiz) | Página inicial da aplicação |
| `pages` | Estrutura **base** em HTML de cada tela — o layout/rota |
| `course_content` | Conteúdo **educacional** salvo em JSON (bootcamps, módulos, aulas, projetos...) |
| `application_content` | Conteúdo **fixo da aplicação** (textos de UI, labels etc.), sem ser o conteúdo educacional |

`pages` e `application_content` seguem o **mesmo conjunto de arquivos** (mesmo nome, um `.html` e um `.json` para cada tela) — a diferença é que um define a estrutura/layout e o outro guarda os textos daquela tela. Hoje todas as pastas são **planas** (sem subpastas): não existe aninhamento tipo `bootcamps/bootcamp/modules/...`, cada tela é um arquivo solto nomeado pela própria rota.

> ⚠️ Estado atual da implementação: a **página inicial** (`index.html`), as listagens de **bootcamps** (`pages/bootcamps.html`), **trilhas** (`pages/modules.html`) e **projetos** (`pages/projects.html`), e as páginas de **detalhe de um bootcamp** (`pages/bootcamp.html`), de **um projeto** (`pages/project.html`) e de **uma trilha** (`pages/module.html`) já estão implementadas, com seus JSON correspondentes. `pages/lesson.html` e `pages/contact.html` ainda são **placeholders vazios**.
>
> `pages/module.html` é a tela de estudo de uma trilha: sidebar com todas as aulas, progresso, e o conteúdo da aula ativa. Ela concentra as duas rotas — a trilha vem do `?id=` e a aula do **hash** (`module.html?id=programacao-do-zero#variaveis`) — então `pages/lesson.html` continua sem uso por enquanto. Hoje só a trilha `programacao-do-zero` tem aulas publicadas; em `pages/modules.html` só os cards de trilhas com aula viram link, os outros continuam sem navegação.
>
> Os cards de `pages/bootcamps.html` e `pages/projects.html` já navegam de verdade para `bootcamp.html?id=<id>` e `project.html?id=<id>`. Mas nem todo item tem o conteúdo de detalhe completo: só o bootcamp `desenvolvedor-backend` tem `detail.curriculum`/`detail.creator`, e só o projeto `calculadora-de-gorjeta` tem `detail.introHtml`/`requirements`/etc. (ver "Convenções dos campos" abaixo). Os demais bootcamps/projetos abrem a mesma página com cabeçalho, descrição e avaliação, mas sem currículo/enunciado — as seções que dependem do `detail` simplesmente não aparecem em vez de ficarem em branco.
>
> As páginas de detalhe (`bootcamp.html`, `project.html`, `module.html`) leem o item pelo `?id=` da própria URL, não por navegação de estado — abrir a URL direto (ou dar F5 nela) funciona igual. Sem `?id=` ou com um `id` que não existe, mostram um painel "não encontrado" com link de volta pra listagem. Em `module.html` o hash da aula também sobrevive ao F5, e a aula concluída fica salva no `localStorage` do navegador.

### Como o HTML consome os JSON

Cada página busca seu conteúdo com `fetch` no carregamento:

| Página | Textos da interface | Conteúdo educacional |
|---|---|---|
| `index.html` | `application_content/pt_br/index.json` | `course_content/pt_br/modules.json`, `course_content/pt_br/projects.json` |
| `pages/bootcamps.html` | `application_content/pt_br/bootcamps.json` | `course_content/pt_br/bootcamps.json` |
| `pages/bootcamp.html` | `application_content/pt_br/bootcamp.json` | `course_content/pt_br/bootcamps.json` (filtrado pelo `?id=` da URL) |
| `pages/modules.html` | `application_content/pt_br/modules.json` | `course_content/pt_br/modules.json` |
| `pages/projects.html` | `application_content/pt_br/projects.json` | `course_content/pt_br/projects.json` |
| `pages/project.html` | `application_content/pt_br/project.json` | `course_content/pt_br/projects.json` (filtrado pelo `?id=` da URL), `course_content/pt_br/modules.json` (nomes das trilhas praticadas) |
| `pages/module.html` | `application_content/pt_br/module.json` | `course_content/pt_br/modules.json` (filtrado pelo `?id=` da URL), `course_content/pt_br/lessons.json` (aulas do módulo) e, sob demanda, o `.html` de cada aula |

Como o conteúdo vem por `fetch`, o site precisa ser aberto por **HTTP** (GitHub Pages ou um servidor local como `python -m http.server`) — abrir o arquivo direto por `file://` bloqueia o carregamento dos JSON e a página mostra um aviso.

---

## 1. `index.html` — Página Inicial

Na raiz do projeto, junto com `favicon.svg`. É a home da aplicação, fora da pasta `pages`. Seu conteúdo de texto correspondente fica em `application_content/pt_br/index.json` (não existe um `course_content` associado a ela, pois não é uma tela de curso).

---

## 2. `pages` — Telas da Aplicação (HTML)

Pasta plana: cada arquivo é uma tela/rota da aplicação. Somente o conteúdo vindo do JSON muda de uma página para outra.

```
pages
├── bootcamps.html    → Listagem dos bootcamps
├── bootcamp.html     → Página de um bootcamp selecionado
├── modules.html      → Listagem de módulos (hoje chamados de "trilhas")
├── module.html       → Página de um módulo (trilha) selecionado
├── lesson.html       → Página de conteúdo de uma aula do módulo
├── projects.html     → Listagem de todos os projetos
├── project.html      → Página de um projeto específico
└── contact.html      → Hoje chamada de "Ranking", será a página de contato
```

### Detalhamento das telas

| Tela | Descrição |
|---|---|
| `bootcamps` | Lista todos os bootcamps disponíveis |
| `bootcamp` | Exibe os detalhes de um bootcamp selecionado |
| `modules` | Lista os módulos ("trilhas") de um bootcamp |
| `module` | Exibe um módulo (trilha) específico |
| `lesson` | Exibe o conteúdo de uma aula do módulo |
| `projects` | Lista todos os projetos |
| `project` | Exibe um projeto específico |
| `contact` | Página de contato *(atualmente chamada de "Ranking" — será substituída)* |

---

## 3. `course_content` — Conteúdo Educacional (JSON)

Pasta `pt_br`: conteúdos em português, organizados por tipo, cada arquivo com `id` próprio e (quando aplicável) o `id` da entidade "pai".

```
course_content
└── pt_br
    ├── bootcamps.json   → id próprio
    ├── modules.json     → id próprio + id do bootcamp
    ├── lessons.json     → id próprio + id do módulo + caminho do .html da aula
    ├── projects.json    → id próprio + id do bootcamp
    └── programacao-do-zero/   → uma pasta por módulo, com o conteúdo das aulas
        ├── logica.html
        ├── ambiente.html
        └── ...                (um .html por aula, nomeado pelo id dela)
```

### A aula em si é HTML, não JSON

Os arquivos soltos em `pt_br` são o **catálogo** (o que existe, como se relaciona, como aparece nas listagens). Já o **conteúdo ensinado** — o texto da aula, os blocos de código, o quiz, o checkpoint — mora num `.html` próprio, dentro de uma pasta com o `id` do módulo. Prosa é prosa: escrever isso como string de JSON seria escapar HTML dentro de JSON, sem ganho nenhum.

Cada pasta de módulo tem um `.html` por aula, e `lessons.json` amarra os dois lados: cada aula tem `content` com o caminho do arquivo, relativo a `course_content/<lang>/`. Isso mantém a tradução simples — um `course_content/en/programacao-do-zero/logica.html` (com `course_content/en/lessons.json` apontando pra ele) é tudo que uma segunda língua precisa, sem tocar em `pages`.

Campos de uma aula em `lessons.json`:

| Campo | Uso |
|---|---|
| `id` | Id da aula. Vira o **hash** da URL (`module.html?id=<módulo>#<id>`) e a chave do progresso salvo. |
| `module_id` | Id do módulo dono da aula (`modules.json`). |
| `order` | Posição na trilha — define a numeração da sidebar e o "anterior/próxima". |
| `title` | Título da aula, no `<h1>` e no breadcrumb. |
| `navTitle` | Título curto na sidebar. Quando ausente, a sidebar usa o `title`. |
| `badge` | Selo acima do título (ex.: `essencial`). Opcional. |
| `readTime` | Tempo estimado de leitura. Opcional. |
| `content` | Caminho do `.html` da aula, relativo a `course_content/<lang>/`. |
| `resources` | Links da seção "// recursos": `name`, `href` e `tags[]` (`{ label, free }`). Lista vazia → a seção some. |

O `.html` da aula é um **fragmento**, não um documento: sem `<html>`, `<head>` ou `<style>`, porque ele é injetado dentro do artigo que `module.html` monta (breadcrumb, cabeçalho, botões de progresso e de fonte, recursos, avaliação e pager vêm da página, não do arquivo). O que o arquivo traz:

```html
<div class="prose"> … texto, listas, blockquotes, blocos de código … </div>

<div class="quiz" …>       …  (opcional)
<div class="checkpoint" …> …  (opcional)
```

Quiz e checkpoint ficam **no HTML da aula**, e não no JSON, justamente pra que o autor decida onde eles entram no meio do texto. As classes que a página estiliza e ativa por JS são:

| Bloco | Marcação esperada |
|---|---|
| Bloco de código | `.code-block` com um `<button class="copy-btn">` e um `<pre><code>`. O rótulo do botão vem do JSON — o texto dentro dele é sobrescrito. |
| Quiz | `.quiz` com `.quiz-opt` por alternativa (`data-correct="1"` na certa, `data-exp` com a explicação) e um `.quiz-feedback` vazio. |
| Checkpoint | `.checkpoint` com `data-expected` (a saída exata esperada), `.cp-challenge`, um `<textarea>` com o código inicial, `.btn-run`, `.pg-out`, `.cp-result` e a `<iframe class="pg-frame" sandbox="allow-scripts">`. Passar no checkpoint marca a aula como concluída. |

O código do checkpoint roda num Web Worker dentro da iframe sandbox, com timeout de 5s — assim um loop infinito é interrompido de verdade, sem travar a página.

### Relação entre entidades

| JSON | ID Próprio | Relacionado a (ID) |
|---|---|---|
| `bootcamps` | id do bootcamp | — |
| `modules` | id do módulo | id do bootcamp |
| `lessons` | id da aula | id do módulo (+ `content`, o `.html` da aula) |
| `projects` | id do projeto | id do bootcamp |

### Convenções dos campos

Campos que se repetem entre os tipos de conteúdo:

| Campo | Uso |
|---|---|
| `level` | Rótulo de exibição (`Iniciante`, `Intermediário`, `Avançado`). As telas normalizam o valor (minúsculas, sem acento) quando precisam dele como chave — ex.: as seções por nível em `projects.html`. |
| `skills` | Lista de tópicos do item. Alimenta as tags dos cards e o filtro "Tópico" da tela de projetos. |
| `published` | Data ISO de publicação. O selo "novo" é derivado dela (últimos 30 dias), não gravado no JSON. |
| `hot` / `rating` | Opcionais; quando ausentes, o card simplesmente não mostra o selo/avaliação. |
| `detail` | Só existe em itens que já têm página de detalhe própria. Guarda o que a listagem não usa; ausente ou com listas vazias → a seção correspondente da página some, em vez de aparecer em branco. Formato varia por tipo (ver linhas abaixo). |
| `detail` de **projeto** | Hoje só em `calculadora-de-gorjeta`: `introHtml`, `objectiveHtml`, `requirements[]`, `challenges[]`, `tips[]`, `trilhas[]` (ids de módulos praticados, viram pílulas linkando `module.html?id=`) e `creator` (`{ name, github }`). |
| `detail` de **bootcamp** | Hoje só em `desenvolvedor-backend`: `creator` (`{ name, github }`) e `curriculum[]` — a jornada em ordem, cada item `{ type: "trilha" \| "projeto", id, title, description }`. `type` decide o badge (Trilha/Projeto) e o link do item: `trilha` → `module.html?id=<id>`, `projeto` → `project.html?id=<id>`. Nem todo `id` de trilha do currículo existe em `modules.json` (ex.: `terminal-para-devs`, `typescript`) — o link já fica pronto pra quando esses módulos forem cadastrados; até lá `module.html` abre com o painel "trilha não encontrada". |

Campos (ou itens de lista) cujo nome termina em **`Html`**, ou que estão dentro de `detail.requirements`/`detail.challenges`/`detail.tips`, guardam HTML já pronto (podem ter `<code>`, `<strong>`) e são inseridos com `innerHTML` — o mesmo padrão já usado em `application_content` (`quoteHtml`, `licenseHtml` etc.). Os demais campos são texto puro, inserido com `textContent`.

> Tipos adicionais como apresentações e pesquisas (ver `application_reference_design/Estrutura dos Conteúdos.md`) ainda não têm arquivo/pasta próprios em `course_content` — serão adicionados quando forem implementados. Quiz e checkpoint já existem, mas como marcação dentro do `.html` da aula, não como tipo de conteúdo separado.

### Publicando uma nova trilha

1. Adicione o módulo em `course_content/pt_br/modules.json` (com `id`, `bootcamp_id`, `nodes` etc.).
2. Crie `course_content/pt_br/<id-do-módulo>/` e escreva um `.html` por aula.
3. Registre cada aula em `course_content/pt_br/lessons.json`, com `module_id`, `order` e `content`.

Nada em `pages` muda: o card na listagem passa a linkar sozinho e `module.html?id=<id>` já serve a trilha.

---

## 4. `application_content` — Conteúdo da Aplicação

Pasta `pt_br`: contém o conteúdo **real/fixo da interface** (não o conteúdo educacional), com um arquivo `.json` para cada tela de `pages`, mais um `index.json` para a página inicial.

```
application_content
└── pt_br
    ├── index.json       → textos da página inicial (index.html)
    ├── bootcamps.json
    ├── bootcamp.json
    ├── modules.json
    ├── module.json     → textos da tela de estudo de uma trilha
    ├── lesson.json
    ├── projects.json
    ├── project.json
    └── contact.json
```

> Cada arquivo aqui corresponde 1:1 a um arquivo de `pages` (mesmo nome), exceto `index.json`, que corresponde ao `index.html` da raiz.

---

## Resumo

- **`index.html`** é a porta de entrada da aplicação.
- **`pages`** define a estrutura/layout de cada tela (arquivos planos, um por rota).
- **`course_content`** fornece o conteúdo educacional dinâmico: o catálogo em JSON (relacionado por IDs) e o conteúdo das aulas em HTML, numa pasta por módulo.
- **`application_content`** fornece os textos fixos da interface, espelhando os arquivos de `pages` (mais `index.json` para a home).

> A pasta `application_reference_design` na raiz **não** faz parte da estrutura da aplicação — é material de referência/mockup usado para planejar o design e os conteúdos.