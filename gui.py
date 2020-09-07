import PySimpleGUI as sg
import os
from main import *
from language import *

icon="snake.png"

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
            info(personalize['lang'])
            window.UnHide()

def info(lang):

    layout = [[sg.Text(lang['h1_controls'], font = 40, justification = 'center')],
              [sg.Text(lang['controls'])],
              [sg.Text(lang['h1_rules'], font = 40, justification = 'center')],
              [sg.Text(lang['rules'])],
              [sg.Text("______________________", font = 40, justification = 'center')],
              [sg.Text(lang['credits'])],
              [sg.Button(lang['back'], key="-MENU-")]]

    window = sg.Window(lang['back'], layout, finalize=True, size=(480,330), return_keyboard_events=True, disable_close=True, icon=icon)
    while(True):
        event, _ = window.read()
        if event in ("-MENU-", '\r'):
            window.Close()
            break

def exitMenu(score, personalize):
    lang = personalize['lang']

    layout = [[sg.Text(lang['game_over'], font = 40, justification = 'center')],
              [sg.Text(lang['score'].format(score), font = 30, justification = 'center')],
              [sg.Button(lang['play_again'], key="-PLAY-")],
              [sg.Button(lang['settings'], key="-SETTINGS-"), sg.Button(lang['info'], key='-INFO-'), sg.Exit(button_text=lang['exit'])]]

    window = sg.Window(lang['exit_window'], layout, finalize=True, icon=icon,
                        element_justification='center', size=(480,210), return_keyboard_events=True)

    eventHandling(window, personalize)


def settings(personalize):
    lang = personalize['lang']
    languages = ['pl', 'en']
    layout = [[sg.Text(lang['language']), sg.OptionMenu(languages, default_value=personalize['lang'], key='lang')],
              [sg.Text(lang['board_size']), sg.Slider(range=(200, 800), default_value=personalize['board_size'],
                resolution = 40, orientation='horizontal', key="board_size")],
              [sg.Text(lang['food_quantity']), sg.Slider(range=(1, 10), default_value=personalize['food'],
                resolution = 1, orientation='horizontal', key="food")],
              [sg.Text(lang['speed']), sg.OptionMenu(lang['speeds'], default_value=lang['speeds'][personalize['speed']-1], key="speed")],
              [sg.Checkbox(lang['speed_increase'], default=personalize['speed_increase'], key='speed_increase'),
                sg.Checkbox(lang['wall_die'], default=personalize['wall_die'], key='wall_die')],
              [sg.Checkbox(lang['show_score'], default=personalize['show_score'], key="show_score")],
              [sg.Button(lang['save'], key="-MENU-")]]

    window = sg.Window('Snake game - SETTINGS', layout, finalize=True, size=(480,280), return_keyboard_events=True, disable_close= True, icon=icon)
    while(True):
        event, values = window.read()
        if event in ("-MENU-", '\r'):
            window.Close()
            values['speed'] = lang['speeds'].index(values['speed'])+1
            return(values)

def mainMenu():
    # default settings
    #FIXME: personalize only if not personalized
    #FIXME: language in personalize as string
    personalize = {'lang': pl, 'board_size': 480, 'food': 1, 'speed': 1, 'speed_increase': True, 'show_score': True, 'wall_die': True}
    lang = personalize['lang']

    sg.theme('Light Blue 3')
    layout = [[sg.Text(lang['welcome'], font = 40)],
             [sg.Button(lang['start'], key="-PLAY-")],
             [sg.Button(lang['settings'], key="-SETTINGS-"), sg.Button(lang['info'], key='-INFO-'), sg.Exit(button_text=lang['exit'])]]
             # FIXME: Exit doesn't work

    window = sg.Window(lang['menu_window'], layout, finalize=True, icon=icon,
                        element_justification='center', size=(480,200), return_keyboard_events=True)

    eventHandling(window, personalize)


if __name__ == '__main__':
    mainMenu()
