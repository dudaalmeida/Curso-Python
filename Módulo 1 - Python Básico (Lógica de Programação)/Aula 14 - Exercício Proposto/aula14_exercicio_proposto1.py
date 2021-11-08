import re

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
num = input('Por favor, digite um número inteiro: ')

if(is_int(num)):
    if(int(num)%2 == 0):
        print('É um número inteiro par')
    else:
        print('É um número inteiro impar')
else:
    print('O valor informado não é um número inteiro')   