
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")  # sempre captura string

ano_nascimento = 2021 - int(idade)  # Casting da idade que era string para inteiro

print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {ano_nascimento}')

