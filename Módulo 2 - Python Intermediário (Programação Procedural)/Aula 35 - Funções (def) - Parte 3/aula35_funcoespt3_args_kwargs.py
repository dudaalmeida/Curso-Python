"""
Funções - def em Python - *args **kwargs (Parte 3)
"""

# Tuplas não podem ser alteradas, mas podem ser convertidas em listas

def function(*args):   # Quando não se sabe quantos argumentos serão passados para essa função
    print(args)        # Verá os argumentos empacotados numa tupla
    print(args[0])     # Acessar o primeiro valor da tupla
    print(args[-1])    # Acessar o último argumento da tupla
    print(len(args))   # Quantos valores tem dentro dessa tupla

    args = list(args)  # Convertendo a tupla numa lista
    args[0] = 20       # Agora é possível alterar o valor

    for v in args:
        print(v)       # Printa cada valor da lista

def function2(*args):
    print(args)

# O nome não precisa ser exatamente *args, mas por convenção a palavra args é adotada, assim como kwargs
def function3(*args, **kwargs):  # kwargs = key word arguments, argumentos com palavras-chave
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])  # Se quiser acessar os índices individualmente

    # Outra forma de acessar os índices individualmente
    nome = kwargs.get('nome')
    print(nome)

    # É muito útil para saber se determinado argumento foi enviado
    idade = kwargs.get('idade')
    
    if idade is not None:   # É possível fazer uma checagem para saber se o argumento existe
        print(idade)
    else:
        print('Idade não existe')
    
    # Da outra maneira, se o argumento não existir, ocorrerá um erro e para a execução do programa, como pode ser visto abaixo
    # idade = kwargs['idade']
    # print(idade)

lista = [1,2,3,4,5]
n1, n2, *n = lista  # O mesmo ocorre com o *args, onde os valores são empacotados dentro de uma variável com *

print(*lista, sep='-')  # Vou estar desempacotando cada valor da lista, ficando como se estivesse escrito: print(1,2,3,4,5)
                        # O argumento sep serve para selecionar o separador, que no caso foi '-'

var = function(1,2,3,4,5)

# Outra opção é mandar a variavel lista, porém desempacotada

function2(lista,'6')        # Se eu não enviar a lista desempacotada, será criada uma lista no primeiro indice da tupla
                            # Algo semelhante a: ([1,2,3,4,5],'6')
function2(*lista,10,20,30)  # Mandando a lista desempacotada, ela passa a fazer parte dos índices da tupla                
                            # Ao enviar a lista desempacotada, cada elemento que for enviado posteriormente fará parte dessa lista
lista2 = [12,34,65,89]
function2(*lista, *lista2)  # Envia ambas as listas desempacatadas, sendo elas mescladas dentros dos args

function3(*lista, *lista2, nome='João', sobrenome='Silva', idade=30)  # Passando argumentos nomeados, que não serão printados no print(args), mas sim no print(kwargs)