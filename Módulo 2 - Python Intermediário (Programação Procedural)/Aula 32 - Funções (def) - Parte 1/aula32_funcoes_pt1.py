"""
Funções - def em Python (Parte 1)
"""

def funcao(msg='Olá', nome='usuário', outro=None):
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    #print(msg,nome)
    return f'{msg} {nome} {outro}'

variavel = funcao()
print(variavel)
variavel = funcao('Hello', 'Duda')
print(variavel)
variavel = funcao(nome='Joseph')
print(variavel)
variavel = funcao(nome='Mary',msg='Hi,',outro='Outro')
print(variavel)
