def run():
    # nombre = input('Escribe tu nombre: ')
    # for letra in nombre:
    #     print(letra)
    
    frase = input('Escribe una frase: ')
    for caracter in frase[::2]:
        print(caracter.upper())

    # for i in range(3,30,3):
    #     print(i)


if __name__ == '__main__':
    run()