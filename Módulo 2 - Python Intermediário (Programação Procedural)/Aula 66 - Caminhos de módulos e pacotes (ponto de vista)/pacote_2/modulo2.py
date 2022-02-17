# Executar esse arquivo sem o código abaixo gera um erro 
# Isso ocorre porque a leitura do arquivo de entrada é feita para frente. No caso, o arquivo de entrada é "aula66_caminhos_modulos_pacotes.py"
# Se fizer o modulo2 ser a entrada, o arquivo não será rodado pois não existe forma de importar arquivos que estão 'para trás' do arquivo de entrada, que estão antes deles

# Mas existe uma maneira de resolver esse problema de importação
# Pasta tests - é uma pasta separada onde serão colocados todos os testes feitos
# Dessa forma, é manipulado path de todos os arquivos dessa pasta para os arquivos desejados para importação

try:
    import sys
    import os
    sys.path.append(         # Adicionar o caminho completo da pasta anterior, a pasta acima da pasta módulo
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'        # '../../'  se eu quiser adicionar mais uma pasta acima, assim por diante
            ) 
        )
    )
except ImportError:
    raise

# Agora a importação funciona

# Importando um módulo dentro do outro
# Ponto de vista que devo analisar é a entrada do programa
from pacote_1.modulo1 import variavel1
variavel2 = 'variavel2'

print(variavel1)



