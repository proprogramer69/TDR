import random
import time
import kivy
from kivy.app import App
from kivy.uix.label import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Line
from kivy.graphics import Color
from kivy.clock import Clock

#el codi és gairebe igual que el tetris altre, pero en aquest els eixos estan girats

s_width = 1920
s_height = 1080
play_width = s_width
play_height = s_height

block_size = 108

top_left_x = s_width-(20*108)
top_left_y = 0


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

I = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '.0000',
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

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (225,225,225), (0, 0, 255), (128, 0, 128)]

mode=0#mode de pantalla partida, per l'altre mode posar un 1 en lloc d'un 0


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x+2
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = -1


def create_grid(locked_positions={}):

    grid = [[(0, 0, 0) for x in range(20)] for x in range(10)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((shape.y + j, shape.x + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions





def valid_space(shape, grid, IA):

    accepted_pos = [[(j, i) for j in range(20) if grid[i][j] == (0, 0, 0)] for i in range(10)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:

                return False
    return True


def check_lost(positions):
    for pos in positions:
        y, x = pos
        if y < 1:
            return True
    return False


def get_shape():
    var = random.choice(shapes)
    return Piece(5, 0, var)





def clear_rows(grid, locked):
    inc = 0
    loco=1
    ind = [0, 0, 0, 0]
    for i in range(len(grid[1])):
        for j in range(len(grid)):
            if grid[j][i]==(0, 0, 0):
                loco=0
        if loco==1:
                ind[inc] = i
                inc += 1
                print(ind)
                for j in range(10):
                    try:
                        del locked[(i, j)]
                    except:
                        continue
        loco=1

    pol=0
    if inc > 0:
        for i in range(4):
            for z in range(len(grid)):
                for j in range(len(grid[i])):
                    pol=20-j
                    if (pol,z) in locked_positions:
                        if pol < ind[i]:
                            locked_positions[(pol+1,z)]=locked_positions[(pol,z)]
                            del locked_positions[(pol, z)]


    return inc


IA=0
sx = top_left_x
sy = top_left_y
p=1
alt=0
left = 0
right = 0
dawn = 0
level = 1
fall_time = 0
var = 0
lines = 0
points = 0
locked_positions = {}
change_piece = False
current_piece = get_shape()
next_piece = get_shape()
loc=0
vel=0.2


class Touch(Widget):
    def __init__(self,**kwargs):
        super(Touch, self).__init__(**kwargs)
        self.rect = {}
        self.rect1 = {}
        Clock.schedule_interval(self.move, 0.4) #creacio de rellotges
        Clock.schedule_interval(self.costat, vel)
        Clock.schedule_interval(self.chupa, 0)

    def on_touch_move(self, touch):
        global locked_positions
        global pos1
        global pos2
        global pos3
        global pos6
        global pos5
        global pos7
        global right
        global left
        global ja
        pos7= touch.pos[1]
        pos6= touch.pos[0]
        print("hola")
        if abs(pos3-pos6) > abs(pos5-pos7):
            ja=1
        else:
            ja=0
            grid = create_grid(locked_positions)
            if current_piece.y>1:
                pos1 = current_piece.x
                pos2 = int(touch.pos[1] // 108 + 2)

                if change_piece == False:
                    if mode == 1:
                        if pos1 > pos2:
                            for i in range(pos1 - pos2):
                                current_piece.x += -1
                                if not (valid_space(current_piece, grid, IA)):
                                    current_piece.x -= -1
                        if pos1 < pos2:
                            for i in range(pos2 - pos1):
                                current_piece.x += 1
                                if not (valid_space(current_piece, grid, IA)):
                                    current_piece.x -= 1





    def on_touch_down(self, touch):#detectar quan toques la pantalla
        global left
        global right
        global s_height
        global alt
        global change_piece
        global pos3
        global pos5
        global locked_positions
        grid = create_grid(locked_positions)
        pos5 = touch.pos[1]
        pos3 = touch.pos[0]
        if change_piece == False:
            if mode==0:
                if touch.pos[0] > s_width*4/5:
                    current_piece.rotation -= 1
                    if not (valid_space(current_piece, grid, IA)):
                        current_piece.rotation += 1
                elif touch.pos[0] < s_width*1/5:
                    if current_piece.y>1:
                        while True:
                            current_piece.y += 1
                            if not (valid_space(current_piece, grid, IA)):
                                current_piece.y -= 1
                                change_piece=True
                                break
                else:
                    if touch.pos[1] >= s_height/2:
                        left=1
                        current_piece.x += 1
                        if not (valid_space(current_piece, grid, IA)):
                            current_piece.x -= 1
                    else:
                        right = 1
                        current_piece.x -= 1
                        if not (valid_space(current_piece, grid, IA)):
                            current_piece.x += 1







    def on_touch_up(self, touch):
        global left
        global right
        global pos3
        global pos4
        global change_piece
        global locked_positions
        grid = create_grid(locked_positions)
        pos4 = touch.pos[0]
        if change_piece == False:
            if mode == 1 and ja==1:
                 if pos3 > pos4+200:
                     current_piece.rotation -= 1
                     if not (valid_space(current_piece, grid, IA)):
                         current_piece.rotation += 1
                 if pos3 < pos4 - 200:
                     if current_piece.y > 1:
                         while True:
                             current_piece.y += 1
                             if not (valid_space(current_piece, grid, IA)):
                                 current_piece.y -= 1
                                 change_piece = True
                                 break
        if mode==0:
            right=0
            left=0
        pos3 = 0


    def costat(self,dt):
        global current_piece
        global left
        global right
        global alt
        global dawn
        global grid
        global IA
        global locked_positions
        global change_piece
        global ja
        grid = create_grid(locked_positions)
        if change_piece == False:
            if right == 2:
                current_piece.x -= 1
                if not (valid_space(current_piece, grid, IA)):
                    current_piece.x += 1
            if left == 2:
                current_piece.x += 1
                if not (valid_space(current_piece, grid, IA)):
                    current_piece.x -= 1
            if dawn == 1:
                current_piece.y += 1
                if not (valid_space(current_piece, grid, IA)):
                    current_piece.y -= 1
            if right == 1:
                right = 2
            if left == 1:
                left = 2
    def move(self,dt):
        global IA
        global locked_positions
        global current_piece
        global change_piece
        global dawn
        grid = create_grid(locked_positions)
        if change_piece==False:
            current_piece.y += 1
            if not (valid_space(current_piece, grid, IA)) and current_piece.y > 0:
                current_piece.y -= 1
                dawn=0
                change_piece = True

    def chupa(self, dt):
        global IA
        global a
        global left
        global right
        global dawn
        global level
        global fall_time
        global var
        global lines
        global points
        global locked_positions
        global change_piece
        global current_piece
        global next_piece
        global p
        global loc


        a = 0
        grid = create_grid(locked_positions)
        shape_pos = convert_shape_format(current_piece)
        if (valid_space(current_piece, grid, IA)):
            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_piece.color
        if change_piece==True:

            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
                with self.canvas:
                    self.rect1[loc] = Rectangle(
                        pos=(top_left_x + pos[0] * block_size, top_left_y + pos[1] * block_size),
                        size=(block_size, block_size))
                    loc += 1
            current_piece = next_piece
            next_piece = get_shape()
            var = clear_rows(grid, locked_positions)
            if var > 0:
                for i in range(len(self.rect1)):
                    self.canvas.remove(self.rect1[i])
                loc = 0
                grid = create_grid(locked_positions)
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j] != (0, 0, 0):
                            with self.canvas: #indicar que utilitzaras el canvas
                                Color(grid[i][j][0], grid[i][j][1], grid[i][j][2], mode="rgba")
                                self.rect1[loc] = Rectangle(
                                    pos=(top_left_x + j * block_size, top_left_y + i * block_size),
                                    size=(block_size, block_size))#crear bloc
                                loc += 1
            p = 0

            change_piece = False
        for i in range(len(self.rect)):
            self.canvas.remove(self.rect[i])
        a = 0
        with self.canvas:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] != (0, 0, 0):
                        if (j, i) not in locked_positions:
                            Color(grid[i][j][0], grid[i][j][1], grid[i][j][2], mode="rgba")
                            self.rect[a] = Rectangle(pos=(top_left_x + j * block_size, top_left_y + i * block_size),
                                                     size=(block_size, block_size))
                            a += 1
        p += 1
        a = 0

        if check_lost(locked_positions):
            MyApp().stop()

class MyApp(App):
    def build(self):
        return Touch()

if __name__=="__main__":
    MyApp().run()

