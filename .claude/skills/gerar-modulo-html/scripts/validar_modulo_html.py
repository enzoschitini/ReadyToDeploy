"""Valida um módulo publicado no site do Ready To Deploy.

Uso:
    python validar_modulo_html.py <module_id> [--raiz .] [--lang pt_br]

Confere o cadastro e as páginas:

  1. O módulo existe em modules.json, tem aulas em lessons.json, `nodes` bate com
     o número de aulas, `order` é 1..N e os ids das aulas são únicos no arquivo;
  2. Todo `content` aponta para um arquivo que existe, na pasta
     `<bootcamp>/<module_id>/` do bootcamp que lista o módulo no currículo
     (o erro clássico: mover as pastas e esquecer do lessons.json);
  3. Nenhum .html da pasta do módulo ficou órfão (sem aula apontando para ele);
  4. Cada página é um *fragmento* (sem <html>/<body>/<h1>), começa pela prosa,
     tem as tags balanceadas, as tabelas dentro de .table-wrap e os blocos de
     código com o botão de copiar;
  5. Nenhum `<` ou `>` cru dentro de <code> — é o que faz sumir da tela coisas
     como `<class 'int'>` e `x <= y`, que precisam virar &lt; e &gt;;
  6. Os quizzes têm exatamente uma alternativa correta, explicação em todas, e
     `name`/`aria-labelledby` coerentes e sem repetição entre as aulas;
  7. O item do currículo do bootcamp não ficou `disabled`.

Sai com código 1 se houver ERROS; AVISOS não impedem a aprovação.
"""

import argparse
import json
import os
import re
import sys

# Tags de container usadas nas aulas (as vazias, como <input>, ficam de fora).
TAGS = ("div", "p", "h2", "ul", "ol", "li", "blockquote", "pre", "code",
        "table", "thead", "tbody", "tr", "th", "td", "fieldset", "legend", "label", "span")


def carregar_json(caminho, erros):
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        erros.append("não achei {}".format(caminho))
    except json.JSONDecodeError as falha:
        erros.append("{} não é um JSON válido: {}".format(os.path.basename(caminho), falha))
    return None


def validar_cadastro(pasta, module_id, erros, avisos):
    """Devolve (aulas, bootcamp_id) depois de conferir os três JSONs."""
    modules = carregar_json(os.path.join(pasta, "modules.json"), erros) or {}
    lessons = carregar_json(os.path.join(pasta, "lessons.json"), erros) or {}
    bootcamps = carregar_json(os.path.join(pasta, "bootcamps.json"), erros) or {}
    if erros:
        return [], None

    modulo = next((item for item in modules.get("modules", []) if item.get("id") == module_id), None)
    if modulo is None:
        erros.append("o módulo {!r} não está em modules.json".format(module_id))
        return [], None

    for chave in ("title", "description", "level", "nodes"):
        if not modulo.get(chave):
            erros.append("o módulo não tem o campo {!r} em modules.json".format(chave))

    todas = lessons.get("lessons", [])
    aulas = sorted([item for item in todas if item.get("module_id") == module_id],
                   key=lambda item: item.get("order", 0))
    if not aulas:
        erros.append("nenhuma aula com module_id {!r} em lessons.json "
                     "(a página do módulo mostraria 'não encontrado')".format(module_id))
        return [], None

    if modulo.get("nodes") != len(aulas):
        erros.append("modules.json diz nodes={} mas há {} aulas cadastradas".format(
            modulo.get("nodes"), len(aulas)))

    ordens = [aula.get("order") for aula in aulas]
    if ordens != list(range(1, len(aulas) + 1)):
        erros.append("os campos 'order' das aulas são {} (esperado 1..{})".format(ordens, len(aulas)))

    repetidos = {aula["id"] for aula in aulas if [item["id"] for item in todas].count(aula["id"]) > 1}
    if repetidos:
        erros.append("ids de aula repetidos em lessons.json: " + ", ".join(sorted(repetidos)))

    for aula in aulas:
        if not aula.get("title"):
            erros.append("a aula {!r} não tem título".format(aula.get("id")))
        if not aula.get("readTime"):
            avisos.append("a aula {!r} não tem readTime".format(aula.get("id")))

    # --- de qual bootcamp é este módulo? ----------------------------------
    bootcamp_id = None
    for bootcamp in bootcamps.get("bootcamps", []):
        curriculo = bootcamp.get("detail", {}).get("curriculum", [])
        item = next((linha for linha in curriculo if linha.get("id") == module_id), None)
        if item is not None:
            bootcamp_id = bootcamp["id"]
            if item.get("disabled"):
                erros.append(
                    "o item do currículo de {!r} ainda está com \"disabled\": true, "
                    "então o card do módulo não é clicável".format(bootcamp_id))
            break
    if bootcamp_id is None:
        avisos.append("nenhum bootcamp lista {!r} no currículo; o módulo só aparece "
                      "na página de módulos".format(module_id))
    elif modulo.get("bootcamp_id") and modulo["bootcamp_id"] != bootcamp_id:
        avisos.append("modules.json diz bootcamp_id={!r}, mas quem lista o módulo é {!r} "
                      "(campo não é lido pelo site, só metadado)".format(
                          modulo["bootcamp_id"], bootcamp_id))
    return aulas, bootcamp_id


