import sys,heapq
I=sys.stdin.readline
n,m=map(int,I().split())
l=[[] for _ in range(n+1)]
for i in range(m):
    u,v,d=map(int,I().split())
    l[u].append((v,d,1,i))
    l[v].append((u,2*d,0,i))
r=[1e99]*(n+1)
r[0],r[1]=0,0
v=[1]*m
q=[(0,1)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e,x,j in l[p]:
        if(r[i]>d+e):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
            v[j]=x
print(sum(r))
print(*v)