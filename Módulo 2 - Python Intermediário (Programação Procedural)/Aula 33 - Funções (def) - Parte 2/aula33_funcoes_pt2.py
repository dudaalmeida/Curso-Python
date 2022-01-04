"""
Funções - def em Python (Parte 2)
"""
def funcao(var):
    return var

variavel = funcao('Valor que eu quero')
#print(variavel)

if variavel:
    print(variavel)
else:
    print('Nenhum valor')

####################################################################################

def divisao(n1,n2):
    if n2 == 0:
        return 
    return n1/n2

result = divisao(1,0)

if result:
    print(result)
else:
    print('Conta Inválida.')

#####################################################################################

def dumb():
    return 1.1

var = dumb()
print(var, type(var))

#####################################################################################

def h(g):
    print(g)

def func():
    return h

g = func()('Colocar o meu valor')

print(id(g), id(h))

if g == h:
    print('g é igual a h')
else:
    print('Blá')

####################################################################################

def function():
    return 'Luiz', 'Otávio'  # Retorna uma tupla

tupla = function()

print(tupla[0], type(var))