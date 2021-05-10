# Tablas de multiplicar elegida por el usuario
# def run():
#     i = int(input('Ingrese la tabla de multiplicar que desea conocer: '))
#     print('')
#     print('Tabla del ' + str(i))
#     for j in range(11):
#         producto = i * j
#         print(str(i) + ' * ' + str(j) + ' = ' + str(producto))


# Tabla de multiplicar del 1 al 10
def run():
    for i in range(1, 11):
        print('Tabla del ' + str(i))
        for j in range(11):
            producto = i * j
            print(str(i) + ' * ' + str(j) + ' = ' + str(producto))
        print('')


if __name__ == '__main__':
    run()