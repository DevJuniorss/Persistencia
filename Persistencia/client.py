from produto_service import ProdutoService

def main():
    service = ProdutoService()

    print("=== Produto mais caro ===")
    print(service.produto_mais_caro())

    print("\n=== Produto mais barato ===")
    print(service.produto_mais_barato())

    print("\n=== Média de preços ===")
    print(f"{service.media_precos():.2f}")

    print("\n=== Produtos acima da média ===")
    for p in service.produtos_acima_da_media():
        print(p)

    print("\n=== Produtos abaixo da média ===")
    for p in service.produtos_abaixo_da_media():
        print(p)

if __name__ == "__main__":
    main()
