from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

#print(escritor.nome)
#print(caneta.marca)
#maquina.escrever()

# Associando Classes
escritor.ferramenta = caneta # Associando com a classe caneta - Está enviando a classe inteira para o atributo
escritor.ferramenta.escrever()

escritor.ferramenta = maquina # Associando com a classe máquina de escrever
escritor.ferramenta.escrever()

# Se a classe Escritor deixasse de existir, as outras classes ainda existiriam

del escritor  # Apagou o escritor
#print(escritor)  # Vai dar erro porque a classe deixou de existir
print(caneta.marca)  # Caneta ainda pode ser usado por outras classes
maquina.escrever()