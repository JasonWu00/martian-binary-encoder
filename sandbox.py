"""
whatever
"""

from pydub import AudioSegment
from pydub.playback import play

soundsfolder = "sounds/"

#song = AudioSegment.from_wav(soundsfolder+"742938__freekit__low-machine-hum.wav")
song = AudioSegment.from_mp3(soundsfolder+"rumble1.mp3")
play(song*5)
