# Exemplo de E-commerce

# A classe precisa dos produtos para listar, somar e inserir no carrinho
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

# Ela pode existir sozinha e não depende em nada da classe carrinho
class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor
