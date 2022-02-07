from itertools import groupby, tee  # Necessita que os dados estejam ordenados

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduarda', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
    {'nome': 'Joe', 'nota': 'B'},
    {'nome': 'Joseph', 'nota': 'A'},
    {'nome': 'Dilmas', 'nota': 'B'},
    {'nome': 'Harry', 'nota': 'B'},
    {'nome': 'Hermione', 'nota': 'A'},
    {'nome': 'Rony', 'nota': 'B'},
    {'nome': 'Draco', 'nota': 'B'},
    {'nome': 'Percy', 'nota': 'B'},
    {'nome': 'Fred', 'nota': 'A'},
    {'nome': 'George', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)  # Ordena por nota
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:  # Valores agrupados gera um iterador, ou seja, ele é esgotável
    va1, va2 = tee(valores_agrupados)          # Faz duas cópias do iterador, va1 e va2

    print(f'Agrupamento:{agrupamento}')        # Printa qual o agrupamento

    for aluno in va1:   # Utiliza cópia 1 do iterador
        print(f'\t{aluno}')

    quantidade = len(list(va2))  # Quantidade de alunos de obteve cada nota
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

    