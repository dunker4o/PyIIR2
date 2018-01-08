# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:33:19 2018

@author: Borko
"""

class IIR2Filter:
    
    def __init__ (self, coefficients):
        self.b0 = coefficients[0]
        self.b1 = coefficients[1]
        self.b2 = coefficients[2]
        self.a0 = coefficients[3]
        self.a1 = coefficients[4]
        self.a2 = coefficients[5]
        
        self.buffer1 = 0
        self.buffer2 = 0
        
        
    def filter(self, value):
        input_accumulator  = 0
        output_accumulator = 0
        
        #Accumulate the IIR part
        input_accumulator = value
        input_accumulator -= (self.a1 * self.buffer1)
        input_accumulator -= (self.a2 * self.buffer2)

        #Accumulate the FIR part
        output_accumulator = input_accumulator* self.b0
        output_accumulator += (self.buffer1 * self.b1)
        output_accumulator += (self.buffer2 * self.b2)
        
        self.buffer2 = self.buffer1
        self.buffer1 = input_accumulator
        
        return output_accumulator