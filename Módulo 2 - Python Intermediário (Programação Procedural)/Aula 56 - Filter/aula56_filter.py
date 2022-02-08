from dados import produtos, pessoas, lista

# A função filter também retorna um iterável
nl = filter(lambda x: x>5, lista)  # Retorna True ou False e os que forem falsos serão removidos da nova lista
print(list(nl))  # [6,7,8,9]

# Funciona de forma bastante semelhante com a list comprehension

nl2 = [x for x in lista if x > 5]
print(nl2) # [6,7,8,9]

print('-'*90)

# Trabalhando com dicionários

def filtra(p):
    if p['preco'] > 50:
        return True
    
#nova_lista = filter(lambda p: p['preco'] > 50, produtos)  # Irá retornar todos os produtos com o preço superior a 50 reais
nova_lista = filter(filtra, produtos)  # Funciona também com uma função normal

for produto in nova_lista:
    print(produto)

print('-'*90)

# Trabalhando com o dicionário pessoas

def filtra_idade(p):
    if p['idade'] < 18:
        return True

menores_de_idade = filter(filtra_idade, pessoas)

for m in menores_de_idade:
    print(m)

# A vantagem da função é a reutiização, porém, a função lamba é mais curta e prática