import threading
from produto_repository import ProdutoRepository

class ProdutoService:
    def __init__(self):
        self.repo = ProdutoRepository()
        self.lock = threading.Lock()

    def produto_mais_caro(self):
        with self.lock:
            produtos = self.repo.carregar()
            return max(produtos, key=lambda p: p.preco, default=None)

    def produto_mais_barato(self):
        with self.lock:
            produtos = self.repo.carregar()
            return min(produtos, key=lambda p: p.preco, default=None)

    def media_precos(self):
        with self.lock:
            produtos = self.repo.carregar()
            if not produtos:
                return 0.0
            return sum(p.preco for p in produtos) / len(produtos)

    def produtos_acima_da_media(self):
        media = self.media_precos()
        with self.lock:
            produtos = self.repo.carregar()
            return [p for p in produtos if p.preco >= media]

    def produtos_abaixo_da_media(self):
        media = self.media_precos()
        with self.lock:
            produtos = self.repo.carregar()
            return [p for p in produtos if p.preco < media]
