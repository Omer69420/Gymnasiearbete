import pygame
from pygame.locals import *
pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Båtspel')


boat = pygame.image.load(r'images\gymnasiearbete2d.png')

run = True
while run:

    screen.blit(boat, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
