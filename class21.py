"""
# Regular Expression:
find  the pattern(string or numbers) in raw string

Methods:
    - match: it will match first pattern in starts of the string
    - search: it will search return single matched pattern in entire string
    - findall: it will return all matched patterns in the string
    - sub: whenever matches it will substitute the pattern
    - split: whenever pattern matches it will split
---

Pattern conditions
------------------
[0-9] --> it will return single matched number
\d --> it will return single matched number
[a-zA-Z] --> it will return single matched charector
\w --> it will return single matched charectr [a-zA-Z0-9]
^ --> it is used for start of the string
$ --> it is used for end of the pattern
{} --> {1,} how many characters or numbers present in string
. --> single characters return
\s --> single space
* --> 0 or more occurances
+ --> 1 or more occurences

# match: it will match start of the string
# re.match(pattern,string)

#search: it will search not only start of the string, and also it will search middle but
        # it will return single
# re.search(pattern,string)

# find all: it will return all matched patterns
# re.findall("pattern",str)

# sub: it will substitute when pattern matches
# re.sub(pattern,sub)

# split: based pattern will split
d = re.split("\s",x)

"""
import re

x = "thirumala reddy thirumala reddy thirumala"

"""
# match: it will match start of the string
# re.match(pattern,string)
data = re.match("thirumala",x)
print(data.group())"""

#search: it will search not only start of the string, and also it will search middle but
        # it will return single
"""
# re.search(pattern,string)
data = re.search("thirumala",x)
print(data.group())
"""

# find all: it will return all matched patterns
"""
# re.findall("pattern",str)
d = re.findall("thirumala", x)
print(d)
"""

# sub: it will substitute when pattern matches

'''
# re.sub(pattern,sub)
d = re.sub("thirumala","akhil", x)
print(d)
'''

# split: based pattern will split
"""
d = re.split("\s",x)
print(d)
print(x.split())

"""
xs = "CVAPB4576M  CVADB4576^ C#ADB4576MS CV23TB4576M CVAKB4576M CVAGB4576M CVAOB4576M"

# data = re.findall("[A-Z]{5}[0-9]{4}[A-Z]]",xs)
# data = re.findall("[A-Z]{2}\d{2}\s[A-Z]",xs)
# data = re.findall("[A-Z]{5}[0-9]{4}.",xs)
data = re.findall("\w{5}[0-9]{4}\w",xs)

print(data)

# [A-Z]{2}\d{2}[A-Z]





