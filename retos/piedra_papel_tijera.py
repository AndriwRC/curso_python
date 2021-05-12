def ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        print('Es un Empate')

    elif opcion1 == 'piedra' and opcion2 == 'tijera':
        print('El ganador es el Jugador 1!')
        return(1)
    elif opcion1 == 'papel' and opcion2 == 'piedra':
        print('El ganador es el Jugador 1!')
        return(1)
    elif opcion1 == 'tijera' and opcion2 == 'papel':
        print('El ganador es el Jugador 1!')
        return(1)

    elif opcion1 == 'piedra' and opcion2 == 'papel':
        print('El ganador es el Jugador 2!')
        return(2)
    elif opcion1 == 'papel' and opcion2 == 'tijera':
        print('El ganador es el Jugador 2!')
        return(2)
    elif opcion1 == 'tijera' and opcion2 == 'piedra':
        print('El ganador es el Jugador 2!')
        return(2)


def run():
    puntaje_jugador1 = 0
    puntaje_jugador2 = 0
    for i in range(3):
        jugador1 = input('Jugador 1, elige piedra, papel o tijera: ')
        jugador2 = input('Jugador 2, elige piedra, papel o tijera: ')

        puntaje = ganador(jugador1, jugador2)

        if puntaje == 1:
            puntaje_jugador1 += 1
        elif puntaje == 2:
            puntaje_jugador2 += 1
        
    if puntaje_jugador1 > puntaje_jugador2:
        print('El ganador definitivo es el jugador 1 con ' + puntaje_jugador1 +' puntos, Felicidades!')
    elif puntaje_jugador1 < puntaje_jugador2:
        print('El ganador definitivo es el jugador 2 con ' + puntaje_jugador2 +' puntos, Felicidades!')
    else:
        print('Es un empate definitivo')


if __name__ == '__main__':
    run()