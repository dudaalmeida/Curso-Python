from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x*2, lista)  # Recebe uma função como primeiro argumento, nesse caso a função lambda está multiplicando os elementos da lista por 2
# A função map() não retorna uma lista pronta, ela retorna um iterador
# Com listas, a função map() não é muito interessante, pois a list comprehension serve melhor ao propósito

nova_lista = [x*2 for x in lista]

print(lista)
print(list(nova_lista))

print('-'*90)

# Trabalhando com dicionários

def aumenta_preco(p):
    p['preco'] = round(p['preco']*1.05, 2)
    return p

# Uma função lambda não permitiria que os valores fossem conservados no dicionário original
novos_produtos = map(aumenta_preco, produtos)  # Acessando o dicionário e pegando a coluna de preços
# A função map() está mapeando uma função que está passando em cada elemento do iterável, ou seja, ela está passando a função em cada elemento do iterável

for produto in novos_produtos:
    print(produto)     

print('-'*90)

# Trabalhando no dicionário de pessoas      

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade']*1.2,2)  # Adciona uma nova chave no dicionário com a nova idade
    return p

idades = map(aumenta_idade, pessoas)

for idade in idades:
    print(idade)