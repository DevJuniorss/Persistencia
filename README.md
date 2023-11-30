Trabalho_02
===========
ClassDiagram da aplicação atual

 ```mermaid
 classDiagram
    Client "1" -- "*"ItemCompra
    Client "1"-- "*"Endereco
    ItemCompra "*"-- "1"Produto
    Client "1" -- "*"Compra
    Estoque "*" -- "*"Produto
    Produto "*" -- "*"Fornecedor
    
class Client{
    -id :Integer 
    -cpf: String
    -nome : String
    -fone : String
    -email : String
    -endereco : Endereco
}
class Endereco{
    -cep : String
    -numero : String
    -rua : String
    -bairro : String
    -cidade : String
    -estado : String
}
class Produto{
    -id : Integer
    -nome : String
    -dataValidade : LocalDate
    -qtdProduto : Integer
    -preco : float

}
class Compra{
    -id : Integer
    -dataHora : LocalDate
    +getValorTotal() float
}
class ItemCompra{
    -id : Integer
    -quantidade : Integer
    -valorUnitario : float
    +getValorTotal() : float
}
class Fornecedor{
    -id : Integer
    -nome : String
    -cnpj : String
    -Endereco : Endereco
    -List<Produto> : List<>
    -fone : String 
}
class Estoque{
    -idProduto : Produto
    -qtdProduto : List<Produto>
}
```#   P e r s i s t e n c i a  
 