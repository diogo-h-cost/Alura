class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f"O titular {self.__titular} tem o saldo de ${self.__saldo}")

    def __pode_sacar(self, valor_sacar):
        disp_saque = self.__saldo + self.__limite
        return valor_sacar <= disp_saque

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property #Metodo de leitura GETTERS
    def titular(self):
        return self.__titular.upper()

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter #Metodo de modificacao SETTERS
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return "001"
    
    @staticmethod
    def cod_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}