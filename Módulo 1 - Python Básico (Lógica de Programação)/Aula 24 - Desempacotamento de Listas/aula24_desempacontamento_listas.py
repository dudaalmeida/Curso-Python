"""
Desempacotamento de listas em Python
"""

lista = ['Luiz','João','Maria',1,2,3,4,5,5,6,7,7,8,8,9]

n1, n2, *outralista, ultimo = lista  #Foram geradas 2 variaveis para os primeiros indices e o que sobra, ele gera uma outra lista com o resto dos valores. Então a varialvel 'ultimo' pega o ultimo valor

m1, m2, *_ = lista  #O *_ serve para não se preocupar com o restante dos valores

print(n2, n1)
print(outralista)
print(ultimo)

print(m1,m2)