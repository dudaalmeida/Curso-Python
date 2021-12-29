"""
Operador ternário em Python
"""

logged_user = False

### Modo comum ##########################################################################

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

### Utilizando operador ternário ########################################################
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

### Exemplo 2 ###########################################################################
idade = input('Qual a sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade>=18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    print(msg)
