import pygame as pg
from classes import *

def main():
    screen_size = 480

    # INITIALIZE PYGAME AND CREATE THE WINDOW
    pg.init()
    screen = pg.display.set_mode((screen_size, screen_size))

    # Title and icon
    pg.display.set_caption("Snake game")
    icon = pg.image.load("snake.png")
    pg.display.set_icon(icon)

    rectangle =  pg.Rect((100,50), (100,100))

    board = Board(surface = screen)
    snake = Snake(board.sizeInFields/2)



    # GAME LOOP
    running = True
    while running:
        # EVENTS HANDLING
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        board.display()
        snake.display(board)
        # screen.fill((0, 0, 255)) # fill the screen with colour
        # screen.blit(icon, (100,100)) # show the picture
        pg.display.update()



    # clock = pg.time.Clock()
    # surface = pg.Surface((screen_size,screen_size))
    # surface = surface.convert()

if __name__ == '__main__':
    main()
