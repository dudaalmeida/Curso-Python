# Será criada a classe Conta que não desejo que seja instanciada, mas quero especializá-la

from classes.conta_poupança import ContaPoupanca
from classes.conta import Conta
from classes.conta_corrente import ContaCorrente

cp = ContaPoupanca(1111,2222,0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)  # Aqui deve dar saldo insuficiente

#conta = Conta(1111,2222,4)  # Não é possível instanciar a classe abbstrata, somente a especialização dela
print('$'*90)

cc = ContaCorrente(agencia=1234, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)  # Aqui deve dar saldo insuficiente pois estourou o limite
cc.depositar(1000)