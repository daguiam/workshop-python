
---

---

# Handling `.csv` files with header column names

Data can be stored and loaded in pretty much any kind of structure using Python, from comma separated values, json, binary files, databases or compressed files.

Here we will introduce how to store and load data in the common comma separated value `.csv` format.

`.csv` files have usually a header, determining what is in each of the columns, and each row corresponds to a new data line.

An example:
```
a,b
0.953274884328,0.908733005091
-0.438914494799,0.192645933745
1.67484667805,2.80511139497

```


To handle `csv` data we use an additional python library, `pandas`.
`pandas` is a great library to handle different data structures and one of the most used python tools in data sciences.
Here we will use it to simply store and load `.csv` files for us, since the `NumPy` library is not as complete.

## Loading data from `.csv` into `NumPy` structure

Assuming that the first line of the `.csv` file includes the names of the respective columns, we can use the numpy library directly.

```python
import numpy as np

filename='data.csv'
data = np.genfromtxt(filename, delimiter=',', names=True)
t = data['t']
sig1 = data['sig1']
```

Or we can use the pandas library together with numpy.

```python
import pandas as pd
import numpy as np

filename = 'data.csv'
data = pd.read_csv(filename)
t = data['t']
sig1 = data['sig1']
```



```python
def function()

```
```python
data = np.genfromtxt(path_to_csv, dtype=None, delimiter=',', names=True)



```