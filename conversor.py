menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input('¿Cuántos pesos argentinos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
elif opcion == 3:
    pesos = input('¿Cuántos pesos mexicanos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
else:
    print("Ingresa una opcion correcta por favor")



# print('')
# dolares = input('¿Cuántos dolares tienes?: ')
# dolares = float(dolares)
# valor_peso = 3875
# pesos = dolares * valor_peso
# pesos = round(pesos, 2)
# pesos = str(pesos)
# print('Tienes $' + pesos + ' pesos')