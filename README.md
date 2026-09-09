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

> ⚠️ Estado atual da implementação: a **página inicial** (`index.html`), as listagens de **bootcamps** (`pages/bootcamps.html`), **trilhas** (`pages/modules.html`) e **projetos** (`pages/projects.html`), e a página de **detalhe de um projeto** (`pages/project.html`) já estão implementadas, com seus JSON correspondentes. Os demais arquivos de `pages` e de conteúdo ainda são **placeholders vazios**.
>
> Nas listagens os cards ainda **não navegam**: as telas de detalhe de bootcamp e de módulo (`bootcamp.html`, `module.html`) não existem, então esses cards são `<article>` sem link. A única navegação até essas listagens vem do menu do `index.html`.
>
> `pages/project.html` já funciona como destino (`pages/project.html?id=<id>`), mas por ora só o projeto `calculadora-de-gorjeta` tem o conteúdo de detalhe completo (ver `detail` em "Convenções dos campos" abaixo) — os outros 21 abrem a mesma página com um cabeçalho básico e sem enunciado/requisitos. O card dele em `pages/projects.html` ainda **não** foi religado para lá, para não fugir do escopo pedido; é um `<a href="pages/project.html?id=calculadora-de-gorjeta">` de uma linha quando quiserem ativar.

### Como o HTML consome os JSON

Cada página busca seu conteúdo com `fetch` no carregamento:

| Página | Textos da interface | Conteúdo educacional |
|---|---|---|
| `index.html` | `application_content/pt_br/index.json` | `course_content/pt_br/modules.json`, `course_content/pt_br/projects.json` |
| `pages/bootcamps.html` | `application_content/pt_br/bootcamps.json` | `course_content/pt_br/bootcamps.json` |
| `pages/modules.html` | `application_content/pt_br/modules.json` | `course_content/pt_br/modules.json` |
| `pages/projects.html` | `application_content/pt_br/projects.json` | `course_content/pt_br/projects.json` |
| `pages/project.html` | `application_content/pt_br/project.json` | `course_content/pt_br/projects.json` (filtrado pelo `?id=` da URL), `course_content/pt_br/modules.json` (nomes das trilhas praticadas) |

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
    ├── lessons.json     → id próprio + id do módulo
    └── projects.json    → id próprio + id do bootcamp
```

### Relação entre entidades

| JSON | ID Próprio | Relacionado a (ID) |
|---|---|---|
| `bootcamps` | id do bootcamp | — |
| `modules` | id do módulo | id do bootcamp |
| `lessons` | id da aula | id do módulo |
| `projects` | id do projeto | id do bootcamp |

### Convenções dos campos

Campos que se repetem entre os tipos de conteúdo:

| Campo | Uso |
|---|---|
| `level` | Rótulo de exibição (`Iniciante`, `Intermediário`, `Avançado`). As telas normalizam o valor (minúsculas, sem acento) quando precisam dele como chave — ex.: as seções por nível em `projects.html`. |
| `skills` | Lista de tópicos do item. Alimenta as tags dos cards e o filtro "Tópico" da tela de projetos. |
| `published` | Data ISO de publicação. O selo "novo" é derivado dela (últimos 30 dias), não gravado no JSON. |
| `hot` / `rating` | Opcionais; quando ausentes, o card simplesmente não mostra o selo/avaliação. |
| `detail` | Só existe em itens que já têm página de detalhe própria (hoje, só o projeto `calculadora-de-gorjeta`). Guarda o que a listagem não usa: `introHtml`, `objectiveHtml`, `requirements[]`, `challenges[]`, `tips[]`, `trilhas[]` (ids de módulos praticados) e `creator` (`{ name, github }`). Ausente ou com listas vazias → a seção correspondente da página some, em vez de aparecer em branco. |

Campos (ou itens de lista) cujo nome termina em **`Html`**, ou que estão dentro de `detail.requirements`/`detail.challenges`/`detail.tips`, guardam HTML já pronto (podem ter `<code>`, `<strong>`) e são inseridos com `innerHTML` — o mesmo padrão já usado em `application_content` (`quoteHtml`, `licenseHtml` etc.). Os demais campos são texto puro, inserido com `textContent`.

> Tipos adicionais como apresentações, quiz e pesquisas (ver `application_reference_design/Estrutura dos Conteúdos.md`) ainda não têm arquivo/pasta próprios em `course_content` — serão adicionados quando forem implementados.

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
    ├── module.json
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
- **`course_content`** fornece o conteúdo educacional dinâmico (via JSON, relacionado por IDs).
- **`application_content`** fornece os textos fixos da interface, espelhando os arquivos de `pages` (mais `index.json` para a home).

> A pasta `application_reference_design` na raiz **não** faz parte da estrutura da aplicação — é material de referência/mockup usado para planejar o design e os conteúdos.