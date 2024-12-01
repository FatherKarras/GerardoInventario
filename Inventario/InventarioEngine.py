"""
Guarda la información del estado del inventario
El inventario es actualmente un 5x4, las letras representan el objeto
"--" representa espacio vacío
"""



class Masterinventario():
    def __init__(self):
        self.casillas = [
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--"]
        ]

        self.inventario = [
            ["guardian", "--", "--", "--", "defensor"],
            ["--", "--", "--", "--", "--"],
            ["--", "rodela", "--", "--", "--"],
            ["--", "--", "--", "aegis", "--"],
            ["--"]
        ]

        self.equipados = [
            ["--", "--"],
            ["aegis", "--"]
        ]

    def Mueveobjeto(self, movimiento):
        self.inventario[movimiento.desdefila][movimiento.desdecolumna] = self.inventario[movimiento.haciafila][movimiento.haciacolumna]
        self.inventario[movimiento.haciafila][movimiento.haciacolumna] = movimiento.mueveobjeto

    def Pulsacasilla(self, activadorcasilla):
        self.casillas[activadorcasilla.desdefila][activadorcasilla.desdecolumna] = "green"

    def Despulsacasilla(self, activadorcasilla):
        self.casillas[activadorcasilla.desdefila][activadorcasilla.desdecolumna] = "--"


    def Eliminaobjeto(self, papelera):
        self.inventario[papelera.desdefila][papelera.desdecolumna] = self.inventario[papelera.haciafila][papelera.haciacolumna]
        self.inventario[papelera.haciafila][papelera.haciacolumna] = papelera.mueveobjeto
        print(self.inventario[4])
        print ("eliminado")
        self.inventario[4] = ["--"]



class Movimiento():
    def __init__(self, desdecasilla, haciacasilla, inventario):
        self.desdefila = desdecasilla[0]
        self.desdecolumna = desdecasilla[1]
        self.haciafila = haciacasilla[0]
        self.haciacolumna = haciacasilla[1]
        self.mueveobjeto = inventario[self.desdefila][self.desdecolumna]


class Papelera():
    def __init__(self, desdecasilla, inventario):
        self.desdefila = desdecasilla[0]
        self.desdecolumna = desdecasilla[1]
        self.haciafila = 4
        self.haciacolumna = 0
        self.mueveobjeto = inventario[self.desdefila][self.desdecolumna]

class Activadorcasilla():
    def __init__(self, desdecasilla, casillas):
        self.desdefila = desdecasilla[0]
        self.desdecolumna = desdecasilla[1]
        self.mueveobjeto = casillas[self.desdefila][self.desdecolumna]






