a,b = map(int, input().split())
s = input()

# print(a,b,s)
ck = True

for i in range(0, (a+b+1)):
    if(i == a):
        if not (s[i] == '-'):
            ck = False
    elif not ('0' <= s[i] <= '9'):
        ck = False

if(ck):
    print("Yes")
else :
    print("No")
