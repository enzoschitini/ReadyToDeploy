"""Cadastra um módulo e suas aulas nos JSONs de course_content/<lang>/.

Uso:
    python registrar_modulo.py manifesto.json [--raiz .] [--lang pt_br]

O manifesto descreve o módulo; o script cuida do resto:

  * `modules.json`  — cria ou atualiza a entrada do módulo (`nodes` = nº de aulas);
  * `lessons.json`  — troca TODAS as aulas daquele `module_id` pelas do manifesto,
                      montando o campo `content` como `<bootcamp>/<módulo>/<arquivo>`
                      (é assim que `pages/module.html` acha o HTML da aula);
  * `bootcamps.json`— tira o `"disabled": true` do item do currículo, para o módulo
                      virar um card clicável na página do bootcamp.

Rodar de novo com o mesmo manifesto é seguro: o módulo e as aulas são substituídos,
não duplicados. As entradas que o manifesto não menciona não são reformatadas — o
script mexe no texto do arquivo, não regrava o JSON inteiro.

Formato do manifesto:

    {
      "bootcamp_id": "python-na-pratica",
      "module_id": "python-variaveis-e-tipos-de-dados",
      "title": "Módulo 1 — Variáveis e Tipos de Dados",
      "description": "Frase que aparece no card do módulo.",
      "level": "Iniciante",
      "skills": ["python", "variaveis"],
      "hot": false,
      "lessons": [
        {
          "id": "python-colab",
          "title": "Introdução ao Google Colab",
          "navTitle": "Google Colab",
          "badge": "essencial",
          "readTime": "3 min de leitura",
          "arquivo": "colab.html",
          "resources": [
            {"name": "Google Colaboratory", "href": "https://colab.research.google.com/",
             "tags": [{"label": "Doc", "free": false}, {"label": "Grátis", "free": true}]}
          ]
        }
      ]
    }

`navTitle`, `badge`, `readTime` e `resources` são opcionais.
"""

import argparse
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

INDENTACAO_ELEMENTO = "    "        # os itens dos arrays ficam a 4 espaços nesses arquivos
CHAVES_INLINE = {"rating"}          # dicts pequenos que o projeto escreve em uma linha só
CAMPOS_AULA = ("id", "module_id", "order", "title", "navTitle", "badge", "readTime",
               "content", "resources")


# ----------------------------------------------------------------- JSON ------
def formatar(valor, base=INDENTACAO_ELEMENTO, chave=None):
    """Serializa no estilo dos arquivos do projeto: 2 espaços por nível,
    listas de escalares e `rating` em uma linha só."""
    if isinstance(valor, dict) and valor and chave not in CHAVES_INLINE:
        interno = base + "  "
        linhas = [
            interno + json.dumps(nome, ensure_ascii=False) + ": " + formatar(item, interno, nome)
            for nome, item in valor.items()
        ]
        return "{\n" + ",\n".join(linhas) + "\n" + base + "}"
    if isinstance(valor, list) and any(isinstance(item, (dict, list)) for item in valor):
        interno = base + "  "
        itens = [interno + formatar(item, interno) for item in valor]
        return "[\n" + ",\n".join(itens) + "\n" + base + "]"
    return json.dumps(valor, ensure_ascii=False)


def localizar_array(texto, chave, desde=0):
    """Índice do '[' do array de nome `chave` a partir de `desde` (-1 se não houver).

    O arquivo pode ter vários arrays com o mesmo nome (cada bootcamp tem o seu
    "curriculum"), por isso a busca é retomável."""
    marca = json.dumps(chave, ensure_ascii=False)
    posicao = texto.find(marca, desde)
    while posicao != -1:
        cursor = texto.find(":", posicao + len(marca))
        if cursor != -1:
            cursor += 1
            while cursor < len(texto) and texto[cursor] in " \t\r\n":
                cursor += 1
            if cursor < len(texto) and texto[cursor] == "[":
                return cursor
        posicao = texto.find(marca, posicao + 1)
    return -1


def elementos_do_array(texto, inicio):
    """[(ini, fim)] de cada elemento do array que começa em `inicio`, e o índice do ']'."""
    decodificador = json.JSONDecoder()
    elementos = []
    cursor = inicio + 1
    while True:
        while cursor < len(texto) and texto[cursor] in " \t\r\n,":
            cursor += 1
        if texto[cursor] == "]":
            return elementos, cursor
        _, fim = decodificador.raw_decode(texto, cursor)
        elementos.append((cursor, fim))
        cursor = fim


