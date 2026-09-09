# Topologia — https://aprenda.oprimo.dev/projetos

Origem: SSR HTML + payload RSC (`self.__next_f`) + chunk do cliente
`/_next/static/chunks/app/projetos/page-*.js` e `/_next/static/chunks/2755-*.js`.

## Ordem das seções (topo → base)

| # | Seção | Modelo de interação |
|---|-------|---------------------|
| 1 | Header sticky (`h-14`, `backdrop-blur`, nav com "Projetos" ativo) | estático + menu mobile |
| 2 | Breadcrumb `Início / Projetos` (separador em `brand-purple`) | estático |
| 3 | `<h1>Projetos</h1>` + parágrafo de abertura | estático |
| 4 | Barra de filtros (busca, Nível, Tópico, contador, chips, "limpar") | **input/click-driven** |
| 5 | Seções por nível: `// Iniciante`, `// Intermediário`, `// Avançado` | derivadas do filtro |
| 6 | Grid de cards (`mt-4 grid gap-4 sm:grid-cols-2`) — 22 projetos | hover nos cards |
| 7 | Estado vazio (`border-dashed`, `py-12`) | aparece com 0 resultados |
| 8 | Footer (idêntico ao da home) | hover nos links |

Não há hero, orbs, stats, manifesto, idealizador ou seção de contribuição —
a página é índice puro. Não há scroll-driven behavior, scroll-snap,
parallax nem biblioteca de smooth scroll.

## Dados

22 projetos, cada um com: `slug`, `title`, `description`, `difficulty`
(`iniciante` | `intermediario` | `avancado`), `published`, `skills[]`,
`trilhas[]`, `estimate`, `creators[]`. Ver `projects.json`.

- 63 tópicos (`skills`) distintos
- distribuição: 5 iniciante · 15 intermediário · 2 avançado
