# Time: 2019/05/15 10:15 PM
# About: https://github.com/jiaaro/pydub

from pydub import AudioSegment
from pydub.playback import play

""" this lib play music, works just really fine """


sound = AudioSegment.from_file('intro.mp3')
play(sound)
































