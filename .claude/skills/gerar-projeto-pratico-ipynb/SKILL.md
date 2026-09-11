---
name: gerar-projeto-pratico-ipynb
description: Gera o projeto prático em .ipynb (Jupyter/Colab) de um módulo do curso "Ready To Deploy", de Enzo Schitini — um notebook com história, missões guiadas, resultado esperado, dicas, desafios extras e checklist, para o aluno praticar os conceitos do módulo — a partir do módulo já pronto em content_generation/jupyter_notebooks/module_NN.ipynb, salvando como module_NN_projeto_pratico.ipynb. Use SEMPRE que o usuário pedir projeto prático, projeto do módulo, atividade prática, exercícios práticos, desafio ou "lista pra praticar" de um módulo do curso (ex: "gera o projeto do módulo 03", "cria a prática do module_05"), mesmo que não fale em "skill" ou "padrão". Não use para gerar o módulo em si (isso é a skill gerar-modulo-ipynb).
---

# Gerar projeto prático .ipynb — Ready To Deploy

Um projeto prático é onde o aluno **usa** o que acabou de aprender no módulo, dentro de uma história. Ele precisa ter um nível real de desafio, mas **não pode parecer uma prova**: é um dia de trabalho numa empresa fictícia, com colegas pedindo coisas no chat. O próprio notebook guia o aluno: os dados já vêm prontos, o pedido é claro, cada missão mostra o resultado esperado e dá uma dica que aponta a seção do módulo a revisar.

O público são **iniciantes que falam português do Brasil**.

## Arquivos da skill

- `scripts/construtor_projeto.py`: classe `ProjetoPratico` (estende o `Notebook` de `gerar-modulo-ipynb`) com `cabecalho()`, `exercicio(codigo_inicial, solucao=...)`, `resultado_esperado()`, `dica()`, `separador()` e `salvar()`, e a função `mensagem(nome, cargo, texto)`. **O `salvar()` executa as soluções e confere cada "Resultado esperado"; se algo não bater, ele mostra a diferença e não grava o arquivo.**
- `scripts/validar_projeto.py`: confere o esqueleto (seções, ordem, missões, extras, checklist) e executa todas as células como o aluno as recebe.
- `references/exemplo_projeto_modulo_01.py`: **padrão ouro**. Leia antes de gerar, para calibrar tom, tamanho das missões, nível de guia e formato. Não copie o conteúdo.
- `references/universo_sabor_express.md`: a empresa, os personagens e o diário do que já aconteceu em cada projeto. Leia antes de escrever a história e atualize depois.

As duas skills dependem uma da outra: os scripts daqui importam `construtor_notebook.py` e `validar_notebook.py` de `../gerar-modulo-ipynb/scripts/`. As regras de Markdown e de estilo de código de lá (seções "Estilo do código" e "Detalhes de Markdown no Jupyter/Colab" do `SKILL.md` dela) valem aqui também.

## Fluxo de trabalho

1. **Leia o módulo inteiro** em `content_generation/jupyter_notebooks/module_NN.ipynb` (o módulo já pronto, não o cru de `raw_content/`). Se ele não existir, avise o usuário e sugira gerar o módulo primeiro com a skill `gerar-modulo-ipynb`.
2. **Faça o inventário do escopo.** Liste as seções, e em cada uma as funções, métodos, operadores e padrões mostrados, e anote os exemplos e motivações do módulo. O escopo permitido é **tudo o que foi ensinado do Módulo 01 até o NN**: dê uma olhada na tabela de Tópicos dos módulos anteriores. Anote também o que ainda **não** foi ensinado (os Tópicos do módulo NN+1 e as dicas de "veremos em módulos futuros"), porque o projeto não pode depender disso.
3. **Leia as duas referências** (o exemplo e o universo).
4. **Planeje antes de escrever** (veja "Desenhando as missões"): o capítulo da história, as missões (tema, personagem, conceito, dados) e os extras.
5. **Escreva o script de geração** no scratchpad, importando o construtor (modelo abaixo), com uma solução para cada missão e cada extra que tenha resultado esperado.
6. **Execute o script e depois o validador.** Corrija qualquer divergência do gabarito e qualquer ERRO; avalie os AVISOS até o resultado ser `APROVADO`.
7. **Atualize o diário** em `references/universo_sabor_express.md` (e a tabela de personagens, se criou algum).
8. **Informe ao usuário** (veja "Relatório final").

