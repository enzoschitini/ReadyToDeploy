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

> ⚠️ Estado atual da implementação: a **página inicial** (`index.html`) e a **listagem de bootcamps** (`pages/bootcamps.html`) já estão implementadas, com seus JSON correspondentes. Os demais arquivos de `pages` e de conteúdo ainda são **placeholders vazios**.
>
> Na tela de bootcamps os cards ainda **não navegam**: a tela `bootcamp.html` não existe, então cada card é um `<article>` sem link. A única navegação até ela vem do menu do `index.html`.

### Como o HTML consome os JSON

Cada página busca seu conteúdo com `fetch` no carregamento:

| Página | Textos da interface | Conteúdo educacional |
|---|---|---|
| `index.html` | `application_content/pt_br/index.json` | `course_content/pt_br/modules.json`, `course_content/pt_br/projects.json` |
| `pages/bootcamps.html` | `application_content/pt_br/bootcamps.json` | `course_content/pt_br/bootcamps.json` |

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