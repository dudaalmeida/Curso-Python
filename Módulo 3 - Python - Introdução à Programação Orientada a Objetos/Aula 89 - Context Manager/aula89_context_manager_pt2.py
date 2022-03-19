# Outra maneira de criar um gerenciador de contexto
from contextlib import contextmanager

@contextmanager
def abrir(arquivo,modo):
    try:
        arquivo = open(arquivo,modo)
        print('Abrindo arquivo')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('abcd.txt','w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

# Em ambos os métodos, utilizar o 'with' é necessário. Sem ele, não funciona