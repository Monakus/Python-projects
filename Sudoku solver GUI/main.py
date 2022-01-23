import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Sudoku solver")

FONT = pygame.font.SysFont('Arial', 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 540, 540
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SQUARE_SIZE = SCREEN_WIDTH/9


class Tile:
    def __init__(self, val=0, pos=(0, 0), color=WHITE):
        self.val = val
        self.pos = pos
        self.color = color


class Board:
    tiles = []

    def __init__(self, bo):
        for i in range(9):
            inner_tiles = []
            for j in range(9):
                inner_tiles.append(Tile(bo[i][j], (i, j)))
            self.tiles.append(inner_tiles)

        pygame.display.update()
        pygame.time.delay(20)

    def draw(self):
        for inner_tiles in self.tiles:  # draw all the tiles
            for tile in inner_tiles:
                pygame.draw.rect(SCREEN, tile.color, (tile.pos[1] * SQUARE_SIZE, tile.pos[0] * SQUARE_SIZE, SQUARE_SIZE - 1, SQUARE_SIZE - 1))
                if tile.val == 0:
                    continue
                text = FONT.render(str(tile.val), True, BLACK)
                SCREEN.blit(text, (tile.pos[1] * SQUARE_SIZE + 20, tile.pos[0] * SQUARE_SIZE))

        for i in range(4):  # draw tile that spearate the boxes
            pygame.draw.line(SCREEN, BLACK, (i * SCREEN_WIDTH/3, 0), (i * SCREEN_WIDTH/3, SCREEN_WIDTH), 4)
            pygame.draw.line(SCREEN, BLACK, (0, i * SCREEN_WIDTH/3), (SCREEN_WIDTH, i * SCREEN_WIDTH/3), 4)

        pygame.display.update()
        pygame.time.delay(20)

    def _find_empty(self):
        for inner_tiles in self.tiles:
            for tile in inner_tiles:
                if tile.val == 0:
                    return tile
        return None

    def _is_valid(self, t, num):
        row = t.pos[0]
        col = t.pos[1]
        for tile in self.tiles[row]:
            if tile.val == num:  # check row
                return False

        for i in range(9):
            if self.tiles[i][col].val == num:  # check column
                return False

        box_row, box_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.tiles[box_row + i][box_col + j].val == num:  # check the box
                    return False
        return True

    def solve(self):
        pygame.event.pump()
        tile = self._find_empty()
        if tile is None:  # if there are no empty cells, we are done
            return True
        for num in range(1, 10):
            if self._is_valid(tile, num):  # check if this number can be put in that cell
                tile.val = num
                tile.color = GREEN
                self.draw()
                if self.solve():
                    return True
                tile.val = 0
                tile.color = RED
                self.draw()
        return False  # triggers backtracking


grid = [[0, 6, 0, 0, 0, 7, 0, 0, 1],
        [0, 0, 1, 0, 8, 0, 7, 6, 2],
        [2, 0, 0, 0, 1, 0, 4, 0, 0],
        [0, 9, 0, 0, 0, 8, 0, 0, 5],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 3, 0, 5, 6, 0, 2, 0, 0],
        [9, 0, 0, 8, 0, 0, 5, 0, 0],
        [0, 0, 8, 7, 4, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 8, 0, 0]]


board = Board(grid)
board.draw()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                board.solve()
