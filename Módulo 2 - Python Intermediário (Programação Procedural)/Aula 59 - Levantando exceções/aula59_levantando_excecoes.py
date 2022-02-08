
def divide (n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise  # Dessa maneira, a exceção será relançada e pode ser capturada posteriormente

try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)

print('-'*90)

# Outro caso é criar a própria exceção

def division (n1,n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')  # Levantando a exceção com mensagem própria
    return n1/n2

try:
    print(division(2,0))
except ValueError as error:
    print('Log: ',error)