def validar_caminhos(pasta, module_id, bootcamp_id, aulas, erros, avisos):
    """Confere se cada `content` resolve em disco e mora na pasta certa."""
    esperada = "{}/{}/".format(bootcamp_id, module_id) if bootcamp_id else None
    paginas = []
    for aula in aulas:
        conteudo = aula.get("content", "")
        if not conteudo:
            erros.append("a aula {!r} não tem o campo 'content'".format(aula.get("id")))
            continue
        caminho = os.path.join(pasta, *conteudo.split("/"))
        if not os.path.isfile(caminho):
            erros.append("a aula {!r} aponta para '{}', que não existe em disco".format(
                aula["id"], conteudo))
            continue
        if esperada and not conteudo.startswith(esperada):
            avisos.append("a aula {!r} está em '{}', fora da pasta esperada '{}'".format(
                aula["id"], conteudo, esperada))
        paginas.append((aula, caminho))

    if esperada:
        pasta_modulo = os.path.join(pasta, bootcamp_id, module_id)
        if os.path.isdir(pasta_modulo):
            usados = {os.path.basename(aula["content"]) for aula in aulas if aula.get("content")}
            for arquivo in sorted(os.listdir(pasta_modulo)):
                if arquivo.endswith(".html") and arquivo not in usados:
                    avisos.append("'{}' está na pasta do módulo mas nenhuma aula aponta "
                                  "para ele".format(arquivo))
    return paginas


