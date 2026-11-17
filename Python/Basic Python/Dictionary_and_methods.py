"""
    # Dictionary in Python
        --> A dictionary in Python is a built-in data type that stores data in key-value pairs.

    --> Each key is unique and is used to access its corresponding value.
    --> Dictionaries are written using curly braces {}.

"""

# Creating a Dictionary
student = {
    'name' : "sobuj",
    "age" : 20,
    'id' : 212,
    'department' : "CSE"
}
print(student)

# Accessing Dictionary Elements / values using their keys.
print(student["name"])
print(student['department'])
print(student.get('name'))      # can also use the get() method.


##### Dictionary Methods in Python
#     --> Here are the most important dictionary methods.
# 1. get()       # --> Returns the value of a specified key.
print(student.get('name'))
# 2. keys()     -->  Returns all keys in a dictionary.
print(student.keys())

# 3. values()       -->  Returns all values in a dictionary.
print(student.values())

# 4. items()        -->  Returns all key-value pairs as tuples.
print(student.items())

# 5. update()        -->  Adds new key-value pairs or updates existing values.
student.update({"age":21})
student.update({"address":"Savar"})
print(student)

# 6. pop()        -->  Removes a specified key and returns its value.
student.pop("address")
print(student)


# 7. popitem()        -->  Removes and returns the last inserted key-value pair.

student.popitem()
print(student)

# 8. clear()        -->  Removes all elements from a dictionary.

student.clear()
print(student)

#### Other Important Dictionary Operations

# Adding a new element:
student = {"name":'sobuj'}
student["age"] = 20
print(student)
# Changing a value:
student['age'] = 21
print(student)

# Checking whether a key exists:
if 'name' in student:
    print('exist')
else:
    print("NO")

# Looping through a dictionary:
for key,val in student.items():
    print(key,":", val)
