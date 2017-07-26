import numpy as np

def verify_threshold(temperature, threshold=30):
    return np.any(temperature >= threshold)

if __name__ == "__main__":
    filename = 'lisbon_temperature.csv'
    data = np.genfromtxt(filename, delimiter=',')
    hour = np.arange(0, 24, 1)
    days = np.arange(11,26)
    
    for day, temperature in zip(days,data):
        if verify_threshold(temperature, threshold=32):
            print 'July %d was very hot'%(day)
        else:
            print 'July %d was okay'%(day)