"""Exemplo de referência (padrão ouro): script que gerou o Módulo 01.

Gerado a partir de content_generation/raw_content/module_01.ipynb e aprovado
pelo autor do curso. Use como modelo de tom, profundidade, organização das
células e estilo de código. Não copie o conteúdo: cada módulo tem o seu tema.

Execução:
    python exemplo_modulo_01.py content_generation/jupyter_notebooks/module_01.ipynb
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from construtor_notebook import Notebook  # noqa: E402

nb = Notebook()


# =====================================================================
# CABEÇALHO
# =====================================================================
nb.md(r"""
# Módulo 01 - Variáveis e Tipos de Dados

---

Neste primeiro módulo você vai dar os primeiros passos em Python. Começamos conhecendo o **Google Colab**, o ambiente onde vamos escrever e executar nossos códigos, e em seguida entendemos o que são **variáveis** e como o Python armazena informações na memória. A partir daí, exploramos os tipos de dados mais importantes da linguagem — **números**, **strings** (textos) e **booleanos** (valores lógicos) — sempre partindo de problemas reais do dia a dia de uma empresa: calcular o ticket médio de um restaurante, padronizar coordenadas geográficas e validar o login de um usuário. Ao final, você terá a base necessária para todos os módulos seguintes.

Curso: Ready To Deploy

