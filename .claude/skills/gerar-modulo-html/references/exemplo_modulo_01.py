"""PADRÃO OURO — script que publica a aula 1 do Módulo 01 do Python na Prática.

Esta é a primeira aula de `content_generation/jupyter_notebooks/module_01.ipynb`
(a seção "## 1. Introdução ao Google Colab") virando a página
`course_content/pt_br/python-na-pratica/python-variaveis-e-tipos-de-dados/colab.html`.

Leia este arquivo antes de publicar um módulo, para calibrar:
  * o tamanho e o recorte de cada bloco;
  * como a saída do `print()` entra como comentário no código;
  * o tom das alternativas do quiz (a explicação diz o *porquê*);
  * o formato do manifesto que o `registrar_modulo.py` consome.

O resultado completo das 5 aulas está publicado em
`course_content/pt_br/python-na-pratica/python-variaveis-e-tipos-de-dados/` —
abra aqueles arquivos para ver o padrão pronto. Não copie o conteúdo, só o padrão.

Para rodar:
    python .claude/skills/gerar-modulo-html/references/exemplo_modulo_01.py [pasta_de_saida]
"""

import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from construtor_pagina import Pagina  # noqa: E402

BOOTCAMP = "python-na-pratica"
MODULO = "python-variaveis-e-tipos-de-dados"


def pagina_colab():
    """Seção '## 1. Introdução ao Google Colab' do notebook.

    O título da aula NÃO entra aqui: o `<h1>` é montado por pages/module.html a
    partir do `title` do lessons.json. As subseções do notebook ('### 1.1
    Ferramenta web') viram h2, que é o único nível de título que o tema estiliza.
    """
    pagina = Pagina()
    pagina.p(
        "O **Google Colab** (*Colaboratory*) é uma ferramenta gratuita do Google que permite "
        "escrever e executar código Python direto no navegador, sem instalar nada no computador. "
        "Ele é baseado no **Jupyter Notebook**, o formato de caderno interativo mais usado no "
        "mercado de dados e ciência de dados."
    )

    pagina.h2("Ferramenta web")
    pagina.p(
        "Por ser uma ferramenta **100% web**, tudo o que você precisa é de um navegador e de uma "
        "conta Google:"
    )
    # Links do notebook não viram <a> no meio do texto: o padrão do site é
    # deixá-los na lista de recursos, no fim da aula (veja o manifesto).
    pagina.lista(
        [
            "Crie (ou use) uma conta Google;",
            "Acesse o Colab pelo endereço `colab.research.google.com`;",
            "Clique em **Arquivo > Novo notebook** para criar o seu primeiro caderno.",
        ],
        ordenada=True,
    )
    # '> 💡 **Dica:** ...' do notebook vira uma citação; o emoji sai, porque no
    # site quem dá o destaque é a barra lateral do bloco.
    pagina.citacao(
        "**Dica:** os notebooks criados ficam salvos automaticamente no seu Google Drive, "
        "na pasta **Colab Notebooks**."
    )

    pagina.h2("Ambiente autogerenciado")
    pagina.p(
        "Dizemos que o Colab é **autogerenciado** porque o próprio Google cuida de toda a "
        "infraestrutura para você:"
    )
    pagina.lista([
        "Ao conectar, o Google **provisiona uma máquina virtual** (um computador na nuvem) "
        "exclusiva para a sua sessão;",
        "Essa máquina é **temporária**: no plano gratuito ela dura no máximo cerca de "
        "**12 horas** e pode ser desconectada antes disso por inatividade;",
        "Quando a sessão termina, **as variáveis e os arquivos temporários são perdidos** - o "
        "notebook (texto e código) continua salvo, mas será preciso executar as células novamente.",
    ])

    pagina.h2("Notebooks e células")
    pagina.p(
        "Um **notebook** (caderno) é um documento web composto por uma sequência de blocos "
        "chamados **células**. Existem dois tipos:"
    )
    pagina.tabela(
        ["Tipo de célula", "Para que serve", "O que acontece ao executar"],
        [
            ["**Texto**", "Explicações, títulos, listas e tabelas", "O texto é formatado e exibido"],
            ["**Código**", "Instruções em Python", "O código é executado e o resultado aparece logo abaixo"],
        ],
    )
    pagina.p("Alguns atalhos úteis no Colab:")
    pagina.tabela(
        ["Atalho", "Ação"],
        [
            ["`Shift + Enter`", "Executa a célula e vai para a próxima"],
            ["`Ctrl + Enter`", "Executa a célula e permanece nela"],
            ["`Ctrl + M` depois `B`", "Cria uma nova célula abaixo"],
            ["`Ctrl + M` depois `M`", "Converte a célula em texto"],
            ["`Ctrl + M` depois `Y`", "Converte a célula em código"],
        ],
    )

    pagina.p(
        "Vamos ao nosso primeiro código! A função `print()` exibe na tela o que estiver entre os "
        "parênteses:"
    )
    # O site não tem playground de Python, então a saída da célula do notebook
    # entra como comentário, na linha do print ou logo abaixo dele.
    pagina.codigo("""
# Nosso primeiro programa: exibindo uma mensagem na tela
print("Olá, mundo!")
# Olá, mundo!
""")

    pagina.p(
        "Um detalhe importante: todas as células de um notebook **compartilham o mesmo estado**. "
        "Ou seja, algo criado em uma célula fica disponível nas outras - desde que a célula onde "
        "foi criado tenha sido **executada antes**. Veja o que acontece ao executar estas duas "
        "células, nesta ordem:"
    )
    # Duas células do notebook = dois blocos de código, para preservar a ideia
    # de "executei uma, depois a outra".
    pagina.codigo("""
# Célula 1 - criando uma mensagem
mensagem_boas_vindas = "Bem-vindo ao Ready To Deploy!"
""")
    pagina.codigo("""
# Célula 2 - utilizando a mensagem criada na célula anterior
print(mensagem_boas_vindas)
# Bem-vindo ao Ready To Deploy!
""")
    pagina.citacao(
        "**Atenção:** a ordem de execução importa, não a posição na página. Se você executar a "
        "segunda célula sem ter executado a primeira, o Python vai acusar um erro (`NameError`), "
        "pois a variável ainda não existe."
    )

    # Um quiz por aula, sempre no fim. A explicação aparece depois da resposta,
    # tanto no acerto quanto no erro, então ela ensina — não julga.
    pagina.quiz(
        "python-colab",
        "O que acontece se você executar uma célula que usa uma variável criada em outra célula "
        "ainda não executada?",
        [
            ("O Python usa o valor 0 por padrão",
             "O Python não inventa valores para nomes que não existem.", False),
            ("O Python gera um erro NameError",
             "A variável ainda não existe na memória, então o Python não a encontra.", True),
            ("O Colab executa a célula anterior automaticamente",
             "O Colab nunca executa outras células sozinho - a ordem é sempre manual.", False),
            ("Nada acontece, o valor fica vazio",
             "Sem a variável na memória, o Python não tem como continuar - ele interrompe "
             "com um erro.", False),
        ],
    )
    return pagina


