"""
Tipos de Dados

str - string - textos 'Assim' "Assim"
int - inteiro - 123456 - 0 - 10 - 50 - 15000
float - real/ponto flutuante - 10.5 - 1.5 - 10.10
bool - booleano/lógico - true falses

"""

print('Luiz',type('Luiz')) # Informa o tipo da variável
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print(bool())

# Type casting -  Converter umtipo para outro

print('Luiz',type('Luiz'), bool('Luiz'))  # Qualquer valor dentro de uma string é avaliado em verdadeiro
print('10',type('10'),type(int('10')))

# Exercício

print('Eduarda Almeida', type('Eduarda Almeida'))
print(21, type(21))
print(1.63,type(1.63))
print(21 >= 18, type(21 >= 18))
