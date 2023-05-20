'''
8. Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos
nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago
a cada refeição. Experimente fazer com que um macaco coma o outro.
É possível criar um macaco canibal?
'''

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

mac1 = Macaco("Chico")
mac1.comer("banana")
print(mac1.verBucho())
mac1.comer("laranja")
print(mac1.verBucho())
mac1.digerir()
print(mac1.verBucho())