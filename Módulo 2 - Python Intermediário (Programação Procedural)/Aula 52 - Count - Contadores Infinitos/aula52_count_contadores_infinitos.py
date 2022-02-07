"""
count - Intertools
"""

# É possível utilizar a função next() com ele, diferentemente da função range() que não gera um iterador mas sim um iterável

from itertools import count

# É um iterador que não tem fim
contador = count(start=5, step=0.2)  # Mas é possível definir o inicio e o step. No step, é possível utilizar número de ponto flutuante ou negativo

for valor in contador:
    print(round(valor,2))  # Arredondar para diminuir a quantidade de casas decimais

    if valor >= 10:
        break

contador2 = count()
lista = ['Luiz', 'João', 'Maria','Eduarda','Silva']
lista = zip(contador2, lista)  # Uma forma de adicionar indices numa lista
print(list(lista))