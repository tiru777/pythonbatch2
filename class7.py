# Loops and range

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

'''
name = input("Enter your name:")# Prakash

for i in name:# prakash
    print(i)

for i in range(10):
    #print(i,end="")
    print(i)

for i in range(5,10,2):
    #print(i,end="")
    print(i)
'''

#break
"""
for x in range(2,10):
    if x ==5:
        break
    print(x)

for x in "thirumala reddt":
    if x == "m":
        break
    print(x)

"""
#for and else: whenever for block completes iterations else will execute,
                #when for iteration breaks it wont execute
'''
for i in range(10):
    print(i)
else:
    print("loop completely executed")

for i in range(5):
    if i==4:
        break
    print(i)
else:
    print("else won't execute")
'''

# continue: when ever specified value satisfied condition
              #it will skip to next iteration

"""
for i in range(7):
    if i ==5:
        break
    print(i, end="")# 01234
    
for i in range(8):
    if i ==5:
        continue
    print(i)
"""

#while: unitl while condition not satified loop will executes
"""
while True:
    x= input("enter your name:")
    print(x)
"""
"""
x = 0

while x<6:# True(0<6),1<6 True,2<6,3<6,4<6,5<6,6<6
    print(x)#0,1,2,3,4,5
    x = x+1#1,2,3,4,5,6
"""

"""
x = "praash"

while "k" in x:
    x = x+"reddy"
    print(x)# praash reddy

x = 7
while x%2 !=0:#1 !=0,6%2=0,0!=0
    print(x)#7
    x = x-1#6
"""






    


















