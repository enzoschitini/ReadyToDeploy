"""Exemplo de referência (padrão ouro): script que gerou o Projeto Prático do Módulo 01.

Baseado em content_generation/jupyter_notebooks/module_01.ipynb. Use como modelo
de tom, ritmo das missões, nível de guia (dados prontos + # TODO), formato das
mensagens dos personagens e de como cada "Resultado esperado" tem uma solução
que o comprova. Não copie o conteúdo: cada módulo tem os seus conceitos.

Execução:
    python exemplo_projeto_modulo_01.py content_generation/jupyter_notebooks/module_01_projeto_pratico.ipynb
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from construtor_projeto import ProjetoPratico, mensagem  # noqa: E402

nb = ProjetoPratico()


# =====================================================================
# ABERTURA: cabeçalho, contexto, objetivo, requisitos, como funciona
# =====================================================================
nb.cabecalho("01", "Sabor Express integra a Cantina da Vó", r"""
Chegou a hora de sair da teoria e colocar a mão no código! Neste projeto você vai usar tudo o que aprendeu no Módulo 01 — **variáveis**, **números**, ***strings*** e **booleanos** — para resolver, em uma única história, um desafio bem parecido com o que aparece no dia a dia de quem trabalha com dados.
""")

nb.md(r"""
## 📖 O contexto

A **Sabor Express** é um aplicativo de delivery que está crescendo rápido. Na semana passada, ela comprou a **Cantina da Vó**, uma pequena rede de restaurantes muito querida na cidade — e adivinha quem acabou de ser contratado(a) para ajudar nessa integração? Você! 🎉

Seu primeiro dia como **Analista de Dados Jr.** começa agora. O time te chamou no chat interno com uma lista de tarefas para hoje, organizadas em **missões**. Cada missão usa um pedaço do que você aprendeu no Módulo 01 — e, no final do dia, você vai juntar tudo em um painel para apresentar na reunião de fechamento.

> 💡 **Dica:** não existe só uma forma "certa" de resolver cada missão. Depois de cada uma você vai encontrar o resultado esperado, mas o caminho até lá é seu. Teste, erre, corrija e tente de novo — é assim que se aprende a programar.
""")

nb.md(r"""
## 🎯 Objetivo

Ao final deste projeto, você terá praticado, dentro de um único cenário conectado:

- Criação e nomenclatura de **variáveis**;
- Operações e conversões com **números** (`int` e `float`);
- Manipulação de ***strings*** (concatenação, *f-strings*, fatiamento e métodos);
- Tomada de decisão com **booleanos** (comparações e operadores lógicos).

Nada de exercícios soltos e sem contexto: tudo aqui acontece dentro da mesma história, do jeito que aconteceria em um projeto de verdade.
""")

nb.md(r"""
## 🧰 Requisitos

Antes de começar, confira se você tem em mãos:

| Requisito | Detalhe |
| --- | --- |
| 🌐 Google Colab | Este notebook aberto e pronto para rodar (a seção 1 do Módulo 01 relembra os atalhos) |
| 📗 Conceitos do Módulo 01 | Variáveis, números, *strings* e booleanos |
| 🧠 Funções nativas | `print()`, `type()`, `len()`, `round()`, `int()`, `float()`, `str()`, `bool()` |
| 📦 Bibliotecas externas | Nenhuma! Só Python puro, do jeitinho que você aprendeu |

Não é necessário nenhum conhecimento além do que foi visto no Módulo 01. Se alguma missão parecer difícil, a dica de cada uma aponta a seção certa para revisar. 😉
""")

nb.md(r"""
## 🗺️ Como o projeto funciona

O notebook está dividido em **5 missões**, na ordem em que a Sabor Express te chamou:

| Missão | Tema | Conceito principal |
| --- | --- | --- |
| 1️⃣ | Ficha de cadastro do restaurante | Variáveis e tipos |
| 2️⃣ | Fechamento de caixa | Números |
| 3️⃣ | Unificando os cadastros | *Strings* |
| 4️⃣ | Central de acesso | Booleanos |
| 5️⃣ | Painel de boas-vindas | Tudo junto! |

Em cada missão você vai encontrar:

