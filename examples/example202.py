#!/usr/bin/env python
""" Example 202

Example subplots and scatter plots
"""
import matplotlib.pylab as plt
import numpy as np

if __name__ == "__main__":
    np.random.seed(0)

    x = np.random.randn(50)
    y = np.random.randn(50)
    
    f, axarr = plt.subplots(2, 1, sharey=True)
    
    plt.sca(axarr[0])
    plt.scatter(x, y,label='Scatter')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example 202')

    plt.sca(axarr[1])
    plt.plot(x, label='x')
    plt.plot(y, label='y')
    
    plt.legend()
    
    #plt.savefig('dataplot.pdf',dpi=300)
    plt.show()
