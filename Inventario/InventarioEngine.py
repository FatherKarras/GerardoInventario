"""
Guarda la información del estado del inventario
El inventario es actualmente un 8x8, las letras representan el objeto
"--" representa espacio vacío
"""



class Masterinventario():
    def __init__(self):
        self.inventario = [
            ["guardian", "--", "--", "--", "defensor", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "rodela", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "aegis", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
        ]

    def Mueveobjeto(self, movimiento):
        self.inventario[movimiento.desdefila][movimiento.desdecolumna] = self.inventario[movimiento.haciafila][movimiento.haciacolumna]
        self.inventario[movimiento.haciafila][movimiento.haciacolumna] = movimiento.mueveobjeto

class Movimiento():
    def __init__(self, desdecasilla, haciacasilla, inventario):
        self.desdefila = desdecasilla[0]
        self.desdecolumna = desdecasilla[1]
        self.haciafila = haciacasilla[0]
        self.haciacolumna = haciacasilla[1]
        self.mueveobjeto = inventario[self.desdefila][self.desdecolumna]