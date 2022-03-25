"""Descrição rápida e simples

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nibh odio, blandit vel
porta ac, rhoncus congue neque. Nam quis odio in lorem volutpat lobortis. Maecenas magna
lectus, laoreet et dui eu, suscipit tristique nisl. Fusce lobortis sodales elit. Etiam
tincidunt iaculis neque, vitae euismod nunc cursus in. Mauris accumsan sagittis libero,
eget ultricies leo elementum at. Vestibulum id rhoncus dolor. Fusce lobortis justo ornare
quam consectetur auctor. Duis facilisis tincidunt aliquet.

Vestibulum auctor, eros quis feugiat efficitur, sem lorem iaculis lacus, eu viverra diam
mauris sit amet urna. Sed tincidunt molestie augue a volutpat. In vel velit convallis, 
laoreet nulla ac, vestibulum ante. Praesent dui sem, sagittis vel urna vitae, aliquet 
posuere magna. Vivamus ac ex sed risus congue pellentesque. Morbi consectetur ipsum sit 
amet lectus mollis, et egestas nisl gravida. Nunc ante ante, dignissim et auctor eget, 
pharetra et velit. Phasellus enim urna, gravida ac euismod eget, auctor ac purus.

"""

variável1 = 'valor 1'

def soma(x,y):
    """Soma x + y"""
    return x + y

def multicacao(x,y,z=None):
    """Multiplica x, y, z

    Multiplica x, y e z. O programador pode omitir a variavel z caso não tenha
    necessidade de usá-la.
    """
    if z:
        return x * y
    else:
        return x * y * z

variavel2 = 'valor 2'
variavel3 = 'valor 3'
variavel4 = 'valor 4'
