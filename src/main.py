import string
#usarei este módulo para importar os caracteres
import random 
#usarei este módulo pra importar os métodos shuffle e choice

caracteres = string.ascii_letters + string.digits + string.punctuation
lista_caracteres = [caracteres]

comprimento = int(input("Digite quantos caracteres a sua senha terá: "))

for c in caracteres:
    random.shuffle(lista_caracteres)
    lista_caracteres.append(c)
    
senha = []

for i in range(comprimento):
    senha.append(random.choice(lista_caracteres))
    random.shuffle(senha)
    
print("".join(senha))