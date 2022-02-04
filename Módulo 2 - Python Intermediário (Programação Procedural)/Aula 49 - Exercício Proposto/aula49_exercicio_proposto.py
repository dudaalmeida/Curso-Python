carrinho = []
# Somar todos os valores utilizando list comprehension
carrinho.append(('Produto 1', 89))
carrinho.append(('Produto 2', 37.90))
carrinho.append(('Produto 3', 73))
carrinho.append(('Produto 4', 35))
carrinho.append(('Produto 5', 10))

total = sum([float(y) for x,y in carrinho])
print(total)