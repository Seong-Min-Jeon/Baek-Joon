import sys,heapq
I=sys.stdin.readline
v,e=map(int,I().split())
l=[[] for _ in range(v+1)]
for _ in range(e):
    x,y,t,k=map(int,I().split())
    l[x].append((y,t,k))
    l[y].append((x,t,k))
r=[1e99]*(v+1)
g=[1e99]*(v+1)
q=[(0,1,0)]
r[1]=0
while q:
    d,p,f=heapq.heappop(q)
    if(f==1 and g[p]<d): continue
    if(f==0 and r[p]<d): continue
    for i,t,k in l[p]:
        if(f==0 and d+t<r[i]):
            r[i]=d+t
            heapq.heappush(q,(d+t,i,0))
        if(f==1 and d+t<g[i]):
            g[i]=d+t
            heapq.heappush(q,(d+t,i,1))
        if(f==0 and d+t-k<g[i]):
            g[i]=d+t-k
            heapq.heappush(q,(d+t-k,i,1))
for i in range(2,v+1):
    print(g[i])