- 💬 uma mensagem de alguém do time, com o pedido;
- 💻 uma célula de código com os dados já prontos e comentários `# TODO` indicando onde você precisa escrever;
- 🔎 **Resultado esperado**, uma prévia do que deve aparecer na tela quando estiver certo;
- 💡 **Dica**, para quando bater aquele branco.

Bora lá?
""")

nb.separador()


# =====================================================================
# MISSÃO 1: variáveis e tipos
# =====================================================================
nb.md(r"""
## 1️⃣ Missão 1 — Ficha de cadastro do restaurante

""" + mensagem("Marina", "Gerente de Cadastro", "Oii, bem-vindo(a) à equipe! Antes de qualquer coisa, preciso que você cadastre a Cantina da Vó no nosso sistema. Cria aí as variáveis com os dados básicos do restaurante, por favor?") + r"""

**Sua missão:** criar as 5 variáveis abaixo (você escolhe os valores, mas respeite o tipo pedido) e depois imprimir o tipo de cada uma com `type()`, só para confirmar que ficou tudo certo.

| Variável | Tipo esperado | Exemplo de valor |
| --- | --- | --- |
| `nome_restaurante` | `str` | `'Cantina da Vó'` |
| `cidade` | `str` | `'São Paulo'` |
| `taxa_entrega` | `float` | `6.90` |
| `tempo_medio_entrega_min` | `int` | `35` |
| `esta_aberto` | `bool` | `True` |
""")

nb.exercicio(r"""
# 🏪 Ficha de cadastro da Cantina da Vó
# TODO: crie as 5 variáveis pedidas pela Marina
# nome_restaurante = ...
# cidade = ...
# taxa_entrega = ...
# tempo_medio_entrega_min = ...
# esta_aberto = ...


# TODO: imprima o tipo de cada variável, uma por linha, usando type()
""", solucao=r"""
nome_restaurante = 'Cantina da Vó'
cidade = 'São Paulo'
taxa_entrega = 6.90
tempo_medio_entrega_min = 35
esta_aberto = True

print(type(nome_restaurante))
print(type(cidade))
print(type(taxa_entrega))
print(type(tempo_medio_entrega_min))
print(type(esta_aberto))
""")

nb.resultado_esperado(r"""
<class 'str'>
<class 'str'>
<class 'float'>
<class 'int'>
<class 'bool'>
""", legenda="os valores podem variar, mas os tipos devem ser estes, nesta ordem")

nb.dica("revise a seção 2.3 (Tipos nativos) do Módulo 01 se tiver dúvida sobre qual tipo usar em cada caso. E não esqueça: nomes de variáveis seguem o padrão `snake_case`.")

nb.separador()


# =====================================================================
# MISSÃO 2: números
# =====================================================================
nb.md(r"""
## 2️⃣ Missão 2 — Fechamento de caixa

""" + mensagem("Diego", "Financeiro", "Fechei aqui os três primeiros dias de venda da Cantina da Vó já dentro do nosso app. Preciso do ticket médio de cada dia e do ticket médio do período inteiro pra reunião de amanhã. Ah, e será que a terça-feira cresceu muito em cima da segunda? Isso ia impressionar a diretoria 👀") + r"""

| Dia | Valor total das vendas (R\$) | Quantidade de vendas |
| --- | --- | --- |
| Segunda (05/02) | 428.50 | 6 |
| Terça (06/02) | 512.75 | 9 |
| Quarta (07/02) | 275.30 | 4 |

**Sua missão:**

1. Calcular o ticket médio de cada dia, arredondado para 2 casas decimais, nas variáveis `ticket_medio_segunda`, `ticket_medio_terca` e `ticket_medio_quarta`;
2. Calcular o **ticket médio do período inteiro** em `ticket_medio_periodo` — lembre-se da diferença entre tirar a média simples dos três tickets e aplicar a fórmula ao total do período (Módulo 01, seção 3.5);
3. Calcular em `crescimento_terca_percentual` quantos **por cento** as vendas de terça cresceram em relação às de segunda;
4. Imprimir tudo com rótulos, como no resultado esperado.
""")

nb.exercicio(r"""
# 💰 Vendas dos três primeiros dias da Cantina da Vó no app da Sabor Express
valor_vendas_segunda = 428.50
quantidade_vendas_segunda = 6

