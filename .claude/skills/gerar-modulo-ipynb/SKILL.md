---
name: gerar-modulo-ipynb
description: Gera um módulo didático em .ipynb (Jupyter/Colab) do curso "Ready To Deploy", de Enzo Schitini, a partir de um conteúdo "cru" (material de aula antigo) em content_generation/raw_content/, reescrevendo-o com muito mais qualidade no padrão oficial do curso e salvando em content_generation/jupyter_notebooks/. Use SEMPRE que o usuário pedir para gerar, criar, reescrever, melhorar, padronizar ou estruturar um módulo, aula ou notebook do curso (ex: "gere o módulo 03", "faz o module_05"), ou quando ele apontar um arquivo em content_generation/raw_content/, mesmo que não fale em "skill", "padrão" ou "Ready To Deploy".
---

# Gerar módulo .ipynb — Ready To Deploy

Transforme um conteúdo cru em um módulo de curso **pronto para publicar**: bem estruturado, didático, correto e executável do começo ao fim. O conteúdo cru serve de **base e roteiro**, não de limite. O resultado deve ser claramente melhor: explicações mais claras, exemplos mais bem escolhidos, erros corrigidos e código comentado com nomes em português.

O público são **iniciantes que falam português do Brasil**. Cada decisão deve ajudar essa pessoa a entender *por que* algo funciona, e não só *como*.

## Arquivos da skill

- `scripts/construtor_notebook.py`: classe `Notebook` com `md()`, `code()`, `separador()` e `salvar()`. Use-a em vez de escrever JSON do .ipynb na mão.
- `scripts/validar_notebook.py`: checa a estrutura e executa todas as células de código.
- `references/exemplo_modulo_01.py`: **padrão ouro**. É o script que gerou o Módulo 01 aprovado pelo autor. Leia antes de gerar um módulo, para calibrar tom, profundidade, tamanho das células e estilo dos comentários. Não copie o conteúdo, só o padrão.

## Fluxo de trabalho

1. **Localize e leia o conteúdo cru inteiro.** Os arquivos crus ficam sempre em **`content_generation/raw_content/`**, com o nome `module_NN.*` (normalmente `.ipynb`). Se o usuário pedir só "gere o módulo 03", procure `content_generation/raw_content/module_03.*`. Se não encontrar, liste a pasta e pergunte qual arquivo usar, em vez de adivinhar ou procurar em outro lugar. Anote os tópicos, a ordem, os exemplos e as motivações ("problema do mundo real" → "revisitando a motivação"). Anote também o que está errado, desatualizado ou fora do escopo do módulo.
2. **Leia `references/exemplo_modulo_01.py`** (pelo menos a primeira vez na sessão).
3. **Descubra número, tema e destino:**
   - Número: do nome do arquivo ou do título cru (`module_03` → `03`). Use sempre dois dígitos.
   - Tema: um nome curto e claro, ex: `Variáveis e Tipos de Dados`.
   - Destino: salve sempre em **`content_generation/jupyter_notebooks/`**, com o nome do módulo: `module_NN.ipynb` (o mesmo nome do arquivo cru, ex: `raw_content/module_03.ipynb` → `jupyter_notebooks/module_03.ipynb`). Só use outro caminho se o usuário pedir explicitamente. Nunca sobrescreva o arquivo cru. Se o arquivo de destino já existir, ele pode ter edições manuais do autor, então pergunte antes de sobrescrever.
4. **Escreva um script de geração** no diretório temporário (scratchpad) que importe o construtor e monte o notebook célula por célula (veja o modelo abaixo).
5. **Execute o script e depois o validador.** Corrija tudo o que for ERRO e avalie os AVISOS até o resultado ser `APROVADO`.
6. **Informe ao usuário** onde o arquivo foi salvo e resuma o que mudou (veja "Relatório final").

