"""
Módulos padrão do Python:
Módulos são arquivos .py (que contém código python) e servem para expandir
as funcionalidades padrão da linguagem.

Veja todos os módulos padrão do Python em;
https://docs.python.org/3/py-modindex.html
"""
# Uma forma de importar o módulo
from sys import platform as so # é uma forma de especificar o que deve ser importado do módulo sys
# O 'as' serve para colocar um apelido 
# import sys  # Importando o módulo sys

# Se for importado só o platform, não será necessário colocar sys.
print(so)  # Informa qual plataforma, ex.: windowws ou linux

#----------------------------------------------------------------------

# from random import randint, random  # Esse comando importar mais de uma função do módulo
# from random import *   # Esse comando faz importar tudo dentro do módulo, o que não é recomendado
from random import randint
# é mais recomendado importar o módulo de forma genérica para saber de onde está vindo a função e para evitar sobreposição

for i in range(10):
    print(randint(0,10))  # Gerando um número aleatório entre 0 e 10

# Se o módulo não tiver disponível, é possivel usar a ferramenta 'pip' para instalar o módulo

# Também é possível criar os próprios módulos