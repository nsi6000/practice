# Python
## Libraries:
### ML and Viz:
* numpy
* pandas
* matplotlib
* numba
* seaborn
### CICD:
* pylint
* pylama
* flake8
* autopep8
* pytest
* Faker
* proselint
* bandit
* vulture
* behave
* see [RealPython Refactoring article](https://realpython.com/python-refactoring/)
	* rope (refactoring using the REPL)
	* radon (cc: code complexity / mi: maintenance index)
	* wily (=> as hook using pre-commit)
	* dataclasses (python >3.7) (or "attrs" if lower version)
	* Handling Complex Dictionaries With Query Tools => JMESPath, glom, asq, and flupy.

### Connectors:
* pyspark
* pyflink
* pulsar
* pymongo
* cassandra-driver
* confluent-kafka
* airflow
* redis
* pykka
* pyodbc (SQL Server)
* neo4j
* (mysql)
* psycopg\[binary\]
### Misc:
* msgpack
* pprint
* jsonschema
* greatexpectations



## Beginner:
* Variables
* Conditions
* Chained Conditionals
* Operators (+ / - * ** % //)
* Control Flow (If/Else)
* Loops and Iterables
* Basic Data Structures
	* Lists
	* Tuples
	* Dictionaries
	* Sets
	* Strings
	* Booleans
	* Ints and floats
* Functions
* Mutable vs Immutable Data Types
* Common Methods (upper, lower, add elem,...)
* File IO (read/write text/csv file)
## Intermediate:
* Object Oriented Programming (Classes and Objects)
* Data Structures (queues, hashmaps, stacks, trees,...)
* Comprehensions (lists, dicts, sets,...)
* Lambda Functions
* Map, Filter
* Collections
* The Asterisk (*) Operator (*args & **kwargs)
* Inheritance (+ polymorphism)
* Dunder Methods
* PIP
* Environments
* Modules
* Async IO
## Expert:
* Decorators
* Generators 
* Context Managers
* Metaclasses
* Concurrency & Parallelism (Multithreading + Multiprocessing)
* Testing (unittest, pytest)
* Packages
* Cython


* Itertools
* Exceptions and Errors
* Logging
* JSON
* Random Numbers
* Function Arguments
* Shallow vs Deep Copying


## NumPy
* TODO

```python
#Array : same data types.
#1D array = vector
#2D array = matrix

import random
import numpy as np
a = np.array([[0,1,2,3],[4,5,6,7]])
a.shape
a[1,3]
a[1,2] = 8
a[1]

prob = random.random()
prob2 = random.randint(1,6)

np.random.randint(1,6,(4,6))

np.dot(returns, weights)
np.array.T #transpose of matrix.
```

## Pandas
* TODO

```python
import numpy as np
import pandas as pd

ser = pd.Series(np.random.random(5), name = "Column 01")
ser
ser[2]
# Series are like dictionaries

pd.DataFrame.mean()
pd.DataFrame.std()
pd.DataFrame.var()
pd.DataFrame.cov()
pd.DataFrame.corr()

mydata.shift(1)
mydata.iloc[0]
mydata.loc['Adj Close']
```

## Matpotlib
* TODO

```python
import matplotlib.pyplot as plt

.show()
plt.scatter(X,Y).axis([0,2500,0,1500000]).show()
plt.ylabel('House Price')
plt.xlabel('House Size')
```


```python
from scipy import stats
import statsmodels.api as sm

#linear regression with sm
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()

#linear regression with scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
```


```python
from pandas_datareader import data as wb

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
#PG = Ticker of Procter-Gamble.
PG
PG.info()
PG.head()
PG.tail()
PG.head(20)
PG.tail(20)


tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_data = pd.DataFrame()
for t in tickers:
	new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']
new_data.tail()


import quandl
mydata_01 = quantdl.get("FRED/GDP")
mydata_01.head()

import pandas as pd
mydata_01.to_csv('C:/Python/examples_01.csv')
mydata_02 = pd.read_csv('C:/Python/examples_02.csv', index_col='Date')
mydata_02.to_excel('C:/Python/examples_03.xlsx')
mydata_03 = pd.read_excel('C:/Python/examples_03.xlsx')
mydata_03 = mydata_03.set_index('Year') #assignment because set_index doesn't apply it by itself.
```




```python
from fibo import fib as fibonacci
#Libraries: numpy, pandas, matplotlib, math, random, statsmodel, quandl.
print("Hello World.")
type()
x = 1.5
int / float / string / True-False.
casting: int(), str(), float().
+ - * / **
== != > < >= <= (is, is not)
#comment
line continuation: \
0-based indexes.
not and or (order: NAO)
IF ... ELIF ... ELSE ...
even = [0,2,4,6,8]
for n in even:
	print(n, end=" ")
x = 0
while x <= 20:
	print(n, end=" ")
	x += 2
range(10) == range(0,10,1)
def plus_ten(a,b,c):
	result = a + 10
	return result
functions: min() max() abs() sum() round() pow() len().
List = list(range(10))
List = ["a","b","c"]
List[1] List[-2]
List.apprend("d")
List[:2] List[4:] List[-2:]
List.index("b")
List.sort(reverse=True)
List3=[List1,List2]
Tuple = (1,2,3)
Tuple[0]
Dictionary = {"a":"cat","b":"dog"}
Dictionary["b"] = "parrot"
Dictionary.split(",")
Dictionary.get("cat")
```

## Azure VM Flask App
* create VM in Azure (b4ms)
* Add ports: VM settings -> Networking -> Add inbound/outbound port rule -> 5000.
* ssh -i <azure-vm-key>.pem azureuser@<IP-address-of-vm>
* sudo apt-get update
* sudo apt-get install python3 / python3-flask
* sudo pip3 install matplotlib
* vim app.py
    * matplotlib code (<https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py>)
    * import random
    * random.randint(1,5) x2
    * refresh to see changes.
* flask run --host 0.0.0.0
* go to browser: <vm-ip>:5000
* pip3 install yfinance
* import yfinance as yf
* tcs = yf.download('TCS', '2014-01-01', '2019-01-01')
* ax.legend()
* ax.plot(tcs['Volume'], label = 'TCS ticker')

## Idiomatic python:
* range() and enumerate()
* list/dict comprehension
* print() and breakpoint()/<variable-name>/n.
* f-strings
* sorted(animals, key=lambda animal: animal['age'])
* DSA: set, generator, dict, default dict, Counter, deque, namedtuple.
* functools - HOFs...
* itertools - iterators...
* \_\_main__
* zip/unzip dicts (**a)


