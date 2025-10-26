# Dictionary in python:Dictionary are used to store data values in key:value pairs.
# They are unordered,mutable(changeable)& do not allow duplicates.
# it is working in the form of word and meaning is known as pairs.
# word is react in the form of key and meaninig is react in the form of value.
# you can store various data types.
data={
    "name":"jhon wick",
    "subjects":["c","c++","pyhon"],
    "class":"B.Sc(cs)",
    "reg no":27,
    "is adult":"True",
    "cgpa":9.9
}
print(data)
print(type(data))
data['name']="Azhan" # to change the value.
data["surname"]="asangani" # to add a new value.
print(data)

# Nested dictionary:To store the data in under the data store another data.
student={
    "name":"ibrahim",
    "subjects":{
        "maths":82,
        "physics":91,
        "chemistry":95.6
    }
}
print(student)
print(student["subjects"]) # to access all the subjects.
print(student["subjects"]["physics"]) # to access only physics.
print(student.keys()) # returns all keys.but it will not return nested keys.
print(list(student.keys()))  # returns keys in the form of list.
print(student.values()) # returns all values.
print(list(student.values())) # returns values in the form of list.
print(student.items()) # returns all(keys,values) pairs as tuple.
pairs=list(student.items())
print(pairs[0]) # returns first tuple.
print(student.get("name")) # returns keys according to the value.

# print(student["name2"]) # Error  if 1 line is error next line will not be executed.
print(student.get("name2")) # No error >> none
 
student.update({"country":"india"}) # inserts specified item to the dictionary.
print(student)
new_dict={"name":"Ronaldo"} # to change the dictionary name.
student.update(new_dict) # update the dictionary items.
print(student)

# set in python: set is a collection of the unordered items.
# Each element in set must be unique and immutable.
# set is mutable but set element is immutable.
collection={1,2,2,3,'sets',"world"} # duplicate values cannot be allowed in sets.
print(collection)
print(type(collection))
print(len(collection)) # total number of items.

collection=set() # Empty set ; syntax
print(type(collection))

# set methods:
# Hashable value is immutable but unhashable is mutable.
collection=set()
collection.add(1) # Adds an element.
collection.add(2)
collection.add(2)
collection.add("Iam a hero")
collection.add((1,2,3,4))
print(collection)
print(collection.remove(2)) # Remove the element.
print(collection)
collection.clear() # Empties the set.
print(len(collection)) 
collection={"hello","Azhan","king","pyhon","legend"} # Removes a random values.
print(collection.pop())

# set methods:
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))  # combines both set values & returns new value.

set1={1,2,3,4}
set2={4,3,6,7}
print(set1.intersection(set2))  # Combines common values & returns a new value.

# practice question(1): store following word meanings in a python dictionary:
data={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(data)

# practice question(2):you are given a list of subjects.Assume one classroom is required for 1 subject.
# how many classroom are needed by all students.
# "python","java","c++","Java","javascript","python","c++","java","c"

subject={"python","java","javascript","c++","c","java","c++"}
print(len(subject))

# practice question(3):WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# start with an empty dictionary & add one by one.use subject as key marka as value.
marks={}
x=int(input("Enter the mark of physics:"))
marks.update({"physics":x})

y=int(input("Enter the mark of chemistry:"))
marks.update({"chemistry":y})

z=int(input("Enter the mark of maths:"))
marks.update({"maths":z})
print(marks)

# practice question(4):figure out a way to store 9 & 9.0 as separate value in the set.
# (you can take help of build-in data types)
values={9,'9.0'}
print(values)
 
values={
    ("int",9),
    ("float",9.0)
}
print(values)

