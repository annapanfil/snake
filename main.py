import pygame as pg
from classes import *
import PySimpleGUI as sg
import os

def main():
    screen_size = 480

    # create PySimpleGUI window
    layout = [[sg.Text('Test of PySimpleGUI with PyGame')],
              [sg.Graph((screen_size, screen_size), (0, 0), (screen_size, screen_size), key='-GRAPH-')],
              [sg.Button('Draw'), sg.Exit()]]

    window = sg.Window('PySimpleGUI + PyGame', layout, finalize=True)

    # integrate PyGame with PySimpleGUI (tkinter exactly)
    graph = window['-GRAPH-']
    embed = graph.TKCanvas
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    # os.environ['SDL_VIDEODRIVER'] = 'windib' # windows
    os.environ['SDL_VIDEODRIVER'] = 'x11' # linux


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
    food = Food(board_size = board.sizeInFields)

    # GAME LOOP
    running = True
    while running:
        clock.tick(10)

        # PySimpleGUI events handling
        ev, values = window.read(timeout=10)
        if ev in (sg.WIN_CLOSED, 'Exit'):
            running = False
        pg.display.update()

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

if __name__ == '__main__':
    main()
