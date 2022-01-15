"""
add (adiciona), update (atualiza), clear, discard
union | une
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

# Sets são um conjunto de elementos que você adicionar dentro de uma mesma estrutura de dados
# A maior diferença entre as listas, dicionários e os sets é que os sets só suportam elementos únicos
# Os sets só recebem valores, não tem par de chaves e valores
# Os sets só suportam elementos imutáveis
# Sets são conjuntos em inglês
# Os sets não possuem índices, de forma que não dá para acessar os valores diretamente do set

s1 = {1,2,3,4,5,6}

for v in s1:  # Ainda é possível iterar sobre os sets, mas não acessá-los diretamente
 print(v)

# Se declarar dessa forma: s2 = {}, você não estará criando um set mas sim um dicionário
# Assim, outra forma de criar um set é

s2 = set()   # Assim cria um set vazio
s2.add(1)    # Adiciona o elemento '1' no set
s2.add(100)  # O número é adicionado sem perder a ordem, não fica numa posição aleatória dentro do set 
s2.add((4,5,6))

s2.discard(100)  # Descarta o elemento '100' do set
s2.update('a')   # Adiciona o elemento 'a'
s2.update('Python')  # Ela irá iterar sobre cada elemento dessa string, de forma que terá todas as letras do elemento Python dentro do set
                     # E o update não respeita ordem
print(s2)        # O print seria assim: {1, 'n', 'a', 'P', 't', 'y', 'h', (4, 5, 6), 'o'}

s3 = set()
s3.update([1,2,3,4,5], {5,6,7,8})  # Os sets não aceitam elementos duplicados, de forma que um dos 5s será ignorado

print(s3)

# Dessa forma, sets são utilizados geralmente para eliminar elementos duplicados numa lista

l1 = [1,2,1,1,5,6,6,6,6,6,6,6,8,9,7,'Ar','Ar']
l1 = set(l1)  # Converte a lista para um set
l1 = list(l1)  # Ao retornar como lista, terão sido removidos todos os elementos repetidos
               # Porém os elementos irão retornar fora de ordem
print(l1)

# Union ou | - Para encontrar a união entre os dois sets

s4 = {1,2,3,4,5,7}
s5 = {1,2,3,4,5,6}
s6 = s4 | s5

print(s6)

# Intersection - Os elementos que ambos tem em comum
s7 = s4 & s5 
print(s7)

# Difference -  A ordem importa
# Se for utilizada o sinal '-' com dois sets, serão pegos apenas os elementos do set da esquerda
s8 = s4 - s5  # Neste caso, aparecerá so o '7'
s9 = s5 - s4  # Neste caso, aparecerá so o '6'
print(s8)
print(s9)

# Symmetric difference - Elementos exclusivos de cada set
s10 = s4 ^ s5  # Neste caso, serão o 6 e 7
print(s10)

# Exemplo de situação
l1 = ['Luiz','João','Maria']
l2 = ['João','Maria','Maria','Luiz','Luiz','Luiz','Luiz','Luiz',]

print(l1 != l2)  # Mostrará que são diferentes

# Mas se desejo saber se as listas são iguais independentemente dos elementos duplicados
l1 = list(set(l1))
l2 = list(set(l2))

print(l1 == l2)  # Agora mostra que as listas são iguais
# O problema disso é que a lista foi modificada

# Pode ser feita uma verificação sem mudar a estrutura da lista
l1 = ['Luiz','João','Maria']
l2 = ['João','Maria','Maria','Luiz','Luiz','Luiz','Luiz','Luiz']

if set(l1) == set(l2):
    print('l1 é igual a l2')
else:
    print('l1 é diferente de l2')

