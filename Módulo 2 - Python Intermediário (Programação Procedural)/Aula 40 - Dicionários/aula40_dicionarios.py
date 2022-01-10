# Os dicionários são muito semelhantes as listas porém neles, você controla os índices
# Ele é uma estrutura de dados que suporta um par de chave (indice) e valor

d1 = {'chave1':'valor da chave'}  # Dicionário criado - Essa é a forma mais usada geralmente
d1['nova_chave'] = 'Valor da nova chave'  # Acrescentando uma nova chave

print(d1)
print(d1['chave1'])  # Para vizualizar a chave1
print('----------------------------------')

# Outra forma de criar dicionário 

d2 = dict(chave='Valor da Chave', chave2='Valor da chave 2') 
print(d2)
print('----------------------------------')


# Se a chave se repete, o valor que permanencerá será o último indicado
d3 = {'chave1':'valor da chave', 'chave1':'valor da chave','chave1':'valor final da chave'} 
print(d3)  # Chaves nos dicionários precisam ser únicas
print('----------------------------------')

# Paras as chaves, é possível usar qualquer tipo de dado imutável em Python, mas geralmente sõa utilizadas strings
d4 = {
    'str' : 'Usando string',
    123 : 'valor',
    (1,2,3,4) : 'Usando tupla',
}

print(d4[(1,2,3,4)])
print('----------------------------------')

# Se for procurada uma chave que não existe, o código entrará numa exceção e dará erro
# Como prevenção, pode ser feita uma verificação

d4['naoexiste'] = 'Agora existe'
if 'naoexiste' in d4:
    print(d4['naoexiste'])
else:
    print('Essa chave não existe no dicionário')
print('----------------------------------')

# Outra maneira de resolver

print(d4.get('nomedachave'))  # Se a chave não existir simplesmente será exibido None e o código não parará de funcionar

d4['nomedachave'] = 'Agora existe também' 

if d4.get('nomedachave') is not None:  # Outra forma de verificação
    print(d4.get('nomedachave'))  

print('----------------------------------')

# Atualização de valores dentro de chaves
d4['str'] = 'Novo valor de str'   # Essa mesma forma pode ser usada para atualizador o valor de uma determinada chave
d4.update({'nova_chave':'Novo valor'})  # Serve para atualizar ou criar
print(d4)

# Para apagar alguma chave
del d4['str']
print(d4)
print('----------------------------------')

# Checando dentro do dicionário

print('str' in d4)             # Chcando se a chave existe em d4
print('valor' in d4.values())  # Checando se o valor 'valor' existe nos valores
print(len(d4))                 # Quantos pares existem
print('----------------------------------')

# Iterar sobre dicionários

for k in d4:  # Dessa forma acessa as chaves
    print(k)
print('----------------------------------')


for v in d4.values():  # Dessa forma acessa os valores
    print(v)
print('----------------------------------')


# Uma forma de acessar a chave juntamente com o valor
for k in d4.items():  # É possível observar que são criadas tuplas 
    print(k)
    print(k[0], k[1])  # Dessa forma está acessando a chave e o valor, separadamente
print('----------------------------------')


# Outra maneira é desempacotando os valores
for k,v in d4.items():
    print(k,v)
print('----------------------------------')


# Podem ser criados dicionários dentro de outros dicionários
clientes ={
    'clientes1' : {
        'nome' : 'Luiz',
        'sobrenome': 'Otávio',
    },
     'clientes2' : {
        'nome' : 'João',
        'sobrenome': 'Moreira',
    },
      'clientes3' : {
        'nome' : 'Maria',
        'sobrenome': 'Joaquina',
    },
}

# Forma de iterar dicionários dentro de dicinários
for clientes_k, clientes_v in clientes.items(): # Executa a chaves dos clientes
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items(): # Executa os dados dentro de cada chave que representa um cliente
        print(f'\t{dados_k} = {dados_v}')
print('----------------------------------')


# Associando valores dentro de dicionários

d5 = {1: 'a', 2: 'b', 3: 'c', 'd': ['João','da Silva']}
v1 = d5  # Dessa forma, eles não estõa sendo duplicados mas sim associoados também

v1[1] = 'Luiz'  # Não está criando um novo objeto. Ambos são idênticos e apontam para o mesmo endereço de memória

print(d5,v1)  # É possível obserar que o valor está sendo alterado nos dois
print(v1 == d5)
print('----------------------------------')

# Se quiser criar uma cópia rasa do dicionário, deve ser feito isso
v2 = d5.copy()  # Porém os valores não foram copiados para cá, eles são só uma referência uma shallow copy (cópia rasa)
v2[1] = 'Lucas'

print(d5,v2)  # Dessa forma, o valor só será alterado em v2
print(v2['d'][0])  # Acessando diretamento o item da lista que está dentro do dicionário
print('----------------------------------')

# A partir do momento em que eu acesso o valor de uma chave dentro de uma lista que é um item mutável, ele será alterado nas duas listas
# Daí o nome 'shallow copy' é referente a ser possível alterar os valores dentro

v2['d'][0] = 'Joãozinho'
print(d5,v2) 
print('----------------------------------')

# Só não teria esse problema com tuplas pois elas são imutáveis

# Para criar uma cópia real de um dicionário
import copy  # Importando o módulo copy

v3 = copy.deepcopy(d5)  # Neste momento, os dicionários passam a ser independentes
v3['d'][0] = 'Joaquim'
print(d5,v3) 
print('----------------------------------')

# É possível converter listas em dicionários

lista = [
    ['c1', 1],
    ['c2', 1],
    ['c3', 1],
]

d6 = dict(lista)
print(d6)

# Funciona também com tuplas dentro de lsitas

lista2 = [
    ('c1', 1),
    ('c2', 1),
    ('c3', 1),
]

d7 = dict(lista)
print(d7)

# E com listas dentro de tuplas ou simplesmente tuplas dentro de tuplas

lista2 = (
    ['c1', 1],
    ['c2', 1],
    ['c3', 1],
)

d8 = dict(lista)
print(d8)
print('----------------------------------')

# Para dicionários também existem as funções pop() e popitem()
d9 = {
    1: 2,
    2: 3,
    4: 5,
    6: 7,
}

d9.pop(4)     # Irá eliminar a chave 4
d9.popitem()  # Irá eliminar o último item independente da chave
print(d9)

# Também é possível concatenar dois dicionários

d10 = {
    'a': 'b',
    'c': 'd',
}

d9.update(d10)  # Irá adicionar os itens de d10 no d9
print(d9)
