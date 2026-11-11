n = int(input())
mx = -100000
mn = 100000
lst = list(map(int, input().split()))
for it in lst:
    mx = max(mx, it)
    mn = min(mn, it)

for num in lst :
    if num == mx:
        print(mn, end=" ")
    elif num == mn:
        print(mx, end=" ")

    else:
        print(num, end=" ")

