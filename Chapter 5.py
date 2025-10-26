# Loops in python: loops are used to repeat instructions.
# variable count=1 is said to be iterators.Running the loops is said to be iteration.
# infinite loops are very dangeres . it holds the execution of a program.do not used at all.
# while loops.
count=1
while count<=5:
    print("hello")
    count+=1
    print(count)  

i=1    
while i<=1000:
    print('hello',i)
    i+=1

# practice questions(1): print the nembers from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1 
print('loop ended')

# practice questions(2):print the number from 100 to 1.
i=100
while i>=1: #stopping condition.
    print(i)
    i-=1

# practice questions(3):print the multiplication table of a number n.
n=int(input("Enter the number:"))
i=1
while i<=12:
    print(n*i)
    i+=1

# practice question(4):print the element of the following list using a loop.
num=[1,4,9,16,25,36,49,64,81,100]

# traverse(travel the element 1 by 1)
index=0
while index<len(num): 
    print(num[index]) 
    index+=1

# practice question(5):search for a number x in this tuple. 
num=(1,4,9,16,25,36,49,64,81,100)

x=49
i=0  # initialization
while i<len(num):
    if(num[i]==x):
        print("Found at idx",i)
    i+=1

# Break and continue statement:Break is used to terminate the loop when uncountered.
# continue is used to terminates the execution in the current iteration & continues execution of the loop with the next iteration.

# break:
i=0
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

num=(1,4,9,16,25,36,49,64,81,100)

x=49
i=0  # initialization

while i<len(num):
    if(num[i]==x):
        print("Found at idx",i)
        break
    else:
        print("finding...")
    i+=1

print("end of the loop")

# continue:
i=0
while i<=5:
    if(i==3):
        i+=1
        continue # skip
    print(i)
    i+=1

# To print odd or even number.
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue # skip
    print(i)
    i+=1

# for loops:are used for sequential traversal.For traversing list,string,tuples etc.
heros=["SRK","vijay","allu arjun","yash"]

for val in heros:
    print(val)

str="Mohammed azhan"
for char in str:
    print(char)
else:
    print('END')

# practice question(1):using for loop print the element of the following list using a loop.
nums=[2,6,7,10,15,20,26,50,80,100,120]

for el in nums:
    print(el)

# practice question(2):search for a number x in this tuple using loop.
# it is also called linear search.
nums=[2,6,7,10,15,20,26,50,80,100,120,50]
x=50

idx=0
for el in nums:
    if(el==x):
        print("Number found at idx",idx)
    idx+=1

# Range():range function returns a sequence of numbers,starting from 0 by default,and increaments by 1 (by default),
# And stops before a specified number.
print(range(5))
seq=range(10)

for i in range(10):  #range(stop)
    print(i)

for i in range(2,10): # range(start,stop)
     print(i)

for i in range(2,10,2): # range(start,stop,step)
     print(i)

# To print odd or even number.
for i in range(2,100,2):
     print(i)

# practice question(1):To print numbers from 1 to 100.
for i in range(1,101):
     print(i)

# practice question(2):To print numbers from 100 to 1.
for i in range(100,0,-1):
     print(i)

# practice question(3):print the multiplication table of a number n.
n=int(input("Enter the number:"))

for i in range(1,11):
    print(n*i)

# Pass statement:pass is a null statement that does nothing.it is used as a placeholder for future code.
for i in range(5):
    pass

print("i have some work")

# practice question(1):To find the sum of first n natural numbers.(using while loop)
n=5

sum=0
i=1
while i<=n:
    sum+=i
    i+=1

print("Total sum =",sum)

# practice question(2):To find the factorial of first n natural numbers.(using for loop)
n=5

fact=1
i=1
while i<=n:
    fact*=i
    i+=1

print("Factorial =",fact)

# using for loop:
n=3
fact=1

for i in range(1,n+1):
    fact*=i

print("Factorial =",fact)

