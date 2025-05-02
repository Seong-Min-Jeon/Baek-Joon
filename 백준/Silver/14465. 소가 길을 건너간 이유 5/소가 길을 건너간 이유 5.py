import sys
I=sys.stdin.readline
n,k,b=map(int,I().split())
l=[0]*100001
for _ in range(b): l[int(I())]=1
m=sum(l[1:k+1])
c=m
for i in range(1,n-k+1):
    c-=l[i]; c+=l[i+k]
    m=min(m,c)
print(m)