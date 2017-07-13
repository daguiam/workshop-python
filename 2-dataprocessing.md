# Data processing with python

Data analysis or data processing is one of the core requirements in any scientific field.
Python is a general purpose language that has an extensive library of importable modules for nearly any field.

In this workshop we will talk about using the most popular of these python modules to understand how to handle data, process it and plot.

## Making sure we have the right environment

Open up a python interpreter and type in each of the following lines

```python
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> import matplotlib
>>> import numpy
>>> import scipy
>>> import pandas
>>> 
```
No error should be raised if all these packages are correctly installed. 
The anaconda package installer should have installed all of these correctly.



## SciPy - Scientific Computing Tools for Python 
Check more here <https://www.scipy.org/about.html>

> SciPy refers to several related but distinct entities:

> * The SciPy Stack, a collection of open source software for scientific computing in Python, and particularly a specified set of core packages.
> * The community of people who use and develop this stack.
> * Several conferences dedicated to scientific computing in Python - SciPy, EuroSciPy and SciPy.in.
> * The SciPy library, one component of the SciPy stack, providing many numerical routines.

> Taken from <https://www.safaribooksonline.com/library/view/python-for-data/9781449323592/ch04.html>
>
> SciPy is a collection of packages addressing a number of different standard problem domains in scientific computing. Here is a sampling of the packages included:

> * scipy.integrate: numerical integration routines and differential equation solvers
> * scipy.linalg: linear algebra routines and matrix decompositions extending beyond those provided in numpy.linalg.
> * scipy.optimize: function optimizers (minimizers) and root finding algorithms
> * scipy.signal: signal processing tools
> * scipy.sparse: sparse matrices and sparse linear system solvers
> * scipy.special: wrapper around SPECFUN, a Fortran library implementing many common mathematical functions, such as the gamma function
> * scipy.stats: standard continuous and discrete probability distributions (density functions, samplers, continuous distribution functions), various statistical tests, and more descriptive statistics
> * scipy.weave: tool for using inline C++ code to accelerate array computations


## NumPy <http://www.numpy.org/>
> NumPy is the fundamental package for scientific computing with Python. It contains among other things:
> * a powerful N-dimensional array object
> * sophisticated (broadcasting) functions
> * tools for integrating C/C++ and Fortran code
> * useful linear algebra, Fourier transform, and random number capabilities

> Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.
> NumPy is licensed under the BSD license, enabling reuse with few restrictions.

> Taken from <https://www.safaribooksonline.com/library/view/python-for-data/9781449323592/ch04.html>
>
>NumPy, short for Numerical Python, is the foundational package for scientific computing in Python. The majority of this book will be based on NumPy and libraries built on top of NumPy. It provides, among other things:
> * A fast and efficient multidimensional array object ndarray
> * Functions for performing element-wise computations with arrays or mathematical operations between arrays
> * Tools for reading and writing array-based data sets to disk
> * Linear algebra operations, Fourier transform, and random number generation
> * Tools for integrating connecting C, C++, and Fortran code to Python
>
> Beyond the fast array-processing capabilities that NumPy adds to Python, one of its primary purposes with regards to data analysis is as the primary container for data to be passed between algorithms. For numerical data, NumPy arrays are a much more efficient way of storing and manipulating data than the other built-in Python data structures. Also, libraries written in a lower-level language, such as C or Fortran, can operate on the data stored in a NumPy array without copying any data.



## pandas <http://pandas.pydata.org/>

> pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
> 
> pandas is a NUMFocus sponsored project. This will help ensure the success of development of pandas as a world-class open-source project, and makes it possible to donate to the project.

> Taken from <https://www.safaribooksonline.com/library/view/python-for-data/9781449323592/ch04.html>
>
>pandas provides rich data structures and functions designed to make working with structured data fast, easy, and expressive. It is, as you will see, one of the critical ingredients enabling Python to be a powerful and productive data analysis environment. The primary object in pandas that will be used in this book is the DataFrame, a two-dimensional tabular, column-oriented data structure with both row and column labels:
>
        total_bill  tip   sex     smoker  day  time    size
    1   16.99       1.01  Female  No      Sun  Dinner  2
    2   10.34       1.66  Male    No      Sun  Dinner  3
    3   21.01       3.5   Male    No      Sun  Dinner  3
    4   23.68       3.31  Male    No      Sun  Dinner  2
    5   24.59       3.61  Female  No      Sun  Dinner  4
    6   25.29       4.71  Male    No      Sun  Dinner  4
    7   8.77        2     Male    No      Sun  Dinner  2
    8   26.88       3.12  Male    No      Sun  Dinner  4
    9   15.04       1.96  Male    No      Sun  Dinner  2
    10  14.78       3.23  Male    No      Sun  Dinner  2
> pandas combines the high performance array-computing features of NumPy with the flexible data manipulation capabilities of spreadsheets and relational databases (such as SQL). It provides sophisticated indexing functionality to make it easy to reshape, slice and dice, perform aggregations, and select subsets of data. pandas is the primary tool that we will use in this book.



