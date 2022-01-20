lista = [
    ('chave', 'valor'),
    ('chave2','valor2'),
]

d1 = {x: y for x,y in lista}  # chave: valor 
# Porém a linha acima funcionaria da mesma forma que o comando: d1 = dict(lista)
print(d1)

d2 = {x: y*2 for x,y in lista}
print(d2)

d3 = {x.upper(): y.upper() for x,y in lista}
print(d3)

d4 = {x: y for x,y in enumerate(range(5))}
print(d4)

d5 = {x for x in range(5)}  # Nesse caso, está sendo analisaado um 'set'
print(d5, type(d5))

d6 = {f'chave_{x}': x**2 for x in range(5)}
print(d6, type(d6))