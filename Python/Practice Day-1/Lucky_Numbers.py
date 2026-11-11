# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/M

a , b = map(int, input().split())

def luky(n):
    s = str(n)
    for char in s:
        if(char != '4' and char != '7'):
            return False
    return True

numbers = []
for num in range(a,b+1):
    if (luky(num)) :
        numbers.append(num)

if(len(numbers) == 0): 
    print("-1")

else :
    for num in numbers:
        print(num, end = " ")

