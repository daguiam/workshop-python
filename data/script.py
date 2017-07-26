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
    
    fig, axarray = plt.subplots(2, 2, sharex='col', sharey='row')

    # Bottom left
    plt.sca(axarray[1,0])
    plt.pcolormesh(hour,days,data)

    plt.ylabel('Day')
    plt.xlabel('Time of day')
    # Top left
    plt.sca(axarray[0,0])
    plt.plot(hour, temp_mean, label='Average')
    plt.plot(hour, temp_max, label='Maximum')
    plt.plot(hour, temp_min, label='Minimum')
    plt.ylabel('Temperature [C]')
    plt.legend()

    # Bottom right
    plt.sca(axarray[1,1])
    day_mean = np.mean(data, axis=1)
    day_max = np.max(data, axis=1)
    day_min = np.min(data, axis=1)

    plt.plot(day_mean, days, label='Average')
    plt.plot(day_max, days, label='Maximum')
    plt.plot(day_min, days, label='Minimum')
    plt.xlabel('Temperature [C]')

    # Hiding top right frame
    axarray[0,1].axis('off')

    plt.suptitle('Lisbon temperature in July 2017')
    fig.savefig('lisbon_temp.svg')
    plt.show()