# OPPS in python:to map with real world scenarios,we started using object in code.
# this is called object oriented programming.
# class and object in python:class is a blueprint for creating objects.

# creating class
class Student:
    name="Azhan"

# creating object (instance)
S1=Student()
print(S1.name)

# class
class Car:
    colour="white"
    brand="Rolls royles"

# object
car1=Car()
print(car1.colour)
print(car1.brand)

# Constructor: __init__ function.
# All classes have a function call __init__(),which always executed when the object is initiated.
# The data store inside the class or object or variable is called attributes.
class Student:
    name="Zaid"

    # Default constructors
    def __init__ (self):
        print("My name is azhan...")

S1=Student()

# class
class Student:

    # parameterized constructors
    def __init__ (self,name,marks):  # constuctor(parameter)
        self.name=name
        self.marks=marks

# object
S1=Student("Anas",85)
print(S1.name,S1.marks)

S2=Student("Arman",95)
print(S2.name,S2.marks)

# Methods:methods are functions that belongs to objects.
# class is a collection of attributes and methods
class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def welcome(self):         # welcome is a methods
            print("welcome student",self.name)

    def student_marks(self):   # student_marks is a methods
        return self.marks

s1=Student("Azhan",100)
s1.welcome()
print(s1.student_marks())

# practice question(1):create student class that takes name & marks of three subjects as arguments un constructor.
# Then create a method to print the average.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

# static methods:methods that don't use parameter(work at class level)
    @staticmethod         # (decorator) which is changing the behaviour of my normal function.
    def hello():
        print("hello")
    
    def get_avg(self):       # get_avg is a methods
        sum=0
        for val in self.marks:
            sum+=val
        print("hello",self.name,"your avg score is:",sum/2)

s1=Student("Anas",[88,95,90])
s1.get_avg()

s1.name="shayaan"  # also direcly change your name.
s1.get_avg()

s1.hello( )      # static

# Abstraction:hiding implemention details of a class and only showing the essential features to the user.
class Car:
    def __init__ (self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True            # hiding the details in output.
        self.acc=True               # hiding the details in output.
        print("car started...")

car1=Car()
car1.start()  

# Practice question(1):

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited ")
        print("Total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited ")
        print("Total balance=",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(20000,12345)
acc1.debit(1000)
acc1.credit(10000)


    


        




