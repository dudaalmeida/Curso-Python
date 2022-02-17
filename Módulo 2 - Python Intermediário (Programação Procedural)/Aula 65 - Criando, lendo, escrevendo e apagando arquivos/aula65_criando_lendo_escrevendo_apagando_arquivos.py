# Como, na primeira execução, o arquivo citado abaixo não existe, ele será criado pelo código
file = open('abc.txt','w+')  # 'w+' significa leitura e escrita. Ela também limpa o arquivo e começamos a escreve nele zerado.
file.write('Linha 1 \n')   # Escrever coisas no arquivo
file.write('Linha 2 \n')   
file.write('Linha 3 \n')  

file.seek(0,0)  # Para retornar o cursor para o inicio do arquivo. ParÂmentros, offset que é a posição e o whence que é a relatividade de onde você está procurando 
# 0,0 para pegar a posição absoluta
print('Lendo linhas')
print(file.read())  # Lê o arquivo inteiro e retorna uma string
# Mas dessa forma não funciona sem a função .seek()

print('#'*90)

file.seek(0,0)  # Retornar o cursor a posição inicial de novo
# Outro modo de leitura é linha por linha
print(file.readline(), end='')  # Lê uma linha por vez. O "end=''" é para ele não mandar por padrão uma quebra de linha no fim do arquivo
print(file.readline(), end='')  # Ao utilizar essa função novamente, o cursor continuará de onde ele parou, lendo agora a linha 2
print(file.readline(), end='')

print('#'*90)

file.seek(0,0)

# Também é possível jogar linha por linha em uma lista
# print(file.readlines())  # Um for é uma opção melhor

for linha in file.readlines():   # Fazer 'for linha in file:' também funciona
    print(linha, end='')

file.close()  # Importante sempre fechar o arquivo para evitar erros

####################################################################################
# Outra maneira de abertura de arquivo - Mas não é a melhor maneira

try:
    file = open('abc.txt','+w')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

print('-'*90)

####################################################################################
# Utilizando gerenciadores de contexto

print('"+w": Apagando o arquivo e reescrevendo')

with open('abcd.txt','+w') as file2:
    file2.write('Linha 1\n')
    file2.write('Linha 2\n')
    file2.write('Linha 3\n')

    file2.seek(0)
    print(file2.read())

print()

print('"r": Apenas lendo o arquivo')

with open('abcd.txt','r') as file2:   # Agora, é só leitura
    print(file2.read())

print()

print('"a+": Adiciona coisas no arquivo sem apagar ele por completo')

with open('abcd.txt','a+') as file2:   # Adiciona coisas no arquivo sem apagar ele por completo, colocando o cursor no final do arquivo
    file2.write('Outra Linha')
    file2.seek(0)
    print(file2.read())

print()

print('"w+": Apagando tudo que está dentro do arquivo e adicionando o que tem no código')

with open('abcd.txt','w+') as file2:   # Apaga tudo que está dentro dentro do arquivo, e vai criar a linha abaixo
    file2.write('Outra Linha\n')
    file2.seek(0)
    print(file2.read())

print()
print('-'*90)

####################################################################################################
# Para apagar arquivos

import os

os.remove('abc.txt')  # Apagar o arquivo criado
# os.remove('abcd.txt') 

###################################################################################################
# Arquivo json

import json

d1 = {
    'Pessoa 1':{
        'nome': 'Luiz',
        'idade': 25,
    },
     'Pessoa 2':{
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)  # Convertendo o arquivo para json

with open('abc.json','w+') as file3:
    file3.write(d1_json)

print(d1_json)