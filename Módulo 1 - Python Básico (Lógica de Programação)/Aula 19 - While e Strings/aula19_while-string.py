frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
new_string = ''
letra = ''
c = 0

input_user = input('Qual letra deseja colocar maiuscula: ')

while c < tamanho:
    ## print(frase[c])
    letra = frase[c]
    if letra == input_user:
        new_string += input_user.upper()
    else:    
        new_string += letra
    c += 1

print(new_string)