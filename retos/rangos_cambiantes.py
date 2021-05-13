def dentro_rango(limite_inferior, limite_superior, comparacion):
    if comparacion <= limite_superior and comparacion >= limite_inferior:
        print('El numero ' + str(comparacion) + ' se encuentra dentro del rango')
        return True
    else:
        print('El numero ' + str(comparacion) + ' no se encuentra dentro del rango')
        return False

def run():
    limite_inferior = int(input('Ingrese el limite inferior: '))
    limite_superior = int(input('Ingrese el limite superior: '))
    comparacion = int(input('Ingrese un numero para comparar: '))

    while dentro_rango(limite_inferior, limite_superior, comparacion) == False:
        comparacion = int(input('Por favor ingrese un nuevo numero para comparar: '))


if __name__ == '__main__':
    run()