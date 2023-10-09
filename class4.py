# string manipulations
"""
upper: converting to upper case
lower: converting to lower case
isupper: checking whether upper or not and return TRue or False
islower:checking whether lower or not and return TRue or False
title: it will convert capital letter in each word of a sentence
capitalize: it will convert intial charector of a sentence
split: it will split the sentence based specified thing
replace: if you want replace particular string to specified new string
join: we can join specified str to sequence
       "str".join(sequence)

"""

x = "syed basha"
y = x.upper() # SYED BASHA
yy = x.lower() # syed basha
yy.isupper() # False
yy.islower() # True

yyy = x.title() # Syed Basha
xx = x.capitalize() # Syed basha

z = x.split() # ['syed', 'basha']

x.split('d') # ['sye', 'basha']

x.replace("syed","prakash") # prakash basha prakash

"python".join(x)  # spythonypythonepythondpython pythonbpythonapythonspythonhpythona


# starts with

x.startswith("s") # True
#endswith
#print(x.endswith("f")) # False






# input
"""
x = input("enter the string:") # Thirumala Reddy
print(type(x))
x = x+" balireddigari"
print("string is:",x) #Thirumala Reddy balireddigari
"""
"""
x = input("enter the x value:")   # type str #10
y = input("enter the y value:")    #  type str #30

print("sum of x and y",int(x)+int(y)) # 40
"""
"""
x = int(input("enter the x value:"))   # type str #10
y = int(input("enter the y value:"))


print("sum of x plus y",x+y)

"""

x = int(input())
u = int(input())
print(x+u)
































