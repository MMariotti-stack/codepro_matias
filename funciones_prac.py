#crear un tablero, debo crear una matriz donde voy a utilizar un for loop anidado para que itere entre filas y columnas, y luego voy a agregar al gato y al raton en ella
import random

filas = 10
columnas = 10

def crear_tablero(filas, columnas, gato, raton):
    tablero = [["." for j in range(columnas)] for i in range(filas)]
    tablero[gato[0]][gato[1]] = "G"
    tablero[raton[0]][raton[1]] = "R"

    return tablero

#mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

if __name__ == "__main__":
    gato = [0,0]
    raton = [filas -1, columnas -1]
    tablero = crear_tablero(filas, columnas, gato, raton)
    mostrar_tablero(tablero)

#obtener movimientos validos, debo verificar las 4 direcciones posibles (arriba, abajo, izquierda, derecha) desde una posicion y devolver solo los movimientos que esten dentro de los limites del tablero
def verificar_movimientos(nuevo_movi):
    fila, columna = nuevo_movi
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
    movimientos_validos = []
    for nuevo_movi in direcciones:
        nueva_fila = fila + nuevo_movi[0]
        nueva_columna = columna + nuevo_movi[1]
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            movimientos_validos.append((nueva_fila, nueva_columna))
    return movimientos_validos

#mover gato y raton aleatoriamente, debo obtener los movimientos validos para cada uno y usar random.choice para seleccionar uno al azar, luego actualizar sus posiciones
def mover_aleatorio(gato, raton):
    movimiento_gato = verificar_movimientos(gato)
    if movimiento_gato:
        gato[0], gato[1] = random.choice(movimiento_gato)
    
    movimiento_raton = verificar_movimientos(raton)
    if movimiento_raton:
        raton[0], raton[1] = random.choice(movimiento_raton)
    
    return(gato, raton)

#ejecutar el programa pidiendo las dimensiones del tablero y agregando la posicion del gato, raton y mostrar el tablero
if __name__ == "__main__":
    gato = [0,0]
    raton = [filas -1, columnas -1]
    gato, raton = mover_aleatorio(gato, raton)
    tablero = crear_tablero(filas, columnas, gato, raton)
    mostrar_tablero(tablero)


