# Especificação — projetos.html

## Visão geral
- **Arquivo alvo:** `projetos.html` (raiz do repo, irmão de `index.html`)
- **Fonte do conteúdo:** https://aprenda.oprimo.dev/projetos
- **Fonte do layout:** `index.html` (tokens, header, cards, footer reaproveitados na íntegra)
- **Screenshots:** `docs/design-references/aprenda-oprimo-dev/projetos/`
- **Modelo de interação:** input/click-driven (busca, níveis, tópicos). Sem scroll-driven.

## Mapeamento de design (original → index.html)

| Original (Tailwind) | Neste arquivo |
|---|---|
| `brand-green` (destaque, hover, CTA) | `--brand-indigo` (`#7d6cff`) |
| `variant="info"` do badge de nível | `.badge` (ciano) |
| card `rounded-xl border bg-card p-5 gap-3` | `.card` |
| `mt-4 grid gap-4 sm:grid-cols-2` | `.card-grid` |
| `font-mono text-sm font-bold uppercase tracking-widest` | `.kicker` |
| badge "novo" `rounded-full border px-2 py-0.5 text-[10px]` | `.pill-new` |
| `border-border text-foreground` (skill) | `.tag` |
| header/footer | reaproveitados de `index.html` sem alteração |

Adições visuais em relação ao original, para alinhar com `index.html`:
barra de progresso de scroll, grid-lines + orbs suaves atrás do cabeçalho
(`.page-bg`, altura 32rem, opacidade .16/.18) e `Entrar` no header.

## Estrutura
```
header.site-header (Projetos com .is-active)
main#conteudo
  .scroll-progress
  .page-wrap
    .page-bg  (grid-lines + orb-pink + orb-purple)
    .container.page-main
      nav.crumbs        Início / Projetos
      h1.page-title     PROJETOS
      p.page-lead
      .browser
        .filters
          input#q.search-input
          .filter-row  → .filter-label + .level-group (3 .chip-btn) + .topic-wrap
          .count-row   → #count-text + chips ativos + limpar
        #level-sections → 3 <section> (iniciante / intermediario / avancado)
        p#empty-state
footer.site-footer
```

## Valores computados (medidos no original)
- container: `max-width 72rem`, `padding-inline 1rem` (`1.5rem` ≥640px)
- `main` da página: `padding-block 3rem` (`4rem` ≥640px)
- breadcrumb: mono `.75rem`, `gap .375rem`, separador `--brand-purple`
- `h1`: display, `900`, uppercase, `1.875rem` → `2.25rem` ≥640px, `tracking -.025em`, `margin-top 1rem`
- lead: `margin-top .5rem`, `max-width 65ch`, `--muted-foreground`
- busca: `border-radius .75rem`, `padding .75rem 1rem`, `font-size .875rem`, foco → borda indigo
- chip de nível: `border-radius .375rem`, `padding .25rem .625rem`, mono `.75rem`
- dropdown: `w 100%` (`16rem` ≥640px), `padding .5rem`, `border-radius .75rem`, lista `max-height 16rem`
- grid de cards: `gap 1rem`, 1 coluna → 2 colunas em `640px`
- seções: `gap 2.5rem` entre níveis
- estado vazio: `border dashed`, `padding 3rem 1rem`, centralizado

## Estados e comportamentos
Ver `../BEHAVIORS.md` — a lógica de filtro (`norm`, AND entre critérios, OR dentro
de cada um), a ordenação dos tópicos (`count desc → nome pt-BR`), o texto do
contador, os chips com `✕`, o botão `limpar`, a regra de 30 dias do badge "novo"
e o fechamento do dropdown por `mousedown` externo/`Escape` foram portados 1:1.

## Dados
`../projects.json` — 22 projetos com `slug`, `title`, `description`, `difficulty`,
`published`, `skills[]`, `trilhas[]`, `estimate`, `creators[]`.
Cada card carrega `data-slug`, `data-difficulty`, `data-skills`, `data-published`
e `data-haystack` (título + descrição + skills), consumidos pelo filtro.

## Responsivo
- **≥768px:** nav do header visível, botão de menu oculto
- **≥640px:** cards em 2 colunas; label "Nível" visível; grupo de níveis vira flex; dropdown `16rem` ancorado à direita (`margin-left:auto`)
- **<640px:** tudo em coluna única; níveis em grid de 3 colunas full-width; botão Tópico full-width

## Lacunas conhecidas
- `TrendingBadge` ("em alta") e `RatingBadge` (★) dependem de uma instância
  PocketBase externa; não vêm no HTML do servidor e ficaram de fora.
- Os cards apontam para `#` com `data-slug`, seguindo a convenção de links
  placeholder já usada em `index.html` (as páginas de detalhe não existem no repo).
