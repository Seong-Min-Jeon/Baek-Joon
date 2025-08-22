import sys, heapq
I=sys.stdin.readline
k,n,r=int(I()),int(I()),int(I())
l=[[] for _ in range(n+1)]
for _ in range(r):
    a,b,c,d=map(int,I().split())
    l[a].append((b,c,d))
r=[[1e9]*(k+1) for _ in range(n+1)]
r[1][0]=0
q=[(0,0,1)]
while q:
    x,y,p=heapq.heappop(q)
    if(r[p][y]<x): continue
    for i,e,f in l[p]:
        if(y+f<=k and r[i][y+f]>x+e):
            r[i][y+f]=x+e
            heapq.heappush(q,(x+e,y+f,i))
t=set(r[n])
if(1e9 in t): t.remove(1e9)
if(len(t)==0): print(-1)
else: print(min(t))