# Crie uma classe que modele um retângulo

class Retangulo:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura
    
    def mudar_lados(self, comprimento, altura):
        self.comprimento, self.altura = comprimento, altura

    @property
    def get_lados(self):
        return self.comprimento, self.altura

    def calcula_area(self):
        area = self.comprimento * self.altura
        return area

    def calcula_perimetro(self):
        perimetro = (self.comprimento * 2) + (self.altura * 2)
        return perimetro
