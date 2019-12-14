#!/usr/bin/python3
# Time: 2019/07/30 2:34 PM
# About: 

import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlFile, ControlText, ControlSlider, ControlPlayer, ControlButton


class Name(BaseWidget):
    def __init__(self):
        super().__init__('another test')

        self._firstname = ControlText('first name')
        self._lastname = ControlText('last name')
        self._fullname = ControlText('full name')
        self._button = ControlButton("press this button")
        self.formset = [('_firstname', '_lastname'), '_button', '_fullname', ' ']
        self._button.value = self.__buttonAction
        # self.message("it works!")


    # add a button event
    def __buttonAction(self):
        self._fullname.value = self._firstname.value + " " + self._lastname.value


if __name__ == '__main__':
    pyforms.start_app(Name)






























