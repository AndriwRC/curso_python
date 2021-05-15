def volumen_figura(figura):
    if figura == 1:
        radio = float(input('Ingrese el radio de la base: '))
        altura = float(input('Ingrese la altura del cilindro: '))
        volumen = round(3.1416 * (radio ** 2) * altura, 2)
        return('El volumen del Cilindro es igual a: ' + str(volumen))
    elif figura == 2:
        radio = float(input('Ingrese el radio de la base: '))
        altura = float(input('Ingrese la altura del cono: '))
        volumen = round((3.1416 * (radio ** 2) * altura) / 3, 2)
        return('El volumen del Cono es igual a: ' + str(volumen))
    elif figura == 3:
        arista = float(input('Ingrese la medida de una arista del cubo: '))
        volumen = arista ** 3
        return('El volumen del Cubo es igual a: ' + str(volumen))


def run():
    menu = """
    * * * Calculadora De Volumenes * * *

    Elige la figura que desees:
    1 - Cilindro
    2 - Cono
    3 - Cubo

    """
    figura = int(input(menu))
    while figura not in {1, 2, 3}:
            figura = int(input('Ingresa una opcion valida: '))

    print(volumen_figura(figura))


if __name__ == '__main__':
    run()