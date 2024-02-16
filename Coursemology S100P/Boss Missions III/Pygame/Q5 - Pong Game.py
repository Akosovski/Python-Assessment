import pygame
import sys

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

paddle_width, paddle_height = 80, 10
paddle_x = width // 2 - paddle_width // 2
paddle_y = height // 2 - paddle_height // 2
paddle_speed = 0.09

ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 0.07, 0.07

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x

    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_speed_x = -ball_speed_x

    screen.fill(black)
    pygame.draw.rect(screen, red, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, green, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.update()