# ReadyToDeploy
Python do zero ao primeiro deploy. Curso completo para iniciantes que querem colocar código em produção.

https://enzoschitini.github.io/ReadyToDeploy/

# Estrutura do Projeto

## Visão Geral

O projeto é organizado em três grandes áreas, que trabalham em conjunto:

| Área | Função |
|---|---|
| `index` (pages) | Estrutura **base** de todas as páginas — o layout/rota de cada tela |
| `course_content` | Conteúdo **educacional** salvo em JSON (bootcamps, módulos, aulas, projetos...) |
| `application_content` | Conteúdo **fixo da aplicação** (textos de UI, labels etc.), sem ser o conteúdo educacional |

Tanto `pages` quanto `application_content` seguem exatamente a mesma árvore de rotas — a diferença é que uma define a estrutura/layout e a outra guarda os textos daquela estrutura.

---

## 1. `index` — Raiz do Projeto (Base)

Pasta `pages`: contém a estrutura base de todas as páginas. Somente o conteúdo vindo do JSON muda de uma página para outra.

```
pages
├── bootcamps                  → Listagem dos bootcamps
│   └── bootcamp                → Página de um bootcamp selecionado
│       └── modules             → Listagem de módulos (hoje chamados de "trilhas")
│           └── module          → Página de um módulo (trilha) selecionado
│               └── lesson      → Página de conteúdo de uma aula do módulo
├── projects                   → Listagem de todos os projetos
│   └── project                 → Página de um projeto específico
└── contact                    → Hoje chamada de "Ranking", será a página de contato
```

### Detalhamento das rotas

| Rota | Descrição |
|---|---|
| `bootcamps` | Lista todos os bootcamps disponíveis |
| `bootcamps/bootcamp` | Exibe os detalhes de um bootcamp selecionado |
| `bootcamps/bootcamp/modules` | Lista os módulos ("trilhas") do bootcamp |
| `bootcamps/bootcamp/modules/module` | Exibe um módulo (trilha) específico |
| `bootcamps/bootcamp/modules/module/lesson` | Exibe o conteúdo de uma aula do módulo |
| `projects` | Lista todos os projetos |
| `projects/project` | Exibe um projeto específico |
| `contact` | Página de contato *(atualmente chamada de "Ranking" — será substituída)* |

---

## 2. `course_content` — Conteúdo Educacional (JSON)

Pasta `pt_br`: conteúdos em português, organizados por tipo, cada arquivo com `id` próprio e (quando aplicável) o `id` da entidade "pai".

```
course_content
└── pt_br
    ├── bootcamps        → id próprio
    ├── modules          → id próprio + id do bootcamp
    ├── lessons          → id próprio + id do módulo
    ├── projects         → id próprio + id do bootcamp
    ├── presentations    → id próprio + id do módulo  (ainda não utilizado)
    ├── quiz             → id próprio + id do módulo  (ainda não utilizado)
    └── research         → id próprio + id do módulo  (ainda não utilizado)
```

### Relação entre entidades

| JSON | ID Próprio | Relacionado a (ID) | Status |
|---|---|---|---|
| `bootcamps` | id do bootcamp | — | ✅ Em uso |
| `modules` | id do módulo | id do bootcamp | ✅ Em uso |
| `lessons` | id da aula | id do módulo | ✅ Em uso |
| `projects` | id do projeto | id do bootcamp | ✅ Em uso |
| `presentations` | id da apresentação | id do módulo | ⏳ Não implementado |
| `quiz` | id do quiz | id do módulo | ⏳ Não implementado |
| `research` | id da pesquisa | id do módulo | ⏳ Não implementado |

---

## 3. `application_content` — Conteúdo da Aplicação

Pasta `pt_br`: contém o conteúdo **real/fixo da interface** (não o conteúdo educacional), espelhando a mesma árvore de `pages`.

```
application_content
└── pt_br
    └── index
        ├── bootcamps
        │   └── bootcamp
        │       └── modules
        │           └── module
        │               └── lesson
        ├── projects
        │   └── project
        └── contact
```

> Essa estrutura é idêntica à de `pages`, garantindo que cada rota tenha seu conjunto correspondente de textos/labels da aplicação.

---

## Resumo

- **`pages`** define a estrutura/layout das telas.
- **`course_content`** fornece o conteúdo educacional dinâmico (via JSON, relacionado por IDs).
- **`application_content`** fornece os textos fixos da interface, seguindo a mesma árvore de `pages`.