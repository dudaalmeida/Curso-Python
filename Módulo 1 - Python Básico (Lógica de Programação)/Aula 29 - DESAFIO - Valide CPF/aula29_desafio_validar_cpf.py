"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

while 1:

    cpf = input('Informe seu cpf: ')
    cpf = cpf.strip()
    novo_cpf = ''
    soma = 0

    for v in range(10,12):
        for n,value in enumerate(range(v,1,-1)):  # Gera o index para usar no vetor e os multiplicadores do cálculo
            soma += value*int(cpf[n])             # Inicia a soma do calculo
            verifica = 11 - (soma % 11)
            if v == 10:                           # Armenguezinho para gerar o cpf novo, mas tem uma maneira bem mais simples, como fazer cpf_novo = cpf[:-2]
                novo_cpf += cpf[n]
        soma = 0
        if verifica <= 9:                         # Define os dois últimos digitos do cpf
            novo_cpf += str(verifica)
        elif verifica > 9:
            novo_cpf += '0'

    if cpf == novo_cpf:
        print('CPF válido')
    else:
        print('CPF inválido')

    loop = input('Deseja testar um novo CPF? s-sim ou n-não: ')
    if loop == 'n': 
        break