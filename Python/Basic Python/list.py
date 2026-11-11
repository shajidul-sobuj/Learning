# Python ee list, array, collection same jinis (short turm ee arki)

# numbers nam ee list declear kori
numbers = [2,5,8,6,9,4,55,23,36,66]
# python ee right side diye, negative indexing hoy, like -1, -2, -3.....
print(numbers[3], numbers[-3])   # 6 and 23 print korbe
# list [ start : end]  $ start index theke shuru kore tobe end er ag porjonto jay
print(numbers[1:6])

# 2 2 kore baraite chaile  # list[ start " end : step"]
print(numbers[1:6:1])
print(numbers[1:6:2])
# reverse le jaoyar jonno
print(numbers[-2:-7:-1])
print(numbers[::-1]) # puro list take reverse kore dey