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

    clock = pg.time.Clock()

    board = Board(surface = screen)
    snake = Snake(start_position = board.sizeInFields/2)

    # GAME LOOP
    running = True
    while running:
        clock.tick(5)
        # EVENTS HANDLING
        try:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    snake.changeDirection(event)

            snake.move(event, board.sizeInFields)
        except GameOver:
            print("GAME OVER")
            running = False

        board.display()
        snake.display(board)
        # screen.fill((0, 0, 255)) # fill the screen with colour
        # screen.blit(icon, (100,100)) # show the picture
        pg.display.update()


if __name__ == '__main__':
    main()
