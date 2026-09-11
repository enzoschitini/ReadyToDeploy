"""Construtor de notebooks .ipynb para os módulos do curso Ready To Deploy.

Uso (dentro de um script de geração):

    import sys
    sys.path.insert(0, r"<caminho da skill>/scripts")
    from construtor_notebook import Notebook

    nb = Notebook()
    nb.md(r'''
    # Módulo 02 - Estruturas de Dados
    ''')
    nb.code(r'''
    # Comentário curto
    print("olá")
    ''')
    nb.salvar("content_generation/jupyter_notebooks/module_02.ipynb")

Cada chamada de md()/code() vira UMA célula. Espaços/quebras de linha no
início e no fim do texto são removidos, então pode escrever o conteúdo
entre aspas triplas sem se preocupar com a primeira/última linha vazia.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")


class Notebook:
    def __init__(self):
        self.celulas = []

    def md(self, texto):
        """Adiciona uma célula de texto (Markdown)."""
        self.celulas.append(("markdown", texto.strip("\n")))

    def code(self, texto):
        """Adiciona uma célula de código Python."""
        self.celulas.append(("code", texto.strip("\n")))

    def separador(self):
        """Adiciona uma célula contendo apenas '---' (usada entre seções principais)."""
        self.md("---")

    def _para_dict(self):
        notebook = {
            "cells": [],
            "metadata": {
                "colab": {"provenance": []},
                "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                "language_info": {"name": "python"},
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        for indice, (tipo, texto) in enumerate(self.celulas):
            linhas = texto.split("\n")
            celula = {
                "cell_type": tipo,
                "id": f"cell-{indice:03d}",
                "metadata": {},
                "source": [linha + "\n" for linha in linhas[:-1]] + [linhas[-1]],
            }
            if tipo == "code":
                celula["execution_count"] = None
                celula["outputs"] = []
            notebook["cells"].append(celula)
        return notebook

    def salvar(self, caminho):
        """Grava o notebook em disco (UTF-8, sem saídas de execução)."""
        pasta = os.path.dirname(caminho)
        if pasta:
            os.makedirs(pasta, exist_ok=True)
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(self._para_dict(), arquivo, ensure_ascii=False, indent=1)
            arquivo.write("\n")
        print(f"{len(self.celulas)} células gravadas em {caminho}")
