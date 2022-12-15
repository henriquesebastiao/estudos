# Crie uma classe para implementar uma conta corrente

class ContaCorrente:
    def __init__(self, conta, titular, saldo=0):
        self.conta = conta
        self.titular = titular
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.titular = nome

    def deposito(self, valor):
        self.saldo += valor
        print(f"A quantia de {valor}, foi depositada com sucesso!")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"A quantidade de {valor}, foi sacada com sucesso!")
        else:
            print("Não há dinheiro suficiente na conta para saque.")
