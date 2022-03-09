# Dentro de associação existem outros dois tipos de relação: Agregação e Composição
# Agregação e Composição: É quando uma classe usa outra classe dentro de si e essa classe precisa da outra classe.

# Agregação -> Exemplo: Carro e Roda. O carro e as rodas existem um sem o outro, porém, o carro
# não funciona de maneira adequada sem as rodas. Ou seja, uma classe, além de utilizar a outra,
# também precisa dela.

#-----------------------------------------------------------------------------------------------#
from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)

carrinho.lista_produto()
print(carrinho.soma_total())
