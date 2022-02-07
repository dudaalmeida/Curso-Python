"""
Combinations, Permutations e Product - Itertools
Combination - Ordem não importa - Não repete
Permutation - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product
# Além de listas, pode ser utilizada com tuplas também ou iteráveis em geral

pessoas = ['Luiz', 'André', 'Eduarda', 'Letícia','Fabrício','Rose']

for grupo in combinations(pessoas,2):  # Grupos de 2
    print(grupo)

print('#'*100)

for grupo in permutations(pessoas,2):  # Grupos de 2, mas agora a ordem importa e agora as combinações repetem, pois são considerados diferentes
    print(grupo)

print('#'*100)

# Mas se eu quiser valores repetidos e a ordem importa, deve ser usado o módulo product

for grupo in product(pessoas,repeat=2):  # Grupos de 2
    print(grupo)