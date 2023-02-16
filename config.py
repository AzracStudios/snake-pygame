import pygame
from game import Game

pygame.init()
pygame.font.init()
pygame.display.set_caption("Snake")


class Config:
    CELL_WIDTH = 30  # WIDTH OF EACH CELL
    GRID_ROWS = 21   # NUMBER OF CELLS PER ROW

    WIN_WIDTH = CELL_WIDTH * GRID_ROWS  # WIDTH OF WINDOW

    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))

    FONT_L = pygame.font.Font("VT323-Regular.ttf", 70)
    FONT_S = pygame.font.Font("VT323-Regular.ttf", 30)

    BG_CELLS_CACHE = []

    FPS = 10

    ## COLORS ##
    CHECKER_LIGHT = (139, 201, 101)
    CHECKER_DARK = (127, 189, 89)
    SNAKE_HEAD = (66, 70, 179)
    SNAKE_BODY = (77, 81, 203)
    APPLE = (235, 87, 87)
    TEXT = (40, 40, 40)