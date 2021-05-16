def tipo(base, lado1, lado2):
    if base == lado1 == lado2:
        return('Equilatero')
    elif base != lado1 != lado2:
        return('Escaleno')
    else:
        return('Isosceles')


def hallar_lado(base, altura, lado1):
    base_1 = ((lado1 ** 2) - (altura ** 2)) ** (1/2)
    base_2 = base - base_1
    lado2 = ((base_2 ** 2) + (altura ** 2)) ** (1/2)
    lado2 = round(lado2, 1)
    return(lado2)


def valor_positivo(numero):
    while numero <= 0:
        numero = float(input('Por favor, Ingrese un valor positivo mayor que 0: '))
    return numero


def run():
    print("""
    Conozca el Area y Tipo de su triangulo
    """)
    
    # Area de Triangulo
    base = float(input('Ingrese la base del triangulo: '))
    base = valor_positivo(base)
    altura = float(input('Ingrese la altura del triangulo: '))
    altura = valor_positivo(altura)
    area = round((base * altura / 2), 2)
    print('El area del triangulo es igual a: ' + str(area) + '\n')
    
    # Tipo de Triangulo
    lado1 = float(input('Ahora Ingrese la medida de un lado del triangulo: '))
    lado1 = valor_positivo(lado1)
    lado2 = hallar_lado(base, altura, lado1)
    print('Su triangulo es de tipo: ' + tipo(base, lado1, lado2))


if __name__ == '__main__':
    run()
