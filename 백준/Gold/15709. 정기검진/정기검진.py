import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,b,k,q=F()
l=[[] for _ in range(n+m+b+1)]
for _ in range(k):
    x,y,z=F()
    l[x].append((y,z))
    l[y].append((x,z))
r=[[1e99]*(n+m+b+1) for _ in range(b)]
for k in range(b):
    j=n+m+k+1
    r[k][0]=0
    h=[(0,j)]
    while h:
        d,p=heapq.heappop(h)
        if(r[k][p]<d): continue
        for i,e in l[p]:
            if(r[k][i]>d+e):
                r[k][i]=d+e
                heapq.heappush(h,(d+e,i))
for _ in range(q):
    s,e=F()
    t=1e99
    for k in range(b):
        t=min(t,r[k][s]+r[k][e])
    print(t if t<1e99 else -1)