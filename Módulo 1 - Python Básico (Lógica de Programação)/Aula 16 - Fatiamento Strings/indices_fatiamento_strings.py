"""
Funções built in

https://docs.python.org/3/library/stdtypes.html (tipos built in)
https://docs.python.org/3/library/functions.html (funções built in)

"""


# positivos    [012345678]
texto        = 'Python S2'
# negativos   -[987654321]

print(texto[3])  ## Acessar o indice indicado do caracter da string (positivo)
print(texto[-2])  ## (negativo)

string = texto[3:7]  ## Endereçar exatemente quais elementos deseja da string, fatiando ela
## espaço embraco não é incluido, no caso do indice 5

print(string)

string = texto[:6]  ## Vai do inicio até o caracter 6

print(string)

string = texto[6:]  # Vai do caracter 6 até o último

print(string)

## O mesmo vale para os indices negativos

string = texto[-9:-3]

print(string)

string = texto[:-1] ## pode ser usado para excluir caracteres

print(string)

## pode ser usado para saltos também

string = texto[0:6:2]  ## [inicio:final:passo]

print(string)

string = texto[0::3]  ## vai até o final com o passo do igual ao segundo valor

print(string)

print(len(texto))


