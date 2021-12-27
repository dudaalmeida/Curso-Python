"""
For / Else em Python
"""

variavel = ['Maria', 'João', 'Ana']

for valor in variavel:
    if valor.lower().startswith('j'):
         continue
    print(valor)
