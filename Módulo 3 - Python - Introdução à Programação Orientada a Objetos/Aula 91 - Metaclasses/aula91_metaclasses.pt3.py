# Utilizando type para criar classes

class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr':'Olá Mundo!'})  #Type é uma metaclasse para criar classes -> Herda de Pai

a = A()
print(A.attr)
print(type(a))  # A 'A' foi criada a partir de type
print(a.nome)