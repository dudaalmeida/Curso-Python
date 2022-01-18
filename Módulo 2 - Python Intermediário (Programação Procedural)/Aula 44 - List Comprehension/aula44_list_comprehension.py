# Exemplo 1

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]  # Iterando o elemento l1 dentro de l2

print(l2)  # Exatamente identico ao l1

# Exemplo 2

ex2 = [v*2 for v in l1]  # Irá multiplicar cada elemento de l1 será multiplicado por 2
print(ex2)

# Exemplo 3

ex3 = [(v, v2) for v in l1 for v2 in range(3)]  # Há dois for rodando juntos, o primeiro itera sobre a primeira lista e o segundo irá iterar sobre cada elemento da primeira lista
print(ex3)  # Irá printar dessa forma: [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]

# Exemplo 4

l2 = ['Luiza', 'Mauro', 'Maria']
ex4 = [v.replace('a','@') for v in l2]  # Irá substituir os 'a' por '@' na l2
print(ex4)

# Exemplo 5

tupla = (
    ('chave1','valor1'),
    ('chave2','valor2'),
)

ex5 = [(y,x) for x, y in tupla]  # Irá inverter as chaces com os valores
ex5 = dict(ex5)  # Está convertendo em dicionário
print(ex5)
print(ex5['valor2'])

# Exemplo 6

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # Pegando todos os números de l3 que são divisíveis por 3 e também divisíveis por 8
print(ex6)  # Foi feita uma espécie de filtragem

# Exemplo 7

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]  # Pega os números divisíveis por 3 e divisíveis por 8 e coloca 0 no lugar dos que não são
print(ex7)
