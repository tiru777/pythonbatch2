# set

"""
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
"""

x = {4,5,6,7,8}
y = {1,2,3,4,5}
print(type(x))
print(type(y))

# add
y.add(10)
print("add:",y)

# update
x.update(y)
print(x)#{1, 2, 3, 4, 5, 6, 7, 8, 10}

# intersection
xx = {1,2,3,4,5}
yy = {3,4,5,6,7}

zz = xx.intersection(yy)#{3,4,5}
print("zz is intersection:",zz)
#union
xy = xx.union(yy)#{1,2,3,4,5,6,7}
print("union:",xy)

# diffrence
zy = xx.difference(yy)
print("difference:",zy)#{1,2}

# pop,popitem,discard,clear,del
xx = {1,1,2,2,23,4,5}

xx.pop()
print(xx)# {2, 3, 4, 5}

xx.remove(4)# {2,3,5}
print(xx)

xx.discard(5)
print(xx)
"""





"""
# dict:
x = {"a":123,"b":345}
y = dict()
yy = {"e":100,"c":200}

x["d"] =300
print(x)

x.update(yy)
print(x)

# sp key
print(x["a"])
print(x.get("a"))
print(x.keys())
print(x.values())
print(x.items())

'''
for key,value in x.items():# ([('a', 123), ('b', 345), ('d', 300), ('e', 100), ('c', 200)])
    print(key)
    print(value)
'''

x.pop("b")
print(x)
x.popitem()
print(x)

"""

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


'''

xx = []

for i in y:
    xx.append(i*i)
print(xx) # [1, 4, 9, 16, 25, 36, 49]

'''
"""
# list 
y = [1,2,3,4,5,6,7]
yy = [i*i for i in y]
print(yy)

#[expression iteration condition]

zz = [i*i for i in y if i%2==0]

print(zz)


#[expression if else iteration]
# [1,2,3,4,5,6,7]

zz = [i*i if i%2==0 else 0 for i in y ]# [0,4,0,16,0,36,]

print(zz)


"""
# tuple

"""
y = (1,2,3,4,5,6,7)
yy = tuple(i*i for i in y)
print(yy)

#(expression iteration condition)

zz = tuple(i*i for i in y if i%2==0)

print(zz)


#(expression if else iteration)
# [1,2,3,4,5,6,7]

zz = tuple(i*i if i%2==0 else 0 for i in y )# [0,4,0,16,0,36,]

print(zz)
"""



# dict
y = {"a":7,"b":4}
xx = {key:value*value for key,value in y.items()}
print(xx)# {'a': 49, 'b': 16}






















