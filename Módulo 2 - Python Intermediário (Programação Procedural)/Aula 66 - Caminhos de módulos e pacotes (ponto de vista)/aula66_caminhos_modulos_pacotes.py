# from pacote_1.modulo1 import variavel1  #Como esse import já está sendo feito no modulo2, não é mais necessário
from pacote_2.modulo2 import variavel2

# print(variavel1)
print(variavel2)

import sys  # Uma forma de saber o que pode ser importado

print(sys.path)  # Gera uma lista com todos os caminhos onde o Python busca módulos