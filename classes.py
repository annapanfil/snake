import pygame as pg

class Snake():
    def __init__(self, screen_size:int, color = (243, 98, 102)):
        self.length = 1
        self.positions = [(screen_size/2, screen_size/2)]
        self.color = color

    def move():
        pass

    def display():
        pass


class Food():
    pass

class Board():
    def __init__(self, surface, field_size = 20, light_color=(98, 175, 243), dark_color=(98, 102, 243)):
        self.field_size = field_size
        self.surface = surface
        self.light_color = light_color
        self.dark_color = dark_color

    @property
    def center(self):
        pass

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
