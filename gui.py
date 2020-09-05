import PySimpleGUI as sg
import os
from main import *

def eventHandling(window):
    personalize = {}
    while(True):
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in ("-PLAY-", '\r'):
            window.Close()
            score = game(personalize)
            exitMenu(score)
            break
        elif event == "-SETTINGS-":
            window.Hide()
            personalize = settings()
            window.UnHide()

def exitMenu(score):
    layout = [[sg.Text("\nGAME OVER", font = 40, justification = 'center')],
              [sg.Text(f'Your score: {score}\n', font = 30, justification = 'center')],
              [sg.Button('Play again', key="-PLAY-")],
              [sg.Button('Settings', key="-SETTINGS-"), sg.Exit()]]

    window = sg.Window('Snake game - GAME OVER', layout, finalize=True,
                        element_justification='center', size=(480,200), return_keyboard_events=True)
    eventHandling(window)


def settings():
    # sg.Popup("You thought you can change anything? xD\nGo and play")
    layout = [[sg.Text('Board size:\t\t\t' ), sg.Slider(range=(200, 800), default_value=480,
                resolution = 40, orientation='horizontal', key="board_size")],
              [sg.Text('Quantity of food (Not working yet):\t' ), sg.Slider(range=(1, 10), default_value=1,
                          resolution = 1, orientation='horizontal', key="food")],
              [sg.Button('Back', key="-MENU-")]]

    window = sg.Window('Snake game - SETTINGS', layout, finalize=True, size=(480,200), return_keyboard_events=True, disable_close= True)
    while(True):
        event, values = window.read()
        if event in ("-MENU-", '\r'):
            window.Close()
            return(values)

def mainMenu():
    sg.theme('Light Blue 3')
    layout = [[sg.Text('\nWelcome to snake game!\n', font = 40)],
             [sg.Button('Start game', key="-PLAY-")],
             [sg.Button('Settings', key="-SETTINGS-"), sg.Exit()]]

    window = sg.Window('Snake game - MENU', layout, finalize=True,
                        element_justification='center', size=(480,200), return_keyboard_events=True)
    eventHandling(window)


if __name__ == '__main__':
    mainMenu()