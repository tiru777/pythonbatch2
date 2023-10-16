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
'''
x = ()
#print(type(x))

'''
'''
x = (1,2,1,1,1,3,4,5,6)
# count
print(x.count(1))#4

#sorted
print(sorted(x))# [1, 1, 1, 1, 2, 3, 4, 5, 6]

# min,max,sum
# functions
print("max",max(x))
print("min",min(x))
print("sum",sum(x))
print("len",len(x))
print("sorted",sorted(x))

# indexing
print(x[3])# 1
print(x[1:7])
'''
'''
# delete
del x

print(x)
'''
'''
# tuple to list to tuple
x = list(x)
print(type(x))

x.append(100)
print(tuple(x))#(1, 2, 1, 1, 1, 3, 4, 5, 6, 100)

'''
'''
for i in x:
    print(i*3)

'''

#=========================================================

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
'''
#type_check
x = {}
print(type(x))# <class 'dict'>
'''

x = {"a":10,"b":30,"c":55}

# keys
print(x.keys())# dict_keys(['a', 'b', 'c'])
print(x.values())# dict_values([10, 30, 55])
# specific key values
# syntax =
    #x["key_name"])
print(x["b"])# 30

# get: x.get("key_name)
print(x.get("a")) # 10

# add

x["name"]="prakash"
print(x)# {'a': 10, 'b': 30, 'c': 55, 'name': 'prakash'}


# update
y = {"z":100,"cc":200,"dd":500}

x.update(y)
print(x)


# items: converted to tuples 
print(x.items())

# for loop
'''
for key,value in x.items():
    print("key:",key)
    print("value:",value)
'''

# pop: specfic key
x.pop("a")
print(x)

# popitems: last key will remove
x.popitem()
print(x)

# clear
x.clear()
# del x





























































