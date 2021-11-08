nome = input('Informe seu nome: ')

len = len(nome)

if len <= 4:
    print('Seu nome é curto')
elif len >= 5 and len <= 6:
    print('Seu nome é normal')
elif len > 6:
    print('Seu nome é muito grande')