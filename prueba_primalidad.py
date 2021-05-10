def es_factor_primo(factor_primo):
    contador = 0

    for j in range(1, factor_primo + 1):
        if factor_primo % j == 0:
            contador += 1

    if contador == 2:
        return True
    else:
        return False

def es_primo(numero):
    for factor_primo in range(1, numero + 1):
        if numero == 2:
            return True
            break
            # Sabemos que 2 es primo, pero para comprobralo con rigurosidad se realiza lo siguiente:
            # if es_factor_primo(numero):
            #     return True
            #     break
            # else:
            #     return False
            #     break
        elif es_factor_primo(factor_primo):
            cociente = numero // factor_primo
            residuo = numero % factor_primo

            if cociente <= factor_primo and residuo != 0:
                return True
                break
            elif residuo == 0:
                return False
                break


def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()