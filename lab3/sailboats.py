import pygame
from pygame.draw import *

pygame.init()

FPS = 30
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

COLORS = {
    "BLUE": (0, 0, 255),
    "BLUE_LIGHT": (51, 255, 255),
    "YELLOW": (230, 230, 0),
    "WHITE": (240, 240, 240),
    "RED": (255, 0, 0),
    "BLACK": (0, 0, 0),
    "BROWN": (204, 102, 0),
    "PINK": (255, 153, 153),
    "GRAY": (190, 190, 190),
}


def draw_back():
    screen.fill(COLORS["BLUE_LIGHT"])
    rect(screen, COLORS["BLUE"], (0, HEIGHT // 7 * 3, WIDTH, HEIGHT // 7 * 4))
    rect(screen, COLORS["YELLOW"], (0, HEIGHT // 7 * 5, WIDTH, HEIGHT // 7 * 2))


def draw_waves():
    radius = 30
    shift = 2 * radius - 15
    x_coord = 0
    while x_coord <= WIDTH:
        circle(screen, COLORS["BLUE"], (x_coord, HEIGHT // 7 * 5 - 20), radius, 0)
        x_coord += shift
        circle(screen, COLORS["YELLOW"], (x_coord, HEIGHT // 7 * 5 + 20), radius, 0)
        x_coord += shift


def draw_sun():
    radius = 50
    circle(screen, COLORS["YELLOW"], (WIDTH // 6 * 5, HEIGHT // 7), radius, 0)


def draw_cloud(coords, radius):
    circle(screen, COLORS["GRAY"], coords, radius, 2)
    circle(screen, COLORS["WHITE"], coords, radius - 2, 0)

    circle(screen, COLORS["GRAY"], (coords[0] + radius // 5 * 4, coords[1] - radius // 5 * 4), radius, 2)
    circle(screen, COLORS["WHITE"], (coords[0] + radius // 5 * 4, coords[1] - radius // 5 * 4), radius - 2, 0)

    circle(screen, COLORS["GRAY"], (coords[0] + 2 * radius // 5 * 4, coords[1]), radius, 2)
    circle(screen, COLORS["WHITE"], (coords[0] + 2 * radius // 5 * 4, coords[1]), radius - 2, 0)

    circle(screen, COLORS["GRAY"], (coords[0] + 3 * radius // 5 * 4, coords[1] - radius // 5 * 4), radius, 2)
    circle(screen, COLORS["WHITE"], (coords[0] + 3 * radius // 5 * 4, coords[1] - radius // 5 * 4), radius - 2, 0)

    circle(screen, COLORS["GRAY"], (coords[0] + 4 * radius // 5 * 4, coords[1]), radius, 2)
    circle(screen, COLORS["WHITE"], (coords[0] + 4 * radius // 5 * 4, coords[1]), radius - 2, 0)


def draw_boat(coords, size):
    rect(screen, COLORS["BROWN"], (coords[0], coords[1], size, size // 4))
    circle(screen, COLORS["BROWN"], coords, size // 4, 0, draw_bottom_left=True)
    polygon(screen, COLORS["BROWN"], [
        (coords[0] + size, coords[1]),
        (coords[0] + 6 * size // 4, coords[1]),
        (coords[0] + size, coords[1] + size // 4),
        (coords[0] + size, coords[1]),
    ])
    circle(screen, COLORS["BLACK"], (coords[0] + 9*size//8, coords[1] + size//10), size // 15, 0)
    circle(screen, COLORS["WHITE"], (coords[0] + 9*size//8, coords[1] + size//10), size // 25, 0)

    line(screen, COLORS["BLACK"],
         [coords[0] + size//3, coords[1]],
         [coords[0] + size//3, coords[1] - size], size//20)

    polygon(screen, COLORS["GRAY"], [
        (coords[0] + size//40 + size//3, coords[1] - size),
        (coords[0] + size//40 + size, coords[1] - size//2),
        (coords[0] + size//40 + size//2, coords[1] - size//2),
        (coords[0] + size//40 + size//3, coords[1] - size),
    ])
    polygon(screen, COLORS["GRAY"], [
        (coords[0] + size//40 + size, coords[1] - size//2),
        (coords[0] + size//40 + size//2, coords[1] - size//2),
        (coords[0] + size//40 + size//3, coords[1]),
        (coords[0] + size//40 + size, coords[1] - size//2),
    ])

    polygon(screen, COLORS["BLACK"], [
        (coords[0] + size//40 + size//3, coords[1] - size),
        (coords[0] + size//40 + size, coords[1] - size//2),
        (coords[0] + size//40 + size//2, coords[1] - size//2),
        (coords[0] + size//40 + size//3, coords[1] - size),
    ], 1)
    polygon(screen, COLORS["BLACK"], [
        (coords[0] + size//40 + size, coords[1] - size//2),
        (coords[0] + size//40 + size//2, coords[1] - size//2),
        (coords[0] + size//40 + size//3, coords[1]),
        (coords[0] + size//40 + size, coords[1] - size//2),
    ], 1)


draw_back()
draw_waves()
draw_sun()

draw_cloud((80, 130), 30)
draw_cloud((300, 50), 20)

draw_boat((100, 200), 100)
draw_boat((300, 220), 150)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