valor_vendas_terca = 512.75
quantidade_vendas_terca = 9

valor_vendas_quarta = 275.30
quantidade_vendas_quarta = 4

# TODO 1: ticket_medio_segunda, ticket_medio_terca e ticket_medio_quarta


# TODO 2: ticket_medio_periodo
# (some todos os valores, some todas as quantidades e só depois divida)


# TODO 3: crescimento_terca_percentual
# (fórmula: (valor_novo - valor_antigo) / valor_antigo * 100)


# TODO 4: imprima os resultados com rótulos
""", solucao=r"""
ticket_medio_segunda = round(valor_vendas_segunda / quantidade_vendas_segunda, 2)
ticket_medio_terca = round(valor_vendas_terca / quantidade_vendas_terca, 2)
ticket_medio_quarta = round(valor_vendas_quarta / quantidade_vendas_quarta, 2)

valor_total_periodo = valor_vendas_segunda + valor_vendas_terca + valor_vendas_quarta
quantidade_total_periodo = quantidade_vendas_segunda + quantidade_vendas_terca + quantidade_vendas_quarta
ticket_medio_periodo = round(valor_total_periodo / quantidade_total_periodo, 2)

crescimento_terca_percentual = round((valor_vendas_terca - valor_vendas_segunda) / valor_vendas_segunda * 100, 2)

print(f'Ticket médio segunda: {ticket_medio_segunda:.2f}')
print(f'Ticket médio terça:   {ticket_medio_terca:.2f}')
print(f'Ticket médio quarta:  {ticket_medio_quarta:.2f}')
print(f'Ticket médio período: {ticket_medio_periodo:.2f}')
print(f'Crescimento de terça em relação à segunda: {crescimento_terca_percentual:.2f}%')
""")

nb.resultado_esperado(r"""
Ticket médio segunda: 71.42
Ticket médio terça:   56.97
Ticket médio quarta:  68.83
Ticket médio período: 64.03
Crescimento de terça em relação à segunda: 19.66%
""")

nb.dica("use `round()` para arredondar e uma *f-string* com `:.2f` para formatar a saída. Se o seu ticket médio do período deu `65.74`, você tirou a média simples dos três tickets — releia a seção 3.5, o Diego caiu nessa mesma pegadinha outro dia.")

nb.separador()


# =====================================================================
# MISSÃO 3: strings
# =====================================================================
nb.md(r"""
## 3️⃣ Missão 3 — Unificando os cadastros

""" + mensagem("Paula", "Integração de Dados", "O sistema antigo da Cantina da Vó guardava o endereço tudo junto, num textão separado por ponto e vírgula. Aqui a gente guarda cada pedaço em uma variável. Você consegue converter isso pra mim? Também recebi um cadastro de cliente digitado todo torto — dá uma arrumada nele também, por favor.") + r"""

**Parte A — Endereço.** No sistema antigo, o endereço está armazenado em `endereco_antigo`, com quatro pedaços separados por `;`: **rua**, **cidade**, **estado** e **CEP**. Separe-os nas variáveis `rua`, `cidade_cantina`, `estado` e `cep` e imprima cada uma.

**Parte B — Cadastro de cliente.** Um cliente digitou o próprio nome com espaços sobrando e letras bagunçadas. Guarde em `nome_cliente` o nome sem os espaços das pontas e com a primeira letra de cada palavra em maiúscula, e imprima.

**Parte C — Mensagem de boas-vindas.** Com uma *f-string*, monte `mensagem_boas_vindas` combinando `nome_cliente`, `nome_restaurante` (da Missão 1) e `cidade_cantina`, neste formato, e imprima:

`Bem-vindo(a), <nome do cliente>! <nome do restaurante> agora faz parte da Sabor Express em <cidade>.`
""")

nb.exercicio(r"""
# 🗺️ Parte A: separando o endereço antigo em 4 variáveis
endereco_antigo = 'Rua das Flores, 245;São Paulo;SP;01234-000'

# TODO: crie rua, cidade_cantina, estado e cep e imprima cada uma


# 🧹 Parte B: limpando o cadastro de um cliente
nome_digitado = '   ana PAULA dos santos   '

# TODO: crie nome_cliente, já limpo e formatado, e imprima


