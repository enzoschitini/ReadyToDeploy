# Lê um arquivo de texto e permite extrair uma linha específica
class ArquivoTXT:

    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.linhas = self._ler_linhas()

    def _ler_linhas(self):
        with open(self.caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            return arquivo.readlines()

    def extrair_linha(self, numero_linha: int):
        return self.linhas[numero_linha - 1].strip()
