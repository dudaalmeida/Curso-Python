"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    
    input <- Nova tarefa
"""
lista_tarefas = []
pops = []

def add():
    tarefa = input('Informe a tarefa: ')
    lista_tarefas.append(tarefa)

def show():
    print()
    print('\t ---- Tarefas ----\n')
    for t in lista_tarefas:
        print(f'\t      {t}')
    print()

def undo():
    try:
        pops.append(lista_tarefas.pop())
    except IndexError:
        print('Lista vazia. Tente adicionar uma terefa.')

def redo():
    try:
        lista_tarefas.append(pops.pop())
    except IndexError:
        print('Não há tarefas a serem refeitas')

while 1:
    comando = input('Informe o tipo de operação dentre add, undo, redo, show ou break para encerrar: ')

    if comando == 'add':
        add()
    elif comando == 'undo':
        undo()
    elif comando == 'redo':
        redo()
    elif comando == 'show':
        show()
    elif comando == 'break':
        break
    else:
        print('Comando inválido. Tente novamente.')
