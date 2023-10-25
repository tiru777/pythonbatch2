# file handling:
"""
we can handle files using multiple modes or methods

modes:
----------
r --> to read the file
w --> to write the file(it will override existing file data with new data),
      - it will create & override a file if not exist
a --> to add the data to existing file
r+ --> read and write
w+ --> write and read
a+ --> append and read
x --> exclusive creation(if file not there it will create, if file is there it will raise error"

# Open: if we open file we have to close
variable = open("file_name",mode)
v.name
v.mode()
v.closed()


# with: no need to close, it will close automatically
with open('file.txt','r') as fp:


Methods:Read
------
- read: it will read entire file data
- readline: it will give single line of file data
- readlines: it will give multiple lines in the list

methods:Write
------
write: any thing
writelines: multiple lines we can write

append
--------
- write

Seek: where you need to go to cursor
"""
# Open: if we open file we have to close
"""
d = open('file.txt','r')
print("file name",d.name)
print("mode name",d.mode)
d.close()
print("check",d.closed)
"""
# with: no need to close, it will close automatically
"""with open('file.txt','r') as fp:
    print("file name", fp.name)
    print("mode name", fp.mode)
print("check",fp.closed)"""


# read mode
"""
Methods:
------
- read: it will read entire file data
- readline: it will give single line of file data 
- readlines: it will give multiple lines in the list
EX:
with open("file.txt",'r') as fp:
    # data = fp.read()# all data
    # data2 = fp.readline()# single line
    data3 = fp.readlines()# list
    print(data3)

"""
# read
def file_read(file_name):
    try:
        with open(file_name,'r') as fp:
            # data = fp.read()# all data
            # data2 = fp.readline()# single line
            data3 = fp.readlines()# list
            return data3
    except FileNotFoundError:
        print("file not available please check path")
    except Exception as error:
        print("error is:",error)
# d = file_read("file.txt")
# print(d)

# write:
"""
methods:
------
write: any thing
writelines: multiple lines we can write
"""
'''
def file_write(file_name):
    try:
        with open(file_name,'w') as fp:
            # data = fp.read()# all data
            # data2 = fp.readline()# single line
            fp.write("hellow syed, prakash, akhil")# list
            return "data written"
    except FileNotFoundError:
        print("file not available please check path")
    except Exception as error:
        print("error is:",error)
d = file_write("prakash.txt")
print(d)'''


# append
# methods: write or writelines

'''def file_append(file_name):
    try:
        with open(file_name,'a') as fp:
            # fp.write("hellow hellow")# list
            fp.writelines("hellow hsdjkhs d\n bgdhgs ds")
            return "data appended"
    except FileNotFoundError:
        print("file not available please check path")
    except Exception as error:
        print("error is:",error)
d = file_append("prakash.txt")
print(d)'''

# read and write

'''def file_append(file_name):
    try:
        with open(file_name,'r+') as fp:
            data = fp.read()
            fp.write("hellow")
            return "data read and appended", data
    except FileNotFoundError:
        print("file not available please check path")
    except Exception as error:
        print("error is:",error)
d ,x= file_append("prakash.txt")
print(d)
print(x)'''


# exclusive creation: mode :x

"""with open("syed.txt","x") as fp:
    fp.write("hellow")"""
with open("tiru.txt","r+") as fp:
    d = fp.seek(5)
    dd = fp.read()
    print(dd)