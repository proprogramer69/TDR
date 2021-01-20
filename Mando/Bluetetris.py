import serial
import pygame
import random
import time
#import pkg_resources.py2_warn

pygame.init()
pygame.font.init()


"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

port = "COM3"
#try:
if True:
    bluetooth = serial.Serial(port, 9600)
    #bluetooth.flushInput()
    # MIDES
    s_width = 800  # amplada pantalla
    s_height = 700  # altura pantalla
    play_width = 300  # meaning 300 // 10 = 30 width per block
    play_height = 600  # meaning 600 // 20 = 20 height per block

    block_size = 30  # mida blocs

    top_left_x = (s_width - play_width) // 2  # posicio x de la graella
    top_left_y = (s_height - play_height) - 20  # posició y de la graella

    # CARGAR MUSIQUES
    sound1 = pygame.mixer.Sound("player.wav")
    sound2 = pygame.mixer.Sound("linea.wav")
    sound3 = pygame.mixer.Sound("minecraft1.wav")
    sound4 = pygame.mixer.Sound("minecraft2.wav")
    sound5 = pygame.mixer.Sound("record.wav")

    # SHAPE FORMATS
    S = [['.....',
          '......',
          '..00..',
          '.00...',
          '.....'],
         ['.....',
          '..0..',
          '..00.',
          '...0.',
          '.....']]

    Z = [['.....',
          '.....',
          '.00..',
          '..00.',
          '.....'],
         ['.....',
          '..0..',
          '.00..',
          '.0...',
          '.....']]

    I = [['..0..',
          '..0..',
          '..0..',
          '..0..',
          '.....'],
         ['.....',
          '0000.',
          '.....',
          '.....',
          '.....']]

    O = [['.....',
          '.....',
          '.00..',
          '.00..',
          '.....']]

    J = [['.....',
          '.0...',
          '.000.',
          '.....',
          '.....'],
         ['.....',
          '..00.',
          '..0..',
          '..0..',
          '.....'],
         ['.....',
          '.....',
          '.000.',
          '...0.',
          '.....'],
         ['.....',
          '..0..',
          '..0..',
          '.00..',
          '.....']]

    L = [['.....',
          '...0.',
          '.000.',
          '.....',
          '.....'],
         ['.....',
          '..0..',
          '..0..',
          '..00.',
          '.....'],
         ['.....',
          '.....',
          '.000.',
          '.0...',
          '.....'],
         ['.....',
          '.00..',
          '..0..',
          '..0..',
          '.....']]

    T = [['.....',
          '..0..',
          '.000.',
          '.....',
          '.....'],
         ['.....',
          '..0..',
          '..00.',
          '..0..',
          '.....'],
         ['.....',
          '.....',
          '.000.',
          '..0..',
          '.....'],
         ['.....',
          '..0..',
          '.00..',
          '..0..',
          '.....']]

    shapes = [S, Z, I, O, J, L, T]  # S, Z, I, O, J, L, T
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


    # index 0 - 6 represent shape


    class Piece(object):  # creació de la classe peça
        def __init__(self, x, y, shape):
            self.x = x
            self.y = y + 2
            self.shape = shape
            self.color = shape_colors[shapes.index(shape)]
            self.rotation = 0


    def create_grid(locked_positions={}):  # crear la idea de caselles i basicament saver les caselles que ja estan pintades

        grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]  # inicia llista de 3 zeros a cada casella

        for i in range(len(grid)):  # cada y          la i és la y,  la j és la x
            for j in range(len(grid[i])):  # cada x respecte una y
                if (j,i) in locked_positions:  # fer sol en les cordenades d'entrada, posa les cordenades locked(osigui les que ja no es poden desplaçar) al grid, el qual les pintara
                    c = locked_positions[(j, i)]
                    grid[i][j] = c
        return grid


    def convert_shape_format(shape):  # convertir la peça
        positions = []
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    positions.append((shape.x + j, shape.y + i))
        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions  # torna les cordenades de la peça


    def update_score(nscore):  # com diu el nom actualitza el record
        with open('score', 'r') as f:  # llegeix el fitxer i el borra
            lines = f.readlines()
            score = lines[0].strip()
        with open('score', 'w') as f:
            if int(score) > nscore:  # si el record es superior al d'abans l'escriu
                f.write(str(score))
                record = 0
            else:
                f.write(str(nscore))  # si no, escriu el d'abans
                record = 1
        return record


    def valid_space(shape, grid, IA):  # saver si esta la fitxa està en un lloc valid basicament mirant

        accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1 or IA != 0:  # he agut de posar IA!=0 perquè si no em detectava posicions que no eren valides perque la IA=1 anava més cap amunt de y=-1 llavors detectava posició valida, en canvi a la IA=0 és necesari perquè quan la peça llarga apareix detecta que està mal colocada al principi
                    return False
        return True


    def check_lost(positions):  # veure si t'has pasat d'alt, o sigui si has perdut
        for pos in positions:
            x, y = pos
            if y < 1:
                return True
        return False


    def get_shape():  # agafar fitxa aleatoriament de la llista
        var = random.choice(shapes)
        # print(var)
        return Piece(5, 0, var)


    def draw_text_middle(text, surface):  # escriure text
        font = pygame.font.SysFont("arial", 60, bold=True)
        label = font.render(text, 1, (255, 255, 255))
        surface.blit(label, (
        top_left_x + play_width / 2 - (label.get_width() / 2), (top_left_y + play_height / 2 - (label.get_width() / 2))))
        pygame.display.update()


    def draw_grid(surface, grid):  # pintar les linees de la graella
        sx = top_left_x
        sy = top_left_y
        for i in range(len(grid)):  # y
            pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
            for j in range(len(grid[i])):  # x
                pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy),
                                 (sx + j * block_size, sy + play_height))


    def clear_rows(win1, grid, locked, pice, poin, pol, lok):  # treure linees
        inc = 0
        si = 0
        ind = [0, 0, 0, 0]
        for i in range(len(grid) - 1, -1, -1):
            row = grid[i]
            if (0, 0, 0) not in row:  # si troba que hi ha linea
                ind[inc] = i  # y de les linees
                inc += 1  # quantitat de linees

                for j in range(len(row)):
                    try:
                        del locked[(j, i)]  # expulsar les pocisions immobils que ha trobat
                    except:
                        continue
        if inc == 4:
            sound2.play()
            for i in range(10):
                bluetooth.write(b'4')
        elif inc>0:
            for i in range(10):
                bluetooth.write(b'3')

        for lol in range(4):  # Animació
            for i in range(4):
                for j in range(10):
                    if ind[i] > 0:
                        grid[ind[i]][j] = (255, 255, 255)
                        si = 1
            if si == 1:

                draw_window(win1, grid, poin, pol, lok)
                draw_next_shape(pice, win1)
                pygame.display.update()
                time.sleep(0.05)
                for i in range(4):
                    for j in range(10):
                        if ind[i] > 0:
                            grid[ind[i]][j] = (0, 0, 0)
                draw_window(win1, grid, poin, pol, lok)
                draw_next_shape(pice, win1)
                pygame.display.update()
                time.sleep(0.05)

        if inc > 0:  # baixar linees superiors
            for i in range(4):
                for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                    x, y = key
                    pol = 3 - i  # per arreglar fallo dient-li a cada linea individualment lo que ha de baixar a partir de la posicio de les linees
                    if y < ind[pol]:
                        newKey = (x, y + 1)
                        locked[newKey] = locked.pop(key)
        return inc


    def draw_next_shape(shape, surface):  # pintar la seguent fitxa
        font = pygame.font.SysFont('arial', 30, bold=True)
        label = font.render('Proxima peça', 1, (255, 255, 255))

        sx = top_left_x + play_width + 50
        sy = top_left_y + play_height / 2 - 100
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

        surface.blit(label, (sx - 15, sy - 60))


    def comprovar_forats(win1, grid, cas):  # comprovar els forats que hi ha tenint en compte
        suma = 0
        inc = 0
        si = 0
        lin = 0
        ind = [0, 0, 0, 0]
        dis = 0
        total = 0
        lol = 100000000000000000000
        final = 0
        pol = 0
        if cas == 5:
            var = 1
        else:
            var = 0

        for i in range(len(grid) - 1, -1, -1):  # 20 vegades
            row = grid[i]
            if (0, 0, 0) not in row:
                ind[inc] = i
                inc += 1
        for i in range(4):
            for j in range(10):
                if ind[i] > 0:
                    grid[ind[i]][j] = (69, 69, 69)  # seleccionar les linees

        for j in range(len(grid[1])):  # veure si hi ha forats a partir dels canvis de espai buit a espai pintats (comprova de dalt cap abaix i d'equerra a dreta)
            no = 0
            si = 0
            dis = 0
            for i in range(len(grid)):
                if grid[i][j] != (69, 69, 69):  # fer veure que les linees seleccionades no existeixen
                    if grid[i][j] != (0, 0, 0):
                        if no == 0:
                            no = 1
                        if si == var:
                            dis += 1
                    else:
                        if no == 1:
                            suma += 1
                            si = 1
                else:
                    lin += 1
            if si == 0:
                dis = 0
            total += dis
        if cas == 1:
            return suma  # tornar els forats

        elif cas == 2:

            return int(lin / 10)

        elif cas == 3 or cas == 5:
            return total
        elif cas == 4:
            for i in range(len(grid)):
                pol = len(grid) - i - 1
                for j in range(len(grid[1])):
                    if grid[pol][j] != (0, 0, 0):
                        final = final + lol
                lol = lol / 10
            return final
        elif cas == 6:
            for i in range(len(grid)):
                pol = len(grid) - i - 1
                canvi = 2
                for j in range(len(grid[1])):
                    can = canvi
                    if grid[pol][j] == (0, 0, 0):
                        canvi = 1
                    else:
                        canvi = 2
                    if can != canvi:
                        if canvi == 1:
                            final = final + lol
                lol = lol / 10
            return final


    def comprovar_una(win1, grid, x, cas):
        suma = 0
        no = 0
        ind = [0, 0, 0, 0]
        inc = 0
        if cas == 1:
            for i in range(len(grid) - 1, -1, -1):  # 20 vegades
                row = grid[i]
                if (0, 0, 0) not in row:
                    ind[inc] = i
                    inc += 1
            for i in range(4):
                for j in range(10):
                    if ind[i] > 0:
                        grid[ind[i]][j] = (69, 69, 69)  # seleccionar les linees
        for i in range(len(grid)):
            if grid[i][x] != (69, 69, 69):
                if grid[i][x] != (0, 0, 0):
                    if no == 0:
                        no = 1
                else:
                    if no == 1:
                        suma += 1
        return suma


    def no_treure_linees(win1,
                         grid):  # lo mateix que ha dalt pero sense treure les linees, ens servira sol per arreglar un bug improvable
        suma = 0
        for j in range(len(grid[1])):
            no = 0
            for i in range(len(grid)):
                if grid[i][j] != (0, 0, 0):
                    if no == 0:
                        no = 1
                else:
                    if no == 1:
                        suma += 1
        return suma


    def draw_window(surface, grid, hola, linee, ni):  # crear la panatalla
        surface.fill((0, 0, 0))
        pygame.font.init()
        with open('score', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()
        font = pygame.font.SysFont("arial", 60, bold=True)
        stil = pygame.font.SysFont("arial", 30, bold=True)
        lod = pygame.font.SysFont("arial", 20, bold=True)
        label = font.render("TETRIS", 1, (255, 255, 255))
        if hola < 10000000:  # fer mes petit el text si no cap
            punts = stil.render("Puns: " + str(hola), 1, (255, 255, 255))
        else:
            punts = lod.render("Puns: " + str(hola), 1, (255, 255, 255))
        lin = stil.render("Linees: " + str(linee), 1, (255, 255, 255))
        lev = stil.render("Nivell: " + str(ni), 1, (255, 255, 255))
        if int(score) < 10000000:
            best = stil.render("Record: " + str(score), 1, (255, 255, 255))
        else:
            best = lod.render("Record: " + str(score), 1, (255, 255, 255))
        surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 15))
        surface.blit(best, (660 - (label.get_width() / 2), 600))
        surface.blit(punts, (120 - (label.get_width() / 2), 160))
        surface.blit(lin, (120 - (label.get_width() / 2), 120))
        surface.blit(lev, (120 - (label.get_width() / 2), 80))
        for i in range(len(grid)):  # y
            for j in range(len(grid[i])):  # x
                pygame.draw.rect(surface, grid[i][j],
                                 (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size),
                                 0)  # es on crea(pinta) tots els blocs a partir de les dades recollides a grid
        pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)  # dibuixar limits
        draw_grid(surface, grid)
        # pygame.display.update()


    def main(win):
        IA = 0  # desideix el tipus de jugavilitat
        dada=0
        pulsat=0
        # A IA=1:
        cont = 0
        continua = 0
        res = 0  # resultat
        antigues = {}  # per arreglar un bug
        millori = 0  # guarda la pocicio de la llista de la millor jugada
        mijualt = 0  # la millor altura
        miju = 0  # la jugada amb menos forats, no es pot iniciar a 0
        equis = 0  # 1 #controla la x de les peces que estan buscant posibles jugades
        igrega = 23  # controla la y de les peces que estan buscant posibles jugades
        gir = 0  # controla el gir de les peces que estan buscant posibles jugades
        mov = 0  # controlador de a quina posible jugada estem
        forats = {}  # lloc on es guarden els forats de cada posible jugada
        altura = {}  # lloc on es guarden les altures de cada posible jugada
        disfo = {}  # lloc on es guarden les distancies als forats de cada posible jugada funciona igual que les altres linees
        rows = {}  # lloc on es guarden les linees de cada posible jugada funciona igual que les altres linees
        dith = {}  # lloc on es guarden la quantitat de blocs a la x com mes avall posible de cada posible jugada funciona igual que les altres linees (distancia total height)
        forax = {}  # lloc on es guarden els forats a la x com mes avall posible on en teoria de cada jugada posible funciona igual que les altres linees
        # A IA=0:
        left = 0  # tirar cap a l'esquerra
        right = 0  # tirar cap a la dreta
        dawn = 0  # tirar cap abaix
        level = 1  # el nivell
        clock = pygame.time.Clock()  # rellotge que fa que la variable de baix vagi augmentant amb el temps
        fall_time = 0  # variable que va augmentant constant amb el temps

        var = 0  # on guardo les linies fetes en una sola tirada
        lines = 0  # les linies
        points = 0  # els punts
        record = 0  # el record
        locked_positions = {}  # les pocicions ocupades per fitxes que no es poden moure
        grid = create_grid(locked_positions)  # graella,les pocicions ocupades per fitxes
        change_piece = False  # per saver quan s'ha de canviar la peça
        run = True  # per mantindre el bucle i per quan vulgui sortir
        current_piece = get_shape()  # peça actual
        next_piece = get_shape()  # seguent peça

        for i in range(300):  # reinici de forats
            forats[i] = -1

        fall_speed = 0.20  # velocitat de caiguda
        mov_time = 0  # variable que va augmentant constant amb el temps
        mov_speed = 0.1  # sensiblitat
        pause = 0  # pausa
        while run:
            if IA == 0:  # Juga una persona

                if pause == 0:
                    grid = create_grid(locked_positions)  # assigna a grid totes les posicions bloquejades
                    if lines > level * 10 and level < 10:  # augmentar el nivell cada 10 linees
                        level += 1
                    fall_time += clock.get_rawtime()
                    mov_time += clock.get_rawtime()
                    clock.tick()
                    if mov_time / 750 > mov_speed:  # rellotge de moviment pulsant tecla
                        mov_time = 0
                        if right == 1:
                            current_piece.x += 1
                            if not (valid_space(current_piece, grid, IA)):  # si el moviment no es valit tornar a l'anterior
                                current_piece.x -= 1
                        if left == 1:
                            current_piece.x -= 1
                            if not (valid_space(current_piece, grid, IA)):
                                current_piece.x += 1
                        if dawn == 1:
                            current_piece.y += 1
                            if not (valid_space(current_piece, grid, IA)):
                                current_piece.y -= 1

                    if fall_time / (
                            1200 - level * 75) > fall_speed:  # rellotge de caiguda de peça, cada vegada és mes rapid
                        fall_time = 0
                        current_piece.y += 1
                        if not (valid_space(current_piece, grid, IA)) and current_piece.y > 0:  # caiguda i fins quan
                            current_piece.y -= 1
                            change_piece = True
                    bluetooth.flushInput()
                    input_data = bluetooth.readline()#decode
                    print(input_data)
                    dada=input_data.splitlines()
                    dada=str(dada[0])
                    dada=dada.replace("b","")
                    dada=dada.replace("'","")
                    print(dada)
                    if dada=="1":
                        dawn = 0
                        right=0
                        left = 1
                        pulsat = 0
                    elif dada=="3":
                        dawn = 0
                        left = 0
                        right=1
                        pulsat = 0
                    elif dada=="4":
                        dawn = 1
                        left = 0
                        right=0
                        pulsat = 0
                    elif dada=="2":
                        dawn = 0
                        right = 0
                        left = 0
                        if pulsat==0:
                            pulsat=1
                            current_piece.rotation += 1
                            if not (valid_space(current_piece, grid, IA)):
                                current_piece.rotation -= 1
                    elif dada=="0":
                        right=0
                        left=0
                        pulsat=0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        """if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT:  # dir que has aixecat el boto
                                left = 0
                            if event.key == pygame.K_RIGHT:
                                right = 0
                            if event.key == pygame.K_DOWN:
                                dawn = 0
    
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:  # dir que has pulsat el boto
                                left = 1
                            if event.key == pygame.K_RIGHT:
                                right = 1
                            if event.key == pygame.K_SPACE:
                                pause = 1
                                ran = random.randint(1, 2)
                            if event.key == pygame.K_r:
                                main_menu(win)
                            if event.key == pygame.K_DOWN:
                                dawn = 1
                            if event.key == pygame.K_UP:  # canviar la posició de la llista de la pesa, o sigui la rotació
                                current_piece.rotation += 1
                                if not (valid_space(current_piece, grid, IA)):
                                    current_piece.rotation -= 1"""
                    shape_pos = convert_shape_format(current_piece)  # cordenades de cada bloc de la fitxa
                    if (valid_space(current_piece, grid, IA)):
                        for i in range(len(shape_pos)):
                            x, y = shape_pos[i]
                            if y > -1:
                                grid[y][
                                    x] = current_piece.color  # pot quedar xulo:(225,225,225) #assigna les cordenades que son correctes de la fixa que esta caient a grid amb el seu corresponent color
                    if change_piece:  # canvi de peça
                        # comprovar_forats(win,grid,6) #m'ajuda a comprovar coses de IA=1
                        for pos in shape_pos:
                            p = (pos[0], pos[1])
                            locked_positions[p] = current_piece.color  # afegir la peça anterior a les pocisions fixes
                        current_piece = next_piece  # canviar fitxa
                        next_piece = get_shape()  # elegir la seguent
                        var = clear_rows(win, grid, locked_positions, next_piece, points, lines,
                                         level)  # veure les linees fetes en aquella jugada
                        lines += var
                        if var > 0:
                            points += (
                                                  var * var - var + 1) * 100 * level  # sistema de puntuació a partir del nivell i les linees fetes en una jugada
                        change_piece = False
                    if record == 0:  # si hi ha record canviar-lo
                        record = update_score(points)
                        if record == 1:
                            sound5.play()
                    else:
                        update_score(points)
                    draw_window(win, grid, points, lines, level)
                    draw_next_shape(next_piece, win)
                    pygame.display.update()  # actualitzar pantalla
                    if check_lost(locked_positions):  # Has perdut?
                        pygame.mixer.music.stop()
                        if record == 1:  # animació de record
                            win.fill((0, 0, 0))  # borrar tot lo que hi ha a la pagina
                            scale_x = 900
                            scale_y = int(scale_x / 600 * 338)
                            gif = pygame.image.load("good-job.jpg")
                            gif = pygame.transform.scale(gif, (scale_x, scale_y))
                            win.blit(gif, ((s_width - scale_x) / 2, (s_height - scale_y) / 2))
                            pygame.display.update()
                            # draw_text_middle("Nou record", win)
                            pygame.mixer.music.load("record.mp3")
                            pygame.mixer.music.play()
                            pygame.time.delay(3000)
                        win.fill((0, 0, 0))  # animació has perdut
                        scale_x = 900
                        scale_y = scale_x
                        im3 = pygame.image.load("game-over1.jpg")
                        im3 = pygame.transform.scale(im3, (scale_x, scale_y))
                        win.blit(im3, ((s_width - scale_x) / 2, (s_height - scale_y) / 2))
                        pygame.display.update()
                        for i in range(10):
                            bluetooth.write(b'2')
                        # draw_text_middle("Has perdut :(",win)
                        pygame.mixer.music.load("lose.mp3")
                        pygame.mixer.music.play()
                        pygame.time.delay(3000)
                        main_menu(win)  # tornar a començar
                else:
                    win.fill((0, 0, 0))  # animació pause
                    pygame.mixer.music.pause()
                    if ran == 1:  # elegir canço aleatoria
                        sound4.play()
                    else:
                        sound3.play()
                    scale_x = 1000
                    scale_y = int(scale_x / 386 * 238)
                    im2 = pygame.image.load("cor.jfif")
                    im2 = pygame.transform.scale(im2, (scale_x, scale_y))
                    win.blit(im2, ((s_width - scale_x) / 2, (s_height - scale_y) / 2))
                    font = pygame.font.SysFont("arial", 80, bold=True)
                    label = font.render("Pausa", 1, (0, 0, 0))
                    win.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                                     (top_left_y + play_height / 2 - (label.get_width() / 2))))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:  # treure la pausa
                                pause = 0
                                sound3.stop()
                                sound4.stop()
                                pygame.mixer.music.unpause()

        return run


    def main_menu(win):
        run = True
        volum = 0
        sound1.play()
        pygame.mixer.music.load("intro.mp3")
        pygame.mixer.music.play(-1)  # reproduir infinites vegades
        pygame.mixer.music.set_volume(volum)
        sound1.set_volume(volum)
        sound2.set_volume(volum)
        sound3.set_volume(volum)
        sound4.set_volume(volum)
        sound5.set_volume(volum)
        for i in range(10):
            bluetooth.write(b'1')
        while run:
            win.fill((0, 0, 0))
            scale_x = int(700 * 1920 / 1080)  # 800
            scale_y = int(scale_x * 1080 / 1920)  # per mantidre la relacio y/x de la imatge
            im1 = pygame.image.load("tetris.jpg")
            im1 = pygame.transform.scale(im1, (scale_x, scale_y))
            win.blit(im1, ((s_width - scale_x) / 2, (s_height - scale_y) / 2))
            font = pygame.font.SysFont("arial", 80, bold=True)
            label = font.render("Clica qualsevol tecla", 1, (0, 0, 0))
            bluetooth.flushInput()
            input_data = bluetooth.readline()
            dada = input_data.splitlines()
            dada = str(dada[0])
            dada = dada.replace("b", "")
            dada = dada.replace("'", "")
            win.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                             (top_left_y + play_height / 2 - (label.get_width() / 2) + 20)))
            # print(top_left_x + play_width / 2 - (label.get_width() / 2),(top_left_y + play_height / 2 - (label.get_width() / 2)))
            pygame.display.update()
            if dada=="1" or dada=="2" or dada=="3" or dada=="4":#no he ficat que no sigui igual a 0 pels strings
                pygame.mixer.music.load("tetris.mp3")
                sound1.stop()
                pygame.mixer.music.play(-1)
                run = main(win)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # començar a jugar quan cliquis algo
                    pygame.mixer.music.load("tetris.mp3")
                    sound1.stop()
                    pygame.mixer.music.play(-1)
                    run = main(win)
                if event.type == pygame.QUIT:  # tancar pantalla quan cliquis la creueta
                    run = False
        bluetooth.close()
        pygame.display.quit()


    win = pygame.display.set_mode((s_width, s_height))  # crear finestra
    pygame.display.set_caption("Tetris")
    main_menu(win)

    # depen de les peces que surt, tambe podia haver fet que calcules la seguent fitxa ,ho podria tirar cap el costat les peces en ple moviment, es podria fer millor posant més parametres de decició pero mes o menys ja esta be           o fent un calcul que em relaciones la altura amb els forats(aixo seria ML?)(en plan repartir importancia o si hi ha una que s'ayunya molt de lo altre ) incluir el maxim de les linees fetes(mes important que altura). Algunes altures poches
    # el problema es que es fan torres cap a dalt
    # exportar
"""except:
    print("hola")#fer una funcio recursiva"""

