filas = 5
columnas = 5

def crear_tablero(filas, columnas, gato, raton):
    tablero = [["." for i in range (columnas)] for j in range(filas)]
    tablero[gato[0]][gato[1]] = "G"
    tablero[raton[0]][raton[1]] = "R"
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def obtener_movimientos_validos(posicion, filas, columnas):
    fila, columna = posicion
    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    movimientos_validos = []
    for direccion in direcciones:
        nueva_fila = fila + direccion[0]
        nueva_columna = columna + direccion[1]

        if 0 < nueva_fila <filas and 0 < nueva_columna <columnas:
            movimientos_validos.append((nueva_fila)(nueva_columna))
    return movimientos_validos

if __name__ == "__main__":
    gato = (0,0)
    raton = (filas -1, columnas -1)
    tablero = crear_tablero(filas, columnas, gato, raton)
    mostrar_tablero(tablero)