import simpleaudio
import numpy
import time as tm

frequencies = [440,466.16,493.88,523.25,
                        554.37,587.33,622.25,659.25,
                        698.46,739.99,783.99,830.61,880.00]  #array of frequencies in an octave
'''
for i in range(0, len(frequencies)):
    frequencies[i] *= (1.05945455**(-12))
'''
fs = 44100  #sample rate
time = 1  #note time

t = numpy.linspace(0, time, time*fs, False)
'''
note = numpy.sin(frequencies[1] * t * 0 * numpy.pi)
audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
audio = audio.astype(numpy.int16)
#simpleaudio.play_buffer(audio, 1, 2, fs)
'''

def playnote(f):
    note = numpy.tan(f * t * 4 * numpy.pi)
    audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
    audio = audio.astype(numpy.int16)
    #simpleaudio.play_buffer(audio, 1, 2, fs)
    return simpleaudio.play_buffer(audio, 1, 2, fs)

play_object1 = playnote(frequencies[0])
play_object2 = playnote(frequencies[4])
play_object3 = playnote(frequencies[7])
tm.sleep(1)

play_object1 = playnote(frequencies[0])
play_object2 = playnote(frequencies[5])
play_object3 = playnote(frequencies[8])
tm.sleep(1)

play_object1 = playnote(frequencies[1])
play_object2 = playnote(frequencies[5])
play_object3 = playnote(frequencies[8])
tm.sleep(1)

play_object1 = playnote(frequencies[1])
play_object2 = playnote(frequencies[5])
play_object3 = playnote(frequencies[10])
tm.sleep(1)
'''
play_object1 = playnote(frequencies[3])
play_object2 = playnote(frequencies[7])
play_object3 = playnote(frequencies[10])
tm.sleep(2)

play_object1 = playnote(frequencies[3])
play_object2 = playnote(frequencies[8])
play_object3 = playnote(frequencies[12])
tm.sleep(2)
'''