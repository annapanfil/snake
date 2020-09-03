import pygame as pg
import random

LEFT = (-1,0)
RIGHT = (1,0)
UP = (0,-1)
DOWN = (0,1)

class Board():
    def __init__(self, surface, field_size = 20, light_color=(98, 175, 243), dark_color=(98, 102, 243)):
        self.field_size = field_size
        self.surface = surface
        self.light_color = light_color
        self.dark_color = dark_color

    @property
    def sizeInFields(self):
        return int(self.screen_size/self.field_size)

    @property
    def screen_size(self):
        return self.surface.get_width()

    def display(self):
        for i in range(self.sizeInFields):
            for j in range(self.sizeInFields):
                rectangle = pg.Rect((i*self.field_size, j*self.field_size), (self.field_size, self.field_size))
                if (i+j)%2 == 0:
                    pg.draw.rect(self.surface, self.dark_color, rectangle)
                else:
                    pg.draw.rect(self.surface, self.light_color, rectangle)


class Snake():

    def __init__(self, start_position, color = (243, 98, 102)):
        self.length = 1
        self.positions = [[start_position, start_position]] # position (in fields)
        self.color = color
        self.score = 0
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def turn(self, turn_direcions):
        # check if eating its tail
        if self.length > 1 and (turn_direcions[0]*-1, turn_direcions[1]*-1) == self.direction:
            pass
            # exit game
        else:
            self.direction = turn_direcions

    def changeDirection(self, event):
        LEFT_KEYS = {pg.K_LEFT, pg.K_a}
        RIGHT_KEYS = {pg.K_RIGHT, pg.K_d}
        UP_KEYS = {pg.K_UP, pg.K_w}
        DOWN_KEYS = {pg.K_DOWN, pg.K_s}

        if event.key in LEFT_KEYS:
            self.turn(LEFT)
        elif event.key in RIGHT_KEYS:
            self.turn(RIGHT)
        elif event.key in UP_KEYS:
            self.turn(UP)
        elif event.key in DOWN_KEYS:
            self.turn(DOWN)
        else:
            print("Niepoprawny klawisz:", event.key)

    def move(self, event):
        # move == change head position, delete end of tail
        head = self.positions[0]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        # check if eating its tail
        if self.length > 2 and new_head in self.positions[2:]:
            pass
            # exit game
        else:
            self.positions.insert(0, new_head)
            self.positions.pop()

    def display(self, board: Board):
        for coords in self.positions:
            rectangle = pg.Rect((coords[0]*board.field_size, coords[1]*board.field_size), (board.field_size, board.field_size))
            pg.draw.rect(board.surface, self.color, rectangle)


class Food():
    pass