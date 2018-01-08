# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 02:33:25 2018

@author: Borko
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Chebyshev2 import Chebyshev2

file_data = np.loadtxt("Test_ECG.dat")

time_frame  = file_data[:,0]
ecg_raw     = file_data[:,1]
fs          = 1000

plt.figure(0)
plt.title("ECG")
plt.plot(time_frame, ecg_raw)
plt.xlabel("msec")
plt.ylabel("mV (raw)")
plt.show()

ecg_fft = np.real(sp.fft(ecg_raw))
ecg_fft_no_mirror = ecg_fft[:len(ecg_fft)//2]
ecg_freq = np.linspace(0, 500, len(ecg_fft)//2)

plt.figure(1)
plt.title("Frequency spectrum of ECG")
plt.plot(ecg_freq, np.abs(ecg_fft_no_mirror))
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()


my_filter = Chebyshev2()
my_filter.lowPass(4, 40, 35, fs)

res = np.zeros(len(ecg_raw))
for i in range(len(ecg_raw)):
    res[i] = my_filter.filter(ecg_raw[i])
    
    
freq_res2 = np.abs(np.real(np.fft.fft(res)))

plt.figure(4)
plt.plot(res)
plt.title("ECG")
plt.xlabel("msec")
plt.ylabel("mV (raw)")
plt.show()

plt.figure(5)
plt.plot(np.linspace(0, 500, len(freq_res2)//2), freq_res2[:len(freq_res2)//2])
plt.title("Spectrum of 50Hz free signal")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()