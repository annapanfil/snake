import pygame as pg
# import os
# import time
from classes import *
from gui import *

def display(board, snake, food):
    board.display()
    snake.display(board)
    for f in food:
        f.display(board)

    pg.display.update()

def game(personalize):
    # print(personalize)

    screen_size = int(personalize['board_size'])
    food_quantity = int(personalize['food'])
    speed = personalize['speed']*5
    show_score = True

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
    center = board.sizeInFields/2
    snake = Snake(start_position = center)
    food = [Food(board_size = center) for _ in range(food_quantity)]


    # display 3...2...1...
    font = pg.font.SysFont(None, 300)

    for i in range(3,0,-1):
        text = font.render(f"{i}", True, (0,0,0))
        display(board, snake, food)
        screen.blit(text, ((center*board.field_size)-50, (center*board.field_size)-80))
        pg.display.update()
        clock.tick(1)

    font = pg.font.SysFont(None, 30)

    # GAME LOOP
    running = True
    while running:
        clock.tick(speed)

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

        display(board, snake, food)
        if show_score:
            text = font.render(f"Score: {snake.length}", True, (0,0,0))
            screen.blit(text, (10, 20))
            pg.display.update()

    clock.tick(1)
    pg.quit()

    return snake.length

if __name__ == '__main__':
    mainMenu()
