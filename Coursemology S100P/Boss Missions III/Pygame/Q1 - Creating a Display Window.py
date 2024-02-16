import pygame
import sys

pygame.init()

width, height = 600, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello pygame!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()