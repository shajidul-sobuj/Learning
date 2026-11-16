# same as list 
# --> list mutable but tuple immutable
# --> list: [],, tuple: (), ste: {}
# echarao list er almost onek methods ei kaj kora jay





# tup = ('pen', 'blue', 'red')
# print(type(tup))
# print(tup)

# tup = ('sobuj', 212)
# print(tup)
# print(type(tup[0]), type(tup[1]))


items = ('pen', 221, 'red')
print(len(items))
print(items[0:])

for item in items:
    print("item -> ", item)


if 221 in items:
    print("exist in item")
else:
    print("not found")