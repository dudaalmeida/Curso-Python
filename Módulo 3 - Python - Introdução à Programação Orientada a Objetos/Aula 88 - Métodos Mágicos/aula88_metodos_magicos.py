"""
Métodos Mágicos: Começam e terminam com __
Eles modificam o compotamento da sua classe
"""

class A:

    def __new__(cls,*args,**kwargs):

        if not hasattr(cls,'_jaexiste'):  # Não está criando uma nova instância quando a primeira foi criada
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste        
    
    #def __new__(cls,*args,**kwargs):  # Esse é o 'construtor'
    #    
    #    def haha(*args,**kwargs):
    #        print('Fala Oi!')
    #    
    #    cls.haha = haha
    #    cls.nome = 'Edurda'
#
    #    print('Eu sou o new')
#
    #    return object.__new__(cls)
    #    #return super().__new__(cls)   # Há o super mesmo a classe A não herdando de nada. Em Python, toda classe deriva de object 
    
    def __init__(self):  
        print('Eu sou o INIT')
    
a = A()
#a.haha()
b = A()
c = A()

print(a==b)
print(b==c)
print(a==c)  

print( id(a), id(b), id(c))  # Todos tem o mesmo ID -> São o mesmo objeto