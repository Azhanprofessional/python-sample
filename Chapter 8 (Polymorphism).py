# Polymorphism: operator overloading
# When the same operator is allowed to have different meaning according to the context.
# Dunder functions : instead of using a+b for addition to use  a.__add__(b).

# implicit overloading
print(2+2)              
print("cristiano"+"ronaldo")  # concatenate 
print([1,2,3]+[4,5])          # merge      

# polymorphism
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i+",self.img,"j")

# Dunder function
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
num1=Complex(2,4)
num1.showNumber()

num2=Complex(6,3)
num2.showNumber()

num3=num1+num2
num3.showNumber()

# practice question(1):Define a circle class to create a circle with radius r using the constructor.
# Define an area() method of the class which calculates the area of the circle.
# Define a perimeter() method of the class which allow you to calculate the perimeter of the circle.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7)*self.radius**2   
     
    def perimeter(self):
        return 2*(22/7)*self.radius    
    
c1=Circle(21)
print(c1.area())
print(c1.perimeter())

# practice question(2):Define a employee class with attributes role, department & salary.
# this class also has a showDetail() method.
# create an engineer class that inherits properties from employee & has additional attributes:name & age.
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetail(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","70,000")

engg1=Engineer("Azhan",20)
engg1.showDetail()

# create a class called order which stores item & its price.
# use Dunder function __gt__() to convey that:
#      order1 > order2 if price of order1 > price of order2.
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        return self.price>order2.price
    
odr1=Order("lays",20)
odr2=Order("juice",10)

print(odr1>odr2)
