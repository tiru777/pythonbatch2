```
Python:
---------
python is dynamic, interpretor, scripting,functional,
        object oriented and high level programming language
```

```
# Type Casting: COnvertion from one data type to other data type
```
```
# operators

# arithimetic operators: +, -,*, /,
                    #//(floor division means it will eliminate decimal value),% 
                    
# comparative operators: ==, !=

# relational operators: >,<,>=,<=
# logical operators: and(T and T=T), or(T or F == T) , not(opposite)
# Membership operators: in, not in
# identity operators: is , is not
# incremnetal operators : +=,-=,*=,/=
```

```
# string manipulations

upper: converting to upper case
lower: converting to lower case
isupper: checking whether upper or not and return TRue or False
islower:checking whether lower or not and return TRue or False
title: it will convert capital letter in each word of a sentence
capitalize: it will convert intial charector of a sentence
split: it will split the sentence based specified thing
replace: if you want replace particular string to specified new string
join: we can join specified str to sequence
       "str".join(sequence)


```

```
# flow controls or conditional statements

"""
# only if
if condition:
    print("if block will execute")

------------------------------
# if and else
if condition:
    print("if block will execute")
else:
    print("else block will execute")
---------------------------
# if ,elif and else

if condition:
    print("if block will execute")
elif condition:
    print("elif block will execute")
else:
    print("else block will execute")

"""


```
```
# indexing, print formats
"""
x = "prakash"

    -7 -6 -5 -4 -3 -2 -1   ===> Negitive index
x= "p   r  a  k  a  s  h"
    0   1  2  3  4  5  6   ===> Positive Index

x[sp_index]
x[start_index:stop_index]
x[start_index:stop_index:step_index]
```

```
# format strings
x = input("enter the name:")
y = int(input("enter the y value:"))

print("x value is and y value is",x,y)
print(f"{x} value x and {y} value is y")   # thirumala value x and 30 value is y

print("%s value x and %d value is y"%(x,y))# reddy value x and 22 value is y
print("{} value x and {} value is y".format(x,y)) # reddy value x and 22 value is y
```

```
"""
range: it will give values from one value to other
1).range(start)
range(start,stop)
range(start,stop,step)

print(range(5)) # range(0,5)
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(3,10)))# [3, 4, 5, 6, 7, 8, 9]
print(list(range(2,10,2)))# [2, 4, 6, 8]


"""
```

```
"""
They are two types of loops in python
1). For
    - for and break
    - for and continue
    - for and else
    syntax:
    for variable in sequence:
        print(variable)
2).while
    - while and break
    - while and continue
    - while and else

- break: it will break the loop 
- continue: 
"""

```

```
Data Structures
    1)list
    2)tuple
    3)dictinoary
    4)set
    


#list
"""
List:
    - list keyword or []
    - it's mutable data type
        - we can increase length of elements present in list or decrease
    - homogenous and hetrogenous it will support
    - it will allow duplicates
    - it will support indexing

Methods:
    - append
    - extend
    - count
    - sort
    - insert
    - remove
    - pop
    - clear
    delete
function
    - max,min,sum,len,sorted
"""

```

```
# tuple
"""
Tuple:
    - tuple keyword or ()
    - it's immutable data type
        - we can't increase length of elements present in list or decrease
    - homogenous and hetrogenous it will support
    - it will allow duplicates
    - it will support indexing

Methods:
    - count
    delete
function
    - max,min,sum,len,sorted
"""
```


```
# dict

"""
dictionary: it is a key and value pair ==>key:value
            - {},dict
            - it wont't indexing
            - keys: - are immutable
                    - unique
                    - shoudln't be dupliactes
                    - int,float,str
            - list:
                    - mutable
                    - dupliactes allows
                    - int,str,float,list,tuple,set,dict

methods:
    - add: dict[key] = value
    - update
    - items
    - dictinory.keys()
    - dictionary.values()
    - pop: we can delete specifc key
    - popitem: it will delete last key
    
"""
```
```
"""
# set
Set is : It won't duplicates
        - set() or {,}
        - homogenous and hetro
        - mutable ==> increase or decrease length
        - order not preserved
        - indexing won't allow
        
methods:
    - add
    - update
    - clear
    - pop: it will delete first element
    - remove
    - discard: it will delete sp element
    - count
    - intersection
    - union
    - diffrence
x = set()
"""
```

```
# comprehension
"""
    - list
    - tuple
    - dict
    - set
"""
"""
1) comp
    [expression loop]
    [i**1 for i in y]
2) conditions
    [expression loop condition]
3) [expression if else loop[]
"""


```
```

"""
Functions: Repeatable code will be reduced by making functions
    1) predefined function: print,sum,min etc
    2) userdefined functions
        - empty arguments: function()
        
        - positional argument or functions
            - function(arg1,arg2)
        - default arguments:
            - non default arguments first and dfeault arguments follows
            -  if you are defining a default argument while calling and
                passing any values to it it will override
        - variable length arguments: *args==>(1,2,3,4)
        - keyword arguments: **kwargs==>(x=20,y=30,z=40)
        
        - lambda function
        - generators
        - iterators
        - decorators

"""
```

