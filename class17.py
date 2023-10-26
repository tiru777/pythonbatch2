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
# Ex: Specific module
"""
import class16
zz = class16.file_write("tttt.txt")
print(zz)
"""

# specific function or variable we can import
"""from class16 import file_write
zz = file_write("tttt.txt")
print(zz)"""

# we can import all functions, variables
"""from class16 import *
z = file_write("reddy.txt")
y = file_append("reddy.txt")
print(z)
print(y)"""

# as: alias
"""import library.package1.test1 as fp
zz = fp.function(4000)
print(zz)"""

"""# entire module 
from library.package2 import test1

z = test1.function(300)

from library.package1.test1 import function
function(300)"""

"""
Name spaces
----------------
Local variables or space or scope: we can access inside function or class only 
global variable: we can access inside of the function or class,and also outside of the function or class
    - if you want to change global variable value you can use global keyword then it will change
"""
z =10# global variable
def local_function(x):
    y = 2# local variable
    return x*y
# print(local_function(100))#200


def global_function(x):
    """
    global variable we can access inside of the function and outside of the function
    :param x:
    :return:
    """
    return x+z


# print(global_function(5))
def global_var_mod_function(x):
    """
    global variable we can access inside of the function and outside of the function
    :param x:
    :return:
    """
    global z
    z = 20
    return x+z # 10+20


print(global_var_mod_function(5))# 25
print("global variable:",z)