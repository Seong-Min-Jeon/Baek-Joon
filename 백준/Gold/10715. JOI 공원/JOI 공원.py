import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,c=F()
l=[[] for _ in range(n+1)]
k=0
for _ in range(m):
    a,b,d=F()
    l[a].append((b,d))
    l[b].append((a,d))
    k+=d
r=[1e99]*(n+1)
r[1]=0
m=1e99
t=set()
q=[(0,1)]
while q:
    d,p=heapq.heappop(q)
    if(p in t): continue
    else: t.add(p)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(i in t): k-=e
    m=min(m,c*d+k)
    for i,e in l[p]:
        if(r[i]>d+e):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
print(m)