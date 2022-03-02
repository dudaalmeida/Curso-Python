# Métodos estáticos
from random import randint
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):  
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):  # Método de Instância
        print(self.ano_atual - self.idade)
    
    
    @classmethod  # Método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento): 
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Método Estático
    @staticmethod  # Não precisa nem da instância nem da classe
    def gera_id():  # Funciona como uma função que existe fora da classe, mas por questão de organização, ela precisa ficar dentro da classe
        rand = randint(10000, 19999)
        return rand
    

p1 = Pessoa('Eduarda', 21)  # Método de Instância
p2 = Pessoa.por_ano_nascimento('João', 1997)  # Através do Método de Classe, o objeto é fabricado
#p2 = Pessoa('João',25)

print(p2)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())  # Funciona normalmente utilizando a instância 