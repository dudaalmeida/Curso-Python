"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'
new_string = ''

#for n,letra in enumerate(texto):
#    print(n, letra)

for n in range(3,10,2):
    print(n)

for n in range(50,10,-2):
    print(n)

print('##############################')
 
for n in range(100):
    if n%8 == 0:
        print(n)

for letra in texto:
    if letra == 't':
        continue  ## Pula o T
        new_string += letra.upper()
    elif letra == 'h':
        new_string += letra.upper()
        break ## termina o laço a partir daqui
    else:
        new_string += letra

print(new_string)

# continue - pula para o próximo laço
# break - termina a iteração