# 💌 Parte C: mensagem de boas-vindas
# TODO: monte mensagem_boas_vindas com uma f-string e imprima
""", solucao=r"""
rua, cidade_cantina, estado, cep = endereco_antigo.split(';')
print(rua)
print(cidade_cantina)
print(estado)
print(cep)

nome_cliente = nome_digitado.strip().title()
print(nome_cliente)

mensagem_boas_vindas = f'Bem-vindo(a), {nome_cliente}! {nome_restaurante} agora faz parte da Sabor Express em {cidade_cantina}.'
print(mensagem_boas_vindas)
""")

nb.resultado_esperado(r"""
Rua das Flores, 245
São Paulo
SP
01234-000
Ana Paula Dos Santos
""", legenda="Partes A e B; a mensagem da Parte C depende do nome que você escolheu na Missão 1", confere="inicio")

nb.dica("para a Parte A, lembre do `.split(';')` que separou `latitude` e `longitude` na seção 4.6 do Módulo 01 — aqui é o mesmo truque, só que desempacotando em 4 variáveis em vez de 2. Para a Parte B, combine `.strip()` com `.title()`, como no exemplo do nome digitado pelo usuário (seção 4.4).")

nb.separador()


# =====================================================================
# MISSÃO 4: booleanos
# =====================================================================
nb.md(r"""
## 4️⃣ Missão 4 — Central de acesso

""" + mensagem("Rafa", "Operações", "Duas coisas urgentes: primeiro, preciso saber se um pedido específico tem direito a frete grátis. Segundo, o João, um dos entregadores da Cantina da Vó, está tentando entrar no nosso sistema com o usuário e a senha que usava lá, e eu preciso que o código me diga se o acesso deve ser liberado.") + r"""

**Parte A — Frete grátis.** A regra da Sabor Express é: o pedido tem frete grátis se o cliente for **VIP** *ou* se o valor do pedido for **maior que R\$ 60,00** — mas só se o endereço estiver dentro da **área atendida**. Crie `tem_frete_gratis` combinando os dados da célula com comparações, `and` e `or`.

**Parte B — Acesso do entregador.** Compare o usuário e a senha que o João digitou com os que estavam cadastrados, guardando os resultados em `usuario_correto` e `senha_correta`. Depois crie `acesso_liberado`, que só pode ser `True` se **as duas** comparações forem verdadeiras.

No final, imprima os quatro resultados com rótulos.
""")

nb.exercicio(r"""
# 🚚 Parte A: o pedido tem direito a frete grátis?
cliente_vip = False
valor_pedido = 74.90
area_atendida = True

# TODO: crie tem_frete_gratis


# 🔐 Parte B: o acesso do entregador deve ser liberado?
usuario_digitado = 'joao.entregador'
senha_digitada = 'vo2024'

usuario_cadastro = 'joao.entregador'
senha_cadastro = 'vo2023'

# TODO: crie usuario_correto, senha_correta e acesso_liberado


# TODO: imprima os quatro resultados com rótulos
""", solucao=r"""
compra_acima_do_minimo = valor_pedido > 60
tem_frete_gratis = (cliente_vip or compra_acima_do_minimo) and area_atendida

usuario_correto = usuario_digitado == usuario_cadastro
senha_correta = senha_digitada == senha_cadastro
acesso_liberado = usuario_correto and senha_correta

print(f'Frete grátis?    {tem_frete_gratis}')
print(f'Usuário correto? {usuario_correto}')
print(f'Senha correta?   {senha_correta}')
print(f'Acesso liberado? {acesso_liberado}')
""")

nb.resultado_esperado(r"""
Frete grátis?    True
Usuário correto? True
Senha correta?   False
Acesso liberado? False
""")

nb.dica("o João digitou `vo2024`, mas a senha cadastrada é `vo2023` — provavelmente ele se confundiu com o ano. Pegar esse tipo de detalhe é exatamente o papel de um sistema de *login*. Se o seu resultado deu diferente, revise a seção 5.3 (operadores lógicos) e o exemplo do frete grátis, logo depois da tabela da verdade.")

nb.separador()


# =====================================================================
# MISSÃO FINAL: integração (resultado aberto, com exemplo conferido)
# =====================================================================
nb.md(r"""
## 5️⃣ Missão 5 — Painel de boas-vindas

