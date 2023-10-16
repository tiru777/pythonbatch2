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