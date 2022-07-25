import pygame

width = 800
height = 600

x = 400
y = 300
delta_x = 20
delta_y = 0

body = [(x, y)]




point = 0


def window():
    width = 800
    height = 600
    pygame.init()
    pygame.display.set_caption('Simple Snake')
    screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))        # Game screen resolution


grid_size = 20
grid_width = 820 / grid_size        # Grid parameters
grid_hight = 600 / grid_size

def grid():
    for y in range(0, int(grid_hight)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(screen, (11, 140, 35), r)                                       # Drawing grid
            else:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(screen, (11, 130, 35), r)

background = pygame.image.load("images\menubg.png")
start_button = pygame.image.load('images\play.png').convert_alpha()
exit_button = pygame.image.load('images\exit.png').convert_alpha()

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

button1 = Button(300, 200, start_button)
button2 = Button(300, 400, exit_button)

class Cube:
    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, (self.color), [self.i, self.j, 20, 20])



purple = Cube(10, 10, (139, 12, 145))
red = Cube(10, 60, (255, 0, 0))
green = Cube(10, 110, (100, 180, 100))
black = Cube(10, 160, (0, 0, 0))



def msg(text, y, z):
    msg_font = pygame.font.SysFont('Comic Sans MS', 20)
    msg_type = msg_font.render(str(text), True, (0, 0, 0))
    screen.blit(msg_type, [y, z])