Destino: `content_generation/jupyter_notebooks/module_NN_projeto_pratico.ipynb`. Se o arquivo já existir, ele pode ter edições manuais do autor: pergunte antes de sobrescrever. Só gere o notebook com as soluções (`caminho_gabarito=` no `salvar()`, ex: `module_NN_projeto_pratico_gabarito.ipynb`) se o usuário pedir.

```python
import sys
sys.path.insert(0, r"<caminho absoluto desta skill>/scripts")
from construtor_projeto import ProjetoPratico, mensagem

nb = ProjetoPratico()
nb.cabecalho("02", "Título do capítulo", r"""Parágrafo de abertura...""")
# ... contexto, objetivo, requisitos, como funciona, nb.separador()

nb.md(r"""
## 1️⃣ Missão 1 — Nome da missão

""" + mensagem("Marina", "Gerente de Cadastro", "Oii! Preciso que...") + r"""

**Sua missão:** ...
""")
nb.exercicio(r"""
# 🏪 Dados prontos para o aluno
precos_cardapio = [32.90, 41.50, 27.00]

# TODO: calcule e imprima o preço médio do cardápio
""", solucao=r"""
preco_medio = sum(precos_cardapio) / len(precos_cardapio)
print(f'Preço médio: R$ {preco_medio:.2f}')
""")
nb.resultado_esperado("Preço médio: R$ 33.80")
nb.dica("revise a seção 1.3 do Módulo 02 ...")
nb.separador()
# ... demais missões, extras e checklist
nb.salvar(r"content_generation/jupyter_notebooks/module_02_projeto_pratico.ipynb")
```

```bash
python <skill>/scripts/validar_projeto.py content_generation/jupyter_notebooks/module_02_projeto_pratico.ipynb
```

## Estrutura obrigatória

Este esqueleto é a identidade dos projetos, e o validador confere todos os itens:

1. **Cabeçalho** via `nb.cabecalho(NN, título, introdução)`: `# 🚀 Projeto Prático — Módulo NN: Título`, um parágrafo de abertura e as linhas de curso e autor.
2. `## 📖 O contexto`: o capítulo da história (onde o aluno está, o que aconteceu desde o projeto anterior, o que o time precisa hoje), fechando com a dica "não existe só uma forma certa".
3. `## 🎯 Objetivo`: lista dos conceitos do módulo que o aluno vai praticar.
4. `## 🧰 Requisitos`: tabela `Requisito | Detalhe` com Google Colab, conceitos dos módulos necessários, funções/métodos usados e bibliotecas (ou "Nenhuma!").
5. `## 🗺️ Como o projeto funciona`: tabela `Missão | Tema | Conceito principal` (uma linha por missão, com `1️⃣`, `2️⃣`...) e a lista do que cada missão contém (💬 💻 🔎 💡). Termina com `nb.separador()`.
6. **Missões** `## 1️⃣ Missão 1 — Nome`, cada uma nesta ordem de células:
   - Markdown: título + `mensagem(...)` do personagem + `**Sua missão:**` com o pedido e os nomes das variáveis a criar;
   - `nb.exercicio(...)`: dados prontos + comentários `# TODO`, com a solução;
   - `nb.resultado_esperado(...)`;
   - `nb.dica(...)`;
   - `nb.separador()`.
7. `## 🌟 Desafios extras`: introdução dizendo que são opcionais, e depois 3 a 5 extras `### <emoji> Extra N — Nome`, cada um com Markdown curto, `nb.exercicio(...)` e, quando fizer sentido, `nb.resultado_esperado(...)`. Sem separador entre os extras; um `nb.separador()` depois do último.
8. `## ✅ Checklist de autoavaliação`: itens `- [ ]` (um por habilidade praticada, não por missão), uma frase de parabéns e um gancho para o próximo módulo, **com o tema real dele** (confira o título de `module_NN+1.ipynb`).

## Desenhando as missões

