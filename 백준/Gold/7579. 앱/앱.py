I=input; F=lambda:map(int,input().split())
n,m=F()
a,b=[*F()],[*F()]
l=[0]*10001
for i in range(n):
    for j in range(10000,b[i]-1,-1):
        l[j]=max(l[j],l[j-b[i]]+a[i])
for i in range(10001):
    if(l[i]>=m): print(i); break