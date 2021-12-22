nome = 'Eduarda'
idade = 21
altura = 1.63
e_maior = idade > 18
peso = 60
imc = peso/(altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)

print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}') # o 'f' ativa o fstrings

print('{} tem {} anos e seu IMC é {:.2f}'.format(nome,idade,imc))

print('{0} {0} {0} tem {1} anos e seu IMC é {2}'.format(nome,idade,imc))

print('{n} tem {i} anos e seu IMC é {im:.2f}'.format(n=nome,i=idade,im=imc))