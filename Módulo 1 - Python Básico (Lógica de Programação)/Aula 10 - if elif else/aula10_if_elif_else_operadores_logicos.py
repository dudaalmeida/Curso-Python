"""
Operadores Lógicos
and, or, not
in, not in
"""
a = 1
b = 3
c = 10
d = 'mkdsksd'
e = 0

expressao = ((b<3) or (c>a))
print(expressao)

if not b > a:
    print('B é maior que A')
else:
    print('A é maior que B')

if not d:
    print('Por favor, preencha o valor de D')

if not e:
    print('Por favor, preencha o valor de E')

nome = 'Eduarda Almeida'

if 'oto' in nome:
    print('Existe a letra "m" no seu nome')
elif 'ma' not in nome:
    print('"ma" não existe no nome')
else:
    print('Não existe')