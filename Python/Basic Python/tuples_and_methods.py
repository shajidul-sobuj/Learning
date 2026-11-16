# same as list 
# --> list mutable but tuple immutable
# 
# echarao list er almost onek methods ei kaj kora jay


"""
What is a Tuple in Python?
    A tuple is a built-in data type in Python that is used to store multiple values in a single variable.

--> A tuple has the following characteristics:
        --> Ordered: Items maintain their insertion order.
        --> Immutable: You cannot change, add, or remove items after creating a tuple.
        --> Allows duplicates: A tuple can contain duplicate values.
        --> Multiple data types: It can store integers, strings, floats, etc.
        --> list: [],, tuple: (), ste: {}

"""



# tup = ('pen', 'blue', 'red')
# print(type(tup))
# print(tup)

# tup = ('sobuj', 212)
# print(tup)
# print(type(tup[0]), type(tup[1]))


items = ('pen', 221, 'red')
items = items + ('black',)           # append kora jayna but tupel jora lagnao jay, so eivabe chaile add kora jete pare
print(len(items))
print(items[0:])

for item in items:
    print("item -> ", item)


if 221 in items:
    print("exist in item")
else:
    print("not found")

# print("Accessing Tuple Elements: ")
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[2])
print(numbers[-1])