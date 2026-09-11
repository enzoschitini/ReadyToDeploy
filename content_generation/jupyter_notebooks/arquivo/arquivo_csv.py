# Lê um arquivo CSV e permite extrair colunas específicas
class ArquivoCSV:

    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.linhas = self._ler_linhas()
        self.colunas = self._extrair_nomes_colunas()

    def _ler_linhas(self):
        with open(self.caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            return arquivo.readlines()

    def _extrair_nomes_colunas(self):
        return self.linhas[0].strip().split(',')

    def extrair_coluna(self, indice_coluna: int):
        valores = []
        for linha in self.linhas[1:]:
            valores.append(linha.strip().split(',')[indice_coluna])
        return valores