def validar_pagina(identificador, html, erros, avisos, nomes_de_quiz):
    def erro(mensagem):
        erros.append("{}: {}".format(identificador, mensagem))

    def aviso(mensagem):
        avisos.append("{}: {}".format(identificador, mensagem))

    # --- é um fragmento, não uma página inteira ---------------------------
    for proibida in ("<html", "<head", "<body", "<h1", "<!doctype"):
        if proibida in html.lower():
            erro("tem '{}'; a aula é um fragmento, o esqueleto vem de pages/module.html".format(
                proibida))
    if not html.lstrip().startswith('<div class="prose">'):
        erro('deveria começar com <div class="prose">')
    if "<h3" in html:
        aviso("usa <h3>, que o tema não estiliza; use <h2> para as subseções")

    # --- tags balanceadas --------------------------------------------------
    for tag in TAGS:
        abre = len(re.findall(r"<{}(?=[ >])".format(tag), html))
        fecha = html.count("</{}>".format(tag))
        if abre != fecha:
            erro("<{}> aberta {}x e fechada {}x".format(tag, abre, fecha))

    # --- código escapado ---------------------------------------------------
    # Um '>' cru é texto literal em HTML (a seta de `# int -> float` renderiza bem).
    # Já um '<' seguido de letra, '/', '!' ou '?' vira abertura de tag: o trecho
    # some da tela sem erro nenhum — é o caso de `<class 'int'>` e `<div>`.
    for trecho in re.findall(r"<code[^>]*>(.*?)</code>", html, flags=re.S):
        engolidos = re.findall(r"<[A-Za-z/!?][^\s]*", trecho)
        if engolidos:
            erro("{} vira tag HTML dentro de <code> e some da tela; escape com &lt;".format(
                ", ".join(repr(achado) for achado in engolidos[:3])))
            break
        if "<" in trecho:
            aviso("há '<' cru dentro de <code>; renderiza, mas o certo é &lt;")
            break

    for bloco in re.findall(r'<div class="code-block">.*?</div>', html, flags=re.S):
        if "copy-btn" not in bloco:
            erro("um .code-block está sem o botão de copiar")
            break

    # --- tabelas -----------------------------------------------------------
    for posicao in (achado.start() for achado in re.finditer(r"<table", html)):
        if 'class="table-wrap"' not in html[max(0, posicao - 60):posicao]:
            aviso("há <table> fora de .table-wrap (sem rolagem horizontal no celular)")
            break

    # --- quizzes -----------------------------------------------------------
    for quiz in re.findall(r'<div class="quiz".*?\n</div>', html, flags=re.S):
        rotulo = re.search(r'aria-labelledby="([^"]+)"', quiz)
        pergunta = re.search(r'class="quiz-q" id="([^"]+)"', quiz)
        if not rotulo or not pergunta:
            erro("um quiz está sem aria-labelledby ou sem a pergunta .quiz-q")
        elif rotulo.group(1) != pergunta.group(1):
            erro("no quiz, aria-labelledby={!r} não bate com o id da pergunta {!r}".format(
                rotulo.group(1), pergunta.group(1)))

        alternativas = re.findall(r'<label class="quiz-opt"([^>]*)>', quiz)
        corretas = sum(1 for atributos in alternativas if 'data-correct="1"' in atributos)
        if len(alternativas) < 2:
            erro("um quiz tem menos de 2 alternativas")
        if corretas != 1:
            erro("um quiz tem {} alternativas corretas (precisa ser exatamente 1)".format(corretas))
        if any("data-exp=" not in atributos for atributos in alternativas):
            aviso("há alternativa de quiz sem data-exp (o aluno não vê o porquê)")

        nome = re.search(r'name="([^"]+)"', quiz)
        if nome:
            if nome.group(1) in nomes_de_quiz:
                erro("o quiz usa name={!r}, já usado em {}".format(
                    nome.group(1), nomes_de_quiz[nome.group(1)]))
            else:
                nomes_de_quiz[nome.group(1)] = identificador

    # --- playground só roda JavaScript -------------------------------------
    if "checkpoint" in html and "language-python" in html:
        aviso("tem .checkpoint numa aula de Python; o playground do site executa "
              "JavaScript, então o código do aluno daria erro")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    analisador = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analisador.add_argument("module_id")
    analisador.add_argument("--raiz", default=".", help="raiz do repositório (padrão: .)")
    analisador.add_argument("--lang", default="pt_br")
    argumentos = analisador.parse_args()

    pasta = os.path.join(argumentos.raiz, "course_content", argumentos.lang)
    erros, avisos = [], []

    aulas, bootcamp_id = validar_cadastro(pasta, argumentos.module_id, erros, avisos)
    paginas = validar_caminhos(pasta, argumentos.module_id, bootcamp_id, aulas, erros, avisos) \
        if aulas else []

    nomes_de_quiz = {}
    for aula, caminho in paginas:
        with open(caminho, encoding="utf-8") as arquivo:
            validar_pagina(aula["id"], arquivo.read(), erros, avisos, nomes_de_quiz)

    print("módulo {} — {} aulas, {} páginas lidas{}".format(
        argumentos.module_id, len(aulas), len(paginas),
        ", bootcamp: " + bootcamp_id if bootcamp_id else ""))
    for aviso in avisos:
        print("AVISO: " + aviso)
    for erro in erros:
        print("ERRO: " + erro)
    print("RESULTADO:", "REPROVADO" if erros else "APROVADO")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
