from typing import NoReturn


num_1 = input("Digite:" )
num_2 = input("Digite:" )

## funções para identificar números: isnumeric, isdigit e isdecimal

#print(num_2.isnumeric())
#print(num_1.isnumeric())

# isnumeric(): irá retornar true se todos os caracteres da string são decimais, só números positivos

if(num_1.isdigit() and num_2.isdigit()):
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1+num_2)
else:
    print('Não pude converter os números para realizar contas')