# indexing, print formats
"""
x = "prakash"

    -7 -6 -5 -4 -3 -2 -1   ===> Negitive index
x= "p   r  a  k  a  s  h"
    0   1  2  3  4  5  6   ===> Positive Index

x[sp_index]
x[start_index:stop_index]
x[start_index:stop_index:step_index]
"""
'''
x = "akhileswar kumar"

print(x[6])#s
print(x[9])#r
print(x[11])#k
print(x[17])# indexout of range error
print(x[-4])#u
print(x[-7])#r
'''

'''
x = "prakash kumar"

print(x[2:8])#akash
print(x[5:11])#sh kum
print(x[:11])#prakash kum
print(x[11:13])# ar
print(x[7:])# kumar
print(x[:])#prakash kumar

'''
'''
x = "syed shaik firdose"

print(x[2:10])#ed shaik
print(x[2:10:1])#ed shaik
print(x[2:10:2])#e hi
print(x[5::2])#sakfroe
print(x[::2])#se hi ids
print(x[::1])# syed shaik firdose
print(x[::-1])#esodrif kiahs deys
print(x[::-2])#eorfkasdy
print(x[::-4])#erksy
#print(len(x))
'''

# format strings
x = input("enter the name:")
y = int(input("enter the y value:"))

print("x value is and y value is",x,y)
print(f"{x} value x and {y} value is y")   # thirumala value x and 30 value is y

print("%s value x and %d value is y"%(x,y))# reddy value x and 22 value is y
print("{} value x and {} value is y".format(x,y))




























