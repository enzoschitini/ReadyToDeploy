---
name: gerar-modulo-html
description: Publica um módulo do curso "Ready To Deploy" no site, a partir de um notebook pronto em content_generation/jupyter_notebooks/module_NN.ipynb - quebra o notebook em uma página HTML por tópico dentro de course_content/<lang>/<bootcamp>/<módulo>/ e cadastra tudo em modules.json, lessons.json e bootcamps.json. Use SEMPRE que o usuário pedir para publicar, cadastrar, subir, transformar em página/HTML ou "colocar no site" um módulo ou aula do curso (ex: "cadastra o módulo 2 no bootcamp Python na Prática", "transforma o module_03.ipynb em páginas", "publica o módulo de listas"), mesmo que não fale em "skill", "HTML" ou "padrão". Não use para gerar o .ipynb em si (isso é a skill gerar-modulo-ipynb).
---

# Publicar módulo em HTML — Ready To Deploy

O site é estático: `pages/module.html?id=<module_id>` monta a casca (cabeçalho, barra lateral
com os tópicos, progresso, quiz, rodapé) e busca o corpo de cada aula em um arquivo HTML.
Publicar um módulo é, então, duas coisas: **quebrar o notebook em uma página por tópico** e
**cadastrar essas páginas nos três JSONs** que o site lê.

Cada tópico do notebook vira um item da barra lateral esquerda. É assim que o aluno navega:
uma aula por vez, com "anterior/próxima" no fim.

## Arquivos da skill

- `scripts/construtor_pagina.py`: classe `Pagina` com `p()`, `h2()`, `lista()`, `tabela()`,
  `citacao()`, `codigo()`, `quiz()` e `salvar()`. Ela escapa o HTML sozinha (inclusive o
  `<class 'int'>` das saídas, que sumiria da tela) e aceita **Markdown inline**
  (`**negrito**`, `` `código` ``, `*itálico*`). Use-a em vez de escrever HTML na mão.
- `scripts/registrar_modulo.py`: recebe um manifesto e cadastra o módulo e as aulas.
  É ele que monta o campo `content` como `<bootcamp>/<módulo>/<arquivo>`.
- `scripts/validar_modulo_html.py`: confere cadastro + páginas (caminhos que resolvem,
  tags balanceadas, código escapado, quizzes coerentes, currículo liberado).
- `references/exemplo_modulo_01.py`: **padrão ouro**. É o script da primeira aula do Módulo 01,
  aprovado pelo autor, com o manifesto correspondente. Leia antes de publicar, para calibrar o
  recorte dos blocos e o tom. O resultado completo das 5 aulas está em
  `course_content/pt_br/python-na-pratica/python-variaveis-e-tipos-de-dados/`.

## Fluxo de trabalho

1. **Leia o notebook inteiro** em `content_generation/jupyter_notebooks/module_NN.ipynb`.
   Anote as seções `## N.`, as subseções `### N.M`, os exemplos e as saídas de cada célula de
   código (elas viram comentário no HTML). Se o notebook não existir, avise o usuário e sugira
   gerá-lo antes com a skill `gerar-modulo-ipynb`.
2. **Leia `references/exemplo_modulo_01.py`** (pelo menos uma vez por sessão).
3. **Descubra o bootcamp e o `module_id` em `course_content/<lang>/bootcamps.json`.** Os módulos
   já estão no currículo do bootcamp, com id definido e `"disabled": true` — **use o id que está
   lá**, não invente um. Ex: o módulo 2 do Python na Prática é
   `python-estruturas-de-dados`. Se não houver item no currículo, pergunte ao usuário onde o
   módulo entra em vez de criar um bootcamp ou um id por conta própria.
4. **Quebre o notebook em aulas** (veja "Do notebook para as aulas").
5. **Escreva o script de geração** no scratchpad, importando o construtor, e rode-o.
   Ele imprime, para cada página, o `readTime` sugerido.
6. **Escreva o manifesto** (também no scratchpad) e rode o `registrar_modulo.py`.
7. **Rode o validador** e corrija até `APROVADO`.
8. **Informe ao usuário** (veja "Relatório final").

```python
import sys
sys.path.insert(0, r"<caminho absoluto desta skill>/scripts")
from construtor_pagina import Pagina

pagina = Pagina()
pagina.p("Uma **lista** guarda vários valores em ordem, dentro de uma só variável.")
pagina.h2("Definição")
pagina.tabela(["Método", "O que faz"], [["`.append(x)`", "Acrescenta `x` no fim"]])
pagina.codigo("""
compras = ["arroz", "feijão"]
compras.append("café")
print(compras)  # ['arroz', 'feijão', 'café']
""")
pagina.citacao("**Atenção:** `.sort()` altera a lista original e devolve `None`.")
pagina.quiz("python-listas", "O que `.append()` devolve?", [
    ("A lista nova", "Ele altera a lista no lugar e devolve None.", False),
    ("None", "Por isso `lista = lista.append(x)` apaga a sua lista.", True),
])
pagina.salvar(r"course_content/pt_br/python-na-pratica/python-estruturas-de-dados/listas.html")
```

