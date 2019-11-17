#thank you to the following recources in my README page for giving me the abilities to code this!
# this code is not legally owned by me, and I do not encourage the act of doing this as it may
# cuase injury or simply break your things. Follow at your own risk!

#matplotlib is an external source that makes data tables for us.
#possibly a pylint problem, but currently gives error
import matplotlib.pyplot as plot
#numbers.py is for compleing complex equations and comes with python!
import numpy as np
#Struct is a module used for binary data starage in which it can pack() or unpack() data
import struct
#wave is an externally downloaded feature that works with listening to audio and creating it
import wave

#this is just a test to see if the code runs, which it does despite pylints error
print("""Hello World! I'm C.H.D.(which stands for chrismas light hack for decorations), 
but you can call me Chad!""")

#number of times wave repeats a second
frequency = 10 #int 1000

# represents the number of samples we have
num_samples = 47000 #int 48000

#sample rate of analog to didgital covert
sampling_rate = 48000.0 #float

#how loud our sound is, or the maximum extent of vibration or oscillation
amplitude = 16000 #full scale 32767 #int 

#This will be our test sample's name
file = "test.wav"

#above is just the setup. Now for the real fun/ or more like confusing challenges
# def get_sine_wave():
#     sine_wave = ""
#     for x in range(num_samples):
#         np.sin(2 * np.pi * frequency * x/sampling_rate)
#         return sine_wave = np.sin(2 * np.pi * frequency * x/sampling_rate))
#the above is a break down of the below line of code, which uses inline coding.
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]

#making a sine wave file
#nframe is the number of frames or samples
nframes=num_samples
#these signal uncompressed data
comptype="NONE" 
compname="not compressed"
#number of channels
nchannels=1
#the sample width in bytes (which are usaully 2-16 bytes per sample)
sampwidth=2

#writes our file with our previously made parameters
wav_file = wave.open(file, "w")
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

#mutiplies our samples and then converts them to binary in order for audio readablity
for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))

#the code above is creating a sound that we can now play in any sound reading application!