import math
n=int(input())
if(math.isqrt(n)**2==n): print(-1); exit()
s=set()
c=0
for i in range(1,math.isqrt(n)+1):
    if(math.isqrt(n-i**2)**2==n-i**2 and i not in s):
        s.add(math.isqrt(n-i**2))
        c+=1
for i in range(1,math.isqrt(n)+1):
    if(n%i==0):
        j=n//i
        if((i+j)%2==0): c+=1
print(c)