import pygame
from pygame.locals import *
import sys
import math
pygame.init()

screen = pygame.display.set_mode(size=(500, 500))
pygame.display.set_caption("The Pie Game - Press 1, 2, 3, 4")
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius
textImage = myfont.render("Hello pygame", True, white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))

    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)
    pygame.draw.rect(screen, color, (*position, *position), width)
    pygame.display.update()
