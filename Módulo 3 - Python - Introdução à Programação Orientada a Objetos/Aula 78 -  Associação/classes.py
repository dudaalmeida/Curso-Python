
class Escritor:
    def __init__(self,nome):
        self.__nome = nome  # Atributo privado -> Meu construtor está fazendo o trabalho de setter
        self.__ferramenta = None
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self,marca):
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('A caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('A máquina está escrevendo...')

