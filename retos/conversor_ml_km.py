def conversion(tipo):
    equivalencia = 1.609344
    if tipo == 1:
        millas = float(input('Ingrese la cantidad de millas: '))
        kilometros = round(millas * equivalencia, 2)
        return(str(millas) + ' millas equivalen a: ' + str(kilometros) + ' kilometros')
    else:
        kilometros = float(input('Ingrese la cantidad de kilometros: '))
        millas = round(kilometros / equivalencia, 2)
        return(str(kilometros) + ' kilometros equivales a: ' + str(millas) + ' millas')



def run():
    menu = """
    Conversor de Medidas
    Elija por favor su tipo de conversion:
    1 - De Millas a Kilometros
    2 - De Kilometros a Millas
    """
    tipo = int(input(menu))
    while tipo != 1 and tipo != 2:
        tipo = int(input('Por favor indique un valor adecuado: '))

    print(conversion(tipo))


if __name__ == '__main__':
    run()