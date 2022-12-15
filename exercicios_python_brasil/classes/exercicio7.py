class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    # Retorna nome
    @property
    def nome(self):
        return self.nome

    # Altera nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    # Retorna fome
    @property
    def fome(self):
        return self.fome

    # Altera fome
    @fome.setter
    def fome(self, fome):
        self.fome = fome

    # Retorna saude
    @property
    def saude(self):
        return self.saude

    # Altera saude
    @saude.setter
    def saude(self, saude):
        self.fome = saude

    # Retorna idade
    @property
    def idade(self):
        return self.idade

    # Altera idade
    @idade.setter
    def idade(self, idade):
        self.idade = idade

    def humor(self):
        return self.saude + self.fome