```
# SDLC
Software Developement Life cycle
SDLC Methods:
    1) Agile
    2) water fall

Agile Methodology
====================

1)Requirement Phase
2)Analysis
3) HDD: High Level Design Document
4) LDD: Low level Design Document
5) Development
6) Testing Phase
7) Demo
8) Deployement
9) Maintenance

Agile Methodology: JIra SOftware-Scrum Board, Confluence
================================
- Epic: Project
- Product Backlogs: Projects features
- Sprint: Multiple of stories
- backlogs: Pending Stories
- Standup Mettings: 3 points: yesterday what you have done,today what your are going to do, blockers
- Sprint planning and review meetings: every sprint start and end
- Retrospective  meeting: monthly
"""
```
```
# lambda
"""
- we can write functions in single line
- for returning lambda will take care

syntax:

variable = lambda arguments:expression
vv = variable(10,20)
variable = (lambda arguments:expression)(values)

"""
```
```

# generator
"""
generator: it will use yield to return the data in the form generator objects
            -<generator object function_generator at 0x0000018B75CCBCA0>



        return                                              yield
        -------                                             -------
- return after it won't execute            - yeild after it will execute
- loop it will stop first iteration        - untill loop complete it will return data


"""
```
```
# iteration
"""
how we are doing loops in the same way we can perform using iter and next
x = iter(sequence)
print(next(x)
"""
```
```
# inner function or nested function
def function_outer():
    def inner_function():
        return "hey i am from inner function"
    z = inner_function()

    return z#  "hey i am from inner function"

z = function_outer()#  "hey i am from inner function"
print(z)

```

```
# function: return
# generator:yeild
# iterator: iter,next
# Decorator
"""
- decorator is a function, which will take function as argument

- without distrubing existing function, we can add features to that function
- it is represented by @ and it's a top of the function

"""

```

```commandline

"""
Exceptional Handling or Error Handling(Solve)
- Whenever error raises the interpretor abnormally terminates script
    for handling the error we are going to execeptional handling

-------
M1:
---
try:
    - error possible area

except:
    - error handle area

M2
---
-->if you want to know what error you should go this
try:
    ---
except Exception as error:
    print("error found:",error)

M3:
---
- if you know exact error
try:
    ---
except TypeError:
    print("error got")

M4:
----
try:
    ----
except Exception:
    ----
finally:
    ----if error raise or error won't raise it will execute

M5:
----
try:
    ---
except:
    ---
else:
    - if error won't raise in try block it will execute otherwise it won't
M6:
---
    raise: we can explicitly error
    raise Exception("error description")
    raise SPError("error description")
"""
```

```commandline
# file handling:
"""
we can handle files using multiple modes or methods

modes:
----------
r --> to read the file
w --> to write the file(it will override existing file data with new data),
      - it will create & override a file if not exist
a --> to add the data to existing file
r+ --> read and write
w+ --> write and read
a+ --> append and read
x --> exclusive creation(if file not there it will create, if file is there it will raise error"

# Open: if we open file we have to close
variable = open("file_name",mode)
v.name
v.mode()
v.closed()


# with: no need to close, it will close automatically
with open('file.txt','r') as fp:


Methods:Read
------
- read: it will read entire file data
- readline: it will give single line of file data
- readlines: it will give multiple lines in the list

methods:Write
------
write: any thing
writelines: multiple lines we can write

append
--------
- write

Seek: where you need to go to cursor
"""

```
```commandline

# Packages
"""
Package: if __init__.py file and multiple python files or modules is called
library: __init__.py,1package or one more packages
module: python file
packages: __init__.py+ modules

import module_name
---------------
    - you will get all the functions and variables from the module

from module_name import function
-----------------------------
    - you will get here specfic function only

from module import *
-------------------------
    - we can import all functions and variables from the module

as means alias
---------------
    - if your module is big name we can change name just like nick name
"""

```

```
"""
Name spaces
----------------
Local variables or space or scope: we can access inside function or class only 
global variable: we can access inside of the function or class,and also outside of the function or class
    - if you want to change global variable value you can use global keyword then it will change
"""
```
```commandline
"""
OOPS: Object Oriented Programming System
    - code repeatability reduce
    - using class keyword we can represent

Methods:
    - Instance method: whenever self keyword is there is called
    - class method: when argument is cls it is called as class method and
                    # we have to represent by using @classmethod
    - static method: if you don't need cls or self arguments passing to
                    # method you can using @staticmethod
    - constructor or initializer
    - Destructure




1) Inheritance
2) polymorphism
3) Encapsulation

-----
4) Abstract

# Defining class
class Employee:# class Name
    pass

ee = Employee()# Object or instance of the class
print(ee)


"""
```