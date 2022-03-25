"""Documentação deste modulo

Ele não faz nada, é apenas um exemplo
Typing - https://docs.python.org/3/library/typing.html
"""

x: int = 10
y: float = 9.9
z: bool = False

# É possível especificar o tipo de retorno usando '-> (tipo)' 
def funcao(p1: float,p2: str,p3: dict) -> float:  # É possível especificar o tipo de cada parâmetro recebi pela função
    return 10.1

print(funcao(1.1,'string', {}))

from typing import Union

def funcao1() -> Union[list,dict]:  # Para funções que retornam mais de um tipo de valor -> Retorna uma lista ou um dicionário
    return []

print(funcao1())


