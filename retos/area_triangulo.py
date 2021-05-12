def tipo_triangulo():
    lado1 = float(input('Ingrese la medida del primer lado del triangulo: '))
    lado2 = float(input('Ingrese la medida del segundo lado del triangulo: '))
    lado3 = float(input('Ingrese la medida del tercer lado del triangulo: '))

    if lado1 == lado2 == lado3:
        return('Equilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return('Isoceles')
    else:
        return('Escaleno')


def hallar_area():
    base = int(input('Ingrese la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))

    area = (base * altura) / 2
    return area


def run():
    print("""
    Conozca el Area y Tipo de su triangulo
    """)

    area = hallar_area()
    tipo = tipo_triangulo()

    print('')
    print('El area del triangulo es igual a: ' + str(area))
    print('Su triangulo es de tipo: ' + tipo)


if __name__ == '__main__':
    run()