
try:  # Irá tentar rodar o código dentro do try, se ocorrer algum erro, ele irá rodar o código dentro do except
    a={}
    print(a[1])
except NameError as erro:  # É possível explicitar o tipo de erro que será tratado
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:  # Se quiser tratar dois erros na mesma exceção
    print('Erro de índice ou de chave')
except Exception as erro:  # Para o caso de mais algum erro, qualquer um, já que não está especificado
    print('Ocorreu um erro inesperado.')
else:  # Será executado sempre que o bloco try rodar sem nenhuma exceção
    print('Seu código foi executado com sucesso!')
finally:  # Será executada sempre, independente de ter ocorrido um erro ou não
    print('Finalmente.')
    a = '#'

print('O código continua')
print(a)

# Isso permite que o código prossiga normalmente
# Também é possível manter outros blocos try, except dentro uns dos outros
# Além disso, é possível lançar exceções


