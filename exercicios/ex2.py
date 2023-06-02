class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
        
    def verBucho(self):
        if len(self.bucho) == 0:
            return "bucho vazio"
        else:
            return " ".join(self.bucho)

    def digerir(self):
        self.bucho.clear()
