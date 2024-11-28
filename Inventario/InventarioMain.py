import pygame
from InventarioEngine import Masterinventario
from InventarioEngine import Movimiento
fps = 30
Iconos = {}

ancho = 800
alto = 800
dimension = 8
tamano_cuadricula = (ancho // dimension)


def Cargadordeimagenes():
    objetos = ["guardian", "rodela", "defensor", "aegis"]
    for objeto in objetos:
        Iconos[objeto] = pygame.transform.scale(pygame.image.load("iconos/" + objeto + ".png"), (tamano_cuadricula,
                                                                                                 tamano_cuadricula))


def main():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    ventana.fill(pygame.Color("white"))
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


                if casillaseleccionada == (fila, columna):
                    casillaseleccionada = ()
                    clicks = []
                if len(clicks) == 0 and (inventario.inventario[fila][columna]) == "--":
                    casillaseleccionada = ()
                    clicks = []
                else:
                    casillaseleccionada = (fila, columna)
                    clicks.append(casillaseleccionada)
                    print(inventario.inventario[fila][columna])
                    # añadimos a la lista los clicks hasta que len(clicks) == 2 y entonces hace el movimiento

                if len(clicks) == 2:
                    movimiento = Movimiento(clicks[0], clicks[1], inventario.inventario)
                    inventario.Mueveobjeto(movimiento)
                    casillaseleccionada = ()
                    clicks = []
                    print(inventario.inventario)

        Pintado(ventana, inventario.inventario)
        reloj.tick(fps)
        pygame.display.flip()


def Pintado(ventana, inventario):
    Pintadorejilla(ventana)
    Pintadoobjetos(ventana, inventario)


def Pintadorejilla(ventana):
    colores = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(dimension):
        for c in range(dimension):
            color = colores[((r+c) % 2)]
            pygame.draw.rect(ventana, color, pygame.Rect(c*tamano_cuadricula, r*tamano_cuadricula, tamano_cuadricula,
                                                         tamano_cuadricula))


def Pintadoobjetos(ventana, inventario):
    for r in range(dimension):
        for c in range(dimension):
            objeto = inventario[r][c]
            if objeto != "--":
                ventana.blit(Iconos[objeto], pygame.Rect(c*tamano_cuadricula, r*tamano_cuadricula, tamano_cuadricula,
                                                          tamano_cuadricula))


if __name__ == "__main__":
    main()
