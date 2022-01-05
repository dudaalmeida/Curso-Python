"""
Funções - def em Python - Escopo de variáveis (Parte 4)
"""

# Variavel de escopo global
var = 'valor'

def function():
    var = 'Outro valor'  # Editando a variavel de dentro da função, ela não é editada no escopo global
                         # Ela foi criada dentro do escopo local da função, sendo agora uma nova variável, não mais a mesma
    print(var)  # A variável vai estar disponível

def function2():
    print(var)

def function3():
    # Não é uma boa prática, mas caso queira alterar o valor de uma variavel global dentro de uma função, é necessário informar que ela é global
    global var      # Agora a variavel global declarada pode ser editada
    var = 'Novo valor'
    print(var)

# Uma forma de uilizar o valor da variavel global sem alterá-la
def function4(arg=None):
    arg = arg.replace('v','c')
    outra_var = 'New'
    return arg

def function5():
    # Não é possível tentar utilizar uma variável global, depois mudar o valor dela dentro da função e ainda usar ela de novo
    #print(var)  # Ao fazer isso, ele só vai considerar a variavel local e vai acusar que está tentando utilizar a variavel local antes de declarar o valor
    var = 1234
    print(var)
    #print(outra_var)  # Não é possível acessar uma variavel local de outra função
    return var

def function6(args):
    print(args)

function()
function2()
function3()
outra_variavel = function4(arg=var)
novo = function5()  # Mas dessa forma é possível acessar a variavél craida localmente
function6(novo)

print(var)
print(outra_variavel)