```bash
python <skill>/scripts/registrar_modulo.py <scratchpad>/manifesto.json
python <skill>/scripts/validar_modulo_html.py python-estruturas-de-dados
```

Rodar o registrador de novo com o mesmo manifesto é seguro: ele substitui o módulo e as aulas,
não duplica, e não reformata as entradas dos outros módulos.

## Onde cada coisa mora

```
course_content/<lang>/
├── bootcamps.json   currículo de cada bootcamp (o item do módulo, com "disabled")
├── modules.json     o módulo (title, description, level, nodes, skills)
├── lessons.json     as aulas (id, module_id, order, title, navTitle, readTime, content, resources)
└── <bootcamp>/<módulo>/<aula>.html     o corpo de cada aula
```

O campo `content` da aula é o caminho **relativo a `course_content/<lang>/`**, e é o único elo
entre o cadastro e o arquivo: se ele não bater com a pasta, a aula abre com "Não foi possível
carregar o conteúdo desta aula". Por isso o `content` é montado pelo registrador, e o validador
confere se cada um resolve em disco.

Para ver o resultado no navegador é preciso um servidor HTTP (por `file://` o `fetch` dos JSONs
falha): `python -m http.server 8000` e abrir
`http://localhost:8000/pages/module.html?id=<module_id>`.

## Do notebook para as aulas

- **Uma seção `## N.` do notebook = uma aula = um item da barra lateral.** O `navTitle` é o
  rótulo curto da lateral; o `title` é o `<h1>` da página.
- **Não repita o título da aula** dentro do HTML: o `<h1>` vem do `title` do lessons.json.
- As subseções `### N.M` viram `h2` — é o único nível de título que o tema estiliza.
- O cabeçalho do notebook (`# Módulo NN`, curso, autor) e a tabela `## Tópicos` **não** viram
  página: viram `title`/`description` do `modules.json`.
- As células `---` de separação somem (cada aula já é uma página).
- O `## Resumo do Módulo` entra no fim da **última** aula, como uma seção `h2`.
- Célula de código + saída viram **um** bloco de `codigo()`, com a saída como comentário
  (`print(idade)  # 30`). Quando forem várias linhas de saída, use um bloco `# Saída:` no fim.
- Links no meio do texto saem da prosa e viram `resources` da aula no manifesto — é o padrão
  do site, que já mostra uma lista de recursos abaixo do conteúdo.
- **Um quiz por aula**, no fim, com 4 alternativas e explicação em todas (ela aparece tanto no
  acerto quanto no erro, então ensina em vez de julgar).
- `readTime`: use o número que o `salvar()` sugerir, ajustando se a aula for mais densa.

## O que o site não tem (e o notebook tem)

- **Não há LaTeX.** Fórmulas `$$...$$` do notebook viram texto ou um bloco de código simples
  (`ticket médio = valor total das vendas / quantidade de vendas`).
- **Não há realce de sintaxe.** A classe `language-python` é só semântica; o que dá legibilidade
  são os comentários.
- **O playground executa JavaScript**, num Web Worker. Em módulos de Python **não use** o bloco
  `.checkpoint` (o código do aluno seria avaliado como JS e daria erro). Só o `quiz` funciona
  para qualquer linguagem.
- **Só `h2` é estilizado** na prosa. Não use `h3`.
- Tabelas precisam do embrulho `.table-wrap` (o construtor já faz) para rolar no celular.

## Estilo

O conteúdo já vem pronto do notebook, então aqui o trabalho é **transpor sem perder**, não
reescrever. Valem as mesmas regras da skill `gerar-modulo-ipynb`: nomes em português e
`snake_case`, comentários curtos que explicam a intenção, termos em inglês em itálico, código
entre crases. Preserve a progressão "Motivação → Definição → Operações → Conversão →
Revisitando a motivação" quando o notebook tiver — fechar o problema do início é o que dá
sentido à aula.

Os emojis de `> 💡 **Dica:**` e `> ⚠️ **Atenção:**` do notebook saem: no site quem dá o destaque
é a barra lateral da citação. Mantenha as palavras **Dica:** e **Atenção:** em negrito.

## Relatório final ao usuário

Responda de forma breve com:

1. Quantas aulas foram publicadas, em que pasta, e que o validador aprovou.
2. A lista de aulas na ordem da barra lateral (título → o que cobre), em uma linha cada.
3. O que mudou no cadastro (módulo criado ou atualizado, currículo liberado).
4. O que ficou de fora do notebook e por quê (ex: um checkpoint interativo que o site não roda).

Não repita o conteúdo das aulas: o usuário vai abrir a página.
