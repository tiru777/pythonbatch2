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
    - Destructure: if you want to delete Object, __del__ method




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
```commandline
"""
OOPS:

1) Inheritance
    i) single inheritance: single parent class to child class.
                    Ex: parent and child
    ii) multi level inheritance:one parent class to other child class from that to another child class
                    Ex: grand_father+ father = child
    iii) multiple inheritance:two parent classes methods we can inherit to child class
                    Ex:father+mother = child
    iv) hierarchical inheritance: we can inherit single base class to many child classes

2) polymorphism:this is called a method overriding or method overloading
3) Encapsulation: means data hiding or protecting or data binding
    -- public: you can access anywhere
    -- protected: you can access outside of the function but specifuc respective of the object using underscore (_)
    -- private: you are not able access private methods are variable outside of the function
                : if you want access you have to provide 
                # object._classname__privatemethod()
    
4) abstract method: From Abc import abstractmethod and ABC
                    # @abstractmethod
                    # abstract means hiding
"""
```
```
"""
Logging: The main purpose is used to debug or get the information execution
- Critical: 50
- Error: 40
- warning: 30
- info: 20
- debug: 10

SYntax
------
import logging
logging.basicConfig()

M1:
--------
logging.basicConfig()# by default logging.WARNING
# it will display only warning messages

M2:
------------
If you need all
    - logging.DEBUG

M3:log file creation
------------------
logging.basicConfig(filename="logs.log",level=logging.DEBUG)
"""
```
```commandline
"""
# Regular Expression:
find  the pattern(string or numbers) in raw string

Methods:
    - match: it will match first pattern in starts of the string
    - search: it will search return single matched pattern in entire string
    - findall: it will return all matched patterns in the string
    - sub: whenever matches it will substitute the pattern
    - split: whenever pattern matches it will split
---

Pattern conditions
------------------
[0-9] --> it will return single matched number
\d --> it will return single matched number
[a-zA-Z] --> it will return single matched charector
\w --> it will return single matched charectr [a-zA-Z0-9]
^ --> it is used for start of the string
$ --> it is used for end of the pattern
{} --> {1,} how many characters or numbers present in string
. --> single characters return
\s --> single space
* --> 0 or more occurances
+ --> 1 or more occurences

# match: it will match start of the string
# re.match(pattern,string)

#search: it will search not only start of the string, and also it will search middle but
        # it will return single
# re.search(pattern,string)

# find all: it will return all matched patterns
# re.findall("pattern",str)

# sub: it will substitute when pattern matches
# re.sub(pattern,sub)

# split: based pattern will split
d = re.split("\s",x)

"""
```
```commandline
"""
MYSQL Integration: connecting with database using python
commit(): data after insert or delete must use commit
fetchone(): it will fetch one record
fetchall(): it will  fetch all record

cursor.execute(query)

"""

```
```commandline
"""
# multi threading and multiprocessing

if you want to run multiple functions or classes parallel
- time reduce
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
Database:It is used to store the records 
Two Types of Databases: 
    - SQL:RDBMS
        - MYSQL,ORACLE,POSTGRESS,MS SQL etc
    - NOSQL
        - DYnamo DB, MONGODB
        
SQL: Structured Query Language

SQL: SQL is a standard language for accessing and manipulating databases.
    - SQL is used to fetch, update, insert,delete,create

      
============================================

Select: To fetch all records, 
------------------------------
Select * from table_name;

Top =>few records
----------------------------------
Select TOP 3 * from table_name;

count,min,max,sum,avg
---------------------------------
select count(*) from table_name;
select sum(price) from table_name
select max(price) from table_name;
select min(price) from table_name;
select avg(price) from table_name;

where,and,or,not
----------------------------------
select * from table_name where price = 2000;
select * from table_name where price =2000 and name = "akhil";
select * from table_name where price =2000 or name = "prakash";
select * from table_name where not name = "syed";

order by: ASC default , DESC
---------------------------------------------
select * from table_name where name order by desc;

DISTINCT: only unique elements , alias; as, like
------------------------------
select distinct city from table_name;
select * from table_name as fp where fp.price = 2000;
select * from table_name where firstname like "ak%";

update:
---------------------
update table_name set column=value where column=value

delete
-----------------------
delete from table_name where column=value

is null or is not null
---------------------
select * from customers where address is Null
select * from customers where address is not Null

joins: two join two or more tables 
------------------
select table1.id, table2.id from table1
inner join table2
on table1.firstname = table2.firstname


inner join: common elements from both tables
left join: left table records and matched records of right table
right join: right table records and matched records of left table
full join: combain of two tables
union: combain of two tables

Group by: grouping based on any column vaue
------------------
select * from table group by column

having: its like where condition but we should along with group by
-------------------------------------
select * from table 
group by column 
having column=value

Database creation or drop
---------------------
Create Database database_name
show databases;
drop database database_name # both table and data
truncate database database_name # only delete not table 

Constraints
--------------
Not Null: mandatory column
unique: value should be unique
primary key: its combination of not null and unique
foreign key: relation between two tables
check: check field value
default: insert default value

Create table
----------------
create table table_name(
        column1 data_type constraint,
        column1 data_type constraint,
        )

CREATE TABLE Employee(
	Employeeid int,
	LastName varchar(255),
	FirstName varchar(255),
	Address varchar(255),
	City varchar(255)
	);
	
drop and truncate
-------------
drop table Employee;
truncate table Employee;

alter
-------------
alter table Employee add Country varchar(20);
alter table Employee drop City;
ALTER TABLE employee RENAME COLUMN LastName to new_name;
alter table Employee modify FirstName varchar(100);

constraint
----------------------------
CREATE TABLE Customers(
	Employeeid int primary key,
	LastName varchar(255),
	FirstName varchar(255) unique,
	Address varchar(255) Not null,
	City varchar(255) DEFAULT "bangalore"
	);
	
foreign key relation
------------------

CREATE TABLE Orders (
    OrderID int PRIMARY key,
    OrderNumber int NOT NULL,
    PersonID int,
    FOREIGN KEY (OrderID) REFERENCES Customers(Employeeid)
);
    
insert
-----------------------
INSERT INTO Customers (Employeeid, LastName, FirstName, Address)
VALUES (1,"reddy","thirumala","rvp");

fetch two table data using joins
-----------------------------------
select * from Customers 
Inner join orders 
on Customers.Employeeid=Orders.OrderID;
```
```Linux

ls : list of items in the current folder
ls -a: list of items and hidden items in the current folder
cd : change directory
pwd : present working directory
mkdir :create new directory
rmdir :remove directory(folder)
chdir :change directory
rm :remove file or folder ex:rm *.jpg removes all jpg files
*  wild card
mv :move or rename a file or folder to a new location

touch :creating new file ex:touch file.txt
cat : display the file content ex:cat file.txt
less : display portion of a file and file content
curl :used for file transfer
clear : clear in terminal
whoami: username
uname: username
passwd: password change
history: 
zoom in :ctl+shift++
zoom out:ctl --
vi: editor using "i" insert, for saving ESC+:+wq,not save ESC:q!



```
