# Introduction to Python

 Python is a quick and light interpreted scripting language that you can use to quickly prototype a tool or a project.

You can use it for everything from simple automation scripts to even full applications, neusral networks, scientific computing, plots, graphical user interfaces, etc ...


## Installation
First you should install the correct python tols for your operating system.

For this tutorial we use

* Python 2.7.0 release at <https://www.python.org/download/releases/2.7/>

Other useful platforms can be used around Python:

* IPython <https://ipython.org/>
    >IPython is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers introspection, rich media, shell syntax, tab completion, and history


* Anaconda <https://www.continuum.io/downloads>

    > Anaconda is the leading open data science platform powered by Python. The open source version of Anaconda is a high performance distribution of Python and R and includes over 100 of the most popular Python, R and Scala packages for data science.

* Jupyter <http://jupyter.org/>

    > The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.
    > Similar to Mathematica notebooks

* Spyder <http://pythonhosted.org/spyder/> (maybe down)
    > Spyder is an interactive Python development environment providing MATLAB-like features in a simple and light-weighted software.




# Basic python syntax


Opening up the python interpreter 

```
ThisBeSilver:2017 - Python workshop diogoaguiam$ python
Python 2.7.12 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:43:17) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> 
```


Python Syntax

```
>>> 1+3
4
>>> a = 3
>>> a + 6
9
>>> b = "Hello world"
>>> b
'Hello world'
>>> print b
Hello world
>>> a = 3 # This is a comment
>>> a
3
>>> """ This is another comment """
' This is another comment '
>>> """ It can be multiline 
... like this """
' It can be multiline \nlike this '
>>> 

```


Python can handle automatically the data formats: int, floats, complex, hex

```
>>> 1
1
>>> 1.0
1.0
>>> 32
32
>>> 3/2
1
>>> 10
10
>>> 1.2
1.2
>>> 0x30
48

>>> 
```

Mathematical operators: + - * / % **

```
>>> 1+2
3
>>> 2-1
1
>>> 2*2
4
>>> 10/5
2
>>> 10/3
3
>>> 10/3.0
3.3333333333333335
>>> 2**8
256
>>> 2**10
1024
>>> 2**10.1
1097.496025637164
>>> 2**10.
1024.0
>>> 0+1j + 2-3j
(2-2j)
>>> 
```



Typical elements of python

### Lists







#### Conditions

Let's do some conditions now

Comparison operators:
 * `<` ... Less than
 * `>` ... More than
 * `<=` ... Less than or equal
 * `>=` ... More than or equal
 * `==` ... Equal to
 * `<>` ... Different
 * `!=` ... Different
 * `is` ... Equality between objects
 * `is not` ... Inequality between objects
 * `in` ... Is contained in list
 * `not in` ... Is not contained in

always return a `True` or `False`


```
>>> a = 1
>>> a == 1
True
>>> a != 1
False
>>> a >= 1
True
>>> b = 2
>>> a == 1 and b == 2
True
>>> a == 1 and b != 1
True

```


```
if <condition 1> :
    <instruction 1>
elif <condition 2> :
    <instruction 2>
...

else :
    <default instruction>
```

Example

```
>>> x = 1
>>> if x == 1:
...     print 'x is 1'
... else:
...     print 'x is not 1'
... 
x is 1
>>> 
```

What about checking if the name you are asking is inside a valid name list?

 ```
>>> namelist = ['John', 'Maria', 'Mohammed']
>>> user = 'George'
>>> if user in namelist:
...     print 'user', user, 'is in the name list'
... else:
...     print 'user',user, 'is not in the name list!'
... 
user George is not in the name list!
>>> 
```



#### Loop sequences


```
while <condition>:
    <instructions>

else:
    <else instructions>
```
Example:

```
>>> i = 0
>>> while i<=5 :
...     print 'Number:',i
...     i += 1
... 
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
>>> 
```


```
for <variable> in <sequence or list >:
    <instructions>
else:
    <else instructions>
```

```
>>> for i in range(5):
...     print 'Number',i
... else:
...     print 'Loop finished!'
... 
Number 0
Number 1
Number 2
Number 3
Number 4
Loop finished!
>>> 
```





