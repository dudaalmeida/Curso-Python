from pessoa import Pessoa

p1 = Pessoa('Eduarda',21)  # Criando um objeto a partir de uma classe

p1.comer('hamburguer')
p1.parar_comer()  # Parou de comer
p1.parar_comer()  # Já havia parado de comer
p1.comer('maçã')  # Voltou a comer
p1.falar('POO')   # Tentou falar comendo
p1.parar_comer()  # Parou de comer para falar
p1.falar('POO')   # Agora pode falar
p1.comer('Pêra')  # Tentou comer enquanto fala, mas não é permitido
p1.parar_falar()  # Parou de falar
p1.comer('Pêra')  # Agora pode comer
p1.parar_comer()
p1.parar_falar()
 
#################################################################
print('#'*90)

p2 = Pessoa('Joana',23)

p1.falar('POO')
p2.comer('sorvete')
p1.comer('churrasco')
p1.parar_falar()
p2.parar_comer()

#################################################################
print('#'*90)

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)  # Funciona utilizando até mesmo a clase em si

print(p1.get_ano_nascimento())  # retorna o ano de nascimento da pessoa
print(p2.get_ano_nascimento())
