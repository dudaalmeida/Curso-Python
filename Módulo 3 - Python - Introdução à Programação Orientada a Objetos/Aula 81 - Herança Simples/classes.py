# Super classe
class Pessoa:
    # Esse termo abaixo vai se repetir em todas as classes semelhantes, como as classes Aluno e Cliente, que também usa nome e idade
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} falando...')
    # Essa classe estabeleceu todos os métodos genéricos

# Um Cliente é uma Pessoa -  Essa classe é uma subclasse
class Cliente(Pessoa):  # Os parêntesis informam que a classe Cliente herda da classe Pessoa. Herda tudo que tem na classe Pessoa
    def comprar(self):
        print(f'{self.nome} está comprando.')
# Essa classe é uma melhoria, uma especilização da classe Pessoa

# Um Aluno é uma Pessoa
class Aluno(Pessoa):
    def estudar(self):  # Esse atributo não é herdado para Pessoa. Pertence somente a classe Pessoa
        print(f'{self.nome} está estudando.')