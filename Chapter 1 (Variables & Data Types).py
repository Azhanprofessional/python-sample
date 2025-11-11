# variable: is a name given to a memory location in a program.
# constant: a fixed value that can't be changed.
name="azhan"
age=20
percent=98.12
a=True
b=None
print(name)
print(age)
print(percent)
age=25
print(age)
print(type(name))
print(type(age))
print(type(percent))
print(type(a))
print(type(b))

# comment shortcut key:ctrl+/
# Escape sequence:\n to print a next line.
# \t Tab space.

# Arithmatic operators
# + is a operator,a b is a operands
a=5
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b) #remainnder value

# Relational operators
a=5
b=3
print(a!=b)
print(a==b)
print(a>=b)
print(a>b)
print(a<b)
print(a<=b)

#Assignment operators
num=5 
num*=2
print("num:",num)

# logical operators(And,Or,Not)
# not operator returns opposite
print(not False)
print(not True)


# And operator if val1 and val2 are true returns true else return false 
val1=False
val2=True
print("and operator:",val1 and val2)

# or operator returns true if one value is true else return false
print("or operator:",val1 or val2)
a=20
b=10
print("or operator:",(a==b) or (a>b))

# type conversion:(automatically)
a=5   # variable a is automatically converted to b into float
b=2.5
print(a+b)

# type casting:(manual)
# string value converted to integer
a=int("3")
b=7.5
print(type(a))
print(a+b)

# input in python:
name=input("What is your name:")
print("my name is",name)

a=input("enter the value:") # result for input() value is alaways a string 
print(type(a),a)

# taking input from user:
int("6")
a=int(input("enter the value: ")) 
print(type(a),a)

# Example:
name=input("Enter the name:")
age=input("Enter the age:")
marks=float(input("Enter the marks:"))

print("welcome:",name)
print("age:",age)
print("marks:",marks)
 
#practice question(1):
#sum of two number.
a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
print("sum=",a+b)

#practice question(2):
#input side of a square and print its area.
side=float(input("Enter the value:"))
print("area=",side*side)# multiple by side by side.

#practice question(3):
#input the two floating point number & print its average.
a=float(input("enter the first no:"))
b=float(input("enter the second no:"))
print("Avg=",a+b/2)
 
#practice question(4):
#input the two integer no,a & b.
a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
print(a>=b) #print true if a is >= to b else print false.