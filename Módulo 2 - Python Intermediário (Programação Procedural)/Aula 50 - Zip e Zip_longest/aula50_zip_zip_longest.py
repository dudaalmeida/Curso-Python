"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count  # Caso não especificasse qual o módulo importado, no código deveria ser utilizado itertools.zip_longest para chamar o comando

indice = count()
cidades = ['São Paulo','Belo Horizonte','Salvador','Monte Belo', 'Outra']
estados = ['SP','MG','BA']

cidades_estados = zip(estados,cidades)  # Junta as duas listas em uma única tupla, retornando um iterador que possui um next()
print(cidades_estados)  # Dessa forma só aparecec o endereço na memória
#print(list(cidades_estados))
#print(dict(cidades_estados))

for valor in cidades_estados:
    print(valor)

# O comando Zip só irá unir até a menor lista, por isso Monte Belo foi excluído

# Zip_longest une as listas inteiramente e preencherá com None o que não tiver valor correspondente
cidades_estados2 = zip_longest(
    indice,
    estados,
    cidades,
    fillvalue= 'Estado'
    )  # Aqui é possível especificar o que preencher no caso de não haver a mesma quantidade de valores nas listas

#print(list(cidades_estados2))

# Dessa maneira, o código entrará num loop infinito pois o iterador count não irá parar de contar e o zip_longest inclui tudo
#for indice, estado, cidade in cidades_estados2:
#    print(indice,estado,cidade)

# Nesse caso, o ideal é usar o coamdo Zip

cidades_estados3 =  zip(
    indice, 
    cidades,
    estados
)  # é gerada uma tupla com valor triplo

for indice, estado, cidade in cidades_estados3:
    print(indice,estado,cidade)

from types import GeneratorType
variavel = zip('Alô', 'Alô')  # Retorna um iterador
print(isinstance(variavel, GeneratorType))  # Verificando se é um gerador
print(list(variavel))

# Para ser um gerador, deveria ser da seguinte forma
variavel2 = ((x,y) for x,y in zip('Alô','Alô'))
print(isinstance(variavel2, GeneratorType))  
print(list(variavel2))

