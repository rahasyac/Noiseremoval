# Name : FNU Rahasya Chandan
# UTA Id: 1000954962
# Noise Removal using FFTS

import numpy as np 
import matplotlib.pyplot as plt # matlab plotting in python
import soundfile as sf

#Read the audio file which is corrupted
audio_file = "P_9_2.wav"
data, sample_rate = sf.read(audio_file)

#Apply FFT
FFT = np.fft.fft(data)

#Plot the magnitude of FFT
plt.figure(1)
plt.plot(FFT)
plt.show()

#Index of the midpoint of the FFT values
index = round(len(FFT) / 2)
FFT[index] = 0

#Choose an offset
offset = 19150

#Set the nvalues in the range of midpoint ± offset to 0.
for n in range(offset):
	FFT[index + n] = 0
	FFT[index - n] = 0

#Plot the magnitude of the FFT after removing the noise frequencies.
plt.figure(2)
plt.plot(FFT)
plt.show()

#Create a new, cleaned signal by applying the inverse FFT
New_FFT = np.fft.ifft(FFT)

#Write a new WAV file 
sf.write('CleanMusic.wav', New_FFT.real, sample_rate)

