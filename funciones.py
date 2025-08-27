import random

def crear_tablero(x, y, gato, raton):
    tablero = [["."for j in range (y)] for i in range(x)]
    tablero[gato[0]][gato[1]] = "G"
    tablero[raton[0]][raton[1]] = "R"
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

if __name__ == "__main__":
    dimension = int(input("Cual sera el tamaño del tablero?"))
    gato = (0,0)
    raton = (dimension -1, dimension -1)
    tablero = crear_tablero(dimension, dimension, gato, raton)
    mostrar_tablero(tablero)

def obtener_movimientos_validos(nuevo_movi):
    fila, columna = nuevo_movi
    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    movimientos_validos = []
    for nuevo_movi in direcciones:
        nueva_fila = fila + nuevo_movi[0]
        nueva_columna = columna + nuevo_movi[1]
        if 0 <= nueva_fila <= 5 and 0 <= nueva_columna <=5:
            movimientos_validos.append((nueva_fila, nueva_columna))
    return movimientos_validos

def mover_aleatorio(gato, raton):
    movimientos_gato = obtener_movimientos_validos(gato)
    if movimientos_gato:
        gato[0], gato[1] = random.choice(movimientos_gato)
    
    movimientos_raton = obtener_movimientos_validos(raton)
    if movimientos_raton:
        raton[0], raton[1] = random.choice(movimientos_raton)
    
    return gato, raton