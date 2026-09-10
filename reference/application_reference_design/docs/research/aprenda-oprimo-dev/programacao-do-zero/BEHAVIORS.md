# BEHAVIORS — trilha "Programação do Zero"

Extraído do HTML SSR das 13 páginas + do chunk cliente
`/_next/static/chunks/app/trilhas/%5Bslug%5D/%5BnodeId%5D/page-d5cd6efdba79a5d1.js`.

## 1. Sidebar de aulas

- **Estado ativo:** `aria-current="page"` no `<a>`; classe `bg-brand-green/10 font-semibold text-brand-green`;
  círculo numerado ganha `border-brand-green text-brand-green`.
- **Estado inativo:** `text-muted-foreground`, círculo `border-border text-muted-foreground`.
- **Hover inativo:** `hover:bg-card hover:text-foreground`, `transition-colors`.
- **Sticky:** `sticky top-16 max-h-[calc(100vh-5rem)] overflow-y-auto pb-8 pr-2`.
- **Progresso:** trilho `h-1 rounded-full bg-border`; preenchimento `h-full rounded-full bg-brand-green transition-all`,
  `style="width:N%"`. Rótulo: `N/13 concluídos` (font-mono, 11px, muted).
- Anônimo no site original → sempre `0/13` e `width:0%`.

## 2. Drawer mobile

`<details class="mb-6 rounded-lg border border-border bg-card/50 lg:hidden">`
`<summary>` = `☰ Aulas · Programação do Zero · 0/13`, `list-style:none`, cursor pointer,
font-mono 12px bold uppercase tracking-widest muted. Corpo com `border-t` e a mesma `<ol>`.

## 3. Controle de tamanho de fonte

Três botões `A−` / `A` / `A+` alinhados à direita, precedidos do rótulo `fonte`
(font-mono 11px uppercase tracking-widest muted). Botões: `h-8 min-w-8 rounded-md border border-border px-2`,
hover `border-foreground/40 text-foreground`, `disabled:opacity-40`.
O botão do meio começa **desabilitado** (tamanho já é o padrão).
Aplicam `style="font-size:1rem"` no container `.prose`.

## 4. NodeStatus (marcar progresso)

Três chips: `Estudando` (ativo: `border-brand-cyan bg-brand-cyan/15 text-brand-cyan`),
`Concluído` (ativo: `border-brand-green bg-brand-green/15 text-brand-green`),
`Pular` (ativo: `border-muted-foreground bg-muted text-muted-foreground`).
Clicar no chip já ativo volta o estado para `pending` (toggle).
No site original, anônimo vê apenas o aviso pontilhado "Entre para acompanhar seu progresso e ganhar XP.".

## 5. Quiz (só em `variaveis`)

Container `not-prose my-8 rounded-xl border border-border bg-card p-5`.
- Kicker `// Quiz` (font-mono 11px bold uppercase tracking-widest, **brand-cyan**).
- Pergunta: `text-base font-semibold sm:text-lg`.
- Alternativas: `<label>` com radio + texto; hover `border-foreground/40 bg-background/30`.
- **Após responder** (`selected !== null`) todos os radios ficam `disabled`:
  - escolhida e correta → `border-brand-green/60 bg-brand-green/10` + sufixo `✓`
  - escolhida e errada → `border-destructive/60 bg-destructive/10` + sufixo `✗`
  - não escolhida e correta → `border-brand-green/40 bg-brand-green/5`
  - demais → `border-border opacity-60`
- Painel de feedback (`aria-live="polite"`): título `Acertou!` (brand-green) ou `Ainda não.` (destructive),
  explicação da alternativa escolhida, e — se errou — linha `Resposta certa:` (kicker brand-cyan) com a
  explicação da correta. Botão `Tentar de novo` reseta a seleção.

## 6. Checkpoint / Playground JS

Cabeçalho: `// Checkpoint · +10 XP` (brand-cyan) à esquerda; status à direita:
`pendente` (muted) → `rodando…` (brand-orange) → `✓ passou` (brand-green) / `✗ falhou` (destructive).
Depois o enunciado (`text-sm font-semibold`), depois o Playground:
- barra `playground · js` (brand-cyan) + botão `▶ Rodar` (vira `rodando…` enquanto executa);
- editor de código (mono, `max-h-[22rem]`, scroll);
- área `saída`: antes de rodar "Clique em Rodar para ver o resultado."; sem logs "(sem saída)";
  logs `error` em destructive, `warn` em brand-orange, resto em foreground.
