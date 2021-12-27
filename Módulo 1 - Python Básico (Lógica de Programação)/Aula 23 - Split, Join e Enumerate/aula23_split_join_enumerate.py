"""
Split, Join Enumerate em Python
* Split - Dividir um string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

contagem = 0

for valor in lista1:
    qtd = lista1.count(valor) ## Quantas vezes cada palavra aparece
    
    if qtd > contagem:
        contagem = qtd
        palavra = valor

print(f' A palavra que apareceu mais vezes foi {palavra} ({contagem}x)')

####################################################################################################

for valor in lista2:
    print(valor.strip().capitalize())  # Remove o espaço do inicio e do fim, além de deixar a primeira letra maiuscula

lista = ['O', 'Brasil', 'é', 'penta.']
string = ' '.join(lista)  ## Gera uma string separada por espaços a partir de uma lista

print(string)

string2 = 'O Brasil é penta.'
lista = string.split(' ')
string3 = '*'.join(lista)

print(string3)

for index, v2 in enumerate(lista):
    print(index,v2,lista[index])  # Indice, valor, valor na lista pelo indice

#########################################################################################
                                #Desempacotamento#

lista3 = [
    [0,'Ana'],
    [1,'Fernanda'],
    [2,'Luiza']
]

for indice, nome in lista3:
    print(indice, nome)

lista4 = ['Ana', 'Fernanda', 'Luiza']

for indice, nome in enumerate(lista4):
    print(indice,nome)

n1, n2, n3 = lista4 # Desempacotamento de lista
print(n1)