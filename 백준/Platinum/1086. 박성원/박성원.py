from collections import deque as D
import math
I=input
n=int(I())
l=[int(I()) for _ in range(n)]
k=int(I())
d=[[0]*k for _ in range(2**n)]
v=[[0]*k for _ in range(2**n)]
p=[pow(10,i,k) for i in range(51)]
h=[len(str(e)) for e in l]
q=D([])
for i,e in enumerate(l):
    d[2**i][e%k]=1
    q.append((2**i,e%k))
while q:
    a,b=q.popleft()
    for i in range(n):
        if(a&(1<<i)): continue
        x=a|(1<<i)
        y=(b*p[h[i]]+l[i])%k
        d[x][y]+=d[a][b]
        if(v[x][y]==0):
            q.append((x,y))
            v[x][y]=1
x,y=d[-1][0],math.perm(n)
g=math.gcd(x,y)
print(f'{x//g}/{y//g}')