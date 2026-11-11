t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    sum = 100000000
    for i in range(0,n-1):
        for j in range(i+1, n):
            sum = min(sum, a[i]+a[j]+j-i)
    print(sum)
    t -= 1

    