""" + mensagem("Ana Lívia", "CEO", "Adorei o trabalho de hoje! Pra fechar o dia com chave de ouro, monta um painel único juntando tudo que você descobriu — cadastro, vendas, integração e acesso. Vou mostrar isso pra diretoria amanhã de manhã.") + r"""

**Sua missão:** usando `print()` e *f-strings*, monte um painel que reúna em um único bloco de texto, pelo menos:

- O nome e a cidade do restaurante (Missão 1);
- O ticket médio do período (Missão 2);
- A mensagem de boas-vindas (Missão 3);
- Se o pedido de exemplo tem frete grátis e se o acesso do entregador foi liberado (Missão 4).

Capriche na formatação: use `'-' * 40` (ou o caractere que preferir) para criar linhas separadoras, como o `separador` da seção 4.3. Aqui **não existe gabarito único** — o painel é seu, deixe com a sua cara!
""")

nb.exercicio(r"""
# 📊 Painel de boas-vindas — Sabor Express x Cantina da Vó
# TODO: monte o seu painel reaproveitando as variáveis das Missões 1 a 4.
# Use print(), f-strings e o operador * para criar os separadores.
""", solucao=r"""
separador = '-' * 40

print(separador)
print(f'🍝 {nome_restaurante} — {cidade}')
print(separador)
print(f'Ticket médio do período: R$ {ticket_medio_periodo:.2f}')
print(mensagem_boas_vindas)
print(f'Frete grátis no pedido de exemplo? {tem_frete_gratis}')
print(f'Acesso do entregador liberado?     {acesso_liberado}')
print(separador)
""")

nb.resultado_esperado(r"""
----------------------------------------
🍝 Cantina da Vó — São Paulo
----------------------------------------
Ticket médio do período: R$ 64.03
Bem-vindo(a), Ana Paula Dos Santos! Cantina da Vó agora faz parte da Sabor Express em São Paulo.
Frete grátis no pedido de exemplo? True
Acesso do entregador liberado?     False
----------------------------------------
""", titulo="Exemplo de resultado", legenda="o seu pode — e deve — ficar diferente; essa é só uma ideia de formato")

nb.dica("se travar na formatação, comece simples: um `print()` por linha já resolve. Só depois de funcionar é que vale a pena caprichar nos separadores e no alinhamento.")

nb.separador()


# =====================================================================
# DESAFIOS EXTRAS (opcionais)
# =====================================================================
nb.md(r"""
## 🌟 Desafios extras

As missões acima já cobrem tudo o que você precisa do Módulo 01. Os desafios abaixo são **totalmente opcionais** — encare como um "modo difícil" para quem quer espremer um pouco mais os conceitos. Vá na ordem que quiser, ou pule direto para o que mais te chamar atenção.
""")

nb.md(r"""
### 🎟️ Extra 1 — Cupom de desconto

A Cantina da Vó está migrando também os cupons promocionais antigos. Cada código guarda o desconto (em %) nos **dois últimos caracteres**. Extraia o desconto do código fatiando a *string*, converta para `int` e aplique-o ao `valor_pedido`, arredondando para 2 casas decimais.
""")

nb.exercicio(r"""
# 🎟️ Extra 1: cupom de desconto
codigo_promo = 'PROMOVO10'
valor_pedido = 74.90

# TODO: crie desconto_percentual (int) e valor_com_desconto, e imprima os dois
""", solucao=r"""
desconto_percentual = int(codigo_promo[-2:])
valor_com_desconto = round(valor_pedido - valor_pedido * desconto_percentual / 100, 2)

print(f'Desconto: {desconto_percentual}%')
print(f'Valor com desconto: R$ {valor_com_desconto:.2f}')
""")

nb.resultado_esperado(r"""
Desconto: 10%
Valor com desconto: R$ 67.41
""")

nb.md(r"""
### 🔢 Extra 2 — Pedido par ou ímpar

A logística da Sabor Express separa os entregadores em rotas pares e ímpares, olhando o número do pedido. Use o operador `%` para calcular `resto_da_divisao` do número do pedido por 2 e, com uma comparação, crie `pedido_par` (lembre do exemplo do número do pedido na seção 3.3).
""")

nb.exercicio(r"""
# 🔢 Extra 2: pedido par ou ímpar
numero_pedido = 4831

