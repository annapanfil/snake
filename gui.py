import PySimpleGUI as sg
import os
from main import *

def eventHandling(window):
    while(True):
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == "-PLAY-":
            window.Close()
            score = game()
            exitMenu(score)
            break
        elif event == "-SETTINGS-":
            window.Hide()
            settings()
            window.UnHide()

def exitMenu(score):
    layout = [[sg.Text("GAME OVER")],
              [sg.Text(f'Your score: {score}')],
              [sg.Button('Settings', key="-SETTINGS-"), sg.Button('Play again', key="-PLAY-"), sg.Exit()]]

    window = sg.Window('Snake game - GAME OVER', layout, finalize=True)
    eventHandling(window)


def settings():
    sg.Popup("You thought you can change anything? xD\nGo and play")

def mainMenu():
    layout = [[sg.Text('Welcome to snake game!')],
             [sg.Button('Settings', key="-SETTINGS-"), sg.Button('Start game', key="-PLAY-"), sg.Exit()]]

    window = sg.Window('Snake game - MENU', layout, finalize=True)
    eventHandling(window)


if __name__ == '__main__':
    mainMenu()
