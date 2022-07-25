import pygame, subprocess
from Func import window, screen, background, button1, button2, purple, red, green, black, msg
window()

font = pygame.font.SysFont("Comic Sans MS", 45)

gamefile = 'python game_file.py'



run = True
while run:

    screen.blit(background, (0, 0))
    if button1.draw():
        game = subprocess.Popen(gamefile, shell=True)
    if button2.draw():
        run = False

    purple.draw()
    red.draw()
    green.draw()
    black.draw()

    msg('= + 1 point and lenght', 35, 5)
    msg('= + 3 points and lenght', 35, 55)
    msg('= - 3 points and lenght', 35, 105)
    msg('= game over !', 35, 155)




    name = font.render("Snake", True, (20, 160, 0))
    screen.blit(name, [340, 50])


    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
