# Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    @property
    def mostra_cor(self):
        print(f"A cor da bola é {self.cor}")
        return self.cor


bola = Bola("amarela", 15, "borracha")

bola.mostra_cor
bola.troca_cor("roxa")
bola.mostra_cor
