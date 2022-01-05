"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def divisivel(parametro):
    if parametro%3 == 0:
        if parametro%5 == 0:
            return 'FizzBuzz'
        return 'Fizz'
    elif parametro%5 == 0:
        return 'Buzz'
    
    return parametro

valor = divisivel(25)
print(valor)