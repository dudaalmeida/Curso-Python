# listas, tuplas, strings -> Sequencias -> Iterável
nome = 'Luiz Otávio'

for letra in nome:
    print(letra)

print('#'*80)

for letra in nome:
    print(letra)

print(nome)

# Geradores e Iteradores: O for converte em tempo de execução a string em um iterador
# O for utilizará o next até o iterador esgotar

iterador = iter(nome)

# Suprimir o erro de quando o iterador esgota
try: 
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

# Não aparecerá nada pois o iterador já foi consumido
for valor in iterador:
    print(valor)

print('Iterador consumido')

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('FOR')

# Aqui ele terminará de consumir o gerador
for letra in gerador:
    print(letra)

# Geradores e iteradores são feitos para os valores deles serem consumidos e depois não usar de novo