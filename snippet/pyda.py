# author: fanchuangwater@gmail.com
# date: 2020/5/25 下午9:14
# 目的: 

import wolframalpha
import PySimpleGUI as sg
import wikipedia

"""
wikipedia
wolframalpha
"""


# user_input = input("Question: ")
client = wolframalpha.Client("E6W8T5-6PAY638WKL")

# 42
# (according to the book The Hitchhiker's Guide to the Galaxy, by Douglas Adams)
# **********************************************************************************************************

sg.theme('DarkPurple')
layout = [
    [sg.Text('What is your question?'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
    ]
window = sg.Window('PyDa', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

    # 1. wolfram
    # res = client.query(values[0])
    # better_res = next(res.results).text
    # sg.Popup(better_res)

    # 2. wiki
    wiki_res = wikipedia.summary(values[0], sentences=1)
    sg.Popup(wiki_res)



window.close()