## matplotlib <https://matplotlib.org/>
> Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, web application servers, and four graphical user interface toolkits.
>
> Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. For a sampling, see the screenshots, thumbnail gallery, and examples directory


---

# Using modules in Python

In python we are able to use modules that allow us to do things the basic python module doesn't.
For this we must first import them into our environment.

The module `SciPy`, for example, is highly useful for scientific computation.
Many signal processing tools are already present in the package.
The documentation can be acessible online or through the `__doc__` docstrings inside the interpreter.

```python
>>> scipy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'scipy' is not defined
>>> import scipy
>>> print scipy.__doc__
>>> print scipy.signal.__doc__
```

A useful subpackage of `SciPy` is the `scipy.constants` package containing many useful physical constants.

```python
>>> import scipy.constants as const
>>> from scipy import constants as const
>>> print const.__doc__
>>> const.m_e
9.10938356e-31
>>> print const.unit('electron mass')
kg
>>> 
```

> ***Question:*** What other constants can you think of? SciPy most likely has them.


Another very important module is `NumPy` that enables easy computing of multidimensional arrays of data and also includes the most used processing functions such as Fourier transforms, linear algebra, etc.

> ***Question:*** What happens when you want to multiply a value elementwise for all the elements in an array?

```python
>>> a = [0,1,2,3,4,5]
>>> b = a**2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
```

> ***Question:*** What about when using the standard array module in Python?
```python
>>> import array
>>> a = array.array('f',[0,1,2,3,4,5])
>>> a
array('f', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
>>> a*2
array('f', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
>>> 
```

For this kind of procedure you should use `NumPy` (<https://docs.scipy.org/doc/numpy/reference/index.html>)

```python
>>> import numpy as np
>>> a = np.array([0,1,2,3,4,5])
>>> b = a**2
>>> b
array([ 0,  1,  4,  9, 16, 25])
```
Creating arrays
```python
>>> a = np.arange(0,10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a = np.arange(0,10,2)
>>> a
array([0, 2, 4, 6, 8])
>>> a = np.linspace(0,10)
>>> a
array([  0.        ,   0.20408163,   0.40816327,   0.6122449 ,
         0.81632653,   1.02040816,   1.2244898 ,   1.42857143,
         1.63265306,   1.83673469,   2.04081633,   2.24489796,
         2.44897959,   2.65306122,   2.85714286,   3.06122449,
         3.26530612,   3.46938776,   3.67346939,   3.87755102,
         4.08163265,   4.28571429,   4.48979592,   4.69387755,
         4.89795918,   5.10204082,   5.30612245,   5.51020408,
         5.71428571,   5.91836735,   6.12244898,   6.32653061,
         6.53061224,   6.73469388,   6.93877551,   7.14285714,
         7.34693878,   7.55102041,   7.75510204,   7.95918367,
         8.16326531,   8.36734694,   8.57142857,   8.7755102 ,
         8.97959184,   9.18367347,   9.3877551 ,   9.59183673,
         9.79591837,  10.        ])
>>> a = np.linspace(0,10,5)
>>> a
array([  0. ,   2.5,   5. ,   7.5,  10. ])
>>> a = np.arange(10).reshape(2,5)
>>> a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> 

```


Creating regular arrays using `NumPy`:
* `arange([start,] stop[, step,][, dtype])` ... Return evenly spaced values within a given interval.
* `linspace(start, stop[, num, endpoint, ...])` ... Return evenly spaced numbers over a specified interval.
* `logspace(start, stop[, num, endpoint, base, ...])` ... Return numbers spaced evenly on a log scale.
* `geomspace(start, stop[, num, endpoint, dtype])` ... Return numbers spaced evenly on a log scale (a geometric progression).

Creating arrays with `zeros` and `ones`:

* `empty(shape[, dtype, order])` ... Returna new array of given shape and type, without initializing entries.
* `eye(N[, M, k, dtype])` ... Return a 2-D array with ones on the diagonal and zeros elsewhere.
* `identity(n[, dtype])` ... Return the identity array.
* `ones(shape[, dtype, order])` ... Return a new array of given shape and type, filled with ones.
* `zeros(shape[, dtype, order])` ... Return a new array of given shape and type, filled with zeros.
* `full(shape, fill_value[, dtype, order])` ... Return a new array of given shape and type, filled with fill_value.



```python
>>> np.dot(a,a)
55
>>> c = np.array([[1,1,1,1,1,1],[2,2,2,2,2,2]])
>>> np.dot(a,c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: shapes (6,) and (2,6) not aligned: 6 (dim 0) != 2 (dim 0)
>>> np.inner(a,c)
array([15, 30])
>>> c.size
12
>>> c.shape
(2, 6)
>>> len(c)
2
>>> 
```

More linear algebra using python can be checked at <https://docs.scipy.org/doc/numpy/reference/routines.linalg.html>

```python
>>> t = np.linspace(0,1,1000)
>>> f = 123
>>> y = np.sin(2*np.pi*f*t)
>>> 
```




# Handling `.csv` files


We show how to load data from `.csv` (comma separated value) files and the 



```python
def function()

```