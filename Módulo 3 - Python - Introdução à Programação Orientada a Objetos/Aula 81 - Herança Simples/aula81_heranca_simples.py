from classes import *

"""
Associanção - Usa | Agregação - Tem | Composição - É dono | Herança - É

"""

c1 = Cliente('Eduarda',21)
c1.falar()  # Mas o método Falar é de todos
c1.comprar()
# c1.estudar()  # Não existe esse método em Cliente

a1 = Aluno('Maria',55)
a1.falar()
a1.estudar()
# a1.comprar  # Não existe esse método em Aluno

# E nada impede de instanciar uma pessoa
p1 = Pessoa('João',18)
p1.falar()  # Único método da classe Pessoa