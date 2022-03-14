class TaErradoError(Exception): # Herdar da classe exception
    pass

def testar():
    raise TaErradoError('Errado')

#testar()  # Levantando o erro

try:
    testar()
except TaErradoError as error:  #Tratando o erro criado
    print(f'Error:{error}')
