import pygame as pg
import os
from classes import *
from gui import *

def game(personalize):
    screen_size = int(personalize['board_size'])
    food = int(personalize['food'])

    # INITIALIZE PYGAME AND CREATE THE WINDOW
    pg.init()
    screen = pg.display.set_mode((screen_size, screen_size))
    # os.environ['SDL_VIDEO_WINDOW_POS'] = '1000,1000' # sets window position – DOESN'T WORK

    # Title and icon
    pg.display.set_caption("Snake game")
    icon = pg.image.load("snake.png")
    pg.display.set_icon(icon)

    clock = pg.time.Clock()

    board = Board(surface = screen)
    snake = Snake(start_position = board.sizeInFields/2)
    food = Food(board_size = board.sizeInFields)

    # GAME LOOP
    running = True
    while running:
        clock.tick(10)

        # EVENTS HANDLING
        try:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    snake.changeDirection(event)

            snake.move(event, board.sizeInFields, food)
        except GameOver:
            print("GAME OVER\nYour score:", snake.length)
            running = False

        board.display()
        snake.display(board)
        food.display(board)
        pg.display.update()

    pg.quit()

    return snake.length



if __name__ == '__main__':
    mainMenu()
