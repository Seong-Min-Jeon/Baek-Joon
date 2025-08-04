import sys,heapq
I=sys.stdin.readline
n,m,s,t=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,x=map(int,I().split())
    l[a].append((b,x))
    l[b].append((a,x))
r=[1e99]*(n+1)
q=[(0,s)]
r[s]=0
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(d+e<r[i]):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
print(r[t])