Criado por: [Enzo Schitini](https://www.linkedin.com/in/enzoschitini)

---
""")

nb.md(r"""
## Tópicos

| **Tópico** | Descrição |
| --- | --- |
| 1. Introdução ao Google Colab | O que é o Colab, como acessá-lo e como funcionam os *notebooks* e suas células. |
| 2. Variáveis | Como armazenar dados na memória, boas práticas de nomenclatura e os tipos nativos do Python. |
| 3. Números | Tipos numéricos, operações aritméticas e conversões, aplicados ao cálculo de um ticket médio. |
| 4. *Strings* | Criação, concatenação, *f-strings*, fatiamento e métodos, aplicados à padronização de coordenadas. |
| 5. Booleanos | Valores lógicos, operadores de comparação e operadores lógicos, aplicados a um sistema de *login*. |
""")

nb.separador()

# =====================================================================
# 1. GOOGLE COLAB
# =====================================================================
nb.md(r"""
## 1. Introdução ao Google Colab

O **Google Colab** (*Colaboratory*) é uma ferramenta gratuita do Google que permite escrever e executar código Python direto no navegador, sem instalar nada no seu computador. Ele é baseado no **Jupyter Notebook**, o formato de caderno interativo mais usado no mercado de dados e ciência de dados.
""")

nb.md(r"""
### 1.1 Ferramenta web

Por ser uma ferramenta **100% web**, tudo o que você precisa é de um navegador e de uma conta Google:

1. Crie (ou use) uma conta Google em [gmail.com](https://gmail.com);
2. Acesse o Colab pelo endereço [colab.research.google.com](https://colab.research.google.com/);
3. Clique em **Arquivo > Novo notebook** para criar o seu primeiro caderno.

> 💡 **Dica:** os notebooks criados ficam salvos automaticamente no seu Google Drive, na pasta **Colab Notebooks**.
""")

nb.md(r"""
### 1.2 Ambiente autogerenciado

Dizemos que o Colab é **autogerenciado** porque o próprio Google cuida de toda a infraestrutura para você:

- Ao conectar, o Google **provisiona uma máquina virtual** (um computador na nuvem) exclusiva para a sua sessão;
- Essa máquina é **temporária**: no plano gratuito ela dura no máximo cerca de **12 horas** e pode ser desconectada antes disso por inatividade;
- Quando a sessão termina, **as variáveis e os arquivos temporários são perdidos** — o notebook (texto e código) continua salvo, mas será preciso executar as células novamente.
""")

nb.md(r"""
### 1.3 Notebooks e células

Um **notebook** (caderno) é um documento *web* composto por uma sequência de blocos chamados **células**. Existem dois tipos:

| Tipo de célula | Para que serve | O que acontece ao executar |
| --- | --- | --- |
| **Texto** | Explicações, títulos, listas, tabelas e fórmulas (Markdown ou HTML) | O texto é formatado e exibido |
| **Código** | Instruções em Python | O código é executado e o resultado aparece logo abaixo |

Alguns atalhos úteis no Colab:

| Atalho | Ação |
| --- | --- |
| `Shift + Enter` | Executa a célula e vai para a próxima |
| `Ctrl + Enter` | Executa a célula e permanece nela |
| `Ctrl + M` + `B` | Cria uma nova célula abaixo |
| `Ctrl + M` + `M` | Converte a célula em texto |
| `Ctrl + M` + `Y` | Converte a célula em código |
""")

nb.md(r"""
Vamos ao nosso primeiro código! A função `print()` exibe na tela o que estiver entre os parênteses:
""")

nb.code(r"""
# Nosso primeiro programa: exibindo uma mensagem na tela
print("Olá, mundo!")
""")

nb.md(r"""
Um detalhe importante: todas as células de um notebook **compartilham o mesmo estado**. Ou seja, algo criado em uma célula fica disponível nas outras — desde que a célula onde foi criado tenha sido **executada antes**. Execute as duas células abaixo em ordem:
""")

nb.code(r"""
# Criando uma mensagem nesta célula...
mensagem_boas_vindas = "Bem-vindo ao Ready To Deploy!"
""")

nb.code(r"""
# ...e utilizando-a em outra célula
print(mensagem_boas_vindas)
""")

nb.md(r"""
> ⚠️ **Atenção:** a ordem de execução importa, não a posição na página. Se você executar a segunda célula sem ter executado a primeira, o Python vai acusar um erro (`NameError`), pois a variável ainda não existe.
""")

nb.separador()

# =====================================================================
# 2. VARIÁVEIS
# =====================================================================
nb.md(r"""
## 2. Variáveis

Programas precisam guardar informações para usá-las depois: o nome de um cliente, o preço de um produto, o saldo de uma conta. Em Python, fazemos isso com **variáveis**.
""")

nb.md(r"""
### 2.1 Definição

Uma **variável** é um nome que aponta para um valor armazenado na **memória RAM** do dispositivo em uso (*notebook*, celular, console de videogame, *smartwatch* etc.). Esse armazenamento é **volátil**: quando o programa termina (ou a sessão do Colab é encerrada), os valores são apagados.

Pense em uma variável como uma **etiqueta colada em uma caixa**: a etiqueta é o nome, e o conteúdo da caixa é o valor.

A sintaxe para criar uma variável é:

```python
nome_da_variavel = valor
```

> 💡 O sinal `=` em Python significa **atribuição** ("guarde este valor neste nome"), e não igualdade matemática.
""")

nb.code(r"""
# Criando (atribuindo) uma variável
idade = 30
print(idade)

# Reatribuindo: o valor antigo é descartado e substituído pelo novo
idade = 27
print(idade)

# Variáveis também podem guardar textos
nome = "André"
print(nome)
""")

nb.md(r"""
### 2.2 Regras e boas práticas de nomenclatura

Os nomes de variáveis seguem algumas **regras obrigatórias**:

- Devem começar com uma **letra** ou **underline** (`_`) — nunca com número;
- Podem conter apenas letras, números e `_` (sem espaços, hífens ou símbolos);
- O Python **diferencia maiúsculas de minúsculas** (*case sensitive*): `cidade` e `Cidade` são variáveis diferentes;
- Não podem ser **palavras reservadas** da linguagem, como `if`, `for`, `True`, `class` etc.

E também uma **convenção** muito importante: em Python usamos o padrão **`snake_case`** (palavras em minúsculas separadas por `_`), conforme o guia de estilo oficial, a [PEP 8](https://peps.python.org/pep-0008/).

| ✅ Válido e recomendado | ❌ Inválido ou não recomendado |
| --- | --- |
| `valor_total` | `valor total` (espaço — inválido) |
| `quantidade_itens` | `2_quantidade` (começa com número — inválido) |
| `nome_cliente` | `nome-cliente` (hífen — inválido) |
| `taxa_juros` | `x`, `abc`, `var1` (válidos, mas não dizem nada sobre o dado) |
""")

nb.code(r"""
# ✅ Nomes descritivos deixam o código fácil de entender
valor_total_compra = 150.90
quantidade_de_itens = 3

# Python é case sensitive: estas são DUAS variáveis diferentes
cidade = "São Paulo"
Cidade = "Rio de Janeiro"

print(cidade)
print(Cidade)
""")

nb.md(r"""
### 2.3 Tipos nativos

Todo valor em Python possui um **tipo**, que define o que ele representa e quais operações podemos fazer com ele. Os tipos nativos (que já vêm com a linguagem) mais básicos são:

| Categoria | Tipo | Exemplo |
| --- | --- | --- |
| Numérico | `int` (inteiro) | `42` |
| Numérico | `float` (decimal) | `3.14` |
| Numérico | `complex` (complexo) | `1 + 2j` |
| Texto | `str` (*string*) | `"Olá"` |
| Lógico | `bool` (booleano) | `True` |
| Vazio | `NoneType` | `None` |

Para descobrir o tipo de qualquer valor ou variável, usamos a função nativa **`type()`**.
""")

nb.md(r"""
**Tipos numéricos:** inteiros (`int`) e decimais (`float`).
""")

nb.code(r"""
# int: números inteiros
preco = 1000
print(preco)
print(type(preco))

# float: números decimais (atenção: use PONTO, e não vírgula)
taxa_de_juros = 0.05
print(taxa_de_juros)
print(type(taxa_de_juros))
""")

nb.md(r"""
**Tipo de texto:** *strings* (`str`), sempre entre aspas simples ou duplas.
""")

nb.code(r"""
# str: textos podem usar aspas duplas...
primeiro_nome = "André"
print(primeiro_nome)
print(type(primeiro_nome))

# ...ou aspas simples, o resultado é o mesmo
pais = 'Brasil'
print(pais)
print(type(pais))
""")

nb.md(r"""
**Tipo lógico:** booleanos (`bool`), que só podem assumir `True` (verdadeiro) ou `False` (falso).
""")

nb.code(r"""
# bool: note a primeira letra MAIÚSCULA em True e False
usuario_maior_de_idade = True
print(usuario_maior_de_idade)
print(type(usuario_maior_de_idade))
""")

nb.md(r"""
**Tipo vazio:** `NoneType`, cujo único valor é `None` e representa a **ausência de valor**.
""")

nb.code(r"""
# None: útil para indicar que um dado não existe ou ainda não foi informado
telefone_fixo = None
print(telefone_fixo)
print(type(telefone_fixo))
""")

nb.md(r"""
Python possui **tipagem dinâmica**: você não precisa declarar o tipo da variável, pois ele é descoberto automaticamente a partir do valor. Isso também significa que uma mesma variável pode passar a guardar um valor de outro tipo:
""")

nb.code(r"""
# O tipo é definido pelo valor, não pela variável
dado = 10
print(type(dado))

dado = "dez"
print(type(dado))
""")

nb.md(r"""
> ⚠️ Apesar de possível, trocar o tipo de uma variável ao longo do código costuma gerar confusão. Prefira manter cada variável com um único tipo.
""")

nb.separador()

# =====================================================================
# 3. NÚMEROS
# =====================================================================
nb.md(r"""
## 3. Números

Os tipos numéricos são a base de qualquer cálculo: preços, quantidades, taxas, métricas de negócio. Nesta seção vamos conhecer esses tipos, suas operações e como converter um no outro.
""")

nb.md(r"""
### 3.1 Motivação

Você precisa calcular o **ticket médio diário** do seu restaurante, ou seja, quanto, em média, cada venda rendeu em um dia. A métrica é calculada dividindo o **valor total das vendas** do dia pela **quantidade de vendas** do mesmo dia:

$$\text{ticket médio} = \frac{\text{valor total das vendas}}{\text{quantidade de vendas}}$$

Esta é a sua planilha:

| Dia | Valor total das vendas (R\$) | Quantidade de vendas | Ticket médio (R\$) |
| --- | --- | --- | --- |
| 19/01 | 153.98 | 3 | ? |
| 20/01 | 337.01 | 7 | ? |
| 23/01 | 295.33 | 5 | ? |

**Como podemos fazer esse cálculo usando Python?**
""")

nb.md(r"""
### 3.2 Definição

Os tipos numéricos armazenam **valores numéricos**:

| Tipo | Descrição | Exemplos |
| --- | --- | --- |
| `int` | Números inteiros (positivos, negativos ou zero) | `10`, `-37`, `500` |
| `float` | Números decimais (ponto flutuante) | `0.333`, `10.1`, `-2.5` |
| `complex` | Números complexos (parte real + parte imaginária `j`) | `1 + 2j` |
""")

nb.code(r"""
# Conferindo o tipo de cada número
print(type(37))
print(type(10.1))
print(type(1 + 2j))
""")

nb.md(r"""
> 💡 **Dica:** para números grandes, você pode usar `_` como separador de milhar. O Python ignora o `_`, mas o código fica bem mais legível.
""")

nb.code(r"""
# O underline serve apenas para facilitar a leitura
faturamento_anual = 1_500_000
print(faturamento_anual)
""")

nb.md(r"""
### 3.3 Operações

Além das quatro operações fundamentais, o Python oferece operadores mais avançados:

| Operador | Operação | Exemplo | Resultado |
| --- | --- | --- | --- |
| `+` | Soma | `7 + 2` | `9` |
| `-` | Subtração | `7 - 2` | `5` |
| `*` | Multiplicação | `7 * 2` | `14` |
| `/` | Divisão | `7 / 2` | `3.5` |
| `//` | Divisão inteira | `7 // 2` | `3` |
| `%` | Resto da divisão (módulo) | `7 % 2` | `1` |
| `**` | Potência (exponenciação) | `7 ** 2` | `49` |
""")

nb.code(r"""
# Testando todos os operadores aritméticos
a = 7
b = 2

print("Soma:           ", a + b)
print("Subtração:      ", a - b)
print("Multiplicação:  ", a * b)
print("Divisão:        ", a / b)
print("Divisão inteira:", a // b)
print("Resto:          ", a % b)
print("Potência:       ", a ** b)
""")

nb.md(r"""
Repare na diferença entre `/` e `//`: a divisão comum **sempre** retorna um `float`, mesmo quando o resultado é exato. Já a divisão inteira descarta a parte decimal e, entre dois inteiros, retorna um `int`.
""")

nb.code(r"""
dividendo = 3
divisor = 2

# Divisão comum: resultado sempre float
resultado_divisao = dividendo / divisor
print(resultado_divisao)
print(type(resultado_divisao))

# Divisão inteira: descarta a parte decimal
resultado_divisao_inteira = dividendo // divisor
print(resultado_divisao_inteira)
print(type(resultado_divisao_inteira))
""")

nb.md(r"""
A **ordem de precedência** segue a matemática: primeiro `**`, depois `*`, `/`, `//` e `%`, e por último `+` e `-`. Use **parênteses** para deixar a ordem explícita:
""")

nb.code(r"""
# Sem parênteses: a multiplicação acontece antes da soma
print(2 + 3 * 4)

# Com parênteses: a soma acontece primeiro
print((2 + 3) * 4)
""")

nb.md(r"""
**Exemplo:** carrinho de compras de um *e-commerce*. Cada vez que o cliente adiciona um item, a quantidade aumenta em 1.
""")

nb.code(r"""
# O carrinho começa vazio
quantidade_itens_carrinho = 0

# Cliente adiciona um item: pegamos o valor atual e somamos 1
quantidade_itens_carrinho = quantidade_itens_carrinho + 1
print(quantidade_itens_carrinho)

# Cliente adiciona mais um item
quantidade_itens_carrinho = quantidade_itens_carrinho + 1
print(quantidade_itens_carrinho)
""")

nb.md(r"""
Como esse padrão é muito comum, o Python oferece os **operadores de atribuição composta**, que fazem a operação e a atribuição de uma só vez:

| Forma curta | Equivale a |
| --- | --- |
| `x += 1` | `x = x + 1` |
| `x -= 1` | `x = x - 1` |
| `x *= 2` | `x = x * 2` |
| `x /= 2` | `x = x / 2` |
""")

nb.code(r"""
# Mesmo exemplo, agora com o operador +=
quantidade_itens_carrinho = 0

quantidade_itens_carrinho += 1
print(quantidade_itens_carrinho)

quantidade_itens_carrinho += 1
print(quantidade_itens_carrinho)
""")

nb.md(r"""
**Exemplo:** total a pagar por um produto vendido a quilo.
""")

nb.code(r"""
# Preço do quilo e quantidade comprada (250 gramas = 0.250 kg)
preco_por_kg = 47
quantidade_kg = 0.250

total_a_pagar = preco_por_kg * quantidade_kg
print(total_a_pagar)
""")

nb.md(r"""
**Exemplo:** o operador `%` (resto) é muito usado para verificar se um número é **par** — todo número par tem resto `0` quando dividido por 2.
""")

nb.code(r"""
numero_pedido = 1024

resto_da_divisao = numero_pedido % 2
print(resto_da_divisao)  # 0 indica que o número é par
""")

nb.md(r"""
### 3.4 Conversão

Podemos converter os tipos numéricos entre si com as funções nativas `int()`, `float()` e `complex()`:
""")

nb.code(r"""
# float -> int: a parte decimal é DESCARTADA (não é arredondamento!)
print(int(3.9))
""")

nb.code(r"""
# int -> float
print(float(10))
""")

nb.code(r"""
# int -> complex
print(complex(1))
""")

nb.md(r"""
Se o objetivo for **arredondar**, use a função `round()`, informando o número e a quantidade de casas decimais desejada. Ela é especialmente útil para valores monetários:
""")

nb.code(r"""
valor_bruto = 51.326666

print(round(valor_bruto))     # arredonda para o inteiro mais próximo
print(round(valor_bruto, 2))  # arredonda para 2 casas decimais
""")

nb.md(r"""
### 3.5 Revisitando a motivação

Agora temos todas as ferramentas para preencher a planilha do restaurante:

| Dia | Valor total das vendas (R\$) | Quantidade de vendas | Ticket médio (R\$) |
| --- | --- | --- | --- |
| 19/01 | 153.98 | 3 | ? |
| 20/01 | 337.01 | 7 | ? |
| 23/01 | 295.33 | 5 | ? |
""")

nb.md(r"""
Ticket médio do dia **19/01**:
""")

nb.code(r"""
valor_vendas_19 = 153.98
quantidade_vendas_19 = 3

ticket_medio_19 = valor_vendas_19 / quantidade_vendas_19
print(round(ticket_medio_19, 2))
""")

nb.md(r"""
Ticket médio do dia **20/01**:
""")

nb.code(r"""
valor_vendas_20 = 337.01
quantidade_vendas_20 = 7

ticket_medio_20 = valor_vendas_20 / quantidade_vendas_20
print(round(ticket_medio_20, 2))
""")

nb.md(r"""
Ticket médio do dia **23/01**:
""")

nb.code(r"""
valor_vendas_23 = 295.33
quantidade_vendas_23 = 5

ticket_medio_23 = valor_vendas_23 / quantidade_vendas_23
print(round(ticket_medio_23, 2))
""")

nb.md(r"""
E o ticket médio do **período inteiro**? Uma primeira ideia seria tirar a média dos três tickets diários:
""")

nb.code(r"""
# Média simples dos tickets diários
media_dos_tickets = (ticket_medio_19 + ticket_medio_20 + ticket_medio_23) / 3
print(round(media_dos_tickets, 2))
""")

nb.md(r"""
Porém, essa abordagem dá o **mesmo peso** para todos os dias, mesmo que o dia 20/01 tenha tido mais que o dobro de vendas do dia 19/01. O jeito correto é aplicar a própria fórmula do ticket médio ao período todo: **somar todos os valores** e dividir pela **soma de todas as quantidades**.
""")

nb.code(r"""
# Totais do período
valor_total_periodo = valor_vendas_19 + valor_vendas_20 + valor_vendas_23
quantidade_total_periodo = quantidade_vendas_19 + quantidade_vendas_20 + quantidade_vendas_23

# Ticket médio do período (média ponderada pela quantidade de vendas)
ticket_medio_periodo = valor_total_periodo / quantidade_total_periodo
print(round(ticket_medio_periodo, 2))
""")

nb.md(r"""
> 💡 Os dois resultados são diferentes! Em análise de dados, entender **o que** uma métrica representa é tão importante quanto saber calculá-la.
""")

nb.separador()

# =====================================================================
# 4. STRINGS
# =====================================================================
nb.md(r"""
## 4. *Strings*

Nomes, endereços, e-mails, descrições de produtos: grande parte dos dados do mundo real é **texto**. Nesta seção vamos aprender a criar, combinar, recortar e transformar *strings*.
""")

nb.md(r"""
### 4.1 Motivação

A empresa em que você trabalha adquiriu uma *startup* de logística, e você precisa identificar os endereços que são comuns às duas bases de dados. O problema é que cada empresa armazena as coordenadas de um jeito:

- Na **sua empresa**, latitude e longitude ficam em duas variáveis separadas: `latitude` e `longitude`;
- Na **startup adquirida**, as duas ficam juntas em uma única variável, `latitude_longitude`, separadas por `;`.
""")

nb.code(r"""
# Formato da sua empresa: dois valores separados
latitude = '-22.005320'
longitude = '-47.891040'

# Formato da startup: um único texto com os dois valores
latitude_longitude = '-22.005320;-47.891040'
""")

nb.md(r"""
**Como podemos padronizar a forma como as coordenadas são armazenadas para que possam ser comparadas?**
""")

nb.md(r"""
### 4.2 Definição

*Strings* armazenam **textos**, ou seja, sequências de caracteres: `'c'`, `'Ready To Deploy'`, `'Andre Perez, 20 anos'`. São do tipo `str` e podem ser escritas com:

| Delimitador | Exemplo | Uso típico |
| --- | --- | --- |
| Aspas simples | `'Olá'` | Textos curtos |
| Aspas duplas | `"Olá"` | Textos que contêm apóstrofo, ex: `"Joana d'Arc"` |
| Aspas triplas | `'''Olá'''` ou `ASPAS_TRIPLASOláASPAS_TRIPLAS` | Textos com várias linhas |
""".replace("ASPAS_TRIPLAS", '"' * 3))

nb.code(r"""
nome_aula = 'Módulo 01 - Variáveis e Tipos de Dados'

print(nome_aula)
print(type(nome_aula))
""")

nb.code(r"""
# Aspas triplas permitem textos em várias linhas
descricao_curso = '''Ready To Deploy
Curso de Python do zero ao deploy.'''

print(descricao_curso)
""")

nb.md(r"""
Uma *string* também pode ser **vazia**, e a função nativa `len()` informa quantos caracteres ela possui:
""")

nb.code(r"""
string_vazia = ""

print(string_vazia)
print(type(string_vazia))
print(len(string_vazia))  # 0 caracteres
""")

nb.code(r"""
# len() conta TODOS os caracteres, incluindo espaços e pontuação
cidade = "São Paulo"
print(len(cidade))
""")

nb.md(r"""
### 4.3 Operações

**Concatenação (`+`)**: junta duas ou mais *strings* em uma só.

**Exemplo:** montando uma apresentação a partir do nome e sobrenome.
""")

nb.code(r"""
nome = 'Andre Marcos'
sobrenome = 'Perez'

# Repare que os espaços também precisam ser concatenados
apresentacao = 'Olá, meu nome é ' + nome + ' ' + sobrenome + '.'
print(apresentacao)
""")

nb.md(r"""
**Repetição (`*`)**: repete uma *string* um determinado número de vezes.
""")

nb.code(r"""
# Útil, por exemplo, para criar linhas separadoras
separador = '-' * 30
print(separador)
""")

nb.md(r"""
**Formatação com *f-strings***: a forma mais moderna e legível de montar textos. Basta colocar um `f` antes das aspas e escrever as variáveis entre chaves `{}`:
""")

nb.code(r"""
nome = 'Andre Marcos'
sobrenome = 'Perez'

apresentacao = f'Olá, meu nome é {nome} {sobrenome}.'
print(apresentacao)
""")

nb.md(r"""
As *f-strings* também aceitam números e permitem **formatar** o valor — por exemplo, `:.2f` exibe um `float` com duas casas decimais:
""")

nb.code(r"""
produto = 'Notebook'
preco_produto = 3499.9

print(f'O produto {produto} custa R$ {preco_produto:.2f}')
""")

nb.md(r"""
> ⚠️ **Atenção:** o operador `+` não junta *strings* com números. Uma linha como `'Idade: ' + 19` gera um erro (`TypeError`). Nesses casos, converta o número com `str()` ou, melhor ainda, use uma *f-string*.
""")

nb.code(r"""
idade_cliente = 19

# print('Idade: ' + idade_cliente)       # ❌ TypeError
print('Idade: ' + str(idade_cliente))    # ✅ convertendo para str
print(f'Idade: {idade_cliente}')         # ✅ usando f-string
""")

nb.md(r"""
**Fatiamento (*slicing*)**: permite acessar um caractere ou um trecho da *string* a partir da sua **posição** (índice). Em Python, os índices **começam em 0**.

**Exemplo:** extraindo informações de um e-mail.
""")

nb.code(r"""
email = 'andre.perez@gmail.com'
""")

nb.md(r"""
**Acessando um único caractere** com `texto[indice]`:

| a | n | d | r | e | . | p | e | r | e | z | @ | g | m | a | i | l | . | c | o | m |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| -21 | -20 | -19 | -18 | -17 | -16 | -15 | -14 | -13 | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
""")

nb.code(r"""
# Índices positivos: contam a partir do início (0)
print(f'Posição 0:  {email[0]}')
print(f'Posição 11: {email[11]}')
""")

nb.code(r"""
# Índices negativos: contam a partir do final (-1 é o último caractere)
print(f'Posição -1: {email[-1]}')
print(f'Posição -2: {email[-2]}')
""")

nb.md(r"""
**Acessando um intervalo** com `texto[inicio:fim]`. O caractere da posição `inicio` **é incluído**, mas o da posição `fim` **não é**:
""")

nb.code(r"""
# Do índice 0 até o 10 (o 11, que é o '@', fica de fora)
usuario_email = email[0:11]
print(usuario_email)
""")

nb.code(r"""
# Do índice 12 até o final
provedor_email = email[12:21]
print(provedor_email)
""")

nb.md(r"""
> 💡 Se omitirmos o início, o fatiamento começa do primeiro caractere; se omitirmos o fim, ele vai até o último. Assim, `email[:11]` equivale a `email[0:11]` e `email[12:]` equivale a `email[12:21]`.
""")

nb.code(r"""
print(email[:11])
print(email[12:])
""")

nb.md(r"""
### 4.4 Métodos

*Strings* possuem diversos **métodos** nativos: funções que "pertencem" ao texto e são chamadas com a sintaxe `texto.metodo()`. Os mais usados no dia a dia são:

| Método | O que faz |
| --- | --- |
| `.upper()` | Converte para maiúsculas |
| `.lower()` | Converte para minúsculas |
| `.title()` | Primeira letra de cada palavra em maiúscula |
| `.strip()` | Remove espaços do início e do fim |
| `.find(trecho)` | Retorna a posição onde o trecho começa (ou `-1` se não encontrar) |
| `.replace(antigo, novo)` | Substitui um trecho por outro |
| `.split(separador)` | Divide o texto em partes a partir de um separador |
| `.count(trecho)` | Conta quantas vezes o trecho aparece |
""")

nb.code(r"""
endereco = 'Avenida Paulista, 1811, São Paulo, São Paulo, Brasil.'
""")

nb.code(r"""
# Maiúsculas e minúsculas
print(endereco.upper())
print(endereco.lower())
""")

nb.code(r"""
# Posição onde o trecho 'Brasil' começa
posicao_pais = endereco.find('Brasil')
print(posicao_pais)
""")

nb.code(r"""
# Substituindo 'Avenida' pela abreviação 'Av.'
print(endereco.replace('Avenida', 'Av.'))
""")

nb.code(r"""
# Contando quantas vezes 'São Paulo' aparece
print(endereco.count('São Paulo'))
""")

nb.code(r"""
# Limpando e padronizando um nome digitado pelo usuário
nome_digitado = '   maria DA silva   '
nome_padronizado = nome_digitado.strip().title()

print(nome_padronizado)
""")

nb.md(r"""
> 💡 *Strings* são **imutáveis**: os métodos não alteram o texto original, eles retornam uma **nova** *string*. Se quiser manter o resultado, guarde-o em uma variável.
""")

nb.code(r"""
# O texto original continua o mesmo após o replace
endereco.replace('Avenida', 'Av.')
print(endereco)

# Para manter a alteração, atribuímos o resultado a uma variável
endereco_abreviado = endereco.replace('Avenida', 'Av.')
print(endereco_abreviado)
""")

nb.md(r"""
### 4.5 Conversão

Podemos converter números em *strings* com `str()` e *strings* em números com `int()` ou `float()` — desde que o texto contenha apenas um número válido.
""")

nb.code(r"""
# int -> str
idade = 19
print(type(idade))

idade_texto = str(idade)
print(type(idade_texto))
""")

nb.code(r"""
# str -> float
valor_texto = '49.90'
valor_numerico = float(valor_texto)

print(valor_numerico * 2)
print(type(valor_numerico))
""")

nb.md(r"""
**Exemplo:** extraindo o valor numérico de um texto de faturamento. Combinamos **fatiamento** e **conversão**:
""")

nb.code(r"""
faturamento_texto = 'R$ 35 mi'
print(faturamento_texto)
print(type(faturamento_texto))

# Fatiamos apenas os caracteres do número ('35') e convertemos para int
faturamento_milhoes = int(faturamento_texto[3:5])
print(faturamento_milhoes)
print(type(faturamento_milhoes))
""")

nb.md(r"""
### 4.6 Revisitando a motivação

Vamos separar a latitude e a longitude da *startup*, que estão juntas no texto `latitude_longitude`.

**Passo 1:** encontrar a posição do caractere `;` que divide os dois valores:
""")

nb.code(r"""
posicao_separador = latitude_longitude.find(';')
print(posicao_separador)
""")

nb.md(r"""
**Passo 2:** extrair a latitude, que vai do início até o separador (sem incluí-lo):
""")

nb.code(r"""
latitude_startup = latitude_longitude[:posicao_separador]
print(latitude_startup)
""")

nb.md(r"""
**Passo 3:** extrair a longitude, que vai do caractere **seguinte** ao separador até o final:
""")

nb.code(r"""
longitude_startup = latitude_longitude[posicao_separador + 1:]
print(longitude_startup)
""")

nb.md(r"""
Pronto! Agora as duas bases estão no mesmo formato. Na próxima seção veremos como **comparar** esses valores — mas já dá para adiantar:
""")

nb.code(r"""
# O resultado True indica que os valores são iguais (veremos isso na seção 5)
print(latitude == latitude_startup)
print(longitude == longitude_startup)
""")

nb.md(r"""
> 💡 **Alternativa:** o método `.split(';')` faz a divisão em um único passo, retornando as partes do texto. Ele usa **listas**, um tipo de dado que veremos em módulos futuros.
""")

nb.code(r"""
latitude_startup, longitude_startup = latitude_longitude.split(';')

print(latitude_startup)
print(longitude_startup)
""")

nb.separador()

# =====================================================================
# 5. BOOLEANOS
# =====================================================================
nb.md(r"""
## 5. Booleanos

Todo programa precisa tomar decisões: liberar ou bloquear um acesso, aprovar ou recusar um pagamento, exibir ou esconder uma mensagem. Por trás de todas essas decisões estão os **booleanos**.
""")

nb.md(r"""
### 5.1 Motivação

Em *websites* (redes sociais, *e-commerces*, sistemas corporativos etc.) é comum o uso de sistemas de controle de acesso, o famoso ***login***. Em geral, o usuário informa dois dados: `usuario` e `senha`.
""")

nb.code(r"""
# Dados digitados pelo usuário na tela de login
usuario = 'andre.perez'
senha = 'andre123'
""")

nb.md(r"""
Do lado do servidor, o *backend* do *site* tem armazenados os dados informados no momento do cadastro: `usuario_cadastro` e `senha_cadastro`.
""")

nb.code(r"""
# Dados salvos no momento do cadastro
usuario_cadastro = 'andre.perez'
senha_cadastro = 'andre321'
""")

nb.md(r"""
**Como comparamos `usuario` com `usuario_cadastro` e `senha` com `senha_cadastro` para decidir se o acesso deve ser concedido ou bloqueado?**
""")

nb.md(r"""
### 5.2 Definição

Os booleanos armazenam **valores lógicos** e só podem assumir dois valores:

- `True` (verdadeiro);
- `False` (falso).

São do tipo `bool`.
""")

nb.code(r"""
verdadeiro = True
falso = False

print(verdadeiro)
print(falso)
print(type(verdadeiro))
""")

nb.md(r"""
Na prática, raramente escrevemos `True` ou `False` diretamente: os booleanos costumam ser o **resultado de comparações**. Os operadores de comparação são:

| Operador | Significado | Exemplo | Resultado |
| --- | --- | --- | --- |
| `>` | Maior que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 5` | `False` |
| `>=` | Maior ou igual a | `5 >= 5` | `True` |
| `<=` | Menor ou igual a | `3 <= 5` | `True` |

> ⚠️ Não confunda `=` (atribuição: guarda um valor) com `==` (comparação: verifica se dois valores são iguais).
""")

nb.md(r"""
**Exemplo:** caixa eletrônico. O saque só pode ser feito se o valor for menor ou igual ao saldo.
""")

nb.code(r"""
saldo_em_conta = 200
valor_do_saque = 100

pode_realizar_saque = valor_do_saque <= saldo_em_conta
print(pode_realizar_saque)
""")

nb.md(r"""
**Exemplo:** cartão de crédito. O pagamento só é aprovado se o código de segurança informado for igual ao cadastrado.
""")

nb.code(r"""
codigo_seguranca_informado = '852'
codigo_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_seguranca_informado == codigo_seguranca_cadastro
print(pode_efetuar_pagamento)
""")

nb.md(r"""
**Exemplo:** comparação de *strings* é **sensível a maiúsculas e minúsculas**. Para comparar ignorando essa diferença, padronize os textos antes:
""")

nb.code(r"""
email_digitado = 'Andre.Perez@Gmail.com'
email_cadastro = 'andre.perez@gmail.com'

print(email_digitado == email_cadastro)                  # False: letras diferentes
print(email_digitado.lower() == email_cadastro.lower())  # True: ambos em minúsculas
""")

nb.md(r"""
### 5.3 Operadores lógicos

Os operadores lógicos permitem **combinar** valores booleanos:

| Operador | Significado | Retorna `True` quando... |
| --- | --- | --- |
| `and` | E | **ambos** os valores são `True` |
| `or` | OU | **pelo menos um** dos valores é `True` |
| `not` | NÃO | o valor é `False` (inverte o resultado) |

O conjunto de resultados possíveis é resumido na chamada **tabela da verdade**:

| A | B | A `and` B | A `or` B | `not` A |
| --- | --- | --- | --- | --- |
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |
""")

nb.md(r"""
**Exemplo:** tabela da verdade do operador `and` (e).
""")

nb.code(r"""
print(True and True)
print(True and False)
print(False and True)
print(False and False)
""")

nb.md(r"""
**Exemplo:** tabela da verdade do operador `or` (ou).
""")

nb.code(r"""
print(True or True)
print(True or False)
print(False or True)
print(False or False)
""")

nb.md(r"""
**Exemplo:** tabela da verdade do operador `not` (não).
""")

nb.code(r"""
print(not True)
print(not False)
""")

nb.md(r"""
**Exemplo:** frete grátis. Uma loja oferece frete grátis para clientes **VIP** **ou** para compras acima de R\$ 200,00 — desde que o endereço **não** seja internacional.
""")

nb.code(r"""
cliente_vip = False
valor_compra = 250.00
endereco_internacional = False

compra_acima_do_minimo = valor_compra > 200
tem_frete_gratis = (cliente_vip or compra_acima_do_minimo) and not endereco_internacional

print(tem_frete_gratis)
""")

nb.md(r"""
> 💡 Você também pode encontrar os operadores `&` (e) e `|` (ou) em alguns códigos — eles funcionam com booleanos e são muito usados em bibliotecas como o **Pandas**. No Python "puro", porém, a forma recomendada e mais legível é usar `and`, `or` e `not`.
""")

nb.md(r"""
### 5.4 Conversão

Podemos converter qualquer valor para booleano com a função nativa `bool()`. A regra é simples: valores que representam **"vazio" ou "zero"** viram `False`; todo o resto vira `True`.

| Valor | `bool(valor)` |
| --- | --- |
| `0` e `0.0` | `False` |
| `""` (*string* vazia) | `False` |
| `None` | `False` |
| Qualquer outro número (ex: `19`, `-3.5`) | `True` |
| Qualquer *string* não vazia (ex: `'O-'`, `' '`) | `True` |
""")

nb.code(r"""
idade = 19
tipo_sanguineo = 'O-'
quantidade_filhos = 0
telefone_fixo = None
telefone_comercial = ''

print(bool(idade))               # número diferente de zero -> True
print(bool(tipo_sanguineo))      # string com conteúdo      -> True
print(bool(quantidade_filhos))   # zero                     -> False
print(bool(telefone_fixo))       # None                     -> False
print(bool(telefone_comercial))  # string vazia             -> False
""")

nb.md(r"""
### 5.5 Revisitando a motivação

Agora podemos resolver o problema do *login*.

**Passo 1:** comparar os dados informados pelo usuário com os dados do cadastro:
""")

nb.code(r"""
usuario_correto = usuario == usuario_cadastro
senha_correta = senha == senha_cadastro

print(f'Usuário correto? {usuario_correto}')
print(f'Senha correta?   {senha_correta}')
""")

nb.md(r"""
**Passo 2:** decidir se o acesso deve ser concedido. Para isso, **as duas** condições precisam ser verdadeiras, então usamos o operador `and`:
""")

nb.code(r"""
conceder_acesso = usuario_correto and senha_correta
print(f'Acesso concedido? {conceder_acesso}')
""")

nb.md(r"""
Como a senha digitada (`andre123`) é diferente da cadastrada (`andre321`), o acesso foi **bloqueado**. Experimente alterar o valor da variável `senha` na seção 5.1 e executar as células novamente!
""")

nb.separador()

# =====================================================================
# RESUMO
# =====================================================================
nb.md(r"""
## Resumo do Módulo

| Tipo | O que armazena | Exemplo | Principais operações |
| --- | --- | --- | --- |
| `int` | Números inteiros | `42` | `+ - * / // % **` |
| `float` | Números decimais | `3.14` | `+ - * / // % **`, `round()` |
| `str` | Textos | `'Python'` | `+`, `*`, *f-strings*, fatiamento, métodos |
| `bool` | Valores lógicos | `True` | Comparações, `and`, `or`, `not` |
| `NoneType` | Ausência de valor | `None` | — |

Funções nativas vistas neste módulo: `print()`, `type()`, `len()`, `round()`, `int()`, `float()`, `complex()`, `str()` e `bool()`.
""")


nb.salvar(sys.argv[1] if len(sys.argv) > 1 else "module_01.ipynb")
