"""
Métodos Mágicos: Começam e terminam com __
Eles modificam o compotamento da sua classe
"""

class A:

    def __init__(self):  
        print('Eu sou o INIT')

    def __call__(self,*args,**kwargs):  # Esse método faz a classe funcionar como uma função
        resultado = 1

        for i in args:
            resultado *= i
        
        return resultado
    
    def fala_oi(self):
        print('Fala oi.')
    
    def __setattr__(self,key,value):  # Toda vez que um atributo for configurado na classe, ele será chamado
        
        if key == 'nome':  # Interceptando a tentativa de criar o atributo nome
            self.__dict__[key] = 'Você não pode fazer isso'
        else:
            self.__dict__[key] = value
    
    def __del__(self):  # Evitar tentar usar esse método
        print('Objeto coletado.')  # Mostra que o objeto foi coletado da memória

    def __str__(self):
        return '<class A>'

    def __len__(self):
        return 55

a = A()
variavel = a(1,2,3,4,5,6,7,8,9,10)
print(variavel)

a.fala_oi()

a.nome = 'Eduarda'
print(a.nome)

a.qualquer = 'Setei Qualquer'
print(a.qualquer)

print(len(a))
