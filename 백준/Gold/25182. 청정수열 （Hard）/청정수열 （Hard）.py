n=int(input())
M=10**9+7
a=0
s=0
for i in range(1,n+1):
    s=(s+i*2)%M
    a=(a+s*i)%M
b=1
for i in range(1,n+1):
    b=(b*i)%M
b=(b**2)%M
print(a,b)