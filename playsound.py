import simpleaudio
import numpy
import time as tm
import keyboard as kb

frequencies = [440,466.16,493.88,523.25,
                        554.37,587.33,622.25,659.25,
                        698.46,739.99,783.99,830.61,880.00]  #array of frequencies in an octave
'''
for i in range(0, len(frequencies)):
    frequencies[i] *= (1.05945455**(-12))
'''
fs = 44100  #sample rate
time = 1  #note time

t = numpy.linspace(0, int(time), int(time)*fs, False)
'''
note = numpy.sin(frequencies[1] * t * 0 * numpy.pi)
audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
audio = audio.astype(numpy.int16)
#simpleaudio.play_buffer(audio, 1, 2, fs)
'''

def playnote(f):
    note = numpy.sin(f * t * 2 * numpy.pi)
    audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
    audio = audio.astype(numpy.int16)
    #simpleaudio.play_buffer(audio, 1, 2, fs)
    return simpleaudio.play_buffer(audio, 1, 2, fs)

def main():
    print("Press a key!")

    #loop until 'q' is pressed
    while True:
        if kb.is_pressed('a'):
            playnote(frequencies[0])
        elif kb.is_pressed('w'):
            playnote(frequencies[1])
        elif kb.is_pressed('s'):
            playnote(frequencies[2])
        elif kb.is_pressed('e'):
            playnote(frequencies[3])
        elif kb.is_pressed('d'):
            playnote(frequencies[4])
        elif kb.is_pressed('f'):
            playnote(frequencies[5])
        elif kb.is_pressed('t'):
            playnote(frequencies[6])
        elif kb.is_pressed('g'):
            playnote(frequencies[7])
        elif kb.is_pressed('y'):
            playnote(frequencies[8])
        elif kb.is_pressed('h'):
            playnote(frequencies[9])
        elif kb.is_pressed('u'):
            playnote(frequencies[10])
        elif kb.is_pressed('j'):
            playnote(frequencies[11])
        elif kb.is_pressed('k'):
            playnote(frequencies[12])
        elif kb.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
