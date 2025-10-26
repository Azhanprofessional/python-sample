# practice question(1):create a new file "practice.txt" using python.add a data in it.
with open("practice.txt","w") as f:
    f.write("hello  everyone\n we are learning file I/o \n")
    f.write("using python \n i like programming in python\n")

# practice question(2):To replace all accurances of 'java' with 'pyhon' in above file.
    with open("practice.txt","r") as f:
        data=f.read()

    new_data=data.replace("pyhon","java")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)

# practice question(3):WAF to search if the word "learning" exists in the file or not.
def check_word():
    word="learning"
    with open("practice.txt","r")as f:
        data=f.read()
        if(data.find(word) !=-1):
            print("found")
        else:
            print("not found") 

check_word()

# practice question(4):WAF to find in which line of the file does the "learning" occur first.
def check_line_number():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
                return  
            line_no+=1

    return -1
check_line_number()

# practice question(5):from a file containing number separated by comma,print the count of even numbers.
count=0
with open("practice2.txt","r") as f:
    data=f.read()
    
    nums=data.split(",")
    for val in nums:
        if (int(val) % 2 ==0):
            count+=1

print(count)






