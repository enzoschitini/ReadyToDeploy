# /trilhas — Topologia da página

Fonte: https://aprenda.oprimo.dev/trilhas (Next.js App Router, SSR + hidratação).
Destino: `trilhas.html` (arquivo estático único, seguindo o design system de `index.html`).

## Ordem visual (topo → base)

| # | Seção | Tipo | Modelo de interação |
|---|-------|------|---------------------|
| 1 | Skip link `#conteudo` | acessibilidade | foco |
| 2 | Header sticky (`~/.ready-to-deploy.py` + nav) | sticky overlay, z-40 | estático + menu mobile (click) |
| 3 | Breadcrumb `Início / Trilhas` | fluxo | estático |
| 4 | `<h1>Trilhas</h1>` + lead | fluxo | estático |
| 5 | **FilterBar** (busca, níveis, dropdown Tópico, contador, chips, limpar) | fluxo | **click + input, client-side** |
| 6 | Grade de 41 cards (`sm:grid-cols-2`) | fluxo | hover nos cards |
| 7 | Estado vazio ("Nenhuma trilha encontrada com esses filtros.") | condicional | reage aos filtros |
| 8 | Footer (4 colunas + barra inferior) | fluxo | hover nos links |

## Layout de página

- Container: `max-width: 72rem` (`max-w-6xl`), `padding-inline: 1rem` (`sm:1.5rem`).
- Conteúdo principal: `padding-block: 3rem` (`sm:4rem`).
- Sem hero, sem orbes animados, sem scroll-snap. O `<main>` é fluxo simples.
- Camadas z: header `z-40`, dropdown de tópicos `z-20`, barra de progresso de scroll `z-50` (adicionada por paridade com `index.html`).

## Dados (extraídos do RSC flight payload)

41 roadmaps, cada um com: `slug`, `title`, `description`, `difficulty`
(`iniciante|intermediario|avancado`), `published` (opcional, ISO), `skills[]`, `creators[]`,
`nodes[]` (usado só para `nodes.length` → contagem de nós).

362 tópicos distintos derivados de `skills`, ordenados por contagem desc e depois
por `localeCompare(pt-BR)`.

## Diferenças assumidas no clone

- `TrendingBadge` ("em alta") e `RatingBadge` (★ nota) são buscados no Firestore em runtime.
  Sem backend, os valores foram capturados do DOM hidratado do site original
  (Chrome headless, `--dump-dom`) e embutidos estaticamente: 3 selos "em alta"
  (programacao-do-zero, backend, git) e 24 notas. São um snapshot de 2026-09-07 — não atualizam sozinhos.
- Paleta: `index.html` substitui `--brand-green` do original por `--brand-indigo` (#7d6cff).
  Todo `brand-green` do original vira `--brand-indigo` aqui.
