# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 02:25:20 2018

@author: Borko
"""

import scipy.signal as signal
from IIR2Filter import IIR2Filter

class Bessel:
        
    def __init__(self):
        self.sos = None
        self.filter_list = []
        
        
    def getSos(self):
        return self.sos
    
    def lowPass(self, order, cut_off, sampling_frequency):
        python_freq = cut_off / sampling_frequency
        self.sos = signal.bessel(order, python_freq*2, 'lowpass', output='sos')
        self.filter_list = []
        for filt in self.sos:
            self.filter_list.append(IIR2Filter(filt))
        
    def highPass(self, order, cut_off, sampling_frequency):
        python_freq = cut_off / sampling_frequency
        self.sos = signal.bessel(order, python_freq*2, 'highpass', output='sos')
        self.filter_list = []
        for filt in self.sos:
            self.filter_list.append(IIR2Filter(filt))
        
    def bandStop(self, order, cut_off1, cut_off2, sampling_frequency):
        python_freq1 = cut_off1 / sampling_frequency
        python_freq2 = cut_off2 / sampling_frequency
        self.sos = signal.bessel(order, [python_freq1*2, python_freq2*2], 'bandstop', output='sos')
        self.filter_list = []
        for filt in self.sos:
            self.filter_list.append(IIR2Filter(filt))
        
    def bandPass(self, order, cut_off1, cut_off2, sampling_frequency):
        python_freq1 = cut_off1 / sampling_frequency
        python_freq2 = cut_off2 / sampling_frequency
        self.sos = signal.bessel(order, [python_freq1*2, python_freq2*2], 'bandpass', output='sos')
        self.filter_list = []
        for filt in self.sos:
            self.filter_list.append(IIR2Filter(filt))
        
    def filter(self, value):
        result = value
        for iir2_filter in self.filter_list:
            result = iir2_filter.filter(result)
        return result