# TODO: crie resto_da_divisao e pedido_par, e imprima os dois
""", solucao=r"""
resto_da_divisao = numero_pedido % 2
pedido_par = resto_da_divisao == 0

print(f'Resto da divisão por 2: {resto_da_divisao}')
print(f'Pedido par? {pedido_par}')
""")

nb.resultado_esperado(r"""
Resto da divisão por 2: 1
Pedido par? False
""")

nb.md(r"""
### 🏅 Extra 3 — Dia recorde

Sem nenhuma estrutura nova — só comparações e operadores lógicos — descubra se a **segunda-feira** teve o maior ticket médio dos três dias, ou seja, se `ticket_medio_segunda` foi maior que `ticket_medio_terca` **e** maior que `ticket_medio_quarta` (variáveis da Missão 2).
""")

nb.exercicio(r"""
# 🏅 Extra 3: a segunda-feira foi o dia de maior ticket médio?
# TODO: crie segunda_foi_o_melhor_dia e imprima o resultado
""", solucao=r"""
segunda_foi_o_melhor_dia = ticket_medio_segunda > ticket_medio_terca and ticket_medio_segunda > ticket_medio_quarta
print(f'A segunda teve o maior ticket médio? {segunda_foi_o_melhor_dia}')
""")

nb.resultado_esperado("A segunda teve o maior ticket médio? True")

nb.md(r"""
### ⭐ Extra 4 — O cliente avaliou o pedido?

Alguns pedidos ainda não têm avaliação, e o sistema guarda isso como `None`. Use `bool()` para criar `cliente_avaliou`. Depois, troque a nota por `5` e rode de novo. E se a nota fosse `0`? Pense no resultado antes de testar 😉 (a tabela da seção 5.4 tem a resposta).
""")

nb.exercicio(r"""
# ⭐ Extra 4: o cliente avaliou o pedido?
nota_avaliacao = None

# TODO: crie cliente_avaliou usando bool() e imprima
""", solucao=r"""
cliente_avaliou = bool(nota_avaliacao)
print(f'Cliente avaliou? {cliente_avaliou}')
""")

nb.resultado_esperado("Cliente avaliou? False", legenda="com `nota_avaliacao = None`")

nb.md(r"""
### 🎨 Extra 5 — Recibo estiloso

Monte um recibo decorado para o pedido de exemplo, com cabeçalho, itens e total. Combine a repetição de caracteres (`*`), *f-strings* e métodos como `.upper()` e `.title()`. Aqui não tem resultado esperado: solte a criatividade! 🎨
""")

nb.exercicio(r"""
# 🎨 Extra 5: seu recibo estiloso
# TODO: capriche!
""")

nb.separador()


# =====================================================================
# CHECKLIST
# =====================================================================
nb.md(r"""
## ✅ Checklist de autoavaliação

Sem provas, sem notas — só uma conferida rápida para você saber onde está:

- [ ] Criei as 5 variáveis da Missão 1 e confirmei os tipos com `type()`
- [ ] Calculei os tickets médios diários e o do período, sem cair na pegadinha da média simples (Missão 2)
- [ ] Separei o endereço antigo em 4 variáveis com `.split(';')` (Missão 3)
- [ ] Limpei o nome do cliente com `.strip()` e `.title()` e montei a mensagem com uma *f-string* (Missão 3)
- [ ] Combinei comparações com `and` e `or` para decidir o frete grátis e o acesso do entregador (Missão 4)
- [ ] Montei o painel final reaproveitando as variáveis das missões anteriores (Missão 5)
- [ ] Tentei pelo menos um dos desafios extras 🌟

Se a maioria dos itens está marcada, parabéns: você colocou em prática tudo o que a Sabor Express (e o Módulo 01) esperavam de você. 🎉

Prepare-se, porque no **Módulo 02** a história continua: a Sabor Express não para de crescer, e guardar cada pedido em uma variável separada não vai dar conta. Hora de conhecer **listas**, **conjuntos** e **dicionários**!
""")


nb.salvar(sys.argv[1] if len(sys.argv) > 1 else "module_01_projeto_pratico.ipynb")
