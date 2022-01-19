
string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'

"""
Dada a string acima:

Deve ser criada uma lista que separe assim:

lista = ['0123456789','0123456789','0123456789','0123456789',0123456789']

E deve dar um retorno dessa forma:

retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.'

"""
n = 10
lista = [string[i:i+n] for i in range(0,len(string),n)]  # Foi para definir os indices de fatiamento, algo semelhante a string[0:10] para fatiar por exemplo 0123456789, só que de forma automatizada
print(lista)
retorno = '.'.join(lista)  # Inserir o '.' como separador
print(retorno)