"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as 'classes' que criam classes
type é uma metaclasse

É util em Frameworks ou Design Paterns
"""
class Meta(type):  # É possível utilizar 'type' para criar classes
    def __new__(mcs, name, bases, namespace):  # mcs = metaclasses, name = nome da classe, bases = As classes pai das classes que estão sendo criadas, namespace = tem todo o atributo de classe e todo método criado naquela classe
        #print(name)  # Toda classe que for criada a partir dessa metaclasse, será visto o nome dela aqui
        if name ==  'A':  # Não quero que a classe A tenha um comportamento diferente das outras, só as filhas dela
            return type.__new__(mcs, name, bases, namespace)  # Crindo a metaclasse

        #print(namespace)  # Vendo o name da B
        
        if 'b_fala' not in namespace:
            print(f'Oi, você precisa que o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass = Meta):  # Quero que a metaclasse criada seja Meta, se comportando de acordo com o que foi estabelecido nela
    def fala(self):
        self.b_fala()

class B(A):
    
    teste = 'Valor'
    b_fala = 'Wow'

    #def b_fala(self):
    #    print('Oi')

    def sei_la(self):
        pass

b = B()
#b.fala()
