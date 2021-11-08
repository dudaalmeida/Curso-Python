nome = 'Eduarda'
idade = 21
altura = 1.63
e_maior = idade > 18
peso = 60

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade:', e_maior)

print(idade*altura)

# Exercício cálculo IMC

imc = peso/(altura**2)
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)