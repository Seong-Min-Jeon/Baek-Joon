import sys
from collections import deque
I=sys.stdin.readline
n,m=int(I()),int(I())
q=deque([])
s=set([i+1 for i in range(n)])
for _ in range(m):
    x,y,k=map(int,I().split())
    q.append((x,y,k))
    if(x in s): s.remove(x)
l=[[0]*(n+1) for _ in range(n+1)]
for e in s:
    l[e][e]=1
while q:
    x,y,k=q.popleft()
    f=0
    for i in range(len(q)):
        a,b,c=q[i]
        if(y==a): f=1; q.append((x,y,k)); break
    if(f): continue
    for i in range(n+1):
        l[x][i]+=l[y][i]*k
for e in s:
    if(l[-1][e]!=0): print(e,l[-1][e])