# Crie uma classe que modele um quadrado

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_lado(self, valor):
        self.lado = valor

    @property
    def get_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado * self.lado
