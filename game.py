import pygame
import random
import requests
import utils
import ctypes
user32 = ctypes.windll.user32
screenheight =  int(user32.GetSystemMetrics(1))
screenwidth =  int(user32.GetSystemMetrics(0))

height = screenheight - 30
width = (screenheight / 2.5) * 2

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("GAME")


carImg = utils.loadImageScaled("car.png", 0.1)
bgImg = utils.loadImageSized(
    "road.png", screen.get_width(), screen.get_height())
hole = utils.loadImageScaled("img/obstacle/hole.png",0.11)

score = 0
i = 0
a = 0
c = 0

clock = pygame.time.Clock()
running = True
carPos = [int(screen.get_width()) / 2 - int(carImg.get_width()) / 2, 10]

font = pygame.font.Font(None, 36)

while running:
    score+=1
   

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            bgImg = utils.loadImageSized("road.png", screen.get_width(), screen.get_height())
            i = 0
            pygame.display.update()

            

    screen.fill((0, 0, 0))
    screen.blit(bgImg, (0, i))
    screen.blit(bgImg, (0, screen.get_height() + i))

    screen.blit(hole, (c, screen.get_height()+a))
    print(c)

    if (i <= -screen.get_height()):
        screen.blit(bgImg, (0, screen.get_height()-i))
        i = 0
    i -= 20

    if (a <= -screen.get_height()-500):
        a = 0
        c = random.randint(0, screen.get_width() )
    a -= 20

    move_ticker = 0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if move_ticker == 0:
            move_ticker = 10
            carPos[0] -= 5
            if carPos[0] < 0:
                carPos[0] = 0
    if keys[pygame.K_RIGHT]:
        if move_ticker == 0:   
            move_ticker = 10     
            carPos[0]+=5
            if carPos[0] > screen.get_width() - carImg.get_width(): 
                carPos[0] = screen.get_width() - carImg.get_width()

    screen.blit(carImg, (carPos[0], carPos[1]))

    if move_ticker > 0:
        move_ticker -= 1

    scoreText = font.render(str(score), True, (255, 255, 255))
    screen.blit(scoreText, (10, 10))


    pygame.display.update()
    
    clock.tick(60)
pygame.quit()
