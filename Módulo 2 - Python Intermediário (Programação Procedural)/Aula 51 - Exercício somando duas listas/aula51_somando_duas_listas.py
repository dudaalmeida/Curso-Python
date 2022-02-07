"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado

lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Solução específica do python
lista_soma = [x+y for x,y in zip(lista_a, lista_b)]
print(lista_soma)

# Solução para qualquer linguagem
lista_soma2 = []
for i in range(len(lista_b)):
    lista_soma2.append(lista_a[i] + lista_b[i])
print(lista_soma2)

# Outra solução para python, mas menos prática
lista_soma3 = []
for i, _ in enumerate(lista_b):
    lista_soma3.append(lista_a[i] + lista_b[i])
print(lista_soma3)

# A última opção, que considera a lista maior, pode ser resolvida da seguinte forma

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma4 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma4)  # [22, 4, 6, 10, 55, 60, 70]