import pygame
from pygame import *

pygame.init()


width,height = 500,700

screen = pygame.display.set_mode((width,height))


rect1 = pygame.Surface((380,100))
drop = pygame.image.load('Dark eyes.JPG')
drop_rect = drop.get_rect()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill('grey')
    rect1.fill('orange')
    screen.blit(drop, drop_rect,(0,0,w,h))
    screen.blit(rect1,(10,10))
    pygame.display.update()
pygame.quit()
