usuario = input('Digite seu usuário: ')

qtd_caracteres = len(usuario)

# print(usuario, qtd_caracteres, type(qtd_caracteres))

"""
if qtd_caracteres < 6:
    print('Você deve digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')
"""

string1 = input('Digite alguma coisa: ')
string2 = input('Digite alguma coisa: ')

print(f'A quantidade total de caracteres foi: {len(string1)+len(string2)}')

print(len(string1))
print(string1.__len__())  # Função len

# A função len não funciona com números