n = int(input())
a = list(map(int, input().split()))

mx = -1000000
mn = 1000000
for x in a:
    if mx < x:
        mx = x
    if mn > x:
        mn = x

for x in a:
    if x == mn:
        print(mx, end=' ')
    elif x == mx:
        print(mn, end=' ')
    else:
        print(x, end=' ')