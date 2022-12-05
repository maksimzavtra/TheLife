import pygame
from config import *
from random import choice


class Board:
    def __init__(self, dim, screen):
        self.x_px = dim[0]
        self.y_px = dim[1]

        self.x = self.x_px // CELL_SIZE
        self.y = self.y_px // CELL_SIZE

        self.matrix = []
        for _ in range(self.x):
            row = [0] * self.y
            self.matrix.append(row)

        self.start = False

        self.screen = screen

    def add_cell(self, xy):
        if self.matrix[xy[0]][xy[1]] == 0:
            self.matrix[xy[0]][xy[1]] = 1
        else:
            self.matrix[xy[0]][xy[1]] = 0

    def draw_cell(self, xy):
        if self.matrix[xy[0]][xy[1]] == 0:
            pygame.draw.rect(self.screen, (0, 0, 0), (xy[0] * CELL_SIZE, xy[1] * CELL_SIZE,
                                                      CELL_SIZE, CELL_SIZE))
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), (xy[0] * CELL_SIZE, xy[1] * CELL_SIZE,
                                                            CELL_SIZE, CELL_SIZE))

    def update_cell(self, x, y, alive):
        count = 0
        for i in range(x - 1, x + 2):
            if i < 0:
                i = len(self.matrix) - 1
            elif i >= len(self.matrix):
                i = 0
            for j in range(y - 1, y + 2):
                if [i, j] != [x, y]:
                    if j < 0:
                        j = len(self.matrix[0]) - 1
                    elif j >= len(self.matrix[0]):
                        j = 0
                    if self.matrix[i][j] == 1:
                        count += 1
        if alive == 0 and count == 3:
            return 1
        if alive == 1 and (count not in [2, 3]):
            return 0
        return alive

    def turn(self):
        matrix = [i.copy() for i in self.matrix]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                matrix[i][j] = self.update_cell(i, j, self.matrix[i][j])
        self.matrix = matrix
        self.draw_map()

    def draw_map(self):
        self.screen.fill((0, 0, 0))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 1:
                    self.draw_cell([i, j])

    def clear(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = 0
        self.draw_map()

    def random(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = choice([0, 0, 0, 1])
        self.draw_map()
