# /trilhas — Comportamentos

Extraídos do bundle de produção (`chunks/app/trilhas/page-*.js`, `chunks/2755-*.js`,
módulo `43333` = helpers de filtro, módulo `1544` = NewBadge).

## Modelo de interação global

**Click/input-driven.** Não há nada scroll-driven nesta página: sem IntersectionObserver,
sem scroll-snap, sem parallax, sem animation-timeline, sem biblioteca de smooth scroll.
O header é `position: sticky` puro e **não** muda de aparência ao rolar.

## FilterBar

Estado: `query: string`, `levels: Set<'iniciante'|'intermediario'|'avancado'>`, `skills: Set<string>`.

### Busca (input `type="search"`)
- Placeholder: `Buscar trilhas por nome, descrição ou tópico…`
- `focus` → `border-color` passa de `--border` para o accent. Sem outline.
- Normalização: `s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')`
  (case- e acento-insensível).
- Escopo da busca: `${title} ${description} ${skills.join(' ')}` normalizado, `.includes(query)`.

### Pills de nível
- 3 botões: Iniciante / Intermediário / Avançado. **Toggle múltiplo** (Set), não rádio.
- Inativo: `border: 1px solid var(--border)`, `color: var(--muted-foreground)`.
- Hover inativo: `border-color: accent`, `color: var(--foreground)`.
- Ativo: `border-color: accent`, `background: accent/15`, `color: accent`, `aria-pressed="true"`.
- Layout: `grid-cols-3` full-width no mobile; `flex` com largura automática a partir de `sm`.

### Dropdown "Tópico"
- Botão: label `Tópico` + (se houver seleção) contador em `bg accent/25 px-1 tabular-nums` + caret `▾`.
- Caret gira 180° quando aberto (`transition-transform`).
- Botão fica no estado "ativo" (mesmas cores da pill ativa) quando `skills.size > 0`.
- Painel: `absolute`, `mt-2`, `rounded-xl`, `border`, `bg-card`, `p-2`, `shadow-lg`,
  `z-20`; full-width no mobile, `width: 16rem` alinhado à direita a partir de `sm`.
- Dentro: input `Filtrar tópicos…` (autofocus) + lista `max-height: 16rem; overflow-y: auto`.
- Cada item: checkbox quadrado `3.5` (`✓` quando marcado), nome truncado, contagem à direita.
- Fecha com: clique fora (`mousedown` fora do wrapper) ou tecla `Escape`.
- Lista vazia → `nenhum tópico`.

### Linha de contagem
- `{n} de {total} trilha{s}` em fonte mono, `--muted-foreground`.
- Chips removíveis para cada nível e cada tópico ativo, com botão `✕`
  (`aria-label="Remover filtro <x>"`).
- Botão `limpar` (só aparece se houver qualquer filtro ativo): cor accent, `hover:underline`.

### Lógica de filtragem (AND entre grupos, OR dentro do grupo)
```
levels.size === 0 || levels.has(r.difficulty)
&& skills.size === 0 || r.skills.some(s => skills.has(s))
&& !query || normalize(title + description + skills).includes(normalize(query))
```
Zero resultados → a grade some e aparece
`<p class="rounded-xl border border-dashed …">Nenhuma trilha encontrada com esses filtros.</p>`.

## Card de trilha
- Link inteiro para `/trilhas/<slug>`.
- `transition-colors`; hover → `border-color` accent e o `<h3>` muda para accent
  (grupo hover, não hover individual).
- Selo "novo" (`NewBadge`): aparece só no client, quando
  `0 <= Date.now() - Date.parse(published) <= 30 dias`.
  Em 2026-09-07 isso dá 6 trilhas: acessibilidade-web (2026-08-29), angular (2026-08-29),
  conventional-commits (2026-08-31), estruturas-de-dados (2026-08-26), nextjs (2026-08-28),
  rabbitmq-mensageria (2026-08-26).
- Contagem de nós: `{n} nó` se 1, `{n} nós` caso contrário.

## Header
- `position: sticky; top: 0; z-index: 40`, `backdrop-filter: blur(8px)`, `background: bg/60`.
- Link ativo (`/trilhas`): `background: var(--muted)`, `color: var(--foreground)`, `aria-current="page"`.
- Menu mobile: botão hambúrguer só abaixo de `md`; abre/fecha lista vertical.

## Responsivo
| Largura | Mudanças |
|---------|----------|
| 1440px | grade 2 colunas; pills de nível em linha; dropdown alinhado à direita (`ml-auto`, 16rem) |
| 768px (`sm` = 640px já aplicado) | idem desktop; padding do container 1.5rem |
| 390px | grade 1 coluna; pills em `grid-cols-3` full-width; dropdown full-width; label "Nível" oculto; nav principal oculta (hambúrguer) |
