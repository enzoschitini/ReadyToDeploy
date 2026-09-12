"""Construtor das páginas HTML de aula do curso Ready To Deploy.

Cada aula do site é um **fragmento** de HTML (não uma página inteira): o
esqueleto, o cabeçalho e a barra lateral vêm de `pages/module.html`, que injeta
este arquivo no meio do artigo. Por isso o fragmento nunca tem <html>, <head>,
<body> nem <h1>.

Uso (dentro de um script de geração):

    import sys
    sys.path.insert(0, r"<caminho da skill>/scripts")
    from construtor_pagina import Pagina

    pagina = Pagina()
    pagina.p("O **Google Colab** roda Python no navegador, sem instalar nada.")
    pagina.h2("Ferramenta web")
    pagina.lista(["Crie uma conta Google;", "Acesse o Colab."], ordenada=True)
    pagina.codigo('''
    print("Olá, mundo!")
    # Olá, mundo!
    ''')
    pagina.salvar("course_content/pt_br/python-na-pratica/modulo/colab.html")

O texto passado para p(), h2(), lista(), tabela(), citacao() e quiz() aceita a
formatação inline do Markdown (**negrito**, *itálico*, `código`, [link](url)) e
é escapado automaticamente. O texto de codigo() é escapado, mas não interpretado:
escreva o Python exatamente como ele deve aparecer na tela.
"""

import html
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

# Dicts pequenos e conhecidos que o site espera ver em uma linha só.
LINGUAGENS = {"python", "text", "bash", "js", "javascript", "json", "sql", "html", "css"}


def inline(texto):
    """Escapa HTML e converte a formatação inline do Markdown."""
    texto = html.escape(str(texto), quote=False)

    # Guarda os trechos de `código` para que ** e * não sejam interpretados dentro deles.
    guardados = []

    def guardar(achado):
        guardados.append("<code>" + achado.group(1) + "</code>")
        return "\x00{}\x00".format(len(guardados) - 1)

    texto = re.sub(r"`([^`]+)`", guardar, texto)
    texto = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        texto,
    )
    texto = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", texto)

    for indice, guardado in enumerate(guardados):
        texto = texto.replace("\x00{}\x00".format(indice), guardado)
    return texto


def atributo(texto):
    """Escapa um texto que vai dentro de um atributo HTML."""
    return html.escape(str(texto), quote=True)


