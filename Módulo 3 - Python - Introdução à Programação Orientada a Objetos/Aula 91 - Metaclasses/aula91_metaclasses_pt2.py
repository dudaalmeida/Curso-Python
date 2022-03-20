class Meta(type): 
    def __new__(mcs, name, bases, namespace): 
        if name ==  'A': 
            return type.__new__(mcs, name, bases, namespace) 

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass = Meta):  
    attr_classe = 'Valor A'

class B(A):
   attr_classe = 'Valor B'  # Com o mesmo nome, o 'Valor B' irá sobrepor o 'Valor A' -> Mas a condição na Meta muda isso

class C(B):
       attr_classe = 'Valor C'

#b = B()
#print(b.attr_classe)

c = C()
print(c.attr_classe)
