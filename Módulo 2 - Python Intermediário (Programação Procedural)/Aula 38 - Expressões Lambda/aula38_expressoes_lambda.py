a = lambda x, y: x * y  # A função é anônima
# Não precisa da palavra return. Sempre que valor é colocado ali, ele é retornado
print(a(2,2))

######################################################

lista = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]

def func(item):  # Função para ordenar a lista
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)

# Nesse sentido, uma expressão lambda deixa o processo mais prático

lista2 = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]

lista2.sort(key=lambda item: item[1], reverse=True)
print(lista2)

# Outro modo para organizar a lista sem alterar a original

lista3 = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]

print(sorted(lista3, key=lambda i: i[1], reverse=True))  # Não altera a lista 3
print(lista3)