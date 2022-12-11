class Conta:
    # A função __init__ é um método especial que é chamado (altomaticamente) quando a classe é instanciada
    def __init__(self):
        self.numero = int(input("Digite o número da conta: "))
        self.titular = input("Digite o nome do titular: ")
        self.saldo = float(input("Digite o saldo: "))
        self.limite = float(input("Digite o limite: "))
        print(conta.Conta().numero, conta.Conta().titular, conta.Conta().saldo, conta.Conta().limite)
import conta