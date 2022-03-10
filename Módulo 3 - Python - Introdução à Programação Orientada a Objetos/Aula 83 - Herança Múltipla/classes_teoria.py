class A:
    def falar(self):
        print(f'Falando... Estou em A')

class B(A):  # Herda direto de A
    def falar(self):
        print(f'Falando... Estou em B')

class C(A):  #A pesar de ser de A, ela não está relacionado com B
    def falar(self):
        print(f'Falando... Estou em C')

class D(B,C): # Herança múltipla -> Vai Herdar primeiro de B
# Problema do Diamente: Quando uma classe que tem herança múltipla herda de duas classes que têm o mesmo método
# Quando há herança múltipla então, o Python busca da esquerda para a direita, no momento de herdar primeiro
    #def falar(self):
    #    print('Falando... Estou em D')
    pass

# Geralmente, quando utilizamos herança múltima, utilizamos mixes. Uma classe mixing não é uma classe abstrata.
# Uma classe mixing não foi feita para ser instanciada diretamente. Ela terá uma funcionalidade adicional que eu quero adiconar em outra classe.
# Porém, essa classe mixing não está presente na hierarquia de classes.

a = A()
a.falar()

b = B()
b.falar()

d = D()
d.falar()
