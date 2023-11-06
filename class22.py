"""
MYSQL Integration: connecting with database using python
commit(): data after insert or delete must use commit
fetchone(): it will fetch one record
fetchall(): it will  fetch all record

cursor.execute(query)

"""
import mysql.connector


def mysql_connection_select():
    # localhost or 127.0.0.1
    mysql_db = mysql.connector.connect(host="localhost", username="mysqlroot",
                                       password="root", database="pythondb")
    my_cursor = mysql_db.cursor()
    my_cursor.execute("select * from customers")
    # data = my_cursor.fetchone()
    data = my_cursor.fetchall()
    return data


def data_insert():
    mysql_db = mysql.connector.connect(host="localhost", username="mysqlroot",
                                       password="root", database="pythondb")
    my_cursor = mysql_db.cursor()
    # my_cursor.execute("""INSERT INTO Customers(employeeid,lastname,firstname,address,city) VALUES(3,"syed","firdose","rvp","bgl")""")

    query = "INSERT INTO Customers(employeeid,lastname,firstname,address,city) VALUES(%s,%s,%s,%s,%s);"
    values = ("3","prakash","gg","mpl","bgl")
    my_cursor.execute(query,values)

    mysql_db.commit()
    my_cursor.execute("select * from customers;")
    data = my_cursor.fetchall()
    print(data)


# data_insert()

def table_creation():
    mysql_db = mysql.connector.connect(host="localhost", username="mysqlroot",
                                       password="root", database="pythondb")
    my_cursor = mysql_db.cursor()
    query = "create table pythonclass (id int,name varchar(20),address varchar(30))"
    my_cursor.execute(query)


# table_creation()
def data_delete():
    mysql_db = mysql.connector.connect(host="localhost", username="mysqlroot",
                                       password="root", database="pythondb")
    my_cursor = mysql_db.cursor()
    # query = "delete from customers where lastname='syed';"
    query = "drop table pythonclass"
    my_cursor.execute(query)
    mysql_db.commit()


# data_delete()
# print(mysql_connection_select())

"""
# multi threading and multiprocessing

if you want to run multiple functions or classes parallel
- time reduce
"""
import threading
def func_sum(arg):
    print(arg+arg)

def func_mult(arg):
    print(arg*arg)

t1 = threading.Thread(target=func_sum,args=(20,))
t2 = threading.Thread(target=func_mult,args=(20,))

t1.start()
t2.start()
t1.join()
t2.join()
