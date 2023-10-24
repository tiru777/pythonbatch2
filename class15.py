"""
Exceptional Handling or Error Handling(Solve)
- Whenever error raises the interpretor abnormally terminates script
    for handling the error we are going to execeptional handling

-------
M1:
---
try:
    - error possible area

except:
    - error handle area

M2
---
-->if you want to know what error you should go this
try:
    ---
except Exception as error:
    print("error found:",error)

M3:
---
- if you know exact error
try:
    ---
except TypeError:
    print("error got")

M4:
----
try:
    ----
except Exception:
    ----
finally:
    ----if error raise or error won't raise it will execute

M5:
----
try:
    ---
except:
    ---
else:
    - if error won't raise in try block it will execute otherwise it won't
M6:
---
    raise: we can explicitly error
    raise Exception("error description")
    raise SPError("error description")
"""
# Ex1:
"""try:
    x = 10
    y = "tirumala"
    print(x+y)
except:
    print("error found in try block")
print("hellow world")

#Ex2
try:
    x = 10
    y = 0
    z = x/y

except Exception as error:
    print("error is:",error)
"""
# Ex3
"""try:
    x = 10
    y = 0
    z = x/y

except Exception as error:
    print("error is:",error)

except:
    print("error found")"""

# Ex
"""
    try:
        x = 10
        y = "reddy"
        print(x+y)
    
    except TypeError:
        print("error is type error")
    
    except Exception as error:
        print("error is:",error)
    
    except:
        print("error found")
"""
# finally
"""
try:
    z = str(10) + "reddy"
    

except TypeError:
    print("error is type error")

except Exception as error:
    print("error is:", error)

finally:
    print("i am from finally block")
"""


# with function
"""def excep_func(x,y):
'''    
    :param args: sequence of elements
    :return: sum of args
    '''
    try:
        z = str(x)+y
        return z

    except TypeError:
        print("error is type error")

    except Exception as error:
        print("error is:",error)

    finally:
        print("i am from finally block")



zz = excep_func(10,"reddy")
print(zz)"""

# Else
"""
try:
    z = str(10) + "reddy"

except TypeError:
    print("error is type error")

except Exception as error:
    print("error is:", error)
else:
    print("i am from else block")
finally:
    print("i am from finally block")
"""

x = 10
y = x+20
print(y)
raise TypeError("Sorry, no numbers below zero")
raise Exception("Sorry, no numbers below zero")