# inner function


'''
def outer_function(x,y):
    def inner_func(x,y):
        return x+y
  
    x= inner_func(x,y)
    return x

x = outer_function(1,2)
print(x)
'''
# function: return
# generator:yeild
# iterator: iter,next
# Decorator
"""
- decorator is a function, which will take function as argument

- without distrubing existing function, we can add features to that function
- it is represented by @ and it's a top of the function

"""
def dec_func(func):
    def inner(x,y):
        if x>y:
            zz = func(x,y)
            return zz
        return "x is less than y"
    
    return inner


@dec_func
def func_sum(x,y):
    return x+y


# print(func_sum(10,20))

#---------------------------------

def func_check(func):
    return func


@func_check
def func():
    return "i am from main function"


xx = func()
print(xx)




