def reescrever_array(texto, chave, descartar, novos):
    """Reescreve o array `chave`: tira quem `descartar(valor)` aprovar e põe `novos` no fim.

    Os elementos mantidos conservam o texto original (e, portanto, a formatação
    que o autor escreveu à mão)."""
    inicio = localizar_array(texto, chave)
    if inicio == -1:
        raise ValueError("Não achei o array {!r} no arquivo.".format(chave))
    elementos, fim = elementos_do_array(texto, inicio)

    mantidos = [texto[ini:termino] for ini, termino in elementos
                if not descartar(json.loads(texto[ini:termino]))]
    partes = mantidos + [formatar(novo) for novo in novos]

    inicio_linha = texto.rfind("\n", 0, fim) + 1
    fechamento = texto[inicio_linha:fim] if texto[inicio_linha:fim].strip() == "" else "  "
    corpo = (",\n" + INDENTACAO_ELEMENTO).join(partes)
    return texto[:inicio] + "[\n" + INDENTACAO_ELEMENTO + corpo + "\n" + fechamento + texto[fim:]


def ler(caminho):
    """Devolve (texto com \\n, fim de linha original).

    Os arquivos do projeto estão misturados (uns em CRLF, outros em LF) e
    regravar tudo em um só formato faria o diff acusar o arquivo inteiro,
    escondendo a mudança de verdade."""
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        texto = arquivo.read()
    return texto.replace("\r\n", "\n"), ("\r\n" if "\r\n" in texto else "\n")


def gravar(caminho, texto, fim_de_linha):
    json.loads(texto)  # rede de segurança: nunca deixa um JSON quebrado em disco
    with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
        arquivo.write(texto.replace("\n", fim_de_linha))


# ------------------------------------------------------------ manifesto ------
def conferir_manifesto(manifesto, pasta_conteudo, avisos):
    faltando = [chave for chave in ("bootcamp_id", "module_id", "title", "description", "lessons")
                if not manifesto.get(chave)]
    if faltando:
        raise SystemExit("ERRO: manifesto sem as chaves obrigatórias: " + ", ".join(faltando))

    identificadores = [aula.get("id") for aula in manifesto["lessons"]]
    if len(set(identificadores)) != len(identificadores):
        raise SystemExit("ERRO: há ids de aula repetidos no manifesto.")

    for aula in manifesto["lessons"]:
        for chave in ("id", "title", "arquivo"):
            if not aula.get(chave):
                raise SystemExit("ERRO: aula {!r} sem a chave {!r}.".format(aula.get("id"), chave))
        caminho = os.path.join(pasta_conteudo, manifesto["bootcamp_id"],
                               manifesto["module_id"], aula["arquivo"])
        if not os.path.isfile(caminho):
            raise SystemExit(
                "ERRO: a aula {!r} aponta para {}, que não existe. "
                "Gere as páginas antes de cadastrar.".format(aula["id"], caminho)
            )
        if not aula.get("readTime"):
            avisos.append("aula {!r} sem readTime".format(aula["id"]))


def montar_modulo(manifesto):
    modulo = {
        "id": manifesto["module_id"],
        "bootcamp_id": manifesto["bootcamp_id"],
        "title": manifesto["title"],
        "description": manifesto["description"],
        "level": manifesto.get("level", "Iniciante"),
        "nodes": len(manifesto["lessons"]),
        "skills": manifesto.get("skills", []),
        "hot": bool(manifesto.get("hot", False)),
    }
    if manifesto.get("rating"):
        modulo["rating"] = manifesto["rating"]
    return modulo


def montar_aulas(manifesto):
    aulas = []
    for ordem, dados in enumerate(manifesto["lessons"], start=1):
        aula = {
            "id": dados["id"],
            "module_id": manifesto["module_id"],
            "order": ordem,
            "title": dados["title"],
            "navTitle": dados.get("navTitle", dados["title"]),
            "badge": dados.get("badge", "essencial"),
            "readTime": dados.get("readTime", "1 min de leitura"),
            "content": "{}/{}/{}".format(manifesto["bootcamp_id"], manifesto["module_id"],
                                         dados["arquivo"]),
        }
        if dados.get("resources"):
            aula["resources"] = dados["resources"]
        aulas.append({chave: aula[chave] for chave in CAMPOS_AULA if chave in aula})
    return aulas


