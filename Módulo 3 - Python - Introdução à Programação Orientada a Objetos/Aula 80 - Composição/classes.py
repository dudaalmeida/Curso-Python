# Cadastro de cleintes numa loja

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    def inserir_endereco(self, cidade, estado):  # Aqui eu recebo a cidade e o estado
        self.enderecos.append(Endereco(cidade, estado))  # E aqui eu repaço a cidade e estado para a classe Endereco
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    def __del__(self):
        print(f'{self.nome} foi apagado.')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado.')

