import PySimpleGUI as sg
import os
from main import *

def eventHandling(window, personalize):
    while(True):
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in ("-PLAY-", '\r'):
            window.Close()
            score = game(personalize)
            exitMenu(score, personalize)        # rekurencja – to chyba niedobrze
            break
        elif event == "-SETTINGS-":
            window.Hide()
            personalize = settings(personalize)
            window.UnHide()
        elif event == "-INFO-":
            window.Hide()
            info()
            window.UnHide()

def info():

    layout = [[sg.Text("CONTROLS", font = 40, justification = 'center')],
              [sg.Text('Move snake:\tarrows or ADWS\nPause:\t\tP')],
              [sg.Text("CREDITS", font = 40, justification = 'center')],
              [sg.Text('Code available on GitHub: github.com/panka134\n©Anna Panfil 2020')],
              [sg.Button('Back', key="-MENU-")]]

    window = sg.Window('Snake game - INFO', layout, finalize=True, size=(480,210), return_keyboard_events=True, disable_close=True)
    while(True):
        event, _ = window.read()
        if event in ("-MENU-", '\r'):
            window.Close()
            break

def exitMenu(score, personalize):
    layout = [[sg.Text("\nGAME OVER", font = 40, justification = 'center')],
              [sg.Text(f'Your score: {score}\n', font = 30, justification = 'center')],
              [sg.Button('Play again', key="-PLAY-")],
              [sg.Button('Settings', key="-SETTINGS-"), sg.Button('Info', key='-INFO-'), sg.Exit()]]

    window = sg.Window('Snake game - GAME OVER', layout, finalize=True,
                        element_justification='center', size=(480,210), return_keyboard_events=True)

    eventHandling(window, personalize)


def settings(personalize):
    # sg.Popup("You thought you can change anything? xD\nGo and play")
    speeds = ["slow", "normal", "fast", "lightning fast"]
    layout = [[sg.Text('Board size:\t' ), sg.Slider(range=(200, 800), default_value=personalize['board_size'],
                resolution = 40, orientation='horizontal', key="board_size")],
              [sg.Text('Quantity of food:\t' ), sg.Slider(range=(1, 10), default_value=personalize['food'],
                resolution = 1, orientation='horizontal', key="food")],
              [sg.Text("Snake speed:\t"), sg.OptionMenu(speeds, default_value=speeds[personalize['speed']-1], key="speed")],
              [sg.Text("Show score:\t"), sg.Checkbox("", default=personalize['show_score'], key="show_score")],
              [sg.Button('Save', key="-MENU-")]]

    window = sg.Window('Snake game - SETTINGS', layout, finalize=True, size=(480,210), return_keyboard_events=True, disable_close= True)
    while(True):
        event, values = window.read()
        if event in ("-MENU-", '\r'):
            window.Close()
            values['speed'] = speeds.index(values['speed'])+1
            return(values)

def mainMenu():
    sg.theme('Light Blue 3')
    layout = [[sg.Text('\nWelcome to snake game!\n', font = 40)],
             [sg.Button('Start game', key="-PLAY-")],
             [sg.Button('Settings', key="-SETTINGS-"), sg.Button('Info', key='-INFO-'), sg.Exit()]]

    window = sg.Window('Snake game - MENU', layout, finalize=True,
                        element_justification='center', size=(480,210), return_keyboard_events=True)

    personalize = {'board_size': 480, 'food': 1, 'speed': 2, 'show_score': True}
    eventHandling(window, personalize)


if __name__ == '__main__':
    mainMenu()
