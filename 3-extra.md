# Advanced features of python

* Importing other scripts
* Passing arguments into python script from terminal
* 


# Importing an existing script and running its functions

We can import the functions of other scripts into our current script.


script1.py
```python

def print_message():
    print 'Hello this is script 1'

if __name__ == "__main__":
    print 'Executing script1.py directly'
    print_message()
```

script2.py
```python
import script1
def print_message():
    print 'Hello this is script 2'

if __name__ == "__main__":
    print 'Executing from script2'
    print_message()
    script1.print_message()
```


```bash
$ python script1.py
Executing script1.py directly
Hello this is script 1
$ python script.py
Executing from script2
Hello this is script 2
Hello this is script 1
$ 
```


# Using `argparse` module to parse command line arguments into our python project

script.py
```python
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print args.echo
```

```bash
$ python script.py 
usage: script.py [-h] echo
script.py: error: too few arguments
$ python script.py  -h
usage: script.py [-h] echo

positional arguments:
  echo

optional arguments:
  -h, --help  show this help message and exit
$ python script.py this is a message
usage: script.py [-h] echo
script.py: error: unrecognized arguments: is a message
$ python script.py "this is a message"
this is a message
$ 
```

