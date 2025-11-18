import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,k=F()
s,t=F()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=F()
    l[a].append((b,c))
r=[[1e99]*k for _ in range(n+1)]
r[s][0]=0
q=[(0,s,0)]
while q:
    d,p,z=heapq.heappop(q)
    if(r[p][z]<d): continue
    for i,e in l[p]:
        if(r[i][(z+e)%k]>d+e):
            r[i][(z+e)%k]=d+e
            heapq.heappush(q,(d+e,i,(z+e)%k))
if(r[t][0]==1e99): print('IMPOSSIBLE')
else: print(r[t][0])