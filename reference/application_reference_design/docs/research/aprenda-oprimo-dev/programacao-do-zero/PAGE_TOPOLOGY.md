# PAGE_TOPOLOGY — trilha "Programação do Zero" (13 nós)

Origem: `https://aprenda.oprimo.dev/trilhas/programacao-do-zero/<nodeId>`
Destino: `programacao_do_zero.html` (arquivo único, roteamento por hash)

## URLs de origem → estado local

| # | nodeId | h1 do artigo | título na sidebar | hash local |
|---|--------|--------------|-------------------|-----------|
| 01 | logica | Lógica de Programação | Pensamento Computacional | `#logica` |
| 02 | ambiente | Configurando o Ambiente | Configurando o Ambiente | `#ambiente` |
| 03 | variaveis | Variáveis e Tipos | Variáveis e Tipos | `#variaveis` |
| 04 | operadores | Operadores e Expressões | Operadores e Expressões | `#operadores` |
| 05 | condicionais | Condicionais | Condicionais | `#condicionais` |
| 06 | loops | Laços e Iteração | Laços e Iteração | `#loops` |
| 07 | funcoes | Funções | Funções | `#funcoes` |
| 08 | strings | Strings e Manipulação de Texto | Strings e Manipulação de Texto | `#strings` |
| 09 | arrays | Listas (Arrays) | Listas (Arrays) | `#arrays` |
| 10 | objetos | Objetos e Dicionários | Objetos e Dicionários | `#objetos` |
| 11 | debug | Depuração e Leitura de Erros | Depuração e Leitura de Erros | `#debug` |
| 12 | git-basico | Git: add, commit, push | Git: add, commit, push | `#git-basico` |
| 13 | projeto-final | Seu Primeiro Projeto | Seu Primeiro Projeto | `#projeto-final` |

Observação: só o nó 01 tem título da sidebar diferente do `<h1>` do artigo. Ambos foram preservados.

## Layout (idêntico nos 13 nós)

```
header (sticky, do index.html)
scroll-progress (fixed, do index.html)
main
└─ .container  →  lg: grid-template-columns: 15rem minmax(0,1fr); gap 2.5rem
   ├─ <aside>  (hidden abaixo de 1024px)
   │   └─ sticky top:4rem; max-height calc(100vh - 5rem); overflow-y auto
   │      ├─ "← Programação do Zero"
   │      ├─ barra de progresso (h .25rem) + "N/13 concluídos"
   │      └─ <ol> 13 nós: círculo numerado (size 1.25rem) + título truncado
   ├─ <details> drawer (só abaixo de 1024px) — "☰ Aulas · Programação do Zero · N/13"
   └─ .lesson-main (min-width:0)
      └─ <article> por nó (max-width 48rem):
         breadcrumb → badge ★ essencial → h1 → tempo de leitura
         → NodeStatus (Estudando / Concluído / Pular)
         → controle de fonte (A− A A+, alinhado à direita)
         → .prose (conteúdo markdown renderizado)
         → [Quiz]        (só em variaveis)
         → [Checkpoint]  (variaveis, operadores, loops, funcoes)
         → section "// recursos"
         → section "// avaliação da trilha"
         → nav pager (← anterior | próxima →)
footer (do index.html)
```

## Modelo de interação por seção

| Seção | Modelo |
|---|---|
| header | estático + menu mobile por clique |
| scroll-progress | scroll-driven (scaleX) |
| sidebar | click-driven (troca de nó) + estado ativo derivado do hash |
| drawer mobile | `<details>` nativo, click-driven |
| NodeStatus | click-driven, persiste em localStorage |
| controle de fonte | click-driven, aplica `font-size` inline na `.prose` |
| copiar código | click-driven, `navigator.clipboard` |
| Quiz | click-driven, uma tentativa por vez + "Tentar de novo" |
| Checkpoint | click-driven ("▶ Rodar"), executa em iframe sandbox com timeout |
| pager | click-driven (navegação entre nós) |
| reveal | scroll-driven (IntersectionObserver), padrão do index.html |
