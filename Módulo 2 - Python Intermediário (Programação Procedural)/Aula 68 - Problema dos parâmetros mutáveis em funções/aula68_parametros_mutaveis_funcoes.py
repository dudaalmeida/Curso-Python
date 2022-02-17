# Problema da função possuir um argumento com algo mutável. Ex.: Listas, dicionários...
# Objetos imutáveis: strings, números, True, False, None

# O Python avalia os argumentos da função um única vez, de forma que se não for passada uma lista no segundo argumento, ele irá utilizar a lista padrão da função
def lista_de_clientes(clientes_iteravel, lista=None):  # Eu mando uma lista e se já tiver uma lista, essas duas listas são unidas dentro da função
    if lista is None:  # Se o argumento não foi enviado
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_clientes1 = ['Fabrício']
#clientes1 = lista_de_clientes(['João', 'Maria', 'Eduarda'], lista_clientes1)  # Resolveria parcialmente o problema, pois as outras listas continuariam com o mesmo problema
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduarda'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes2 = lista_de_clientes(['José', 'Mariana', 'Francisco'])

print(clientes1)
print(clientes2)

# Em resumo, não se deve utilizar parâmetros mutáveis como argumentos de uma função