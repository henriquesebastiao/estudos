class Conta:
    # A função __init__ é um método especial que é chamado (altomaticamente) quando a classe é instanciada
    def __init__(self, numero, titular, saldo, limite):
        # Colocar o __ antes do nome da variável torna ela privada
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def saca(self, valor):
        self.__saldo -= valor
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")