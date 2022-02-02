def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    return str(dolares)


def run():
    menu = """
        Bienvenido al conversor de monedas 💰
        
        1 - Pesos colombianos
        2 - Pesos argentinos
        3 - Pesos mexicanos
        
        Elige una opcion: """

    control = 0

    while control != 1:        
        opcion = int(input(menu))
        
        if opcion == 1:
            resultado = conversor("colombianos", 3933)
            control = 1
        elif opcion == 2:
            resultado = conversor("argentinos", 65)
            control = 1
        elif opcion == 3:
            resultado = conversor("mexicanos", 24)
            control = 1
        else:
            print("Ingresa una opcion correcta por favor")

    print("Tienes $" + resultado + " dolares")


if __name__ == "__main__":
    run()

# print('')
# dolares = input('¿Cuántos dolares tienes?: ')
# dolares = float(dolares)
# valor_peso = 3875
# pesos = dolares * valor_peso
# pesos = round(pesos, 2)
# pesos = str(pesos)
# print('Tienes $' + pesos + ' pesos')
