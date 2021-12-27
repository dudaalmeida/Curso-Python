"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

texto = 'Valor'

#         0    1    2    3    4     5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#print(lista[0:3])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)

l1.extend(l2) ## Extende os valores da l2 no fim da l1
print(l1)

l2.append('B')  ## Adiciona o valor 'B' no fim na l2
print(l2)

l2.insert(0, 'banana')  ## Insere o valor "banana" no indice 0 e "empurra" para a direita o resto dos valores
print(l2)

l2.pop()  ## Remove o último elemento da lista
print(l2)

l4 = [1,2,3,4,5,5,6,7,8,9]
del(l4[3:5])  ## Deleta os valores dos indices 3 ao 5
print(l4)

l4.insert(0,'banana')
print(l4)
del(l4[0])  ## Deleta o valor do indice 0
print(l4)

print(max(l4))  ## Valor máximo de l4
print(min(l4))  ## Valor mínimo de l4

l5 = list(range(0,100,8)) ## Gera objeto range e converte em lista
print(l5)

for valor in l5:  ## Iterando a lista em um laço for
    print(valor)

l6 = ['String', True, 10, -20.5]

for elem in l6:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

#######################################################################################################
# -------------------------------------- JOGUINHO DA FORCA -------------------------------------------#

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    
    print(f'Você ainda tem {chances} chances.')

    letra = input('Digite um letra: ')

    if len(letra) > 1:
        print('Ahh, isso não vale! Digite apenas uma letra.')
        continue

    digitadas.append(letra)
    
    if letra in secreto:
        print(f'Que legal! A letra {letra} existe na palavra secreta.')
    else:
        print(f'Aish! A letra {letra} não existe na palavra secreta.')
        digitadas.pop()
        chances -= 1
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print(f'Que legal! Você ganhou! A palavra era: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    