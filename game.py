import pygame
import random
import pygame_textinput
import requests
import utils
import ctypes

user32 = ctypes.windll.user32
screenheight = int(user32.GetSystemMetrics(1))
screenwidth = int(user32.GetSystemMetrics(0))

height = screenheight - 30
width = (screenheight / 2.5) * 2

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode(size=(width, height-50))
pygame.display.set_caption("Car Game")

carImg = utils.loadImageScaled("img/car.png", 0.1)
# Drehen Sie das Auto um 180 Grad
carImg = pygame.transform.flip(carImg, False, True)
bgImg = utils.loadImageSized("img/road.png", screen.get_width(), screen.get_height())
hole = utils.loadImageScaled("img/obstacle/hole.png", 0.11)

score = 0
i = 0
a = -screen.get_height()  # Startposition oberhalb des Bildschirms
c = random.randint(0, screen.get_width())

gameOver = False
started = False

clock = pygame.time.Clock()
running = True
carPos = [int(screen.get_width()) / 2 - int(carImg.get_width()) / 2, screen.get_height() - int(carImg.get_height()) - 10]

speed_increase = 0.1  # Geschwindigkeitszunahme pro Schleifendurchlauf
speed = 5  # Startgeschwindigkeit

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)
start_text = game_over_font.render("Car Game", True, (255, 0, 0))
start_button = pygame.Rect(325, 800, 200, 50)
name_input =  pygame_textinput.TextInputVisualizer()
username_input_boarder = pygame.Rect(325, 850, 200, 50)


def check_collision(car_pos, obstacle_pos):
    car_rect = pygame.Rect(car_pos[0], car_pos[1], carImg.get_width(), carImg.get_height())
    obstacle_rect = pygame.Rect(obstacle_pos[0], obstacle_pos[1], hole.get_width(), hole.get_height())
    return car_rect.colliderect(obstacle_rect)

while running:
    events = pygame.event.get()
    for event in events:
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.VIDEORESIZE:
             bgImg = utils.loadImageSized("road.png", screen.get_width(), screen.get_height())
             i = 0
             pygame.display.update()
         if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
            started = True     
    if not started:
        screen.fill((225, 225, 225))
        name_input.update(events)
        screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 4 - start_text.get_height() // 2))
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        pygame.draw.rect(screen, (255, 255, 255), start_button, 2)
        pygame.draw.rect(screen, (0, 255, 0), username_input_boarder)
        pygame.draw.rect(screen, (255, 255, 255), username_input_boarder, 2)
        start_button_text = font.render("Start", True, (255, 255, 255))
        screen.blit(start_button_text, (start_button.centerx - start_button_text.get_width() // 2, start_button.centery - start_button_text.get_height() // 2))
        screen.blit(name_input.surface, (username_input_boarder.left + 2, username_input_boarder.centery - start_button_text.get_height() // 2 ))
        if(len(name_input.value) > 14):
            name_input.value = name_input.value[:14]
        
    else:
        if(gameOver):
            game_over_text = game_over_font.render("Game Over | score: " + str(score), True, (255, 0, 0))
            screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
            
        else:
        
         score += 1
         
    
         screen.fill((0, 0, 0))
         screen.blit(bgImg, (0, i))
         screen.blit(bgImg, (0, i - screen.get_height()))
    
         screen.blit(hole, (c, a))
    
         if i >= screen.get_height():
             screen.blit(bgImg, (0, i - screen.get_height()))
             i = 0
             speed += speed_increase  # Erhöhe die Geschwindigkeit
    
         i += int(speed)
    
         if a >= screen.get_height() + 500:
             a = -screen.get_height()
             c = random.randint(0, screen.get_width())
         a += int(speed)
    
         move_ticker = 0
         keys = pygame.key.get_pressed()
         if keys[pygame.K_LEFT]:
             if move_ticker == 0:
                 move_ticker = 10
                 carPos[0] -= 5
                 if carPos[0] < 0:
                     carPos[0] = 0
         if keys[pygame.K_RIGHT]:
             if move_ticker == 0:
                 move_ticker = 10
                 carPos[0] += 5
                 if carPos[0] > screen.get_width() - carImg.get_width():
                     carPos[0] = screen.get_width() - carImg.get_width()
    
         screen.blit(carImg, (carPos[0], carPos[1]))
    
         if check_collision(carPos, (c, a)):
             gameOver = True  # Game Over bei Kollision
    
         if move_ticker > 0:
             move_ticker -= 1
    
         scoreText = font.render(str(score), True, (255, 255, 255))
         screen.blit(scoreText, (10, 10))
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
