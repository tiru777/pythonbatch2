
# input
x = [1,2,3,4,5]
y = (4,5,6,7)
z = {10,20,30,40}

# output: (1,2,3,4,5,6,7,10,20,30,40)

def collective(arg1,arg2,arg3):
     x = list(arg1)
     y = list(arg2)
     z = list(arg3)
     x.extend(y)
     x.extend(z)
    #data = list(arg1)+list(arg2)+list(arg3)
     return tuple(x)

d = collective(x,y,z)
print(d)
