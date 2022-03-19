#arquivo = open('abc.txt','w')
#arquivo.write('Alguma coisa.')
#arquivo.close()  # É muito importante fechar os arquivos

# Uma forma que os desenvolvedores do Python encontraram para solucionar foi:

#with open('abc.txt','w') as arquivo:
#    arquivo.write('Alguma coisa.')

# Agora não é necessário mais o close
# O Python permite criar o próprio gerenciador de contexto

class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):  # Tenho que retornar o que vai para a variável arquivo
        print('Retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):  # As últimas 3 variáveis só serão utilizadas no caso de uma excessão
        print('Fechando arquivo')
        self.arquivo.close()
        print(exc_type)  # Tipo da excessão
        print(exc_val)   # O valor que estamos trabalhando
        print(exc_tb)    # O traceback da excessão
        return True      # A excessão não será levantada -> Mas se deve tratar a excessão

with Arquivo('abc.txt','w') as arquivo:
    arquivo.write('Alguma coisa.')
    #arquivo.asasasasd('Alguma coisa.')