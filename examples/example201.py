#!/usr/bin/env python
""" Example 201

Plotting example of two signals using matplotlib
"""
import matplotlib.pylab as plt
import numpy as np



if __name__ == "__main__":


    t = np.linspace(0,5,501)
    sig1 = 0.8*np.sin(np.pi*t)
    sig2 = 10*np.exp(-t/2-1)*np.cos(np.pi*t)
    
    plt.plot(t, sig1,label='Signal 1')
    plt.plot(t, sig2, 
                label='Signal 2',
                color='green')

    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Example 201')
    plt.grid()
    #plt.legend(['Sig1','sig2'])
    plt.legend()

    plt.show()
