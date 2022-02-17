# As funções decoradores vão simplesmente envolver as funções que você quiser, dando ou não o comportamento dela se você preferir assim
# Geralmente, ao decorar uma função, deseja-se substituíla por outra

def fala_oi():
    print('Oi')

variavel1 = fala_oi
variavel1()  # É a mesma coisa que fala_oi()

print(type(variavel1))  # Minha variavél é uma função

print('-'*90)
###############################################################

def master(funcao):  # Função decoradora
    def slave(*args, **kwargs):
        #print('Olá')  # O print() teoricamente é uma função que está sendo executada dentro da função slave
        print('Agora estou decorada')
        funcao(*args, **kwargs)
    return slave  # Retorna a função sem executar

# Decorador
@master  # Forma de decorar a função com a função decoradora master()
def fala_ola():
    print('Olá!')

@master
def outra_funcao(msg):
    print(msg)


#variavel = master()
#variavel()  # Seria o mesmo que slave() 
#print(type(variavel))

#fala_ola = master(fala_ola)  # Isso é como se estivesse executando a função diretamente, só que ela foi decorada com a função master, se tornando escrava dela

#fala_ola()

outra_funcao('Olá, eu sou Eduarda')  # Com o @master agora ela está decorada

# Uma função decoradora normalmente é utilizada para adicionar algum recurso na função e afins



