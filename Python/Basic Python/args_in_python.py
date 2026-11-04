"""
def sum(*number):
    print(number)
    sm = 0
    for dig in number:
        sm+=dig
    return sm

ans = sum(1,2,3,5,6,4)
print(ans)

"""





def sum(num1, num2, *args):
    total = 0
    for dig in args:
        total += dig

    return total
total = sum(1,2,2,5,4,6,4,5)
print(total)