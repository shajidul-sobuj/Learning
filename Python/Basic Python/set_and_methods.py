"""
    # What is a Set in Python?
        -> A set is a built-in data type in Python used to store multiple unique values in a single variable.

    # A set has the following characteristics:
        --> Unordered: Items do not have a fixed position.
        --> Mutable: You can add or remove elements.
        --> No duplicates: A set automatically removes duplicate values.
        --> Unindexed: You cannot access elements using index numbers.
        --> Multiple data types: A set can contain integers, strings, floats, etc.

"""


# Example of a Set

numbers = {10, 20, 10, 30, 20}
print(numbers)

# #  Set with Different Data Types
# my_set = {10, "Hello", 3.5, True}
# print(my_set)

# # Empty Set
# a = set()
# print(a)
# print(type(a))





# add()
#   --> Adds one element to a set.
numbers.add(40)
print(numbers)


# update()
#   -->  Adds multiple elements from another iterable to a set.
numbers.update([40, 50, 60])
print(numbers)


#  remove()
#   --> Removes a specified element from a set.
#   --> If the element does not exist, it raises a KeyError.

numbers.remove(20)
print(numbers)


# discard()
#   --> Removes a specified element from a set.
#   --> If the element does not exist, it does not raise an error.
numbers.discard(50)
print(numbers)

# pop()
#   --> Removes and returns an arbitrary element from a set.
x = numbers.pop()
print(x)
print(numbers)

# clear()
#   --> Removes all elements from a set.
numbers.clear()
print(numbers)



# union()
#     --> eturns all unique elements from two sets.
#     --> It can also be performed using the | operator.

A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))  
print(A | B)    # 2 vabei likha jay


# intersection()
#   --> Returns only the common elements between two sets.
#   --> It can also be performed using the & operator.
A = {1, 2, 3}
B = {3, 4, 5}
print(A.intersection(B))
print(A & B)    # 2 vabei likha jay

# difference()
#   --> Returns elements that exist in the first set but not in the second set.
#   --> It can also be performed using the - operator.

A = {1, 2, 3}
B = {3, 4, 5}
print(A.difference(B))
print(A-B)      # 2 vabei likha jay

# symmetric_difference()
#   -->> Returns elements that are in either set, but not in both sets.
#   --> It can also be performed using the ^ operator.
A = {1, 2, 3}
B = {3, 4, 5}

print(A.symmetric_difference(B))
print(A^B)


# isdisjoint()
#   --> Checks whether two sets have no common elements
A = {1, 2, 63, 6}
B = {4, 5, 8, 9}
print(A.isdisjoint(B))

# issubset()
#   --> Checks whether one set is a subset of another
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

# issuperset()
#   --> Checks whether one set is a superset of another
A = {1, 2, 3, 4, 5}
B = {1, 2}
print(A.issuperset(B))