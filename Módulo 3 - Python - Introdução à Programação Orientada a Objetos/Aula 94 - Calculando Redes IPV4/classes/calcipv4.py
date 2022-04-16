import re

class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self,valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido')

        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)
    
    @mascara.setter
    def mascara(self,valor):
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError('Máscara Inválida.')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')    

    @prefixo.setter
    def prefixo(self,valor):
        if not valor:
            return
        
        if not isinstance(valor,int):
            raise TypeError('Prefixo Inválido.')

        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 bits.')

        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32,'0')  # Zero do lado direito
        if not hasattr(self, 'mascara'):
            self._mascara = self._bin_to_ip(self._mascara_bin)
    
    @staticmethod
    def _valida_ip(ip):  #Valida se o ip está escrito corretamente
        regexp = re.compile(
            r'^(([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}))$'
        )
        if regexp.search(ip):
            return True
    
    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]  # Antes havia a forma binária era '0b111111'. Para tirar esse '0b' foi utilizado o [0:2] e para preecher com zeros foi utilizado o zfill(8)
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+i],2)) for i in range(0,32,n)]
        return '.'.join(blocos)
    
    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self.broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits*'1')
        self._broadcast = self._bin_to_ip(self.broadcast_bin)
        return self._broadcast
    
    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self.rede_bin = self._ip_bin[:self.prefixo] + (host_bits*'0')
        self._rede = self._bin_to_ip(self.rede_bin)
        return self._broadcast
    
    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)