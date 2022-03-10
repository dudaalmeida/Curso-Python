from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self,nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado.'
            self.log_info(info)
            print(info)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return

        info = 'O aparelho agora está conectado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._conectado} não está conectado.'
            print(error)
            self.logo_error(error)
            return
        
        info = 'Aparelho foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False