- **De 3 a 6 missões.** Em geral, uma por seção principal do módulo (na mesma ordem, para a dificuldade crescer junto com o conteúdo) e uma **missão final de integração**, que junta os resultados das anteriores em um painel, relatório ou pequeno "sistema". Se o módulo tiver uma seção muito curta, junte-a a outra missão.
- **Cada missão é um pedido de negócio, não um enunciado de exercício.** "O Diego precisa do ticket médio pra reunião" em vez de "Calcule a média". O personagem explica *por que* precisa; o bloco **Sua missão** explica *o que* entregar.
- **Espelhe as motivações do módulo, sem copiá-las.** Se o módulo calculou ticket médio de um restaurante, a missão calcula outra métrica parecida, com outros dados, e cita a seção onde o aluno viu a técnica. Isso faz o aluno transferir o conceito em vez de copiar a solução.
- **Guie sem entregar a resposta.** A célula de código traz os dados prontos e `# TODO` numerados com os nomes das variáveis a criar. Uma pista de fórmula no comentário é aceitável (`# fórmula: (novo - antigo) / antigo * 100`); a linha de código pronta, não.
- **Varie o grau de liberdade:** as primeiras missões têm resultado exato; a missão final tem resultado aberto ("não existe gabarito único"), com um **exemplo** de resultado (`titulo="Exemplo de resultado"`), que também é conferido contra uma solução; o último extra pode ser totalmente livre.
- **Extras são um "modo difícil", não mais do mesmo:** uma pegadinha do módulo (ex: `bool(0)`), uma combinação de dois conceitos, ou um detalhe que o módulo só mencionou. Uma pergunta para o aluno pensar antes de testar ("E se a nota fosse `0`? 😉") engaja mais do que uma ordem.

## Regras que garantem que o projeto funciona

Estas regras vêm de erros reais do primeiro projeto. Siga todas:

- **Nenhum número do enunciado é calculado de cabeça.** Todo `resultado_esperado` conferido precisa de uma `solucao` que o imprima. O construtor recusa gravar se não bater. Use `confere="inicio"` quando o final da saída depender de escolhas do aluno, e `confere=None` só quando não houver solução possível. O texto das dicas não é conferido: se uma dica citar um número (ex: "se deu 65.74, você tirou a média simples"), calcule-o com Python antes de escrever.
- **As células entregues precisam rodar com "Executar tudo"**, antes de o aluno escrever qualquer coisa: só dados, comentários e `# TODO`. Nunca use em linha executável uma variável que o aluno ainda vai criar; cite-a apenas em comentário.
- **Toda variável usada em outra missão precisa ter o nome definido no enunciado** ("guarde em `ticket_medio_periodo`"). Se a missão 5 ou um extra depende de algo da missão 2, o aluno precisa ter criado exatamente aquele nome.
- **Saídas com rótulo.** Quando uma missão imprime mais de um valor, o resultado esperado usa *f-strings* com rótulo (`Senha correta?   False`), nunca uma coluna de `True`/`False` soltos que o aluno não sabe a qual variável se referem.
- **Evite valores na fronteira de arredondamento** (resultados terminados em 5 na terceira casa, como `63.665`): o `round()` do Python pode surpreender o aluno. Escolha dados que arredondem sem ambiguidade.
- **Respeite o escopo do inventário.** Se o projeto do Módulo 01 precisaria de `if`, a decisão vira um booleano guardado em variável e impresso. Nada de bibliotecas externas que o módulo não usou.
- **Nomes em português, descritivos e em `snake_case`**, sem acentos nos identificadores (`nome_digitado`, não `nome_bagunçado`; `quantidade_vendas_segunda`, não `qtd_seg`).
- Em Markdown, valores em reais como `R\$ 60,00` (fora de crases e blocos de código); o validador avisa quando esquecer.

## Tom e linguagem

- Segunda pessoa, leve e bem-humorado, sem infantilizar. Os personagens têm personalidade (veja o universo), mas as mensagens são curtas: 2 a 4 frases.
- Vocabulário de trabalho, não de prova: **missão, pedido, entrega, resultado esperado**. Evite "questão", "exercício", "nota", "correto/incorreto", "avaliação" (exceto no nome do checklist).
- Emojis têm papel fixo (títulos das seções, 💬 🔎 💡 e um por extra); não os espalhe pelo texto.
- Termos em inglês em itálico (*string*, *login*), código entre crases.

## Continuidade da história

Por padrão, cada projeto é um **novo capítulo da Sabor Express**: o aluno continua no mesmo emprego, com o mesmo time, e o contexto começa lembrando rapidamente o que aconteceu antes ("Depois de integrar a Cantina da Vó, ..."). Reaproveite personagens e fatos do diário, e dê a cada personagem pedidos da sua área. Se o tema do módulo encaixar melhor em outro cenário, ou se o usuário pedir outra história, tudo bem: registre a decisão no diário.

## Relatório final ao usuário

Responda de forma breve com:

1. Caminho do arquivo e número de células; confirme que o gabarito bateu e que a validação passou.
2. O capítulo da história em uma frase e a tabela de missões (missão → conceito do módulo).
3. Os extras, em uma linha cada.
4. Qualquer conceito do módulo que ficou de fora do projeto, e por quê.

Não repita o conteúdo do notebook, porque o usuário vai abri-lo.
