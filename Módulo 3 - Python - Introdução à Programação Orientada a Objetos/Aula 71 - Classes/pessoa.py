from datetime import datetime

# Um método é uma função que pertece a classe
class Pessoa:  # Classe é uma espécie de molde, que nesse caso em específico, pode ser usado para criar várias 'pessoas'
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def teste(self):  # Quando uma função está denntro de uma classe, ela é um método dessa classe
        print('Pessoa está falando...')  # A palavra self serve para referenciar a instância

    # O parâmetro self não precisa ser enviado.
    def __init__(self, nome, idade, comendo=False, falando=False):  # O parâmetro self deve ser enviado obrigatoriamente (por enquanto -> é diferente em métodos estáticos)
        self.nome = nome  # Mesmo tendo o mesmo nome, são variáveis diferentes. é necessária a atribuição
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        variavel = 'Valor'  # Só existe no escopo desse método
        #print(variavel)  # Como o __init__ é chamado semre que instacio a classe, o comando sempre será executado ao rodar o main

    def outro_metodo(self):
        print(self.nome)  # O valor de nome está disponível para outros métodos

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return  # Usando isso, o código irá parar aqui e não executará o que temm abaixo

        if self.falando:
            print(f'Não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True  #Modificando o status pois ao executar essa função, ele passará a 'comer'
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False
    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
