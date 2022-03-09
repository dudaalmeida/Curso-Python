# No caso se composição, uma classe vai ser dona de objetos de outra classe
# Isso quer dizer que se a classe pricipal for apagada, todos os objetos que a classe principal
# utilizou serão apagados vão ser apagados com ela.

# Na composição, uma classe pretence a outra classe.

from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()
del cliente1  # Será apagado o cliente e os endereços que pertecem a esse cliente
print()

cliente2 = Cliente('Maria', 55)
cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()
del cliente2  
print()

cliente3 = Cliente('João', 19)
cliente3.inserir_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
del cliente3  
print()

print('#'*90)

# No momento que um cliente é apagado da memório, todos os endereços também são apagados da memória

