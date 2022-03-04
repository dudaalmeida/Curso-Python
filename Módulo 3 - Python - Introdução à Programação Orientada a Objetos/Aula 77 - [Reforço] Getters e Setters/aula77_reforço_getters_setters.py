# SETTER = Configurando um valor (=)
# GETTER = Obter um valor - Retornar o valor daquela coisa que foi configurada no Setter (.)
# O Getter pode existir sem o Setter, mas não o contrário
# Geralmente em Python, getters e setters são utilizados quando o código está sendo refatorado

class Pessoa:

    def __init__(self, nome):
        #self.atributo = 'inicial'  # Não certo esse atributo estar disponível fora da classe
        self._nome = nome  # O '_nome' é quem sustenta o valor e o getter é uma função que obtém o valor do atributo que possui o '_' e o setter é a função que configura o valor do atributo com '_'

    @property
    def nome(self):
        #return self.atributo
        return self._nome

    # Para criar um setter em Python: 
    # Pegar o nome de algum método que foi usado como @property e colocar '.setter'
    @nome.setter
    def nome(self, nome):  # A função será na mesma estrutura do getter, porém, recebendo um parâmetro para alterar
        #self.atributo = nome  # Esse atributo só serve para salvar o valor que for usado no setter e no getter
        #print('O SETTER FOI EXECUTADO')
        self._nome = nome
    
    @property  # São decoradores que permitem que se coloque o mesmo nome na função
    def sobrenome(self):
        return 'DESCONHECIDO'

p1 = Pessoa('Jonas')
#p1.nome = 'João'  # O que vai acontecer: Eu vou passar no setter, vou configurar o atributo e quando chamar p1.atributo, será visto 'João'
#print(p1.atributo)
print(p1.nome)  # Não põe parêntesis porque é desejado que a função se comporte como atributo
print(p1.sobrenome)