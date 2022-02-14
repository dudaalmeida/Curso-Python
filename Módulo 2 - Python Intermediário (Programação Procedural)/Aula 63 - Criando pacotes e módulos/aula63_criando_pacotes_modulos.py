# import vendas.calc_precos  # Forma de importar o pacote e o módulo dentro dele
# from vendas import calc_precos  # Outra forma de importar que reduz melhor o código
from vendas.calc_precos import aumento, reducao  # Forma mais curta de todas

import vendas.formata.preco as formata
#import vendas.formata import preco as preco2


preco = 49.90
#preco_com_aumento = vendas.calc_precos.aumento(valor=preco, porcentagem=15)
#preco_com_aumento = calc_precos.aumento(valor=preco, porcentagem=15)
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco,porcentagem=15, formata=True)
print(preco_com_reducao)

print(formata.real(preco))