```python
import sys
sys.path.insert(0, r"<caminho absoluto desta skill>/scripts")
from construtor_notebook import Notebook

nb = Notebook()
nb.md(r"""
# Módulo 02 - Estruturas de Dados
...
""")
nb.code(r"""
# Comentário curto explicando a intenção
lista_de_compras = ["arroz", "feijão"]
print(lista_de_compras)
""")
nb.salvar(r"content_generation/jupyter_notebooks/module_02.ipynb")
```

```bash
python <skill>/scripts/validar_notebook.py content_generation/jupyter_notebooks/module_02.ipynb
```

Use strings `r"""..."""` para não precisar escapar `\` (LaTeX, `R\$`). Se o texto precisar conter `"""`, monte essa parte com concatenação ou `.replace()`.

## Estrutura obrigatória

A estrutura abaixo é a identidade visual do curso, e todos os módulos precisam ser idênticos nesse esqueleto.

**Célula 1: cabeçalho** (exatamente este formato):

```markdown
# Módulo NN - Tema do Módulo

---

Um parágrafo de visão geral: o que o aluno vai aprender, em que ordem e com quais problemas reais o módulo vai trabalhar, e por que isso importa para o que vem depois.

Curso: Ready To Deploy

Criado por: [Enzo Schitini](https://www.linkedin.com/in/enzoschitini)

---
```

**Célula 2: tópicos** (uma linha por seção principal, com descrição breve e concreta):

```markdown
## Tópicos

| **Tópico** | Descrição |
| --- | --- |
| 1. Nome do tópico | O que será visto, em uma frase. |
| 2. Nome do tópico | ... |
```

**Depois, uma célula `---` e as seções:**

- Seção principal: `## N. Nome` seguida de uma descrição rápida (2 a 3 frases) do que é e por que importa.
- Subseções: `### N.M Nome`. **Sem negrito e sem ponto final** no número (`### 2.1 Definição`, não `### **2.1. Definição**`).
- Uma célula `---` (use `nb.separador()`) **entre** as seções principais.
- A tabela de Tópicos deve bater exatamente com as seções `## N.` do notebook, porque o validador confere isso.

**Fim do notebook:** `---`, depois `## Resumo do Módulo` (uma tabela ou lista que consolida o que foi visto). Essa seção final não entra na tabela de Tópicos.

Não adicione uma seção `## Conteúdo Extra` (links de documentação e aprofundamento) a menos que o usuário peça explicitamente.

Remova elementos de marca ou autoria do material cru (logos, "Caderno de Aula", nomes de outras escolas ou autores, links pessoais antigos). O cabeçalho do Ready To Deploy os substitui.

## Divisão em células

Um notebook é lido e executado aos poucos, então cada célula deve ter **um único papel**:

- Título de subseção e o texto que o introduz podem ficar juntos. Já uma tabela grande, uma lista longa, um aviso ou uma fórmula entram numa célula própria quando isso melhora a leitura.
- O texto que apresenta um exemplo (`**Exemplo:** ...`) fica numa célula de Markdown, logo antes da célula de código.
- **Uma ideia por célula de código.** Prefira várias células curtas (3 a 15 linhas) a uma célula longa que mistura conceitos.
- Estados que se acumulam (variáveis criadas antes e usadas depois) são normais, mas o notebook precisa rodar do início ao fim na ordem.

## Como melhorar o conteúdo

O ganho de qualidade vem principalmente daqui:

- **Preserve todos os tópicos e exemplos relevantes do cru**, na mesma lógica de progressão, e expanda o que estiver raso. Quando o cru tiver o padrão "Motivação → Definição → Operações → Conversão → Revisitando a motivação", mantenha-o: fechar o problema do início é o que dá sentido ao conteúdo.
- **Explique o porquê.** Onde o cru só lista algo ("operadores: + - * /"), transforme em tabela com **operador | significado | exemplo | resultado**. Onde o cru mostra código sem contexto, diga antes o que o aluno vai observar.
- **Acrescente o que falta a um iniciante:** armadilhas comuns (ex: `=` vs `==`, `int()` que trunca em vez de arredondar), boas práticas (PEP 8, `snake_case`), atalhos úteis e alternativas mais modernas (ex: *f-strings*). Faça isso sem fugir do tema do módulo.
- **Corrija erros do cru** em vez de replicá-los: variáveis sobrescritas por engano, `type()` da variável errada, cálculos conceitualmente errados (ex: média de médias apresentada como média geral), práticas não idiomáticas (ex: `&` e `|` no lugar de `and` e `or` em Python puro). Quando a correção for didática, mostre as duas formas e explique a diferença.
- **Atualize referências desatualizadas:** produtos descontinuados, links quebrados, nomes antigos de serviços.
- **Conteúdo fora do escopo** (ex: uma célula solta com laços num módulo introdutório) fica de fora e é citado no relatório final. Não force no módulo algo que depende de tópicos ainda não ensinados. Se for útil, mencione em uma dica que "veremos isso em módulos futuros".
- Use destaques com moderação e sempre com o mesmo formato:
  - `> 💡 **Dica:** ...` para atalhos, boas práticas e curiosidades úteis;
  - `> ⚠️ **Atenção:** ...` para erros comuns e armadilhas.
- Em texto, marque termos em inglês com itálico (*string*, *slicing*, *backend*) e nomes de código com crase (`print()`, `int`).

## Estilo do código

O código também é material didático e deve ser lido como tal:

- **Nomes em português, descritivos e em `snake_case`**: `valor_vendas_19`, `quantidade_itens_carrinho`, `pode_realizar_saque`, e não `svv_19`, `qtd`, `x`. Nomes curtos como `a`/`b` só em demonstrações puramente matemáticas.
- **Comentários curtos em português** que explicam a *intenção* ou o *porquê* (`# float -> int: a parte decimal é DESCARTADA`), e não que repetem o código. Um comentário por bloco lógico costuma bastar.
- Organize o código em blocos separados por linha em branco: dados de entrada → processamento → `print` do resultado.
- Deixe as saídas legíveis: use *f-strings* com rótulos (`print(f'Ticket médio: {ticket:.2f}')`) quando houver mais de um valor impresso.
- **Toda célula precisa executar sem erro**, porque um aluno que roda "Executar tudo" não pode travar no meio. Para mostrar um erro, deixe a linha comentada com `# ❌ TypeError` e mostre a forma correta logo abaixo.
- Não use `input()` (trava a execução automática): simule a entrada do usuário com uma variável.
- Entregue as células **sem saídas** (o construtor já faz isso), para que o aluno execute e veja por conta própria.
- Se o módulo exigir bibliotecas externas (pandas, matplotlib...), coloque os `import` em uma célula no início da seção que os usa. Se a biblioteca não existir na máquina local, o validador vai acusar erro de importação: nesse caso, confira o resto manualmente e avise o usuário.

## Detalhes de Markdown no Jupyter/Colab

- O `$` inicia uma fórmula LaTeX. Escreva valores em reais como `R\$ 200,00` nas células de texto (dentro de código ou crases não é preciso).
- Fórmulas: `$$\text{ticket médio} = \frac{\text{valor total}}{\text{quantidade}}$$`.
- O caractere `|` dentro de tabelas quebra a coluna. Mantenha operadores com `|` fora das tabelas ou use `&#124;`.

## Relatório final ao usuário

Depois de gerar e validar, responda de forma breve com:

1. Caminho do arquivo e número de células, e confirme que a validação passou (todas as células executaram).
2. **Principais melhorias**: o que foi expandido ou acrescentado.
3. **Correções** de erros do cru, com uma frase de explicação cada.
4. **O que ficou de fora** e por quê (conteúdo fora do escopo, imagens/logos antigos, links removidos).

Não repita todo o conteúdo do notebook na resposta, porque o usuário vai abri-lo.
