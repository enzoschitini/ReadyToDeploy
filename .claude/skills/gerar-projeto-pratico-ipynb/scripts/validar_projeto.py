"""Valida um projeto prático .ipynb do curso Ready To Deploy.

Uso:
    python validar_projeto.py caminho/do/module_NN_projeto_pratico.ipynb

Verifica:
  1. Cabeçalho '# 🚀 Projeto Prático — Módulo NN: Título' com as linhas de curso e autor;
  2. Seções fixas presentes e na ordem: contexto, objetivo, requisitos, como funciona,
     missões, desafios extras e checklist;
  3. Missões numeradas 1..N, batendo com a tabela de "Como o projeto funciona";
  4. Cada missão tem mensagem 💬, célula de código com '# TODO', '🔎' e '💡 **Dica:**';
  5. Desafios extras numerados 1..N, cada um com a sua célula de código;
  6. Checklist com itens '- [ ]';
  7. 'R$' sem escape, células sem saídas salvas e execução de TODAS as células
     como o aluno as recebe (reaproveitado de gerar-modulo-ipynb/validar_notebook.py).

A conferência do "Resultado esperado" contra as soluções é feita pelo construtor,
no momento do salvar(), porque as soluções não ficam dentro do notebook.

Sai com código 1 se houver ERROS; AVISOS não impedem a aprovação.
"""

import os
import re
import sys

_PASTA_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gerar-modulo-ipynb", "scripts")
sys.path.insert(0, os.path.normpath(_PASTA_BASE))
from validar_notebook import carregar, remover_codigo_inline, validar_codigo  # noqa: E402

SECOES_FIXAS_INICIO = [
    ("O contexto", r"^## 📖 O contexto"),
    ("Objetivo", r"^## 🎯 Objetivo"),
    ("Requisitos", r"^## 🧰 Requisitos"),
    ("Como o projeto funciona", r"^## 🗺️ Como o projeto funciona"),
]
RE_MISSAO = r"^## (\d+)\S*\s+Missão"
RE_EXTRAS = r"^## 🌟 Desafios extras"
RE_EXTRA = r"^### \S+\s+Extra (\d+) — \S"
RE_CHECKLIST = r"^## ✅ Checklist de autoavaliação"


def primeira_linha_que_casa(texto, padrao):
    return next((linha for linha in texto.splitlines() if re.match(padrao, linha)), None)


