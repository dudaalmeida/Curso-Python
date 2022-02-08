from dados import produtos, pessoas, lista
from functools import reduce

# A função reduce é uma acumuladora
# Acumula todos os valores e reduz em um só

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)  # A cada volta do laço, ela irá executar essa função i: i + ac
print(soma_lista)

print('-'*90)

# Trabalhando com o dicionário de produtos

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)  # Vai acumular os preços dentro do ac
print(round(soma_precos))

print('-'*90)

# Trabalhando com o dicionário de idades

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(f' Média de idades é {soma_idades/ len(pessoas)}')