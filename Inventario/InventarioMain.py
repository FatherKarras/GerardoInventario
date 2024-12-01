import pygame
from InventarioEngine import Masterinventario
from InventarioEngine import Movimiento
from InventarioEngine import Papelera
from InventarioEngine import Activadorcasilla

fps = 30
Iconos = {}

ancho = 800
alto = 800
filas = 4
columnas = 5
tamano_cuadricula = 100
papeleraimagen = pygame.transform.scale(pygame.image.load("iconos/papelera.png"), (100, 100))


def Cargadordeimagenes():
    objetos = ["guardian", "rodela", "defensor", "aegis"]
    for objeto in objetos:
        Iconos[objeto] = pygame.transform.scale(pygame.image.load("iconos/" + objeto + ".png"), (tamano_cuadricula - 5,
                                                                                                 tamano_cuadricula - 5))

def main():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    surface1 = pygame.Surface((500, 400))
    surface2 = pygame.Surface((100, 100))
    reloj = pygame.time.Clock()
    ventana.fill(pygame.Color("white"))
    surface2.fill("white")
    inventario = Masterinventario()
    Cargadordeimagenes()
    running = True

    casillaseleccionada = () # tuple: fila y columna
    clicks = [] #trackea los clicks del jugador en dos tuples: [(6,4), (5,4)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickdelraton = pygame.mouse.get_pos()
                columna = clickdelraton[0]//tamano_cuadricula
                fila = clickdelraton[1]//tamano_cuadricula

                if columna < 5 and fila < 4:
                    if len(clicks) == 0 and (inventario.inventario[fila][columna]) == "--":
                        casillaseleccionada = ()
                        clicks = []
                    else:
                        casillaseleccionada = (fila, columna)
                        clicks.append(casillaseleccionada)
                        activacasilla = Activadorcasilla(clicks[0], inventario.casillas)
                        inventario.Pulsacasilla(activacasilla)

                    if len(clicks) == 2:
                        movimiento = Movimiento(clicks[0], clicks[1], inventario.inventario)
                        inventario.Mueveobjeto(movimiento)
                        desactivacasilla = Activadorcasilla(clicks[0], inventario.casillas)
                        inventario.Despulsacasilla(desactivacasilla)
                        casillaseleccionada = ()
                        clicks = []
                        print(inventario.inventario)

                elif columna == 6 and fila == 6:
                    if len(clicks) == 0:
                        casillaseleccionada = ()
                        clicks = []
                    if len(clicks) == 1:
                        print("papelera")
                        desactivacasilla = Activadorcasilla(clicks[0], inventario.casillas)
                        inventario.Despulsacasilla(desactivacasilla)
                        papelera = Papelera(clicks[0], inventario.inventario)
                        inventario.Eliminaobjeto(papelera)
                        casillaseleccionada = ()
                        clicks = []

                else:
                    if len(clicks) == 0:
                         casillaseleccionada = ()
                         clicks = []
                    if len(clicks) == 1:
                        desactivacasilla = Activadorcasilla(clicks[0], inventario.casillas)
                        inventario.Despulsacasilla(desactivacasilla)
                        casillaseleccionada = ()
                        clicks = []


        ventana.blit(surface1, (0, 0))
        ventana.blit(surface2, (600, 600))
        reloj.tick(fps)
        Pintado(surface1, surface2, inventario.inventario, inventario.casillas)
        pygame.display.flip()


def Pintado(surface1, surface2, inventario, casillas):
    Pintadorejilla(surface1, casillas)
    Pintadoobjetos(surface1, inventario)
    Pintadoiconos(surface2)



def Pintadorejilla(surface1, inventario):
    for r in range(filas):
        for c in range(columnas):
            casilla = inventario[r][c]
            if casilla == "--":
                pygame.draw.rect(surface1, ("gray"), pygame.Rect(c*tamano_cuadricula, r*tamano_cuadricula, tamano_cuadricula-5,
                                                         tamano_cuadricula-5))
            if casilla == "green":
                pygame.draw.rect(surface1, ("green"), pygame.Rect(c * tamano_cuadricula, r * tamano_cuadricula, tamano_cuadricula - 5,
                                             tamano_cuadricula - 5))


def Pintadoiconos(surface2):
    surface2.blit(papeleraimagen, pygame.Rect(0, 0, tamano_cuadricula, tamano_cuadricula))


def Pintadoobjetos(surface1, inventario):
    for r in range(filas):
        for c in range(columnas):
            objeto = inventario[r][c]
            if objeto != "--":
                surface1.blit(Iconos[objeto], pygame.Rect(c*tamano_cuadricula, r*tamano_cuadricula, tamano_cuadricula,
                                                          tamano_cuadricula))


if __name__ == "__main__":
    main()
