#!/usr/bin/env python
""" Example 203

Making figures ready for publication
"""
import matplotlib.pylab as plt
import numpy as np
import sys
if __name__ == "__main__":
    np.random.seed(0)

    t = np.linspace(0,5,101)
    sig1 = 0.8*np.sin(np.pi*t)
    sig2 = 10*np.exp(-t/2-1)*np.cos(np.pi*t)
    
    fig = plt.figure(figsize=(3.5,2))
    
    plt.plot(t, sig1, label='Signal 1', linewidth=1)
    plt.plot(t, sig2, label='Signal 2', linewidth=1)
    
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Amplitude', fontsize=10)
    plt.title('Title of example 203', fontsize=10)

    
    plt.legend(fontsize=10)
    
    plt.subplots_adjust(top=0.85,
                        bottom=0.21,
                        left=0.16, 
                        right=None,
                        wspace=None,
                        hspace=None )


    plt.savefig('dataplot.png')
    plt.show()
