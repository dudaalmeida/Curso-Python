### Método na 'mão grande' ###
x = 10
y = 'Luiz'

z = x
x = y
y = z
print(f'x={x} e y={y}')

### Método prático ###
x = 10
y = 'Luiz'

x,y = y,x
print(f'x={x} e y={y}')

### Método prático - Exemplo 2 ###
x = 10
y = 'Luiz'
z = 'Otávio'

x,y,z = z,x,y
print(f'x={x} , y={y} e z={z}')


