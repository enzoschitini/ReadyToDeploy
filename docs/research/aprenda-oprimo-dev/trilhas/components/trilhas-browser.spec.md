# TrilhasBrowser — Especificação

## Overview
- **Arquivo destino:** `trilhas.html` (seções `.filter-bar` + `.card-grid` + estado vazio)
- **Modelo de interação:** click + input, 100% client-side, sem scroll-driven
- **Origem:** módulos webpack `67546` (TrilhasBrowser), `12368` (FilterBar), `78293` (RoadmapCard), `43333` (helpers)

## Estrutura DOM
```
div.mt-8.flex.flex-col.gap-8
├── div.flex.flex-col.gap-4                  ← FilterBar
│   ├── input[type=search]
│   ├── div.flex.flex-wrap.items-center.gap-2
│   │   ├── span "Nível"  (hidden < sm)
│   │   ├── div.grid.grid-cols-3.gap-2 (sm:flex)   ← 3 pills
│   │   └── div.w-full (sm:ml-auto sm:w-auto)      ← dropdown Tópico
│   │       └── div.relative > button + div.absolute (painel)
│   └── div.flex.flex-wrap.items-center.gap-2.text-xs
│       ├── span "41 de 41 trilhas"
│       ├── chips removíveis (nível/tópico)
│       └── button "limpar"
└── div.grid.gap-4.sm:grid-cols-2            ← 41 × <a> card
    │ (ou) p.rounded-xl.border-dashed        ← estado vazio
```

## Estilos computados (valores exatos)

### Input de busca
- width: 100%; border-radius: 0.75rem; border: 1px solid var(--border)
- background: var(--card); padding: 0.75rem 1rem; font-size: 0.875rem
- color: var(--foreground); outline: none; transition: border-color .15s
- placeholder color: var(--muted-foreground)
- **:focus** → border-color: accent

### Pill de nível
- border-radius: 0.375rem; border: 1px solid; padding: 0.25rem 0.625rem
- font-family: mono; font-size: 0.75rem; transition: colors .15s
- inativo: border var(--border) / color var(--muted-foreground)
- hover: border accent / color var(--foreground)
- ativo: border accent / background accent 15% / color accent

### Botão "Tópico"
- display: flex; align-items: center; gap: 0.375rem; border-radius: 0.375rem
- padding: 0.375rem 0.625rem (sm: 0.25rem 0.625rem); font mono 0.75rem
- w-full + justify-center no mobile; w-auto + justify-start a partir de sm
- badge de contagem: border-radius 0.125rem; background accent/25; padding-inline 0.25rem; tabular-nums
- caret `▾`: transition-transform; `rotate(180deg)` quando aberto

### Painel do dropdown
- position: absolute; margin-top: 0.5rem; z-index: 20
- left:0; right:0 (mobile) → sm: left:auto; right:0; width: 16rem
- border-radius: 0.75rem; border 1px var(--border); background var(--card)
- padding: 0.5rem; box-shadow: 0 10px 15px -3px rgb(0 0 0/.1), 0 4px 6px -4px rgb(0 0 0/.1)
- input interno: mb-2; border-radius 0.375rem; background var(--background); padding 0.375rem 0.625rem; mono 0.75rem
- lista: max-height 16rem; overflow-y auto
- item: flex; gap 0.5rem; border-radius 0.375rem; padding 0.375rem 0.5rem; mono 0.75rem; hover background var(--muted)
- checkbox: size 0.875rem; border-radius 3px; border 1px var(--border) → marcado: border accent + background accent/20
- contagem à direita: margin-left auto; tabular-nums; color var(--muted-foreground)

### Card (idêntico ao `.card` de index.html)
- display: flex; flex-direction: column; gap: 0.75rem
- border-radius: 0.75rem; border 1px var(--border); background var(--card); padding: 1.25rem
- transition: border-color .15s; **hover** → border-color accent; `h3` → accent
- h3: font-display; 1.25rem; weight 800; uppercase; color var(--card-foreground)
- p: 0.875rem; color var(--muted-foreground)
- badge de nível: bg brand-cyan/15; color brand-cyan; mono 0.75rem; padding 0.125rem 0.5rem
- "ver trilha →": margin-top auto; mono 0.75rem; color accent

### Estado vazio
- border-radius 0.75rem; border 1px **dashed** var(--border)
- padding: 3rem 1rem; text-align center; font-size 0.875rem; color var(--muted-foreground)
- texto: `Nenhuma trilha encontrada com esses filtros.`

## Estados e comportamentos
Ver `../BEHAVIORS.md` (seção FilterBar) — lógica de filtro, normalização de acentos,
fechamento por Escape/clique-fora, regra de 30 dias do selo "novo".

## Conteúdo
41 trilhas com `slug`, `title`, `description`, `difficulty`, `nodes.length`, `published`, `skills[]`,
extraídas literalmente do RSC payload de https://aprenda.oprimo.dev/trilhas.
362 tópicos distintos no dropdown, ordenados por contagem desc + `localeCompare('pt-BR')`.

## Responsivo
- **1440px:** grade 2 colunas, pills inline, dropdown à direita com 16rem
- **768px:** igual (breakpoint `sm` = 640px)
- **390px:** grade 1 coluna, pills `grid-cols-3` full-width, dropdown full-width, label "Nível" oculto
