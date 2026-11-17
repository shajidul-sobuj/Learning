n = int(input())
a = list(map(int, input().split()))

neg = -1
for i in a[::]:
    if i != a[neg]:
        print("NO")
        exit()
    neg = neg-1
    
print("YES")