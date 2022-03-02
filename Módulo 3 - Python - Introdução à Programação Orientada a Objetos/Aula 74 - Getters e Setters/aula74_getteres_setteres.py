# Um getter obtém um valor - Deve manter o nome da variável que será alterada
# Um setter configura um valor
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))
    
    # Getter
    @property
    def preco(self):
        return self._preco  # Convenção de colocar o '_' do nome da variável para evitar loop

    # Setter
    @preco.setter
    def preco(self, valor):  # 'valor' é o que será atribuido para a variável
        if isinstance(valor, str):  # Checando se é uma instância de string
            valor = float(valor.replace('R$',''))  # Retira a moeda e faz um casting para converter a string em número

        self._preco = valor
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()  # Faz com que somente a primera letra seja maiúscula

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome,p1.preco)

p2 = Produto('caneca','R$15')
p2.desconto(10)
print(p2.nome,p2.preco)

