#thank you to the following recources in my README page for giving me the abilities to code this!
#numbers.py is for compleing complex equations and comes with python!
import numpy as np
#wave is an externally downloaded feature that works with listening to audio and creating it
import wave as wav
#Struct is a module used for binary data starage in which it can pack() or unpack() data
import struct as s
#matplotlib is an external source that makes data tables for us.
#possibly a pylint problem, but currently gives error
import matplotlib.pyplot as plot

#this is just a test to see if the code runs, which it does despite pylints error
print("""Hello World! I'm C.H.D.(which stands for chrismas light hack for decorations), 
but you can call me Chad!""")

#number of times wave repeats a second
frequency = 1000 #int

# represents the number of samples we have (we currently have non.)
num_samples = 48000

#sample rate of analog to didgital covert
sampling_rate = 48000.0 #float

#how loud our sound is, or the maximum extent of vibration or oscillation
amplitude = 32767 #half scale 16000 #int

#This should be our sound sample (in which we have none)
file = "test.wav"

#above is just the setup. Now for the real fun/ or more like confusing challenges
# def get_sin_wave():
#     sine_wave = ""
#     for x in range(num_samples):
#         np.sin(2 * np.pi * frequency * x/sampling_rate)
#         return sine_wave = np.sin(2 * np.pi * frequency * x/sampling_rate))
#the above is a break down of the below line of code which uses inline coding.
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]

#more preperation for later coding
nframes=num_samples
comptype="NONE" 
compname="not compressed"
nchannels=1
sampwidth=2