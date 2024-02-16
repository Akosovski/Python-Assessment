import pygame
import sys

pygame.init()

width, height = 600, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shapes")

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

square_size = 50
square_x = 200
square_y = height // 2 - square_size // 2

circle_radius = 25
circle_x = width - 200
circle_y = height // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    pygame.draw.rect(screen, red, (square_x, square_y, square_size, square_size))
    pygame.draw.circle(screen, green, (circle_x, circle_y), circle_radius)

    pygame.display.update()