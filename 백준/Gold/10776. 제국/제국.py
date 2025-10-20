import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
k,n,m=F()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c,d=F()
    l[a].append((b,c,d))
    l[b].append((a,c,d))
s,z=F()
r=[[1e99]*k for _ in range(n+1)]
r[s]=[0]*k
q=[(0,0,s)]
while q:
    d,b,p=heapq.heappop(q)
    if(r[p][b]<d): continue
    for i,e,f in l[p]:
        if(b+f<k and r[i][b+f]>d+e):
            r[i][b+f]=d+e
            heapq.heappush(q,(d+e,b+f,i))
t=min(r[z])
print(t if t!=1e99 else -1)