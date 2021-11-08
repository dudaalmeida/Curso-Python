"""
Formatando valores com modificadores

:s - Texto (Strings)
:d - Inteiros (int)
:f - Números com ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPOP - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = "Eduarda almeida"
print(f'{nome:s}')

print(f'{num1:0>10}')  ## A variável deve ter 10 casas, então o restante será preenchido com zeros a esquerda

num3 = 1150
print(f'{num3:0<10}')  ## A variável deve ter 10 casas, então o restante será preenchido com zeros a direita
print(f'{num3:0^10}')  ## A variável deve ter 10 casas, então o restante será preenchido com zeros no centro
print(f'{num3:0>10.2f}')  ## A variável deve ter 10 casas, então o restante será preenchido com zeros a esquerda, contando com as casa decimais

nome2 = 'Otávio Miranda'
print(f'{nome2:|^50}')

nome_formatado = '{:@>50}'.format(nome)  ## Preenche com @ até bater 50 (a esquerda)
nome_formatado2 = '{n}{n}{n}{n}'.format(n=nome)
print(nome_formatado)
print(nome_formatado2)

sobrenome = 'Almeida'

nome_formatado2 = '{0:$^50} {1:#^50}'.format(nome, sobrenome)  ## Passando o índice do nome e do sobrenome
print(nome_formatado2)

print(nome.ljust(20,'$'))  ## Justifica o nome completando ele com "$"
print(nome.lower())  ## Tudo minúsculo
print(nome.upper())  ## Tudo maiúsculo
print(nome.title())  ## Primeiras letrasa maiúsculas