# -------------------------------------------------------------- currículo ----
def habilitar_curriculo(texto, bootcamp_id, module_id, avisos):
    """Tira o `"disabled": true` do item do currículo do bootcamp."""
    dados = json.loads(texto)
    bootcamp = next((item for item in dados["bootcamps"] if item["id"] == bootcamp_id), None)
    if bootcamp is None:
        avisos.append("bootcamp {!r} não existe em bootcamps.json".format(bootcamp_id))
        return texto, False

    curriculo = bootcamp.get("detail", {}).get("curriculum", [])
    item = next((linha for linha in curriculo if linha.get("id") == module_id), None)
    if item is None:
        avisos.append(
            "o currículo do bootcamp {!r} não tem um item com id {!r}; "
            "acrescente-o à mão em bootcamps.json para o módulo aparecer na trilha".format(
                bootcamp_id, module_id)
        )
        return texto, False
    if not item.get("disabled"):
        return texto, False

    # Remove a chave no texto (em vez de regravar o item) para não mexer no
    # estilo de uma linha por item do currículo.
    inicio = localizar_array(texto, "curriculum")
    while inicio != -1:
        elementos, fim_array = elementos_do_array(texto, inicio)
        for ini, fim in elementos:
            valor = json.loads(texto[ini:fim])
            if valor.get("id") == module_id and valor.get("disabled"):
                trecho = texto[ini:fim]
                limpo = re.sub(r',\s*"disabled"\s*:\s*true', "", trecho)
                limpo = re.sub(r'"disabled"\s*:\s*true\s*,\s*', "", limpo)
                return texto[:ini] + limpo + texto[fim:], True
        inicio = localizar_array(texto, "curriculum", fim_array)
    return texto, False


# ------------------------------------------------------------------ main -----
def main():
    analisador = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analisador.add_argument("manifesto")
    analisador.add_argument("--raiz", default=".", help="raiz do repositório (padrão: .)")
    analisador.add_argument("--lang", default="pt_br", help="idioma do course_content (padrão: pt_br)")
    argumentos = analisador.parse_args()

    pasta_conteudo = os.path.join(argumentos.raiz, "course_content", argumentos.lang)
    if not os.path.isdir(pasta_conteudo):
        raise SystemExit("ERRO: não achei a pasta {}.".format(pasta_conteudo))

    with open(argumentos.manifesto, encoding="utf-8") as arquivo:
        manifesto = json.load(arquivo)

    avisos = []
    conferir_manifesto(manifesto, pasta_conteudo, avisos)
    module_id = manifesto["module_id"]

    # --- modules.json ------------------------------------------------------
    caminho = os.path.join(pasta_conteudo, "modules.json")
    texto, fim_de_linha = ler(caminho)
    ja_existia = any(item["id"] == module_id for item in json.loads(texto)["modules"])
    texto = reescrever_array(texto, "modules",
                             lambda item: item.get("id") == module_id,
                             [montar_modulo(manifesto)])
    gravar(caminho, texto, fim_de_linha)
    print("modules.json: módulo {!r} {}".format(module_id, "atualizado" if ja_existia else "criado"))

    # --- lessons.json ------------------------------------------------------
    caminho = os.path.join(pasta_conteudo, "lessons.json")
    texto, fim_de_linha = ler(caminho)
    anteriores = sum(1 for item in json.loads(texto)["lessons"] if item.get("module_id") == module_id)
    aulas = montar_aulas(manifesto)
    texto = reescrever_array(texto, "lessons",
                             lambda item: item.get("module_id") == module_id,
                             aulas)
    gravar(caminho, texto, fim_de_linha)
    print("lessons.json: {} aulas cadastradas{}".format(
        len(aulas), " (substituíram {})".format(anteriores) if anteriores else ""))
    for aula in aulas:
        print("  {}. {:22} -> {}".format(aula["order"], aula["id"], aula["content"]))

    # --- bootcamps.json ----------------------------------------------------
    caminho = os.path.join(pasta_conteudo, "bootcamps.json")
    texto, fim_de_linha = ler(caminho)
    texto, mudou = habilitar_curriculo(texto, manifesto["bootcamp_id"], module_id, avisos)
    if mudou:
        gravar(caminho, texto, fim_de_linha)
        print("bootcamps.json: item do currículo habilitado (disabled removido)")

    for aviso in avisos:
        print("AVISO: " + aviso)
    print("Agora rode o validador: validar_modulo_html.py " + module_id)


if __name__ == "__main__":
    main()
