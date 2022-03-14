"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (da mesma assinatura) mas comportamentos
diferentes.
Mesma assisnatura =  Mesma quantidade e tipo de parâmetros

Mesmo comportamento da aula anterior onde foi criado o método estático Conta
na superclasse, e as outras classes herdaram e modificaram ela
"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self,msg): pass

class B(A):
    def fala(self,msg):  # Precisa ser de mesma assinatura da Classe A, ou seja, precisa ter os parâmetros self e msg
        print(f'B está falando: msg')

class C(A):
    def fala(self,msg):  # Também é obrigado a ter os parâmetros self e msg
        print(f'C está falando: msg')

# As Classes B e C tem comportamentos diferentes

b = B()
c = C()
b.fala('Um assusnto.')
c.fala('Outro assunto.')

# Esse tipo de polimorfismo é o único que o Python suporta, o polimorfismo de sobreposição.
# Existe o polimorfismo de sobrecarga, mas o Python não suporta
