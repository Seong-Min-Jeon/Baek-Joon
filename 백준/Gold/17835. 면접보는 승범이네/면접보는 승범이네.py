import sys,heapq
I=sys.stdin.readline
n,m,k=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    v,u,c=map(int,I().split())
    l[u].append((v,c))
for e in map(int,I().split()): l[0].append((e,0))
r=[1e99]*(n+1)
q=[(0,0)]
r[0]=0
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,k in l[p]:
        if(d+k<r[i]):
            r[i]=d+k
            heapq.heappush(q,(d+k,i))
print(r.index(max(r)))
print(max(r))