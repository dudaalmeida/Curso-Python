"""
Encapsulamento meio que esconde determinadas partes de seu código com o intuito de proteger a sua aplicação

Na programação orientada a objetos clássica, existem modificadores de acesso
Com métodos e atributos públicos: public, protected e private
-> public - Métodos e atributos que podem ser acessados dentro e fora da classe
-> protected - Métodos e atributos que podem ser acessados apenas dentro da classe ou das 'filhas' daquela classe
-> private - Método ou atributos que só estão disponíveis dentro da classe

No Python: 

_  - private/protected (mas na verdade é public com _ no nome)-> Só que ele é fraco e ainda é possível acessar os dados se digitar o nome correto, assim como configurá-lo (Em alguns lugares, isso é chamado de protected)
__ - private, só que mais forte. Proíbe acessar esse método/atributo. Pode acessar e modificar com _NOMEDACLASSE__nomeatributo

A convenção diz para ninguém alterar esse atributo se tiver _ ou __

"""

class BaseDeDados:
    def __init__(self):  # Em Python, o __init__ é coisa mais próxima que existe de um construtor
        self.__dados = {}  # 'coração' da classe. O fato de que ele estava público foi um problema
        # No Python há uma convenção de que se existir um '_' na frente do atributo, recomenda-se que ele não seja acessado
        # Com __ ele não será acessaado de jeito nenhum

    # Se eu quiser liberar o acesso da variável __dados:
    @property
    def dados(self):  # Está fazendo um método da classe parecer uma propriedade da classe
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes'not in self.__dados:  # Na primeira vez que isso for usado, será criado o dicionário
            self.__dados['clientes'] = {id:nome}
        else:                            # Nas próximas vezes, esse dicionário será atualizado, sendo inseridos novos __dados
            self.__dados['clientes'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

#bd.dados = 'Uma outra coisa'  # Fazer isso irá quebrar todos os métodos criados anteriomentes (No caso de estar sem o underline)

bd.__dados = 'Uma outra coisa'  # Nesse caso, o Python acessa um recurso onde ele renomeia o atributo/método com o nome da classe e cria esse novo.
# Nessa situação, o código não quebra mais

print(bd.__dados)  # Será printado 'Uma outra coisa'
# Isso ocorreu justamente porque ele foi criado na linha 43. Ele não é mesmo que está dentro do escopo da classe

# Se quiser ver o atributo real, deverá ser feito:
print(bd._BaseDeDados__dados)

#bd.apaga_cliente(2)
bd.lista_clientes()

print(bd.dados)  # Com método getter, agora é possível acessar diretamente o valor da variável

# Se fosse criado um setter, também teria a possibilidade de alteração
