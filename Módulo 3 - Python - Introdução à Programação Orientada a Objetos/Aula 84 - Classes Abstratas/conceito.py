"""
-> Uma Classe Abstrata em Python pode ser considerada um projeto para outras classes. 

-> Ele permite que você crie um conjunto de métodos que devem ser criados em qualquer classe 
filha construída a partir da classe abstrata. 

-> Uma classe que contém um ou mais Métodos Abstratos é chamada de Classe Abstrata.

-> Um método abstrato é um método que possui uma declaração, mas não possui uma implementação. 

"""
from abc import ABC, abstractmethod # Abstract Base Class

class A(ABC):  # Até o momento, ao somente herdar a ABC, ainda é possível instanciar a classe -> Só há impedimento se houver um método abstrato dentro da classe
    @abstractmethod
    def falar(self):
        pass

class B(A):  # Essa classe não pode ser instanciada enquanto não existir o método falar
    def falar(self):
        print('Agora estou falando...')

a = B()
a.falar()