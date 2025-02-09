import heapq
I=input
n,m=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,I().split())
    l[a].append((b,c)); l[b].append((a,c))
q=[(0,1)]
r=[1e9 for _ in range(n+1)]
r[1]=0
while q:
    c,p=heapq.heappop(q)
    if(r[p]<c): continue
    for i,e in l[p]:
        if(e+c<r[i]): r[i]=e+c; heapq.heappush(q,(e+c,i))
print(r[-1])