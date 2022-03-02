class A:
    c = 123  # Não é variável de instância

    def __init__(self):
        self.c = 321  # Variável de instância
        # Só que, por conta da variav´rl da classe e da instância rodarem ao mesmo tempo, a variavél 'c' declada aqui ficará só com as instâncias

a1 = A()
a2 = A()

#A.c = 321  # Dessa forma muda para todas as instâncias
#a1.c = 456  # Muda só na instância - Na realidade está criando um atributo na instância


# Primeiro o insterpretador do Python irá buscar na instância se a variável existe, se não existir nela, ele irá procura na classe
print(a1.__dict__)  
print(a2.__dict__)  # Por isso que nesse caso ele não encontrou nada
print(A.__dict__)   # Na classe existe

print()

# Nos 3 casos abaixo, existe o acesso a variável de classe c
print(a1.c)
print(a2.c)
print(A.c)

# Tomar cuidado ao alterar a variável de classe
# Para alterar em todas as instâncias, o ideal é utilizar a classe diretamente para realizar a alteração
A.c = 'Alterado'

print(a1.c)
print(a2.c)
print(A.c)

