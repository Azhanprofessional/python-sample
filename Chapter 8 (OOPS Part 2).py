# # Private (like) attributes and methods:
# # private attributes and methods are meant to be used only within the class..
# # And are not accessible from outside the class.
# # For private use two (__)underscore infront of __attributes and __methods.
# class Account:
#     def __init__ (self,acc_no,acc_password):
#         self.acc_no=acc_no
#         self.acc_password=acc_password

#     def reset_password(self):
#         return self.__acc_password      # private 

# acc1=Account(2454334,"AdFhkf")
# print(acc1.acc_no)
# print(acc1.acc_password)

# # Eg: 2
# class Member:
#     __name="sayeed"

#     def __hello(self):
#         print("Hi member")

#     def welcome(self):
#         self.__hello()

# p=Member()
# print(p.welcome())

# # inheritance:wehen one class derives the properties & methods of another class.
# class Car:
#     colour="Black"

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Car_name(Car):
#     def __init__ (self,name):
#         self.name=name

# car1=Car_name("Lamborgini")

# print(car1.name)
# print(car1.colour)


# # single inheritance

# # parent class
# class Fruites:
#     def apple(self):
#         print("apple is good for health")

# # child class (inherits from fruites)
# class vegetable(Fruites):
#     def carrot(self):
#         print("carrot is also good for health")

# b=vegetable()
# b.apple()        # inherited method
# b.carrot()       # child own method

# print("the class is end")

# # Multiple inheritence

# # parent class 1
# class Father:
#     def show_father(self):
#         print("this is father class")

# # parent class 2 
# class Mother:
#     def show_mother(self):
#         print("this is mother class")

# # child class (inherits from both father & mother class)
# class Child(Father,Mother):
#     def show_child(self):
#         print("this is child class")

# c=Child()
# c.show_father()         # inherits from father
# c.show_mother()         # inherits from mother
# c.show_child()          # own method

# print("the class is end")

# # multi_level inheritance

# # Base class
# class physics:
#     def show_physics(self):
#         print("this is physics hour")

# # Derived class from physics
# class chemistry(physics):
#     def show_chemistry(self):
#         print("this is chemistry hour")

# # Derived class from chemistry
# class computer(chemistry):
#     def show_computer(self):
#         print("this is computer hour")

# c=computer()
# c.show_physics()        # inherited from physics
# c.show_chemistry()      # inherited from chemistry
# c.show_computer()       # own method

# Super method: is used to access method of the parent class.

# parent class
class Bike:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("bike has started")

    @staticmethod
    def stop():
        print("bike has stopped")

# child class
class Honda(Bike):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)     # using super() method inherits from class Bike. 

car1=Honda("shine","petrol")
print(car1.name)
print(car1.type)

# class method:A class method is bound to the class & receives the class as an implicit first argument.
# non-static method can't access or modify class state & generally for utility.

# parent class
class Student:
    name="ronaldo"

# child class
    @classmethod                 # decoreder
    def changename(cls,name):    # using classmethod directly change the name of parent class.
        cls.name=name

p1=Student()
p1.changename("Dhoni")
print(p1.name)
print(Student.name)

# property:we use @property decorator on any method in the class to use method as a property.

class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem

    @property
    def percentage(self):
        return str((self.math+self.phy+self.chem)/3) + "%"
    
stu1=Student(88,97,60)
print(stu1.percentage)

stu1.chem=90
print(stu1.percentage)


