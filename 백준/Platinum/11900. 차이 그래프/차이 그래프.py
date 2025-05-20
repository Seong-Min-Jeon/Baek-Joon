import heapq
import sys
I=sys.stdin.readline
n=int(I())
a=list(map(int,I().split()))
q=[(0,0)]
r=[1e9]*n
r[0]=0
while q:
    c,u=heapq.heappop(q)
    if(r[u]<c): continue
    for v in range(n):
        if(u>v and a[u-v-1]>0):
            t=a[u-v-1]
            if(r[v]>c+t): r[v]=c+t; heapq.heappush(q,(c+t,v))
        if(u<v and a[u-v+n-1]>0):
            t=a[u-v+n-1]
            if(r[v]>c+t): r[v]=c+t; heapq.heappush(q,(c+t,v))
for _ in range(int(I())):
    x,y=map(int,I().split())
    x,y=x-x,y-x
    if(y<0): y+=n
    if(r[y]==1e9): print(-1)
    else: print(r[y])