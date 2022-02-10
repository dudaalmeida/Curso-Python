import math

PI = math.pi  # Para criar uma constante se utiliza o nome com letra maiúcula

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

###  INFORMAÇÃO IMPORTANTE ###
if __name__ == '__main__':  # Se esse módulo estiver sendo importado, não será executada essa parte. Será se tiver sendo executado localmente
    lista = [1,2,3,4,5]

    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
