
def mestre(irmaos, escolas):
    return irmaos(irmao1='Maria', irmao2='Joaquim', irmao3='João'), escolas('Adventista', 'Militar')

def irmaos(*args, **kwargs):
    irmao1 = kwargs.get('irmao1')
    irmao2 = kwargs.get('irmao2')
    irmao3 = kwargs.get('irmao3')
    return f'Seus irmãos são {irmao1}, {irmao2} e {irmao3}.'

def escolas(*args, **kwargs):
    escola1 = args[0]
    escola2 = args[1]
    return f'Eles estudam nas escolas {escola1} e {escola2}.'

info1 , info2 = mestre(irmaos,escolas)
print(info1, info2)

########################################################################################################
## Método do Professor

def master(funcao,*args,**kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi, {nome}!'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}!'

executando = master(fala_oi, 'Luiz')
executando2 = master(saudacao, 'Luiz', saudacao='Bom dia,')
print(executando)
print(executando2)