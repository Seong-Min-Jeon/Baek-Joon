import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m=f()
c=f()
l=[[] for _ in range(n+1)]
l[0]=[(i+1,i+1) for i in range(n)]
for _ in range(m):
    a,x,y=f()
    l[x].append((y,a))
    l[y].append((x,a))
r=[1e99]*(n+1)
r[0]=0
for i,e in enumerate(c): r[i+1]=e
q=[(0,0)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,j in l[p]:
        if(r[j]>=d+r[i]):
            r[j]=d+r[i]
            heapq.heappush(q,(r[j],j))
print(r[1])