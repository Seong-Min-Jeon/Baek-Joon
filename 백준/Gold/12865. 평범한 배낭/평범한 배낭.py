import sys
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,k=f()
l=[list(f()) for _ in range(n)]
r=[0]*(k+1)
for i in range(n):
    w,v=l[i]
    for j in range(k,w-1,-1):
        r[j]=max(r[j],r[j-w]+v)
print(r[-1])