import pygame, random, time
from Func import grid, window, width, height, screen, x, y, delta_x, delta_y, point, body, background

window()         # Opening game window

game_over = False

font = pygame.font.SysFont("courier", 45)
sfont = pygame.font.SysFont("Comic Sans MS", 30)


class Berry:
    def __init__(self, color):
        self.color = color
        self.x = random.randrange(0, width) // 20 * 20
        self.y = random.randrange(0, height) // 20 * 20

    def draw(self):
        pygame.draw.rect(screen, (self.color), [self.x, self.y, 20, 20])

    def eat(self):
        global point
        if (self.x == x and self.y == y):
            while ((self.x, self.y) in body):
                self.x, self.y = random.randrange(0, width) // 20 * 20, random.randrange(0, height) // 20 * 20
                point += 1

        else:
            del body[0]
                                                                                                        ### Food classes
class Apple(Berry):

    def eat(self):
        global point
        if (self.x == x and self.y == y):
            while ((self.x, self.y) in body):
                self.x, self.y = random.randrange(0, width) // 20 * 20, random.randrange(0, height) // 20 * 20
                point += 3
                for i in range(3):
                    body.append((x, y))

class Bomb(Berry):

    def eat(self):
        global game_over
        if (self.x == x and self.y == y):
            while ((self.x, self.y) in body):
                self.x, self.y = random.randrange(0, width) // 20 * 20, random.randrange(0, height) // 20 * 20
                game_over = True

class Rotten_berry(Berry):
    def eat(self):
        global point
        if (self.x == x and self.y == y):
            while ((self.x, self.y) in body):
                self.x, self.y = random.randrange(0, width) // 20 * 20, random.randrange(0, height) // 20 * 20
                point -= 3
                for i in range(3):
                    del body[0]


berry = Berry((139, 12, 145))

apple = Apple((255, 0, 0))
                                                ## Food objects
bomb = Bomb((0, 0, 0))

rotten_berry = Rotten_berry((100, 180, 100))



def snake():
    global x, y, game_over, point, berry
    x = (x + delta_x) % width
    y = (y + delta_y) % height

    if((x, y) in body):
        game_over = True
        return
    body.append((x, y))

    berry.eat()

                                                                    ## Main game function
    grid()

    score = sfont.render(f"Score: {point}", True, (230, 136, 5))
    screen.blit(score, [0, 0])
    if point > 0:
        if point % 5 == 0:
            apple.draw()
            apple.eat()
    if point > 0:
        if point % 10 == 0:
            bomb.draw()
            bomb.eat()
        if point % 4 == 0:
            rotten_berry.draw()
            rotten_berry.eat()


    berry.draw()


    for(i, j) in body:
        pygame.draw.rect(screen, (181, 196, 15), [i, j, 20, 20])
        pygame.draw.rect(screen, (90, 12, 145), [i+4, j+4, 12, 12])
    pygame.display.update()


while True:
    if(game_over):
        pygame.display.update()
        screen.blit(background, (0, 0))
        msg = font.render("GAME OVER!", True, (0, 0, 0))
        screen.blit(msg, [275, 100])
        msg2 = font.render(f"Score: {point}", True, (0, 0, 0))
        screen.blit(msg2, [285, 200])
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        quit()


                                                                                        ## Main game loop
    pygame.time.delay(50)
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT) and x > 0:
                delta_x = -20
                delta_y = 0
            elif (event.key == pygame.K_RIGHT) and x < 780:
                delta_x = 20
                delta_y = 0                                                             ## Key's movement settings
            elif (event.key == pygame.K_UP) and y > 0:
                delta_x = 0
                delta_y = -20
            elif (event.key == pygame.K_DOWN) and y < 580:
                delta_x = 0
                delta_y = 20
            else:
                continue
            snake()
    if(not events):
        snake()         ## This keeps the player moving at the start of the game with no actions required
                        ## Also it keeps the loop from executing the game_over function at the beginning of game
                        ## otherwise snake will deal with del body[0] so the game will close immediately with game over result
