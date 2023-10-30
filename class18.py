"""
OOPS: Object Oriented Programming System
    - code repeatability reduce
    - using class keyword we can represent

Methods:
    - Instance method: whenever self keyword is there is called
    - class method: when argument is cls it is called as class method and
                    # we have to represent by using @classmethod
    - static method: if you don't need cls or self arguments passing to
                    # method you can using @staticmethod
    - constructor or initializer: whenever you defined or created object
                            # the first method internally calls to initializer
    - Destructure: if you want to delete Object, __del__ method

- Class level variables usage




1) Inheritance
2) polymorphism
3) Encapsulation

-----
4) Abstract

# Defining class
class Employee:# class Name
    pass

ee = Employee()# Object or instance of the class
print(ee)


"""

# instance method: whenever self keyword is there is called
class Employee:
    def display(self):
        """
        instance method
        :return: string
        """
        return "hey i am from display method"
    def display2(self):

        return "hey i am from display2 method"

# ee = Employee()# Object or instance of the class
# print(ee.display())
# print(ee.display2())

class University:
    def department(self,dep_name,dep_st):

        return f"hey i am from {dep_name} and strength is {dep_st} "
    def student(self,sdt_name,rl_n):

        return f"hey my name is {sdt_name} and roll number {rl_n}"
    def college(self,*args):
        return args

# uu = University()# Object or instance of the class
# print(uu.department("python",30))
# print(uu.student("reddy","12345"))
# print(uu.college(1,2,3,4,5))


# class Method:when argument is cls it is called as class method and
            # we have to represent by using @classmethod

class Caching:
    @classmethod
    def department(cls,dep_name,dep_st):

        return f"hey i am from {dep_name} and strength is {dep_st} "

    @classmethod
    def student(cls,sdt_name,rl_n):

        return f"hey my name is {sdt_name} and roll number {rl_n}"

    @classmethod
    def college(cls,*args):
        return args

# uu = Caching()# Object or instance of the class
# print(uu.department("python",30))
# print(uu.student("reddy","12345"))
# print(uu.college(1,2,3,4,5))

# static method: if you don't need cls or self arguments passing to
                # method you can using @staticmethod


class CachingStatic:
    @staticmethod
    def department(dep_name,dep_st):

        return f"hey i am from {dep_name} and strength is {dep_st} "

    @staticmethod
    def student(sdt_name,rl_n):

        return f"hey my name is {sdt_name} and roll number {rl_n}"

    @staticmethod
    def college(*args):
        return args

# uu = CachingStatic()# Object or instance of the class
# print(uu.department("python",30))
# print(uu.student("reddy","12345"))
# print(uu.college(1,2,3,4,5))

# initializer or constructor: whenever you defined or created object
                            # the first method internally calls to initializer
class KrPuram:
    def __init__(self):
        print("hey i am from constructor method")

# kk = KrPuram()

# variable defining in constructor
class Bangalore:
    def __init__(self,name,pincode):
        self.city_name = name
        self.pincode = pincode
        print(f"hey i am from {self.city_name} {self.pincode}")

# kk = Bangalore("krpuram","560036")

# usage of self variables
class Country:
    def __init__(self,name,pincode):
        self.city_name = name
        self.pincode = pincode
        # print(f"hey i am from {self.city_name} {self.pincode}")

    def display(self,arg):
        return self.city_name +self.pincode+ arg

# cc = Country("bangalore","560036")
#
# print(cc.display("green"))

# class level variables, how to call or usage class level variables

class Simple:
    x = 20
    def display(self,arg):
        return Simple.x+arg #use classname.variable name

# ss = Simple()
# print(ss.display(20))

# Destructure:if you want to delete Object, __del__ method by using del keyword
class Simple2:
    x = 20
    def display(self,arg):

        return Simple.x+arg #use classname.variable name
    def __del__(self):
        print("object deleted")

ss = Simple2()
print(ss.display(20))
del ss
print(ss.display(20))







