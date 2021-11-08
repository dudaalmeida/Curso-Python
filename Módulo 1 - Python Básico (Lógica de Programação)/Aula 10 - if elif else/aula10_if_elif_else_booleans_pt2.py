"""
Operadores Relacionais
== > >= < <= !=
"""

v = 'valor'  # = é atribuição, == é comparação

num_1 = 3  #int
num_2 = 2  #int

expressao1 = num_1 == num_2
expressao2 = num_1 > num_2
expressao3 = num_1 >= num_2
expressao4 = num_1 != num_2

# print(expressao1)
# print(expressao2)
# print(expressao3)
# print(expressao4)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

idade_menor = 18
idade_maior = 30

if idade>=idade_menor and idade<=idade_maior:
        print(f' {nome} pode pegar o empréstimo')
else:
    print(f' {nome} não pode pegar o empréstimo')
