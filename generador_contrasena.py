import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    numero_caracteres = int(input('Ingrese el numero de caracteres que desea: '))

    for i in range(numero_caracteres):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    # Convertir lista en string:
    contrasena = ''.join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasesña es: ' + contrasena)


if __name__ == '__main__':
    run()