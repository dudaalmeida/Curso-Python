
# Criando uma tupla
t1      =   (1 , 2 , 3,'a','Luiz')
#  indices   0   1   2  3    4

print(t1,type(t1))

for v in t1:  # Iterando printando um elemento por vez
    print(v)

# Também pode ser criada sem os parenteses
t2 = 1,2,3,4,5
print(t2,type(t2))

# Se eu quiser uma tupla com um elemento
t3 = 1,  # Se a virgula não for colocada, ela será considerada um inteiro
print(t3, type(t3))

# É possível concatenar as tuplas
t4 = 1,2,3,4,5
t5 = 6,7,8,9,10
t6 = t4 + t5
print(t6,type(t6))

# É possível desempacotar a tupla em variáveis
t7 = 1,2,'João',4,5
n1, n2, n3, *_, n10  = t7
print(n3)
print(n10)  # Se eu quiser pegar o último valor

# É possível repetir uma tupla com um multiplicador
t8 = (1,2,3,4,5)*20  # Ela será repetida 20 vezes, por exemplo
print(t8)

# Uma tupla pode ser convertida numa lista e dessa forma, pode ser modificada
t9 = (1,2,'Fran','Olá')
t9 = list(t9)  # Converte a tupla em lista

# Uma forma de modificar é fazer a alteração enquanto ela estiver na forma de lista e então convertê-la novamente em tupla
t9[1] = 3000
t9 = tuple(t9)  # Converte a lista em tupla