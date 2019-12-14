#!/usr/bin/python3
# Time: 2019/07/30 1:48 PM
# About: 

import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlFile, ControlText, ControlSlider, ControlPlayer, ControlButton


class FirstForm(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('just a test app')

        self._videofile = ControlFile('Video  ControlFile ')
        self._outputfile = ControlText('Results output file  ControlText')
        self._threshold = ControlSlider('Threshold  ControlSlider', default=114, minimum=0, maximum=255)
        self._blobsize = ControlSlider("Minimum blob size  ControlSlider ", default=110, minimum=100, maximum=2000)
        self._player = ControlPlayer('Player  ControlPlayer')
        self._runbutton = ControlButton('Run  ControlButton')

        self._videofile.changed_event = self.__videoFileSelectionEvent
        self._runbutton.value = self.__runEvent
        self._player.process_frame_event = self.__process_frame

        self._format = [
            ('_videofile', '_outputfile'),
            '_threshold',
            ('_blobsize', '_runbutton'),
            '_player'
        ]

    def __videoFileSelectionEvent(self):
        self._player.value = self._videofile.value

    def __process_frame(self, frame):
        return frame

    def __runEvent(self):
        pass


if __name__ == '__main__':
    pyforms.start_app(FirstForm)






























