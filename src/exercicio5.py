#usarei este módulo para importar os caracteres
import string

#usarei este módulo pra importar os métodos shuffle e choice
import random 

#utilizando o método 'digits' para usar os números
caracteres = string.digits
lista_caracteres = []

comprimento = 11

for c in caracteres:
    random.shuffle(lista_caracteres)
    lista_caracteres.append(c)
    
senha = []

for i in range(comprimento):
    senha.append(random.choice(lista_caracteres))
    random.shuffle(senha)
    
print("".join(senha))

def validar_cpf(senha):
    senha = [int(char) for char in senha if char.isdigit()]

    if len(senha) != 11:
        return False

    if senha == senha[::-1]:
        return False

    for i in range(9, 11):
        valor = sum((senha[num] * ((i+1) - num) for num in range(0, i)))
        digitos = ((valor * 10) % 11) % 10
        if digitos != senha[i]:
            return False
    return True

if validar_cpf(senha): 
    print('A senha é um CPF')
else:
    print('A senha não é um CPF')