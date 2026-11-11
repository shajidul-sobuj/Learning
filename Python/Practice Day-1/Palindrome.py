# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I
# solve of CF this ptoblem using Python...

s = input()
zro = True
t = ''
length = len(s)
length = length*-1
for it in s[::-1]:
    if(it != '0'):
        zro = False
    if it == '0' and zro == True:
        it = it
    else :
        t += it

print(t)
if s == t :
    print("YES\n")
else :
    print("NO\n")    
    





