# Comportamentos — /projetos

Extraídos do bundle do cliente (lógica exata, não estimada).

## 1. Normalização de texto (`S8`)
```js
s => s.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "")
```
Usada tanto na busca de projetos quanto na busca dentro do dropdown de tópicos.

## 2. Filtro de projetos (`J8`) — AND entre critérios, OR dentro de cada um
```js
projects.filter(p =>
  (levels.size === 0 || levels.has(p.difficulty)) &&
  (skills.size === 0 || p.skills.some(s => skills.has(s))) &&
  (!q || norm(`${p.title} ${p.description} ${p.skills.join(" ")}`).includes(q))
)
```
`q = norm(query.trim())`.

## 3. Lista de tópicos (`P9`)
Conta ocorrências de cada `skill` em todos os projetos e ordena por
`count desc`, empate → `name.localeCompare(other, "pt-BR")`.

## 4. Botões de Nível
`aria-pressed` alterna. Inativo: `border-border text-muted-foreground`,
hover → `border-brand-green text-foreground`.
Ativo: `border-brand-green bg-brand-green/15 text-brand-green`.

## 5. Dropdown Tópico
- Abre/fecha por clique; fecha em `mousedown` fora e em `Escape`.
- Botão ganha estilo ativo + badge com a contagem (`bg-brand-green/25 px-1 tabular-nums`) quando há tópicos selecionados.
- Caret `▾` recebe `rotate-180` aberto (`transition-transform`).
- Painel: `absolute z-20 mt-2 w-full rounded-xl border bg-card p-2 shadow-lg sm:w-64`, `autoFocus` no input.
- Input `placeholder="Filtrar tópicos…"`; lista `max-h-64 overflow-y-auto`.
- Item: checkbox `size-3.5 rounded-[3px]` com `✓`, nome truncado, contagem à direita (`tabular-nums`).
- Lista vazia → `nenhum tópico`.

## 6. Contador e chips
- Texto: `{visíveis} de {total} projeto` + `s` quando `total !== 1`.
- Cada filtro ativo vira um chip `border-brand-green bg-brand-green/15` com botão `✕` (`aria-label="Remover filtro <x>"`).
- Botão `limpar` aparece só quando há qualquer filtro ativo; zera busca, níveis e tópicos.

## 7. Badge "novo" (`isNew`)
`Date.now() - Date.parse(published) <= 30 dias` (e não negativo).
Renderizado só após a montagem no cliente. Todos os 22 projetos têm
`published` entre 2026-08-25 e 2026-08-30.

## 8. Seções por nível
Ordem fixa `iniciante → intermediario → avancado`; seção com 0 resultados
não é renderizada. Com 0 resultados totais, o grid é substituído por
`Nenhum projeto encontrado com esses filtros.`

## 9. Hover no card
`border-border → border-brand-green` e `h3` → `text-brand-green`
(`transition-colors`).

## 10. Responsivo
- `sm` (640px): grid de cards vira 2 colunas; label "Nível" aparece;
  grupo de níveis vira flex; dropdown vira `w-64` ancorado à direita (`sm:ml-auto`).
- `md` (768px): nav do header aparece, botão de menu some.

## Não implementado no clone
`TrendingBadge` ("em alta") e `RatingBadge` (★ média) vêm de uma instância
PocketBase externa; não estão no HTML do servidor e não têm dados públicos
recuperáveis sem backend.
