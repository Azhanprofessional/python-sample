# String: is a data type that stores sequence of characters.
# strings are immutable(cannot be changed).
# Example.
str="iam mohammed azhan"
print(str)

# concatenation: +adding two string.
str1="hello"
str2="world"
str=str1+str2
print(str)

#length of string:calculate a string using len().length number start from 1.
str1="college"
len1=len(str1)
print(len1)

str2="name"
length= str1 +" "+ str2 #its adding space also. 
print(len(length))
 
# indexing: is a position number.
# in python string number start from 0 insted of 1.
# index number access using square bracket[].
str="Hello azhan"
a=str[1]
print(a)

# slicing: accessing parts of a string.
# ending index cannot be included.
str="your name"
print(str[5:]) 

# Negative index: In python we also count backward
# Backward string start from -1 end of string & decreasing the value.
str="mango"
print(str[-5:-1]) 

# string function(): there are verious string functions in python.
str="iam from vaniyambadi" # returns true if string endswith "di" else return false.
print(str.endswith("di"))
 
str="iam from vaniyambadi"
print(str.capitalize()) # the first letter i will be capitalize I.

str="education is the most powerful"
print(str.replace("most","must")) # replace old to new word.

str="knowledge is free"
print(str.find("free")) # it is find index number.

str="it is better to learn"
print(str.count("e")) # it will count the same letter or word that how many times exsist.

# practice question:input the users first name & print its length.
name=input("Enter the name:")
print("length of my name is",len(name)) 

# conditional statement:(if,elif,else and nested-if)
m=40
if m==80:  # if condition always check conditions.
    print("first class")
elif m==40:  # elif condition check when if condition returns false.
    print("second class")
elif m==90:
    print("distintion") 
else:       # if all condition is false else statement will be execute.
    print("third class")

#nested-if: returns if statement in under the if statement. 
age=18
if age>=18:
    if age>=80:
        print("connot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#pratice question(1): grade student based on marks.
m=int(input("Enter the mark of student:")) 
if m>=90:
    print("grade A")
elif (m>=80 and m<90):
    print("grade B")
elif (m>=70 and m<80):
    print("grade C")
elif (m<70):
    print("grade D")

#pratice question(2): check if a number entered is a even or odd.
num=int(input("Enter the number:"))
if num%2==0:
    print("Even number")
else:
    print("Add number")

#pratice question(3): find the greatest of 3 number.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    print("first is greatest",a)
if b>=c:
    print("second is greatest",b)
else:
    print("third is largest",c)

#pratice question(4):check if the number is multiple by 7 or not.
num=int(input("Enter the number:"))
if num%7==0:
    print("multiple by 7")
else:
    print("not multiple by 7")

