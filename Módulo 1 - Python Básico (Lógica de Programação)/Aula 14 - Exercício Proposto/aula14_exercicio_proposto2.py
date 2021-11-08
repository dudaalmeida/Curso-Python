import re

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
num = input('Por favor, informe qual a hora (0-23)h :')

if(is_int(num)):
    num = int(num)
    if(num >= 0 and num <= 11):
        print('Bom dia!')
    elif(num >= 12 and num <= 17):
        print('Boa tarde!')
    elif(num >= 18 and num <= 23):
        print('Boa noite!')
    else:
        print('O número informado não corresponde a nenhuma hora do dia')
else:
    print('O valor não corresponde a uma hora do dia')   