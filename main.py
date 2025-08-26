import random

class Tablero:
    def __init__(self):
        self.matriz = [["." for i in range(5)] for j in range(5)]
    
    def es_valida(self, x, y):
        return 0 <= x < 5 and 0 <= y < 5
    
    def mostrar(self, gato, raton):
        for fila in range(5):
            for col in range(5):
                self.matriz[fila][col] = "." #2
        
        self.matriz[gato.x][gato.y] = "G"
        self.matriz[raton.x][raton.y] = "R"
        
        print("\nTablero")
        for fila in self.matriz:
            print(" ".join(fila)) #3
        print()
    
    def distancia(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

class Gato:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def movimientos_posibles(self, tablero):
        movimientos = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in direcciones:
            nuevo_x = self.x + dx
            nuevo_y = self.y + dy
            if tablero.es_valida(nuevo_x, nuevo_y):
                movimientos.append((nuevo_x, nuevo_y))
        
        return movimientos
    
    def minimax(self, tablero, profundidad, es_gato, gato_x, gato_y, raton_x, raton_y):
        if profundidad == 0:
            dist = tablero.distancia(gato_x, gato_y, raton_x, raton_y)
            return -dist
        
        if es_gato:
            mejor_valor = float('-inf')
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dx, dy in direcciones:
                nuevo_gato_x = gato_x + dx
                nuevo_gato_y = gato_y + dy
                
                if tablero.es_valida(nuevo_gato_x, nuevo_gato_y):
                    valor = self.minimax(tablero, profundidad - 1, False, nuevo_gato_x, nuevo_gato_y, raton_x, raton_y)
                    mejor_valor = max(mejor_valor, valor)
            
            return mejor_valor
        else:
            mejor_valor = float('inf')
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dx, dy in direcciones:
                nuevo_raton_x = raton_x + dx
                nuevo_raton_y = raton_y + dy
                
                if tablero.es_valida(nuevo_raton_x, nuevo_raton_y):
                    valor = self.minimax(tablero, profundidad - 1, True, gato_x, gato_y, nuevo_raton_x, nuevo_raton_y)
                    mejor_valor = min(mejor_valor, valor)
            
            return mejor_valor
    
    def elegir_movimiento(self, tablero, raton):

        movimientos = self.movimientos_posibles(tablero)
        if not movimientos:
            return False
        
        mejor_movimiento = None
        mejor_valor = float('-inf')
        
        for mov_x, mov_y in movimientos:
            valor = self.minimax(tablero, 1, False, mov_x, mov_y, raton.x, raton.y)
            
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = (mov_x, mov_y)
        
        if mejor_movimiento:
            self.x, self.y = mejor_movimiento
            return True

class Raton:
    def __init__(self):
        self.x = 4
        self.y = 4
    
    def movimientos_posibles(self, tablero):
        movimientos = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in direcciones:
            nuevo_x = self.x + dx
            nuevo_y = self.y + dy
            if tablero.es_valida(nuevo_x, nuevo_y):
                movimientos.append((nuevo_x, nuevo_y))
        
        return movimientos
    
    def mover_aleatorio(self, tablero):

        movimientos = self.movimientos_posibles(tablero)
        
        if movimientos:
            movimiento_elegido = random.choice(movimientos)
            self.x, self.y = movimiento_elegido
            return True
        

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.gato = Gato()
        self.raton = Raton()
        self.turno = 0
        self.max_turnos = 10
    
    def gato_atrapa_raton(self):
        return self.gato.x == self.raton.x and self.gato.y == self.raton.y
    
    def jugar(self):
        print("Gato vs Raton")
        print(f"El gato inicia en la posicion ({self.gato.x}, {self.gato.y})")
        print(f"El raton inicia en la posicion ({self.raton.x}, {self.raton.y})")
        
        while self.turno < self.max_turnos:
            print(f"\nTurno {self.turno + 1}/{self.max_turnos}")
            
            self.tablero.mostrar(self.gato, self.raton)
            
            self.gato.elegir_movimiento(self.tablero, self.raton)
            
            if self.gato_atrapa_raton():
                print("\nFin del juego")
                self.tablero.mostrar(self.gato, self.raton)
                print("El gato atrapo al raton")
                return
            
            self.raton.mover_aleatorio(self.tablero)
            
            if self.gato_atrapa_raton():
                print("\nFin del juego")
                self.tablero.mostrar(self.gato, self.raton)
                print("El gato gana")
                return
            
            self.turno += 1
            
            input("Presiona enter para continuar al siguiente turno")
        
        print("El raton escapo")

if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
