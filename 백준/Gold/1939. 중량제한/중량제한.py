import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=F()
    l[a].append((b,-c))
    l[b].append((a,-c))
s,z=F()
r=[0]*(n+1)
r[s]=-1e99
q=[(-1e99,s)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(r[i]>max(d,e)):
            r[i]=max(d,e)
            heapq.heappush(q,(r[i],i))
print(-r[z])