lista = [1,2,3,4,5,6]
print(hasattr(lista, '__iter__'))  # Esse método verifica se é iterável

# O que o for faz para transformar a lista em um iterador é usar o método __iter__
for v in lista:  # Transforma a lista em um iterador
    print(v)

lista = iter(lista)   # Transforma a lista em um iterador

# Para verificar se é um iterador
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print('--------------------------------------')

# Um iterável é um objeto que você pode iterar sobre ele mas ele não necessariamente é um iterador (não necessariamente irá te dar um valor de cada vez)
# Um iterador vai te dar um valor de cada vez sempre que você precisar desse valor

# Geradores - Geralmente utilizados para evitar problemas de memória
import sys
import time

lista2 = list(range(10))  
print(sys.getsizeof(lista2))  # Pegando quantos bytes de memória essa lista está consumindo no computador

# Os geradores não te dão todos os valores de uma vez, eles de dão o que você pediu no momento

# Função geradora -> Agora irá retornar um valor por vez em vez de esperar o array ser preenchido (lazy evaluation)
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
print(g)

# Os geradores possuem os métodos iteradores e iteráveis
print(hasattr(g,'__iter__'))
print(hasattr(g,'__next__'))

#for v in g:
#    print(v)

# Outra forma de fazar um gerador - Método mais manual
# A melhor maneira ainda é com o for

def gerador():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gerador()
print(next(g))
print(next(g))
print(next(g))
# Se colocar mais um print(next(g)) o python irá gerar uma excessão StopIteration informando que não há mais a ser mostrado

lista3 = [x for x in range(10000)]
print(type(lista3))
print(sys.getsizeof(lista3))
lista4 = (x for x in range(10000))  # Essa é uma forma muito mais simples do que utilizar uma função para criar um gerador
print(type(lista4))
print(sys.getsizeof(lista4))

# Apesar das listas serem idênticas, a diferença de tamanho é considerável
# Mesmo que o range da lista gerador aumente, o espaço ocupado será o mesmo
# Os geradores não vão salvar todos os valores na memória e só vai te entregar um valor qualquer quando você pedir