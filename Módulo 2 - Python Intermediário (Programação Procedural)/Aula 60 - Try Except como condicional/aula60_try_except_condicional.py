def converte_numero(valor):
    try:  # tenta converter em número inteiro
        valor = int(valor)
        return valor
    except ValueError:
        try:  # Tenta converter um float
            valor = float(valor)
            return valor
        except:
            pass  # Irá retornar None

while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is None:
        print('Erro: Isso não é número.')
    else:
        print(numero*5)