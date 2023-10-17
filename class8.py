"""
Data Structures
    1)list
    2)tuple
    3)dictinoary
    4)set
    
"""

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

'''
x = []
print(type(x)) # <class 'list'>
'''

x = [1,40,1,2,1,30,2,3]

# append
x.append(50)# [1, 2, 3, 40, 30, 50]
#x.append([1,2,3])#[1, 2, 3, 40, 30, 50, [1, 2, 3]]

# extend
x.extend([1,2,3,3])#[1, 2, 3, 40, 30, 50, 1, 2, 3, 3]

'''
x = [5,4,3,2]
y = [3,4,5]
x.extend(y) # [5, 4, 3, 2, 3, 4, 5]
'''

# sort
z = [1,2,6,10,1,0,3,10]

z.sort()# [0, 1, 1, 2, 3, 6, 10, 10]
z.sort(reverse=True)# [10, 10, 6, 3, 2, 1, 1, 0]
# print(sorted(z))# [0, 1, 1, 2, 3, 6, 10, 10]
# print(z)

#count
#print(z.count(3))#2

# indexing,insert, index
zz = [1,2,6,10,1,0,3,10]

#print(zz[6])#3
#print(zz[2:6])# [6, 10, 1, 0]

zz.insert(2,100)# [1, 2, 100, 6, 10, 1, 0, 3, 10]

#print(zz.index(10))#4


# clear,pop,remove,del
xy = [1,2,3,4,5,10]
xy.pop()
print("pop",xy)# [1, 2, 3, 4,5]

xy.remove(2)
print(xy)# [1, 3, 4, 5]

xy.clear()# [] empty list
print(xy)

del xy
# print(xy)# error will get



# functions
print(zz)
print("max",max(zz))
print("min",min(zz))
print("sum",sum(zz))
print("len",len(zz))
print("sorted",sorted(zz)) # [0, 1, 1, 2, 3, 6, 10, 10, 100]







































