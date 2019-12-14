#!/usr/bin/python3
# Time: 2019/07/09 4:47 PM
# About: 

# pip3 install pyautogui

import time
import pyautogui as pt

""" check out weather"""


pt.FAILSAFE = True      # keep safe :)
# pt.PAUSE = 2.5

print(pt.size())
print(pt.position())


# open a new tab, and search weather info
pt.moveTo(500, 500)
pt.click()
pt.hotkey('ctrl', 't')
pt.moveTo(318, 88)          # 这个位置是 浏览器的搜索栏的位置
pt.click()
pt.typewrite("weather")
pt.press('enter')
pt.press('enter')
time.sleep(5)
print("where is mouse: ", pt.position())        # still (318, 88)
pt.hotkey('ctrl', 'w')


# alert function\
"""
time.sleep(10)
pt.alert("This is a alert!")
time.sleep(10)
pt.confirm("Here is a confirm message!")
time.sleep(10)
pt.prompt("Input me something...")

"""

# others
# pt.hotkey('alt', 'printscreen')       # 屏幕截图
# print("ok")


KEY_NAMES = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
     ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
     '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
     '{', '|', '}', '~',
     'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
     'browserback', 'browserfavorites', 'browserforward', 'browserhome',
     'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
     'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
     'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
     'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
     'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
     'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
     'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
     'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
     'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
     'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
     'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
     'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
     'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
     'command', 'option', 'optionleft', 'optionright']

