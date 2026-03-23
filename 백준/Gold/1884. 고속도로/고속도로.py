import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
K,N,R=int(I()),int(I()),int(I())
l=[[] for _ in range(N+1)]
for _ in range(R):
    a,b,c,d=F()
    l[a].append((c,d,b))
r=[[1e99]*(K+1) for _ in range(N+1)]
r[1][0]=0
q=[(0,0,1)]
while q:
    d,t,p=heapq.heappop(q)
    if(r[p][t]<d): continue
    for a,b,c in l[p]:
        if(b+t<=K and r[c][b+t]>d+a):
            r[c][b+t]=d+a
            heapq.heappush(q,(d+a,b+t,c))
x=min(r[N])
print(x if x!=1e99 else -1)