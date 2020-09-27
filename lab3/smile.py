import pygame
from pygame.draw import *

pygame.init()

FPS = 30
WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

COLORS = {
    "GRAY": (192, 192, 192),
    "YELLOW": (230, 230, 0),
    "RED": (255, 0, 0),
    "BLACK": (0, 0, 0),
}

screen.fill(COLORS["GRAY"])

radius = 100

circle(screen, COLORS["BLACK"], (WIDTH // 2, HEIGHT // 2), radius, 3)
circle(screen, COLORS["YELLOW"], (WIDTH // 2, HEIGHT // 2), radius - 3, 0)
rect(screen, COLORS["BLACK"], (WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 20))

circle(screen, COLORS["BLACK"], (WIDTH // 2 - 40, HEIGHT // 2 - 40), radius // 5, 3)
circle(screen, COLORS["RED"], (WIDTH // 2 - 40, HEIGHT // 2 - 40), radius // 5 - 3, 0)
circle(screen, COLORS["BLACK"], (WIDTH // 2 - 40, HEIGHT // 2 - 40), radius // 7 - 3, 0)

circle(screen, COLORS["BLACK"], (WIDTH // 2 + 40, HEIGHT // 2 - 40), radius // 3, 3)
circle(screen, COLORS["RED"], (WIDTH // 2 + 40, HEIGHT // 2 - 40), radius // 3 - 3, 0)
circle(screen, COLORS["BLACK"], (WIDTH // 2 + 40, HEIGHT // 2 - 40), radius // 5 - 3, 0)

polygon(screen, COLORS["BLACK"], [(100, 100), (200, 50),
                                  (300, 100), (100, 100)])

polygon(screen, COLORS["BLACK"], [
    (WIDTH // 2 - 20, HEIGHT // 2 - 50),
    (WIDTH // 2 - 60, HEIGHT // 2 - 70),
    (WIDTH // 2 - 55, HEIGHT // 2 - 75),
    (WIDTH // 2 - 15, HEIGHT // 2 - 55),
    (WIDTH // 2 - 20, HEIGHT // 2 - 50),
])

polygon(screen, COLORS["BLACK"], [
    (WIDTH // 2 + 0, HEIGHT // 2 - 50),
    (WIDTH // 2 + 50, HEIGHT // 2 - 90),
    (WIDTH // 2 + 45, HEIGHT // 2 - 95),
    (WIDTH // 2 - 5, HEIGHT // 2 - 55),
    (WIDTH // 2 + 0, HEIGHT // 2 - 50),
])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
