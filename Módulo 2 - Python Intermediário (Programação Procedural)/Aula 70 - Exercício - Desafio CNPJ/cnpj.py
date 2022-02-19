## Seprar tudo em funções, o máximo possível
# Também fazer uma função que desencadeie outras funções

# import re

def remover_caracteres(cnpj):    # re.sub(r'^0-9','',cnpj)  é uma exxpressão regular que poderia substituir o replace
    cnpj = cnpj.replace('/','')
    cnpj = cnpj.replace('.','')
    cnpj = cnpj.replace('-','')
    return cnpj

def encontrar_digitos(novo_cnpj):
    for i in range(2):

        soma = operacao_digito(novo_cnpj, len(novo_cnpj)+1)
        d = 11 - (soma%11)
        if d >= 9:
            novo_cnpj += '0'
        else:
            novo_cnpj += str(d)
        
    return novo_cnpj

def operacao_digito(novo_cnpj, t):
    produto = []
    multiplicador = ''
    for i in range(t,1,-1):
        if i >= 10:
            i -= 8
        multiplicador += str(i)

    for i in range(t-1):
        produto.append(int(novo_cnpj[i])*int(multiplicador[i]))
    soma = sum([i for i in produto])

    return soma

def valida_cnpj(cnpj):
    cnpj = remover_caracteres(cnpj)
    cnpj_valido = encontrar_digitos(cnpj[:-2])

    if cnpj == cnpj_valido:
        print('O CNPJ informado é válido.')
    else:
        print('CNPJ inválido.')

cnpj = input('Informe seu CNPJ: ')
valida_cnpj(cnpj)