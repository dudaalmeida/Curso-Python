
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nome} falando...')
    
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando.')
    
    def falar(self):
        print('Estou em Cliente')


class ClienteVIP(Cliente):  # Também é um Cliente e um Pessoa
    
    #def falar(self):  # Agora o método da classe Pessoa foi sobreposto
    #    super().falar()  # Mas se eu quiser que o método da classe pai (ou imediatamente superior) seja executado primeiro, utilizo d palavra super() referenciando a classe que eu quero
    #    Pessoa.falar(self)  #Dessa forma, se referencia a classe de que virá o método
    #    print('Falando diferente.')
    
    def __init__(self, nome, idade, sobrenome):  # Tem que receber os mesmos parâmetros que receberia no init da classe Pessoa
        super().__init__(nome,idade)  # Para chamar o método que já está pronto, repassando os parâmetros de Pessoa
        #Pessoa.__init__(nome,idade)  # Também funciona para aproveitar o método

        self.sobrenome = sobrenome

    def falar(self):  # Irá executar o falar de Pessoa, de Cliente e por último, o de ClienteVIP
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')