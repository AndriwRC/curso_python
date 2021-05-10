def run():
    numero = 0
    while numero < 1000:
        numero += 1
        divisores = 0
        i = 1
        
        while i <= numero:
            if numero % i == 0:
                divisores += 1
            i += 1

        if divisores != 2:
            continue

        print(numero)


if __name__ == '__main__':
    run()