# O manifesto fecha o ciclo: ele diz ao registrar_modulo.py quais páginas viram
# aulas, em que ordem, e com quais recursos. O campo `content` do lessons.json é
# montado por ele como <bootcamp>/<módulo>/<arquivo> — não escreva o caminho à mão.
MANIFESTO = {
    "bootcamp_id": BOOTCAMP,
    "module_id": MODULO,
    "title": "Módulo 1 — Variáveis e Tipos de Dados",
    "description": "Primeiro módulo do Python na Prática: Google Colab, variáveis, números, "
                   "strings e booleanos, sempre partindo de problemas reais do dia a dia.",
    "level": "Iniciante",
    "skills": ["python", "google-colab", "variaveis", "tipos-de-dados", "numeros",
               "strings", "booleanos"],
    "hot": False,
    "lessons": [
        {
            "id": "python-colab",
            "title": "Introdução ao Google Colab",
            "navTitle": "Google Colab",
            "badge": "essencial",
            "readTime": "3 min de leitura",   # o salvar() sugere este número
            "arquivo": "colab.html",
            "resources": [
                {
                    "name": "Google Colaboratory - página oficial",
                    "href": "https://colab.research.google.com/",
                    "tags": [{"label": "Doc", "free": False}, {"label": "Grátis", "free": True}],
                },
            ],
        },
        # ... as outras quatro aulas do módulo (variaveis, numeros, strings, booleanos)
    ],
}


def main():
    # Sem argumento, escreve num diretório temporário: este script é para
    # consultar e conferir, não para republicar a aula que já está no ar.
    destino = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        tempfile.gettempdir(), "exemplo_" + MODULO)
    pagina_colab().salvar(os.path.join(destino, "colab.html"))

    caminho_manifesto = os.path.join(destino, "manifesto.json")
    with open(caminho_manifesto, "w", encoding="utf-8") as arquivo:
        json.dump(MANIFESTO, arquivo, ensure_ascii=False, indent=2)
    print("manifesto de exemplo em " + caminho_manifesto)


if __name__ == "__main__":
    main()
