"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

def juros(num,percent):
    return num*((100+percent)/100)
    
valor = juros(12,10)
print(f'{valor:.3f}')