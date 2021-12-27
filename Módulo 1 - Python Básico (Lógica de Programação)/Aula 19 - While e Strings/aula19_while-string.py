frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
new_string = ''
c = 0

while c < tamanho:
    #print(frase[c])
    new_string += frase[c]
    c += 1

print(new_string)