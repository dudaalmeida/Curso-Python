class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):  # São atributos relacionados a instância
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    # Abaixo é um decorador que está decorando esse método da classe
    @classmethod  # Método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):  # Criei um método que é um método de classe e retorna a própria classe, porém agora com nome e idade com base nos parâmetros enviados
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

p1 = Pessoa('Eduarda', 21)  # Método de Instância
p2 = Pessoa.por_ano_nascimento('João', 1997)  # Através do Método de Classe, o objeto é fabricado
#p2 = Pessoa('João',25)

print(p2)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()