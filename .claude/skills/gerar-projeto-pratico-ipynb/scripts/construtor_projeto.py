"""Construtor de projetos práticos .ipynb do curso Ready To Deploy.

Estende a classe Notebook da skill gerar-modulo-ipynb (mesmo formato de .ipynb)
com os blocos fixos de um projeto prático e com um GABARITO conferido:

  - exercicio(codigo_inicial, solucao=...): a célula entregue ao aluno contém só
    o código inicial (dados + comentários # TODO). A solução NÃO vai para o
    notebook, mas é executada no salvar() logo depois do código inicial;
  - resultado_esperado(saida): cria a célula "🔎 Resultado esperado" e registra
    a saída para ser comparada com o que a solução realmente imprime.

Se alguma saída esperada não bater com a solução, o salvar() mostra a diferença
e NÃO grava o notebook. Assim, nenhum número do enunciado é calculado "de cabeça".

Uso (dentro de um script de geração):

    import sys
    sys.path.insert(0, r"<caminho desta skill>/scripts")
    from construtor_projeto import ProjetoPratico, mensagem

    nb = ProjetoPratico()
    nb.cabecalho("02", "Título do projeto", "Parágrafo de abertura...")
    nb.md(r'''
    ## 1️⃣ Missão 1 — Nome da missão

    ''' + mensagem("Marina", "Gerente de Cadastro", "Oi! Preciso de..."))
    nb.exercicio(r'''
    preco_produto = 10
    # TODO: calcule e imprima o dobro do preço
    ''', solucao=r'''
    print(f'Dobro: {preco_produto * 2}')
    ''')
    nb.resultado_esperado("Dobro: 20")
    nb.dica("revise a seção 3.3 do Módulo 02.")
    nb.separador()
    nb.salvar("content_generation/jupyter_notebooks/module_02_projeto_pratico.ipynb")
"""

import contextlib
import io
import os
import sys
import traceback

# Reaproveita o construtor base da skill irmã, para que módulos e projetos
# tenham exatamente o mesmo formato de .ipynb.
_PASTA_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gerar-modulo-ipynb", "scripts")
sys.path.insert(0, os.path.normpath(_PASTA_BASE))
from construtor_notebook import Notebook  # noqa: E402

MODOS_CONFERENCIA = ("exato", "inicio", None)


def mensagem(nome, cargo, texto):
    """Balão de chat de um personagem, usado para apresentar o pedido de cada missão."""
    return f'> 💬 **{nome} ({cargo}):** "{texto}"'


def _normalizar(saida):
    linhas = [linha.rstrip() for linha in saida.strip("\n").split("\n")]
    return "\n".join(linhas).strip("\n")


class ProjetoPratico(Notebook):
    def __init__(self):
        super().__init__()
        self.solucoes = {}        # índice da célula de código -> código da solução
        self.conferencias = []    # (índice da célula, saída esperada, modo)
        self._ultimo_exercicio = None

    def cabecalho(self, numero_modulo, titulo, introducao):
        """Célula 1 do projeto, no formato fixo do curso."""
        self.md(
            f"# 🚀 Projeto Prático — Módulo {numero_modulo}: {titulo}\n\n---\n\n"
            f"{introducao.strip()}\n\n"
            "Curso: Ready To Deploy\n\n"
            "Criado por: [Enzo Schitini](https://www.linkedin.com/in/enzoschitini)\n\n---"
        )

    def exercicio(self, codigo_inicial, solucao=None):
        """Célula de código do aluno. `solucao` é executada logo após o código inicial, só na conferência."""
        self.code(codigo_inicial)
        indice = len(self.celulas) - 1
        if solucao is not None:
            self.solucoes[indice] = solucao.strip("\n")
        self._ultimo_exercicio = indice

    def resultado_esperado(self, saida, legenda=None, titulo="Resultado esperado", confere="exato"):
        """Célula "🔎 Resultado esperado" referente ao último exercicio().

        confere="exato":  a saída da solução precisa ser idêntica;
        confere="inicio": a saída da solução precisa COMEÇAR com este texto
                          (útil quando o final depende de escolhas do aluno);
        confere=None:     não confere (use só quando não houver solução possível).
        """
        if confere not in MODOS_CONFERENCIA:
            raise ValueError(f"confere deve ser um de {MODOS_CONFERENCIA}")
        if confere and self._ultimo_exercicio not in self.solucoes:
            raise ValueError("resultado_esperado() conferido precisa de um exercicio(..., solucao=...) antes dele.")
        saida = _normalizar(saida)
        titulo_formatado = f"🔎 **{titulo}**" + (f" ({legenda})" if legenda else "") + ":"
        self.md(f"{titulo_formatado}\n\n```\n{saida}\n```")
        if confere:
            self.conferencias.append((self._ultimo_exercicio, saida, confere))

    def dica(self, texto):
        self.md(f"> 💡 **Dica:** {texto.strip()}")

    def verificar_gabarito(self):
        """Executa o notebook "resolvido" em ordem e devolve a lista de divergências (vazia = tudo certo)."""
        namespace = {"__name__": "__main__"}
        saidas = {}
        for indice, (tipo, texto) in enumerate(self.celulas):
            if tipo != "code":
                continue
            codigo = texto + ("\n" + self.solucoes[indice] if indice in self.solucoes else "")
            buffer = io.StringIO()
            try:
                with contextlib.redirect_stdout(buffer):
                    exec(compile(codigo, f"celula_{indice}", "exec"), namespace)
            except Exception:
                return [f"Célula {indice}: o código (inicial + solução) gerou erro:\n{traceback.format_exc(limit=1)}"]
            saidas[indice] = buffer.getvalue()

        divergencias = []
        for indice, esperado, modo in self.conferencias:
            obtido = _normalizar(saidas.get(indice, ""))
            bateu = obtido == esperado if modo == "exato" else obtido.startswith(esperado)
            if not bateu:
                divergencias.append(
                    f"Célula {indice} (conferência '{modo}'):\n"
                    f"--- esperado no enunciado ---\n{esperado}\n"
                    f"--- impresso pela solução ---\n{obtido}"
                )
        return divergencias

    def _versao_gabarito(self):
        gabarito = Notebook()
        for indice, (tipo, texto) in enumerate(self.celulas):
            if tipo == "code" and indice in self.solucoes:
                gabarito.code(f"{texto}\n\n# ✅ Solução\n{self.solucoes[indice]}")
            elif tipo == "code":
                gabarito.code(texto)
            else:
                gabarito.md(texto)
        return gabarito

    def salvar(self, caminho, caminho_gabarito=None):
        """Confere o gabarito e só então grava o notebook (e, opcionalmente, uma versão com as soluções)."""
        divergencias = self.verificar_gabarito()
        if divergencias:
            print("GABARITO DIVERGENTE — o notebook NÃO foi gravado.\n")
            print("\n\n".join(divergencias))
            sys.exit(1)
        print(f"Gabarito conferido: {len(self.conferencias)} resultado(s) esperado(s) batem com as soluções.")
        super().salvar(caminho)
        if caminho_gabarito:
            self._versao_gabarito().salvar(caminho_gabarito)