class Pagina:
    def __init__(self):
        self.blocos = []   # conteúdo de dentro de <div class="prose">
        self.extras = []   # blocos que vão DEPOIS da prosa (quiz)
        self.palavras = 0
        self.linhas_codigo = 0

    # ---------------------------------------------------------------- texto --
    def p(self, texto):
        """Um parágrafo."""
        self._contar(texto)
        self.blocos.append("<p>" + inline(texto) + "</p>")

    def h2(self, titulo):
        """Título de subseção. O tema usa <h1> para o título da aula e só estiliza <h2>,
        então toda subseção da aula (as '### N.M' do notebook) vira h2."""
        self._contar(titulo)
        self.blocos.append("<h2>" + inline(titulo) + "</h2>")

    def lista(self, itens, ordenada=False):
        """Uma lista <ul> (padrão) ou <ol> (ordenada=True)."""
        etiqueta = "ol" if ordenada else "ul"
        linhas = ["<" + etiqueta + ">"]
        for item in itens:
            self._contar(item)
            linhas.append("<li>" + inline(item) + "</li>")
        linhas.append("</" + etiqueta + ">")
        self.blocos.append("\n".join(linhas))

    def citacao(self, *paragrafos):
        """Um <blockquote> — o formato das dicas e avisos ('> 💡 **Dica:** ...' do notebook).
        O emoji do notebook não é usado aqui: no site o destaque é a barra lateral do bloco."""
        linhas = ["<blockquote>"]
        for paragrafo in paragrafos:
            self._contar(paragrafo)
            linhas.append("<p>" + inline(paragrafo) + "</p>")
        linhas.append("</blockquote>")
        self.blocos.append("\n".join(linhas))

    def tabela(self, cabecalho, linhas):
        """Uma tabela com <thead> e <tbody>, dentro de .table-wrap (rolagem no celular)."""
        titulos = []
        for celula in cabecalho:
            self._contar(celula)
            titulos.append("<th>" + inline(celula) + "</th>")

        corpo = []
        for linha in linhas:
            if len(linha) != len(cabecalho):
                raise ValueError(
                    "A linha {!r} tem {} colunas, mas o cabeçalho tem {}.".format(
                        linha, len(linha), len(cabecalho)
                    )
                )
            celulas = []
            for celula in linha:
                self._contar(celula)
                celulas.append("<td>" + inline(celula) + "</td>")
            corpo.append("<tr>" + "".join(celulas) + "</tr>")

        # thead e tbody em linhas próprias; uma <tr> por linha, como nas aulas já publicadas.
        self.blocos.append(
            '<div class="table-wrap"><table>\n'
            + "<thead><tr>" + "".join(titulos) + "</tr></thead>\n"
            + "<tbody>\n"
            + "\n".join(corpo)
            + "\n</tbody>\n</table></div>"
        )

    # --------------------------------------------------------------- código --
    def codigo(self, codigo, linguagem="python"):
        """Um bloco de código com botão de copiar.

        O site não tem realce de sintaxe nem playground de Python, então a saída
        dos `print()` entra como comentário no próprio código:

            print(idade)  # 30
        """
        if linguagem not in LINGUAGENS:
            raise ValueError(
                "Linguagem {!r} fora do conjunto usado no site: {}".format(
                    linguagem, ", ".join(sorted(LINGUAGENS))
                )
            )
        texto = codigo.strip("\n")
        self.linhas_codigo += len(texto.splitlines())
        self.blocos.append(
            '<div class="code-block">'
            '<button type="button" class="copy-btn" aria-label="Copiar código">copiar</button>'
            '<pre><code class="language-' + linguagem + '">'
            + html.escape(texto, quote=False)
            + "\n</code></pre></div>"
        )

    def bruto(self, trecho):
        """Escotilha de emergência: insere HTML já pronto na prosa, sem escapar."""
        self.blocos.append(trecho.strip("\n"))

    # ----------------------------------------------------------------- quiz --
    def quiz(self, nome, pergunta, alternativas):
        """Um quiz de múltipla escolha, que fica FORA da prosa, no fim da página.

        `nome` precisa ser único no site (use o id da aula, ex: "python-colab").
        `alternativas` é uma lista de tuplas (texto, explicação, correta=False):

            pagina.quiz("python-numeros", "Quanto é `7 // 2`?", [
                ("3.5", "3.5 é o resultado de 7 / 2.", False),
                ("3", "A divisão inteira descarta a parte decimal.", True),
            ])

        A explicação aparece depois da resposta, tanto para acerto quanto para erro,
        então escreva sempre o *porquê*, não só "certo"/"errado".
        """
        corretas = [item for item in alternativas if len(item) > 2 and item[2]]
        if len(corretas) != 1:
            raise ValueError(
                "O quiz {!r} tem {} alternativas corretas; precisa ter exatamente 1.".format(
                    nome, len(corretas)
                )
            )
        if len(alternativas) < 2:
            raise ValueError("O quiz {!r} precisa de pelo menos 2 alternativas.".format(nome))

        self._contar(pergunta)
        identificador = "quiz-" + nome
        linhas = [
            '<div class="quiz" role="group" aria-labelledby="' + identificador + '-q">',
            '  <p class="kicker-cyan">// Quiz</p>',
            '  <p class="quiz-q" id="' + identificador + '-q">' + inline(pergunta) + "</p>",
            '  <fieldset class="quiz-options">',
            '    <legend class="sr-only">Escolha uma alternativa</legend>',
        ]
        for indice, item in enumerate(alternativas):
            texto, explicacao = item[0], item[1]
            correta = "1" if (len(item) > 2 and item[2]) else "0"
            linhas.append(
                '    <label class="quiz-opt" data-correct="' + correta + '"'
                ' data-exp="' + atributo(explicacao) + '">'
                '<input type="radio" name="' + identificador + '" value="' + str(indice) + '" />'
                '<span class="txt">' + inline(texto) + "</span>"
                '<span class="mark" aria-hidden="true"></span></label>'
            )
        linhas.append("  </fieldset>")
        linhas.append('  <div class="quiz-feedback" aria-live="polite" hidden></div>')
        linhas.append("</div>")
        self.extras.append("\n".join(linhas))

    # ---------------------------------------------------------------- saída --
    def _contar(self, texto):
        self.palavras += len(re.findall(r"\S+", str(texto)))

    def tempo_de_leitura(self):
        """Sugestão de `readTime` para o lessons.json, em minutos.

        150 palavras/minuto (leitura técnica, mais lenta que texto corrido) mais
        um tempo por linha de código. É um chute informado: ajuste no manifesto
        se a aula for mais densa ou mais leve do que a conta sugere."""
        minutos = self.palavras / 150 + self.linhas_codigo / 30
        return max(1, round(minutos))

    def para_html(self):
        corpo = '<div class="prose">\n' + "\n".join(self.blocos) + "\n</div>\n"
        for extra in self.extras:
            corpo += "\n\n" + extra + "\n"
        return corpo

    def salvar(self, caminho):
        """Grava o fragmento em disco (UTF-8) e sugere o tempo de leitura.

        Se a página já existir, conserva o fim de linha dela (o projeto tem
        arquivos em CRLF e em LF), para o diff mostrar só o que mudou."""
        pasta = os.path.dirname(caminho)
        if pasta:
            os.makedirs(pasta, exist_ok=True)
        conteudo = self.para_html()
        fim_de_linha = "\n"
        if os.path.isfile(caminho):
            with open(caminho, encoding="utf-8", newline="") as arquivo:
                if "\r\n" in arquivo.read():
                    fim_de_linha = "\r\n"
        with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
            arquivo.write(conteudo.replace("\n", fim_de_linha))
        minutos = self.tempo_de_leitura()
        print(
            "{}: {} blocos, {} palavras, {} linhas de código "
            '-> readTime sugerido: "{} min de leitura"'.format(
                os.path.basename(caminho),
                len(self.blocos) + len(self.extras),
                self.palavras,
                self.linhas_codigo,
                minutos,
            )
        )
        return minutos
