#!/usr/bin/python3
# Time: 2019/07/09 4:25 PM
# About: 


import PySimpleGUI as sg

layout = [
    [sg.Text("Persistent window")],
    [sg.Input(do_not_clear=True)],
    [sg.Button('Read'), sg.Exit()]
]

window = sg.Window("window stays open", layout)

while 1:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    print(event, values)

window.Close()

































