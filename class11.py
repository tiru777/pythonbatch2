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

def func_name_pr():
    print("hello")
    
zz = func_name_pr()# call func
print("function data:",zz)


'''
def func_name():
    return "hello"
    
zz = func_name()# call func
print("function returned data:",zz)

def dollo_650(arg):#3
    return arg*arg#3*3=9


zz = dollo_650(3)
print(zz)

'''

"""
# empty arguments
def function():
    return 123

zz = function()
#print(zz)

# positional arguments

def function(x,y,z):# 10,20,1
    
    if x>y or y<z:#10>20 and 20<1
        return True
    
    else:
        return False


zz = function(20,10,1)
#print(zz)

# default arguments
    # non default arguments first and dfeault arguments follows
    # if you are defining a default argument while calling and
            #passing any values to it it will override

def function(x,y=33,z=10):# 10,33,10
    
    if x>y or y<z:#10>33 and 33<10
        return True
    
    else:
        return False


#zz = function(10)
zz = function(30,20,40)
#print(zz)

# keyword argument

def function(x,y):
    return x*y

zz = function(y=30,x=20)
print(zz)

"""


# variable length arguments

def function_prakash(*arg):

    x = []
    for i in arg:#(10,3,5,6,7)
        x.append(i*i)
        
    return x
    

#print(function_prakash(10,3,5,6,7))


# variable length of keyword arguments
def function_key(**kwargs):
    return( kwargs) # dictionary


zz=function_key(y=30,x=20,z=40)
print(zz)# {'y': 30, 'x': 20, 'z': 40}



















