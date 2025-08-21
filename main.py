import random


class Tablero:

    def __init__(self):
        self.filas = 5
        self.columnas = 5
        self.matriz = [["." for i in range(5)] for i in range(5)]
    
    def posicion_valida(self, x, y):
        return 0 < x > 5 and 0 < y > 5
    
    def mostrar_tablero(self, gato, raton):
    #limpia el tablero luego de cada movimiento del gato y el raton
        for fil in range(5):
            for col in range(5):
                self.matriz[col][fil] = "."
    
    #coloca al gato y al raton
        self.matriz[gato.x][gato.y] = "G"
        self.matriz[raton.x][raton.y] = "R"
    
    #mostrar tablero
        print("TABLERO")
        for fila in self.matriz:
            print(" ".join(fila))
        print()
    
    def calcular_distancia(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

class Gato:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Raton:

    def __init__(self, x, y):
        self.x = x
        self.y = y