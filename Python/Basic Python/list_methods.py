numbers = [2,5,78,12,46,55]

# list er last ee new element add korte  { list.append(val) }
numbers.append(98)
print(numbers)

# kono index ee kono element add korte { list.insert(index, val) }
numbers.insert(1, 77)
print(numbers)

# kono element remove korte, { list.remove(val) }  # oi value thakle remove hobe nahole, error show korbe
# so be careful, check element ta ache kina

numbers.remove(78)
print(numbers)
      
#   last theke kono element delete korte list.pop()
numbers.pop()
print(numbers)

# puro array/list ekebare khali korte hole list.clear()
# numbers.clear()
# print(numbers)

# kono element ache kina, tahole tar index return korte,,, list.index(val)
idx = numbers.index(5)
print(idx)

# kono value kotobar ache count korte  list.count(val)
fre = numbers.count(99)
print(fre)

# array sort korte...  sort(*)
numbers.sort(*)
