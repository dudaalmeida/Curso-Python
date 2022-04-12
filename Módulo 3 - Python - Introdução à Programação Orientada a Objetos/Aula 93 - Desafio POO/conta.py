from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('O valor do depósito precisa ser numérico.')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('O valor do depósito precisa ser numérico.')
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print('-------------------------')
        print(f'Agencia: {self.agencia} ')
        print(f'Conta: {self.conta} ')
        print(f'Saldo: {self.saldo} ')
        print('--------------------------')

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self,valor):
        if not isinstance(valor, (int,float)):
            raise ('O valor deve ser numérico')
        
        if (self.saldo + self.limite) < valor:
            print('Saldo Insuficiente.')
            return
        
        self.saldo -= valor
        self.detalhes()

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('O valor deve ser numérico.')
    
        if self.saldo < valor:
            print('Saldo Insuficiente.')
            return
        
        self.saldo -= valor
        self.detalhes()
