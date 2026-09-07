# Especificação — página de nó da trilha (`programacao_do_zero.html`)

- **Arquivo alvo:** `programacao_do_zero.html`
- **Conteúdo verbatim:** `docs/research/aprenda-oprimo-dev/programacao-do-zero/lessons.json`
- **Comportamentos:** `../BEHAVIORS.md`
- **Modelo de interação:** click-driven (sidebar/pager/hash) + scroll-driven (progress bar, reveal)

## Estilos computados relevantes (do original)

### Grid da página
`max-width:72rem; padding-inline:1rem; padding-block:2rem`
`@media (min-width:640px){padding-inline:1.5rem}`
`@media (min-width:1024px){display:grid; grid-template-columns:15rem minmax(0,1fr); gap:2.5rem}`

### Sidebar
`position:sticky; top:4rem; max-height:calc(100vh - 5rem); overflow-y:auto; padding-bottom:2rem; padding-right:.5rem`
- back link: font-mono, 11px, 700, uppercase, `letter-spacing:.1em`, `color:var(--muted-foreground)`; hover → `var(--foreground)`
- trilho: `margin-top:.5rem; height:.25rem; border-radius:9999px; background:var(--border); overflow:hidden`
- preenchimento: `height:100%; border-radius:9999px; background:var(--brand-indigo); transition:all .15s`
- rótulo: `margin-top:.375rem; font-mono; 11px; color:var(--muted-foreground)`
- item: `display:flex; align-items:center; gap:.75rem; border-radius:.375rem; padding:.375rem .5rem .375rem .625rem; font-size:.875rem; transition:color .15s, background-color .15s`
- círculo: `width/height:1.25rem; border-radius:9999px; border:1px solid; font-mono; 10px; 700`
- ativo: `background:rgba(125,108,255,.10); font-weight:600; color:var(--brand-indigo)`; círculo `border-color/color:var(--brand-indigo)`
- título do item: `min-width:0; flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap`

### Artigo
`max-width:48rem; padding-bottom:3rem`
- breadcrumb: font-mono `.75rem`, separador `/` em `var(--brand-purple)`, atual em `var(--foreground)`
- badge: `inline-flex; gap:.25rem; border-radius:.375rem; padding:.125rem .5rem; font-mono .75rem 500; background:rgba(125,108,255,.15); color:var(--brand-indigo)`
- h1: `margin-top:.75rem; font-display; 1.875rem; 900; uppercase; letter-spacing:-.025em` → `2.25rem` em ≥640px
- tempo de leitura: `margin-top:.5rem; font-mono .75rem; color:var(--muted-foreground)`
- `.prose`: `margin-top:1rem; font-size:1rem` (mutável via controle de fonte)
  - `p`: `margin-block:1.25em`
  - `strong`: `color:#fff; font-weight:600`
  - `code` inline: `font-size:.875em; font-weight:600; color:var(--brand-indigo)` (original: brand-green)
  - `pre`: `padding:.857143em 1.14286em; border-radius:.375rem; margin-block:1.71429em; font-size:.875em; line-height:1.71429; overflow-x:auto`
  - `blockquote`: `border-inline-start:.25rem solid; padding-inline-start:1em; margin-block:1.6em; font-style:italic; font-weight:500`
  - `h2`: font-display, `margin-top:2em; margin-bottom:1em; font-size:1.5em; font-weight:700`
  - `ul/ol`: `padding-inline-start:1.625em; margin-block:1.25em`; `li` `margin-block:.5em`

### Seções finais
- kicker `// recursos` / `// avaliação da trilha`: `font-mono .875rem 700 uppercase; letter-spacing:.1em; color:var(--muted-foreground)`; seções com `margin-top:3rem`
- card de recurso: `border-radius:.5rem; border:1px solid var(--border); background:var(--card); padding:1rem; gap:.5rem`; hover `border-color:var(--brand-cyan)`
- tag: `border-radius:.375rem; border:1px solid; padding:.125rem .5rem; font-mono .75rem 500`; "Grátis" com `background:rgba(125,108,255,.15); color:var(--brand-indigo); border-color:transparent`
- pager: `margin-top:3rem; border-top:1px solid var(--border); padding-top:1.5rem`; cards `flex:1; border-radius:.5rem; border:1px solid var(--border); background:var(--card); padding:.75rem`; hover `border-color:var(--brand-cyan)` e título vira cyan

## Estados

| Estado | Gatilho | Antes → Depois |
|---|---|---|
| nó ativo | hash / clique na sidebar / pager | item muted → indigo com fundo `rgba(125,108,255,.1)`; artigo correspondente sai de `hidden` |
| progresso | clique em "Concluído" | `width:0%` → `width:(n/13*100)%`, `transition:all .15s`; contador `N/13` |
| fonte | A− / A / A+ | `font-size` da `.prose` entre `0.875rem` e `1.25rem`, passo `0.0625rem`; botão do meio `disabled` quando `1rem` |
| copiar | clique | rótulo `copiar` → `copiado!` por 1.6s |
| quiz | escolha de alternativa | radios desabilitados + cores por acerto/erro + painel de feedback |
| checkpoint | ▶ Rodar | `pendente` → `rodando…` → `✓ passou` / `✗ falhou`; timeout 5s |

## Textos verbatim
Todos em `lessons.json` (prose HTML, títulos, tempo de leitura, recursos) e em `BEHAVIORS.md`
(quiz, desafios, mensagens de UI).

## Responsivo
- ≥1024px: grid 15rem/1fr, sidebar visível, drawer oculto
- <1024px: coluna única, drawer `<details>` acima do artigo
- ≥640px: h1 2.25rem, padding lateral 1.5rem
