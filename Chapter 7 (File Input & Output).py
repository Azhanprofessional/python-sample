# File I/O :python can be used to perform different operations on a file.(read & write data)
# types of all files.
# 1.Text files:.txt,.docx,.log etc.
# 2.Binary files:.mp4,.mov,.png,.jpeg etc.

# to read a file.
f=open("demo.txt","r")

data=f.read()
print(data)
f.close()

# to write a file.
f=open("demo.txt","w")
f.write("i want to learn python")
f.close()

# # add a new file.
f=open("sample.txt","a")
f.close()

# to read and overwrite.(pointer start)-no truncate.(file is not delete)
f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

# to read and overwrite-truncate.(file is delete)
f=open("demo.txt","w+")
print(f.read())
f.close()

# to read and append.(pointer end)-no truncate (file is not delete)
f=open("demo.txt","a+")
print(f.read())
f.close()

# with syntax().the with syntax automatically close a file.
with open("demo.txt","r") as f:
    data=f.read()
    print(data)  

# deleting a file using os modele.
# module (like a code library) is a file written by another programmer that generally has a functions we can use.
# import os
# os.remove("demo.txt")



    
    