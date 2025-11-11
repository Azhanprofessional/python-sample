# Function:is a block of code that perform a specific task.
# if we written same line of code 2 or more times. you should convert into funtion.
# It takes some parameter input and returns the output.
# Function is used to decrease the number of lines and Redundantcy(repeat) also decrease.
def calc_sum(a,b):   # (parameter a,parameter b)
    sum=a+b
    print(sum)
    return sum

calc_sum(5,10)    # Function call
calc_sum(2,3)     # Function call
calc_sum(10,20)   # Function call  

def calc_sum(a,b):    # this two lines are said to be function definition.
    return a+b

sum=calc_sum(200,500) # calc_sum is said to be function call & (argument 200,argument 500)
print(sum)

# No parameter input and no return output functions.
def print_hello():
    print("hello")

print_hello()
print_hello()

# To print the average of 3 numbers.
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)    
    
calc_avg(20,35,45)

# default argument:asigning a default value to parameter,which is used when no argument is passed.
def calc_product(a=2,b=2):   # default value
    print(a*b)

calc_product()   # no argument

def calc_product(a,b=2):   # default value
    print(a*b)

calc_product(3)  

# practice question(1): WAF To print the length of a list.(list is the parameter)
countries=["india","china","bangladesh","pakistan"]
fruites=["apple","mango","banana","watermilon","popayas"]

def print_len(list):
    print(len(list))

print_len(countries)
print_len(fruites)

# practice question(2):WAF to print the element of a list in a single line.(list is the parameter)
def print_list(list):
    for item in list:
        print(item,end=" ") 

print_list(countries)

# practice question(3):WAF to print the factorial of n.(n is the parameter)
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

calc_fact(5)

# practice question(4):WAF to convert USD to INR.
def converter(usd_value):
    inr_value=usd_value*84
    print(usd_value,"USD=",inr_value,"INR")

converter(2)

# To print odd or even number using function.
def odd_even(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

odd_even(4)

# Recursive function: A function calls itself repeatedly.
def show(n):
    if (n==0):  # base case:
        return
    print(n)
    show(n-1)

show(5)

# practice question(1):write a recursive funtion to calculate the sum of first n natural number.
def calc_sum(n):
    if (n==0):
        return 0
    return calc_sum(n-1)+n

sum=calc_sum(10)
print(sum)

# practice question(2):write a recursive funtion to print all the element in a list.
# hint:use list & index as parameters.

def print_list(list,idx=0):
    if(idx==len(list)):     # base case
        return
    print(list[idx])
    print_list(list,idx+1)

bike=["Hunter","passion","splender","unicorn"]    
    
print_list(bike)

