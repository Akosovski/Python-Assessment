import pygame
import sys

pygame.init()

width, height = 300, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Shapes in Pygame")

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

circle_radius = 15
circle_x = width - 100
circle_y = height // 2
circle_speed = 10

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    circle_y += circle_speed
    if circle_y - circle_radius <= 0 or circle_y + circle_radius >= height:
        circle_speed = -circle_speed

    screen.fill(black)
    pygame.draw.circle(screen, green, (circle_x, circle_y), circle_radius)
    pygame.display.update()
    clock.tick(60)
