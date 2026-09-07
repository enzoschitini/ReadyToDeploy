# ARTIFACT_MANIFEST — trilha "Programação do Zero"

## Origem → destino

| URL de origem | Destino |
|---|---|
| `/trilhas/programacao-do-zero/logica` | `programacao_do_zero.html#logica` |
| `/trilhas/programacao-do-zero/ambiente` | `programacao_do_zero.html#ambiente` |
| `/trilhas/programacao-do-zero/variaveis` | `programacao_do_zero.html#variaveis` |
| `/trilhas/programacao-do-zero/operadores` | `programacao_do_zero.html#operadores` |
| `/trilhas/programacao-do-zero/condicionais` | `programacao_do_zero.html#condicionais` |
| `/trilhas/programacao-do-zero/loops` | `programacao_do_zero.html#loops` |
| `/trilhas/programacao-do-zero/funcoes` | `programacao_do_zero.html#funcoes` |
| `/trilhas/programacao-do-zero/strings` | `programacao_do_zero.html#strings` |
| `/trilhas/programacao-do-zero/arrays` | `programacao_do_zero.html#arrays` |
| `/trilhas/programacao-do-zero/objetos` | `programacao_do_zero.html#objetos` |
| `/trilhas/programacao-do-zero/debug` | `programacao_do_zero.html#debug` |
| `/trilhas/programacao-do-zero/git-basico` | `programacao_do_zero.html#git-basico` |
| `/trilhas/programacao-do-zero/projeto-final` | `programacao_do_zero.html#projeto-final` |

Arquivo único, como `index.html`, `trilhas.html` e `projetos.html`. Os 13 nós ficam
todos no DOM e o hash decide qual `<article>` fica visível.

## Assets

Nenhum. As 13 páginas de origem não têm imagens, vídeos ou SVGs próprios — só texto,
blocos de código e ícones já presentes no `index.html` (menu, GitHub). Fontes vêm do
Google Fonts, iguais às do `index.html`.

## Conteúdo

Extraído do HTML SSR de cada nó (`docs/research/.../lessons.json`) e do payload RSC
para os componentes só-cliente (quiz e checkpoints, documentados em `BEHAVIORS.md`).
O texto renderizado da `.prose` do clone foi comparado palavra a palavra com o do
original nos 13 nós: **idêntico** (a única diferença é o rótulo "copiar" do botão de
código, que existe nos dois).

## Adaptações conscientes

1. **Paleta.** O acento do original é `--brand-green #50fa7b`; o clone usa
   `--brand-indigo #7d6cff`, o acento do `index.html` — mesma decisão já aplicada em
   `trilhas.html` e `projetos.html`. `--destructive #ff5555` foi adicionado.
2. **Fundo dos blocos de código.** O original usa `rgba(0,0,0,.5)` sobre `#131320`;
   sobre o preto do `index.html` isso sumiria, então o clone usa `var(--card)` + borda.
3. **Login.** O original esconde NodeStatus, Quiz e Checkpoint atrás de login
   (anônimo vê só um aviso pontilhado). O clone entrega a experiência de usuário
   logado, com progresso em `localStorage` em vez de PocketBase.
4. **Roteamento.** 13 URLs viraram 13 hashes num arquivo só.

## Lacunas conhecidas

- **Sem realce de sintaxe no editor do playground.** O original usa
  `react-simple-code-editor` + Prism dentro do editor; o clone usa um `<textarea>`
  monoespaçado. Os blocos de código do conteúdo não são realçados nem no original.
- **Sem transpilação de TypeScript.** O original passa o código por sucrase antes de
  rodar; o clone executa JavaScript direto. Os 4 desafios da trilha são JS puro.
- **Sem tela cheia no playground.** O original tem um botão de fullscreen.
- **Sem XP/ranking real.** O texto "+10 XP creditados" é reproduzido, mas não há backend.
- **Avaliação da trilha** é estática (`—` / "ainda sem avaliações"), como no original hoje.

## Execução de código do usuário

Igual ao original em substância: `<iframe sandbox="allow-scripts">` com `srcdoc`
(origem opaca, sem acesso ao documento pai) e, dentro dela, um **Web Worker** criado a
partir de um Blob. `console.log/info/warn/error` são interceptados e devolvidos por
`postMessage`. Timeout de 5s → `worker.terminate()`.

O worker é essencial: um `while(true){}` numa iframe sandbox trava o processo de
renderização daquele contexto, e recriar a iframe **não** resolve (a nova também não
carrega). Só `terminate()` interrompe de fato. Verificado no navegador:
loop infinito → timeout → a execução seguinte volta a funcionar normalmente.
