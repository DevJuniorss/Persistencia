import csv
from produto import Produto

class ProdutoRepository:
    def __init__(self, arquivo="produtos.csv"):
        self.arquivo = arquivo

    def salvar(self, produtos):
        with open(self.arquivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for p in produtos:
                writer.writerow([p.id, p.nome, p.preco])

    def carregar(self):
        produtos = []
        try:
            with open(self.arquivo, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for linha in reader:
                    if len(linha) == 3:
                        produtos.append(Produto(int(linha[0]), linha[1], float(linha[2])))
        except FileNotFoundError:
            pass
        return produtos
