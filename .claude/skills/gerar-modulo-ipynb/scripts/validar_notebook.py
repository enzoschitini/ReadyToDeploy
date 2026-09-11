"""Valida um módulo .ipynb gerado para o curso Ready To Deploy.

Uso:
    python validar_notebook.py caminho/do/module_XX.ipynb

Verifica:
  1. Estrutura do cabeçalho (título, curso, autor) e da tabela de Tópicos;
  2. Numeração das seções (## N.) e subseções (### N.M) coerente com a tabela;
  3. Células de código sem saídas salvas;
  4. Cifrões soltos em Markdown (ex: "R$" sem escape, que o Jupyter/Colab
     interpreta como fórmula LaTeX);
  5. Executa TODAS as células de código em sequência (em um subprocesso)
     e aponta a primeira célula que gerar erro.

Sai com código 1 se houver ERROS; AVISOS não impedem a aprovação.
"""

import json
import os
import re
import subprocess
import sys
import tempfile


def carregar(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        notebook = json.load(arquivo)
    celulas = []
    for celula in notebook["cells"]:
        fonte = celula["source"]
        texto = "".join(fonte) if isinstance(fonte, list) else fonte
        celulas.append((celula["cell_type"], texto, celula))
    return celulas


def remover_codigo_inline(texto):
    # Ignora blocos ``` e trechos `inline`, onde "$" é literal
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", texto)


def validar_estrutura(celulas, erros, avisos):
    markdowns = [(i, texto) for i, (tipo, texto, _) in enumerate(celulas) if tipo == "markdown"]
    if not markdowns:
        erros.append("O notebook não tem células de texto.")
        return

    # --- Cabeçalho ---------------------------------------------------------
    _, cabecalho = markdowns[0]
    if not re.match(r"^# Módulo \d{2,} - \S", cabecalho):
        erros.append("A primeira célula deve começar com '# Módulo NN - Tema'.")
    for trecho in ("#### Curso: Ready To Deploy", "#### Criado por: Enzo Schitini"):
        if trecho not in cabecalho:
            erros.append(f"Cabeçalho sem a linha '{trecho}'.")
    if cabecalho.count("---") < 2:
        avisos.append("Cabeçalho deveria ter as duas linhas '---' do modelo.")

    # --- Tabela de tópicos ------------------------------------------------
    topicos = []
    celula_topicos = next((t for _, t in markdowns if t.lstrip().startswith("## Tópicos")), None)
    if celula_topicos is None:
        erros.append("Não há célula começando com '## Tópicos'.")
    else:
        for linha in celula_topicos.splitlines():
            achado = re.match(r"^\|\s*(\d+)\.\s*(.+?)\s*\|", linha)
            if achado:
                topicos.append(int(achado.group(1)))
        if not topicos:
            erros.append("A célula de Tópicos não contém a tabela '| N. Tópico | Descrição |'.")

    # --- Seções e subseções ------------------------------------------------
    secoes = []
    secao_atual = None
    for indice, texto in markdowns:
        for linha in texto.splitlines():
            secao = re.match(r"^## (\d+)\. \S", linha)
            subsecao = re.match(r"^### (\d+)\.(\d+) \S", linha)
            if secao:
                secao_atual = int(secao.group(1))
                secoes.append(secao_atual)
            elif subsecao:
                numero = int(subsecao.group(1))
                if numero != secao_atual:
                    erros.append(f"Célula {indice}: subseção '{linha.strip()}' fora da seção {secao_atual}.")
            elif re.match(r"^###? \*\*", linha):
                avisos.append(f"Célula {indice}: título em negrito ('{linha.strip()}'); o padrão é sem negrito.")

    if secoes != list(range(1, len(secoes) + 1)):
        erros.append(f"Seções principais fora de ordem ou com lacunas: {secoes}.")
    if topicos and secoes and topicos != secoes:
        erros.append(f"Tabela de Tópicos {topicos} não bate com as seções do notebook {secoes}.")

    # --- Cifrões soltos ---------------------------------------------------
    for indice, texto in markdowns:
        sem_codigo = remover_codigo_inline(texto)
        if re.search(r"(?<!\\)R\$", sem_codigo):
            avisos.append(f"Célula {indice}: 'R$' sem escape em Markdown; use 'R\\$'.")


def validar_codigo(celulas, erros, avisos):
    codigos = [(i, texto, c) for i, (tipo, texto, c) in enumerate(celulas) if tipo == "code"]
    if not codigos:
        avisos.append("O notebook não tem células de código.")
        return

    for indice, _, celula in codigos:
        if celula.get("outputs"):
            avisos.append(f"Célula {indice}: contém saídas salvas; o padrão é entregar sem saídas.")

    # Monta um script que executa célula por célula e informa qual falhou
    partes = ["import traceback, sys", "_ns = {'__name__': '__main__'}"]
    for indice, texto, _ in codigos:
        if any(linha.lstrip().startswith(("!", "%")) for linha in texto.splitlines()):
            avisos.append(f"Célula {indice}: comando mágico/shell (! ou %) não foi executado na validação.")
            continue
        partes.append(
            "try:\n"
            f"    exec(compile({texto!r}, 'celula_{indice}', 'exec'), _ns)\n"
            "except Exception:\n"
            f"    print('\\n### ERRO NA CÉLULA {indice} ###', file=sys.stderr)\n"
            "    traceback.print_exc()\n"
            "    sys.exit(1)"
        )

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as script:
        script.write("\n".join(partes))
        caminho_script = script.name

    ambiente = dict(os.environ, PYTHONIOENCODING="utf-8", MPLBACKEND="Agg")
    try:
        resultado = subprocess.run(
            [sys.executable, caminho_script],
            capture_output=True, text=True, encoding="utf-8",
            stdin=subprocess.DEVNULL, timeout=300, env=ambiente,
        )
    except subprocess.TimeoutExpired:
        erros.append("A execução das células passou de 300s (loop infinito ou input()?).")
        return
    finally:
        os.remove(caminho_script)

    if resultado.returncode != 0:
        erros.append("Falha ao executar as células de código:\n" + resultado.stderr.strip()[-3000:])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)

    celulas = carregar(sys.argv[1])
    erros, avisos = [], []
    validar_estrutura(celulas, erros, avisos)
    validar_codigo(celulas, erros, avisos)

    total_codigo = sum(1 for tipo, _, _ in celulas if tipo == "code")
    print(f"{len(celulas)} células ({total_codigo} de código, {len(celulas) - total_codigo} de texto)")
    for aviso in avisos:
        print(f"AVISO: {aviso}")
    for erro in erros:
        print(f"ERRO: {erro}")
    print("RESULTADO:", "REPROVADO" if erros else "APROVADO")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
