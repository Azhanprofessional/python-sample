# list in python:A build-in data type that stores set of values.& enclosed within square bracket[].
# list is mutable.
# it can store elements of different data types(integer,float,string,..etc)
student=['arun',78,'delhi',99,66.5]
print(student)
print(type(student))
print(student[0])
print(student[1])
student[0]='zaid'
print(student)
print(len(student))

# list slicing.ending index cannot be included.
marks=[34,56,78,90]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-4:-1]) #negative index

# list method:
list=[1,2,3]
list.append(4) # to add a element in a list
print(list)

list=[4,3,5,6]
list.sort() # sort the element in accending order.
print(list) 
list.sort(reverse=True) # sort the element in descending order.
print(list)
list[0]=3  # list can be changed.

my_list=['apple', 'banana', 'cherry'] 
my_list.insert(1,'orange') # insert an element at a specific position
print(my_list)
my_list.reverse() # reverse the order of elements in the list
print(my_list)
my_list.remove('banana') # remove an element from the list
print(my_list)
my_list.pop(0) # remove the index element from the list.
print(my_list)

# tuple in python:A build-in data type that as create immutable sequence of value.
# Enclosed within parenthesis separated with commas.
tup=() # having parenthesis
print(type(tup))

tup=(1,2,3,4)
print(tup)
print(tup[0])
print(tup[2])
print(tup[1:4]) #tuple slicing.

# Tuple methods.
tup=(2,3,4,5,6)
print(tup)
print(tup.index(3)) # searching the element.
print(tup.count(4)) # it counts the same number.how many times the come.

# practice question(1):user to enter the names of their 3 favorite movies & store them in a list.
movies=[]  # Empty list
mov1=input("Enter the first movie:")
mov2=input("Enter the second movie:")
mov3=input("Enter the third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
  
# practice question(2):check if a list contain palindrome of elements.(Hint:use copy() method).
# palindrome is a first and last same number of element as order shown.
# Eg: [racecar]  [1,2,3,2,1]  [1,"abc,"abc",1]
list1=["racecar"] # first and last number of element must be same.
list2=["carrace"] # not same element.

copy_list1=list1.copy() # copy the list1 element.
copy_list1.reverse() # reverse the copy_list1 element.

if(copy_list1==list1): # returns palindrome if list1 equals to copy_list1 elements. 
    print("palindrome")
else:
    print("Not palindrome")
 
# practice question(3):count the no.of student with "A" grade in the following tuple.
grade=("C","D","A","B","A","B","A")
print(grade.count("A"))

# practice question(4):store the above value in a list & sort them from "A"to"D.
my_list=["C","D","A","B","A","B","A"]
my_list.sort()
print(my_list)