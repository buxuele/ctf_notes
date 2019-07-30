#!/usr/bin/python3
# Time: 2019/07/09 4:17 PM
# About: 

import PySimpleGUI as sg

layout = [
    [sg.Text("please tell me something about you:")],
    [sg.Text('Name', size=(15, 1)), sg.Input('name')],
    [sg.Text('Address', size=(15, 1)), sg.Input('Address')],
    [sg.Text('Phone', size=(15, 1)), sg.Input('Phone')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("First GUI window").Layout(layout)
button, values = window.Read()

print(button, values[0], values[1], values[2])












