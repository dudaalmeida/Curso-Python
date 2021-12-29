
nome = input('Qual o seu nome: ')

### método mão grande
if nome:
    print(nome)
else:
    print('Você não digitou nada')

### Operador OR
print(nome or 'Você não digitou nada')  ## Se 'nome' tiver algum valor diferente de vazio, ela será exibida. Do contrário, exibe a mensagem depois do OR

print(nome or None or False or 0 or 'Você não digitou nada!' or 'Outra coisa')  #Ele irá parar na primeira expressão verdadeira que achar

### Exemplo 2
a = 0       # Retorna Falso
b = None    # Retorna Falso
c = False   # Retorna Falso
d = []      # Retorna Falso
e = {}      # Retorna Falso
f = 22      # Retorna Verdadeiro
g = 'Luiz'  # Retorna Verdadeiro

variavel = a or b or c or d or e or g or f
print(variavel)