- **Timeout de 5s** → log de erro `⏱️ Execução excedeu 5s - worker terminado (provável loop infinito).`
- **Aprovação:** junta os logs de nível `log`/`info` com `\n` e compara por igualdade exata com `expected`.
- Painel `✓ Passou!` + `+10 XP creditados. O nó foi marcado como concluído.`
- Painel de falha: `Saída diferente da esperada` + `Esperado: <code>` + `Saída: <code>` (ou `(vazia)`)
  + `Edite o código, clique em Rodar, e tente novamente.`
- Execução isolada: `<iframe sandbox="allow-scripts" src="/playground.html">` + Web Worker.

Desafios encontrados (só estes 4 nós têm Checkpoint):

| nodeId | challenge | starterCode | expected |
|---|---|---|---|
| variaveis | Crie uma variável `nome` com o valor 'Ana' e imprima no console. | `let nome = '';\nconsole.log(nome);` | `Ana` |
| operadores | Imprima o resto da divisão de 17 por 5 (operador %). | `console.log();` | `2` |
| loops | Use um for para imprimir os números de 1 a 3, um por linha. | `for (let i = 1; i <= 3; i++) {\n  // imprima i aqui\n}` | `1\n2\n3` |
| funcoes | Crie uma função dobro(n) que devolve n * 2 e imprima dobro(21). | `function dobro(n) {\n  // seu código aqui\n}\nconsole.log(dobro(21));` | `42` |

## 7. Blocos de código do conteúdo

`<div class="group relative">` + botão `copiar` posicionado `absolute right-2 top-2`,
`opacity-0 group-hover:opacity-100 focus-visible:opacity-100`,
hover `border-brand-green text-brand-green`. Conteúdo em `<pre><code class="language-*">`.
Linguagens usadas: `js` (8), `javascript` (4), `bash` (2), `python` (1).
**Sem realce de sintaxe** no SSR — o Prism só é usado dentro do editor do playground.

## 8. Avaliação da trilha

`// avaliação da trilha` → card com `—` (font-display 3xl black), 5 estrelas `★`
em `text-muted-foreground/40`, e `ainda sem avaliações` (font-mono 11px muted).
Idêntico nos 13 nós (a trilha não tem avaliações).

## 9. Pager entre aulas

`border-t border-border pt-6`, dois cards flex-1 `rounded-lg border border-border bg-card p-3`,
hover `border-brand-cyan` e o título vira `text-brand-cyan`.
Esquerda: `← anterior`; direita alinhada à direita: `próxima →`.
Nó 01 não tem "anterior"; nó 13 não tem "próxima".

## 10. Responsivo

- **≥1024px:** grid `15rem / 1fr`, sidebar visível, drawer oculto.
- **<1024px:** sidebar oculta, drawer `<details>` acima do artigo, coluna única.
- **≥640px:** `h1` vai de `text-3xl` para `text-4xl`; padding lateral de 1rem para 1.5rem.
- **390px:** tudo em coluna; os dois cards do pager continuam lado a lado (flex-1).

## 11. Tokens de cor do original (dark)

`--background #131320` · `--foreground #f8f8f2` · `--card #191a28` · `--border #2b2c44`
`--muted-foreground #9aa0c4` · `--primary #bd93f9` · `--destructive #ff5555`
`--brand-green #50fa7b` · `--brand-cyan #8be9fd` · `--brand-purple #bd93f9` · `--brand-pink #ff79c6`

**Adaptação no clone:** o `programacao_do_zero.html` segue a paleta do `index.html`
(fundo `#000`, card `#0d0d16`), e `--brand-green` (acento do original) é substituído por
`--brand-indigo #7d6cff`, que é o acento do repositório — mesma decisão já aplicada em
`trilhas.html` e `projetos.html`. `--destructive #ff5555` foi adicionado para os estados de erro.
Fundo do `<pre>` do original é `rgba(0,0,0,.5)`; sobre fundo preto isso some, então o clone usa
`var(--card)` com borda.
