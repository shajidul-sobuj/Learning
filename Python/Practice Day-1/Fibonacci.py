n = int(input())

arr = []
arr.append(0)
arr.append(1)
for it in range(2,n+1):
    num = arr[it-1]+arr[it-2]
    arr.append(num)

print(arr[n-1])
    
