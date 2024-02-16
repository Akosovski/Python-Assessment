import pygame
import sys

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

black = (0, 0, 0)
green = (0, 255, 0)

circle_radius = 15
circle_x = width - 100
circle_y = height // 2
circle_speed = 500

clock = pygame.time.Clock()

move_up = False
move_down = False
move_left = False
move_right = False

while True:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False

    if move_up:
        circle_y -= circle_speed * dt
    if move_down:
        circle_y += circle_speed * dt
    if move_left:
        circle_x -= circle_speed * dt
    if move_right:
        circle_x += circle_speed * dt

    circle_x = max(0, min(width - circle_radius, circle_x))
    circle_y = max(0, min(height - circle_radius, circle_y))

    screen.fill(black)
    pygame.draw.circle(screen, green, (int(circle_x), int(circle_y)), circle_radius)
    pygame.display.update()