def validar_estrutura(celulas, erros, avisos):
    markdowns = [(i, texto) for i, (tipo, texto, _) in enumerate(celulas) if tipo == "markdown"]
    if not markdowns:
        erros.append("O notebook não tem células de texto.")
        return

    # --- Cabeçalho ---------------------------------------------------------
    _, cabecalho = markdowns[0]
    if not re.match(r"^# 🚀 Projeto Prático — Módulo \d{2,}: \S", cabecalho):
        erros.append("A primeira célula deve começar com '# 🚀 Projeto Prático — Módulo NN: Título'.")
    for trecho in ("Curso: Ready To Deploy", "Criado por: [Enzo Schitini]"):
        if trecho not in cabecalho:
            erros.append(f"Cabeçalho sem a linha '{trecho}'.")

    # --- Posição de cada marco do roteiro ---------------------------------
    def posicao(padrao):
        return next((i for i, texto in markdowns if primeira_linha_que_casa(texto, padrao)), None)

    marcos = []
    for nome, padrao in SECOES_FIXAS_INICIO:
        indice = posicao(padrao)
        if indice is None:
            erros.append(f"Seção obrigatória ausente: '{nome}'.")
        marcos.append((nome, indice))

    missoes = []  # (número, índice da célula)
    for i, texto in markdowns:
        for linha in texto.splitlines():
            achado = re.match(RE_MISSAO, linha)
            if achado:
                missoes.append((int(achado.group(1)), i))
    numeros_missoes = [numero for numero, _ in missoes]
    if not missoes:
        erros.append("Nenhuma missão encontrada ('## 1️⃣ Missão 1 — ...').")
    elif numeros_missoes != list(range(1, len(missoes) + 1)):
        erros.append(f"Missões fora de ordem ou com lacunas: {numeros_missoes}.")
    elif not 3 <= len(missoes) <= 6:
        avisos.append(f"{len(missoes)} missões; o padrão é entre 3 e 6.")
    marcos += [(f"Missão {numero}", indice) for numero, indice in missoes]

    indice_extras = posicao(RE_EXTRAS)
    indice_checklist = posicao(RE_CHECKLIST)
    if indice_extras is None:
        erros.append("Seção obrigatória ausente: 'Desafios extras'.")
    if indice_checklist is None:
        erros.append("Seção obrigatória ausente: 'Checklist de autoavaliação'.")
    marcos += [("Desafios extras", indice_extras), ("Checklist", indice_checklist)]

    presentes = [(nome, indice) for nome, indice in marcos if indice is not None]
    for (nome_a, a), (nome_b, b) in zip(presentes, presentes[1:]):
        if a >= b:
            erros.append(f"Ordem das seções: '{nome_a}' deveria vir antes de '{nome_b}'.")

    # --- Tabela de missões em "Como o projeto funciona" --------------------
    indice_como = dict(marcos).get("Como o projeto funciona")
    if indice_como is not None:
        texto_como = celulas[indice_como][1]
        linhas_tabela = [int(m.group(1)) for m in (re.match(r"^\|\s*(\d+)\S*\s*\|", l) for l in texto_como.splitlines()) if m]
        if linhas_tabela != numeros_missoes:
            erros.append(f"Tabela de 'Como o projeto funciona' {linhas_tabela} não bate com as missões {numeros_missoes}.")

    # --- Conteúdo de cada missão --------------------------------------------
    limites = [indice for _, indice in missoes] + [indice_extras if indice_extras is not None else len(celulas)]
    for (numero, inicio), fim in zip(missoes, limites[1:]):
        trecho = celulas[inicio:fim]
        textos_md = [texto for tipo, texto, _ in trecho if tipo == "markdown"]
        codigos = [texto for tipo, texto, _ in trecho if tipo == "code"]
        if not any("> 💬 **" in t for t in textos_md):
            erros.append(f"Missão {numero}: falta a mensagem do personagem ('> 💬 **Nome (Cargo):** ...').")
        if not any("# TODO" in c for c in codigos):
            erros.append(f"Missão {numero}: falta uma célula de código com '# TODO'.")
        if not any("🔎" in t for t in textos_md):
            erros.append(f"Missão {numero}: falta o bloco '🔎 Resultado esperado' (ou 'Exemplo de resultado').")
        if not any("> 💡 **Dica:**" in t for t in textos_md):
            erros.append(f"Missão {numero}: falta a '> 💡 **Dica:**'.")

    # --- Desafios extras -----------------------------------------------------
    if indice_extras is not None:
        fim_extras = indice_checklist if indice_checklist is not None else len(celulas)
        extras = []
        for i in range(indice_extras, fim_extras):
            tipo, texto, _ = celulas[i]
            if tipo == "markdown":
                for linha in texto.splitlines():
                    achado = re.match(RE_EXTRA, linha)
                    if achado:
                        extras.append((int(achado.group(1)), i))
        numeros_extras = [numero for numero, _ in extras]
        if not extras:
            erros.append("Nenhum desafio extra encontrado ('### 🎟️ Extra 1 — ...').")
        elif numeros_extras != list(range(1, len(extras) + 1)):
            erros.append(f"Desafios extras fora de ordem ou com lacunas: {numeros_extras}.")
        elif not 3 <= len(extras) <= 5:
            avisos.append(f"{len(extras)} desafios extras; o padrão é entre 3 e 5.")
        limites_extras = [indice for _, indice in extras] + [fim_extras]
        for (numero, inicio), fim in zip(extras, limites_extras[1:]):
            if not any(tipo == "code" for tipo, _, _ in celulas[inicio:fim]):
                erros.append(f"Extra {numero}: falta a célula de código para o aluno.")

    # --- Checklist -----------------------------------------------------------
    if indice_checklist is not None and "- [ ]" not in celulas[indice_checklist][1]:
        erros.append("O checklist de autoavaliação não tem itens '- [ ]'.")

    # --- Cifrões soltos --------------------------------------------------------
    for indice, texto in markdowns:
        if re.search(r"(?<!\\)R\$", remover_codigo_inline(texto)):
            avisos.append(f"Célula {indice}: 'R$' sem escape em Markdown; use 'R\\$'.")


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
