nome = 'Luiz'
idade = 32
altura = 1.8
peso = 80
ano_atual = 2021

ano_nasc = ano_atual - idade
imc = peso/(altura**2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')
