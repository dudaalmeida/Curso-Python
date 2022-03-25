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
class MinhaClasse:
    """Documentação normal

    Conforme qualquer outra documentação que você tenha usado anteriormente.    
    """
    atributo = 1
    atributo2 = 'Valor'

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """

        self.texto = texto
        self.exibe_texto(texto)
    
    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres na tela

        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """

        if not isinstance(texto,str):
            raise TypeError('Texto precisa ser uma string.')
        
        if len(texto) > 100:
            raise ValueError('Texto precisa ter 100 caracteres ou menos.')
        
        return texto

    pass
