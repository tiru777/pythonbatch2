# lambda
"""
- we can write functions in single line
- for returning lambda will take care

syntax:

variable = lambda arguments:expression
vv = variable(10,20)
variable = (lambda arguments:expression)(values)

"""
"""
def function(x,y):
    return x+y

z = function(10,20)
print(z)

zz = lambda x,y:x+y
print(zz(10,20))




def function(*args):
    return sum(args)


zzz = function(10,20,30)
print(zzz)

zzzz = lambda *args: sum(args)
print(zzzz(10,20,30))
"""

# generator
"""
generator: it will use yield to return the data in the form generator objects
            -<generator object function_generator at 0x0000018B75CCBCA0>



        return                                              yield
        -------                                             -------
- return after it won't execute            - yeild after it will execute
- loop it will stop first iteration        - untill loop complete it will return data


"""
'''
def function(*args):
    for i in args:# (10,20,30,40)
        return i*i# 10*10=100

zz = function(10,20,30,40)#100
print(zz)#100

def function_generator(*args):
    for i in args:# (10,20,30,40)
        yield i*i# 10*10=100

zz = function_generator(10,20,30,40)#100
print(list(zz))#100

'''
# iteration
"""
how we are doing loops in the same way we can perform using iter and next

"""
"""
x = list(range(10))#[0,1,2,3,4,5,6,7,8,9]
zz = iter(x)

print(next(zz))#0
print(next(zz))#1
print(next(zz))#2
print(next(zz))#3
"""
# inner function or nested function

'''
def function_outer():
    return "hey i am from outer function"
'''

'''
def function_outer():
    def inner_function():
        return "hey i am from inner function"
    
    return "hey i am from outer function"
'''
'''
def function_outer():
    def inner_function():
        return "hey i am from inner function"
    zz = inner_function()

    return "hey i am from outer function"
'''
def function_outer():
    def inner_function():
        return "hey i am from inner function"
    z = inner_function()

    return z#  "hey i am from inner function"

z = function_outer()#  "hey i am from inner function"
print(z)




















































