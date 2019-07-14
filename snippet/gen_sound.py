# Time: 2019/05/15 9:16 PM
# About: play with music

import numpy as np
import simpleaudio as sa

"""
install check:
import simpleaudio.functionchecks as fc
fc.LeftRightCheck.run()


# play a audio file, failed at mp3 file 

filename = 'intro.mp3'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()

"""

# generate a wave file using numpy

frequency = 440
fs = 44100
seconds = 3


t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)

audio = note * (2**15 -1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()









