x = 0

while x<6:
    x = x + 1
    if(x == 2):
        continue  ## Pula para o próximo laço, não executando as linhas posteriomes a palavra
    if(x == 4):
        break  ## Sai do laço
    #print(x)

x = 0
while x < 10:
    y = 0
    while y < 5:
        #print(f' x vale {x} e y vale {y}') 
        y += 1
    x +=1


while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    op = input('Digite o operador: ')
    sair = input('Deseja sair? [s]sim ou [n]não: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    if sair == 's':
        break

    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        print(num1+num2)
    elif op == '-':
        print(num1-num2)
    elif op == '/':
        print(num1/num2)
    elif op == '*':
        print(num1*num2)
    else:
        print('OPERADOR INVÁLIDO. ')