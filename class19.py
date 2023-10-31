"""
OOPS:

1) Inheritance
    i) single inheritance: single parent class to child class.
                    Ex: parent and child
    ii) multi level inheritance:one parent class to other child class from that to another child class
                    Ex: grand_father+ father = child
    iii) multiple inheritance:two parent classes methods we can inherit to child class
                    Ex:father+mother = child
    iv) hierarchical inheritance: we can inherit single base class to many child classes

2) polymorphism:this is called a method overriding or method overloading
3) Encapsulation: means data hiding or protecting or data binding
    -- public: you can access anywhere
    -- protected: you can access outside of the function but specifuc respective of the object using underscore (_)
    -- private: you are not able access private methods are variable outside of the function
                : if you want access you have to provide
                # object._classname__privatemethod()

4) abstract method: From Abc import abstractmethod and ABC
                    # @abstractmethod
                    # abstract means hiding
"""
# Inheritance:
# single inheritance: single parent class to child class
class Father:
    def display(self):
        return "hey i am from father class method"

class Child(Father):
    def display2(self,*args):
        return args

# cc = Child()
# print(cc.display2(1,2,3,4,5))
# print(cc.display())

# multi level inheritance: one parent class to other child class from that to another child class
class University:
    def uni_display(self):
        return "hey i am from university class method"
class Department(University):
    def display(self):
        return "hey i am from department class method"

class Student(Department):
    def display2(self,*args):
        return "hey i am from student class method"


# ss = Student()
# print(ss.uni_display())
# print(ss.display())
# print(ss.display2())

# Multiple inheritance: two parent classes methods we can inherit to child class
# ex: father+mother = chile
class FatherM:
    def display(self):
        return "hey i am from parent father class"

class Mother:
    def display2(self):
        return "hey i am from mother class"

class Childd(Father,Mother):# MRO: method resolution order
    def display3(self):
        return "hey i am from child class"


# ccc = Childd()
# print(ccc.display2())
# print(ccc.display3())
# print(ccc.display())


# hierarchical inheritance: we can inherit single base class to many child classes
class Base:
    def display(self):
        return "i am base classs"


class Child1(Base):
    def display1(self):
        return "i am base classs"


class Child2(Base):
    def display2(self):
        return "i am base classs"


# polymorphism: this is called a method overriding or method overloading

# method overriding
class Employer:
    def display(self):
        print('hey i am from employer display method')

class Employee(Employer):
    def display(self):
        print('hey i am from employee display method')

# ee = Employee()
# ee.display()

# methods calling from child classes
class University:
    def uni_display(self):
        return "hey i am from university class method"
class Department(University):
    def display(self):
        return "hey i am from department class method"
class Student(Department):
    def display2(self):
        print(Department.display(self))
        print(University.uni_display(self))
        return "hey i am from student class method"

# ss = Student()
# print(ss.display2())
"""
3) Encapsulation: means data hiding or protecting or data binding
    -- public: you can access anywhere
    -- protected: you can access outside of the function but specifuc respective of the object using underscore (_)
    -- private: you are not able access private methods are variable outside of the function
                : if you want access you have to provide 
                # object._classname__privatemethod()
    """
x = 10 # public
_xy = 10 # protected
__xyz = 10 # private

class Country:
    def display(self):# public
        return "hey i am from display public"
    def _display2(self):# protected
        return "hey i am from display2 public"
    def __display3(self):# private
        return "hey i am from display3 public"
cc = Country()
print(cc.display())
print(cc._display2())
print(cc._Country__display3())# access private method

