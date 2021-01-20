import pygame
import random
import time
#import pkg_resources.py2_warn #per convertir a .exe

#vaig plantejar aquest tetris com una quadricula on cada quadradet tenia una variable que podia estar en tres pocicions(0,1,2) 0:no hi ha res 1:hi ha algo pero no es fixe 2: hi ha algo fixe
def peça(x, y, borrar):  # quadrada
    global pos
    global ran
    global gir
    # equacio de cada peça en cada pocisio
    if ran == 1:
        color = (255, 255, 255)
        pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
        pos[19 - y][x + 1] = [borrar, color, pos[19 - y][x + 1][2]]
        pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
        pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
    if ran == 2:
        color = (255, 0, 0)
        if gir == 0:  # soc concient que hi ha una manera mes matematica pero es dificil
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - y][x + 1] = [borrar, color, pos[19 - y][x + 1][2]]
        elif gir == 1:

            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x + 1] = [borrar, color, pos[19 - (y - 2)][x + 1][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
        elif gir == 2:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - (y - 2)][x - 1] = [borrar, color, pos[19 - (y - 2)][x - 1][2]]
        elif gir == 3:
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - y][x - 1] = [borrar, color, pos[19 - y][x - 1][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]

    if ran == 3:
        color = (255, 166, 0)
        if gir == 0:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - y][x - 1] = [borrar, color, pos[19 - y][x - 1][2]]
        elif gir == 1:
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - y][x + 1] = [borrar, color, pos[19 - y][x + 1][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
        elif gir == 2:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - (y - 2)][x + 1] = [borrar, color, pos[19 - (y - 2)][x + 1][2]]
        elif gir == 3:
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x - 1] = [borrar, color, pos[19 - (y - 2)][x - 1][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]

    if ran == 4:
        color = (255, 0, 255)
        if gir == 0 or gir == 2:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - (y - 3)][x] = [borrar, color, pos[19 - (y - 3)][x][2]]
        if gir == 1 or gir == 3:
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
            pos[19 - (y - 1)][x + 2] = [borrar, color, pos[19 - (y - 1)][x + 2][2]]

    if ran == 5:
        color = (255, 255, 0)
        if gir == 0:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
        elif gir == 1:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
        elif gir == 2:
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
        elif gir == 3:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]

    if ran == 6:
        color = (0, 0, 255)
        if gir == 0 or gir == 2:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - y][x + 1] = [borrar, color, pos[19 - y][x + 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
        if gir == 1 or gir == 3:
            pos[19 - (y - 2)][x] = [borrar, color, pos[19 - (y - 2)][x][2]]
            pos[19 - y][x - 1] = [borrar, color, pos[19 - y][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]
    if ran == 7:
        color = (0, 255, 0)
        if gir == 0 or gir == 2:
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - y][x - 1] = [borrar, color, pos[19 - y][x - 1][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x + 1] = [borrar, color, pos[19 - (y - 1)][x + 1][2]]
        if gir == 1 or gir == 3:
            pos[19 - (y - 2)][x - 1] = [borrar, color, pos[19 - (y - 2)][x - 1][2]]
            pos[19 - y][x] = [borrar, color, pos[19 - y][x][2]]
            pos[19 - (y - 1)][x] = [borrar, color, pos[19 - (y - 1)][x][2]]
            pos[19 - (y - 1)][x - 1] = [borrar, color, pos[19 - (y - 1)][x - 1][2]]


pos={}
ran=random.randint(1,7)
gir=0

def hola():
    global pos
    global ran
    global gir
    mode = 0
    pos={}
    pantallay = 700
    pantallax = int(pantallay / 2)
    tamany = int(pantallax / 10)
    pantalla = pygame.display.set_mode((pantallax, pantallay))
    pygame.display.set_caption("tetris")
    for i in range(-4, 24):
        pos[i] = {}
        for j in range(-4, 14):
            pos[i][j] = [0, (0, 0, 0), (0, 0, 0)]  # activitat,color, borrat
    ran = random.randint(1, 7)
    x = 4
    y = 21
    canvi = 0
    rellotge = pygame.time.Clock()
    caiguda = 0
    moviment = 0
    fuck = 0
    gir = 0
    posades = 0
    comparacio = 0
    linea = 0
    total = 0
    a = 0
    b = 0
    hey = 0
    bucle = True
    while bucle:
        rellotge.tick()
        caiguda += rellotge.get_rawtime()
        moviment += rellotge.get_rawtime()
        if moviment>100:
            moviment=0
            tecla=pygame.key.get_pressed()

            if tecla[pygame.K_LEFT]:
                if canvi==0:
                    canvi=1
                    for i in range(20):
                        for j in range(10):
                            if pos[i][j][0] == 1:
                                if j > 0:
                                    if pos[i][j-1][0] == 2:
                                        canvi = 0
                                else:
                                        canvi=0
                    if canvi==1:
                         peça(x, y, 0)
                         x -= 1


            if tecla[pygame.K_RIGHT]:
                if canvi == 0:
                    canvi=1
                    for i in range(20):
                        for j in range(10):
                            if pos[i][j][0] == 1:
                                if j < 9:
                                    if pos[i][j + 1][0] == 2:
                                        canvi = 0
                                else:
                                    canvi=0
                    if canvi == 1:
                        peça(x, y, 0)
                        x += 1

            if tecla[pygame.K_DOWN]:
                if canvi == 0:
                    for i in range(20):
                        for j in range(10):
                            if pos[i][j][0] == 1:
                                if i == 19:
                                    fuck = 1
                                if fuck == 0:
                                    if pos[i + 1][j][0] == 2:
                                        fuck = 1
                    if fuck == 0:
                        peça(x, y, 0)
                        y -= 1
                        canvi = 1


        if caiguda>150:
            caiguda=0
            if canvi == 0:
                for i in range(20):
                    for j in range(10):
                        if pos[i][j][0] == 1:
                            if i==19:
                                fuck=1
                            if fuck==0:
                                if pos[i+1][j][0]==2:
                                    fuck=1
                if fuck==0:
                    peça(x, y, 0)
                    y-=1
                    canvi=1

        if fuck==1:
            peça(x, y, 2)
            for i in range(20):
                lol=19-i
                for i in range(4):
                    linea=0
                    for j in range(10):
                        if pos[lol][j][0]==2:
                            linea+=1
                    if linea==10:
                        for z in range(20):
                            lol2=19-z
                            if lol2<=lol:
                                for j in range(10):
                                    pos[lol2][j] = pos[lol2-1][j]
            gir=0
            hey=1
            x = 4
            y = 21
            fuck=0
            ran = random.randint(1, 7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bucle = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if canvi == 0:
                            for i in range(20):
                                for j in range(10):
                                    if pos[i][j][0] == 1:
                                        a += 1
                                    if pos[i][j][0] == 2:
                                        posades += 1
                                        pos[i][j][2] = pos[i][j][1]
                            peça(x, y, 0)
                            gir += 1
                            if gir == 4:
                                gir = 0
                            canvi = 1
        if canvi==1:
            canvi=0
            peça(x,y,1)

            for i in range(20):
                for j in range(10):
                    if pos[i][j][0] == 2:
                        comparacio += 1
            for i in range(20):
                for j in range(10):
                    if pos[i][j][0] == 1:
                       b += 1

            if comparacio < posades or a>b:
                peça(x, y, 0)
                for i in range(20):
                        for j in range(10):
                            if pos[i][j][2] != (0,0,0):
                                    pos[i][j][0] = 2
                                    pos[i][j][1] = pos[i][j][2]
                            pos[i][j][2]=(0,0,0)
                if gir==0:
                    gir=3
                else:
                    gir-=1

                peça(x, y, 1)
            else:
                pantalla.fill((0, 0, 0))
                for i in range(-1,20):
                    for j in range(10):
                        if mode==0:
                            if pos[i][j][0]!=0:
                                pygame.draw.rect(pantalla, (pos[i][j][1]), (j*tamany,i*tamany,tamany,tamany))
                                if pos[i][j][0]==2:
                                    if i<1:
                                        bucle = False
                        elif mode==1:
                            if hey==0:
                                if pos[i][j][0]==1:
                                    pygame.draw.rect(pantalla, (pos[i][j][1]), (j*tamany,i*tamany,tamany,tamany))
                                    if pos[i][j][0]==2:
                                        if i<1:
                                            bucle = False
                            else:
                                if pos[i][j][0] != 0:
                                    pygame.draw.rect(pantalla, (225,225,225), (j * tamany, i * tamany, tamany, tamany))
                                    if pos[i][j][0] == 2:
                                        if i < 1:
                                            bucle = False

            hey = 0
            comparacio=0
            posades=0
            a = 0
            b = 0
        pygame.display.update()


    pygame.display.quit()

