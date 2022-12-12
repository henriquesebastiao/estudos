class Conta:
    # A função __init__ é um método especial que é chamado (altomaticamente) quando a classe é instanciada
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular}")

    def saca(self, valor):
        self.saldo -= valor
        print(f"Saldo de {self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor
        print(f"Saldo de {self.saldo} do titular {self.titular}")