import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":
    filename = 'lisbon_temperature.csv'
    data = np.genfromtxt(filename, delimiter=',')
    hour = np.arange(0, 24, 1)
    days = np.arange(11,26)

    temp_mean = np.mean(data, axis=0)
    temp_max = np.max(data, axis=0)
    temp_min = np.min(data, axis=0)
    
    plt.plot(hour, temp_mean, label='Average')
    plt.plot(hour, temp_max, label='Maximum')
    plt.plot(hour, temp_min, label='Minimum')

    plt.legend()
    plt.show()