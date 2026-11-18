n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if m > n:
    print("NO")
    exit()

it = 0
for x in a:
    if it < m and x == b[it]:
        it = it+1

if it == m:
    print("YES")
else:
    print("NO")