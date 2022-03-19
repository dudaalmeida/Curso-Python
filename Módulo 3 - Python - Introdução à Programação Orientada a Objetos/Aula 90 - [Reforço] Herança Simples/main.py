# Em teoria, não se pode utilizarum método de uma classe filho numa classe pai
# É possível, porém aumenta a complexidade de seu código

"""
Biblioteca -> chama_metodo_da_interface()
    Interface(Biblioteca)
        metodo_da_interface()

main -> interface
"""

from classes.interface import Interface

i1 = Interface()
i1.chama_metodo_da_interface()